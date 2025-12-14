## characters.rpy
## 角色定义 / Character Definitions

################################################################################
## 角色定义
## 在这里定义所有角色。之后替换实际角色名称和颜色。
################################################################################

## 旁白/内心独白（无名字显示）
define narrator = Character(None, kind=adv)

## 主角内心独白
define protag_thought = Character(None, kind=adv, what_prefix='"', what_suffix='"', what_italic=True)

## 示例角色 - 请根据实际剧本修改
## 格式: define 变量名 = Character("显示名称", color="名字颜色")

define placeholder_a = Character("角色A", color="#c8ffc8")
define placeholder_b = Character("角色B", color="#c8c8ff")
define placeholder_c = Character("角色C", color="#ffc8c8")

## 未知角色（用于角色未揭示身份时）
define unknown = Character("???", color="#888888")

################################################################################
## 角色精灵图定义
## 使用 layeredimage 实现表情变化
################################################################################

## 占位符精灵图 - 用纯色方块代替
## 当美术资源准备好后，替换为实际的 layeredimage 定义

image placeholder_a_sprite = Solid("#4a7c4a", xsize=400, ysize=800)
image placeholder_b_sprite = Solid("#4a4a7c", xsize=400, ysize=800)
image placeholder_c_sprite = Solid("#7c4a4a", xsize=400, ysize=800)

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
