# -*- coding: utf-8 -*-
"""
Script converter: Converts raw script to Ren'Py format
Handles branching with A:/B: options and 【选项分线到此结束】 convergence markers
"""

import re

def escape_quotes(text):
    """Escape straight double quotes for Ren'Py"""
    return text.replace('"', '\\"')

def has_curly_quotes(text):
    """Check if text contains curly double quotes"""
    return '"' in text or '"' in text

def format_dialogue(text):
    """Format dialogue string, using single quotes if curly quotes present"""
    if has_curly_quotes(text):
        # Use single quotes as delimiter, escape any single quotes in text
        escaped = text.replace("'", "\\'")
        return f"'{escaped}'"
    else:
        # Use double quotes as delimiter, escape any double quotes in text
        escaped = text.replace('"', '\\"')
        return f'"{escaped}"'

def convert_content_line(line, indent="    "):
    """Convert a single content line to Ren'Py format"""
    line = line.strip()

    if not line:
        return None

    # Skip convergence marker (handled separately)
    if '选项分线到此结束' in line:
        return None

    # Route transition screens 【展示X周目分屏"标题"】
    if '展示' in line and '周目分屏' in line:
        # Extract title between quotes using flexible matching
        import re as re2
        title_match = re2.search(r'分屏.(.+?).】$', line)
        if title_match:
            title = title_match.group(1)
            return f'{indent}call screen route_title("{title}")'

    # Stage direction (standalone) -> comment
    stage_match = re.match(r'^【(.+?)】$', line)
    if stage_match:
        return f"{indent}## {stage_match.group(1)}"

    # Character dialogue with inline stage direction
    char_action_match = re.match(r'^(王霜|阿鹤|尸首)【(.+?)】[：:](.*)$', line)
    if char_action_match:
        char_name = char_action_match.group(1)
        action = char_action_match.group(2)
        dialogue = char_action_match.group(3).strip()
        char_var = {'王霜': 'wangshuang', '阿鹤': 'ahe', '尸首': 'shishou'}[char_name]
        return f'{indent}## {action}\n{indent}{char_var} {format_dialogue(dialogue)}'

    # Character dialogue (simple)
    char_match = re.match(r'^(王霜|阿鹤|尸首)[：:](.*)$', line)
    if char_match:
        char_name = char_match.group(1)
        dialogue = char_match.group(2).strip()
        char_var = {'王霜': 'wangshuang', '阿鹤': 'ahe', '尸首': 'shishou'}[char_name]
        return f'{indent}{char_var} {format_dialogue(dialogue)}'

    # Section headers
    if re.match(r'^[一二三四五六七八九十]+周目', line):
        return f"\n## {line}\n"

    # End markers
    end_match = re.match(r'^【(.*(End|结局).*)】$', line)
    if end_match:
        return f"{indent}## {end_match.group(1)}"

    # Narrative text
    return f'{indent}{format_dialogue(line)}'


def is_choice_a(line):
    return bool(re.match(r'^A[：:]\s*.+$', line.strip()))

def is_choice_b(line):
    return bool(re.match(r'^B[：:]\s*.+$', line.strip()))

def is_convergence(line):
    return '选项分线到此结束' in line

def parse_choice(line):
    """Parse choice line, returns (text, madness_add)"""
    match = re.match(r'^[AB][：:]\s*(.+)$', line.strip())
    if match:
        text = match.group(1).strip()
        madness_match = re.search(r'[（(]madness\s*\+\s*(\d+)[）)]', text)
        madness_add = 0
        if madness_match:
            madness_add = int(madness_match.group(1))
            text = re.sub(r'[（(]madness\s*\+\s*\d+[）)]', '', text).strip()
        return text, madness_add
    return None, 0


def convert_route(lines, start_line, end_line, label_name, route_num):
    """Convert a route section with proper branching"""
    output = []
    output.append(f"## route{route_num}.rpy")
    output.append(f"## Route {route_num}")
    output.append("")
    output.append(f"label {label_name}:")

    i = start_line
    choice_counter = 0

    while i < end_line and i < len(lines):
        line = lines[i].strip()
        i += 1

        if not line:
            continue

        # Check for choice A - starts a branching block
        if is_choice_a(line):
            choice_counter += 1
            choice_a_text, choice_a_madness = parse_choice(line)

            # Collect content for choice A until we hit B:
            choice_a_content = []
            while i < end_line and i < len(lines):
                next_line = lines[i].strip()
                if is_choice_b(next_line):
                    break
                if next_line:  # Skip empty lines
                    choice_a_content.append(next_line)
                i += 1

            # Now at B: line
            choice_b_text = None
            choice_b_madness = 0
            choice_b_content = []

            if i < end_line and is_choice_b(lines[i].strip()):
                choice_b_text, choice_b_madness = parse_choice(lines[i].strip())
                i += 1

                # Collect content for choice B until convergence or next choice
                while i < end_line and i < len(lines):
                    next_line = lines[i].strip()
                    if is_convergence(next_line):
                        i += 1  # Skip the convergence marker
                        break
                    if is_choice_a(next_line):
                        # Another choice block without convergence - B leads to ending?
                        break
                    if next_line:
                        choice_b_content.append(next_line)
                    i += 1

            # Generate menu structure
            output.append("")
            output.append("    menu:")

            # Choice A
            output.append(f'        "{choice_a_text}":')
            if choice_a_madness > 0:
                output.append(f"            $ madness += {choice_a_madness}")
            if choice_a_content:
                for content_line in choice_a_content:
                    converted = convert_content_line(content_line, "            ")
                    if converted:
                        output.append(converted)
            else:
                output.append("            pass")

            # Choice B
            if choice_b_text:
                output.append(f'        "{choice_b_text}":')
                if choice_b_madness > 0:
                    output.append(f"            $ madness += {choice_b_madness}")
                if choice_b_content:
                    for content_line in choice_b_content:
                        converted = convert_content_line(content_line, "            ")
                        if converted:
                            output.append(converted)
                else:
                    output.append("            pass")

            output.append("")
            continue

        # Regular content line (not part of choice)
        converted = convert_content_line(line)
        if converted:
            output.append(converted)

    # End of route
    output.append("")
    output.append(f"    ## Route {route_num} 结束")
    output.append(f"    $ unlock_route({route_num})")
    output.append("    return")

    return '\n'.join(output)


def main():
    with open(r'X:\GameDev\AOL_afterstory\main_script_raw.txt', 'r', encoding='utf-8') as f:
        lines = [line.rstrip('\n') for line in f.readlines()]

    print(f"Total lines: {len(lines)}")

    # Route 1: lines 45-643 (0-indexed: 44-642)
    route1 = convert_route(lines, 44, 643, "route1_start", 1)
    with open(r'X:\GameDev\AOL_afterstory\game\scripts\route1.rpy', 'w', encoding='utf-8') as f:
        f.write(route1)
    print("Route 1 converted!")

    # Route 2: lines 644-1339 (0-indexed: 643-1338)
    route2 = convert_route(lines, 643, 1339, "route2_start", 2)
    with open(r'X:\GameDev\AOL_afterstory\game\scripts\route2.rpy', 'w', encoding='utf-8') as f:
        f.write(route2)
    print("Route 2 converted!")

    # Route 3: lines 1340-end (0-indexed: 1339-end)
    route3 = convert_route(lines, 1339, len(lines), "route3_start", 3)
    with open(r'X:\GameDev\AOL_afterstory\game\scripts\route3.rpy', 'w', encoding='utf-8') as f:
        f.write(route3)
    print("Route 3 converted!")

    print("All routes converted successfully!")


if __name__ == "__main__":
    main()
