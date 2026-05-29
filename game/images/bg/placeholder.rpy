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
## 在 splashscreen 启动后一直跑。所有引用 bg_polyhedron_video 的地方（主菜单、序章首场景）
## 都从同一个 channel 取当前帧 —— 切场景不重置帧位置，做到无缝衔接。
## 暂时只在 prologue 的"无色透明多面体动画"场景使用；后续如要全局生效，把 SCENE_BG_MAP
## 里的 '无色透明多面体动画' 改成 '无色透明多面体'，并把 main_script_raw.txt 里的临时改名改回。
image bg_polyhedron_video = Movie(
    channel="polyhedron_video",
    size=(1920, 1080)
)

image bg_summergaze = Transform("images/bg/summergaze.png", xysize=(1920, 1080), fit="cover")
image bg_sungaze = Transform("images/bg/sungaze.png", xysize=(1920, 1080), fit="cover")
image bg_dessertgaze = Transform("images/bg/dessertgaze.png", xysize=(1920, 1080), fit="cover")
image bg_desert = Transform("images/bg/desert.png", xysize=(1920, 1080), fit="cover")

## 甜品店：内嵌水面波纹 shader，让画面持续流动。
## shader 注册和 _ripple_tick callback 见 game/scripts/shaders.rpy。
image bg_dessertshop:
    Transform("images/bg/甜品店6.50.png", xysize=(1920, 1080), fit="cover")
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
