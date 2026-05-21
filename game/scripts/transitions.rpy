## transitions.rpy
## 场景转场效果定义 / Scene Transition Definitions
##
## 在此统一调整全游戏的转场手感。route .rpy 由 convert_script.py 生成，
## 转场与特效处会引用下面这些名字。

## 默认场景转场 —— 柔和的长溶解
define scene_soft = Dissolve(0.8)

## 戏剧性瞬间的特效转场（由舞台提示关键词触发，见 convert_script.py 的 SPECIAL_FX）
define fx_glitch = hpunch    ## 故障 / glitch —— 横向震动
define fx_shock = vpunch     ## 惊吓 / 冲击 —— 纵向震动
