## achievements.rpy
## Steam 成就骨架。用 Ren'Py 内置 achievement 模块（有无 Steam 都能跑：没 Steam 时
## 记在 persistent，接上 Steam 后 sync 会补推）。Steam 端启用见 options.rpy 的
## config.steam_appid，以及启动器 Install Libraries → Steam。

## 已解锁成就的内部 key 集合（真值来源；与是否填了 Steam 名字无关，先记录、后补推）。
default persistent.achievements_unlocked = set()

init python:
    ##########################################################################
    ## ★★★ 成就映射 ★★★
    ## 右边是 Steam **API Name**（代码里用的稳定标识）—— 必须和你在 Steamworks 后台
    ## 注册成就时填的 "API Name" 一字不差。玩家看到的**显示名**（中/英）在后台各语言
    ## 里单独设置，就是每行注释里的「中文 / English」。左边 key 是游戏内部标识，别改。
    ##########################################################################
    ACHIEVEMENTS = {
        ## —— 每个结局（含坏结局）——
        "bad_end_1":  "WAVERING_TILL_DEATH",      # 举棋不定 / Wavering Till Death
        "bad_end_2":  "CURIOSITY_KILLS_THE_CAT",  # 好奇害死猫 / Curiosity Kills the Cat
        "bad_end_3":  "FAIR_CARNAGE",             # 平等杀戮 / Fair Carnage
        "normal_end": "IN_THE_RAIN",              # 在雨中 / In the Rain
        "happy_end":  "THAT_MAKES_TWO_OF_US",     # 对饮成？人 / That Makes Two of Us
        "true_end":   "THE_END_OF_A_LONG_DREAM",  # 大梦初醒 / The End of a Long Dream

        ## —— 前两个周目完成 ——
        "route1_clear": "ENDLESS_SUMMER",         # 无休夏日 / Endless Summer
        "route2_clear": "ALL_BUT_NAUGHT",         # 一场空 / All But Naught

        ## —— 一个存档里，每个 madness 选择都选了 +1 的那一项 ——
        "all_madness":  "DIARY_OF_A_MADMAN",      # 狂人日记 / Diary of a Madman

        ## —— 全成就（集齐上面所有）——
        "all_achievements": "LOVELY_SUMMERTIME",  # 完美夏日 / Lovely Summertime
    }

    _META_KEY = "all_achievements"
    _NON_META_KEYS = [k for k in ACHIEVEMENTS if k != _META_KEY]

    def _push_to_steam(key):
        """名字填好了才真正推给 Steam；占位符 TODO_ 时跳过。"""
        name = ACHIEVEMENTS.get(key)
        if name and not name.startswith("TODO_"):
            achievement.grant(name)
            achievement.sync()

    def grant_achievement(key):
        """记录并解锁一个成就（幂等），顺带检查"全成就"。"""
        if key not in ACHIEVEMENTS or key in persistent.achievements_unlocked:
            return
        persistent.achievements_unlocked.add(key)
        _push_to_steam(key)
        ## 全成就：集齐其它所有非 meta 成就 → 解锁
        if key != _META_KEY and all(k in persistent.achievements_unlocked for k in _NON_META_KEYS):
            grant_achievement(_META_KEY)

    def sync_achievements():
        """把已记录的成就全部补推到 Steam。用于：填好名字后的首次启动、换设备、
        或离线解锁后再联网。after_load / 主菜单调一次即可（见 variables.rpy）。"""
        for key in persistent.achievements_unlocked:
            _push_to_steam(key)
        achievement.sync()

    def check_madness_achievement():
        """"一个存档里每个 madness 选择都选了 +1" → 解锁。
        madness_choices_seen / madness_plus_taken 由转换器在每个 madness 菜单埋点
        （见 convert_script.py 的 menu 生成 + variables.rpy 的 default）。
        语义：本存档至今遇到的每个"带 +1 选项"的选择，玩家都选了 +1。在每个结局处检查。"""
        if madness_choices_seen > 0 and madness_choices_seen == madness_plus_taken:
            grant_achievement("all_madness")
