## characters.rpy
## 角色定义 / Character Definitions

################################################################################
## 角色定义
## 在这里定义所有角色。之后替换实际角色名称和颜色。
################################################################################

## 旁白/内心独白（无名字显示）
define narrator = Character(None, kind=adv)

## 大文本框旁白（用于长篇背景叙述）
define large_narrator = Character(None, kind=adv, screen="large_say")

## 主角内心独白
define protag_thought = Character(None, kind=adv, what_prefix='"', what_suffix='"', what_italic=True)

## 主要角色
## 格式: define 变量名 = Character("显示名称", color="名字颜色")

define wangshuang = Character("王霜", color="#9b59b6")  # 紫色
define wangshuang_unknown = Character("王霜（？）", color="#9b59b6")  # 紫色，身份存疑
define ahe = Character("阿鹤", color="#4a90d9")  # 蓝色
define shishou = Character("尸首", color="#dc143c")  # 深红色

## 配角 - Supporting Characters
define lurenjia = Character("路人甲", color="#7f8c8d")  # 灰色
define lurenyi = Character("路人乙", color="#95a5a6")  # 浅灰色
define lurenbing = Character("路人丙", color="#6c7a89")  # 深灰色
define lurending = Character("路人丁", color="#a0a0a0")  # 中灰色
define jieluowa = Character("杰罗瓦", color="#e67e22")  # 橙色
define mijie = Character("米姐", color="#27ae60")  # 绿色
define youliya = Character("尤里娅", color="#f1c40f")  # 金色

## 未知角色（用于角色未揭示身份时）
define unknown = Character("???", color="#888888")

################################################################################
## 角色精灵图定义
## 使用 layeredimage 实现表情变化
################################################################################

## 占位符精灵图 - 用纯色方块代替
## 当美术资源准备好后，替换为实际的 layeredimage 定义

image wangshuang_sprite = Solid("#9b59b6", xsize=400, ysize=800)
image ahe_sprite = Solid("#4a90d9", xsize=400, ysize=800)
image shishou_sprite = Solid("#dc143c", xsize=400, ysize=800)

## 实际角色精灵图示例（当资源准备好时使用）：
# layeredimage character_name:
#     always:
#         "sprites/character_name/base.png"
#     group expression:
#         attribute neutral default:
#             "sprites/character_name/neutral.png"
#         attribute happy:
#             "sprites/character_name/happy.png"
#         attribute sad:
#             "sprites/character_name/sad.png"
#         attribute angry:
#             "sprites/character_name/angry.png"

################################################################################
## 角色立绘位置预设
################################################################################

## 常用位置
transform left_pos:
    xalign 0.2
    yalign 1.0

transform center_pos:
    xalign 0.5
    yalign 1.0

transform right_pos:
    xalign 0.8
    yalign 1.0

transform far_left_pos:
    xalign 0.1
    yalign 1.0

transform far_right_pos:
    xalign 0.9
    yalign 1.0

## 带动画的入场/退场
transform enter_left:
    xalign 0.0
    alpha 0.0
    linear 0.3 xalign 0.2 alpha 1.0

transform enter_right:
    xalign 1.0
    alpha 0.0
    linear 0.3 xalign 0.8 alpha 1.0

transform exit_left:
    linear 0.3 xalign 0.0 alpha 0.0

transform exit_right:
    linear 0.3 xalign 1.0 alpha 0.0
