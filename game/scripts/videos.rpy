## videos.rpy
## 视频播放通道与共享 Movie 资源。
##
## 为什么不直接用 Movie(play=...)：每次 displayable 被 mount / unmount 都会从头重播，
## 主菜单到序章的过渡会重置帧位置。把视频挂到独立的 audio/movie channel 上，
## 多个 Movie() displayable 都从同一个 channel 取帧，主菜单切到序章时帧位置不变。

init python:
    ## 无色透明多面体循环用的独立 channel。movie=True 是必须的，否则不能给 Movie() 取帧。
    ## mixer="music" 让它跟 BGM 共用音量条；clip 本身没有音轨，所以这只影响"如果以后换有声片"。
    ## loop=True 让 channel 自动循环播放。
    renpy.music.register_channel(
        "polyhedron_video",
        mixer="music",
        loop=True,
        stop_on_mute=False,
        movie=True,
    )
