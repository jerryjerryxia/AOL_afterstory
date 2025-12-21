## music_config.rpy
## Developer music selector configuration
## Maps scene IDs to available background music tracks

init python:
    # Scene music configuration
    # Each scene ID maps to a label and list of candidate tracks
    # "file" should match files in game/audio/bgm/

    scene_music = {
        "prologue_1": {
            "label": "序章 - 深海场景",
            "tracks": [
                {"id": "gaidankousetsu", "name": "Gaidankousetsu", "file": "Gaidankousetsu.mp3"},
                {"id": "electric_sea", "name": "Electric Sea", "file": "ElectricSea.mp3"},
                {"id": "padmasana", "name": "Padmasana", "file": "Padmasana.mp3"},
                {"id": "doutokutosetsu", "name": "Doutokutosetsu", "file": "Doutokutosetsu.mp3"},
                {"id": "shinsou_no_reijou", "name": "Shinsou no reijou", "file": "Shinsou_no_reijou.mp3"},
            ]
        },
        "route1_scene1": {
            "label": "一周目 场景1 - 沙滩",
            "tracks": [
                {"id": "shine_of_silver_thaw", "name": "Shine of Silver Thaw", "file": "Shine_of_Silver_Thaw.mp3"},
                {"id": "sunflower_of_night", "name": "The sunflower of the night", "file": "The_sunflower_of_the_night.mp3"},
                {"id": "running_waters", "name": "Running Waters", "file": "RunningWaters.mp3"},
                {"id": "jellyfish", "name": "Jellyfish", "file": "Jellyfish.mp3"},
            ]
        },
        "route1_scene2": {
            "label": "一周目 对话场景",
            "tracks": [
                {"id": "moonlit_reverie", "name": "Moonlit Reverie", "file": "Moonlit_Reverie.mp3"},
                {"id": "hoyoku", "name": "Hoyoku", "file": "Hoyoku.mp3"},
                {"id": "sutekimeppou", "name": "Sutekimeppou", "file": "Sutekimeppou.mp3"},
            ]
        },
        "route1_hallucination": {
            "label": "一周目 幻视场景",
            "tracks": [
                {"id": "beautiful_daughter", "name": "Beautiful Daughter", "file": "Beautiful_Daughter.mp3"},
            ]
        },
        "route1_deepspace": {
            "label": "一周目 深空场景",
            "tracks": [
                {"id": "deepspace", "name": "DeepSpace", "file": "DeepSpace.mp3"},
                {"id": "snowfall", "name": "snowfall", "file": "øneheart_x_reidenshi_snowfall.mp3"},
                {"id": "time_slows_down", "name": "time slows down", "file": "time_slows_down.mp3"},
                {"id": "broken_air", "name": "Broken Air", "file": "Broken_Air.mp3"},
            ]
        },
        "route1_desert": {
            "label": "一周目 沙漠场景",
            "tracks": [
                {"id": "whispers_twilight", "name": "Whispers in the Twilight", "file": "Whispers_in_the_Twilight.mp3"},
                {"id": "whats_left", "name": "What's Left Feels Light", "file": "What's_Left_Feels_Light.mp3"},
                {"id": "sanpo", "name": "Sanpo", "file": "Sanpo.mp3"},
            ]
        },
        "route1_transition": {
            "label": "一周目 场景过渡",
            "tracks": [
                {"id": "blackfly", "name": "BlackFly", "file": "BlackFly.mp3"},
            ]
        },
        "route1_return": {
            "label": "一周目 回归场景",
            "tracks": [
                {"id": "shine_of_silver_thaw", "name": "Shine of Silver Thaw", "file": "Shine_of_Silver_Thaw.mp3"},
                {"id": "sunflower_of_night", "name": "The sunflower of the night", "file": "The_sunflower_of_the_night.mp3"},
                {"id": "running_waters", "name": "Running Waters", "file": "RunningWaters.mp3"},
                {"id": "shianchu", "name": "Shianchu", "file": "Shianchu.mp3"},
            ]
        },
        "route2_opening": {
            "label": "二周目 开场",
            "tracks": [
                {"id": "gaidankousetsu", "name": "Gaidankousetsu", "file": "Gaidankousetsu.mp3"},
                {"id": "electric_sea", "name": "Electric Sea", "file": "ElectricSea.mp3"},
                {"id": "padmasana", "name": "Padmasana", "file": "Padmasana.mp3"},
                {"id": "doutokutosetsu", "name": "Doutokutosetsu", "file": "Doutokutosetsu.mp3"},
                {"id": "shinsou_no_reijou", "name": "Shinsou no reijou", "file": "Shinsou_no_reijou.mp3"},
            ]
        },
        "route2_lofi": {
            "label": "二周目 Lo-fi对话场景",
            "tracks": [
                {"id": "moonlit_reverie", "name": "Moonlit Reverie", "file": "Moonlit_Reverie.mp3"},
                {"id": "hoyoku", "name": "Hoyoku", "file": "Hoyoku.mp3"},
                {"id": "sutekimeppou", "name": "Sutekimeppou", "file": "Sutekimeppou.mp3"},
            ]
        },
        "route2_battle": {
            "label": "二周目 战斗/紧张场景",
            "tracks": [
                {"id": "sensou", "name": "Sensou", "file": "Sensou.mp3"},
                {"id": "gehou", "name": "Gehou", "file": "Gehou.mp3"},
            ]
        },
        "route2_shiniki": {
            "label": "二周目 Shiniki场景",
            "tracks": [
                {"id": "shiniki", "name": "Shiniki", "file": "Shiniki.mp3"},
            ]
        },
        "route2_chat": {
            "label": "二周目 唠嗑场景",
            "tracks": [
                {"id": "shitagokoro", "name": "Shitagokoro", "file": "Shitagokoro.mp3"},
            ]
        },
        "route2_kegen": {
            "label": "二周目 Kegen场景",
            "tracks": [
                {"id": "kegen", "name": "Kegen", "file": "Kegen.mp3"},
            ]
        },
        "route2_weird": {
            "label": "二周目 怪异唠嗑",
            "tracks": [
                {"id": "tamikurasou", "name": "Tamikurasou", "file": "Tamikurasou.mp3"},
            ]
        },
        "route3_opening": {
            "label": "三周目 开场",
            "tracks": [
                {"id": "gaidankousetsu", "name": "Gaidankousetsu", "file": "Gaidankousetsu.mp3"},
                {"id": "electric_sea", "name": "Electric Sea", "file": "ElectricSea.mp3"},
                {"id": "padmasana", "name": "Padmasana", "file": "Padmasana.mp3"},
                {"id": "doutokutosetsu", "name": "Doutokutosetsu", "file": "Doutokutosetsu.mp3"},
                {"id": "shinsou_no_reijou", "name": "Shinsou no reijou", "file": "Shinsou_no_reijou.mp3"},
            ]
        },
        "route3_shiniki": {
            "label": "三周目 Shiniki场景",
            "tracks": [
                {"id": "shiniki", "name": "Shiniki", "file": "Shiniki.mp3"},
            ]
        },
        "route3_chat": {
            "label": "三周目 唠嗑场景",
            "tracks": [
                {"id": "shitagokoro", "name": "Shitagokoro", "file": "Shitagokoro.mp3"},
            ]
        },
        "route3_jellyfish": {
            "label": "三周目 Jellyfish场景",
            "tracks": [
                {"id": "jellyfish", "name": "Jellyfish", "file": "Jellyfish.mp3"},
            ]
        },
        "route3_lovely_summer": {
            "label": "三周目 Lovely Summer Time",
            "tracks": [
                {"id": "lovely_summertime", "name": "Lovely Summer Time", "file": "LovelySummertime.wav"},
            ]
        },
        "route3_final": {
            "label": "三周目 最终场景",
            "tracks": [
                {"id": "doutokutosetsu", "name": "Doutokutosetsu", "file": "Doutokutosetsu.mp3"},
            ]
        },
        "route3_ending": {
            "label": "三周目 结局",
            "tracks": [
                {"id": "go_with_flow", "name": "Go with the Flow", "file": "GoWithTheFlow.wav"},
            ]
        },
    }
