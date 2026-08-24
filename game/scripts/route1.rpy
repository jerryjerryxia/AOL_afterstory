## route1.rpy
## Route 1

label route1_start:

## 一周目：浮潜

    call screen route_title(_("浮潜"))
    ## 脸入水后冒泡泡的音效：face-down-bubble
    $ play_sfx("audio/sfx/face-down-bubble.wav")
    ## 转场：虚空对视
    show void default with scene_dissolve
    ## 背手站立，默认表情
    $ wait_sfx()
    wangshuang "欢迎回来，阿鹤。"
    ahe "嗯...那...倒不如去死...？"
    ## 背手站立，吃惊表情
    wangshuang "哦？有趣的提议，为什么呢？"
    ahe "我...不好意思...我觉得我有点..."

    $ madness_choices_seen += 1
    menu:
        extend ""
        "不对劲...":
            pass
        "很有精神！":
            $ madness += 1
            $ madness_plus_taken += 1
            pass

    ## 抱胸站立，默认表情
    wangshuang "嗯，从之前的病史来看，你总是在这两个状态之间来回反复，但现在你是什么感觉呢？"
    ahe "..."
    ## 抱胸站立，无奈表情
    wangshuang "啊...连这也说不出来么？"
    ## 背手站立，默认表情
    wangshuang "那也可以聊聊你此刻看到的，或听到的，都可以聊，我在听呢。"
    ahe "我感觉...有某种暴戾的东西在我耳边一直说个不停，它想我去做一些非常恶毒的事情..."
    ## 抱胸站立，面无表情
    wangshuang "唔，原来如此，原来如此。"
    ahe "我...又病了吗？"
    ## 右手叉腰，左手食指竖起做讲解状，默认表情
    wangshuang "不，恰恰相反，阿鹤。要我说，你现在就像太阳一样稳定。"
    ahe "太阳？"
    ## 背手站立，吃惊表情
    wangshuang "哦，不好意思，太阳在那儿。"
    ## 玻璃破碎音效：glass-smash-normalized
    $ play_sfx("audio/sfx/glass-smash-normalized.wav")
    ## 转场：夏日对视
    scene bg_summergaze with scene_soft
    ## 场景背景里的黑暗碎裂，变为完美夏日，金色的沙滩和蔚蓝的海，只是一个人都没有
    ## 场景音乐参考风格1：樹氷の輝き (Shine of Silver Thaw)，夜の向日葵（The sunflower of the night），Running Waters - https://audionautix.com/Music/RunningWaters.mp3 (Jason Shaw)，Shianchu
    ## 场景音乐参考风格2：Jellyfish - https://audionautix.com/Music/Jellyfish.mp3  (Jason Shaw)
    $ set_scene_music("route1_scene1")
    ## 表情：大笑
    scene summergaze_laugh
    $ renpy.transition(Dissolve(0.2), layer="master")
    $ wait_sfx()
    wangshuang "你看，太阳。"
    ahe "嗯，太阳。"
    wangshuang "金色的，温暖的，让人舒适而安心的太阳，它就在那里。"
    wangshuang "对于沐浴日光中的人来说，明白这一点就够了。"
    ahe "可它分明是我视野里最暴烈、最盛气凌人的东西了。"
    ## 表情：面无表情
    scene summergaze_blank
    $ renpy.transition(Dissolve(0.2), layer="master")
    wangshuang "那就闭上眼睛吧。那样你的问题便会迎刃而解了。"
    ahe "可我还是觉得我快要..."

    $ madness_choices_seen += 1
    menu:
        extend ""
        "疯了...":
            pass
        "睡着了。":
            $ madness += 1
            $ madness_plus_taken += 1
            pass

    ## 表情：默认
    scene summergaze_default
    $ renpy.transition(Dissolve(0.2), layer="master")
    wangshuang "嗯，那样也是无可厚非的事情。"
    ahe "那怎么可能是——"
    wangshuang "当然就是这样的，阿鹤。"
    ## 表情：小吃惊
    scene summergaze_surprised
    $ renpy.transition(Dissolve(0.2), layer="master")
    wangshuang "这是你的心理咨询。你是来访者，而我是咨询师。假如你连这种基本前提都不愿接受的话，你来这里又是为什么？"
    ahe "可我确实想不起来啊...所以...我该怎样才能好起来？"
    wangshuang "修补本就完整的东西，那自然是做不到的。"
    ahe "..."
    ## 表情：面无表情
    scene summergaze_blank
    $ renpy.transition(Dissolve(0.2), layer="master")
    wangshuang "你不同意。"
    ahe "...你...求求你不要再浪费我的时间了..."
    ## 表情：小声嘀咕
    scene summergaze_mutter
    $ renpy.transition(Dissolve(0.2), layer="master")
    wangshuang "说起时间，你要那东西有什么用？"
    ahe "我还要——我还得..."
    ## 表情：默认
    scene summergaze_default
    $ renpy.transition(Dissolve(0.2), layer="master")
    wangshuang "我在听呢。"
    wangshuang "不用紧张的，阿鹤，你现在尽可以畅所欲言哦。如果说话还是有困难的话，尝试先闭上眼睛深呼吸一阵子，就像我之前教你的那样。"
    ahe "...想不起来...什么都想不起来..."
    wangshuang "那就试着想想你是怎么来到这里的，或者想想你在来这里之前正在做什么事，这些都能帮助你回忆过去。"
    wangshuang "但即使什么也想不起来也不必懊恼，那是意料之中的事情。"
    ahe "这...这肯定又是你的把戏！"
    ## 表情：小声嘀咕
    scene summergaze_mutter
    $ renpy.transition(Dissolve(0.2), layer="master")
    wangshuang "总是向外归因可解决不了问题啊，我的朋友。"
    wangshuang "你的病虽然看起来已经根治了，但以你的身心状态而言，任何时候复发我都不意外。"
    wangshuang "不过，你还是没回答我的问题——时间对现在的你而言，有什么用？"
    ahe "啊——啊——没用...完全没用...一切都结束了..."
    ## 表情：小吃惊
    scene summergaze_surprised
    $ renpy.transition(Dissolve(0.2), layer="master")
    wangshuang "哦？所以还是想起来了一些。"
    ahe "你...毁掉了整个逝乐园。"
    ## 表情：大笑
    scene summergaze_laugh
    $ renpy.transition(Dissolve(0.2), layer="master")
    wangshuang "那倒也不必谦虚啊，阿鹤。要知道，这件事少了你是绝对不可能成功的——领衔主演肯定得让给你，我当个制片人就行了。"
    ## 表情：默认
    scene summergaze_default
    $ renpy.transition(Dissolve(0.2), layer="master")
    wangshuang "你也不用觉得我抬举你，过度谦虚只会让人习惯性地逃避责任，是一种需要调整的心态。"
    ahe "可是我...我..."
    ## 表情：面无表情
    scene summergaze_blank
    $ renpy.transition(Dissolve(0.2), layer="master")
    wangshuang "嗯，我懂的，阿鹤。在完成一件惊人的壮举后，出现冒充者综合征是非常常见的事情。但不论你怎么想，事已至此，还是放平心态最重要。"
    ahe "...行啊...你就继续哔哔吧...随便了...随你便了..."
    wangshuang "哎你看你这人，三天两头向外归因，遇事不决就无视问题——"
    ## 表情：小声嘀咕
    scene summergaze_mutter
    $ renpy.transition(Dissolve(0.2), layer="master")
    wangshuang "{size=-10}这就是为什么我离——{/size}"
    ahe "什么？"
    ## 表情：默认
    scene summergaze_default
    $ renpy.transition(Dissolve(0.2), layer="master")
    wangshuang "没事。没事。阿鹤，你知道太阳为什么不会死吗？"
    ahe "因为它不想死？"
    ## 转场：张目对日pt1
    scene bg_sungaze with scene_soft
    ## 面无表情
    wangshuang "错咯——太阳自出生的那一刻起便像氢弹般持续自毁，早就动了死的念头，但它还是在天上烧了四十多亿年。"
    ahe "我不明白..."
    ## 默认
    wangshuang "你当然不明白，你肯定在想‘可这明明也是外因导致的，毕竟整个太阳系都齐心协力地求它继续活下去’。"
    ahe "唔..."
    ## 面无表情
    wangshuang "被我猜到了吧？然而现实恰恰相反——太阳不死仅仅是因为它的使命尚未完成而已，而它的死活与它或其他任何造物的想法，则是没有半点关系。"
    ## 小声嘀咕
    wangshuang "想法是轻薄的、由外界塑造的，一坨烂泥一样谁都可以捏一把，但同时也是无足轻重的。而使命则是彻头彻尾、由内而外的——只有在‘使命’松手之后，‘想法’才配拥有虚假的自由。"
    ahe "这和我们又有什么关系？"
    ## 转场：夏日对视
    scene bg_summergaze with scene_soft
    ## 表情：默认
    scene summergaze_default
    $ renpy.transition(Dissolve(0.2), layer="master")
    wangshuang "当然有关系了，不然你怎么会出现在这里？"
    ahe "可我从来没有想过要出现在这里..."
    wangshuang "嗯，‘你’当然不想。"
    ahe "所以我们在这里做什么？"
    wangshuang "这个嘛，你会明白的。"
    ahe "好吧...如果一切都无需解释，而我们又没有别的事情可以做，那我就只能在这里和你开瞪眼大赛了。"
    wangshuang "你也可以认为这只是一种较为朴素的过程而已。"
    ahe "哈...？"
    wangshuang "嗯，就是那样，朴素，过程，都能听懂对吧？那样就够了。随便用言语去解释概念是会污染概念的，所以你还是不要再多探究了为好。"
    ahe "哦...对对对...懂了...全都懂了...个鬼..."
    ## 表情：大笑
    scene summergaze_laugh
    $ renpy.transition(Dissolve(0.2), layer="master")
    wangshuang "但话说回来，瞪眼大赛啊，我，接受挑战！"
    ahe "没说真要来啊..."
    ## 表情：面无表情
    scene summergaze_blank
    $ renpy.transition(Dissolve(0.2), layer="master")
    show screen op_lock(2)
    wangshuang "盯——"
    hide screen op_lock
    ahe "..."
    show screen op_lock(2)
    wangshuang "盯——"
    hide screen op_lock
    ahe "..."
    wangshuang "噗——"
    ahe "..."
    ## 表情：大笑
    scene summergaze_laugh
    $ renpy.transition(Dissolve(0.2), layer="master")
    wangshuang "——噗噗呃啊——我败了..."
    ahe "自取其辱啊，阿霜。你从我们认识到现在为止有哪一次赢过么？"
    ## 表情：小声嘀咕
    scene summergaze_mutter
    $ renpy.transition(Dissolve(0.2), layer="master")
    wangshuang "哼，你还有脸得意！能盯着你那张臭脸看这么久还不笑的就只有死人了。"
    ahe "嗯...所以我每天起床刷牙的时候都要死一次..."
    wangshuang "你能活到今天确实不容易。"
    ahe "还不是拜你所赐..."
    ## 表情：默认
    scene summergaze_default
    $ renpy.transition(Dissolve(0.2), layer="master")
    wangshuang "不用谢不用谢。那你来吧，拿走你的战利品。"
    ahe "哈？"
    wangshuang "别哈，让你来你就来。"
    ## 屏幕缩放，显得王霜近了很多
    ahe "是什么东西？"
    ## 表情：面无表情
    scene summergaze_blank
    $ renpy.transition(Dissolve(0.2), layer="master")
    wangshuang "你看就是了。"
    ## 转场：张目对日pt1
    scene bg_sungaze with scene_soft
    ## 王霜右手轻轻握拳，阳光透过其中细小的孔洞透了过来
    ahe "什么都看不到。"
    wangshuang "凑近啊你，看仔细点！"
    ahe "啊你别拽我！"
    wangshuang "嗯，就这样对准，给我仔细看好了。"
    ## Extended文本框开始 - accumulating textbox
    ahe "呃...嗯？"
    with fx_quake
    extend "——啊啊啊啊啊啊啊啊啊啊啊！"
    ## Extended文本框结束
    ## 背景开始旋转，白屏逐渐溢满了整个屏幕
    ## 右侧Split Extended大文本框开始 - 右半屏分页
    split_right_page_narrator "自你双眼完成聚焦的一瞬，一阵刺眼的光晕便抹去了视野里的一切，仿佛王霜把天上那轮烈日移植进了你的眼球。"
    extend "\n你在一瞬间里双眼紧闭，整张脸上肌肉拧成一团，死死地挤压你抽搐的眼帘。但为时已晚，那令人绝望的强光已经在你脑海的更深处生了根。"
    split_right_page_narrator "随着炫目的光而来的，是蚀骨的火。这由内而外的火顺着你的双眼、你的视神经蔓延。后脑勺烧了起来，随后是整个大脑皮层，最终你的全身都在这挥之不去的炫光中熊熊灼烧。"
    ## 右侧Split Extended大文本框结束
    ## 右侧Split Extended大文本框开始 - 右半屏分页
    split_right_page_narrator "你将身躯团成球状、死死绷住全身肌肉以抵御这钻心之痛，但在光与火的风暴面前也只是杯水车薪。"
    extend "\n就像太阳一般稳定..."
    extend "\n你想立刻去死，那是缓解疼痛的唯一方法，但你非常清楚，此刻死亡就和使命一样遥不可及。"
    ## 右侧Split Extended大文本框结束
    ## 转场：白屏
    scene bg_white_video with scene_soft
    ## Extended大文本框开始 - accumulating large textbox（不分句）
    $ no_click_split = True
    large_narrator "那声音又响了起来。"
    extend "\n——去找啊，否则这疼痛就永远不会有尽头。"
    extend "\n——去别处，就是这样。"
    extend "\n——否则这疼痛就永远不会有尽头。"
    extend "\n——你的大脑不会适应，你也绝无希望自我了断。"
    extend "\n——只能迈开步子。"
    extend "\n——只有这一个选择。"
    extend "\n——去找吧。"
    $ no_click_split = False
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox（不分句）
    $ no_click_split = True
    large_narrator "——去无人的深海。"
    extend "\n——去银白的沙漠。"
    extend "\n——去漆黑的深渊。"
    extend "\n——去伸手。"
    extend "\n——去坠落。"
    extend "\n——去沉默。"
    extend "\n——直到你再次回到这里为止。"
    $ no_click_split = False
    ## Extended大文本框结束
    ## 白屏逐渐褪去
    ## 转场：甜品店对视1
    ## 长黑场过渡（不可点击快进）
    stop music fadeout 3.0
    show black zorder 100:
        alpha 0.0
        linear 3.0 alpha 1.0
    $ hard_pause(3.0)
    $ hard_pause(0.5)
    scene bg_dessertgaze1
    show black zorder 100:
        alpha 1.0
        linear 2.0 alpha 0.0
    $ hard_pause(2.0)
    hide black
    ## 一家疑似餐厅的背景，又是王霜和阿鹤面对面坐着
    ## 场景音乐风格参考：420
    $ set_scene_music("route1_scene2")
    ahe "呃啊——！"
    ## 表情：疑惑
    scene dessert1_puzzled
    $ renpy.transition(Dissolve(0.2), layer="master")
    wangshuang "嗯？怎么了？"
    ahe "你刚刚...是不是对我做了非常不得了的事情。"
    ## 表情：撇嘴
    scene dessert1_pout
    $ renpy.transition(Dissolve(0.2), layer="master")
    wangshuang "嗯，对。你盯着我发呆，我盯着你发呆，确实挺不得了的。"
    ahe "呃...所以我们为什么在这里？"
    wangshuang "这可是你说要来的。"
    ahe "那我要走了。"
    ## 表情：疑惑
    scene dessert1_puzzled
    $ renpy.transition(Dissolve(0.2), layer="master")
    wangshuang "我们刚坐下诶，你要去哪儿？"
    ahe "不知道，要离开这里就是了。"
    ahe "...能麻烦开一下门吗？"
    ## 表情：默认
    scene dessert1_default
    $ renpy.transition(Dissolve(0.2), layer="master")
    wangshuang "不如问问店家咯。"
    ahe "好吧...你好，能帮我把门开一下吗？"
    wangshuang "不好意思啊先生，老板刚才说了，今天店里的客人都必须留到天黑之后才能走。"
    ahe "你是这儿的店员？而且天已经黑了。"
    wangshuang "老板说，还不够黑。"
    ahe "好吧...所以我能走了吗？"
    ## 表情：坏笑
    scene dessert1_smirk
    $ renpy.transition(Dissolve(0.2), layer="master")
    wangshuang "不能。"
    ahe "你好烦。"
    ## 表情：撇嘴
    scene dessert1_pout
    $ renpy.transition(Dissolve(0.2), layer="master")
    wangshuang "就算出去了，你准备做什么？"
    ahe "把大石头推上山，把琴弦拧成电缆，什么都可以。"
    wangshuang "意思是你准备换个地方无所事事。"
    ahe "再无所事事都胜过和你呆在这里。"
    ## 表情：疑惑
    scene dessert1_puzzled
    $ renpy.transition(Dissolve(0.2), layer="master")
    wangshuang "啊，已经这么遭人嫌了么..."
    ahe "...多少有点自知之明吧你..."
    ## 表情：撇嘴
    scene dessert1_pout
    $ renpy.transition(Dissolve(0.2), layer="master")
    wangshuang "彼此彼此咯，毕竟我们都只是遵循着强烈的愿望，尝试了一直以来想要尝试的事情。"
    ahe "...区别在于我不需要人陪葬。"
    wangshuang "不，区别在于我做到了，而你没有。"
    ahe "..."
    ## 表情：默认
    scene dessert1_default
    $ renpy.transition(Dissolve(0.2), layer="master")
    wangshuang "而你拒绝与我共处一室的真正原因只是嫉妒，仅此而已。"
    ahe "闭嘴吧..."
    ## 表情：坏笑
    scene dessert1_smirk
    $ renpy.transition(Dissolve(0.2), layer="master")
    wangshuang "我闭嘴了又有什么用？难道你那苍白的“理想”就不需要人来陪葬了？"
    wangshuang "你为了{i}尤里娅{/i}那小姑娘折断了多少人的骨头？阿鹤，狡辩是没有意义的，无论如何我们都是逝乐园覆灭的共犯。"
    ahe "..."
    ## 转场：甜品店对视2
    scene bg_dessertgaze2 with scene_dissolve
    ## 表情：默认
    scene dessert2_default
    $ renpy.transition(Dissolve(0.2), layer="master")
    wangshuang "所以不如放下成见，吃点团子，如何？"
    ## 默默吃一口
    ahe "..."
    ## 手中出现无色透明多面体
    wangshuang "这就对了嘛，来都来了。"
    ahe "..."
    wangshuang "有件事你可能不知道，他们家团子是加了 {i}KAS{/i} 才这么好吃的。"
    ahe "诶？所以之后我会上瘾？"
    wangshuang "也许。"
    ahe "行吧，如果能让你从我眼前消失的话。"
    ## 手中出现无色透明多面体，多面体形状略微改变
    wangshuang "你见过哪门子的药能让东西凭空消失的？而且靠染上新瘾来戒旧瘾可是个无底洞啊。"
    ahe "那你还让我吃？以及你自己不也在做同样的事情？"
    wangshuang "那确实还是有点不想看着你和我坠入同样的深渊嘛，毕竟我还挺在乎你的。不过最后还是好奇心赢了，嘿嘿嘿。"
    ahe "别恶心我了，求你了。"
    ## 表情：撇嘴
    scene dessert2_pout
    $ renpy.transition(Dissolve(0.2), layer="master")
    wangshuang "你这人，连真心话都不让人说。"
    ahe "王霜？真心话？这两个词出现在同一个句子里是一种语法错误吧！"
    wangshuang "连真心话都分不清，以后可是要吃大亏的哦。"
    ## 手中出现无色透明多面体，多面体形状略微改变2
    wangshuang "哦，对，团子有得是，千万别客气，请吧——"
    ## 转场：甜品店对视3
    scene bg_dessertgaze3 with scene_dissolve
    ahe "明明刚说完不想我染上。"
    wangshuang "{i}KAS{/i} 生理上确实不成瘾啊，只是太多人会陷进它能让人看到的那些东西，最后心理上产生依赖了，所以你才能在安息地见到那么多活死人。"
    ahe "那我看我估计危险。"
    wangshuang "所以嘛，你到底会怎样呢，阿鹤？我很期待哦。"
    ahe "可是只致幻的话岂不是很无聊？尤其对你来讲。"
    ## 表情：小激动
    scene dessert3_excited
    $ renpy.transition(Dissolve(0.2), layer="master")
    wangshuang "无聊？可别太刺激了！你知道十二小时起步的感官过载是什么感觉吗？五感全部推到极限，尤其是视觉，所有东西的颜色都比平时看到的要鲜艳无数倍，而且全都彼此交融，到最后视野里就是五彩斑斓的白。"
    wangshuang "所有东西都是饱满到极致的，你懂我意思吗？不单是感官上的饱满，而是存在上的饱满，第四维度上的饱满——是那种...不论我们怎么干涉都无法改变的东西。"
    wangshuang "然后脑子里就只剩一个念头：“我操这下不得了了要被外界存在的压强挤碎了快他妈跑”，然后据说，我就开始往窗户外面跳...？也不知道是被谁拉住的，是你吗？应该不是，你应该拽不住我。"
    ## 表情：默认
    scene dessert3_default
    $ renpy.transition(Dissolve(0.2), layer="master")
    wangshuang "总之要不是后来配了眼镜，不然我是绝对不敢再用{i}KAS{/i}的，那次是真的差点死了..."
    ahe "哦，这样一来你那“磕完药差点死掉的小故事集”就又有新章节可以更新了咯。"
    ## 表情：小激动
    scene dessert3_excited
    $ renpy.transition(Dissolve(0.2), layer="master")
    wangshuang "那可是正儿八经的人命啊喂！"
    wangshuang "不过一般人的反应应该不会那么夸张。你会喜欢的，我觉得。"
    ahe "所以我们要在这里待到什么时候？"
    ## 表情：默认
    scene dessert3_default
    $ renpy.transition(Dissolve(0.2), layer="master")
    wangshuang "等时机到了，自然就能离开。"
    ahe "也是一种较为朴素的过程？"
    wangshuang "哦？如此简明且精确的定义，谁教你的？"
    ahe "一个傻逼。"
    ## 表情：小激动
    scene dessert3_excited
    $ renpy.transition(Dissolve(0.2), layer="master")
    wangshuang "{shake}好刻薄！{/shake}"
    ahe "像您这样有成就的大人物，只被骂傻逼还请偷着乐吧。"
    ## 表情：撇嘴
    scene dessert3_pout
    $ renpy.transition(Dissolve(0.2), layer="master")
    wangshuang "所以确实没法放过我了吗？"
    ahe "你还需要人放过？"
    ## 表情：默认
    scene dessert3_default
    $ renpy.transition(Dissolve(0.2), layer="master")
    wangshuang "当然，我又不是没有罪恶感的人。"
    ahe "存疑。"
    wangshuang "哎阿鹤，虽然有些事情我确实做得...不太好...从世俗意义上来说，但也没必要这样质疑我演戏的质量嘛。"
    ahe "你看，你都自首了。还不逮捕你自己。"
    ## 表情：撇嘴
    scene dessert3_pout
    $ renpy.transition(Dissolve(0.2), layer="master")
    wangshuang "那我还得兼任检察官辩护律师和法官，太麻烦了。"
    ahe "用来消磨时间正合适，反正用不完。"
    wangshuang "不不不那就不对了，如果你还想“消磨时间”，那就说明你修为尚浅，还没悟透其中道理。"
    ahe "...好的，师傅。"
    ahe "话说师傅，你手里拿的是什么？"
    ## 表情：默认
    scene dessert3_default
    $ renpy.transition(Dissolve(0.2), layer="master")
    wangshuang "哦，这个？不是什么重要的东西，但你可以尝尝看。"
    ahe "尝尝看？"
    wangshuang "对啊，吃的。要不要试试？"
    $ current_music_scene = None
    stop music fadeout 1.0

    $ madness_choices_seen += 1
    menu:
        extend ""
        "算了":
            "阿霜手里把玩的那物件，你之前肯定见过，却想不起任何细节。"
            "总之没想到竟是一件吃食。"
            "从它那轻若无物又变幻莫测的形态来看，可能真是什么珍馐也说不定。当然，是另一剂猛药的可能性绝对更大。"
            "但无论如何，在 {i}KAS{/i} 即将穿过血脑屏障的前一刻，再往身体里追加不明物质想必不是什么明智决定。"
            "你并不准备在来到这破地方的第一晚就这样放飞自我。"
            ahe "算了吧，都吃过团子了。"
            wangshuang "哦，那随你便咯——说起来啊，阿鹤，你喜欢红色还是蓝色？"
        "接受。":
            $ madness += 1
            $ madness_plus_taken += 1
            "虽然你清楚地意识到你跳动的血管里，{i}KAS{/i} 即将穿越脑血屏障，随时可能把你的意识送上云端，可你那该死的好奇心还是压过了残存的理性。"
            "你接过王霜手里那无色透明的多面体。"
            "那东西轻若无物又变幻莫测，看似是固体，摸起来却又有介于凝胶和麻薯之间的质感，躺在你手心里，冰冰凉的。"
            "你毫无戒心地将那不明物件送进嘴里，简单地咀嚼了一阵，没有尝出任何味道就囫囵吞下了。"
            ## Extended文本框开始 - accumulating textbox
            "…"
            extend "\n……"
            extend "\n………"
            ## Extended文本框结束
            ahe "没味道啊。"
            wangshuang "哦？嗯...那好像也是其中一种可能性...算正常吧。"
            ahe "所以接下来会怎样？"
            wangshuang "这个嘛，你马上就会见到了——所以说阿鹤，你喜欢红色还是蓝色？"

    ## 音乐开始 fade out
    $ current_music_scene = None
    stop music fadeout 4.0
    ahe "蓝色啊，怎么了？"
    wangshuang "你看——"
    ## 转场：甜品店对视4
    scene bg_dessertgaze4 with scene_dissolve
    ## 蓝色波纹特效，并逐渐加入更多色彩
    ## 场景音乐参考：进入幻视，所以虽然场景没变音乐也要切换https://audionautix.com/Music/Beautiful%20Daughter.mp3 (Jason Shaw)，
    $ set_scene_music("route1_hallucination")
    ## Split Extended大文本框开始 - 左右分栏
    split_left_narrator "你正摸不着头脑，转眼间却发现了周遭惊人的变故——四周逐渐泛起蓝色、波浪状的纹理，很快侵蚀了整个视野。"
    extend "\n你反倒比先前要更加冷静，又低头吃了几口团子。甜腻腻的滋味在口腔中涟漪般散开，每颗味觉细胞都在欣喜若狂地发送着饱足的信号。"
    split_right_narrator "甜味的颜色？金黄的莓红的草绿的深棕的，味觉的色彩洪流汇入弥漫在整个视觉空间的海蓝色波浪中。"
    extend "\n你抬头望向王霜，她也望着你，脸上含蓄地挂了一抹邪魅的笑容，眼神里却又流露出一丝欣慰，仿佛望着一个迷路的孩子。"
    extend "\n她略卷的水蓝色长发在周身空间的波浪里散着，勾勒出洋流的轮廓。"
    ## Split Extended大文本框结束
    ## Split Extended大文本框开始 - 左右分栏
    split_left_narrator "你心中对她海啸般的戒心早已荡然无存了——你几乎有些喜欢她现在的样子，宛如一个母亲，又像是神明，给视野不断抹上温柔的蓝色。"
    extend "\n每一缕神经都在扩张。启示性的景象。时间和空间波浪。无孔不入的色彩和甜味。蓝色的。交响。"
    split_right_narrator "反复咀嚼伤痛直至淡而无味，直到甜味凭空冒出来。"
    extend "\n在一切都已结束的当下，连时间都已丧失价值，唯一还能让你睁开双眼的，就只有——"
    ## Split Extended大文本框结束
    ## 居中大字文本框开始 - centered large font textbox
    centered_large_narrator "瘾。"
    ## 居中大字文本框结束
    ## Split Extended大文本框开始 - 左右分栏
    ## 转场：甜品店对视5
    scene bg_dessertgaze5 with scene_dissolve
    split_left_narrator "王霜的微笑越发邪魅——她逐渐成为了一个微笑。"
    extend "\n成瘾。糖分子的洪流。只消一个浪头就使你染上了挥之不去的瘾。"
    extend "\n渴望的源头冲动的源头向往的源头发现了。"
    split_right_narrator "浪潮般的甜味反复沁入意识。她开始微笑。她停止微笑。目光所及之处就能看见她的微笑。"
    ## Split Extended大文本框结束
    ## Split Extended大文本框开始 - 左右分栏
    split_left_narrator "燥热使得意识模糊，痛苦消减。鼓的声音。恒久的鼓声从背景里逐渐浮现，强烈起来，震耳欲聋，每一击都与心跳同调。"
    extend "\n在这暧昧混沌里，你感到安逸。"
    extend "\n这样就够了。"
    ## Split Extended大文本框结束
    ## 撇嘴
    wangshuang "说到底，我们所做的一切也只是为了满足癖好而已。"
    ahe "这大概是一件无可厚非的事情。"
    ## 默认
    wangshuang "大概吧。也许那就是所有人的使命。"
    wangshuang "如此轻浮如此下作，如此美妙。"
    ahe "如此轻而易举。"
    wangshuang "如此唾手可得。"
    ahe "如此甜蜜..."
    ahe "我想要..."

    $ madness_choices_seen += 1
    menu:
        extend ""
        "更多。":
            $ madness += 1
            $ madness_plus_taken += 1
            ahe "我想要就这样继续下去。"
            wangshuang "那就这样继续下去吧。只要你继续睁着眼睛，这一切就不会消失。"
        "就这样睡去。":
            ahe "我困了。"
            wangshuang "无妨，就这样睡去也无可厚非。"

    ## Extended大文本框开始 - accumulating large textbox
    ## 转场：甜品店对视6
    scene bg_dessertgaze6 with scene_dissolve
    large_narrator "更多思绪已无意义，一如时间。"
    extend "\n蓝色空间里的凉爽糖分让你浑身的燥热与恶意消减了大半，你置身一片透明的海域里，又像是漂浮在空洞的宇宙空间中。"
    extend "\n一切都是许可的，这样的冲动从未如此强烈过。"
    extend "\n你迫切地想要伸出手，但双臂已经先你一步向前伸了出去，贪婪地揉捏着冰凉而柔顺的空气，水蓝色的空气。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "更深的见解就隐藏其中，因为一切都是许可的，视野中的所有事物都是从始至终连贯而统一的，如此怡人，如此饱满。"
    extend "\n人类的智识自然无力探寻其中奥秘，但在王霜无处不在的笑容辉耀之下，你的一部分认知已踏入了更深层的水域。"
    extend "\n越向深处就越被不可知所掣肘，当眼前的色彩开始回旋，你意识到或许梦境的另一面并非现实，而是某种更加完整且怖人的造物。"
    ## Extended大文本框结束
    ## 转场：甜品店对视6.51
    scene bg_dessertgaze6_51 with scene_dissolve
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "你的知能越是提升，它的样貌就越发模糊，谜样的面容中只显露出一抹依稀可见的残酷笑容，仿佛在嘲讽你的徒劳。"
    extend "\n但你已经满足了，由内而外地满足了，在饱满的感官刺激中感到一阵——疲劳？"
    extend "\n幸福的疲劳、优质的疲劳、苦苦追寻的疲劳、允许你在辗转反侧后终于入睡的甜美疲劳。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "世界空无一人，因为任何个体都不具备足够的差异能够让它们自称“存在”，因此你将它们尽数吞下，如同团子。"
    extend "\n糖分继续满溢出来，沿着你存在的边缘缓缓淌下，坠入周身蔚蓝的虚空之中，粘稠而香甜。"
    extend "\n糖浆，万物的粘合剂。就用它来替代血液。"
    extend "\n完成之后就去睡吧。"
    extend "\n你的愿望在那念头浮出水面的瞬间便成为了现实，而你只想在这静谧安详的世界里睡去。"
    ## Extended大文本框结束
    ## 色彩开始还原
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "然而当你行将合眼时，一阵强烈的恶心自胃里上涌，就像有人抓住你的肠胃，自下而上地用力挤压。"
    extend "\n警告：过热。过热。"
    extend "\n钟表嘀嗒作响。"
    extend "\n恶心加剧，肠胃彻底拧成一团，而其中汹涌的内容物已经呼之欲出。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "你死命闭气抵抗，汗如雨下，浑身冷颤使你几乎维持不住坐姿，眼看就要从座椅上滚下来。"
    extend "\n随着肠胃痉挛越发剧烈，你终究败在了本能反应面前，脖颈狠狠向前一抻，“哇”地一声吐了出来。"
    extend "\n和你所熟知的呕吐不同，你吐出的只有色彩。"
    ## Extended大文本框结束
    ## 转场：甜品店对视7
    scene bg_dessertgaze7 with scene_dissolve
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "呕吐物与面前桌子接触的瞬间，水蓝的桌面便恢复了原本的颜色。"
    extend "\n你吐出的色彩越多，这令人沮丧的还原就越发提速，转眼便侵蚀了大半个视野。"
    extend "\n色彩还原的地方，水面般摇曳的空间停止了动态，原本随处可见的王霜的微笑也随着视野的复原消散了。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "桌布洁白，金属餐具冷峻，暖色的室内灯光随着呕吐物飘散，不断渗入空气中的每个角落。"
    extend "\n面前盘子里躺着几个没吃完的团子，团子上面糖浆的金黄色泽明艳地让你毛骨悚然。"
    extend "\n胃里再次翻腾起来。你赶紧移开了目光。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "你感到疲惫不堪，只想回到一个更加清醒的地方。"
    extend "\n眼前桌面的存在与本质看起来产生了某种根本性的分离，但你已经没有心力去捕捉这种恼人的细节。"
    extend "\n因为你注意到，在美妙的水蓝色消逝殆尽后，王霜并没有回来。"
    extend "\n空空如也的店里坐着空空如也的你。"
    ## Extended大文本框结束
    ## 画面出现裂痕
    ## Extended大文本框开始 - accumulating large textbox
    ## 转场：甜品店对视8
    scene bg_dessertgaze8 with scene_dissolve
    large_narrator "还原之后的世界仿佛脱了水般脆弱不堪，单是目光扫过就让其表面生出了一连串细小的裂痕。"
    extend "\n更多裂痕。"
    extend "\n直到它们在空间中汇聚成令人不安的绵延裂隙。"
    extend "\n直到周身一切如同一幅缺乏保养的老旧油画那样，一片片剥落，露出背景里黑黢黢的虚空。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "你明知该离开了，却仍旧无动于衷。"
    extend "\n周身空间在微颤中继续碎裂，而你则带着某种同样脆弱的信念静坐原地，任凭倦意侵蚀你脑海中残存的意识。"
    extend "\n{size=-10}只需要她带你离开这里...这样就够了...{/size}"
    extend "\n{size=-10}只需要她...这样...就够了...{/size}"
    extend "\n..."
    extend "\n......"
    extend "\n........."
    extend "\n就够了..."
    extend "\n即便如此，王霜依旧没有回来。"
    ## Extended大文本框结束
    ## 水底泡泡上浮音效：Bubbles_10
    $ play_sfx("audio/sfx/Bubbles_10.wav")
    ## 音效完成后再执行转场
    $ wait_sfx()
    ## 转场：粉红屏
    scene black with scene_soft
    $ current_music_scene = None
    stop music fadeout 1.0
    ## Extended文本框开始 - accumulating textbox
    $ wait_sfx()
    ahe "阿霜？"
    extend "\n你在吗？"
    extend "\n你要是再假装消失的话我就要去死咯？"
    ## Extended文本框结束
    ## Extended文本框开始 - accumulating textbox
    ahe "阿霜？"
    extend "\n有人吗？"
    extend "\n..."
    ## Extended文本框结束
    ## 场景音乐参考：https://audionautix.com/Music/DeepSpace.mp3 (Jason Shaw)
    $ set_scene_music("route1_deepspace")
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "没有人。周身只有一片暧昧的粉红色雾气。"
    extend "\n你试着蜷起手指，只觉得手心传来一阵稍纵即逝的触感，冰凉而虚幻。"
    extend "\n你挣扎着想要活动身体，却猛地意识到自己的横膈膜停止了张弛。"
    ## Extended大文本框结束
    ## 居中大字文本框开始 - centered large font textbox
    centered_large_narrator "请保持呼吸。"
    ## 居中大字文本框结束
    ## 呼吸ambience音效开始
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "空气中充斥着一股微妙的甜腻味道。"
    extend "\n粉红色的？"
    extend "\n在童年故乡的某个傍晚，太阳将要落山，你踌躇满志地幻想未来时，也曾闻到过这样的味道。"
    extend "\n它让你想起一些美好但没有意义的事情。"
    extend "\n比如王霜柔软而光滑的——"
    extend "\n比如月明星稀的夜空。"
    extend "\n比如此刻。"
    extend "\n无论如何也没法从中逃离，但请保持呼吸。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "你漂浮着。"
    extend "\n腹中偶有痉挛，就像方才经历了一场盛大的呕吐。"
    extend "\n吐到浑身只剩下电流与心跳。"
    extend "\n色彩与声音。"
    ## Extended大文本框结束
    ## 居中大字文本框开始 - centered large font textbox
    centered_large_narrator "原来如此，原来如此。"
    ## 居中大字文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "请严肃呕吐。"
    extend "\n只要能够继续呼吸。"
    extend "\n耳畔那滔滔不绝的声音终于消褪了。"
    extend "\n此刻你只能听见自己身体的动静。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "请不要脱水。"
    extend "\n请不要腐烂。"
    extend "\n请不要在一具人形脊椎动物的皮囊里窒息。"
    ## Extended大文本框结束
    ## 呼吸音效
    ## Extended大文本框开始 - accumulating large textbox（不分句）
    $ no_click_split = True
    $ interro_reset()
    large_narrator "——录入中——录入中——"
    extend "\n——接下来将对生体失窃案的犯罪嫌疑人进行问询。"
    extend "\n——请问，您在过去的二十四小时内，是否经历过严重肉体伤害、认知紊乱、大量出血、死亡等重大健康隐患？"
    extend "\n——..."
    label _extmenu_1:
        window hide Dissolve(.25)
        menu:
            "有":
                $ _intro_fade_pending = True
                extend "\n——有\n——请详细交代该经历的过程。"
                extend "\n——请注意，您没有权利保持沉默。"
                window hide Dissolve(.25)
                menu:
                    "王霜把三根冰凿子打进我的眼窝之后，又让我对她做同样的事。透过骨头你就知道了...是软软的，摸起来像嫩豆腐。":
                        $ interro_insane += 1
                        $ interro_seen.add("王霜把三根冰凿子打进我的眼窝之后")
                        $ _intro_fade_pending = True
                        extend "\n——王霜把三根冰凿子打进我的眼窝之后，又让我对她做同样的事。透过骨头你就知道了...是软软的，摸起来像嫩豆腐。\n——觉得可爱吗？"
                        window hide Dissolve(.25)
                        menu:
                            "一般般...":
                                $ interro_calm += 1
                                $ _intro_fade_pending = True
                                extend "\n——一般般...\n——您的回答已被记录。"
                            "恶心死了！":
                                $ interro_death += 1
                                $ _intro_fade_pending = True
                                extend "\n——恶心死了！\n——预料之外呢，阿鹤先生。"
                            "可爱！":
                                $ interro_insane += 1
                                $ _intro_fade_pending = True
                                extend "\n——可爱！\n——很好。"
                    "吃过 KAS 之后我就拉着身边不知道是谁一个箭步跳出了窗户。就是飞得不够高，反而不容易死，毕竟第一次嘛，走的是保守选项。":
                        $ interro_halluc += 1
                        $ _intro_fade_pending = True
                        extend "\n——吃过 {i}KAS{/i} 之后我就拉着身边不知道是谁一个箭步跳出了窗户。就是飞得不够高，反而不容易死，毕竟第一次嘛，走的是保守选项。\n——请问您还记得剂量吗？"
                        window hide Dissolve(.25)
                        menu:
                            "不记得，王霜给的。":
                                $ interro_calm += 1
                                $ _intro_fade_pending = True
                                extend "\n——不记得，王霜给的。\n——您的回答已被记录。"
                            "三百八十二点三毫克，误差在零点四毫克之内。":
                                $ interro_halluc += 1
                                $ _intro_fade_pending = True
                                extend "\n——三百八十二点三毫克，误差在零点四毫克之内。\n——如果您无法如实作答，请不要胡乱编造答案。"
                            "我他妈脑子要是这么好使我还有空在你这儿跟你讲相声？":
                                $ interro_hostile += 1
                                $ _intro_fade_pending = True
                                extend "\n——我他妈脑子要是这么好使我还有空在你这儿跟你讲相声？\n——您的脑子确实非常重要，阿鹤先生。"
                    "尤里娅，她已经彻底离开这里了。用喉管与嘴唇并不能拼出她的声带——她...她骗了我...":
                        $ interro_death += 1
                        $ _intro_fade_pending = True
                        extend "\n——{i}尤里娅{/i}，她已经彻底离开这里了。用喉管与嘴唇并不能拼出她的声带——她...她骗了我...\n——请问您与{i}尤里娅{/i}女士——"
                        window hide Dissolve(.25)
                        menu:
                            "闭嘴...":
                                $ interro_hostile += 1
                                $ _intro_fade_pending = True
                                extend "\n——闭嘴...\n——您的回答已被记录。"
                            "我们是同事关系，正处于一段禁断的办公室恋情之中。":
                                $ interro_halluc += 1
                                $ _intro_fade_pending = True
                                extend "\n——我们是同事关系，正处于一段禁断的办公室恋情之中。\n——根据我们的调查，这属于不实信息。"
                            "死了。还有什么要问的么？":
                                $ interro_death += 1
                                $ _intro_fade_pending = True
                                extend "\n——死了。还有什么要问的么？\n——请尝试提供朴素事实以外的信息，阿鹤先生。"
                    "沙滩上可以用盐雕出永远不会腐朽的雕像哦。海风会让它变得无比坚硬，直到下一次涨潮为止。":
                        $ interro_calm += 1
                        $ _intro_fade_pending = True
                        extend "\n——沙滩上可以用盐雕出永远不会腐朽的雕像哦。海风会让它变得无比坚硬，直到下一次涨潮为止。\n——请不要提供与本次问询无关的信息，阿鹤先生。"
                        extend "\n——以及为什么您对“不朽”的定义是以天为单位的..."
            "没有":
                if "m1B" not in interro_once:
                    $ interro_calm += 1
                    $ interro_once.add("m1B")
                $ _intro_fade_pending = True
                extend "\n——没有\n——检测到您提供了不实信息，请再次作答。"
                ## 重新展示本次选择
                jump _extmenu_1
    extend "\n——请问，您盗窃本公司的生体产品，是出于自主意愿，还是有他人指使？"
    extend "\n——..."
    window hide Dissolve(.25)
    menu:
        "是自愿的":
            $ _intro_fade_pending = True
            extend "\n——是自愿的\n——请详细交代您的动机。"
            extend "\n——请注意，您没有权利保持沉默。"
            window hide Dissolve(.25)
            menu:
                "她属于我，仅此而已。":
                    $ interro_halluc += 1
                    $ _intro_fade_pending = True
                    extend "\n——她属于我，仅此而已。\n——请问您是如何得出这一结论的呢？"
                    window hide Dissolve(.25)
                    menu:
                        "她亲口告诉我的。":
                            $ interro_halluc += 1
                            $ _intro_fade_pending = True
                            extend "\n——她亲口告诉我的。\n——很不幸，当事人的语料库中并没有检索出类似的消息呢，阿鹤先生。"
                        "但凡正常人的脑子都能得出这一结论的吧...":
                            $ interro_hostile += 1
                            $ _intro_fade_pending = True
                            extend "\n——但凡正常人的脑子都能得出这一结论的吧...\n——我恐怕有坏消息要告诉您，阿鹤先生。"
                        "因为可爱！":
                            $ interro_insane += 1
                            $ _intro_fade_pending = True
                            extend "\n——因为可爱！\n——明白了。"
                "她说想去外面看看。":
                    $ interro_calm += 1
                    $ _intro_fade_pending = True
                    extend "\n——她说想去外面看看。\n——请问您还记得她是在怎样的场合下告知您这个想法的吗？"
                    window hide Dissolve(.25)
                    menu:
                        "不记得，王霜告诉我的。":
                            $ interro_calm += 1
                            $ _intro_fade_pending = True
                            extend "\n——不记得，王霜告诉我的。\n——请不要随意相信他人传播的不实信息啊，阿鹤先生..."
                        "在她死前。":
                            $ interro_death += 1
                            $ _intro_fade_pending = True
                            extend "\n——在她死前。\n——您的回答已被记录。"
                        "能麻烦您别再问这种刁钻的记忆力考题了么？":
                            $ interro_hostile += 1
                            $ _intro_fade_pending = True
                            extend "\n——能麻烦您别再问这种刁钻的记忆力考题了么？\n——您没有权力质疑问题的合理性，阿鹤先生，请如实作答。"
                "零件啊！零件不够用了，王霜说零件不够用了，那就只好自己出来找了咯。":
                    $ interro_insane += 1
                    $ _intro_fade_pending = True
                    extend "\n——零件啊！零件不够用了，王霜说零件不够用了，那就只好自己出来找了咯。\n——请确认您对于这个回答的严肃性。"
                    window hide Dissolve(.25)
                    menu:
                        "非常严肃非常认真非常一丝不苟非常——":
                            $ interro_insane += 1
                            $ _intro_fade_pending = True
                            extend "\n——非常严肃非常认真非常一丝不苟非常——\n——请立刻停止无意义的胡言乱语，阿鹤先生。"
                        "不如去问问王霜，看看她怎么说。":
                            $ interro_calm += 1
                            $ _intro_fade_pending = True
                            extend "\n——不如去问问王霜，看看她怎么说。\n——这不是需要您操心的问题。"
                        "确认了。然后呢？":
                            $ interro_hostile += 1
                            $ _intro_fade_pending = True
                            extend "\n——确认了。然后呢？\n——明白。您的回答已被记录。"
                "血...":
                    $ interro_death += 1
                    $ _intro_fade_pending = True
                    extend "\n——血...\n——请展开聊聊"
                    window hide Dissolve(.25)
                    menu:
                        "无可奉告。":
                            $ interro_calm += 1
                            $ _intro_fade_pending = True
                            extend "\n——无可奉告。\n——如果您坚持沉默，我们将保留采取强制措施的可能性，还请您多多理解。"
                        "只有足够的血我们才能继续生存下去，你明白吗？这是基本常识吧，我亲爱的朋友，那么请问你愿意捐献——":
                            $ interro_insane += 1
                            $ _intro_fade_pending = True
                            extend "\n——只有足够的血我们才能继续生存下去，你明白吗？这是基本常识吧，我亲爱的朋友，那么请问你愿意捐献——\n——问询对象出现了严重的精神状态波动，立即停止问询，启用code purple——"
                        "杀了她，就能见到血。有什么很难理解的地方吗？":
                            $ interro_death += 1
                            $ _intro_fade_pending = True
                            extend "\n——杀了她，就能见到血。有什么很难理解的地方吗？\n——您的回答已被记录。"
        "受人指使":
            $ _intro_fade_pending = True
            extend "\n——受人指使\n——请交代该第三方的身份。"
            extend "\n——请注意，您没有权利保持沉默。"
            window hide Dissolve(.25)
            menu:
                "是尤里娅。":
                    $ interro_halluc += 1
                    $ _intro_fade_pending = True
                    extend "\n——是{i}尤里娅{/i}。\n——请详细交代她的动机。"
                    window hide Dissolve(.25)
                    menu:
                        "她想要消失，仅此而已。":
                            $ interro_calm += 1
                            $ _intro_fade_pending = True
                            extend "\n——她想要消失，仅此而已。\n——这恐怕是您的一厢情愿，阿鹤先生。"
                            extend "\n——悉听尊便。"
                        "因为可爱！":
                            $ interro_insane += 1
                            $ _intro_fade_pending = True
                            extend "\n——因为可爱！\n——请停止无谓的胡言乱语，阿鹤先生。"
                            extend "\n——喂喂喂，质疑{i}尤里娅{/i}可爱的人可都没什么好下场啊，你可要想清楚了。"
                            extend "\n——...让我们继续吧..."
                        "她想要让逝乐园整个消失啊，你们居然连这种事情都不清楚？情报工作做得不够到位啊，滑稽哦！":
                            $ interro_halluc += 1
                            $ _intro_fade_pending = True
                            extend "\n——她想要让逝乐园整个消失啊，你们居然连这种事情都不清楚？情报工作做得不够到位啊，滑稽哦！\n——阿鹤先生精神分裂分析报告呢？需要重新评估么..."
                "是王霜。":
                    $ interro_calm += 1
                    $ _intro_fade_pending = True
                    extend "\n——是王霜。\n——请详细交代她的动机。"
                    window hide Dissolve(.25)
                    menu:
                        "不清楚，她只是告诉我要这么做而已。":
                            $ interro_calm += 1
                            $ _intro_fade_pending = True
                            extend "\n——不清楚，她只是告诉我要这么做而已。\n——阿鹤先生...没有检测到不实信息么...无妨，那我们继续..."
                        "那可是为逝乐园带来毁灭与重生的女神啊！你们这些卑微的肉体凡胎又有什么资格去了解她的行动纲领？！":
                            $ interro_insane += 1
                            $ _intro_fade_pending = True
                            extend "\n——那可是为逝乐园带来毁灭与重生的女神啊！你们这些卑微的肉体凡胎又有什么资格去了解她的行动纲领？！\n——..."
                            extend "\n——怎么了？惊讶地说不出话来了么？也好，那就在她残酷的圣光中继续颤抖吧！"
                        "用来研究。":
                            $ interro_hostile += 1
                            $ _intro_fade_pending = True
                            extend "\n——用来研究。\n——请详细交代她的研究课题和目的。"
                            extend "\n——你们还是自己去问她吧。"
                "是米特拉布。":
                    $ interro_hostile += 1
                    $ _intro_fade_pending = True
                    extend "\n——是米特拉布。\n——请详细交代该组织的动机。"
                    window hide Dissolve(.25)
                    menu:
                        "你去问他们的老板啊，店面离你们这么近，跑来问我是做什么？":
                            $ interro_calm += 1
                            $ _intro_fade_pending = True
                            extend "\n——你去问他们的老板啊，店面离你们这么近，跑来问我是做什么？\n——请注意您的立场，阿鹤先生。"
                            extend "\n——假如你真的觉得我脑子里有你们想要的信息，打开我的脑子不就行了，为什么要在这儿浪费时间？"
                            extend "\n——..."
                        "米姐喜欢看生体喝醉的样子，她觉得那很性感。":
                            $ interro_halluc += 1
                            $ _intro_fade_pending = True
                            extend "\n——米姐喜欢看生体喝醉的样子，她觉得那很性感。\n——醉态确实是本公司生体产品最新推出的性能优化点之一，非常高兴这一优化受到了用户的喜爱。我们将择机上门送上我们的感谢。"
                        "她是来调查你们的，准备好人财两空吧，资本主义的走狗们。":
                            $ interro_hostile += 1
                            $ _intro_fade_pending = True
                            extend "\n——她是来调查你们的，准备好人财两空吧，资本主义的走狗们。\n——请提供浅显事实之外的信息。"
                            extend "\n——你们连这都知道了，还有什么事情不是浅显事实的..."
                            extend "\n——无妨，让我们继续吧。"
                "死人...是死人...":
                    $ interro_death += 1
                    $ _intro_fade_pending = True
                    extend "\n——死人...是死人...\n——阿鹤先生，请不要顾左右而言他。"
                    window hide Dissolve(.25)
                    menu:
                        "他们已经到门口了...还不去迎接么？":
                            $ interro_death += 1
                            $ _intro_fade_pending = True
                            extend "\n——他们已经到门口了...还不去迎接么？\n——阿鹤先生，我们没有时间听您的胡言乱语，如果您已经打定主意——"
                            ## glitch音效
                            ## 转场：黑屏
                            scene bg_black_video with scene_soft
                        "你知道么...只要手法足够细致，听小骨也是可以骨折的...想知道怎么做么...":
                            $ interro_insane += 1
                            $ _intro_fade_pending = True
                            extend "\n——你知道么...只要手法足够细致，听小骨也是可以骨折的...想知道怎么做么...\n——这与我们讨论的话题无关，阿鹤先生，请注意——"
                            ## glitch音效
                            ## 转场：红屏
                            scene black with scene_soft
                        "血...是血...等你们也能看到那景象...一切就太迟了...太迟了...":
                            $ interro_halluc += 1
                            $ _intro_fade_pending = True
                            extend "\n——血...是血...等你们也能看到那景象...一切就太迟了...太迟了...\n——无妨，那就让我们继续吧。"
    extend "\n——本公司将本着公平、公正、公开的原则，保留为具有高度危险性的犯罪嫌疑人实施脑前叶白质切除术的可能性 ，请问您有异议吗？"
    extend "\n——..."
    window hide Dissolve(.25)
    menu:
        "随便吧。":
            $ interro_calm += 1
            $ _intro_fade_pending = True
            extend "\n——随便吧。\n——感谢您的配合。"
            extend "\n——如有必要，我们保证将以最人道的方式对您进行无害化处理。"
            extend "\n——请耐心等待审议结果。"
        "有。":
            $ interro_hostile += 1
            $ _intro_fade_pending = True
            extend "\n——有。\n——阿鹤先生，请注意您此刻没有反对的权利。"
            extend "\n——如有必要，我们保证将以最人道的方式对您进行无害化处理。"
            extend "\n——在此期间，请您不要尝试阻挠我们的工作人员的日常工作，耐心等待审议结果。"
        "都已经做过一遍了，看来你们还挺闲得慌？" if "王霜把三根冰凿子打进我的眼窝之后" in interro_seen:
            $ interro_insane += 1
            $ _intro_fade_pending = True
            extend "\n——都已经做过一遍了，看来你们还挺闲得慌？\n——为了确保您的无害化，我们将对您进行核磁共振检查，在那之前请确保您体内没有任何金属制品。"
            extend "\n——如果您有佩戴心脏起搏器、植入式除颤器等设备，请自行移除。"
            extend "\n——您的核磁共振检查将在三十分钟后开始。"
        "顺便杀了我如何？":
            $ interro_death += 1
            $ _intro_fade_pending = True
            extend "\n——顺便杀了我如何？\n——这恐怕暂时是不可能的，阿鹤先生。"
        "如果牺牲大脑的一部分就能延迟末日的到来的话，请便吧。":
            $ interro_halluc += 1
            $ _intro_fade_pending = True
            extend "\n——如果牺牲大脑的一部分就能延迟末日的到来的话，请便吧。\n——末日是会来临的，阿鹤先生，请放心吧。"
    extend "\n——感谢您的配合，针对您的综合处置措施将在明天的问询之后对外公开，请静候佳音。"
    extend "\n——录入完毕——"
    $ no_click_split = False
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "凝胶柔软。"
    extend "\n玻璃也柔软。"
    extend "\n黑夜柔软。"
    extend "\n光源柔软。"
    extend "\n粉红色雾气却坚硬如铁。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    $ interro_evaluate()
    large_narrator "更新了对于犯罪嫌疑人的心理评估和综合处置措施："
    ## 精神状态：平稳【仅平稳>1】/疯狂【仅疯狂>1】/分裂【平稳和疯狂皆>1】/检测失败【前三选项皆不成立时】
    extend "\n精神状态：[interro_mental!t]"
    ## 人格特质：冷静【对抗<=1】/对抗【对抗>1】
    extend "\n人格特质：[interro_trait!t]"
    ## 污染进程：幻觉【仅幻觉>1】/死亡【仅死亡>1】/幻灭【幻觉和死亡皆>1】/无污染【前三选项皆不成立时】
    extend "\n污染进程：[interro_pollution!t]"
    ## 建议执行：记忆消除并释放【平稳/检测失败 × 冷静 × 无污染/幻觉/死亡 】，记忆消除和无限期监禁【疯狂 × 冷静 × 幻觉/死亡/幻灭/无污染，以及 平稳/检测失败 · 冷静 · 幻灭】，脑白质切除、记忆消除并释放【平稳/检测失败 × 对抗 × 无污染/幻觉/死亡，疯狂·对抗·无污染，分裂 × 冷静/对抗 × 无污染】，脑白质切除、记忆消除并无限期监禁【疯狂 × 对抗 × 幻觉/死亡/幻灭，平稳/检测失败 × 对抗 × 幻灭，分裂 × 冷静/对抗 × 幻觉/死亡/幻灭】
    extend "\n建议执行：[interro_verdict!t]"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "需要时刻监测的数据点："
    extend "\n生命体征。"
    extend "\n死亡体征。"
    extend "\n不可有误。"
    extend "\n脑电波。"
    extend "\n脑电波。"
    extend "\n————————————？"
    extend "\n有误。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox（不分句）
    $ no_click_split = True
    large_narrator "——现在开始插入——记忆——"
    extend "\n——连续24小时的核磁共振？嗨，小意思！除非这人的骨头是铁做的——？"
    extend "\n——当然啦，即使真的如此，那让他被由内而外地彻底烤熟，也不失为一种凄美悲壮的结局。"
    extend "\n——嗯...就是要考虑清理问题...也对...血肉混进仪器里了终归是一件麻烦事..."
    extend "\n——所以...总之会继续监测的。"
    extend "\n——因为那正是...目的...盛大地收...后为后人所铭记，哈哈。现在的年轻人啊..."
    extend "\n——…的理想？"
    extend "\n——理想？说得好像你这年近三十的__是一个十三岁的孩子。"
    extend "\n——同时，请务必...忘记..."
    extend "\n——弹出中——弹出中——"
    $ no_click_split = False
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox（不分句）
    $ no_click_split = True
    large_narrator "——读取中——读取中——"
    extend "\n——喂，所以你会为我保持呼吸么？"
    extend "\n——为我拆出旁人的肋骨，为我洞穿无辜者的肺叶？"
    extend "\n——为我毫无理由地献上溢美之词？"
    extend "\n——赠予我自由？"
    extend "\n——赠予我死亡？"
    extend "\n——无趣啊。"
    extend "\n——但请保持呼吸。"
    extend "\n——读取失败——"
    $ no_click_split = False
    ## Extended大文本框结束
    ## 呼吸音效
    ahe "哦。"
    ahe "呃..."
    ahe "啊...！"
    ahe "阿...霜..."
    ahe "我..."
    ahe "..."
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "横膈膜早就停止了张弛，当你意识到自己无法呼吸时，一切已经晚了。"
    extend "\n你感到浑身发胀。那是因为粉红色的神经毒素正顺着透明细长的针刺注入你的血管。"
    extend "\n直到你全身都染上粉红色。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox（不分句）
    $ no_click_split = True
    large_narrator "粉红色的雾气散成一丝丝隐约可见的、游移的细线——水母的触手。"
    extend "\n这分明是她精心策划的长期疗程的开端，却因为视线模糊而永远定格在了肤浅的一面。"
    extend "\n——杀人的也罢，懦弱的也罢，捏成一个便是了。"
    extend "\n——剧毒的也罢，解毒的也罢，混成一锅就行了。"
    extend "\n总之要合而为一，总之要并联，总之要揉碎了再捏起来，总之即使不为了重生也要彻底毁灭。"
    extend "\n总之必须保持呼吸。"
    $ no_click_split = False
    ## Extended大文本框结束
    ## 呼吸音效
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "你想了起她的善。"
    extend "\n你只能想起她的善。"
    extend "\n在这水母勾勒的温暖牢笼里，你只被允许想起她的善。"
    extend "\n伞盖边缘在你看不到的远处有节奏地收缩舒张。每一根触手都与你相连。"
    extend "\n触手连接肌肤的地方，有火苗在跳动。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "呼吸停止的那一刻，你感到舌尖有些麻木。"
    extend "\n一股苦涩液体自喉管深处涌上来。"
    extend "\n却在抵达舌尖的瞬间消散。"
    extend "\n因为要保持呼吸道畅通。"
    extend "\n请保持呼吸。"
    ## Extended大文本框结束
    ## 呼吸音效
    ## Extended大文本框开始 - accumulating large textbox
    ## 转场：灰屏
    scene black with scene_soft
    large_narrator "你想起她那窗明几净的办公室，但却无法回忆起分毫色彩。"
    extend "\n因为她是治愈的灰，包容的灰。"
    extend "\n任何色彩倾泻其中，都只能归零的灰。"
    extend "\n灰在扩散，由点到面，最后变得宛如一帘浩大的幕布般徐徐展开。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "你只能眼睁睁地看着面前的灰幕展开。"
    extend "\n因为还原的灰幕此刻也是你的愿望。"
    extend "\n即使身处灰幕下就必须遭受失去皮肤般的剧烈疼痛。"
    extend "\n嚎叫。你只能歇斯底里的嚎叫。在嚎叫中睡去又醒来。"
    extend "\n你并不明白自己为何嚎叫，明明只是感到疼痛而已。"
    extend "\n也许那嚎叫源自一种强加于你的欢欣，使你不能自已地庆祝一个残酷灵魂的自由与暴行。"
    ## Extended大文本框结束
    ## Extended文本框开始 - accumulating textbox
    "灰幕沉默。你也终归沉默。"
    extend "\n所以，还要保持呼吸么？"
    ## Extended文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "灰幕的蔓延永无止境，一如疼痛的叠加永无止境。"
    extend "\n更多毒液渗入血管，血液沸腾起来，内脏在冒着泡的炽热血液浇灌下燃烧、破裂，但你只能感受到你执意选择的灰。"
    extend "\n痛觉与痛苦开始分离。在日复一日的感官撕扯中，你的体表逐渐只剩下介于触觉和冷感之间的微妙麻木。"
    extend "\n但横膈膜仍在均匀地舒张。"
    extend "\n这就够了。"
    extend "\n这就...够了。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "她说，一定要保持呼吸。"
    extend "\n因此你义无反顾地照做。"
    extend "\n即使灰幕吞噬了整个视野，也不会停歇。"
    ## Extended大文本框结束
    ## 电视机关机音效
    ## 电视机关机转场
    ## 转场：黑屏
    scene bg_black_video with scene_soft
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "..."
    extend "\n......"
    extend "\n........"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "在长久的漂浮中，你的肢体变得干瘪而暗哑，仿佛再薄一点就要与灰幕融为一体。"
    extend "\n但即使是这样的肢体，也只能站起来，让身子暖起来，让肠胃蠕动起来。"
    extend "\n让血液流淌起来，即使横膈膜早就停止了舒张。"
    extend "\n钟声。钟声。钟声。钟声。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "在钟声里，你在视野的余光中瞥见了某种远大于你的存在，祂在召唤着你。"
    extend "\n耳畔传来细弱的声音，那嗓音神秘而熟悉 - 你的病终究与我一样，我羸弱的爱人。"
    extend "\n你听见那声音，就像听见了复活的钟声，虽然振聋发聩，却使你义无反顾地站了起来。"
    extend "\n同时停止了呼吸。"
    ## 呼吸ambient音效停止
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "要去哪儿呢？"
    extend "\n要从粉红色的雾气里走出去？"
    extend "\n完全进到灰幕里去？"
    extend "\n治病也罢，杀人也罢。"
    extend "\n总要去些地方——"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "再回过神来时，贯穿全身的疼痛已经退却了，你的肢体看起来健康而饱满。"
    extend "\n脑袋略有些刺痛，但你知道大脑皮层以内是不存在痛觉神经的，所以这痛觉想必与眼前的灰幕一样一触即碎。"
    extend "\n想到这里，你缓缓伸出手。"
    ## 玻璃破碎音效
    ## 转场：黑屏
    scene bg_black_video with scene_soft
    $ current_music_scene = None
    stop music fadeout 1.0
    large_narrator "..."
    extend "\n......"
    extend "\n........."
    ## Extended大文本框结束
    $ current_music_scene = None
    stop music fadeout 1.0
    ## 沙漠中的脚步声
    ## 转场：银白色沙漠
    scene bg_desert with scene_soft
    ## 沙漠长风音效
    ## 抱胸站立，无奈表情
    wangshuang "喂，到了没啊？"
    ahe "没有。"
    ## 背手站立，面无表情
    wangshuang "那还要走多久？"
    ahe "到不了了。"
    ## 背手站立，吃惊表情
    wangshuang "啊？我们已经走了好久了诶。"
    ahe "或者说我们早就到了，但找不到对的骨头。"
    ## 抱胸站立，无奈表情
    wangshuang "你就一定要拼出一副完整的骨架才满意么？"
    ahe "不然好像我们也走不出这里。"
    wangshuang "啊...我当初就不该听你的鬼话和你一起来这里的..."
    ahe "不是挺好的么？像你这样整天坐办公室的，偶尔就需要走动走动。"
    ## 背手站立，吃惊表情
    wangshuang "就算要走路也别让我来沙漠里找骨头啊..."
    ahe "明明就是你自己要跟来的。"
    ## 抱胸站立，无奈表情
    wangshuang "呃呃呃我究竟中了什么邪才把你——"
    ahe "嗯？把我怎么？"
    ## 背手站立，默认表情
    wangshuang "没事，别在意。"
    ## Extended文本框开始 - accumulating textbox
    "..."
    extend "\n......"
    extend "\n........."
    ## Extended文本框结束
    ahe "嗯...大腿骨明明应该是最容易找到的才对..."
    ## 背手站立，默认表情
    wangshuang "这根不是？"
    ahe "那根我刚才试过了，髋关节对不上。"
    wangshuang "这边还有四五根，你都试过了？"
    ahe "诶？你是从哪儿找来的？"
    ## 抱胸站立，默认表情
    wangshuang "来的时候遍地都是啊，眼前一眼望去还有七八根。"
    ahe "所以精神科的也得会认骨头？"
    ## 抱胸站立，坏笑表情
    wangshuang "骨科可是我的强项。"
    ahe "有什么东西不是你的强项的么..."
    ## Extended文本框开始 - accumulating textbox
    "…"
    extend "\n……"
    extend "\n………"
    ## Extended文本框结束
    ahe "对上了诶。"
    ## 背手站立，默认表情
    wangshuang "我找来的，当然对咯。所以呢？接下来要做什么？"
    ahe "头骨..."
    ## 右手叉腰，左手食指竖起做讲解状，面无表情
    wangshuang "吼，只剩头骨了么...嗯...阿鹤啊——"
    ## 场景音乐参考：Stranger_Files, Sweet_Regrets，Whispers in the Twilight
    $ set_scene_music("route1_desert")
    ahe "嗯？"
    wangshuang "你知道自己在做什么，对吧？"
    ahe "拼一副骨架而已。"
    ## 背手站立，面无表情
    wangshuang "而已？你不会觉得光靠一副骨架就能把她带回来吧？"
    ahe "...!"
    ## 抱胸站立，面无表情
    wangshuang "与其尝试那种毫无意义的事情，直接离开也可以，门就在那边。"
    ahe "可是...我还..."
    wangshuang "你觉得执拗是一种美德么？"
    ahe "...我只是..."
    wangshuang "嗯，尽管继续骗自己。"
    ahe "...阿霜...之前这个梦里永远都只有我一个人...为什么这次你也在这里？"
    ## 右手叉腰，左手食指竖起做讲解状，默认表情
    wangshuang "因为我也能做同样的梦。"
    ahe "可是..."
    ## 背手站立，坏笑表情
    wangshuang "只不过我不会无聊到去尝试那种事情就是了。"
    ahe "可你...为什么要做这个梦？"
    ## 背手站立，默认表情
    wangshuang "当然是因为后悔咯，否则人是不可能来到这里的。"
    ahe "还有...能让你后悔的事？"
    wangshuang "当然。只要做过选择，就一定会后悔。"
    ahe "可如果你已经变成神了——"
    ## 抱胸站立，无奈表情
    wangshuang "哈？你在说什么呢？"
    ahe "好吧..."
    ## 背手站立，面无表情
    wangshuang "你想啊，无论我们做了什么事，那都意味着同一时空内其他行为的可能性被完全抹杀了，不是么？所以从定义上来讲，活着就是一场超长的悔恨之旅。"
    wangshuang "不过你也别觉得那是什么坏事。应该说，完全不需要后悔的认知架构才真的要人命。我之前专门做过这方面的研究。"
    ahe "什么研究？"
    ## 右手叉腰，左手食指竖起做讲解状，面无表情
    wangshuang "‘全知全能的代价’。"
    ahe "那和后悔一点都不相关吧..."
    ## 抱胸站立，默认表情
    wangshuang "别急，听我讲完你就懂了。"
    ## 右手叉腰，左手食指竖起做讲解状，默认表情
    wangshuang "所谓‘全知全能’，虽然听着像是造物主才被允许拥有的力量，但事实上以今天的技术，想要在有限时空里模拟这一状态不算难。"
    ## 抱胸站立，面无表情
    wangshuang "试想，假若在我们与杰罗瓦的最后一战里，你在见到他放出的{i}尤里娅{/i}的那一刻们就放弃了抵抗，会怎么样？一切就结束了对吧？"
    ## 背手站立，默认表情
    wangshuang "那你再想，如果我能把这段不存在的“记忆”高清模拟出来，数据化掉，然后灌回你脑子里。"
    ## 右手叉腰，左手食指竖起做讲解状，默认表情
    wangshuang "加上你脑子里原本就存在的记忆，这时让你同时体验选择支两边的事件，那在这样的认知草拟完成后，你是不是就已经实现对于这段记忆的‘全知全能’了？"
    ahe "可那样的话，记忆肯定会和现实发生冲突的吧。"
    ## 抱胸站立，面无表情
    wangshuang "当然，但假若两边的记忆，从肢体感官到事件次序，无不张弛有度地印在你脑海里，那对于一个不了解认知草拟的被试来说，该如何戳穿自己‘全知全能’的假象？"
    ahe "必须要外人点破才行。"
    ## 右手叉腰，左手食指竖起做讲解状，默认表情
    wangshuang "对，但不全对——即使有外人指出矛盾，又有多少人愿意摒弃自己的“切身体验”，转而允许他人的只言片语来定夺自己的认知？"
    ahe "..."
    ## 右手叉腰，左手食指竖起做讲解状，面无表情
    wangshuang "我们的实验数据也指向这一点——在草拟完成的三天内，所有被试都明确拒绝了外界干预，以不容置疑的姿态维持着选择支两边的草拟。"
    ahe "他们...在自行草拟？"
    wangshuang "没错。我们人工植入的认知流并没有在结尾处安排收束性事件，而在我们灌进去的认知与现实发生冲突后，被试们全部选择了无视现实，并开始自行草拟选择支两边的后续内容。"
    ## 抱胸站立，默认表情
    wangshuang "更有意思的是，所有被试在自行草拟的过程中多巴胺通路都在暴走，就仿佛这虚假的全知全能让他们——"
    ahe "成瘾了。"
    ## 右手叉腰，左手食指竖起做讲解状，得意表情
    wangshuang "Bingo！我们用计算生成的认知数据让人染上了成瘾性的精神分裂，而这——"
    ahe "就是全知全能的代价？"
    ## 抱胸站立，坏笑表情
    wangshuang "嘿嘿，别兴奋过头了，阿鹤。"
    wangshuang "一个人双线程草拟时需要的算力...这么说吧，会在草拟开始后的短时间内爆炸增长，而最初的草拟全是在被试脑内执行的...。"
    ahe "..."
    ## 抱胸站立，面无表情
    wangshuang "嗯，第一批被试的脑子大多都烧了，物理意义上的。后来第二批还动用了医院的计算机集群，最后效果也没好多少就是..."
    ## 抱胸站立，无奈表情
    wangshuang "所以说能后悔是好事啊，能用如此低成本的认知模式来替代脑细胞被烧干，是一桩好买卖。"
    ahe "那这个梦..."
    ## 背手站立，默认表情
    wangshuang "嗯，是我给自己搭的，用来强制认知收束的疗养院。后来发现效果不错，自然也就向一些VIP们开放咯。"
    ahe "你自己也参与了？"
    wangshuang "当然，我可是第一批被试。只是我的脑子不太一样，成瘾这个问题对我来说并不存在，可以随时自行结束草拟，所以可以在当被试的同时一边跟进实验。"
    ahe "所以为什么没有让其他被试来这里..."
    ## 抱胸站立，无奈表情
    wangshuang "哦...哈哈...这个嘛，毕竟当时搭得比较匆忙，这个梦境第一版的认知收束任务只能单线程地跑，慢得不行的同时还会很吃资源，所以就算开放了也救不了太多人...哈哈..."
    $ current_music_scene = None
    stop music fadeout 1.0
    ## 沙漠长风音效
    ahe "..."
    wangshuang "..."
    ahe "这就是你后悔的事情？"
    ## 抱胸站立，默认表情
    wangshuang "你觉得呢？"
    ahe "我怎么知道..."
    wangshuang "嗯，那还是保持无知比较好。"
    ahe "只要你心安理得就行..."
    ## 背手站立，面无表情
    wangshuang "..."
    ahe "所以这梦也是你那朴素过程的一部分？"
    ## 背手站立，默认表情
    wangshuang "那可不一样，现在能够来到这里的都是游离于朴素过程之外的异客。当他们离开这里时，我希望他们至少能明白自己为什么会这样游离。"
    ahe "唔，所以这也是你的实验的一部分，带课题的。"
    ## 右手叉腰，左手食指竖起做讲解状，默认表情
    wangshuang "不不不，这只是一个治疗场所而已。【右手叉腰，左手食指竖起做讲解状，得意表情】不过对于你来说...哼哼。"
    ahe "怎么了？"
    ## 抱胸站立，默认表情
    wangshuang "没事，我之前还在想，你为什么还能来到这里。不过从你刚才手上一直在忙活的事情来看，这早就不是问题了。"
    ahe "可你说它没有意义。"
    ## 背手站立，默认表情
    wangshuang "嗯，现在我也维持原判。"
    ahe "..."
    ## 抱胸站立，坏笑表情
    wangshuang "不想知道为什么？"
    ahe "不是很想。"
    ## 背手站立，默认表情
    wangshuang "行吧。毕竟我们有得是时间。"
    ahe "..."
    wangshuang "..."
    ahe "..."
    wangshuang "..."
    ## 右手叉腰，左手食指竖起做讲解状，得意表情
    wangshuang "嗯...但是我站累了，所以让我来告诉你吧——你要找的头骨并不存在，所以就算一直这样找下去，你也永远不会达到你的目的。"
    ahe "啊...可是...你是怎么知道的？"
    wangshuang "喏——"
    ## 原本王霜的位置闪过尸首的黑影
    with fx_shock
    ahe "啊——！"
    ## glitchy音效
    ## 背手站立，默认表情上蒙了glitch
    wangshuang "因为欧按物昆咽——"
    ahe "阿...霜？"
    ## 王霜面部开始出现glitch
    with fx_glitch
    ## glitchy音效
    ## 抱胸站立，坏笑表情上蒙了glitch
    wangshuang "啊啊呐唔一握艾鈤——..."
    ## glitchy音效
    ## 右手叉腰，左手食指竖起做讲解状，默认表情上蒙了glitch
    wangshuang "唵椅迩唵毋炆戊囮吔坳唔岙莪。"
    ## glitch消失
    with fx_glitch
    ahe "阿霜，你还好吗？"
    ## 抱胸站立，默认表情
    wangshuang "嗯？怎么了？"
    ahe "你刚才...当我没说。所以为什么头骨不存在？"
    ## 右手叉腰，左手食指竖起做讲解状，得意表情
    wangshuang "因为我看不见。"
    ahe "啊？"
    ## 王霜面部开始出现glitch
    with fx_glitch
    ## glitchy音效
    ## 尸首黑影闪过
    with fx_shock
    ## 背手站立，默认表情上蒙了glitch
    wangshuang "一焱髻暨戊馹曳葳邑吖霭肮毐峪镍醪！"
    ahe "喂...阿霜你又——"
    ## glitch消失
    with fx_glitch
    ## 右手叉腰，左手食指竖起做讲解状，得意表情
    wangshuang "哎，话又说回来，我也没说过缺了头骨就不行啊。"
    wangshuang "既然你这么想见她，那肯定得成全你嘛——你看，你的“作品”啊，从各种意义上已经完成了。"
    ahe "什——"
    ## 尤里娅登场
    ## 一般态默认
    youliya "你好，阿鹤。"
    ahe "诶？你——"
    youliya "嗯，我当然还活着。"
    ahe "可是...可是我..."
    ## glitchy音效
    ## 一般态面部glitch
    youliya "你豋炅宓恇蠹璱钅飰棏巠敪玸——"
    ahe "啊...等等...等一下！"
    ## 一般态默认
    youliya "嗯，又失忆了么...离我们上次分别也没过多久吧，阿鹤？"
    ahe "不是...{i}尤里娅{/i}...不对..."
    ## glitchy音效
    ## 一般态面部glitch
    youliya "喔，确实是不太对——。"
    ## 尤里娅消失
    ## 场景音乐参考：N2-07
    $ set_scene_music("route1_horror1")
    ahe "{i}尤里娅{/i}，{i}尤里娅{/i}？"
    ## glitchy音效
    ## 抱胸站立，默认表情上蒙了glitch
    wangshuang "飒炟曠莩皎靸礚睫覅是否解释你的诨涤？"
    ahe "啊...你们...你们...等等..."
    ## 尤里娅出现
    ## 一般态坏笑
    youliya "嗯...有什么好等的？只是撕碎了几百个长得和我一样的东西就承受不住了？这可不是我认识的阿鹤呢。"
    ahe "呃...啊...可是...可是..."
    ## 一般态邪恶表情1
    youliya "但那对你来说根本不重要吧，毕竟都是最后关头了，无论怎样都不能输给一群杰罗瓦控制的假人嘛！尤其那些东西只是长得和我一样而已，根本不需要任何同情。"
    youliya "只要你“看到”那些东西不是“我”，自然就可以随手杀掉了——一切都顺理成章，无可厚非，对吧？"
    ahe "..."
    ## 一般态默认
    youliya "可是阿鹤，你知道吗？所有复制体的感官都会回流到我的身体。"
    ahe "{i}尤里娅{/i}...这不是——"
    youliya "每根断掉的骨头、每滴流出来的血、每副碎掉的内脏——虽然对我来说这些痛苦并不真实，可那体验还是让我记忆犹新啊，每一次死掉。"
    ## 一般态坏笑glitch
    youliya "死掉诶...那就是你口中的“无法重复的深邃体验”吧。能连续体验那么多次，我是不是该...感谢你呢？"
    ahe "..."
    ## 一般态默认
    youliya "那么作为你的谢礼，让我来告诉你一点浅显的事实吧。"
    ## 一般态坏笑
    youliya "阿鹤哥，在逝乐园终结的前几天里，不只你自己，连你身边的大家，所有人都在演戏哦：我、王霜、米姐，全都一样。"
    ## 一般态默认
    youliya "你是不是觉得，只要强撑着送我离开了逝乐园，你就能得到解脱了？"
    ahe "——！"
    youliya "你是不是觉得，只要抛下你所拥有的一切，最可怕的下场无非就是死掉而已？"
    youliya "你是不是以为，只要假惺惺地承担起所有人的痛苦，你就能满足你那跳出日常的冲动了？"
    ## 一般态邪恶表情1
    youliya "完全不动脑子就接受这样的结论，简直是错得不能再错了啊，我一败涂地的救世主先生。"
    ## 一般态邪恶表情2
    youliya "那么——请见证你愚行真正的后果吧。"
    ## 场景音乐参考：N2-14，播放完一次N2-14之后，回到N2-07
    $ set_scene_music("route1_horror2")
    ## 尤里娅异变
    ## 炸裂jump scare音效
    ## 浑身伤痕累累仿佛由尸块缝纫而成的无头尸首登场
    ## 心跳音效
    ## 屏幕边缘开始随着心跳的节奏震动
    ahe "——么！！！"
    shishou "阿鹤，事到如今你又在害怕什么呢？这可是你亲手拼出来的身子哦。"
    ahe "啊...啊啊啊啊...啊啊啊啊啊啊啊啊啊啊——"
    ## 抱胸站立，默认表情
    wangshuang "别跑啊，这可是你们的感人重逢诶！"
    ahe "别过来！"
    shishou "阿鹤，我们还没聊完——"
    ahe "你别过来！！！"
    ## 进入一个向前跑动的sequence，可以是少量几帧透视感比较明显的画面，然后无限循环
    ## 做些古怪特效，世界有点崩解的感觉
    ahe "这不是真的这不是真的这不是真的这不是真的这不是真的这不是真的这不是真的这不是真的这不是真的这不是真的这不是真的这不是真的这不是真的这不是真的这不是真的这不是真的这不是真的这不是真的这不是真的这不是真的这不是真的这不是真的这不是真的！"
    ## 背手站立，默认表情
    wangshuang "阿鹤？"
    ahe "啊——！你为什么还在这里！"
    ## 抱胸站立，坏笑表情
    wangshuang "我当然在啦，她也还在——"
    shishou "哈喽~"
    ahe "别过来！你别过来！再见！"
    ## 重新开始跑动sequence
    ## 心跳音效渐强
    ahe "啊...保持呼吸...保持呼吸...保持呼吸...保持呼吸..."
    shishou "你好。"
    ahe "..."
    ## 背手站立，默认表情
    wangshuang "这就跑不动了？"
    ahe "...不要...过来..."
    wangshuang "要知道，你可是自愿来到这里的哦。"
    shishou "嗯。"
    ahe "我...一定...要...离开这里！"
    ## 抱胸站立，默认表情
    wangshuang "阿鹤啊，你倒是冷静下来仔细想想，你费了这么大力气把她拼凑出来，可当她真正活过来之后又无法直视她了？"
    ahe "这不是我想要的..."
    ## 背手站立，坏笑表情
    wangshuang "只因为她身子不完整？"
    ahe "这不是我想要的！"
    ## 右手叉腰，左手食指竖起做讲解状，得意表情
    wangshuang "那就把头埋进沙子里啊，那样你就什么都不用看了。"
    ahe "呃...啊——对不起——"
    ## 转场：图片黑屏
    scene black with scene_soft
    $ current_music_scene = None
    stop music fadeout 1.0
    ## 沙漠长风音效
    ## Extended大文本框开始 - accumulating large textbox
    ## 心跳音效恢复
    large_narrator "沙地冰凉而干燥，在这个无声的世界里，你艰难地呼吸。"
    extend "\n随着恐惧略微消散，你察觉到这地下似乎不像想象中那样黑暗，便试探性地睁开双眼，但立刻后悔了，因为你见到了比地面上那无头尸首更加令人绝望的恐怖——"
    extend "\n沙砾。"
    extend "\n满眼都是沙砾。但只消稍稍细看，那一颗颗的，分明就不是沙砾。"
    ## Extended大文本框结束
    ## 转场：眼珠背景
    scene black with scene_soft
    ## 心跳音效渐强
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "每颗“沙砾”都是一颗无色透明多面体。"
    extend "\n而每颗多面体里，都有一颗泛着血丝的眼珠。"
    extend "\n随着那些眼珠在你视野里逐渐清晰，它们似乎也注意到了你的存在。"
    extend "\n无数锥子般的目光将你刺得千疮百孔。"
    ## Extended大文本框结束
    ## 场景音乐参考：N2-14 - 从上次音乐停的位置继续播放，不要重头开始
    $ set_scene_music("route1_horror3")
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "你绝望地想要把头抽出来，但原本稀松的沙地此刻如钢钳一般将你的头死死扼住，任凭双手在沙地上狂乱地挥舞抓挠，也无法动摇分毫 。"
    extend "\n你只能眼睁睁看着那些布满血丝的眼珠朝你的脸逐渐聚拢，随后——"
    ## Extended大文本框结束
    ## 连续破裂音效
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "它们一颗颗地在你眼前爆裂开来，里面迸发出浑浊的玻璃体与血液的混合物，飞溅到你脸上，温热而粘稠。"
    extend "\n所剩无几的空气中弥漫着你闻所未闻的诡异气味。那是尸体的味道，但其来源并非布满你颜面的异色粘液。"
    extend "\n几团大块的血污顺着你的脸颊缓缓滑下，留下一道道蜗牛足迹般亮晶晶的轨迹。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "尸体的味道越发浓烈。"
    extend "\n嘴唇也沾上了血污，怎奈双手与头颅天各一方，你无法想象如何在不扩大事态的前提下将嘴唇清理干净，只能强行忍受温热湿软的污物在唇上缓缓滑落的触感。"
    extend "\n你极力缩紧喉头，拼尽全力不哇地一声吐出来，但那念头很快就被另一种思绪所覆盖了。"
    ## Extended大文本框结束
    ## 居中大字文本框开始 - centered large font textbox
    centered_large_narrator "你想——"
    ## 居中大字文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "尸体气味的浓度达到了顶峰。"
    extend "\n你十分清楚那气味的来源，只是仍在试图移开目光，就像你一直以来所做的那样。"
    extend "\n但一直逃避的人终究会无路可逃。"
    extend "\n当人制造了过多的尸体，那他自己迟早也会步入其造物的行列。"
    extend "\n一阵遥远而熟悉的冲动自心底涌上来。"
    extend "\n你想死。"
    ## Extended大文本框结束
    ## 转场：红屏
    scene black with scene_soft
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "手心传来温热而粘稠的触感，你自然知道那是什么，于是开始用力甩手。"
    extend "\n但无论你怎么使劲，那事物仍旧纹丝不动地包裹着你整个手掌。"
    extend "\n就像一副牢靠的手套。"
    extend "\n就像你的第二层皮肤。"
    ## Extended大文本框结束
    ## 闪现尤里娅破碎的脸
    ## glitch音效
    ahe "啊——！"
    ahe "对不起...对不起...对不起..."
    ## 大文本框开始
    large_narrator "对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起对不起"
    ## 大文本框结束
    ## 玻璃破碎音效
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "口中不断重复着同样的三个音节，直到语言失去意义，只剩下干涩的空气波动无情地敲打你的耳膜。"
    extend "\n血液骨髓脂肪溢出来。脂肪明黄。胆汁墨绿。血液暗红。"
    extend "\n手心粘稠依旧。"
    extend "\n痛觉早已麻木，你厚实的第二层皮肤将那无用的感官尽数咽下，同时把一种绝不可饶恕的体验传进你的血管，鞭辟入里。"
    ## Extended大文本框结束
    ahe "别...请不要..."
    ahe "啊...！"
    ahe "啊——不要——不要啊啊啊啊啊啊啊啊！"
    ## 居中大字文本框开始 - centered large font textbox
    centered_large_narrator "快感。"
    ## 居中大字文本框结束
    ## 居中大字文本框开始 - centered large font textbox
    centered_large_narrator "你回忆起了快感。"
    ## 居中大字文本框结束
    ## 闪现尤里娅破碎的脸
    ## glitch音效
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "你正欲一拳轰向自己的太阳穴死而后快，可你那呼啸的拳头却只能砸在软绵绵的沙地上，连自己的脸颊都碰不到就泄尽了力气。"
    extend "\n呕吐欲再次升翻涌起来。"
    extend "\n你屏住呼吸，一拳拳砸向沙地，却始终徒劳无功。"
    extend "\n把头颅从沙地中抽出也做不到，沙地像断头台的木枷般将你头颅死死扼住。"
    extend "\n而刀板则迟迟不落下。"
    extend "\n它在等你自己动手。"
    ## Extended大文本框结束
    ## 骨头断裂音效
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "无力忍耐眼前非人的幻象，你死死扼住自己沙地以上的脖颈。"
    extend "\n锁骨似乎断了，但那疼痛反倒让呕吐欲减轻了些。"
    extend "\n脑血管轰鸣，视野四周开始坍缩，黑暗自无形中侵入进来。"
    extend "\n地心引力渐强，你的身躯逐渐被沙砾吞没。窒息终于在眼球中冒出的血污将你口鼻覆盖之前到来了。"
    extend "\n死亡，你此刻唯一的救赎，她在你面前舒展开魅惑的身躯。"
    extend "\n黑暗，一切都坠入黑暗，你的视野、身躯，你无际的意识。"
    extend "\n黑暗。"
    ## Extended大文本框结束
    $ current_music_scene = None
    stop music fadeout 1.0
    ## 心跳音效停
    ## 转场：黑屏，但是里面盖着王霜微笑的幽灵
    scene black with scene_soft
    ## Extended大文本框开始 - accumulating large textbox（不分句）
    $ no_click_split = True
    large_narrator "——但你也不能就这样一走了之。"
    extend "\n——你早就明白这一点了。"
    extend "\n——即使如此也要继续折磨自己？"
    extend "\n意识消散的前一刻，你依稀听见一个温柔声音在你耳边低语。"
    extend "\n——不如再次伸出手去，撕——"
    $ no_click_split = False
    ## Extended大文本框结束
    ## 电视机关机音效
    ## 电视机关机转场
    ## 转场：图片黑屏
    scene black with scene_soft
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "..."
    extend "\n......"
    extend "\n........."
    ## Extended大文本框结束
    ## 脸入水后冒泡泡的音效
    ## 转场：虚空对视
    show void default with scene_dissolve
    wangshuang "欢迎回来。"
    ahe "倒不如去死。"
    wangshuang "哦？为什么呢？"
    ahe "不好意思...我觉得我有点...不对劲..."
    wangshuang "嗯，看起来也是。那就出去吧，我们。"
    ahe "只要那样就能好起来吗？"
    wangshuang "就上次的经验来说，算是相当有效呢。"
    ahe "好吧...听你的...总没错的...对吧..."
    wangshuang "当然了，我们走吧。"
    ## 转场：完美夏日
    scene black with scene_soft
    ## 场景音乐参考风格：樹氷の輝き (岸部真明)，夜の向日葵（素晴日bgm），Running Waters - https://audionautix.com/Music/RunningWaters.mp3 (Jason Shaw)，Shianchu - 同场景不复用配乐的话，换成这首还挺合适的
    $ set_scene_music("route1_return")
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "你跟在王霜身后，穿过无形的门。"
    extend "\n门后是淡金色的细腻沙滩和蔚蓝的海，略带盐味的小风，耳畔是轻柔起伏的浪声。"
    extend "\n空无一人的海滩上，完美的夏日拉开序幕。"
    extend "\n你觉得眼前图景似乎触动到了心中的某个隐秘的角落，却怎么也抓不住那感觉，只好作罢。"
    extend "\n仿佛那感觉并不属于你。"
    ## Extended大文本框结束
    ahe "这里...很舒适。"
    wangshuang "对。"
    ahe "应该感到快乐与安逸吗，像现在这样？"
    wangshuang "当然，不用想那么多。"
    ahe "可是很难不在意啊。如果快乐与安逸如此简明，那我们之前所做的一切又是为了什么..."
    wangshuang "那当然也是有意义的，毕竟它让我们回到了这里。"
    ahe "...所以这就是你想让世人体验的世界吗？一个完美且静止的夏日？"
    wangshuang "不，世人的想法与我无关。"
    ahe "所以为什么要——"
    wangshuang "阿鹤，你一定要知道吗？"
    ahe "..."
    wangshuang "如果你连这样的决心都下不了，还请你继续盯着眼前的画面，再多做几个梦，而不是在这里问我无意义的问题。"
    ahe "..."

    menu:
        extend ""
        "我想知道":
            wangshuang "那就继续想去吧。眼前风景足够你继续想一阵子了，等你想明白了，你自然知道来什么地方找我。"
            ## Extended大文本框开始 - 大文本框分句
            large_narrator "丢下这句话，阿霜便化作一阵轻烟消散了，只在完美夏日光景里留下孤零零的你。"
            extend "\n你其实早就下定决心要弄明白阿霜心里那些令你不安的事情，但一时的迟疑终究遭致永远的败北。"
            extend "\n想不出来，根本想不出来。"
            ## Extended大文本框结束
            ## Extended大文本框开始 - 大文本框分句
            large_narrator "你木讷地盯着王霜原本站立的位置，视野逐渐模糊起来。"
            extend "\n越是尝试回想那女人的脸庞，她就越显得陌生。"
            extend "\n你也越发清醒地意识到，即使在逝乐园里一起厮混了七八年，你还是根本不了解这个给你故乡带来灾变的女人。"
            extend "\n你熟知她出租屋的潮湿空气，也了解她几乎不加任何调味料的寡淡饮食，却从未胆敢踏足她内心真正黑暗的角落。"
            extend "\n你只知道，有一种令你望而却步的毁灭冲动从那角落里弥漫出来，而你也就因此止步不前了。"
            ## Extended大文本框结束
            ## 居中文本框开始 - centered textbox
            centered_narrator "于是，王霜永远地消失了。"
            ## 居中文本框结束
            ## Extended大文本框开始 - 大文本框分句
            large_narrator "而你则在她留给你的完美夏日中，徒劳地坐守着取之不尽用之不竭的欢欣。"
            extend "\n淡金色的细腻沙滩，蔚蓝的海，略带盐味的小风，轻柔起伏的浪声。"
            extend "\n在空无一人的海滩上，你逐渐感到有些怅然若失。"
            extend "\n你很清楚，那是不属于你的情感，但其感受之真切，又让你不得不偶尔正视它的分量。"
            ## Extended大文本框结束
            ## Extended大文本框开始 - 大文本框分句
            large_narrator "可终究是难以得出定论。"
            extend "\n当云雾聚散、潮涨潮落上万次之后，你逐渐归纳出了风儿与海浪的行动规律。"
            extend "\n你也曾尝试过行走起来、奔跑起来，但最后总会如期回到原地。"
            extend "\n云雾会继续聚散，潮汐也会继续涨落，于是百思不得其解的你，便只好在完整且无限的生命中无止境地留守下去。"
            ## Extended大文本框结束
            "Bad End 1: 举棋不定"
            ## Bad End 1：举棋不定
            $ unlock_ending("bad_end_1")
            return
        "我必须知道":
            wangshuang "这样么...你可一定要想明白，开弓可就没有回头箭了。"
            ahe "我说了，我必须知道。"
            wangshuang "哈。行啊，那你闭上眼睛。"
            ahe "..."
            ## 转场：黑屏
            scene bg_black_video with scene_soft
            ## 水中探头出水的音效
            wangshuang "可以睁眼了。"
            ## 转场：灰白夏日1
            scene black with scene_soft
            ahe "这..."
            wangshuang "我眼中的世界——或者说，在我们来到这完美的夏日海滩之前，我眼中的世界。"
            ahe "你的灰..."
            wangshuang "怎么样？是不是挺无聊的？"
            ahe "可是，等等，那些眼睛——"
            wangshuang "哦，对，都忘了它们还在了。它们一直都在那儿，不会把你怎么样的，只要你不乱来。"
            ahe "乱来？指的是什么？"
            wangshuang "不用担心啦，我看你现在这样子也没什么乱来的能力。"
            ahe "好吧..."
            ## Extended大文本框开始 - 大文本框分句
            large_narrator "确实如此，在包容的灰幕中，你感知不到任何危险。"
            extend "\n一切都让你感到超乎常理的安全，仿佛置身母亲温暖的怀抱之中。"
            extend "\n“比较”不再重要。在灰的抚慰下，事物不再具备它们原本的质地——仅仅是灰而已，平整、柔软、不加修饰。"
            extend "\n“边界”不复存在。在灰的调剂下，事物之间的隔阂分崩离析，相互流进彼此，在同一张灰色的网下成为同样的事物。"
            ## Extended大文本框结束
            ## 居中文本框开始 - centered textbox
            centered_narrator "但你很快就意识到，这一切都与你无关。"
            ## 居中文本框结束
            ## Extended大文本框开始 - 大文本框分句
            large_narrator "远处沙滩上的眼睛并不是你的眼睛。它只是幽幽地观望着你的一举一动。"
            extend "\n你与事物之间的隔阂一如既往地高耸着。"
            extend "\n你迫切想要融入灰，但这愿望越是强烈，你就越感到身处深灰色的海底，周身却干燥无比。"
            extend "\n窒息。因为这一切都与你无关。"
            ## Extended大文本框结束
            ahe "我想回去了。"
            wangshuang "移开目光可帮不到你哦。"
            ahe "我们回去吧。"
            wangshuang "当然，回头就行。"
            ## 转场：灰白夏日2
            scene black with scene_soft
            ahe "门呢？"
            wangshuang "如你所见，门已经不在了。"
            ahe "回不去了吗？"
            wangshuang "当然回得去，只要你想。"
            ahe "可我..."
            wangshuang "不太自信嘛，阿鹤。"
            ahe "这...难道就是来到这里的代价？"
            wangshuang "嗯...如果一定要说的话，连代价也说不上，因为你只看到了其中的一角。"
            ahe "但你想要离开这里其实易如反掌吧？"
            wangshuang "没错，但我不会这么做。"
            ahe "与其把我困在这里，用这时间去做些更有意义的事情不好吗？"
            wangshuang "我不想重复说过的话，阿鹤。你所知的一切都已经结束了，这里只有完美的夏日，以及你和我。"
            ahe "你和我的重要性是？"
            wangshuang "没有重要性，只是存在而已。"
            ahe "好吧..."
            wangshuang "我印象里的你偶尔还是会挣扎一下的。"
            ahe "...我累了。"
            wangshuang "巧了，我也累了。但这里不存在睡眠，我们只能望着它，直到不累为止。"
            ahe "那就这样吧。"
            ## Extended大文本框开始 - 大文本框分句
            large_narrator "倦意填满了你的全部意识，但你无论如何也无法入睡。"
            extend "\n在灰白夏日的牢笼中，你与王霜四目相对，连说话的力气也没剩下。"
            extend "\n眼前的女子既是狱长，又是囚徒，你们在她一砖一瓦精心搭建的完美监狱中意识清醒地度过无限的时间。"
            ## Extended大文本框结束
            ## Extended大文本框开始 - 大文本框分句
            large_narrator "并不是一场对杀或审问，只是沉默的两人在完整的世界里等待崩溃的发生。"
            extend "\n数千或数万次潮起潮落后，你终于下定决心问王霜太阳是否会在某个时刻落下或爆炸，但还未张嘴就打消了这个念头。"
            extend "\n你看见她心满意足地望着眼前一成不变的光景，双眼里只留下了某种接近疯狂的极乐。"
            extend "\n万物皆落入她深邃的眼底，在光信号到电信号的转码过程中被碾得粉碎，逐渐成为更加无意义的存在。"
            ## Extended大文本框结束
            ## Extended大文本框开始 - 大文本框分句
            large_narrator "你也不例外，任她将你纳入视野的巨大黑洞中，成为幅员辽阔的空虚的一角。"
            extend "\n那精致而脆弱的空虚，只能在这绝对无尘的美好光景中存在，连一丝空气的振动都会令其在顷刻间支离破碎。"
            extend "\n你决定保持沉默。"
            extend "\n她并不是囚徒。"
            extend "\n她从来都不是囚徒。"
            extend "\n这里的囚徒只有你一人。"
            extend "\n你只能继续等待下去。"
            extend "\n等待下一次——"
            ## Extended大文本框结束

    ## 灰幕开始冒泡泡，屏幕四周开始被黑色侵蚀
    ## 最后只剩下一片纯黑幕和一块无色透明多面体
    ## 从水中探头+大口吸气音效
    ## 转场：黑屏
    scene bg_black_video with scene_soft

    ## Route 1 结束
    $ unlock_route(1)
    return