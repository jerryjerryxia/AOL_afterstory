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
