# -*- coding: utf-8 -*-
"""
Google Docs Sync Script
Syncs main_script_raw.txt with a Google Doc

Usage:
    python sync_gdocs.py pull   # Download from Google Docs to local
    python sync_gdocs.py push   # Upload local to Google Docs
    python sync_gdocs.py        # Interactive mode
"""

import os
import sys

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Configuration
SCOPES = ['https://www.googleapis.com/auth/documents']
DOCUMENT_ID = '1zwxsyE2W0buSmJcK_pYYGkjbZTNUcqBkBpAw2DOnd7w'
LOCAL_FILE = r'X:\GameDev\AOL_afterstory\main_script_raw.txt'
CREDENTIALS_FILE = r'X:\GameDev\AOL_afterstory\client_secret_584057721624-0m919ufs37dl7m4vdvcq5b22r83tf6vj.apps.googleusercontent.com.json'
TOKEN_FILE = r'X:\GameDev\AOL_afterstory\token.json'


def get_credentials():
    """Get or refresh OAuth credentials."""
    creds = None

    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)

        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())

    return creds


def get_doc_text(service):
    """Extract plain text from Google Doc."""
    doc = service.documents().get(documentId=DOCUMENT_ID).execute()

    text_content = []
    for element in doc.get('body', {}).get('content', []):
        if 'paragraph' in element:
            for para_element in element['paragraph'].get('elements', []):
                if 'textRun' in para_element:
                    text_content.append(para_element['textRun'].get('content', ''))

    return ''.join(text_content)


def clear_doc(service):
    """Clear all content from Google Doc."""
    doc = service.documents().get(documentId=DOCUMENT_ID).execute()

    # Find the end index of the document
    end_index = 1
    for element in doc.get('body', {}).get('content', []):
        if 'endIndex' in element:
            end_index = max(end_index, element['endIndex'])

    if end_index > 2:
        requests = [{
            'deleteContentRange': {
                'range': {
                    'startIndex': 1,
                    'endIndex': end_index - 1
                }
            }
        }]
        service.documents().batchUpdate(documentId=DOCUMENT_ID, body={'requests': requests}).execute()


def push_to_doc(service, text):
    """Push text content to Google Doc (replaces all content)."""
    clear_doc(service)

    if text:
        requests = [{
            'insertText': {
                'location': {'index': 1},
                'text': text
            }
        }]
        service.documents().batchUpdate(documentId=DOCUMENT_ID, body={'requests': requests}).execute()


def pull():
    """Download content from Google Docs to local file."""
    print("Pulling from Google Docs...")

    creds = get_credentials()
    service = build('docs', 'v1', credentials=creds)

    text = get_doc_text(service)

    with open(LOCAL_FILE, 'w', encoding='utf-8') as f:
        f.write(text)

    print(f"Downloaded {len(text)} characters to {LOCAL_FILE}")


def push():
    """Upload local file to Google Docs."""
    print("Pushing to Google Docs...")

    with open(LOCAL_FILE, 'r', encoding='utf-8') as f:
        text = f.read()

    creds = get_credentials()
    service = build('docs', 'v1', credentials=creds)

    push_to_doc(service, text)

    print(f"Uploaded {len(text)} characters to Google Docs")


def main():
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        if command == 'pull':
            pull()
        elif command == 'push':
            push()
        else:
            print(f"Unknown command: {command}")
            print("Usage: python sync_gdocs.py [pull|push]")
    else:
        print("Google Docs Sync")
        print("================")
        print("1. Pull (download from Google Docs)")
        print("2. Push (upload to Google Docs)")
        print()
        choice = input("Choose (1/2): ").strip()

        if choice == '1':
            pull()
        elif choice == '2':
            push()
        else:
            print("Invalid choice")


if __name__ == '__main__':
    main()
