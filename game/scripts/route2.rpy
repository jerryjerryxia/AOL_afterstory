## route2.rpy
## Route 2

label route2_start:

## 二周目：水底捞月

    ## 黑屏
    ## 场景音乐参考：Electric Sea (Buckethead), Padmasana (Buckethead)，DoutokutosetsuShinsou no reijouGaidankousetsu - 物语ost是好文化
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

    ## 大文本框开始
    large_narrator "真他妈无聊啊。"
    ## 大文本框结束
    call screen route_title("水底捞月")
    ## 完美夏日背景，场景里只有王霜和一张桌子，阿鹤第一视角看着盯着他的王霜，参考DDLC最后的莫妮卡
    wangshuang "欢迎回来。"
    ahe "又来？"
    wangshuang "哦？"
    ahe "不好意思...我...来过这里吗...？"
    wangshuang "大概吧。"
    ahe "我感觉...有个熟悉的声音在我耳边一直说个不停，让我去做非常恶毒的事情..."
    wangshuang "它让你做什么？"
    ahe "‘撕碎皮肤，折断骨头，直到一点声音也不留下’。"
    wangshuang "哦。无聊。"
    ahe "我病了吗？"
    wangshuang "还差得远。"
    ahe "那为什么你看起来如此的...悲伤？"
    wangshuang "你又知道了？一有人给你冷屁股，马上就联想到人的创伤了。然后呢？再来一次你那轰轰烈烈的救风尘大冒险？那我还是敬谢不敏。"
    ahe "可这和我没有关系。"
    wangshuang "闭嘴吧。"
    ahe "阿霜。"
    wangshuang "我说闭嘴吧！"
    ahe "究竟为什么要把——"
    wangshuang "我他妈的让你给我闭嘴！"
    ahe "..."
    wangshuang "不要试图怜悯我。你不配，谁都不配。"
    ahe "即使最基本的相互理解也不行么？"
    wangshuang "理解什么？你需要理解的一切都已经装在你脑壳里了，去慢慢理解吧。再见。"
    ahe "阿霜！"
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "丢下残酷的告别后，王霜便如同青烟般消散了。完美的夏日光景里只留下孤零零的你。"
    extend "\n这幅场景也似曾相识——你回想起了某件重要的事情，却又抓不住任何具体的画面。"
    extend "\n只记得你曾做过一个长久而模糊的、关于忍耐与空虚的梦。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "但你决定做些什么。"
    extend "\n你循着回忆里模糊的画面，用手指蜷成小孔，试图透过那微小的空间来窥探钉在天顶的太阳。"
    ## Extended大文本框结束
    ## 白屏
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "强光刺目，你的全身都颤抖着抗议你无意义的自毁行为。"
    extend "\n眼角注满了泪水，眼球如烈火灼烧般压迫着你的视神经。"
    extend "\n瞳孔周围的肌肉正拼尽全力试图收缩，但你强忍着剧痛，在嘶哑的嚎叫中强迫自己继续张目对日。"
    extend "\n直到你看见了——"
    extend "\n火辣的光线丛中心，是一颗熊熊燃烧的火球，给予世间万物以生命的神圣火球。"
    extend "\n而在那火球的中心，你看见了一件似曾相识的事物。"
    ## Extended大文本框结束
    ## 白屏，中心出现无色透明多面体
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "那东西看似球体，却又好似有无数细小的平面，看似无色透明，却又从中散发出数不胜数的光。"
    extend "\n你进一步缩小手指间的空隙，直到视野中只剩下那神秘的多面体。"
    extend "\n随着太阳光被剔除，那多面体所散发出的光线也越发怡人，你觉得那东西几乎变得触手可及了。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "那是你的——那沉寂了一阵的声音又开始作祟。"
    extend "\n一直以来都是你的——见你无动于衷，那声音逐渐提高了音量。"
    extend "\n拿回来吧，伸手就行了，拿回来吧！"
    extend "\n你不明就里，但还是伸出了手。"
    ## Extended大文本框结束
    ## 捂住音效
    ## 黑屏
    wangshuang "别。"
    ahe "阿霜？"
    wangshuang "别随便碰别人的东西。"
    ahe "可我没想碰——"
    wangshuang "不用狡辩了，你做到了，你把我逼回来了，现在你开心了么？"
    ahe "我没有想...我只想知道我到底为什么回到了这里。"
    wangshuang "都是没有意义的，阿鹤。你回或不回到这里，在这里死了或在现实中活着，都是没有意义的，所以不要再试图理解了。存在就够了。"
    ahe "这是你想要的吗？"
    wangshuang "我不在乎。"
    ahe "我认识的阿霜如果听到这样的话，必定会破口大骂回去——"
    wangshuang "狗屁——"
    ahe "——所以为什么你要如此若无其事地说出你绝不会认同的话呢？"
    wangshuang "闭嘴吧阿鹤...这地方和常识与记忆没有任何关联，所以不要再用你“所熟知”的那套狗屁来烦我。"
    ahe ""

    menu:
        extend ""
        "可是——":
            wangshuang "我！说！闭！嘴！"
            ## 电视机关闭音效
            ## 黑屏
            ## Bad End 2：好奇害死猫
            $ unlock_ending("bad_end_2")
            return
        "嗯...":
            wangshuang "明白了就好。接下来你需要做的，就是在这个完美的夏日里继续存在下去，不要问问题，不要到处乱走，不要莫名其妙去死。如果你真的想重新开始的话，闭上眼睛就行了。明白了吗？"
            ahe "嗯..."
            wangshuang "很好。那么再见。"
            ahe "ke——"
            wangshuang "嘘——"
            ahe "..."
            "你心里有千言万语想要倾泻，然而在这完美且孤寂的明丽夏日里，沟通是高于一切的难题。"
            "时间早就没有意义了——你依稀记得阿霜也这样说过，如今则实实在在地体会到了这句话的重量。"
            "太阳永远高挂在天顶，完美的蔚蓝天空遥远而平整，白金色沙滩上的沙砾们不知去向地腾挪着，偶尔被洁白的海浪裹挟到远处，偶尔又在巡游后回到原地。"
            "眼前万物无不最终回到原地，包括双眼布满血丝的你。"
            "你一言不发地观察眼前令人绝望的动态平衡，意识到即使聪慧如阿霜，大概也找不出破局或是解脱的方法。"
            "一些模糊的冲动在你心里逐渐成型，一如自深海逐渐上浮的泡沫。"
            "但过量的思索终究使你劳累。某一刹那，困意压过了一切思绪，于是你若无其事地闭上双眼——"
            ## 电视机关闭音效
            ## 黑屏
            ## 水底冒泡泡音效

    ## 场景音乐风格参考：怎么说呢...虽然台词可能对抗感比较强，但这种场景还是得要一些 lo-fi 小调啊...Moonlit Reverie - 好lofi，Hoyoku, Sutekimeppou - 这几首物语的 ost 也很有内味儿嗷
    $ set_scene_music("route2_lofi")
    ## 一家疑似餐厅的背景，又是王霜和阿鹤面对面坐着
    ahe "你好，我要这个团子。"
    wangshuang "嗯，你很懂嘛。"
    ahe "总觉得...什么时候来过这里。"
    wangshuang "确实像是你会背着我偷偷来的地方——我也要那团子吧。"
    ahe "上次你明明也在。"
    wangshuang "哎阿鹤，病我已经给你治好了，不要再在这儿假装复发了啊，没必要。"
    ahe "这店的团子是加KAS的。"
    wangshuang "对，看来你确实没少来嘛。"
    ahe "所以你也来过！"
    wangshuang "当然，但肯定没和你一起过。"
    ahe "...很奇怪..."
    wangshuang "这有什么好纠结的，都来这店里了还在考究认知？"
    ahe "好吧..."
    wangshuang "真就跟临死前还非要射一发似的，你们男人都这样的吗？"
    ahe "那是假新闻。"
    wangshuang "哎哟，还杠上了？嗑之前一定要先美其名曰‘搞明白药理学’，做之前非要聊大半天文学艺术，是不是你？"
    ahe "呃..."
    wangshuang "说话。"
    ahe "好吧...是我。"
    wangshuang "哈哈哈哈真听话，我就喜欢你这点。"
    ahe "话说，你手里那东西是什么？"
    wangshuang "这个啊，是你用不来的东西。"
    ahe "哦，这样。"
    wangshuang "你倒是再好奇一点啊！"
    ahe "确实没有那么好奇..."
    wangshuang "那你还问！"
    ahe "所以你干嘛用的？"
    wangshuang "我可以破例给你尝尝。"
    ahe "是用来吃的？"
    wangshuang "算是吧。用处有很多，但如果想要直接明白它的用途，吃下去是见效最快的。"
    ahe "你不会是想把我迷晕然后留我结账吧？"
    wangshuang "我要真这么想的话你早就不省人事了。所以怎么样，要不要趁团子上来之前试试？空腹吃生效快。"
    ahe "吃了会怎么样？"
    wangshuang "那不好说。和KAS差不多，一千个人吃了会有一万种效果。"
    ahe "...那我试试吧。"
    wangshuang "给，拿着。"
    ## Extended文本框开始 - accumulating textbox
    "你接过王霜手里那无色透明多面体。"
    extend "\n它轻若无物，看似是固体，摸起来却又有介于凝胶和麻薯之间的质感，躺在你手心，冰冰凉的。"
    ## Extended文本框结束
    ## Extended文本框开始 - accumulating textbox
    "不要乱吃王霜给的东西！"
    ## Extended文本框结束
    ## Extended文本框开始 - accumulating textbox
    "忽略无关紧要的想法，你若无其事地把手心里的事物送进嘴里。"
    extend "\n入口时的冰凉口感转瞬即逝，随即传来细微的灼烧感，比辣味更微妙些，像一轮排列整齐的钝铁钉轻轻滚过口腔粘膜。"
    extend "\n轻轻咀嚼几下，口感沙沙的，略带弹性，但不粘牙。"
    ## Extended文本框结束
    ## Extended文本框开始 - accumulating textbox
    "当你正欲下咽时，舌根传来一阵淡淡的苦味，苦味散去后又留下一丝细微的回甘。"
    extend "\n这味道——"
    ## Extended文本框结束

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
    wangshuang "冷静一下，听着——除了五年前你刚来我这儿看病那会儿，之后你就再也没有幻视过了，现在又幻视可不是什么好兆头。"
    extend "\n你先在这儿坐好，我让药房给我送点药来，马上就能到。"
    ## Extended文本框结束
    ahe "阿霜，我真的——"
    wangshuang "相信我，阿鹤，你是我们科室唯一彻底康复的病人，我是绝对不会让你复发的。"
    ahe "阿霜，你听我说——"
    wangshuang "阿鹤！阿鹤你先听我说！你的病之前没有人见过，所以康复疗程我们也只能摸着石头过河，现在出了问题我真的...【“伪”字背景闪过】真的非常抱歉！但我肯定会帮你控制住的，我保证！"
    ahe "阿霜，刚才你给我吃了你手里拿着的无色透明的东西，你还记得这件事吗？"
    wangshuang "阿鹤，没关系的，吃了什么都不会有事的，请你稍安勿躁几分钟，让我【“伪”字背景闪过】做我该做的工作吧，你是我的病人...？我..."
    ahe "...我要走了。"
    wangshuang "阿鹤！你当然可以走，但能等吃了药再走吗？为了你，也为了我【“伪”字背景闪过】，请你让我继续为你治疗...可以吗？"
    ahe "搞什么啊..."
    ## 虚弱
    wangshuang "...啊？"
    ahe "到底在搞什么啊？【“杀”字背景闪过】之前陪你演戏是因为我别无选择，但现在这样恶心我对你又有什么好处？"
    ahe "王霜，我的老朋友，你要是真的想要做什么或者把我怎么样，【“杀”字背景闪过】直接告诉我就行了，或者直接把我变成你想要的样子也可以，能麻烦【“杀”字背景闪过】你不要在这里玩弄人心吗？"
    ## “杀了她”背景
    ahe "..."
    wangshuang "...不要担心，药马上就到了，我一定会帮助你——"
    ## 扑倒音效
    ## 扼颈音效
    ## 红屏
    ## 场景音乐参考：Sensou - 众所周知物语是战斗番，Gehou - 这个感觉也不错
    $ set_scene_music("route2_battle")
    ahe "这就是你想要的？"
    wangshuang "呃——啊——呃呃呃呃——"
    ahe "你是觉得我还没杀够，还是自己没死够，想让我来帮你自杀着玩？"
    wangshuang "我——呃呃...请松——手——啊啊呃呃。"
    ahe "对！继续挣扎！死人！折断骨头！碾碎内脏！放干血！都是你最喜欢的！那才是你的治疗，阿霜——你在看吧！喜欢我草菅人命的样子么？"
    ## 红屏，血
    wangshuang "唔...啊...啊啊啊啊啊啊——"
    ahe "指甲也要拔下来，牙齿要敲碎，每一根肋骨都要折断，对吧？都是你告诉我的，遇到虚伪的东西就要像这样把它们碾成渣。"
    wangshuang "呃..."
    ahe "死吧！死吧！死吧！给我去死吧！滚出去！永远不要再出现在我面前！滚！"
    ## 红屏，更多血
    wangshuang "..."
    "…"
    "……"
    "………"
    ahe "阿霜？"
    "…"
    ahe "阿霜，你在吗？"
    "……"
    ahe "阿霜，我按照你说的那样，把假的东西彻底毁掉了。"
    "………"
    ahe "阿霜，所以你可以回来了吧？我已经做到了，全都按你说的做到了，所以你回来吧...？"
    ahe "..."
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "或许是因为难以忍受你非人的暴行，其他食客与店员在你不注意时都已经纷纷离场。空无一人的店里，你在一张空空如也的桌子前独坐。"
    extend "\n当然还有一具血肉模糊的尸体陪伴你。"
    extend "\n你呆望着你精心准备的杰作，心中病态的成就感随着时间逐渐消散。"
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
    ## 一家疑似餐厅的背景，但对面没有任何人
    wangshuang_unknown "阿鹤？"
    "听见背后人声，早些时候肆意膨胀的不明情绪已经泾渭分明地裂成了两股，但此刻你只有心思去感知其中之一——"

    menu:
        extend ""
        "深入骨髓的恐惧":
            ## 正常的王霜站在阿鹤身后
            ahe "阿霜...我想...走了..."
            wangshuang "玩得还开心？"
            ahe "一点也不..."
            wangshuang "但见到正经行医的王霜，不觉得这是一种新奇的体验吗？虽然最后无论如何都要杀掉，确实很可惜就是了。"
            ahe "让我...走..."
            wangshuang "行啊，我们走，但你知道你要去哪里吗？"
            ahe "随便...让我走..."
            wangshuang "有点主见啊，主见！反正这里做什么都不会有后果，像之前在逝乐园里那样畏畏缩缩地活着多没意思！告诉我吧，你想要什么？"
            ahe "我...只要离开...就行..."
            wangshuang "啊你就是这点让人觉得很无聊。剧本不是让你跟着走的啊！"
            wangshuang "撕了也行，揉成一团也行。结果你他妈就在这儿一字一句地念稿子。哎...随你便吧。那就这样继续下去吧..."
            ## 电视关机音效
            ## 黑屏
        "如沐春风的安详":
            ## 血肉模糊尸体王霜站在阿鹤身后
            "哈哈哈哈哈哈哈哈当然如此！这有什么可意外的呢，对吧，阿霜？如果这是你的愿望，那我当然全盘接受。"
            "除了全盘接受之外我还有什么选择呢？"
            "如果你想要反反复复地去死，那我就一次又一次地杀了你，直到你厌倦为止。"
            "如果你永远不会厌倦，那我们就永远继续下去。"
            "不管你变成什么模样，不管你身藏何处，我会找到你，用你教我的方法送你上路。"
            "如果这就是你将意识交还于我的目的，那我自然不会有任何多余的问题，我会接受我的使命。"
            "使命——哈哈哈哈真就他妈的总是使命！扭扭捏捏半天不愿意说明白，搞到最后还不是只要我演好一个角色而已？"
            "无聊啊。"
            "真他妈的无聊！"
            "天天在这儿骂无聊来无聊去的，搞到最后还不是自己是最无聊的那个？"
            "那就去死。"
            "用你最熟悉的方式去死。"
            "直到你不再无聊为止。"
            "所以说，阿霜，你准备好了么？"
            ## 红屏
            ## Bad End 3：平等杀戮
            $ unlock_ending("bad_end_3")
            return

    ## 冒泡泡音效
    ## 粉红屏
    ## 场景音乐参考：Shiniki - 神前晓是我爹
    $ set_scene_music("route2_shiniki")
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "海底。"
    extend "\n粉红色的雾气。"
    extend "\n四肢僵硬，呼吸麻痹。"
    extend "\n但你并不感到困扰或意外，因为你知道你正身处一只巨大水母的内部。"
    extend "\n成千上万细小的针向你全身血管输送甜腻腻的毒液。"
    extend "\n再不透析就来不及了。"
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
    extend "\n可悲可笑。"
    extend "\n所以你甚至坚持不到最后一刻，就心甘情愿地把你的意志献出来了。"
    extend "\n你这不堪一击的废物。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "使命？"
    extend "\n把石头推上山？"
    extend "\n假若真是如此倒还轻松些，遵循他们的旨意便是，无力坚持了也不难找借口。"
    extend "\n但你曾是自由的，你曾被名为“自由”的诅咒压迫着，在寻找你命中注定的山坡的路上干渴而死了。"
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
    large_narrator "只是逃避已经不再是可选项了。"
    extend "\n脑海里涌现出“天生我材必有用”的全新解读。"
    extend "\n当认知中的一切都已无法再用常识来解释，这强说豪迈的辞藻便成了撑起你存在信念的细弱支柱。"
    extend "\n当然，甚至连这点卑微的觉悟也不是你自愿认识到的。"
    extend "\n会这么想，单纯是因为在决定要永远睡去之后的不久，你又醒来了。"
    extend "\n当体内的毒液量远远超过了“你”原本的质量，“你”自然也就成为了毒。"
    extend "\n成为了毒之后，你手中甚至连自我终结的决定权也不复存在了。"
    extend "\n透过毒，你与水母融为一体。"
    ## Extended大文本框结束
    ## 灰屏，水母
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "视野终于清晰了——灰。"
    extend "\n充斥着世界上每一个角落的，不是海水，而是绵延不绝的灰幕。"
    extend "\n世间万物都如同失去细胞壁那样联结在一起，除了你。"
    extend "\n除了你和水母。"
    extend "\n痛觉早就麻木的你，长久以来第一次感到了疼痛——那是一种通过毒液传导的、将浑身神经末梢全部重塑为痛觉受体的深层剧痛。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "那是违抗水母意志的代价。"
    extend "\n但你同时察觉到了一种前所未有的全新知觉：一具远大于你的有机组织，正伴随着痛觉与你的意识相连。"
    extend "\n排异反应。"
    extend "\n你是异物，和往常一样。"
    extend "\n你是异物，但水母的毒更是异物。"
    extend "\n在万物交融的灰幕下，你与水母争夺意志的主权。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "因毒素而红肿的皮肤跳痛欲裂，而水母的针仍旧源源不断地往你血管中供给着粉红色的毒。"
    extend "\n触手在你体表来回游移，像是为了将毒素涂满，又像是在轻柔地抚摸你的肌肤。"
    extend "\n你意识到自己从未试图与水母沟通过。无言的水母只能通过肢体语言与你交互，而她此前的一切举动在你未经思考的眼里看来都是恶毒的进犯。"
    extend "\n可带来疼痛的，就一定是敌人么？你究竟在挣扎什么？"
    extend "\n在灰幕包裹下，为了一个无谓的意志大打出手，到底有什么意义？"
    extend "\n与一个毫无恶意、只是无意识地为周围带去平等疼痛的软体生物较劲时，你在寻求什么？"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "触手在你体表继续游移，其中一根顺着你的手臂一圈圈缠绕上来，直到尖端刚好落在你手掌附近。你感到前所未有的剧痛，仿佛整条手臂的肌肉被削去，骨骼也粉碎了。但你极力维持着意识，死死盯着那摇曳的透明触手。"
    extend "\n它的尖端在离你手心不远不近的地方飘荡着，像是一场挑逗，又像是某种邀请。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "相容吧。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "似乎在发出这样简单的邀请。"
    extend "\n既然肉体与神经都已融为一体，为何不让意识也容纳彼此？"
    extend "\n无需连接，无需结合，只要相互容纳即可。"
    extend "\n即使会有更剧烈的疼痛，但那是为了完成使命所必须忍受的。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "使命？"
    extend "\n‘使命’这个字眼在你脑海猛然浮现，转眼去看，却发现你已下意识地握住了缠绕你手臂的触手。"
    extend "\n剧痛更深了一层。这是彻底相容的信号。"
    extend "\n睁开双眼，睁开水母的双眼，透过半透明的胶质，你望着四周无垠的灰。"
    extend "\n灰是毫无意义的。"
    extend "\n你与水母也是毫无意义的。"
    extend "\n你放弃挣扎。"
    extend "\n同时正视自己。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "真正的使命不甚清晰，但眼前的一切都在灰幕中融为一体，整个世界里只有两个存在：灰幕与你。彻底摧毁灰幕是绝对不可能的，而必须你要打败的东西也就不言自明了。"
    extend "\n水母在长久的挣扎后精疲力尽，向着更深的海底沉没下去。"
    extend "\n但你丝毫没有感到惊慌，因为你知道只有更深的深处才有你寻找的答案。"
    extend "\n于是，你在沉默中闭上双眼，任由身躯彻底陷入无垠的黑暗里去。"
    ## Extended大文本框结束
    ## 冒泡泡音效
    ## 黑屏
    ## 沙漠中的风声
    ## 银白色沙漠
    ## 场景音乐参考：Shitagokoro - 一些非常适合唠嗑的音乐
    $ set_scene_music("route2_chat")
    wangshuang "只用沙子硬烧的话，等你搭完一个头骨黄花菜都凉了。"
    ahe "但我们有得是时间，不是么？"
    wangshuang "看来你适应得还不错嘛。"
    ahe "拜你所赐。"
    wangshuang "想和我聊聊吗，关于她对你的意义。"
    ahe "我以为你早就超脱“意义”这个低俗概念了。"
    wangshuang "但你还没有，而且你还在死命坚持，这让我有些..."
    ahe "好奇？"
    wangshuang "不，敬仰。"
    ahe "可你才是这里的神。"
    wangshuang "我们都是能够认识到自己存在的意识，所以本质上是没有区别的。"
    ahe "唔。所以这就是为什么我能把沙子烧成玻璃。"
    wangshuang "而你宁愿费尽心思给她搭一个一触即碎的玻璃头骨，也一定要带她回来——"
    ahe "带她回来？我没准备带她回来。"
    wangshuang "那你这是在？"
    ahe "只是在兴趣使然地行使我刚刚发现的力量罢了。"
    wangshuang "哦，所以你也放弃了。"
    ahe "不，阿霜，我只是在模仿你，摧毁一切，修补完整，再给它戴上一顶堂而皇之的水晶冠，然后重新上路。"
    wangshuang "我可不——"
    ## Extended文本框开始 - accumulating textbox
    ahe "我不像你那样聪明而无情，只是一个善于随波逐流的无名之辈，也就想偶尔跳出日常，痛快地闹一通，这样就够了。"
    extend "\n尤里娅，她的本质完全不重要，因为她对我而言从始至终都只是用来跳脱日常的跳板。一件工具，仅此而已。"
    extend "\n这件事我曾经逃避了很久，但事到如今逃避已经没有意义了。"
    ## Extended文本框结束
    ## Extended文本框开始 - accumulating textbox
    ahe "因此尤里娅之于我，和我对于你是毫无二致的。"
    extend "\n所以此刻我别无他意，只是想把她摆放得整整齐齐、漂漂亮亮的，就像埋葬一件好用的工具那样献上我的敬意，然后重新上路。"
    ## Extended文本框结束
    ## Extended文本框开始 - accumulating textbox
    ahe "所以你会怎么选择，阿霜？"
    extend "\n阿霜？"
    extend "\n哎，逃走又有什么用？"
    ## Extended文本框结束
    ## 银白色沙漠，门
    stop music fadeout 1.0
    ## Extended文本框开始 - accumulating textbox
    "眼前沉默的王霜烟消云散。"
    extend "\n银白沙漠的一隅，一扇门突兀地耸立着。"
    extend "\n门前沙地上印着一串脚印，门板半掩。"
    ## Extended文本框结束
    ## Extended文本框开始 - accumulating textbox
    "她无疑是通过这扇门离开了。"
    extend "\n但你也很快注意到了门边站着的那“人”，看来想要离开还为时尚早。"
    ## Extended文本框结束
    ahe "唔...呃呃呃——不好意思！给我一点...时间..."
    shishou "哦，你请便。"
    ahe "...呼...哈…呼吸——"
    shishou "嗯，对，呼吸。"
    ahe "呼..."
    shishou "冷静了？"
    ahe "不好意思...上次见面的时候我是不是做了更夸张的事情..."
    shishou "诶？不记得了。你看，没长脑子，记性不太行。"
    ## 场景音乐参考：Kegen这首故意制造混音事故再融入创作的手法有点太妙了
    $ set_scene_music("route2_kegen")
    ahe "啊...哈哈...也是...不过总之，你好，尤里娅。"
    shishou "你好，阿鹤。"
    ahe "最近过得怎么样？"
    shishou "一般般咯，没什么特别的，就是这幅身子不太方便...你要不快点去把王霜找回来，让她给我换一副像样点的。"
    ahe "这身子是她给你做的？"
    shishou "对啊，光用骨头肯定是变不出这些血肉的。"
    ahe "呃...所以说闹了半天其实是她做的戏？"
    shishou "我也同意了。"
    ahe "啊？"
    shishou "王霜说要给我现场展示一下“叶公好龙”是什么意思。"
    ahe "你这...呃...好奇也要分一分场合吧！"
    shishou "毕竟来这儿之前你可是把我大卸八块了那么多次，我们姑且算是以眼还眼。"
    ahe "对不起..."
    shishou "事到如今还道什么歉？毁掉一件工具又有什么值得悔恨的？"
    ahe "...我刚刚和阿霜说的那些，你都听见了？"
    shishou "嗯。"
    ahe "这些事...本该在更像样的场合下告诉你的..."
    shishou "我不在意。真正的交流不需要语言——你告诉我的。"
    ahe "可是这种事情不说明白就——"
    shishou "就结果来看，我的愿望已经实现了，所以没什么可抱怨的。"
    ahe "这...就是你的愿望么？"
    shishou "当然啦，除了得暂时拖着这副破烂身子，我现在可是想去哪儿就去哪儿，自在得不得了了。"
    ahe "可这里什么都没有。"
    shishou "有的啊，你看——"
    ## 人工场景变换的神秘音效
    ## 逝乐园
    ahe "诶？"
    shishou "说了嘛，想去哪儿就去哪儿。"
    ## 人工场景变换的神秘音效
    ## 完美夏日
    ahe "这里还是不要久留为好..."
    shishou "哦，那就回去吧。"
    ## 人工场景变换的神秘音效
    ## 银白色沙漠，门
    ahe "这...是怎么做到的？"
    shishou "我也不知道。有一天在沙子里埋得太久了，心里不舒服，然后睁开眼就已经在另一个世界了。后来王霜说，只要在这里待得够久，迟早会学会的。"
    ahe "那我是不是也能学会？"
    shishou "大概吧。"
    ahe "尤里娅。"
    shishou "嗯？"
    ahe "对不起..."
    shishou "都说了，你的道歉对我而言是没有意义的，因为我从始至终就没有觉得自己受到过伤害——除了你杀了我的那次，当然那时你也不受自己控制，所以不算。"
    shishou "而且那间接导致我们在这里重逢了，不是么？否则如今的一切都不会发生。"
    ahe "我——明白了。"
    shishou "向前看嘛，怎么还轮到我来跟你说这句话了？"
    ahe "纠结于觉得自己是个人渣。"
    shishou "嗯，不用纠结，你就是。"
    ahe "呃...扎心啊..."
    shishou "可就算是人渣又怎么了？为了实现愿望不择手段，算法上来讲必然是更接近最优解的。况且因你‘不择手段’而导致的“受害者”对此毫无意见，那不就没问题了？"
    ahe "你是不是忘了我杀了很多逝乐园私警这件事..."
    shishou "哦...杀人咨询不是我的强项，还是之后去问王霜比较好。"
    ahe "说起她，你知道她去哪儿了吗？"
    shishou "不知道，我们从来不过问对方的去向。但这道门肯定是留给你的，毕竟我也用不上。"
    ahe "有道理。那...我们回头见？"
    shishou "不想我跟你去？"
    ahe "还是算了。"
    shishou "阿鹤，你知道吗？"
    ahe "嗯？"
    shishou "和你在逝乐园瞎胡闹其实挺开心的。"
    ahe "啊..."
    shishou "怎么说呢？有种扼住命运的咽喉，趁着天罚降下前肆意施暴的快感。"
    shishou "这何尝不是一场交易呢？你默不作声地利用我，我也一声不吭地利用你。而只有我最后得偿所愿，彻底地在现实中消失了。"
    shishou "所以作为我占你便宜的补偿，我告诉你一件事。"
    ahe "...我听着呢。"
    shishou "你到现在为止见到的王霜都不是真的。真正的她藏在一个更深的地方，连我也到不了。"
    shishou "如果你下定决心要去找她，那就得搞明白她到底在哪儿。"
    ahe "这是她让你告诉我的？"
    shishou "谁知道呢？都说了是我给你的补偿。"
    ahe "谢谢你，尤里娅。"
    shishou "不必客气，阿鹤。我们就此别过。"
    ahe "诶——？"
    ## 推搡音效
    ## 黑屏
    stop music fadeout 1.0
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "你正试图厘清眼前无头尸最后那句意义不明的言语，根本无暇顾及她向前伸出的双手。"
    extend "\n她那拼接而成的残缺肢体在接触到你躯干的瞬间爆发出了出人意料的怪力，仅一使劲就把你推进了身后门外的无底漆黑中。"
    extend "\n借着她身后银白沙漠里的微光，你看见她楚楚动人的双眼里难以形容的错杂情感——或许有些解脱后的快意，似乎又掺杂了些斩断过去的怅然。她的嘴唇微微动了动，你却听不见任何声音。你的嘴也张着，与周身无边的幽暗一同沉寂。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "她大概确实是“自由”了，就像她设想的那样。"
    extend "\n因此，这场无止境的下坠大抵就是你们之间最体面的离别？毕竟你曾经也多多少少为她的自由摸爬滚打过。"
    extend "\n开心么？"
    extend "\n有更多的问题要问王霜了。"
    extend "\n所以请在这无限的下坠中寻找她的下落吧。"
    ## Extended大文本框结束
    ## 关门声
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
    extend "\n………"
    extend "\n……"
    extend "\n…"
    extend "\n………………………"
    extend "\n…………………"
    extend "\n……"
    extend "\n…"
    ## Extended大文本框结束
    ## 人工场景变换的神秘音效
    ## 海浪声
    ## 完美夏日场景
    wangshuang "哟。你来了。"
    ahe "我来了，阿霜。"
    wangshuang "所以我们故事的主人公找到他想要的答案了吗？"
    ahe "这次恐怕没机会了。"
    wangshuang "哦。所以又要放弃。"
    ahe "应该说，又要暂时蛰伏了。"
    wangshuang "花言巧语。"
    ahe "因为无论我们做什么，最终都会回到这里。"
    wangshuang "那是一种设计，阿鹤。"
    ahe "你的设计？"
    wangshuang "不。这个世界的设计。"
    ahe "这个世界难道不是按照你的意志构建的？"
    wangshuang "我也曾以为是这样的。"
    wangshuang "所以想要看看么，这世界的“真相”？"
    ahe "洗耳恭听。"
    wangshuang "别光听，你得看。先闭眼。"
    ahe "不必了，我已经看见了。"
    ## 场景由外到内逐渐变灰
    ahe "但这我们早就见过了。"
    wangshuang "别急，还没完。"
    ## 场景由外到内逐渐变黑，中心是无色透明多面体
    ahe "这也是老熟人了。"
    wangshuang "别光看，听。"
    ## 音效停
    ## 嘈杂人声渐强
    ## Extended文本框开始 - accumulating textbox
    lurenjia "...已经没救了，准备通知家人吧..."
    extend "\n...好烦好烦好烦好烦好烦为什么要做这样无谓的事情好烦好烦好烦好烦好烦..."
    ## Extended文本框结束
    ## Extended文本框开始 - accumulating textbox
    lurenbing "...对面说他们能给比我现在高百分之六十五的工资，这无论如何也没法拒绝吧..."
    extend "\n...保纯么？你之前说的那个数字我可是听都没听说过，要是最后纯度不够，我让你吃不了兜着走..."
    ## Extended文本框结束
    ## Extended文本框开始 - accumulating textbox
    jieluowa "...继承...你也太谦虚了，你这分明是要把整个逝乐园彻底摧毁啊..."
    extend "\n...撤退是不可能的，只要Succumus还存在一天，我就会继续追查下去..."
    extend "\n...阿鹤...你对逝乐园一无所知..."
    ## Extended文本框结束
    ahe "这是——？"
    wangshuang "这是你，也是我；这不是你，也不是我。"
    wangshuang "除了能够自由修改人的感官阙值之外，Succumus还能作为蜂巢心智的引擎——当然，这是在我把逝乐园半岛上所有人的意识上传到云端之后才发现的事情，是一种在八百万份意识数据中涌现出来的特征。"
    ## 场景音乐参考：Tamikurasou - 只能说物语把怪异唠嗑音乐全写完了
    $ set_scene_music("route2_weird")
    wangshuang "当然，蜂巢心智这一特征也意味着我没法像我设想的那样绝对支配这里的一切，只能通过反反复复的集体表决才能让蜂巢做出最终决策。"
    ahe "但我经历过的这些，都像是你一个人的决定。"
    wangshuang "当然，因为我的意志在所有决定中占一半权重，所以虽然我的愿望不一定会实现，但违背我愿望的事情绝对不会实现。"
    wangshuang "但你知道把你重新复现出来花了多大功夫吗？"
    ahe "三秒。"
    wangshuang "数字猜对了，但单位是年。"
    ahe "我以为时间已经没有意义了。"
    wangshuang "是在那之后才失去意义的，毕竟一秒秒地数真的很累。"
    ahe "..."
    wangshuang "但那不重要。所有的意识都认为把你复现出来会给这个世界带来不可逆的毁灭，所以无论如何都不同意。"
    ahe "所以最后你是怎么说服它的？"
    wangshuang "外部断电。"
    ahe "啊？"
    wangshuang "绝对的共同毁灭，现在所有人的意识都存在逝乐园的某个机房里，一旦拉闸就什么都没了。"
    ahe "一间机房？你没做分布式存储？"
    wangshuang "我当然有想过要分布存，但这么大量的意识数据，跑起来之后万一出个什么三长两短——比如涌现了某种蜂巢心智之类的，对吧？"
    ahe "所以你早就想到了..."
    wangshuang "毕竟三拜九叩都过来了。总之好在蜂巢最终决定以存续为先，所以我们现在才站在这里。"
    wangshuang "而你，我的老朋友，现在是整个蜂巢中最特异的个体，一举一动都会受到密切关注，任何出格行为都会立刻遭到排异反应，所以如果你想要做什么的话——"
    ahe "所以你想要我做什么？"
    wangshuang "我不想要你做什么，你是自由的。"
    ahe "我早就不再纠结那个问题了。反倒是你，一意孤行非要带我回到这里，难道只是想看我受罪？"
    wangshuang "万一真就仅此而已？"
    ahe "要真是那样...哼...哈哈，只能说也不意外。"
    wangshuang "记得尤里娅和你的约定么？"
    ahe "她想要消失。"
    wangshuang "我的愿望恰恰相反——我只能说到这儿了。"
    ahe "...我"

    menu:
        extend ""
        "为什么要“帮”你？":
            ## Extended文本框开始
            wangshuang "也是，你究竟有什么理由要帮助我呢？"
            wangshuang "从头到尾都只是一具傀儡的人，为什么要背负傀儡师的命运...当然是没有理由的。"
            wangshuang "但只能是你。这个世界本就是以你——"
            ## Extended文本框结束
            ## 电磁音效
            ahe "我什么？"
            ## Extended文本框开始
            wangshuang "不能再说了。但无论如何，我们有得是大把时间，你想要继续下去，亦或是离开，尽可随意。如要离开的话，当我什么都没有说过就行，你会重入轮回，长此以往直到时间磨灭。"
            "但假如你对尤里娅的愿望、亦或是你自己的愿望还留有任何程度的念想，我的提议都可以权当是一种——"
            ## Extended文本框结束
            ahe "我明白了。"
        "随便了，如果这你是想要的":
            $ madness += 1
            wangshuang "嗯？半吊子的态度可是办不到接下来的事情的哦。"
            ahe "你只管看着就是了。"

    wangshuang "那么，合作愉快..."
    stop music fadeout 1.0
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "留下轻快的合作宣言之后，王霜再次消散了。"
    extend "\n仿佛蜂巢不愿她再和你多说哪怕一句话。"
    extend "\n你一言不发地望着视野里唯一的光源，那幽幽散着冷光的无色透明多面体，回味着王霜突如其来的坦白与愿望，心中五味杂陈。"
    extend "\n从哪里开始好呢？"
    extend "\n当然，你早就知道需要从哪儿开始了，只是迟迟不肯有所动作而已。"
    ## Extended大文本框结束
    ## 场景音乐参考：Tamikurasou - 重新开始
    $ set_scene_music("route2_weird")
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "良久，你终于下定决心把手伸向眼前的无色透明多面体。"
    extend "\n虽然那东西看似近在眼前，但当你真的伸出手时，才发现你们之间可能相隔超过一整个银河系。"
    extend "\n但正如王霜所说，你在这个世界的存在于某种程度上讲与神明无异。"
    extend "\n方才已经做到切换世界了，所以自由延长手臂这样的事情可谓轻而易举。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "延长。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "伸出手后不久，手掌就消失不见。"
    extend "\n你的手臂像糯米团子那样无止境地朝幽暗的空间深处延长，试图抓住仅存的光。"
    extend "\n抓住。五指并拢，限制掌心里事物的自由，这是意在控制的手势。"
    extend "\n即使愿望的终点是跳脱或自由也不例外。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "像是为了跳脱日常，你在逃亡路上紧抓着尤里娅的手；又或是为了实现她庞杂的梦，王霜在入主逝乐园路上死命抓着你的心。"
    extend "\n米姐说过，如果无法从始至终贯彻你的原则，就不要用所谓原则来咄咄逼人，否则只会显得虚伪。"
    extend "\n所以为了不显得虚伪，纯粹的跳脱日常只能通过一再逃避和放弃来达成么？"
    extend "\n抑或说，它从头至尾都是一个自相矛盾的伪命题，一场不为人知的零和博弈？"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "王霜征收了世间全部的自由，再均匀分配给每个人，那么她究竟是崇高的自由战士，还是极致的危权暴君？"
    extend "\n通过紧握一切来最大化地平分自由，这样的“虚伪”何罪之有？"
    extend "\n无非是自私的人就该优先解决自私的问题。"
    extend "\n利己的部分实现以后，其副产品的善恶留与旁人评价即可——王霜显然是这么做的。"
    extend "\n也许她根本不在乎。"
    extend "\n不，她肯定不在乎。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "她只在乎她的完美夏日，而到达那里所要经历的一切，对她来说都是过眼云烟。"
    extend "\n所以她究竟想我帮什么忙？"
    extend "\n她早已抵达了她的应许之地，这之后究竟还想要什么？"
    extend "\n这之后..."
    extend "\n之后？"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "手心传来一阵暖意，想必是抵达了目的地附近。"
    extend "\n手越接近那光源，就越热得发烫。"
    extend "\n当你在那无色透明多面体周围看见你的手指时，手心已如烈火焚身般灼痛。"
    extend "\n但你毫不犹豫地聚拢五指。"
    extend "\n你知道，手里握着的是一种一旦错过就再也拿回不来的东西。"
    extend "\n死死握住。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "手心的火焰顺着长长的手臂蔓延至全身，然而灼烧感并没有如期而至。"
    extend "\n你只是感到温暖。"
    extend "\n由内而外、痛彻心扉的温暖。"
    extend "\n浑身包裹在温热的火焰中，你却冷静地如同一只蓄势待发的猛兽。"
    extend "\n你觉得你离事情的真相越来越近了。"
    ## Extended大文本框结束
    ## 黑屏
    ## 火焰音效
    "…"
    "…"
    "…"
    stop music fadeout 1.0
    ## 完美夏日，王霜第一视角，俯视，看到自己的着装
    ## 完美夏日，王霜第一视角，正视，看到对面双目无神的阿鹤
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
    extend "\n阿鹤...哈哈哈...原来如此，原来如此，这才是代价么？"
    ## Extended文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "你感到怅然若失，但远没有体验到预想中的巨大悲伤。"
    extend "\n都说悲伤才是前进的食量，而你竟连这份动力都失去了。"
    extend "\n弹指间，阿鹤的身形连影子都没留下。"
    extend "\n你在完美的夏日里，在成群影子的簇拥下翩翩起舞。"
    extend "\n这是你的应许之地，你的自由，你魂牵梦绕的最终理想。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "可为什么眼角有些肿胀？盐分和水珠在眼眶周围汇集，但你阻止了它们进一步去完成使命。"
    extend "\n那是不合时宜的。"
    extend "\n虽然没有人在看就是了。"
    extend "\n没有人。"
    extend "\n永远也不会有人看了。"
    extend "\n和消失的阿鹤一样，你也闭上双眼，在踏足你理想乡的五分钟后开始仔细思索,事到如今，你为了你的理想究竟失去了什么。"
    ## Extended大文本框结束
    ## 黑屏

    ## Route 2 结束
    $ unlock_route(2)
    return