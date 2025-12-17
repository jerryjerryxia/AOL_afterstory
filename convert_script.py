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

def convert_content_line(line, indent="    ", use_large_textbox=False):
    """Convert a single content line to Ren'Py format"""
    line = line.strip()

    if not line:
        return None

    # Skip convergence marker (handled separately)
    if '选项分线到此结束' in line:
        return None

    # Skip large textbox markers (handled in convert_route)
    if '大文本框开始' in line or '大文本框结束' in line:
        return None

    # Route transition screens 【展示X周目分屏"标题"】
    if '展示' in line and '周目分屏' in line:
        # Extract title between quotes using flexible matching
        import re as re2
        title_match = re2.search(r'分屏.(.+?).】$', line)
        if title_match:
            title = title_match.group(1)
            return f'{indent}call screen route_title("{title}")'

    # Music trigger markers 【音乐：scene_id】
    music_match = re.match(r'^【音乐[：:](.+?)】$', line)
    if music_match:
        scene_id = music_match.group(1).strip()
        return f'{indent}$ set_scene_music("{scene_id}")'

    # Bad End markers - unlock ending and return to main menu (MUST be before general stage direction check)
    bad_end_match = re.match(r'^【(Bad End \d+[：:].*)】$', line)
    if bad_end_match:
        end_text = bad_end_match.group(1)
        # Extract the bad end number
        num_match = re.search(r'Bad End (\d+)', end_text)
        end_num = num_match.group(1) if num_match else "1"
        return f"{indent}## {end_text}\n{indent}$ unlock_ending(\"bad_end_{end_num}\")\n{indent}return"

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

    # Narrative text - choose narrator based on mode
    if use_large_textbox:
        return f'{indent}large_narrator {format_dialogue(line)}'
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


def collect_accumulating_block(lines, start_i, end_line, marker_end, use_large=False):
    """
    Collect lines between markers and output them with extend for accumulating display.
    First line is normal dialogue, subsequent lines use extend to append.
    Returns (output_lines, new_index)
    """
    collected = []
    i = start_i

    while i < end_line and i < len(lines):
        line = lines[i].strip()
        i += 1

        if not line:
            continue

        # Check for end marker
        if marker_end in line:
            break

        # Character dialogue
        char_match = re.match(r'^(王霜|阿鹤|尸首)[：:](.*)$', line)
        if char_match:
            char_name = char_match.group(1)
            dialogue = char_match.group(2).strip()
            char_var = {'王霜': 'wangshuang', '阿鹤': 'ahe', '尸首': 'shishou'}[char_name]
            collected.append((char_var, dialogue))
        else:
            # Stage directions - skip
            if line.startswith('【') and line.endswith('】'):
                continue
            # Narration
            collected.append((None, line))

    if not collected:
        return [], i

    output = []
    indent = "    "

    # First line: normal dialogue
    first_speaker, first_text = collected[0]
    if use_large:
        output.append(f'{indent}large_narrator {format_dialogue(first_text)}')
    elif first_speaker:
        output.append(f'{indent}{first_speaker} {format_dialogue(first_text)}')
    else:
        output.append(f'{indent}{format_dialogue(first_text)}')

    # Subsequent lines: use extend to append with newline
    for speaker, text in collected[1:]:
        # extend appends to previous text
        output.append(f'{indent}extend {format_dialogue(chr(92) + "n" + text)}')

    return output, i


def convert_route(lines, start_line, end_line, label_name, route_num):
    """Convert a route section with proper branching"""
    output = []
    output.append(f"## route{route_num}.rpy")
    output.append(f"## Route {route_num}")
    output.append("")
    output.append(f"label {label_name}:")

    i = start_line
    choice_counter = 0
    last_dialogue = None  # Track the last dialogue line for menu caption
    use_large_textbox = False  # Track large textbox mode

    while i < end_line and i < len(lines):
        line = lines[i].strip()
        i += 1

        if not line:
            continue

        # Check for accumulating block markers (【Extended文本框开始】 or 【Extended大文本框开始】)
        # These use extend to accumulate text with each click
        if 'Extended大文本框开始' in line:
            output.append("    ## Extended大文本框开始 - accumulating large textbox")
            accumulated, i = collect_accumulating_block(lines, i, end_line, 'Extended大文本框结束', use_large=True)
            output.extend(accumulated)
            output.append("    ## Extended大文本框结束")
            continue

        if 'Extended文本框开始' in line and 'Extended大文本框' not in line:
            output.append("    ## Extended文本框开始 - accumulating textbox")
            accumulated, i = collect_accumulating_block(lines, i, end_line, 'Extended文本框结束', use_large=False)
            output.extend(accumulated)
            output.append("    ## Extended文本框结束")
            continue

        # Check for large textbox markers (non-combined, single line mode)
        if '大文本框开始' in line and 'Extended' not in line:
            use_large_textbox = True
            output.append("    ## 大文本框开始")
            continue
        if '大文本框结束' in line and 'Extended' not in line:
            use_large_textbox = False
            output.append("    ## 大文本框结束")
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
            # Keep the dialogue line before menu, use "extend" to keep textbox visible
            output.append("")
            output.append("    menu:")
            output.append('        extend ""')
            last_dialogue = None

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
        converted = convert_content_line(line, use_large_textbox=use_large_textbox)
        if converted:
            output.append(converted)
            # Track dialogue lines (character dialogue or narration) for menu captions
            # These are lines that display in the textbox
            stripped = converted.strip()
            if not stripped.startswith('##') and not stripped.startswith('$') and not stripped.startswith('call '):
                last_dialogue = stripped

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

    # Route 1: lines 45-716 (0-indexed: 44-715) - ends at 【一周目End】
    route1 = convert_route(lines, 44, 716, "route1_start", 1)
    with open(r'X:\GameDev\AOL_afterstory\game\scripts\route1.rpy', 'w', encoding='utf-8') as f:
        f.write(route1)
    print("Route 1 converted!")

    # Route 2: lines 717-1339 (0-indexed: 716-1338) - starts at 二周目
    route2 = convert_route(lines, 716, 1339, "route2_start", 2)
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
