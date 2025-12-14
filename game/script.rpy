## script.rpy
## 游戏入口和主脚本 / Main Script Entry Point

################################################################################
## 闪屏 - 确保主菜单显示
################################################################################

label splashscreen:
    ## 这个 label 在游戏启动时运行，确保主菜单正常显示
    ## return 后 Ren'Py 会自动显示 main_menu 屏幕
    return

################################################################################
## 游戏开始
################################################################################

label start:
    ## 初始化
    $ current_route = None

    ## 播放背景音乐（占位）
    # play music "audio/bgm/main_theme.ogg" fadein 1.0
    # $ unlock_music("main_theme")

    ## 显示背景
    scene bg_placeholder with fade

    ## 测试对话
    "这是一段测试对话。"
    "点击鼠标左键或按空格键继续。"

    ## 显示角色
    show placeholder_a_sprite at center_pos with dissolve

    placeholder_a "你好，这是角色A的测试对话。"
    placeholder_a "这个对话框显示了角色名称和对话内容。"

    hide placeholder_a_sprite with dissolve

    ## 测试选择支
    menu:
        "这是一个测试选项。请选择："

        "选项一 - 通往结局A":
            $ choice_flags["key_choice_1"] = "option_a"
            jump test_route_a

        "选项二 - 通往结局B":
            $ choice_flags["key_choice_1"] = "option_b"
            jump test_route_b

################################################################################
## 测试路线 A
################################################################################

label test_route_a:
    scene bg_placeholder_alt with fade

    "你选择了选项一。"
    "这条路线将通往结局A。"

    show placeholder_b_sprite at center_pos with dissolve

    placeholder_b "欢迎来到路线A。"

    hide placeholder_b_sprite with dissolve

    jump test_ending_a

################################################################################
## 测试路线 B
################################################################################

label test_route_b:
    scene bg_placeholder_alt with fade

    "你选择了选项二。"
    "这条路线将通往结局B。"

    show placeholder_c_sprite at center_pos with dissolve

    placeholder_c "欢迎来到路线B。"

    hide placeholder_c_sprite with dissolve

    jump test_ending_b

################################################################################
## 结局
################################################################################

label test_ending_a:
    scene black with fade

    "【结局A】"
    "这是测试结局A。"

    $ unlock_ending("a")

    "感谢游玩测试版本。"

    return

label test_ending_b:
    scene black with fade

    "【结局B】"
    "这是测试结局B。"

    $ unlock_ending("b")

    "感谢游玩测试版本。"

    return
