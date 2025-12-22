## variables.rpy
## 游戏变量和标记 / Game Variables and Flags

################################################################################
## 测试模式 - Test Mode
## 设为 True 可以快进未读文本，用于测试多周目流程
################################################################################

define config.developer = True  # 启用开发者模式
default persistent.test_mode = True  # 测试模式开关

init python:
    # 测试模式：允许跳过未读文本
    if persistent.test_mode:
        config.allow_skipping = True
        _preferences.skip_unseen = True

################################################################################
## 持久化数据（跨存档保存）
################################################################################

## 结局解锁状态
default persistent.bad_end_1_unlocked = False  # 举棋不定
default persistent.bad_end_2_unlocked = False  # 好奇害死猫
default persistent.bad_end_3_unlocked = False  # 平等杀戮
default persistent.normal_end_unlocked = False  # 日常
default persistent.happy_end_unlocked = False  # Happy End?

## 周目进度追踪
default persistent.route1_complete = False  # 一周目完成
default persistent.route2_complete = False  # 二周目完成
default persistent.route3_complete = False  # 三周目完成

## 音乐解锁状态（用于音乐鉴赏）
default persistent.music_unlocked = set()

## 开发者音乐选择（场景ID -> 曲目ID）
default persistent.scene_music_selections = {}

################################################################################
## 游戏内变量（每次游戏重置）
################################################################################

## 当前路线
default current_route = None

## madness 值 - 根据选择增加
default madness = 0

## 关键选择记录
default choice_flags = {}

## 当前场景转场信息（开发者用）
default current_scene_name = None  # 场景名称，如 "两座冰雕2"
default current_scene_desc = None  # 场景描述

################################################################################
## 辅助函数
################################################################################

init python:
    def unlock_music(track_name):
        """解锁音乐鉴赏中的曲目"""
        if track_name not in persistent.music_unlocked:
            persistent.music_unlocked.add(track_name)

    def is_music_unlocked(track_name):
        """检查曲目是否已解锁"""
        return track_name in persistent.music_unlocked

    def unlock_ending(ending_id):
        """解锁结局"""
        if ending_id == "bad_end_1":
            persistent.bad_end_1_unlocked = True
        elif ending_id == "bad_end_2":
            persistent.bad_end_2_unlocked = True
        elif ending_id == "bad_end_3":
            persistent.bad_end_3_unlocked = True
        elif ending_id == "normal_end":
            persistent.normal_end_unlocked = True
        elif ending_id == "happy_end":
            persistent.happy_end_unlocked = True

    def unlock_route(route_num):
        """标记周目完成"""
        if route_num == 1:
            persistent.route1_complete = True
        elif route_num == 2:
            persistent.route2_complete = True
        elif route_num == 3:
            persistent.route3_complete = True

    def get_current_route():
        """获取当前应进入的周目"""
        if not persistent.route1_complete:
            return 1
        elif not persistent.route2_complete:
            return 2
        else:
            return 3

    def get_ending_count():
        """获取已解锁的结局数量"""
        count = 0
        if persistent.bad_end_1_unlocked:
            count += 1
        if persistent.bad_end_2_unlocked:
            count += 1
        if persistent.bad_end_3_unlocked:
            count += 1
        if persistent.normal_end_unlocked:
            count += 1
        if persistent.happy_end_unlocked:
            count += 1
        return count

    ##########################################################################
    ## 开发者音乐选择器函数
    ##########################################################################

    def select_and_play_music(scene_id, track_id):
        """选择并播放场景音乐"""
        if scene_id not in scene_music:
            return

        # Save selection
        persistent.scene_music_selections[scene_id] = track_id

        # Find track and play
        for track in scene_music[scene_id]["tracks"]:
            if track["id"] == track_id:
                renpy.music.play("audio/bgm/" + track["file"], fadeout=1.0, fadein=1.0)
                break

    def set_scene_music(scene_id):
        """设置当前场景音乐并自动播放"""
        global current_music_scene
        store.current_music_scene = scene_id

        if scene_id not in scene_music:
            return

        tracks = scene_music[scene_id]["tracks"]
        if not tracks:
            return

        # Check if we have a saved selection for this scene
        saved_track_id = persistent.scene_music_selections.get(scene_id)

        if saved_track_id:
            # Play the saved selection
            for track in tracks:
                if track["id"] == saved_track_id:
                    renpy.music.play("audio/bgm/" + track["file"], fadeout=1.0, fadein=1.0)
                    return

        # No saved selection - play first track
        renpy.music.play("audio/bgm/" + tracks[0]["file"], fadeout=1.0, fadein=1.0)
