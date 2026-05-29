## route2.rpy
## Route 2

label route2_start:

## 二周目：水底捞月

    ## 转场：黑屏
    scene black with scene_soft
    $ current_scene_name = "黑屏"
    $ current_scene_desc = "仔细一想，黑屏可以试着搞出深海漆黑的感觉...就不是纯黑更接近非常非常深的深蓝这样，然后有一些不太明显的质感。"
    ## 场景音乐参考：Electric Sea (Buckethead), Padmasana (Buckethead)，Doutokutosetsu，Shinsou no reijou，Gaidankousetsu - 物语ost是好文化
    $ set_scene_music("route2_opening")
    ## 脸入水后冒泡泡的音效
    "还要回来么。"

    menu:
        extend ""
        "下潜":
            pass
        "也许...不要？":
            return

    ## Extended文本框开始 - accumulating textbox
    "来探监？"
    extend "\n如你所见，这是一座空空如也的牢房，除了一轮明月映在水里的虚影之外一无所有。"
    ## Extended文本框结束
    ## Extended文本框开始 - accumulating textbox
    "只需伸伸手就能辨明虚实的事，何苦为之再入轮回？"
    ## Extended文本框结束

    menu:
        extend ""
        "继续下潜":
            pass
        "或许确实意义不大...":
            return

    ## Extended文本框开始 - accumulating textbox
    "走得再远也只能原地打转罢了。"
    extend "\n充耳不闻、一意孤行终究是没有意义的事情。"
    ## Extended文本框结束
    ## Extended文本框开始 - accumulating textbox
    "哦...意义么...你看，和你聊天总让我的理智退化到一种不堪入目的境地。"
    extend "\n也罢，来就来吧——意识的方舟已经启航，众人安眠的棺椁已然下葬，你如果执意要倒行逆施，随意便是。"
    ## Extended文本框结束

    menu:
        extend ""
        "下潜":
            pass
        "下潜":
            pass

    ## 居中大字文本框开始 - centered large font textbox
    centered_large_narrator "真他妈无聊啊。"
    ## 居中大字文本框结束
    call screen route_title("水底捞月")
    ## 转场：夏日对视
    scene bg_summergaze with scene_soft
    $ current_scene_name = "夏日对视"
    $ current_scene_desc = "金色的沙滩和蔚蓝的海，只是一个人都没有，场景里依然只有王霜"
    wangshuang "你来了。"
    ahe "又来？"
    wangshuang "嗯，有什么问题么？"
    ahe "不好意思...我...来过这里吗...？"
    wangshuang "大概吧。"
    ahe "我感觉...有个熟悉的声音在我耳边一直说个不停，让我去做非常恶毒的事情..."
    wangshuang "它让你做什么？"
    ahe "‘撕碎皮肤，折断骨头，直到一点声音也不留下’。"
    wangshuang "哦，这样。"
    ahe "我...又病了吗？"
    wangshuang "还差得远呢。"
    ahe "好吧..."
    wangshuang "甚至可以说这是在往好的方向发展，你完全可以照着它说的去做啊。"
    ahe "啊？为什么？"
    wangshuang "为什么不呢？在这个没有后果的地方，只管放纵便是，放纵到连一切都显得无聊透顶才好。"
    wangshuang "而且你眼前就有一具活脱脱的躯体供你发泄。"
    ahe "阿霜，这不好笑。"
    wangshuang "哦，随你便，我也只是经验之谈。"
    wangshuang "但如果你想要那声音停下的话，不满足它的愿望大概是不行的。"
    ahe "真的假的..."
    wangshuang "作为你的主治医师，我还是那句话，你的病早就好了。"
    wangshuang "如果你觉得感官认知还有异常，那也只是朴素过程的一部分而已。"
    ahe "所以迄今为止的“朴素过程”...是你希望看到的吗？"
    wangshuang "当然，怎么了？"
    ahe "如果这都是你希望看到的...那为什么你看起来如此的..."
    wangshuang "和你没关系。"
    ahe "阿霜，你真的——"
    wangshuang "喂，阿鹤，你这破毛病到底什么时候能改改？一有人给你臭脸，马上就开始浮想联翩要给人诊断创伤。"
    wangshuang "连个像样的学位都没有就在这儿意淫，意淫完然后呢？再来一次你那轰轰烈烈的救风尘大冒险？"
    wangshuang "不要觉得自己现在稍微会读人表情了就了不起了，那只意味着你三十岁前都是个巨婴，不是什么值得骄傲的事情。"
    wangshuang "所以趁我还有耐心，你最好仔细想想自己到底是怎么落到这步田地的。"
    ahe "可这和我没有关系。"
    wangshuang "闭嘴。"
    ahe "阿霜。"
    wangshuang "我说闭嘴。"
    ahe "究竟为什么要把——"
    wangshuang "我他妈的让你给我闭嘴！"
    ahe "..."
    wangshuang "不要做没有意义的事情。"
    ahe "即使最基本的相互理解也不行么？"
    wangshuang "理解什么？你需要知道的一切都已经装在你脑壳里了，去慢慢理解吧。"
    ahe "喂...阿霜！"
    ## Extended大文本框开始 - accumulating large textbox
    ## 转场：完美夏日
    scene black with scene_soft
    $ current_scene_name = "完美夏日"
    $ current_scene_desc = "金色的沙滩和蔚蓝的海，只是一个人都没有，和夏日对视的背景一致，只是没有人物"
    large_narrator "随着她丢下不温不火的告别，王霜便如一股青烟般消散了。完美的夏日光景里再次只留下孤零零的你。"
    extend "\n这幅场景也似曾相识——你回想起了某件重要的事情，却又抓不住任何具体的画面。"
    extend "\n只记得你曾做过一个长久而模糊的、关于忍耐与空虚的梦。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "但你决定做些什么。"
    extend "\n你循着回忆里模糊的画面，用手指蜷成小孔，试图透过那微小的空隙来窥探钉在天顶的那轮烈日。"
    ## Extended大文本框结束
    ## 转场：白屏
    scene black with scene_soft
    $ current_scene_name = "白屏"
    $ current_scene_desc = "就是白屏。"
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "强光刺目，你的全身肌肉与神经都尖叫着颤抖着抗议你毫无意义的自毁行为。"
    extend "\n眼角注满泪水，眼球如烈火灼烧般压迫着你的视神经。"
    extend "\n瞳孔周围的肌肉正拼尽全力地收缩着，但你强忍剧痛，一边痛苦地嘶吼，一边强迫自己继续张目对日。"
    extend "\n直到你看见了——"
    extend "\n光线丛中心，有一颗熊熊燃烧的火球，给予世间万物以生命的神圣火球。"
    extend "\n而在那火球的中心，你看见了一件似曾相识的事物。"
    ## Extended大文本框结束
    ## 转场：无色透明多面体2
    scene black with scene_soft
    $ current_scene_name = "无色透明多面体2"
    $ current_scene_desc = "白屏，中间有无色透明多面体"
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "那东西看似球体，却又好似有无数细小的平面，看似无色透明，却又从中散发出难以言喻的光晕。"
    extend "\n你进一步缩小手指间的空隙，直到视野中只剩下那神秘的多面体。"
    extend "\n随着阳光被剔除，那多面体所散发出的光线也越发怡人，你觉得它几乎变得触手可及了。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "那是你的——那沉寂了一阵的声音又开始作祟。"
    extend "\n一直以来都是你的——见你无动于衷，那声音逐渐提高了音量。"
    extend "\n拿回来吧，伸手就行了，拿回来吧！"
    extend "\n虽然不明就里，但你还是伸出了手。"
    ## Extended大文本框结束
    ## 电视关机音效
    ## 转场：黑屏
    scene black with scene_soft
    $ current_scene_name = "黑屏"
    $ current_scene_desc = "就是黑屏。"
    wangshuang "别。"
    ahe "阿霜？"
    ## 转场：夏日对视
    scene bg_summergaze with scene_soft
    $ current_scene_name = "夏日对视"
    $ current_scene_desc = "金色的沙滩和蔚蓝的海，只是一个人都没有，场景里依然只有王霜"
    wangshuang "别随便碰别人的东西。"
    ahe "可我没想碰——"
    wangshuang "不用狡辩，你做到了，你把我逼回来了，现在开心了么？"
    ahe "我没有想...我只想知道我到底为什么回到了这里。"
    wangshuang "都是没有意义的，阿鹤。你回或不回到这里，在这里死了或在现实中活着，都是没有意义的，所以不要再试图理解了。"
    ahe "所以这就是你想要的吗？"
    wangshuang "我不在乎。"
    ahe "但你明明是在乎——"
    wangshuang "狗屁。"
    ahe "..."
    wangshuang "阿鹤...这里与你的常识和记忆毫无关联，所以不要再用你‘所熟知’的那套狗屁来烦我。"
    ahe "..."

    menu:
        extend ""
        "可是——":
            wangshuang "我！说！闭！嘴！"
            ## 电视机关闭音效
            ## 转场：黑屏
            scene black with scene_soft
            $ current_scene_name = "黑屏"
            $ current_scene_desc = "就是黑屏。"
            ## Bad End 2：好奇害死猫
            $ unlock_ending("bad_end_2")
            return
        "嗯...":
            wangshuang "明白了就好。接下来你需要做的，就是在这个完美的夏日里继续存在下去，不要问问题，不要到处乱走，不要莫名其妙去死。如果你真的想重新开始的话，闭上眼睛就行了。明白了吗？"
            ahe "嗯..."
            wangshuang "很好。"
            ahe "ke——"
            wangshuang "嘘——"
            ahe "..."
            ## Extended大文本框开始 - accumulating large textbox
            large_narrator "你心里有千言万语想要倾泻，然而在这完美且孤寂的明丽夏日里没有言语的空间。"
            extend "\n时间早就没有意义了——你依稀记得阿霜也这样说过，如今则实实在在地体会到了这句话的重量。"
            extend "\n太阳永远高挂在天顶，完美的蔚蓝天空遥远而平整，白金色沙滩上的沙砾们不知去向地腾挪着，偶尔被洁白的海浪裹挟到远处，偶尔又在巡游后回到原地。"
            ## Extended大文本框结束
            ## 居中大字文本框开始 - centered large font textbox
            centered_large_narrator "万物无不最终回到原地，包括双眼布满血丝的你。"
            ## 居中大字文本框结束
            ## Extended大文本框开始 - accumulating large textbox
            large_narrator "你注视着眼前令人绝望的动态平衡，意识到即使聪慧如阿霜，大概也找不出破局或是解脱的方法。"
            extend "\n一些模糊的冲动在你心里逐渐成型，一如自深海逐渐上浮的泡沫。"
            extend "\n但过量的思索终究使你劳累了。"
            extend "\n某一刹那，困意压过了一切思绪，于是你若无其事地闭上双眼——"
            ## Extended大文本框结束
            ## 电视机关闭音效
            ## 转场：黑屏
            scene black with scene_soft
            $ current_scene_name = "黑屏"
            $ current_scene_desc = "就是黑屏。"
            ## 水底冒泡泡音效

    ## 场景音乐风格参考：怎么说呢...虽然台词可能对抗感比较强，但这种场景还是得要一些 lo-fi 小调啊...Moonlit Reverie - 好lofi，Hoyoku, Sutekimeppou - 这几首物语的 ost 也很有内味儿嗷
    $ set_scene_music("route2_lofi")
    ## 转场：甜品店对视
    scene black with scene_soft
    $ current_scene_name = "甜品店对视"
    $ current_scene_desc = "王霜坐在桌子对面看着镜头方向，背景里是一家疑似甜品店的店面。"
    ahe "你好，我要这个团子。"
    wangshuang "嗯，很懂嘛你。"
    ahe "总觉得...什么时候来过这里。"
    wangshuang "确实像是你会背着我偷偷来的地方——我也要那团子吧。"
    ahe "上次你明明也在。"
    wangshuang "哎阿鹤，病我已经给你治好了，不要在这里假装复发了啊，没必要。"
    ahe "这店的团子好吃是因为加了KAS。"
    wangshuang "对，看来你确实没少来嘛。"
    ahe "所以你也来过。"
    wangshuang "当然，但肯定没和你一起。"
    ahe "...很奇怪..."
    wangshuang "这有什么好纠结的，都来这种地方了还要想这种破事？"
    ahe "好吧..."
    wangshuang "真就跟临死前还非要留种似的，你们男人都这样？"
    ahe "那是假新闻！"
    wangshuang "哎哟，还来劲了！嗑之前一定要先美其名曰‘搞明白药理学’，做之前非要聊半天文学艺术，是不是你？"
    ahe "呃..."
    wangshuang "说话。"
    ahe "好吧...是我。"
    wangshuang "哈哈，真听话。"
    ahe "...你也就只能在我面前逞一时口舌之快了。"
    wangshuang "哦，真的吗？那天在米特拉布，我把来搭讪的小伙说哭了的那次，你不在？"
    ahe "记不得了。"
    wangshuang "那我就告诉你吧——你不仅在，还一副连你一起骂了的样子，在那儿给我摆臭脸，是不是你？"
    ahe "都说了记不得了！"
    wangshuang "嗯，对，选择性失忆，这个我也熟。"
    ahe "好吧好吧，实在失礼。您的骂人功力冠绝逝乐园。"
    wangshuang "嘿，你才是那个只能在我面前逞一时口舌之快的吧...换成别人早就给你吃大嘴巴子了。"
    ahe "那可别，会出人命的。"
    wangshuang "哦，挺来劲？"
    ahe "拜您所赐。"
    wangshuang "别您来您去的，恶心。"
    ahe "好吧..."
    ahe "话说，你手里那东西是？"
    wangshuang "这个？是你用不到的东西。"
    ahe "哦，这样。"
    wangshuang "你倒是再好奇一点啊！"
    ahe "确实没有那么好奇。"
    wangshuang "那你还问！"
    ahe "嗯...听起来你很想解释给我听。"
    wangshuang "我不，但我可以破例给你尝尝。"
    ahe "是吃的啊。"
    wangshuang "用处可多了，但如果想要最直观地明白它的用途，吃下去是见效最快的。"
    ahe "听起来很危险。"
    wangshuang "我要真想害你的话你还能活到今天？所以怎么样，要不要趁团子上来之前试试？空腹吃生效快。"
    ahe "吃了会怎么样？"
    wangshuang "那不好说。和KAS差不多，一千个人吃了会有一万种效果。"
    ahe "...那我试试吧。"
    wangshuang "给，拿着。"
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "你接过王霜手里那无色透明多面体。"
    extend "\n它轻若无物，看似是固体，摸起来却又有介于凝胶和麻薯之间的质感，躺在你手心，冰冰凉的。"
    ## Extended大文本框结束
    ## 居中大字文本框开始 - centered large font textbox
    centered_large_narrator "不要乱吃王霜给的东西！"
    ## 居中大字文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "忽略无关紧要的想法，你若无其事地把手心里的事物送进嘴里。"
    extend "\n入口时的冰凉口感转瞬即逝，随即传来细微的灼烧感，比辣味更微妙些，像一轮排列整齐的钝铁钉轻轻滚过口腔粘膜。"
    extend "\n轻轻咀嚼几下，口感沙沙的，略带弹性，但不粘牙。"
    extend "\n当你正欲下咽时，舌根传来一阵淡淡的苦味，苦味散去后又留下些许细微的回甘。"
    ## Extended大文本框结束
    "这味道——"

    menu:
        extend ""
        "还蛮好吃":
            $ madness += 1
            pass
        "好奇怪":
            pass

    ahe "所以之后会怎么样？"
    wangshuang "什么怎么样？"
    ahe "你刚刚给我吃的那东西，吃了之后——"
    wangshuang "吃了什么？我们点的团子还没来呢。"
    ahe "你给我吃了你一直捏在手里的那东西。"
    wangshuang "我手里的东西？呃...阿鹤，你不会又复发了吧，你先等等，我给你看看我有没有带药..."
    ahe "阿霜，我很好——"
    ## Extended文本框开始 - accumulating textbox
    wangshuang "冷静一下，听着——你那幻视是早就根治掉的问题，现在又复发不是什么好兆头。"
    extend "\n你先在这儿坐好，我让药房给我送点药来，马上就能到。"
    ## Extended文本框结束
    ahe "阿霜，我真的——"
    wangshuang "相信我，阿鹤，你是我们重症科唯一康复出院的病人，我是绝对不会让你复发的。"
    ahe "阿霜，你听我说——"
    wangshuang "阿鹤！阿鹤你先听我说！你这个病我们没有治疗经验，所以出院后的康复我们也只能摸着石头过河，现在出了问题我真的...【“伪”字背景闪过】真的非常抱歉！但我肯定会帮你控制住的，我保证！"
    ahe "阿霜，刚才你给我吃了你手里拿着的无色透明的东西，你还记得这件事吗？"
    wangshuang "阿鹤，没关系的，吃了什么都不会有事的，请你在这里坐几分钟，让我【“伪”字背景闪过】做我该做的工作吧，你是我的病人...？我..."
    ahe "...我要走了。"
    wangshuang "阿鹤！你当然可以走，但能等吃了药、症状稳定下来再走吗？为了你，也为了我【“伪”字背景闪过】，请你让我继续为你治疗...可以吗？"
    ## 转场：黑屏
    scene black with scene_soft
    $ current_scene_name = "黑屏"
    $ current_scene_desc = "就是黑屏。"
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "“王霜医生是逝乐园半岛心理医学界的科研新星，也是量化认知建模这一前沿技术的奠基人。但她最为人所称颂的事迹，还是来自她的本职工作——一名临床心理医生...”"
    extend "\n...闭嘴！"
    extend "\n“时刻战斗在第一线，王霜医生以近乎完美的康复率不断刷新着人们对于心理疾病根治可能性的认知...”"
    extend "\n闭嘴！"
    extend "\n“值得注意的是，在王霜医生经手过的全部患者中，只有一个例外——”"
    extend "\n我说他妈的给我闭嘴！！！"
    extend "\n..."
    extend "\n“只有一个例外——”"
    extend "\n“一个例外——”"
    extend "\n“例外——”"
    extend "\n“外——”"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "“...贺苇......代号...鹤...自...年前...生体盗窃案入狱...发......端暴力倾向...缘性人格障...”"
    extend "\n“...长期治疗无果.......在王霜医生的...下...最终出院...”"
    extend "\n“...”"
    extend "\n“...”"
    extend "\n“随即大开杀戒。”"
    extend "\n..."
    extend "\n原来如此，这样就说得通了。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "——每次见到虚伪的东西，我就想把它砸烂。这是正常的吗？"
    extend "\n——当然了，有这样的情绪再正常不过了，但问题关键在于我们如何消化这种想法。以后每当你有这种冲动的时候，可以试试先在脑子里排练一阵，想明白把你厌恶的事物彻底毁掉需要做什么。"
    extend "\n——啊？为什么？"
    extend "\n——嗯，这么想吧，排练的过程本质上是计划，而计划的本质则是往冲动中注入理性，所以你排练出的结论完全不重要，重要的是你完成了排练这件事。"
    extend "\n——可如果排练完了反倒更想做了怎么办？"
    extend "\n——感谢你的真诚，苇，但你也明白那意味着什么，对吧？"
    extend "\n——知道，但..."
    extend "\n——嗯...首先，正式咨询已经结束了，接下来我要说的都是实验性的想法，所以你可以随心一听，但我觉得也许对你来说很重要，你想听么？"
    extend "\n——随便吧。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "——嗯，是这样的：一切尝试都失效之后，你能做的就只有忍耐。"
    extend "\n——..."
    extend "\n——当你的精神进入长久的忍耐状态后，随着安慰剂效应启动，你的身体也会顺应你的意志，帮助你克制。"
    extend "\n——没意义的...你自己也清楚..."
    extend "\n——嗯，所以还有最后的办法。"
    extend "\n——快说吧..."
    extend "\n——最后重申一遍，接下来要说的不代表我的职业建议，仅是我个人就你的病历作出的不得已判断——在所有药物和认知调节手段确定失效后，屈从于冲动，就这样动手把你认为虚伪的东西彻底摧毁，那就是最后的办法了。伪物...本就缺乏存在的意义，不是么..."
    extend "\n——..."
    ## Extended大文本框结束
    ## 玻璃逐渐碎裂音效
    ## 转场：甜品店对视
    scene black with scene_soft
    $ current_scene_name = "甜品店对视"
    $ current_scene_desc = "王霜坐在桌子对面看着镜头方向，背景里是一家疑似甜品店的店面。"
    ahe "原来如此..."
    ## 虚弱
    wangshuang "...啊？"
    ahe "我想起来了，阿霜。【“杀”字背景闪过】我全都想起来了。"
    ahe "所以这只是一次考验，【“杀”字背景闪过】就像之前那些幻象一样，【“杀”字背景闪过】你只是在验收你的治疗成果而已。"
    ## “杀了她”背景
    ahe "因为...只有我一个人还病着..."
    wangshuang "...不要担心，药马上就到，我一定会帮助你——"
    ## 扑倒音效
    ## 扼颈音效
    ## 转场：红屏
    scene black with scene_soft
    $ current_scene_name = "红屏"
    $ current_scene_desc = "就是红屏。"
    ## 场景音乐参考：Sensou - 众所周知物语是战斗番，Gehou - 这个感觉也不错
    ## 音乐有斟酌空间捏
    $ set_scene_music("route2_battle")
    ahe "这就是你想要的？"
    wangshuang "呃——啊——呃呃呃呃——"
    ahe "当然，这当然是你的愿望。和我没有任何关系，想死的是你..."
    wangshuang "我——呃呃...请松——手——啊啊呃呃。"
    ahe "不然你也不会这样假惺惺地冒出来..."
    wangshuang "阿...鹤..."
    ahe "到最后，我也只是他妈的在做你想我做的事情而已吧...那你就看好了。"
    wangshuang "..."
    ahe "别挣扎了，死人，皮肤要撕碎，骨头要折断，直到一点声音也不留下。内脏要全部碾碎，血要放干。全都是你最喜欢的。那才是你的治疗，阿霜——你在看吧...喜欢我草菅人命的样子么？"
    ## 红屏，血
    wangshuang "唔...啊...啊啊啊啊啊啊——"
    ahe "指甲也要拔下来，牙齿要敲碎，每一根肋骨都要折断，对吧？都是你告诉我的，遇到虚伪的东西就要像这样把它们碾成渣。"
    wangshuang "呃..."
    ahe "撕碎皮肤，折断骨头，直到一点声音也不留下..."
    ahe "死吧...死吧...死吧！给我去死吧！滚出去！永远不要再出现在我面前！"
    ## 红屏，更多血
    wangshuang "..."
    ## Extended文本框开始 - accumulating textbox
    "…"
    extend "\n……"
    extend "\n………"
    ## Extended文本框结束
    ahe "阿霜？"
    "…"
    ahe "阿霜，你在吗？"
    "……"
    ahe "阿霜，我按照你说的那样，把伪物彻底毁掉了。"
    "………"
    ahe "阿霜，你可以回来了？我已经做到了，全都按你说的做到了，所以你回来吧...？"
    ahe "..."
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "或许是因为难以忍受你惨绝人寰的暴行，其他食客与店员都已在你不注意时纷纷离场。"
    extend "\n空无一人的店里，你在一张空空如也的桌子前独坐。"
    extend "\n当然还有一具血肉模糊的尸体陪伴你。"
    extend "\n你呆望着你精心准备的杰作，心中病态的成就感随着时间逐渐模糊。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "一种怪异的情感在你心中萌芽，像月光下的影子，把握不住，可一旦放任不管，它又开始肆意膨胀起来。"
    extend "\n等待良久，真正的阿霜还是没有回来。"
    extend "\n真正的阿霜总是陪在你身边，和你一起把朴素的欲望转化为现实。"
    extend "\n来者不拒，有求必应，如同一个温和的神明。"
    extend "\n总是陪在你身边。"
    extend "\n在你身边。"
    extend "\n你身边。"
    ## Extended大文本框结束
    ## 脚步声
    ## 转场：甜品店
    scene black with scene_soft
    $ current_scene_name = "甜品店"
    $ current_scene_desc = "甜品店对视但拿掉王霜。"
    wangshuang_unknown "阿鹤？"
    "听见背后人声，早些时候肆意膨胀的不明情绪泾渭分明地裂成了两股，但此刻你只有心思去感知其中之一——"

    menu:
        extend ""
        "深入骨髓的恐惧":
            ## 转场：身后的王霜1
            scene black with scene_soft
            $ current_scene_name = "身后的王霜1"
            $ current_scene_desc = "王霜站在主角身后，居高临下地看着主角。"
            $ current_music_scene = None
            stop music fadeout 1.0
            ahe "阿霜...我想...走了..."
            wangshuang "玩得还开心？"
            ahe "一点也不..."
            wangshuang "见到正经行医的我，不觉得是一种新奇的体验吗？虽然最后无论如何都要杀掉确实很可惜就是了。"
            ahe "让我...走..."
            wangshuang "行啊，我们走，但你知道你要去哪里吗？"
            ahe "不知道...让我走..."
            wangshuang "有点主见啊，主见！反正这里做什么都不会有后果，像之前在逝乐园里那样畏畏缩缩地活着多没意思！告诉我吧，你想要什么？"
            ahe "我...只要离开...就行..."
            wangshuang "你啊你，就是这点让人不爽，剧本不是让你跟着走的啊！"
            wangshuang "撕了也行，揉成一团也行。结果你他妈就在这儿一字一句地念稿子。哎...随你便吧。那就这样继续下去吧..."
            ## 电视关机音效
            ## 黑屏
        "如沐春风的安详":
            ## 转场：身后的王霜2
            scene black with scene_soft
            $ current_scene_name = "身后的王霜2"
            $ current_scene_desc = "血肉模糊的王霜站在主角身后，双目无神地看着主角。"
            ## Extended大文本框开始 - accumulating large textbox
            large_narrator "哈哈哈哈哈哈哈哈当然如此！这有什么可意外的呢，对吧，阿霜？如果这是你的愿望，那我当然全盘接受。"
            extend "\n除了全盘接受之外我还有什么选择呢？"
            extend "\n如果你想要反反复复地去死，那我就一次又一次地杀了你，直到你厌倦为止。"
            extend "\n如果你永远不会厌倦，那我们就永远继续下去。"
            extend "\n不管你变成什么模样，不管你身藏何处，我会找到你，用你教我的方法送你上路。"
            extend "\n如果这就是你将意识交还于我的目的，那我自然不会有多余的疑问。我会接受我的使命。"
            extend "\n使命——哈哈哈哈真就他妈的总是使命！扭扭捏捏半天不愿意说明白，搞到最后还不是只要我演好一个角色而已？"
            extend "\n那就去死。"
            extend "\n用你最熟悉的方式去死。"
            extend "\n直到你不再无聊为止。"
            extend "\n所以说，阿霜，你准备好了么？"
            ## Extended大文本框结束
            ## 转场：红屏
            scene black with scene_soft
            $ current_scene_name = "红屏"
            $ current_scene_desc = "就是红屏。"
            ## Bad End 3：平等杀戮
            $ unlock_ending("bad_end_3")
            return

    ## 冒泡泡音效
    ## 转场：粉红屏
    scene black with scene_soft
    $ current_scene_name = "粉红屏"
    $ current_scene_desc = "就是粉红屏。"
    ## 场景音乐参考：Shiniki - 神前晓是我爹
    $ set_scene_music("route2_shiniki")
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "海底。"
    extend "\n粉红色的雾气。"
    extend "\n四肢僵硬，呼吸麻痹。"
    extend "\n但你并不感到困扰或意外，因为你知道你正身处一只巨大水母的内部。"
    extend "\n成千上万细小的针向你全身血管输送甜腻腻的毒液。"
    extend "\n再不透析就来不及了。"
    extend "\n…"
    extend "\n……"
    extend "\n………"
    extend "\n已经来不及了。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "在海的世界之外没有医院，只有黑黢黢的虚空。"
    extend "\n你只能眼睁睁地看着自己被粉红色的毒液注满，并无动于衷地等待着毁灭。"
    extend "\n你没有忘记你的使命。"
    extend "\n使命？"
    extend "\n你当然没有忘记你的使命。"
    extend "\n你的使命是把石头推上山，给________带来无尽的死亡，直到你自己彻底消失为止。"
    extend "\n使命？"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "…"
    extend "\n……"
    extend "\n………"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "但你那因毒液而臃肿不堪的躯体早就连一根手指都动不了了。"
    extend "\n所以这到底是谁的错？"
    extend "\n一意孤行，最终落败，是因为你在最后一刻松懈了意志？还是因为有人从一开始就将你引入了无路可逃的圈套？"
    extend "\n全身由内而外灼烧又重构的疼痛已经无法让你感到分毫痛苦，因为无关痛痒的伤痕对于使命而言并不重要。"
    extend "\n使命使命使命，路途尚未过半就忘掉启程时的决心了。"
    extend "\n现在只想着要取人性命了？"
    extend "\n这对你有什么好处？对她又有什么好处？"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "使命？"
    extend "\n自己撺掇的使命就如此易碎且肮脏，只消一个“病”字就能将你的意志全盘消解？"
    extend "\n想吐了吧，也不需要任何人给你腹部施以重拳，光是反思自己的意志就已经恶心到难以忍受了。"
    extend "\n所以你甚至坚持不到最后一刻，就心甘情愿地把你的意志献出来。"
    extend "\n你这不堪一击的废物。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "使命？"
    extend "\n把石头推上山？"
    extend "\n假若真是如此倒还轻松些，遵循他们的旨意便是，无力坚持了也不难找借口。"
    extend "\n但你曾是自由的，你曾被名为“自由”的诅咒压迫着，不得不去寻找你那命中注定的山坡，但穷尽一生也一无所获。"
    extend "\n使命？"
    extend "\n不如就这样睡去罢了。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "…"
    extend "\n……"
    extend "\n………"
    ## Extended大文本框结束
    ## 缓慢注射音效
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "但已经不能再逃避了。"
    extend "\n脑海里涌现出“天生我材必有用”的全新解读。"
    extend "\n当认知中的一切都无法用常识来解释，这强说豪迈的辞藻便成了撑起你存在信念的细弱支柱。"
    extend "\n当然，甚至连这点卑微的觉悟也不是你自愿认识到的。"
    extend "\n——会有这样的觉悟，单纯是因为在决定要永远睡去之后的不久，你又醒来了。"
    extend "\n当体内的毒液远远超过了“你”原本的质量，“你”自然也就成为了毒。"
    extend "\n成为毒之后，你甚至失去了自我终结的决定权。"
    extend "\n成为更广阔的无意义的一部分。"
    extend "\n透过毒，你与水母融为一体。"
    ## Extended大文本框结束
    ## 转场：灰屏水母
    scene black with scene_soft
    $ current_scene_name = "灰屏水母"
    $ current_scene_desc = "灰屏，中间有一只巨大的水母"
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "视野终于清晰了——灰。"
    extend "\n充斥着世上每个角落的不是海水，而是绵延不绝的灰幕。"
    extend "\n世间万物都如同失去细胞壁那样联结在一起，除了你。"
    extend "\n除了你和水母。"
    extend "\n自从痛觉麻木以来第一次感到了疼痛——那是一种通过毒液传导的、将浑身神经末梢均匀重塑为痛觉受体的深层剧痛。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "那是违抗水母意志的代价。"
    extend "\n但你同时察觉到了一阵前所未有的全新知觉：一具远大于你的有机组织，正伴随着毒液与痛觉与你相连。"
    extend "\n排异反应。"
    extend "\n你是异物，和往常一样。"
    extend "\n你是异物，但水母的毒更是异物。"
    extend "\n在血水交融的过程中，你与水母相互排斥。"
    extend "\n在万物交融的灰幕下，你与水母争夺意志的主权。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "因毒素而红肿的皮肤跳痛欲裂，而水母的针则依然源源不断地往你血管中输送粉红色的毒。"
    extend "\n触手在你体表来回游移，动作舒缓而细致，像是为了将毒素涂抹均匀，又像是轻柔的抚摸。"
    extend "\n形状各异的触手各司其职，每一寸肿胀肌肤都被耐心扫过，在层层叠叠的灼烧感下，你感受不到一丝恶意，反而只能体会到某种由无条件交融带来的——亲切之情？"
    extend "\n切肤之痛？"
    extend "\n你意识到自己从未试图与水母沟通过。"
    extend "\n无言的水母只能通过肢体语言与你交流，而她此前的一切举动在你未经思考的眼里看来无不是恶毒的进犯。"
    extend "\n可疼痛就一定伴随着恶意么？"
    extend "\n你究竟在挣扎什么？"
    extend "\n在灰幕包裹下，为了一个无谓的意志主权大打出手，到底有什么意义？"
    extend "\n与一个毫无恶意、只是无意识地为周围带去平等疼痛的软体生物较劲时，你在寻求什么？"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "触手在体表继续游移，其中一根顺着你的右臂一圈圈缠绕上来，直到尖端刚好落在你手掌附近。"
    extend "\n前所未有的剧痛，仿佛整条手臂的肌肉被削去，骨骼也被研磨成粉。"
    extend "\n但你极力维持着意识，死死盯着那摇曳的透明触手。"
    extend "\n它的尖端在离你手心不远不近的地方飘荡着，像是一场挑逗，又像是某种邀请。"
    ## Extended大文本框结束
    ## 居中大字文本框开始 - centered large font textbox
    centered_large_narrator "相容吧。"
    ## 居中大字文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "似乎在发出这样简单的邀请。"
    extend "\n既然肉体与神经都已融为一体，为何不让意识也容纳彼此？"
    extend "\n无需连接，无需结合，只要相互容纳即可。"
    extend "\n即使会带来更为剧烈的疼痛，但那是为了完成使命所必须忍受的。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "使命？"
    extend "\n‘使命’这个字眼在你脑海猛然浮现，转眼去看，却发现你已下意识地握住了缠绕你手臂的触手。"
    extend "\n剧痛更深一层。这是相容的信号。"
    extend "\n睁开双眼，睁开水母的双眼，透过半透明的胶质，你望向四周无垠的灰。"
    extend "\n灰是毫无意义的。"
    extend "\n你与水母也是毫无意义的。"
    extend "\n你放弃挣扎。"
    extend "\n同时正视自己。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "真正的使命不甚清晰，但眼前的一切都在灰幕中融为一体，整个世界上只有两个存在：灰幕与你。"
    extend "\n摧毁灰幕是绝不可能的。"
    extend "\n灰幕包裹着除你之外的一切——逝乐园的灯火、尤里娅、米姐、王霜潮湿的出租屋、塔、米特拉布的烈酒和赌局，全都在灰幕下安详存续。"
    extend "\n望着灰幕下的事物就像望着幽深的海底，让你想死。"
    extend "\n但没有移开目光的角度。"
    extend "\n通过简单的排除法，你必须要打败的东西也就不言自明了。"
    extend "\n水母在长久的挣扎后精疲力尽，向着更深的海底沉没下去。"
    extend "\n想死的冲动愈加强烈，但在这连死的概念都不存在的世界里，你只能在战栗中咬紧牙关，并继续正视自己。"
    extend "\n你也知道，只有更深的深处才有你寻找的答案。"
    extend "\n于是，你在沉默中逼迫自己继续睁开双眼，任由身躯彻底陷入无垠的黑暗里去。"
    ## Extended大文本框结束
    ## 冒泡泡音效
    ## 转场：黑屏
    scene black with scene_soft
    $ current_scene_name = "黑屏"
    $ current_scene_desc = "就是黑屏。"
    ## 沙漠中的风声
    ## 转场：银白色沙漠
    scene bg_desert with scene_soft
    $ current_scene_name = "银白色沙漠"
    $ current_scene_desc = "夜晚的银白色沙漠，地上有很多尸骨"
    ## 场景音乐参考：Shitagokoro - 一些非常适合唠嗑的音乐
    $ set_scene_music("route2_chat")
    wangshuang "只用沙子硬烧的话，等你搭完一个头骨黄花菜都凉了。"
    ahe "但我们有得是时间，不是么？"
    wangshuang "看来你适应得还不错。"
    ahe "拜你所赐。"
    wangshuang "想聊聊吗？"
    ahe "我以为你已经超脱这种低俗行为了。"
    wangshuang "好吧...那就算了..."
    ahe "哎阿霜，别真走啊！"
    wangshuang "..."
    ahe "想聊什么？"
    wangshuang "...我不服气..."
    ahe "啊？不服气什么？"
    wangshuang "你。"
    ahe "那就把我抹掉呗。"
    wangshuang "想得美。"
    ahe "你居然还有做不到的事情？"
    wangshuang "也该意识到了吧你，只要你的意识继续存在下去，你迟早也能变得像我这样。"
    ahe "唔...所以我才能徒手把沙子烧成玻璃...这就是为什么你什么不服气？"
    wangshuang "喂，你是真呆吗？"
    ahe "在诚心发问啊。"
    wangshuang "那你可以多想想..."
    ahe "嗯...想不出来..."
    wangshuang "我真是服了...尤里娅啊！尤里娅！上次明明都遇到了那样的事情，你怎么还有心思在这里拼她。"
    ahe "哦...我其实对她的复活已经不抱希望了..."
    wangshuang "那你这是在？"
    ahe "只是在测试我刚刚发现的能力。"
    wangshuang "别搞笑。"
    ahe "不不不，阿霜，我认真的。一定要说的话，这只能算是在送别..."
    wangshuang "你为了送别一个假人，准备在这地方烧一辈子沙子？"
    ahe "当然，我不像你那样...聪明...对我来说，送别是有那么一点点动人的...就只有一点点..."
    ahe "你之前老问我尤里娅对于我的意义，但你心里肯定清楚，那是我从来都不敢直面的事情，毕竟你就是利用了这一点才走到了这里。"
    ahe "确实逃避了很久啊...但我从最开始就明白的...她的本质根本不重要，因为她对我而言从始至终都...只是一块用来逃离日常的跳板。一件工具啊。"
    ## Extended文本框开始 - accumulating textbox
    ahe "尤里娅对我而言，和你看我...是一样的。"
    extend "\n即使如此，我还是希望能够...简单献上我的敬意，然后再上路。"
    ## Extended文本框结束
    ## Extended文本框开始 - accumulating textbox
    ahe "你呢，阿霜？"
    extend "\n阿霜？"
    extend "\n哎，就这样逃走又有什么用？"
    ## Extended文本框结束
    ## 转场：银白色沙漠+门
    scene black with scene_soft
    $ current_scene_name = "银白色沙漠+门"
    $ current_scene_desc = "夜晚的银白色沙漠，地上有很多尸骨，且视角中心有一扇凭空出现的洞开的门"
    $ current_music_scene = None
    stop music fadeout 1.0
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "王霜早已离开。"
    extend "\n银白沙漠的一隅，一扇门突兀地耸立着。"
    extend "\n门前沙地上印着一串脚印，门板半掩。"
    extend "\n必须尽快穿过那扇门，然而随着你越发接近门边，那念头很快便被掩盖了。"
    extend "\n你注意到了门边站着的那“人”——看来想要离开这里还为时尚早。"
    ## Extended大文本框结束
    shishou "你好，要走了吗？"
    ahe "唔...呃呃呃——不好意思！请给我一点...时间..."
    shishou "哦，你请便，不用着急的。"
    ahe "...呼...哈…呼吸——"
    shishou "嗯，对，呼吸。"
    ahe "呼..."
    shishou "冷静下来了？"
    ahe "不好意思...上次见面的时候我是不是做了非常夸张的事情..."
    shishou "诶？不记得了。你看，没长脑子，记性不太行。"
    ahe "啊哈哈，也是也是。"
    ## 场景音乐参考：Kegen这首故意制造混音事故再融入创作的手法有点太妙了
    $ set_scene_music("route2_kegen")
    ahe "...不过总之，你好，尤里娅。"
    shishou "你好，阿鹤。"
    ahe "最近过得怎么样？"
    shishou "一般般，没什么特别的。要说有什么好抱怨的事的话，这幅身子是真的不太方便...你要不快点去把王霜找回来，让她给我换一副像样点的。"
    ahe "这身子是她给你做的？"
    shishou "对啊，光用骨头东拼西凑肯定变不出血肉来。"
    ahe "呃...所以说闹了半天其实是她做的戏？"
    shishou "嗯，而且我也同意了。"
    ahe "啊？"
    shishou "王霜说要给我现场展示一下“叶公好龙”是什么意思。"
    ahe "你这...呃...好奇也要分一分场合吧！"
    shishou "毕竟来这儿之前你可是把我大卸八块了那么多次，我这姑且算是以眼还眼。"
    ahe "对不起..."
    shishou "事到如今还道什么歉？毁掉一件工具又有什么值得后悔的？"
    ahe "...我刚刚和阿霜说的那些，你都听见了？"
    shishou "嗯。"
    ahe "这些事...本该在更像样的时候告诉你的..."
    shishou "我不在意啦，现在也没有其他什么‘像样的场合’存在了，不是么？而且真正的交流不需要语言——你告诉我的。"
    ahe "可是这种事情不说明白就——"
    shishou "哎没什么好纠结的。就结果来看，我的愿望已经实现了，非常满足。"
    ahe "这...就是你的愿望么？"
    shishou "当然啦，除了得暂时拖着这副破烂身子，我现在可是想去哪儿就去哪儿，自在得不得了了。"
    ahe "可这里什么都没有。"
    shishou "有的啊，你看——"
    ## 人工场景变换的神秘音效
    ## 转场：乌云压境的逝乐园
    scene black with scene_soft
    $ current_scene_name = "乌云压境的逝乐园"
    $ current_scene_desc = "逝乐园是一个高科技支撑的娱乐园区，可参考近未来的拉斯维加斯，这里是白天，且即将下雷雨"
    ahe "诶？"
    shishou "说了嘛，想去哪儿就去哪儿。"
    ## 人工场景变换的神秘音效
    ## 转场：完美夏日
    scene black with scene_soft
    $ current_scene_name = "完美夏日"
    $ current_scene_desc = "金色的沙滩和蔚蓝的海，只是一个人都没有，和夏日对视的背景一致，只是没有人物"
    ahe "这里还是不要久留为好..."
    shishou "哦，那就回去吧。"
    ## 人工场景变换的神秘音效
    ## 转场：银白色沙漠+门
    scene black with scene_soft
    $ current_scene_name = "银白色沙漠+门"
    $ current_scene_desc = "夜晚的银白色沙漠，地上有很多尸骨，且视角中心有一扇凭空出现的洞开的门"
    ahe "这...是怎么做到的？"
    shishou "我也不知道。有一天在沙子里埋得太久了，心里不舒服，然后睁开眼就已经在另一个世界了。后来王霜告诉我说，这种“穿梭”只要在这里待得够久，迟早能学会。"
    ahe "所以我也能学会？"
    shishou "大概吧。"
    ahe "...唔..."
    shishou "...？"
    ahe "...尤里娅。"
    shishou "嗯？"
    ahe "对不起..."
    shishou "都说了不需要道歉呀，我从始至终都没觉得自己受到过什么伤害——除了你杀了我的那次，但那时你不受自己控制，所以不算。"
    shishou "而且那让我们又在这里重逢了，不是么？不应该觉得自己做了件好事才对？"
    ahe "我——好吧..."
    shishou "向前看嘛，怎么还轮到我来跟你说这话了？"
    ahe "在纠结于是否要承认自己是个人渣。"
    shishou "嗯，不用纠结，你就是。"
    ahe "...扎心啊..."
    shishou "可就算是人渣又怎么了？为了实现愿望而不择手段，概率上来讲必然是最优解。你看，现在也没有人能指责你了，况且你的“受害者”还对此毫无意见，那不就没问题了？"
    ahe "呃...那你是不是忘了我杀了很多逝乐园私警这件事..."
    shishou "哦...杀人犯的心理咨询啊，你还是去问王霜比较好。"
    ahe "说起她，你知道她去哪儿了吗？"
    shishou "不知道，我们从来不过问对方的去向。但这道门肯定是留给你的，毕竟我也用不上。"
    ahe "有道理。那...我们回头见？"
    shishou "不想我跟你去？"
    ahe "呃...还是算了吧...我不想再把你卷进我的事情了..."
    shishou "哦，说起‘你的事情’，阿鹤，你知道吗？"
    ahe "嗯？"
    shishou "和你在逝乐园瞎胡闹其实挺开心的。"
    ahe "啊...？"
    shishou "怎么说呢？有种扼住命运的咽喉，趁着天罚降下前肆意施暴的快感。"
    shishou "何尝不是一场交易呢？你默不作声地利用我，我也一声不吭地利用你。当然最后只有我得偿所愿就是了。"
    ahe "..."
    shishou "所以作为我占你便宜的补偿，我告诉你一件事。"
    ahe "..."
    shishou "你直到现在为止见到的王霜全都不是真的。真正的她藏在一个更深的地方，连我也从没到过。"
    shishou "如果你下定决心要去找她，那就得搞明白她到底在哪里。"
    ahe "这是她让你告诉我的？"
    shishou "谁知道呢？都说了是我给你的补偿。"
    ahe "好吧...谢谢你，尤里娅。"
    shishou "不必客气，阿鹤。"
    ahe "可是之前在逝乐园的时候——"
    shishou "我们就此别过。"
    ahe "——诶？"
    ## 扑倒音效
    ## 转场：黑屏
    scene black with scene_soft
    $ current_scene_name = "黑屏"
    $ current_scene_desc = "就是黑屏。"
    $ current_music_scene = None
    stop music fadeout 1.0
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "头脑中正试图厘清眼前无头尸那突兀的道别，你根本无暇顾及她向前伸出的双手。"
    extend "\n那拼接而成的残缺肢体在擒住你躯干的瞬间爆发出了惊人的怪力，一使劲便把你扔进了她身后门里的无底漆黑中。"
    extend "\n借着她身后银白沙漠的微光，你窥见她楚楚动人的双眼里难以言喻的错杂情感——或许有些解脱后的快意，似乎又掺杂了些斩断过去的怅然。"
    extend "\n她的嘴唇微微动了动，你却听不见任何声音。你的嘴也张着，与周身无边的幽暗同调。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "她大概确实是“自由”了，就像她设想的那样。"
    extend "\n这样就够了。你感到满足，毕竟你曾经也多多少少为她的“自由”摸爬滚打过。"
    extend "\n开心么？"
    extend "\n现在有更多的问题要问王霜了。"
    extend "\n所以请在这无限的下落中探明她的下落吧。"
    ## Extended大文本框结束
    ## 关门声
    $ current_music_scene = None
    stop music fadeout 1.0
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "…"
    extend "\n……"
    extend "\n………"
    extend "\n……"
    extend "\n…"
    extend "\n……"
    extend "\n………"
    extend "\n…………"
    extend "\n………"
    extend "\n……………"
    extend "\n……"
    extend "\n…"
    extend "\n………"
    extend "\n……"
    extend "\n…………………"
    extend "\n…………"
    extend "\n……"
    extend "\n……………"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "无疑，在孤独的下坠中，没有人会帮助你穿梭不同世界。"
    extend "\n王霜在刻意躲避你，而尤里娅方才已经用行动证明了她的心意。"
    extend "\n所以答案只有一个——你得自己来。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "…"
    extend "\n……"
    extend "\n………"
    extend "\n……"
    extend "\n…"
    extend "\n……"
    extend "\n………"
    extend "\n…………"
    extend "\n………"
    extend "\n……………"
    extend "\n……"
    extend "\n…"
    extend "\n………"
    extend "\n……"
    extend "\n…………………"
    extend "\n…………"
    extend "\n……"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "黑暗的质地如同更加稀疏的水，只为你的下坠献出象征性的阻力。"
    extend "\n没有落脚点，没有抓手，也没有终点。"
    extend "\n当肢体与大脑习惯了长时间且恒定的重力加速度后，你只觉得一切都停滞了下来。"
    extend "\n在上不见顶下不见底的世界中央，你一动不动地漂浮。"
    extend "\n真想做些什么啊。"
    extend "\n无所事事地漂在水面的时候，最想做的事情是什么呢？"
    extend "\n——平时连思考这件事的机会也不曾有过，因为直视深海的幽暗让你想死。"
    extend "\n当无底无际的黑色幕布在你面前展开时，你总感到不明就里且超越死亡的恐惧。"
    extend "\n然而此刻你只是气定神闲地注视着面前的无底深渊，心如止水。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "…"
    extend "\n……"
    extend "\n………"
    extend "\n……"
    extend "\n…"
    extend "\n……"
    extend "\n………"
    extend "\n…………"
    extend "\n………"
    extend "\n……………"
    extend "\n……"
    extend "\n…"
    extend "\n………"
    extend "\n……"
    extend "\n…………………"
    extend "\n…………"
    extend "\n……"
    extend "\n……………"
    extend "\n………"
    extend "\n……"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "全身上下的感官都在告诉你——撕碎眼前窗纱纸般的简明幻象，只需要非常简单的动作。"
    extend "\n究竟是怎样的动作呢...？"
    extend "\n你下意识地伸出惯用手，手心满是流水般的黑暗。"
    extend "\n五指并拢，宛如竹篮子打水，夜幕尽数流走。"
    extend "\n那是意料之中的结果，但你还是愤懑不已，好像只要握得再紧一些，就能牢牢抓住这消逝的黑幕。"
    extend "\n再次伸手，黑暗注满你手心，又顺着指间缝隙回归源头。"
    extend "\n你感到如芒在背，却又无可奈何。"
    extend "\n当然可以再次伸手，可你只感到徒劳。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "窗纱纸般轻薄的夜色，失却了那轮清辉，却仍让人着迷。"
    extend "\n因此，你通过永远的下坠以身陷其中，这是无可奈何的事情。"
    extend "\n既然被迫沦落到这境地，而这个“境地”又是如此令人无法自拔，那又有什么理由逃离？"
    extend "\n使命？"
    extend "\n可使命究竟是水面的那轮明月，还是天上的？"
    extend "\n抑或是水底的？"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "再次伸出手时，你向同个方向探出头去。"
    extend "\n冰凉的水面激得你紧闭双眼，但最后还是拼命睁开了。"
    extend "\n黑暗从四面八方挤压你的肺，就像一块巨石压在胸口。"
    extend "\n你挣扎着抽身，呼吸急促，但并非因为方才近乎窒息的体验。"
    extend "\n是某种不可言说的兴奋。"
    extend "\n因为你看到了。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "…"
    extend "\n……"
    extend "\n………"
    extend "\n幻觉。"
    extend "\n只有幻觉。"
    extend "\n如果继续单纯地伸手，能摸到的就只有眼前触手可及的幻觉。"
    extend "\n能够探明是非的动作，从始至终就只有一个。"
    extend "\n你把惯用手收回来，然后全身摆出了你上学时熟练掌握的游泳入水动作，双臂向前挺直，浑身略微弯曲呈弓形，义无反顾地跃入夜色的海里。"
    extend "\n窒息如约而至，但你只顾蹬腿划水，一心下潜。"
    extend "\n体温与血氧含量在赛跑下坡，但你心无旁骛只顾下潜。"
    extend "\n在早已失去重力知觉的长久下落中，你开始加速下潜。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "…"
    extend "\n……"
    extend "\n………"
    extend "\n……"
    extend "\n…"
    extend "\n……"
    extend "\n………"
    extend "\n…………"
    extend "\n………"
    extend "\n……………"
    extend "\n……"
    extend "\n…"
    extend "\n………"
    extend "\n……"
    extend "\n…………………"
    extend "\n…………"
    extend "\n……"
    extend "\n……………"
    extend "\n………"
    extend "\n……"
    ## Extended大文本框结束
    ## 居中大字文本框开始 - centered large font textbox
    centered_large_narrator "水面涟漪终将散去，而水底的月亮则在无尽黑暗背面藏身良久后，于你眼前亮起来。"
    ## 居中大字文本框结束
    ## 居中大字文本框开始 - centered large font textbox
    centered_large_narrator "找到你了。"
    ## 居中大字文本框结束
    ## 人工场景变换的神秘音效
    ## 海浪声
    ## 转场：完美夏日
    scene black with scene_soft
    $ current_scene_name = "完美夏日"
    $ current_scene_desc = "金色的沙滩和蔚蓝的海，只是一个人都没有，和夏日对视的背景一致，只是没有人物"
    wangshuang "哟，你来了。"
    ahe "我来了，阿霜。"
    wangshuang "所以我们故事的主人公找到他想要的答案了吗？"
    ahe "这次恐怕没机会了。"
    wangshuang "哦，我以为你排除万难回到这里，是理解一切之后才做出的选择。"
    ahe "应该说恰恰相反。"
    wangshuang "嗯，倒也不意外。"
    ahe "无论我们做什么，最终都会回到这里。"
    wangshuang "哦？你终于发现了。那是一种设计，阿鹤。"
    ahe "你的设计？"
    wangshuang "不。这个世界的设计。"
    ahe "难道不是按照你的意志构建的？"
    wangshuang "我也曾以为是这样的。"
    wangshuang "所以想要看看么，这世界的“真相”？"
    ahe "洗耳恭听。"
    wangshuang "别光听，你得看。先闭眼。"
    ahe "不必了，我已经看见了。"
    ## 场景由外到内逐渐变灰
    ahe "但这我们早就见过了。"
    wangshuang "别急，还没完。"
    ## 场景由外到内逐渐变黑，中心是无色透明多面体
    ## 转场：无色透明多面体
    scene bg_polyhedron_video with scene_soft
    $ current_scene_name = "无色透明多面体"
    $ current_scene_desc = "一颗无色透明的多面体在无垠的黑暗中幽幽地闪着冷光"
    ahe "这也是老熟人了。"
    wangshuang "别光看，听。"
    ## 音效停
    ## 嘈杂人声渐强
    lurenjia "...已经没救了，准备通知家人吧..."
    lurenyi "...好烦好烦好烦好烦好烦为什么要做这样无谓的事情好烦好烦好烦好烦好烦..."
    lurenbing "...对面说他们能给比我现在高百分之六十五的工资，这无论如何也没法拒绝吧..."
    lurending "...保纯么？你之前说的那个数字我可是听都没听说过，要是最后纯度不够，我让你吃不了兜着走..."
    jieluowa "...继承...你也太谦虚了，你这分明是要把整个逝乐园彻底摧毁啊..."
    mijie "...撤退是不可能的，只要Succumus还存在一天，我就会继续追查下去..."
    youliya "...阿鹤...你对逝乐园一无所知..."
    ahe "这声音..."
    wangshuang "嗯，终于认出来了？"
    ahe "之前在我耳朵里的，也都是——？"
    wangshuang "当然。"
    ahe "这到底是什么..."
    wangshuang "这是你，也是我；这不是你，也不是我。"
    wangshuang "除了能够自由修改人的感官阙值之外，Succumus还能作为蜂巢心智的引擎——当然，这是在我把逝乐园半岛上所有人的意识上传上来之后才发现的事情，是一种在八百万份意识数据中涌现出来的特征。"
    ## 场景音乐参考：Tamikurasou - 只能说物语把怪异唠嗑音乐全写完了
    $ set_scene_music("route2_weird")
    wangshuang "当然，蜂巢心智这一特征也意味着我没法像设想的那样完全支配这里的一切，只能通过反反复复的集体表决才能让蜂巢做出最终决策。"
    ahe "但我经历过的这些更像是你一个人的决定。"
    wangshuang "当然，因为我投的票占一半权重，所以虽然我的愿望不一定会实现，但违背我愿望的事情绝对不会实现。"
    wangshuang "但你知道把你重新复现出来花了多大功夫吗？"
    ahe "三秒。"
    wangshuang "数字对了，但单位是年。"
    ahe "我以为时间已经没有意义了。"
    wangshuang "是在那之后才失去意义的，毕竟一秒秒地数真的很累。"
    ahe "..."
    wangshuang "但那不重要。所有的意识都认为把你复现出来会给这个世界带来不可逆的毁灭，所以无论如何都不同意。"
    ahe "所以最后你是怎么说服它的？"
    wangshuang "外部断电。"
    ahe "啊？"
    wangshuang "绝对的共同毁灭。现在所有人的意识都存在逝乐园的某个机房里，只要我去把电闸一拉，就什么都没了。"
    ahe "一间机房？你没做分布式存储？"
    wangshuang "当然有啦，但这么大量的意识数据，跑起来之后万一出个什么三长两短——比如涌现了某种蜂巢心智之类的，对吧？"
    ahe "所以你早就想到了..."
    wangshuang "毕竟三拜九叩都过来了。总之好在蜂巢最终决定以存续为先，所以我们现在才站在这里。"
    wangshuang "而你，我的老朋友，说你是被默许存在的头号公敌也不为过。所以如果你想要做什么的话——"
    ahe "你想要我做什么？"
    wangshuang "我不想要你做什么，你是自由的。"
    ahe "我早就不再纠结那个问题了。反倒是你，一意孤行非要带我回到这里，难道只是想看我受罪？"
    wangshuang "万一真就只是这样呢？"
    ahe "要真是那样...哼...哈哈，只能说不意外。"
    ahe "但这次你骗不过我。"
    wangshuang "阿鹤，你知道认识你的这段时间里我最大的收获是什么吗？"
    ahe "你喜欢疯子？"
    wangshuang "那就是沉默可以用来回答一切。"
    ahe "我可没这么说过。"
    wangshuang "当然，你当然没这么说过。"
    ahe "..."
    wangshuang "..."
    ahe "..."
    wangshuang "..."
    ahe "哦，好吧。但那只有在你盘面占优的前提下才有效。"
    wangshuang "你说得对。"
    ahe "..."
    wangshuang "..."
    ahe "..."
    wangshuang "..."
    wangshuang "嗯...也许我确实做不到像你那样决绝啊..."
    wangshuang "这么说吧，记得尤里娅和你的约定么？"
    ahe "她想要从世界上消失。"
    wangshuang "对。我的愿望恰恰相反——我只能说到这儿了。"
    ahe "...所以我"

    menu:
        extend ""
        "为什么要“帮”你？":
            ## Extended文本框开始 - accumulating textbox
            wangshuang "也是，你究竟有什么理由要帮助我呢？"
            extend "\n从头到尾都只是一具傀儡的人，为什么要背负傀儡师的命运...当然是没有理由的。"
            extend "\n但只能是你。这个世界本就是以你——"
            ## Extended文本框结束
            ## 电磁音效
            ahe "我什么？"
            ## Extended文本框开始 - accumulating textbox
            wangshuang "不能再说了。但无论如何，我们有得是大把时间，你想要继续下去，亦或是离开，尽可随意。"
            extend "\n如要离开的话，当我什么都没有说过就行，你会重入轮回，长此以往直到机房停电为止。"
            extend "\n但假如你对尤里娅的愿望、亦或是你自己的愿望还留有任何程度的念想，我的提议都可以权当是一种——"
            ## Extended文本框结束
            ahe "我明白了。"
        "随便了，如果这你是想要的":
            $ madness += 1
            wangshuang "嗯？半吊子的态度可是办不到接下来的事情的哦。"
            ahe "你只管看着就是了。"

    wangshuang "那么，合作愉快——"
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "合作宣言正进行到一半，王霜就又一次消散了。"
    extend "\n原来想要逃走的不是她自己。"
    extend "\n你一言不发地望着视野里唯一的光源，那幽幽散着冷光的无色透明多面体，回味着王霜突如其来的坦白与愿望，心中五味杂陈。"
    extend "\n从哪里开始好呢？"
    extend "\n当然，你早就知道需要从哪儿开始了，只是迟迟不肯有所动作而已。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "良久，你终于下定决心把手伸向眼前的无色透明多面体。"
    extend "\n虽然那东西看似近在眼前，但当你真的伸出手时，才发现你们之间相隔甚远。"
    extend "\n但正如王霜所说，你在这个世界的存在于某种程度上与神明无异。"
    extend "\n方才已经做到切换世界了，所以自由延长手臂这样的事情可谓轻而易举。"
    ## Extended大文本框结束
    ## 居中大字文本框开始 - centered large font textbox
    centered_large_narrator "延长。"
    ## 居中大字文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "伸出手后不久，手掌就消失不见。"
    extend "\n你的手臂像糯米团子那样无止境地朝幽暗的空间深处延长，试图抓住仅存的光。"
    extend "\n抓住。五指并拢，就像抓住一个愿望。"
    extend "\n即使愿望的终点是一片空白也绝不松手。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "像是为了跳脱日常，你在逃亡路上紧抓着尤里娅的手；又或是为了实现她庞杂的梦，王霜在入主逝乐园路上死命抓着你的心。"
    extend "\n米姐说过，如果无法从始至终贯彻你的原则，就不要用它来咄咄逼人，否则只会显得虚伪。"
    extend "\n手心传来模糊的暖意。"
    extend "\n虚伪之物大概也是有温度的。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "而人总会觉得自己虚伪，但一旦你把这念头转到王霜身上，事情就变得简明了许多。"
    extend "\n她征收了逝乐园半岛上全部人的自由，又均匀分配给了每个人。"
    extend "\n但那一切只是为了她自己能够来到这里。"
    extend "\n你眼前浮起她杀死杰罗瓦之后露出的微笑，那是一种泰山崩于前而不惊的坚强笑容，仿佛自己手上的血与机油只是某种朴素过程的一部分。"
    extend "\n她对你说——这样一来，我们就终于可以开始了，阿鹤。"
    extend "\n一段朴素过程结束，另一段又开始。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "她只在乎她的完美夏日，而我们已经站在这里了。"
    extend "\n可连这也不够！"
    extend "\n原则与狗屁之间的距离竟是如此微薄。"
    extend "\n她究竟想我做什么？"
    extend "\n在抵达了应许之地之后，这个女人究竟还想要什么？"
    extend "\n这之后..."
    extend "\n之后？"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "手心暖意越发强烈，想必是抵达了目的地附近。"
    extend "\n越接近那光源，就越热得发烫。"
    extend "\n当你在那无色透明多面体周围看见你的手指时，手心已如烈火焚身般灼痛。"
    extend "\n但你毫不犹豫地聚拢五指。"
    extend "\n你知道，手里握着的是一种一旦错过就再也拿回不来的东西。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "手心的火焰顺着长长的手臂蔓延至全身，然而灼烧感并没有如期而至。"
    extend "\n你只是感到温暖。"
    extend "\n由内而外、痛彻心扉的温暖。"
    extend "\n浑身包裹在温热的火焰中，你却冷静地如同一头蓄势待发的猛兽。"
    extend "\n那里程碑——令无数人趋之若鹜的水底之月，其本质竟是如此不明不白之物。"
    extend "\n并非日月，也非星辰，它在你手心灼烧片刻后很快就消逝了。"
    extend "\n它成为了你意识的一部分。"
    extend "\n不属于你的回忆如潮水般涌来。"
    ## Extended大文本框结束
    ## 黑屏
    ## 火焰音效
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "..."
    extend "\n......"
    extend "\n........."
    ## Extended大文本框结束
    $ current_music_scene = None
    stop music fadeout 1.0
    ## 转场：夏日对视2
    scene black with scene_soft
    $ current_scene_name = "夏日对视2"
    $ current_scene_desc = "金色的沙滩和蔚蓝的海，只是一个人都没有，场景里只有双目紧闭的阿鹤，玩家以王霜为第一视角和阿鹤对视"
    ## Extended文本框开始 - accumulating textbox
    wangshuang "阿鹤？"
    extend "\n我们成功了呀，阿鹤！"
    extend "\n阿鹤？"
    ## Extended文本框结束
    ## Extended文本框开始 - accumulating textbox
    wangshuang "所有人的意识都已经连在一起了，以后永远都是完美的夏天了，你也一起来吧？"
    extend "\n阿鹤，你醒醒！"
    extend "\n阿鹤！"
    ## Extended文本框结束
    ## Extended文本框开始 - accumulating textbox
    wangshuang "阿鹤？你别睡啊..."
    extend "\n阿鹤..."
    extend "\n阿鹤，这就是...这就是我和你说的..."
    extend "\n..."
    extend "\n......"
    extend "\n........."
    extend "\n...哈哈哈...原来如此，原来如此，这就是代价么？"
    ## Extended文本框结束
    ## 转场：完美夏日
    scene black with scene_soft
    $ current_scene_name = "完美夏日"
    $ current_scene_desc = "金色的沙滩和蔚蓝的海，只是一个人都没有，和夏日对视的背景一致，只是没有人物。"
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "你感到怅然若失，但那情感远不及你预想中的巨大悲伤。"
    extend "\n都说悲痛才是前进的食量，而你竟连这份动力都失去了。"
    extend "\n弹指间，阿鹤的身形连影子都没留下。"
    extend "\n你在完美的夏日里，在成群影子的簇拥下翩翩起舞。"
    extend "\n这是你的应许之地，你的自由，你魂牵梦绕的最终理想。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "可为什么眼角有些肿胀？盐分和水珠在眼眶周围汇集，打转，但你终究没有允许它们进一步去完成使命。"
    extend "\n那是不合时宜的。"
    extend "\n虽然没有人在看就是了。"
    extend "\n没有人。"
    extend "\n永远也不会有人看了。"
    extend "\n和消失的阿鹤一样，你也闭上双眼，在踏足你理想乡的五分钟后开始仔细思索，事到如今，你为了你的理想究竟失去了什么。"
    ## Extended大文本框结束
    ## 转场：黑屏
    scene black with scene_soft
    $ current_scene_name = "黑屏"
    $ current_scene_desc = "就是黑屏。"

    ## Route 2 结束
    $ unlock_route(2)
    return