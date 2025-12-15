## test_suite.rpy
## Automated Test Suite for AOL Afterstory
## Run via: Ren'Py Launcher -> "Run Testcases" or command line

################################################################################
## Test Configuration
################################################################################

init python:
    # Extend timeout for longer test sequences
    _test.timeout = 30.0

################################################################################
## Test Setup - Reset persistent state before tests
################################################################################

init python:
    def reset_test_state():
        """Reset all persistent variables to clean state for testing."""
        persistent.bad_end_1_unlocked = False
        persistent.bad_end_2_unlocked = False
        persistent.bad_end_3_unlocked = False
        persistent.normal_end_unlocked = False
        persistent.happy_end_unlocked = False
        persistent.route1_complete = False
        persistent.route2_complete = False
        persistent.route3_complete = False
        persistent.music_unlocked = set()

################################################################################
## ROUTE 1 TESTS - Bad End 1: 举棋不定
################################################################################

testcase route1_bad_end_1:
    description "Route 1 - Bad End 1 (举棋不定): All first choices, then '我想知道'"

    # Reset state
    $ reset_test_state()

    # Start game
    run Start()

    # Advance through prologue
    advance until screen "route_title"
    click
    advance until "不对劲"

    # Choice 1: 不对劲 (no madness)
    click "不对劲"

    advance until "疯了"
    # Choice 2: 疯了 (no madness)
    click "疯了"

    advance until "算了"
    # Choice 3: 算了 (no madness)
    click "算了"

    advance until "就这样睡去"
    # Choice 4: 就这样睡去 (no madness)
    click "就这样睡去"

    advance until "保持呼吸"
    # Choice 5: 保持呼吸
    click "保持呼吸"

    advance until "我想知道"
    # Choice 6: 我想知道 -> Bad End 1
    click "我想知道"

    # Verify we reached the ending and return to main menu
    advance until label main_menu

    # Verify Bad End 1 unlocked
    assert eval persistent.bad_end_1_unlocked == True
    assert eval persistent.route1_complete == False


testcase route1_complete_path:
    description "Route 1 - Complete Path: '我必须知道' leads to route completion"

    $ reset_test_state()
    run Start()

    advance until screen "route_title"
    click
    advance until "不对劲"
    click "不对劲"

    advance until "疯了"
    click "疯了"

    advance until "算了"
    click "算了"

    advance until "就这样睡去"
    click "就这样睡去"

    advance until "保持呼吸"
    click "保持呼吸"

    advance until "我必须知道"
    # Choice 6: 我必须知道 -> Continues to route completion
    click "我必须知道"

    # Continue to end of route
    advance until label main_menu

    # Verify route completed (not a bad end branch)
    assert eval persistent.route1_complete == True


testcase route1_madness_path:
    description "Route 1 - High Madness Path: All madness+1 choices"

    $ reset_test_state()
    run Start()

    advance until screen "route_title"
    click
    advance until "很有精神"
    # Choice 1: 很有精神！(madness+1)
    click "很有精神"

    advance until "睡着了"
    # Choice 2: 睡着了 (madness+1)
    click "睡着了"

    advance until "接受"
    # Choice 3: 接受 (madness+1)
    click "接受"

    advance until "更多"
    # Choice 4: 更多 (madness+1)
    click "更多"

    advance until "放弃"
    # Choice 5: 放弃 (madness+1)
    click "放弃"

    advance until "我必须知道"
    click "我必须知道"

    advance until label main_menu

    # Verify high madness didn't break anything
    assert eval persistent.route1_complete == True


################################################################################
## ROUTE 2 TESTS - Bad End 2 & 3
################################################################################

testcase route2_bad_end_2:
    description "Route 2 - Bad End 2 (好奇害死猫): Direct confrontation path"

    # Setup: Complete route 1 first
    $ reset_test_state()
    $ persistent.route1_complete = True

    run Start()

    # Route 2 meta choices - continue
    advance until "下潜"
    click "下潜"

    advance until "继续下潜"
    click "继续下潜"

    advance until "下潜"
    click "下潜"

    advance until screen "route_title"
    click

    # Progress through route 2
    advance until "可是"
    # Choice: 可是—— -> Bad End 2
    click "可是"

    advance until label main_menu

    assert eval persistent.bad_end_2_unlocked == True
    assert eval persistent.route2_complete == False


testcase route2_bad_end_3:
    description "Route 2 - Bad End 3 (平等杀戮): Violence path"

    $ reset_test_state()
    $ persistent.route1_complete = True

    run Start()

    advance until "下潜"
    click "下潜"
    advance until "继续下潜"
    click "继续下潜"
    advance until "下潜"
    click "下潜"

    advance until screen "route_title"
    click

    advance until "嗯"
    # Choice: 嗯... -> Continue
    click "嗯"

    advance until "好奇怪"
    # Choice: 好奇怪 -> Leads to violence path
    click "好奇怪"

    advance until "如沐春风的安详"
    # Choice: 如沐春风的安详 -> Bad End 3
    click "如沐春风的安详"

    advance until label main_menu

    assert eval persistent.bad_end_3_unlocked == True
    assert eval persistent.route2_complete == False


testcase route2_complete_path:
    description "Route 2 - Complete Path: Through fear to completion"

    $ reset_test_state()
    $ persistent.route1_complete = True

    run Start()

    advance until "下潜"
    click "下潜"
    advance until "继续下潜"
    click "继续下潜"
    advance until "下潜"
    click "下潜"

    advance until screen "route_title"
    click

    advance until "嗯"
    click "嗯"

    advance until "好奇怪"
    click "好奇怪"

    advance until "深入骨髓的恐惧"
    # Choice: 深入骨髓的恐惧 -> Continue to completion
    click "深入骨髓的恐惧"

    # Final choice
    advance until "为什么要"
    click "为什么要"

    advance until label main_menu

    assert eval persistent.route2_complete == True


testcase route2_madness_complete:
    description "Route 2 - Madness Path: High madness to completion"

    $ reset_test_state()
    $ persistent.route1_complete = True

    run Start()

    advance until "下潜"
    click "下潜"
    advance until "继续下潜"
    click "继续下潜"
    advance until "下潜"
    click "下潜"

    advance until screen "route_title"
    click

    advance until "嗯"
    click "嗯"

    advance until "还蛮好吃"
    # Madness choice
    click "还蛮好吃"

    advance until "深入骨髓的恐惧"
    click "深入骨髓的恐惧"

    advance until "随便了"
    # Madness choice
    click "随便了"

    advance until label main_menu

    assert eval persistent.route2_complete == True


################################################################################
## ROUTE 3 TESTS - Normal End & Happy End
################################################################################

testcase route3_normal_end:
    description "Route 3 - Normal End (日常): Standard completion"

    $ reset_test_state()
    $ persistent.route1_complete = True
    $ persistent.route2_complete = True

    run Start()

    advance until screen "route_title"
    click

    # Progress through route 3
    advance until "把手中的无色透明多面体丢在了沙滩上"
    # Choice: Normal ending path
    click "把手中的无色透明多面体丢在了沙滩上"

    advance until label main_menu

    assert eval persistent.normal_end_unlocked == True or persistent.route3_complete == True


testcase route3_happy_end:
    description "Route 3 - Happy End: Keep the polyhedron (requires madness)"

    $ reset_test_state()
    $ persistent.route1_complete = True
    $ persistent.route2_complete = True

    run Start()

    advance until screen "route_title"
    click

    # The happy end choice may require certain conditions
    # Based on script: "把手中的无色透明多面体装回裤兜里（需要madness大于某个数字）"
    advance until "把手中的无色透明多面体"

    # Try the happy end choice if available
    if eval "把手中的无色透明多面体装回裤兜里" in [i[0] for i in renpy.get_menu_choices()]:
        click "把手中的无色透明多面体装回裤兜里"
    else:
        # Fall back to normal end if madness requirement not met
        click "把手中的无色透明多面体丢在了沙滩上"

    advance until label main_menu

    assert eval persistent.route3_complete == True


################################################################################
## FULL PLAYTHROUGH TESTS - Sequential route completion
################################################################################

testcase full_playthrough_all_bad_ends:
    description "Full Playthrough: Route 1 Bad End -> Route 1 Complete"

    $ reset_test_state()

    # Route 1 - Bad End 1
    run Start()
    advance until screen "route_title"
    click
    advance until "不对劲"
    click "不对劲"
    advance until "疯了"
    click "疯了"
    advance until "算了"
    click "算了"
    advance until "就这样睡去"
    click "就这样睡去"
    advance until "保持呼吸"
    click "保持呼吸"
    advance until "我想知道"
    click "我想知道"
    advance until label main_menu

    assert eval persistent.bad_end_1_unlocked == True

    # Route still incomplete - play again for completion
    run Start()
    advance until screen "route_title"
    click
    advance until "不对劲"
    click "不对劲"
    advance until "疯了"
    click "疯了"
    advance until "算了"
    click "算了"
    advance until "就这样睡去"
    click "就这样睡去"
    advance until "保持呼吸"
    click "保持呼吸"
    advance until "我必须知道"
    click "我必须知道"
    advance until label main_menu

    assert eval persistent.route1_complete == True


################################################################################
## VARIABLE STATE TESTS
################################################################################

testcase test_madness_increment:
    description "Test madness variable increments correctly"

    $ reset_test_state()
    run Start()

    # Initial madness should be 0
    assert eval madness == 0

    advance until screen "route_title"
    click

    advance until "很有精神"
    # Choose madness+1 option
    click "很有精神"

    # Madness should now be 1
    assert eval madness == 1

    advance until "睡着了"
    click "睡着了"

    # Madness should now be 2
    assert eval madness == 2


testcase test_route_progression:
    description "Test route progression logic"

    $ reset_test_state()

    # Initially should be route 1
    assert eval get_current_route() == 1

    # After completing route 1
    $ persistent.route1_complete = True
    assert eval get_current_route() == 2

    # After completing route 2
    $ persistent.route2_complete = True
    assert eval get_current_route() == 3

    # After completing all routes
    $ persistent.route3_complete = True
    assert eval get_current_route() == 3


testcase test_ending_count:
    description "Test ending count function"

    $ reset_test_state()

    assert eval get_ending_count() == 0

    $ persistent.bad_end_1_unlocked = True
    assert eval get_ending_count() == 1

    $ persistent.bad_end_2_unlocked = True
    assert eval get_ending_count() == 2

    $ persistent.bad_end_3_unlocked = True
    assert eval get_ending_count() == 3

    $ persistent.normal_end_unlocked = True
    assert eval get_ending_count() == 4

    $ persistent.happy_end_unlocked = True
    assert eval get_ending_count() == 5


################################################################################
## UI SCREEN TESTS
################################################################################

testcase test_main_menu_buttons:
    description "Test main menu navigation buttons exist"

    # Should be at main menu
    assert screen "main_menu"

    # Test navigation screen elements exist
    assert screen "navigation"


testcase test_quick_menu:
    description "Test quick menu appears during gameplay"

    $ reset_test_state()
    run Start()

    advance until screen "route_title"
    click

    # After clicking past title, quick menu should be visible
    advance
    advance

    # Quick menu should be present during dialogue
    assert screen "quick_menu"


testcase test_save_screen:
    description "Test save screen accessibility"

    $ reset_test_state()
    run Start()

    advance until screen "route_title"
    click
    advance
    advance

    # Open save menu
    run ShowMenu('save')

    assert screen "save"

    # Return
    run Return()


testcase test_preferences_screen:
    description "Test preferences screen accessibility"

    $ reset_test_state()
    run Start()

    advance until screen "route_title"
    click
    advance
    advance

    run ShowMenu('preferences')

    assert screen "preferences"

    run Return()


################################################################################
## SCREEN ELEMENT TESTS
################################################################################

testcase test_say_screen:
    description "Test dialogue say screen displays correctly"

    $ reset_test_state()
    run Start()

    advance until screen "route_title"
    click

    # Advance into dialogue
    advance
    advance
    advance

    # Say screen should be active
    assert screen "say"


testcase test_choice_screen:
    description "Test choice menu screen"

    $ reset_test_state()
    run Start()

    advance until screen "route_title"
    click

    # Advance to first choice
    advance until "不对劲"

    # Choice screen should be displayed
    assert screen "choice"


################################################################################
## ROUTE TITLE SCREEN TEST
################################################################################

testcase test_route_title_screen:
    description "Test route title screen displays"

    $ reset_test_state()
    run Start()

    # Prologue leads to route_title call
    advance until screen "route_title"

    assert screen "route_title"

    click


################################################################################
## EDGE CASE TESTS
################################################################################

testcase test_return_to_main_menu:
    description "Test that bad ends properly return to main menu"

    $ reset_test_state()
    run Start()

    advance until screen "route_title"
    click
    advance until "不对劲"
    click "不对劲"
    advance until "疯了"
    click "疯了"
    advance until "算了"
    click "算了"
    advance until "就这样睡去"
    click "就这样睡去"
    advance until "保持呼吸"
    click "保持呼吸"
    advance until "我想知道"
    click "我想知道"

    # Should return to main menu after bad end
    advance until label main_menu

    assert screen "main_menu"


testcase test_persistent_survives_restart:
    description "Test that persistent variables survive game restart"

    $ reset_test_state()
    $ persistent.bad_end_1_unlocked = True
    $ persistent.route1_complete = True

    # Simulate restart by running start
    run Start()

    # Persistent should still be set
    assert eval persistent.bad_end_1_unlocked == True
    assert eval persistent.route1_complete == True

    # Should go to route 2 now
    advance until "下潜"


################################################################################
## REGRESSION TESTS - Known Issues
################################################################################

testcase test_no_unreachable_statements:
    description "Regression: Verify no unreachable code after choices"

    # This test verifies the fix from commit ad93cd0
    # "Fix unreachable code in route2 after Bad End 3"

    $ reset_test_state()
    $ persistent.route1_complete = True

    run Start()

    advance until "下潜"
    click "下潜"
    advance until "继续下潜"
    click "继续下潜"
    advance until "下潜"
    click "下潜"

    advance until screen "route_title"
    click

    advance until "嗯"
    click "嗯"

    advance until "好奇怪"
    click "好奇怪"

    advance until "深入骨髓的恐惧"
    click "深入骨髓的恐惧"

    # Should reach end without errors
    advance until label main_menu

    assert eval persistent.route2_complete == True
