## script.rpy
## 游戏入口和主脚本 / Main Script Entry Point

################################################################################
## 闪屏 - 确保主菜单显示
################################################################################

label splashscreen:
    ## 这个 label 在游戏启动时运行，确保主菜单正常显示
    ## return 后 Ren'Py 会自动显示 main_menu 屏幕
    ##
    ## 启动无色透明多面体循环视频。channel 在 game/scripts/videos.rpy 注册。
    ## 一旦播放，channel 会一直跑下去 —— 主菜单和序章首场景的 Movie() displayable
    ## 都从这个 channel 取帧，所以从菜单切到游戏不会有重新播放的跳。
    $ renpy.music.play("images/bg/polyhedron.webm", channel="polyhedron_video", loop=True)
    return

################################################################################
## 游戏开始
################################################################################

label start:
    ## 初始化变量
    $ madness = 0
    $ choice_flags = {}

    ## 跳转到序章
    jump prologue
