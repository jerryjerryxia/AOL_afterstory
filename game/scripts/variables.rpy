## variables.rpy
## 游戏变量和标记 / Game Variables and Flags

################################################################################
## 持久化数据（跨存档保存）
################################################################################

## 结局解锁状态
default persistent.ending_a_unlocked = False
default persistent.ending_b_unlocked = False

## 音乐解锁状态（用于音乐鉴赏）
default persistent.music_unlocked = set()

## 玩家是否已完成一周目
default persistent.first_playthrough_complete = False

################################################################################
## 游戏内变量（每次游戏重置）
################################################################################

## 当前路线（如果有分支）
default current_route = None

## 关键选择记录
default choice_flags = {
    "key_choice_1": None,
    "key_choice_2": None,
    # 根据剧本需求添加更多
}

## 好感度/关系值（如果需要）
# default affection = {
#     "character_a": 0,
#     "character_b": 0,
# }

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
        if ending_id == "a":
            persistent.ending_a_unlocked = True
        elif ending_id == "b":
            persistent.ending_b_unlocked = True
        persistent.first_playthrough_complete = True

    def get_ending_count():
        """获取已解锁的结局数量"""
        count = 0
        if persistent.ending_a_unlocked:
            count += 1
        if persistent.ending_b_unlocked:
            count += 1
        return count
