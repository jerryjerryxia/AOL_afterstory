## transitions.rpy
## 场景转场效果定义 / Scene Transition Definitions
##
## 在此统一调整全游戏的转场手感。route .rpy 由 convert_script.py 生成，
## 转场与特效处会引用下面这些名字。

## 默认场景转场 —— 经过黑场的淡入淡出（淡出 0.4s / 黑场停留 0.1s / 淡入 0.5s）
## 比纯溶解更明确：无论前后背景多相似，黑场都能让"换场"被清楚感知。
define scene_soft = Fade(0.4, 0.1, 0.5)

## 戏剧性瞬间的特效转场（由舞台提示关键词触发，见 convert_script.py 的 SPECIAL_FX）
define fx_glitch = hpunch    ## 故障 / glitch —— 横向震动
define fx_shock = vpunch     ## 惊吓 / 冲击 —— 纵向震动
