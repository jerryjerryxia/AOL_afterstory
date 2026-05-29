## placeholder.rpy
## 占位符背景定义 / Placeholder Background Definitions

## 主背景占位符 - 深灰色
image bg_placeholder = Solid("#2a2a2a", xsize=1920, ysize=1080)

## 备用背景占位符 - 深蓝色
image bg_placeholder_alt = Solid("#1a2a3a", xsize=1920, ysize=1080)

## 黑屏
image black = Solid("#000000", xsize=1920, ysize=1080)

## 白屏
image white = Solid("#ffffff", xsize=1920, ysize=1080)

## 更多占位背景 - 按需添加
image bg_room = Solid("#3a3a3a", xsize=1920, ysize=1080)
image bg_outdoor = Solid("#2a3a2a", xsize=1920, ysize=1080)
image bg_night = Solid("#1a1a2a", xsize=1920, ysize=1080)

################################################################################
## 正式背景图 / Real background images
##
## 源图为 4K (3840x2160)，游戏虚拟分辨率为 1920x1080。
## 用 Transform 把图缩放到虚拟分辨率；全屏运行在 4K 显示器上时，
## Ren'Py 会以显示器原生分辨率渲染，因此这些背景会以完整 4K 细节显示。
## convert_script.py 中的 SCENE_BG_MAP 把 【转场：场景名】 映射到这些 image 名。
################################################################################

## 无色透明多面体：WebM (VP9) 循环视频。
## 关键：不写 play=，而是从 channel 取帧。channel 在 game/scripts/videos.rpy 注册，
## 在 splashscreen 启动后一直跑。所有引用 bg_polyhedron_video 的地方（主菜单、序章首场景、
## 以及剧本中其它所有 无色透明多面体 场景）都从同一个 channel 取当前帧。
image bg_polyhedron_video = Movie(
    channel="polyhedron_video",
    size=(1920, 1080)
)

image bg_summergaze = Transform("images/bg/summergaze.png", xysize=(1920, 1080), fit="cover")
image bg_sungaze = Transform("images/bg/sungaze.png", xysize=(1920, 1080), fit="cover")
image bg_desert = Transform("images/bg/desert.png", xysize=(1920, 1080), fit="cover")

## 甜品店对视 1-7 + 6.51：场景渐进。1-3 暖色（团子吃法递进），4-6 转入蓝色调
## 幻视（波纹由弱到强、王霜由实体到融入背景），6.51 过渡，7 阿鹤呕吐导致色彩复原。
## 源图均已 resize 到 3840x2160 以避开 GPU 4096 像素纹理限制（否则会被分块渲染、
## 中间出现接缝；见 git 历史里 甜品店6.50.png 的资料）。
image bg_dessertgaze1 = Transform("images/bg/甜品店对视1.png", xysize=(1920, 1080), fit="cover")
image bg_dessertgaze2 = Transform("images/bg/甜品店对视2.png", xysize=(1920, 1080), fit="cover")
image bg_dessertgaze3 = Transform("images/bg/甜品店对视3.png", xysize=(1920, 1080), fit="cover")
image bg_dessertgaze4 = Transform("images/bg/甜品店对视4.png", xysize=(1920, 1080), fit="cover")
image bg_dessertgaze5 = Transform("images/bg/甜品店对视5.png", xysize=(1920, 1080), fit="cover")
image bg_dessertgaze6 = Transform("images/bg/甜品店对视6.png", xysize=(1920, 1080), fit="cover")
image bg_dessertgaze6_51 = Transform("images/bg/甜品店对视6.51.png", xysize=(1920, 1080), fit="cover")
image bg_dessertgaze7 = Transform("images/bg/甜品店对视7.png", xysize=(1920, 1080), fit="cover")
image bg_dessertgaze8 = Transform("images/bg/甜品店对视8.png", xysize=(1920, 1080), fit="cover")

## 旧资源：之前实验用的甜品店 + 水面波纹 shader。剧本里已经没有 甜品店幻视 场景
## 引用它了，留着以备后续如果要给某一帧加 shader 动画时直接复用。
## shader 注册和 _ripple_tick callback 见 game/scripts/shaders.rpy。
image bg_dessertshop:
    Transform("images/bg/甜品店对视6.50.png", xysize=(1920, 1080), fit="cover")
    shader "game.water_ripple"
    u_ripple_strength 1.5
    u_ripple_speed 1.0
    u_ripple_scale 12.0
    function _ripple_tick

################################################################################
## 资源替换说明
##
## 当美术资源准备好后，将此文件中的 Solid() 替换为实际图片路径：
##
## 例如:
##   image bg_placeholder = "images/bg/main_bg.png"
##   image bg_room = "images/bg/room.png"
##
## 或者直接删除此文件，将 PNG/JPG 文件放入 images/bg/ 目录，
## Ren'Py 会自动识别（文件名即为 image 名称）
################################################################################
