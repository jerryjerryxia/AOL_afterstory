# AOL Afterstory - Ren'Py Visual Novel

## Quick Reference

**Build scripts:** `python convert_script.py` - Converts `main_script_raw.txt` → route `.rpy` files

**Main files:**
- `main_script_raw.txt` - Source of truth for story content
- `convert_script.py` - Script converter
- `game/screens.rpy` - All UI screens
- `game/scripts/variables.rpy` - Game variables and helper functions

## Raw Script Format

```
王霜：Character dialogue
阿鹤：Another character
Plain text is narration
【Stage direction → becomes comment】
A: Choice A text
B: Choice B text（madness+1）
【选项分线到此结束】
【展示一周目分屏"Title"】
【Bad End 1：Ending name】
```

**Characters in converter:** `王霜`→`wangshuang`, `阿鹤`→`ahe`, `尸首`→`shishou`

## Key Implementation Details

1. **Choices keep dialogue visible** using `extend ""` in menu blocks

2. **Delete saves** uses `renpy.list_slots()` + `renpy.unlink_save()` (not file operations)

3. **Route progression:** `get_current_route()` in variables.rpy determines which route to play

4. **Variables:**
   - `default X` = resets each playthrough
   - `default persistent.X` = survives across saves
   - `define X` = constant

5. **Init order:** gui.rpy (-2) → screens.rpy (-1) → others (0)

## Adding Content

**New character:**
1. Add `define newchar = Character("名字", color="#hex")` in characters.rpy
2. Add to char_var dict in convert_script.py
3. Run converter

**New ending:**
1. Add `default persistent.new_end_unlocked = False` in variables.rpy
2. Add case to `unlock_ending()` function
3. Use `【Bad End N：name】` in raw script
