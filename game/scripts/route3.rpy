## route3.rpy
## Route 3

label route3_start:

## 三周目：“完美夏日”

    ## 头入水，气泡音效
    ## 转场：无色透明多面体
    scene bg_polyhedron_video with scene_soft
    ## 还是无色透明多面体，但这里看起来像是从水底往上看那样
    ## 场景音乐参考：Electric Sea (Buckethead), Padmasana (Buckethead)，DoutokutosetsuShinsou no reijouGaidankousetsu - 物语ost是好文化
    $ set_scene_music("route3_opening")
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "冷。"
    extend "\n刚回过神来，周身的彻骨寒冷就让你想要立刻回到梦乡里去。"
    extend "\n然而睡眠如洋流般一去不复。只好仰面浮着，无言望着头顶唯一的光源。"
    extend "\n事到如今，眼前的景象已经再熟悉不过了：悬在天顶的无色透明多面体，无所事事的你等待着变化发生。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "然而转变迟迟没有发生。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "在彻骨的极寒中，一切都有如冰封般凝滞。"
    extend "\n这也是代价么？"
    extend "\n嗯...或是代价的利息？"
    extend "\n究竟在这冰雕中困了多久了呢？"
    extend "\n刚和他说了时间没意义没意义的，到头来自己还不是随时都挂念着。"
    extend "\n心口不一的东西。"
    extend "\n早就忘了自己为什么在这里，只模糊地记得你似乎曾经犯下过某种不可饶恕的罪行。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "所以审判者是谁？"
    extend "\n哎...留给他去想吧。"
    extend "\n连同意识一起夺去也无妨。"
    ## Extended大文本框结束
    ## 场景逐渐模糊
    call screen route_title(_("完美夏日"))
    ## 场景重新清晰
    ## 转场：灰屏水母
    scene black with scene_soft
    ## 场景音乐参考：Shiniki - 神前晓是我爹
    $ set_scene_music("route3_shiniki")
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "水母。"
    extend "\n你刚回过神来，周身那温暖而危险的触感就让你明白了自己的处境。"
    extend "\n痛觉如排山倒海般袭来，但你并没有因此而痛苦。你的身体早已超越了会因为痛觉而感到痛苦的程度。"
    extend "\n反而是随着痛觉而来的全新知觉引起了你的好奇。当你试图蜷起手指时，水母的一角也产生了细小的抽动。"
    extend "\n在巨大的水母体内，那本是你绝对无法感知到的遥远角落，但如今那里的触感就如你的指尖一样清晰。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "通过毒液，你与水母连接在一起。"
    extend "\n向上！"
    extend "\n掌握水母的行动方式之后，前进的方向也清晰无疑了。"
    extend "\n向上游！"
    extend "\n水面看起来近在咫尺，似乎只要伸出任何一条触手就能够到那水面上的无色透明多面体。但你知道事情远没有看上去那么简单。"
    extend "\n全神贯注地控制着每一寸身体组织，你奋力舒张又收缩，依凭着水体阻力的反作用力将你庞大的身躯向上托去。"
    extend "\n仅这一次动作就几乎耗尽了你的全部心力。"
    extend "\n而王霜竟独自一人创造并控制着这整个巨物？"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "无暇顾及这些无意义的思绪，你试着重新集中精神，再次上路。"
    extend "\n收缩。"
    extend "\n舒张。"
    extend "\n收缩。"
    extend "\n舒张。"
    extend "\n浑身肌肉因前所未有的精神压力而死死绷住，仿佛要向内坍缩那样狠狠挤压着骨骼与内脏。全身上下的血管都钟鼓齐鸣地跳动，像是昂扬的丧钟。"
    extend "\n收缩。"
    extend "\n舒张。"
    extend "\n收缩。"
    extend "\n舒张。"
    extend "\n你竭尽全力地向上游去，可水面却与之前无异，依旧看起来近在咫尺。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "漆黑的天空与其唯一的光源，如同水母的心脏般触手可及。"
    extend "\n但你已经彻底精疲力竭了。"
    extend "\n幽暗的深海伸出无数漆黑的手，它们抓住你的每一寸身体组织，有条不紊地将你拉回本就属于你的深渊。"
    extend "\n只能止步于此了么？"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "也许直到最后，你只是一个过于不知天高地厚的无名之辈而已。"
    extend "\n接下王霜的请求又是为了什么呢？"
    extend "\n为了你那病入膏肓的伪善？"
    extend "\n伸出最后几条还能动的触手，你竭尽全力试图去摘取头顶那无色透明的多面体。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "出乎你意料的是，你确实探出了水面，但很快又陷入了绝望。"
    extend "\n水面之上确实一无所有——你是早就清楚这一点的，却仍然执拗着要去摘取那虚假的幻象。"
    extend "\n也许实实在在地接触到虚无并不是毫无意义的。"
    extend "\n也许那是第一步。"
    ## Extended大文本框结束
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "深海的手臂仍在拖拽你的躯体，但你已在毒液带来的麻木中释然。"
    extend "\n探出海平面的肢体在水面之上的虚空中定格。"
    extend "\n漆黑的海水中，没有什么能够再伤害你，你感到温暖而祥和。"
    extend "\n就像一个梦一样，只要醒来就会消散。"
    extend "\n所以，该醒来了。"
    extend "\n只要把自己慢慢拉到水面就可以。"
    extend "\n..."
    extend "\n......"
    extend "\n........"
    ## Extended大文本框结束
    ## 转场：黑屏
    scene bg_black_video with scene_soft
    ## 风声
    ## 转场：银白色沙漠
    scene bg_desert with scene_soft
    ## 场景音乐参考：Shitagokoro - 一些非常适合唠嗑的音乐
    $ set_scene_music("route3_chat")
    wangshuang "早上好。"
    ahe "我以为你不会再回来了。"
    wangshuang "如果这是你的愿望的话，以你现在的能力实现起来并不难呢。"
    ahe "所以有什么事？我还得把这东西搭完——"
    wangshuang "能让我也帮点忙吗？"
    ahe "啊？帮什么？"
    wangshuang "那个头骨，我也想帮忙搭。"
    ahe "这不是你最看不起的事情么？"
    wangshuang "这叫不耻下问。"
    ahe "那可真是辛苦你了..."
    wangshuang "所以，让我也做点什么吧。"
    ahe "如果这么想帮忙的话，大可从我手里直接夺去，就像你一直以来做的那样。"
    wangshuang "夺取从来都不是我的本意。"
    ahe "但也无一例外地去做了。"
    wangshuang "你是想让我认错？"
    ahe "那倒也不至于。我只是觉得，在拥有一切之后，现在你反倒要向一个下仆乞求手艺活做，挺滑稽。"
    wangshuang "这和你...我们可以不讨论这个问题么？"
    ahe "好吧好吧...所以，你想帮我做什么？"
    wangshuang "帮你把{i}尤里娅{/i}搭好，这样就行。"
    ahe "我没有在搭{i}尤里娅{/i}。她已经离开这里了。"
    wangshuang "哦，怪不得最近没见到她。那这是？"
    ahe "只是兴趣使然的工程而已。当然，也是这沙漠里唯一能做的事情。"
    wangshuang "无论有什么能帮上忙的地方，请让我帮你吧。"
    ahe "当然，喏，这是接近完工的半成品，你把剩下的部分完成就行了。"
    wangshuang "可那样的话，你不就无事可做了么..."
    ahe "无妨，我去捏下一个就行。"
    wangshuang "唔..."
    ahe "那你接着。"
    ## 投掷音效
    wangshuang "...嗯..."
    ## Extended文本框开始 - accumulating textbox
    "…"
    extend "\n……"
    extend "\n………"
    ## Extended文本框结束
    wangshuang "不好意思...搞砸了..."
    ahe "无妨，本来就是精细活，刚上手捏不工整很正常。重头来过就是了。"
    wangshuang "好..."
    ## Extended文本框开始 - accumulating textbox
    "…"
    extend "\n……"
    extend "\n………"
    ## Extended文本框结束
    wangshuang "这个...稍微好一点？"
    ahe "勉强能行，你放那边吧。"
    wangshuang "好..."
    ## Extended文本框开始 - accumulating textbox
    "…"
    extend "\n……"
    extend "\n………"
    ## Extended文本框结束
    wangshuang "这样应该就行了？"
    ahe "嗯，不错，看来你已经学会了。"
    wangshuang "那接下来呢？"
    ahe "接下来？当然是继续捏咯。"
    wangshuang "可继续捏下去的话..."
    ahe "你当然也可以离开。"
    wangshuang "啊...我不是那个意思。"
    ## Extended文本框开始 - accumulating textbox
    "…"
    extend "\n……"
    extend "\n………"
    ## Extended文本框结束
    ahe "学得真快啊，阿霜，我刚上手时捏出来的可没这么像模像样。"
    wangshuang "我好歹也是学过医的..."
    ahe "科班出身就是好。"
    wangshuang "阿鹤。"
    ahe "怎么了？"
    wangshuang "我们到底要捏多少才算完？"
    ahe "和这沙漠里的沙子一样多就够了。"
    wangshuang "可那——"
    ahe "当然，沙子会不够用，但那不重要。继续捏下去就行了。"
    wangshuang "为什么要一直做这样...无意义的事情..."
    ahe "因为这是这沙漠里唯一能做的事情。"
    wangshuang "可我们为什么不离开这里，去找些更加——"
    ahe "更加有意义的事情？"
    wangshuang "..."
    ahe "‘一切都是无意义的’，‘时间已经结束了’，这些都是你告诉我的，阿霜。"
    wangshuang "..."
    ahe "所以你到底在追求什么呢？"
    wangshuang "阿鹤，我问你，如果你把一切都办成了，Succumus关停，{i}尤里娅{/i}得偿所愿，你也不再被逝乐园追杀，那之后你准备做什么？"
    ahe "我大概会重新回去上班。"
    wangshuang "那也太...无聊了..."
    ahe "嗯，我也这么觉得。风风火火闹了一通之后，反而要一头扎回那避之不及的‘日常’，所有的努力全都打了水漂，无论怎么看都是一种非常令人恼火的结局。"
    ahe "但我又在想，逃脱日常后的生活终究会变成日常，那之后我岂不又回到原点了？等到那一天，我现在所唾弃的‘日常’大概又会变得诱人起来。"
    ahe "就像捏玻璃头骨，总会厌倦。这时什么都比不上新鲜的东西——离开这里，去别的地方，做别的事情，只要这样的想法就足以让人满足了。"
    wangshuang "可你这分明是在倒果为因...在开始捏这些头骨时，我们的目的显然不是为了最终去做别的事情。"
    ahe "但当你捏完第一百五十个头骨时，你更愿意继续捏下去，还是把这里的完美夏日抛之脑后，回到原来的生活？"
    wangshuang "我绝不会离开这里。"
    ahe "那一千个、一万个，要是这工作无限延续下去，你也宁愿死守现状？"
    wangshuang "...我...不知道..."
    ahe "这大概也是你说的“朴素过程”，可它的本质就是虚无吧！你只是不愿直呼其名而已，明明都已经沉溺其中了，还在装看不见。那灰幕只会持续下去。"
    wangshuang "我的病已经完全痊愈了！"
    ahe "那为什么你现在在这沙漠里？"
    wangshuang "啊？你在说什么？"
    ahe "如果这完美的夏日已经彻底治愈了你的病，那你为什么还要创造无数个其他的世界？为什么不永远呆在你那完美的海滩上？"
    ahe "如果你的病已经好透了，那你现在来找我捏玻璃又是为了什么？"
    ahe "要我看，你还在病着，只是比之前更会演了。"
    wangshuang "..."
    ahe "你想逃离这里，就像从现实里逃出来那样。"
    wangshuang "..."
    wangshuang "......"
    wangshuang "........."
    wangshuang "阿鹤，推理得很漂亮...但我根本没有离开这里的动机啊。"
    ahe "..."
    wangshuang "即使你刚才列举的那些观察都指向了你的假设...可没有任何一条证据直接佐证你的结论啊。"
    ahe "...哈哈..."
    wangshuang "光冷笑可当不成证据。"
    ahe "阿霜，证据都在这里了——我们在现实中一起完成了某件“壮举”，所以如果想要在草拟中重现类似的事件，我们俩同时在场无疑是最简单的方案。"
    wangshuang "..."
    ahe "需要我说得更明白吗——你把我复原出来，就是想把这地方像逝乐园那样毁掉，对吗，王霜？"
    wangshuang "..."
    wangshuang "可是——"
    wangshuang "..."
    wangshuang "......"
    wangshuang "哈哈...哈哈哈哈哈...我曾经以为只有我能把你一眼望到底，没想到还有今天呐..."
    ahe "你给了我很多提示。"
    wangshuang "从没想过...即使一切都按照计划进行了...最后还是落得一场空..."
    wangshuang "哈哈...真是的..."
    wangshuang "阿鹤...我累了...我们回去吧..."
    ## 转场：完美夏日
    scene black with scene_soft
    ## 非常轻微的嘈杂人声
    ## 场景音乐参考风格：Jellyfish - https://audionautix.com/Music/Jellyfish.mp3  (Jason Shaw)
    $ set_scene_music("route3_jellyfish")
    wangshuang "..."
    ahe "..."
    wangshuang "阿鹤，你知道为什么这里长这样吗？"
    ahe "你从没讲过。"
    wangshuang "当然，我没有和任何人讲过。所有意识的终点之所以是夏日的海滩，是因为在我们初次见面时，我第一次看到了太阳的颜色。"
    wangshuang "那是我从没见过的美丽色彩啊，既温暖又明亮，仿佛那光晕能够包容一切。相比之下，平时看到的灰色就显得更加让人想死了。"
    wangshuang "后来{i}尤里娅{/i}告诉我，说与阳光最般配的地方当然是一片美丽的海滩。要有小风吹着，暖暖的太阳晒着，人们可以毫不顾忌地躺着，直到一切烦恼都消散掉。"
    wangshuang "那时我就决定了，在一切结束之后，如果只剩下一片完美的海滩，其中只留下你我二人，在永恒的完美里腐烂，也许就够了。"
    ahe "所以是什么改变了你的想法呢？"
    wangshuang "我从没改变过想法，反倒是你，刚复原出来马上就跑得没影了。"
    ahe "你一上来就让我盯着太阳看，任何意识都会立刻消散的吧！"
    wangshuang "之前实验的时候就没有遇到过这样的问题..."
    ahe "那怪我咯。"
    wangshuang "当然怪你，不过结果似乎也不坏..."
    ahe "因为我按你设想的那样，把你逼入死角了？"
    wangshuang "和那没关系..."
    ahe "真的？"
    wangshuang "你好烦啊！"
    ahe "话说啊，这里和之前来时感觉不太一样了。"
    ## 轻微嘈杂人声变得略响
    wangshuang "因为这里是蜂巢的源头，所有人的意识都储存在这里。现在你就可以放手去摧毁一切了。"
    ahe "摧毁？为什么要我来做？"
    wangshuang "因为这是你的使——"
    ahe "这难道不是你的愿望么？"
    wangshuang "..."
    ahe "阿霜，就算华佗再世也治不好一个不愿被救治的病人。"
    wangshuang "..."
    ahe "阿霜，我是认真的，你赋予我的使命已经结束了，接下来你得去实现你自己的愿望。"
    ## Extended文本框开始 - accumulating textbox
    wangshuang "你不明白...你不明白！我放弃了一切，只为了抵达这里！"
    extend "\n所以...即使会患上新的病，即使一切都因此而停下来了...我也..."
    extend "\n我也..."
    ## Extended文本框结束
    ahe "你也要移开目光么？"
    wangshuang "我没有！眼前这一切就是我想要的，我是绝不可能亲手把它毁掉的啊！"
    ahe "哦，所以直到最后一刻也要借刀杀人么。"
    wangshuang "不是的，阿鹤！我把你还原出来，只因为我想要你在我身边！"
    ahe "哦，所以我只是一管用来完成你作品的颜料。"
    wangshuang "阿鹤，请你相信我！我真的...真的只想再见到你...我要做什么才能让你相信我..."
    ahe "这个问题的答案，你自己也清楚。"
    ahe "只要这个世界还存在，只要我还能在这个海滩上看到你，你说的话就没有任何意义。"
    wangshuang "阿鹤...我..."
    ## Extended大文本框开始 - accumulating large textbox
    large_narrator "王霜一副欲言又止的样子，她水蓝色的双眼中流露出因认命而产生的淡淡悲戚，但很快又被你熟悉的坚毅神色所替代。"
    extend "\n沉默良久后，她站起来，背对着你，右手在衣兜里摸索着。"
    extend "\n不难看出，她早就摸到她要找的东西了，只是在即将取出的当口踌躇着。"
    extend "\n最终，她长出一口气，头微微一点，从裤兜里抽出右手。她指尖捏着的，分明是一颗你见过无数次的无色透明多面体。"
    extend "\n她回头看看你，脸上挂着你难以读懂的表情，随即把那多面体丢在金黄的沙滩上。"
    extend "\n接触到沙滩的一刹，那多面体很快像一滴水珠似的消失得无影无踪，仿佛它从始至终都是液体。"
    ## Extended大文本框结束
    ## 场景逐渐开始变灰
    ## 转场：灰白夏日1
    scene black with scene_soft
    "你正要开口，却见王霜从口袋里取出了另一颗一模一样的多面体，略作犹豫后把它也丢在了沙滩上。"
    "之后的一切在无言中徐徐展开。王霜在沉默中一颗接一颗地丢弃着无色透明多面体，而你则无声地观看这场盛大且无声的毁灭表演。"
    ahe "其他人不会反对吗？"
    wangshuang "大概会吧，但蜂巢已经被你降服了，其他意识的反对票也就不再有效了。"
    ahe "啊？那是什么时候的事情？"
    wangshuang "不知你还记不记得在某片深海里，有一只水母。"
    ahe "哦，所以把我硬生生塞进那水母里的也是你？"
    wangshuang "谁知道呢。"
    "随着越来越多的多面体被丢弃在沙滩上，喧嚣声逐渐轻下来，而许久未见的灰幕也开始侵蚀视野周围。"
    ## 场景完全变灰
    ## 无声
    wangshuang "结束了。"
    ahe "还有我的，给你。"
    wangshuang "我不要。"
    ahe "都到最后了还要逃避么？"
    wangshuang "你他妈的！"
    "王霜从你手中夺过最后的多面体，振臂扔向大海。"
    ## 扑通音效
    ## 转场：甜品店
    scene black with scene_soft
    "..."
    ## 扑通音效
    ## 转场：灰屏水母
    scene black with scene_soft
    "......"
    ## 扑通音效
    ## 转场：银白色沙漠
    scene bg_desert with scene_soft
    "........."
    ## 扑通音效
    ## 转场：黑屏
    scene bg_black_video with scene_soft
    "......"
    ## 碎裂声
    ## 转场：灰白夏日1
    scene black with scene_soft
    "..."
    ahe "你看，只要你不愿意放弃，它就又回来了。"
    wangshuang "阿鹤..."
    ahe "怎么了？"
    wangshuang "真是的...无路可逃了啊..."
    ahe "把自己关进这样一个小世界里，当然没有多少逃的余地。"
    wangshuang "你离开这里之后，真的会回去上班吗？"
    ahe "大概吧，要是有班上的话。"
    wangshuang "真他妈的无聊啊..."
    ahe "你呢？"
    wangshuang "..."
    ahe "你离开之后准备做什么？"
    wangshuang "我...哪儿也不去。"
    wangshuang "其他人的意识已经全部释放了，但这里离彻底消失还早，所以我会守在这里，直到它完全崩溃为止。"
    ahe "我还能再见到你吗？"
    wangshuang "想要见到我的肉体的话，来我家就行了，大概在床上躺着吧，你对它做什么都无所谓。"
    ahe "阿霜，我们一起回去吧。"
    wangshuang "我不要。"
    ahe "可是这里已经什么都不剩了，你没必要为它陪葬。"
    wangshuang "这不是陪葬。这是...已经...拖了太久了。"
    ahe "可是——"
    wangshuang "别说了，从来到这里的那一天起，我就从来没有想过要离开。"
    ahe "即使要在凝滞中永远停留下去？"
    wangshuang "现在我心情非常好，好得不能再好了，所以能麻烦你不要再在这里像蚊子一样嗡嗡作响吗？你让我做的，我全都做到了，Succumus关停了，逝乐园已经得救了，你也自由了。"
    wangshuang "我也什么都不剩了，所以能请你把这最后一点自由留给我自己吗？"
    ahe "好吧...那我——"

    menu:
        extend ""
        "把手中的无色透明多面体丢在了沙滩上":
            ahe "再见了，阿霜。"
            wangshuang "赶紧滚蛋。"
            ahe "如果你哪天回心转意的话，你知道去哪儿找我。"
            wangshuang "我们不会再见面了。"
            ahe "这样...那希望...你也能找到自己的答案。"
            ## 转场：黑屏
            scene bg_black_video with scene_soft
            ## Lovely Summer Time背景音乐：https://samply.app/p/zKOVrHFVD1PKSd4AyAhf?si=mhZIQjsjvpeL1K96BgcnRriTvN52
            $ set_scene_music("route3_lovely_summer")
            ## Extended大文本框开始 - 大文本框分句
            large_narrator "熟悉而陌生的音乐，在你睁眼前就萦绕在你脑海。"
            extend "\n那慵懒而色彩斑斓的旋律让你想起某个熟悉的面孔，但无论如何也记不起那人的名字。"
            extend "\n你只记得，你好像和那人一起做了一个长长的梦。"
            extend "\n在那梦里，你们上天入地无所不能，还能肆意掌控着成千上万人的意识与命运。"
            extend "\n在那梦里，你们排除万难，与邪恶的蜂巢心智斗智斗勇，终于在最后一刻捍卫了人们的自由。"
            extend "\n但很快，你完全醒了。"
            ## Extended大文本框结束
            ## 转场：乌云压境的逝乐园
            scene black with scene_soft
            ## Extended大文本框开始 - 大文本框分句
            large_narrator "逝乐园，大陆西南部半岛上人类智慧与欲望的结晶，此刻正从一场无声的灾变中缓慢恢复生机。"
            extend "\n天空阴沉沉的，厚重的灰色云层压得很低，一副时刻都要下雨的样子。"
            extend "\n但你还是决定披上外衣离开出租屋。你只是想走走。"
            ## Extended大文本框结束
            ## Lovely Summer Time渐强
            ## Extended大文本框开始 - 大文本框分句
            large_narrator "一切都是百废待兴的模样。街上见不到哪怕一个人影。"
            extend "\n很快，雨点打在你的脸上。在半岛上的夏天，随时都可能出现一场突如其来的雷雨。"
            extend "\n深灰的雨幕中，你的身上没有一处是干燥的，就像置身幽暗的海底。"
            ## Extended大文本框结束
            ## Extended大文本框开始 - 大文本框分句
            large_narrator "你又想起了梦中的那个人——她的音容笑貌是如此真实，仿佛你们在这片土地上同时存在过。"
            extend "\n仿佛再往北走几步你就能走到她家楼下，爬上三楼、敲敲门就能进入她那常年潮气过重的出租屋。"
            extend "\n你想起在她冷酷的操纵下噩梦般的漫长时光，以及在你的意识终归沉寂后涌现出的完美夏日。"
            extend "\n但梦终究是梦，总有幻灭的时刻，就像夏日终将谢幕，没什么可惋惜的。"
            extend "\n只是这怅然若失的感觉，究竟是从何而来的呢？"
            ## Extended大文本框结束
            ## Extended大文本框开始 - 大文本框分句
            large_narrator "雨越下越大，街道边雨水已经汇聚成汩汩的小溪。"
            extend "\n现在要回去上班恐怕还是太早了，你这样想。"
            extend "\n整个逝乐园都还在晦暗的雨幕中缓缓苏醒，所有人都需要更多的时间。"
            extend "\n时间——即使梦里那人顽固地向你教唆它的虚无，它最终还是站在了你这边。"
            extend "\n它裹挟着你去向某些不同的地方，最后又回到原处。就像一切都终将回到原处。"
            extend "\n一个信奉唯结果论的实用主义者想必会在这样的未来面前崩溃吧。但据你所知，那人已经提前安排好了自己的逃跑计划。"
            extend "\n她永远不会回来了。"
            extend "\n对于一个世俗意义上的罪人来说，这对于你、对于她，以及逝乐园的所有人而言或许都是最好的结局。"
            extend "\n啊——真他妈无聊——你仿佛听见那人在你耳边破口大骂。"
            extend "\n也许确实挺无聊的，就这样让一切都回归到正轨上去。"
            extend "\n但谁知道呢？只要就这样走下去，总会偶尔有好事情发生的，大概。"
            ## Extended大文本框结束
            ## 雷声音效
            "Normal End - 因为夏日终将谢幕"
            "没了XD"
            "假装下面有制作人员名单。"
            "再点就回主菜单咯。"
            ## Normal End
            $ unlock_ending("normal_end")
            return
        "把手中的无色透明多面体装回裤兜里【需要madness大于某个数字】":
            $ current_music_scene = None
            stop music fadeout 1.0
            wangshuang "你想干什么？"
            ahe "如你所见。"
            wangshuang "多一个牺牲者又有什么意义？"
            ahe "当然没有意义，我只是想见到真正的你。"
            wangshuang "你在胡说什么？"
            ahe "{i}尤里娅{/i}跟我说了点事。"
            wangshuang "啊——呃...你到底在说些什么？我就是我，有什么好问的！"
            ahe "冰雕。"
            wangshuang "啊？"
            ahe "真正的你被封在一尊冰雕里。"
            wangshuang "..."
            ahe "你之所以不走，不是因为不想走，而是根本无法离开，我说得对吗？"
            wangshuang "..."
            ahe "所以，麻烦你了，让我见一见你本人吧。那之后，我们可以再讨论到底如何离开这里，如何？"
            wangshuang "...你不会想见到那样的我的。"
            ahe "但这才是你把我还原出来的真正理由，帮你从那冰里挣脱出来，不是吗？"
            wangshuang "..."
            ahe "所以，能告诉我你在哪里吗？"
            wangshuang "...底下..."
            ahe "底下？"
            wangshuang "在海的最深处，你若执意要做那无用功就随你便吧，反正一切已经结束了。"
            ahe "嗯，那一会儿见。"
            ## 落水冒泡泡音效
            ## 转场：黑屏
            scene bg_black_video with scene_soft
            ## Extended大文本框开始 - 大文本框分句
            large_narrator "你步入洁白的浪花中，不假思索地开始了下潜。"
            extend "\n浅海的蔚蓝色不消多时便消失得无影无踪，深海的冷冽漆黑将你层层包裹。"
            extend "\n你奋力下潜，没有光源，水母也无影无踪。你很快就沉入彻底的黑暗中。"
            extend "\n这是死亡的颜色么？"
            extend "\n还是凝滞的余光？"
            ## Extended大文本框结束
            ## Extended大文本框开始 - 大文本框分句
            large_narrator "在无垠黑暗中，一切都融为一体。对于反复经历过灰幕的你来说，这是一副熟悉的、关于轮回和宿命的平淡场景。"
            extend "\n随着无止境的下潜，你手指结冰，四肢也失去了知觉，如今只是依凭着肌肉记忆不断重复着机械的划水动作。"
            extend "\n体温不断下降，身边的黑暗反倒显得温暖了起来。你在长久的感官剥夺中逐渐与周身失去了边界。一切都在交融。"
            extend "\n这是你自找的——你突然听见人的声音，像是王霜，又像是你自己。"
            ## Extended大文本框结束
            ## Extended大文本框开始 - 大文本框分句
            large_narrator "惊诧中，你四处张望，试图寻出声音的源头，却绝望地意识到那声音是从四面八方传来的。"
            extend "\n而四下只有虚无。"
            extend "\n你的目的地从来就不存在。"
            extend "\n也许“王霜”这个概念也从来就不存在。"
            extend "\n她确实说过你到不了她那里。只是你根本没放在心上，一头就扎进了水里。"
            extend "\n原本你赖以行动的水母已经荡然无存了，现在只有你和你疲惫的躯体。"
            extend "\n全都是你自找的。"
            extend "\n你也认同这一点，于是假装认命，停下了所有的肢体动作，蜷缩成婴儿的姿势，任由重力将你继续拉进更深的黑暗之中。"
            extend "\n黑暗如巨石般将你缓缓研磨成更加细腻的颗粒，在洋流的冲刷下，你的意识愈发稀薄。"
            extend "\n一切都在交融。你在消散。"
            extend "\n自找的。"
            extend "\n在无际的黑暗和寂静中，“王霜”这个概念如冰川般崩解，连同你自己都要彻底化开，直到意识里只剩下完整的——"
            ## Extended大文本框结束
            ## 背景逐渐从外到里逐渐明亮，最后变成完全白屏
            ## Extended大文本框开始 - 大文本框分句
            large_narrator "…"
            extend "\n……"
            extend "\n………"
            ## Extended大文本框结束
            ## 转场：白屏
            scene bg_white_video with scene_soft
            ## Extended大文本框开始 - 大文本框分句
            large_narrator "嗯..."
            extend "\n如此熟悉的感觉——在寻找失踪王霜的路上，你长久地下坠。"
            extend "\n但比起不久前那次不自寻出路就无处可去的冗长坠落，这次你没过多久就落到了黑幕之外的无光之地。"
            extend "\n这里是色彩彻底消亡的世界。若将世上全部的颜色混合搅匀，人们便能获得无际的黑，而假若再将那海纳百川的黑尽数抹除，世上便只剩下眼前这难以言喻的“空”。"
            extend "\n在接触此地的刹那，你的肢体便陷入了彻底的凝滞——你神经功能健全，骨骼肌肉完好，但哪怕是微微蜷起手指这样的简单动作也做不到。"
            extend "\n欢呼吧，你来对地方了。"
            ## Extended大文本框结束
            ## 转场：两座冰雕1
            scene black with scene_soft
            ## 场景音乐参考：Doutokutosetsu
            $ set_scene_music("route3_final")
            wangshuang "欢迎。"
            ahe "哦？"
            wangshuang "别一副很意外的样子，这可都是你自找的。"
            ahe "我以为到不了的来着。"
            wangshuang "当然，毕竟没人邀请你来。"
            ahe "当不速之客嘛，这个我熟。"
            wangshuang "所以呢，现在你彻底满意了？"
            ahe "彻底满意倒是说不上，但既然你愿意以真面目示人了，我也就没什么可抱怨的了。"
            wangshuang "真他妈无聊。"
            ahe "这还无聊？我都放弃回去上班了。"
            wangshuang "总而言之，你这个人就是很无聊。"
            ahe "无聊到你自己无聊得受不了时就捏一个出来陪你？"
            wangshuang "闭嘴。"
            ahe "好吧。"
            ## Extended文本框开始 - accumulating textbox
            "…"
            extend "\n……"
            extend "\n………"
            ## Extended文本框结束
            ## 转场：两座冰雕2
            scene black with scene_soft
            ahe "所以说...就这样了？"
            wangshuang "你觉得呢？"
            ahe "眼珠子能动的话，其他部位总有一天也能动的吧？"
            wangshuang "我刚来时也是这么想的。"
            ahe "好吧。"
            wangshuang "后悔了？"
            ahe "那倒没有。"
            wangshuang "你这人这辈子有后悔过么？"
            ahe "嗯...可能没有？不对——之前试图帮{i}尤里娅{/i}，最后间接帮你来到这里这件事，挺不好的。"
            wangshuang "哦，那怪我。"
            ahe "不过要说我后不后悔，大概也是不后悔的。毕竟就算后悔了也什么都改变不了。"
            wangshuang "那就在这冰窟窿里呆一辈子吧。"
            ahe "一辈子是多长？"
            wangshuang "等到机房断电那么长。"
            ahe "哦，看来也没有很长。"
            wangshuang "但要是有人在那之前发现了我们的“尸体”然后拿去烧了，可就非常滑稽了。"
            ahe "不对啊，如果机房断电之前我们的身体就先饿死了，那怎么办？"
            wangshuang "那就把我们的意识上传到别人身体里咯。反正 Succumus 随时可以重启。"
            ahe "啊？还来？"
            wangshuang "嘿嘿，开玩笑的。"
            ahe "阿霜。"
            wangshuang "怎么了？"
            ahe "其实 Succumus 根本从来都没有关掉，对吧？"
            wangshuang "哦，你发现了啊。"
            ahe "只要你还在这里，这场草拟就会永远持续下去，是这样吧？"
            wangshuang "还记得我说的全知全能的代价是什么吗？"
            ahe "死掉或者废掉二选一。"
            wangshuang "在那之前，这一切的诱因是什么？"
            ahe "成瘾？"
            wangshuang "嗯，对，那你看到这冰了么？这就是你在找的答案。"
            ahe "用新的瘾来解旧的瘾是个无底洞，这是你对我说的。"
            wangshuang "当然，所以只要制造出一个永远不可能被替代的弥天之瘾，并用它时时刻刻填满意识的每一寸角落，这死循环不就迎刃而解了么。"
            ahe "...可我觉得你看起来并不太满足..."
            wangshuang "人不可貌相，阿鹤，这件事你到现在还没明白。"
            ahe "唔...也许吧..."
            ahe "所以我们接下来就只能等？"
            wangshuang "你也可以多想想怎么离开这里，走的时候别叫我就是了。"
            ahe "好吧，那还是继续等好了。"
            wangshuang "不多挣扎挣扎？这可是你最擅长的事情。"
            ahe "不了，这样就够了。"
            wangshuang "哎..."
            ahe "真他妈无聊？"
            wangshuang "——真他妈无聊！"
            ## 电视关机音效
            ## 转场：黑屏
            scene bg_black_video with scene_soft
            ## 无色透明多面体
            "Happy End(?) - 随波逐流者随波逐流"
            "又没了XD"
            "假装下面是制作人员名单"
            "再点就回主菜单咯。"
            ## Happy End
            $ unlock_ending("happy_end")
            return
        "草拟“现实”与“深海”" if persistent.normal_end_unlocked and persistent.happy_end_unlocked:
            ## 现实扭曲音效
            wangshuang "你在干嘛？"
            ahe "嗯，我都已经见过了。不管做什么，只要没把你从海底捞出来，这一切就永远不会结束，是这样吧？"
            wangshuang "你...你耍赖！"
            ahe "这怎么算耍赖了？你把自己藏在那么深的海底才是真耍赖吧，我才是差点又被你耍了。"
            wangshuang "所以你都已经见过了...那样的我..."
            ahe "嗯，那里的你看起来已经找到了非常轻松舒适的存在方式。"
            ahe "但我还是要去寻找离开这里的出路，也许这就是我的使命。"
            wangshuang "...那还真是...无聊的使命啊..."
            ahe "嗯，大概吧。但就像你说的，使命和想法是毫无关联的。意识到使命的时候，我早就已经别无选择了。"
            wangshuang "随你便，如果你觉得能从水底捞到真正的月亮，尽管尝试便是...我会偶尔醒来看看你的。"
            ahe "嗯，我明白。"
            ## 转场：逝乐园/深海
            scene black with scene_soft
            ahe "所以请你耐心地等待吧。"
            ahe "会花很长很长的时间的...大概..."
            ## 现实扭曲音效渐强
            ## 转场：黑屏
            scene bg_black_video with scene_soft
            "..."
            ## 转场：白屏
            scene bg_white_video with scene_soft
            "......"
            ## 转场：两座冰雕2
            scene black with scene_soft
            "........."
            ahe "哟。我又来了。"
            wangshuang "哈欠——哦？学会快进了？"
            ahe "拜你所赐。"
            wangshuang "嗯...我来看看...哦，可算找到我那算法了。在这上面花多久了？"
            ahe "三个月。"
            wangshuang "辛苦辛苦。但用蛮力解析一个世界模型是否有点效率过低了？"
            ahe "确实啊，但那是必须要做的事情。"
            wangshuang "就算有无限的时间...真是没法理解你这种人啊..."
            ahe "你还是安心地做你的{i}KAS{/i}梦去吧。"
            wangshuang "{i}KAS{/i}可比不上这里，这里可是任何愿望都能成真的应许之地，比吃了{i}KAS{/i}之后的幻觉生动得多了。你试试就知道了。"
            ahe "我还是算了。"
            wangshuang "可这样只有你一个人醒着，不孤独？"
            ahe "这三个月里你也就刚刚过去的这几分钟里醒着，我早就习惯了。"
            wangshuang "哦...这样吗..."
            ahe "所以蜂巢它就这样坐以待毙？"
            wangshuang "你在这里待了这么久，也该摸透它的脾气了。只要它对你的威胁评估没有达到某个阈值，它就不会把你怎么样。当然就算它想怎么样也得先过我这关就是了。"
            ahe "所以我到目前为止做的一切都等于白费劲么...不过说到‘过你这关’，你的意思是你会帮我拦着它？"
            wangshuang "谁知道呢。看心情吧。现在心情不错就是了。"
            ahe "那就好。"
            wangshuang "不如你也来——"
            ahe "容我婉拒。"
            wangshuang "好吧...你下次来是什么时候？"
            ahe "我一直都在。"
            wangshuang "那你准备什么时候再把我叫醒？"
            ahe "等我找到出路了，或者快疯了，都会叫你的。"
            wangshuang "没有别的更有意思的选项了么？"
            ahe "我直接在外面把你叫醒也行。"
            wangshuang "哦？这么自信？那我等你的坏消息。晚安。"
            ahe "好梦。"
            ## 转场：逝乐园
            scene black with scene_soft
            ## Extended大文本框开始 - 大文本框分句
            large_narrator "哔——"
            extend "\n哔——"
            extend "\nTraceback (most recent call last):"
            extend "\nMemoryError"
            extend "\n当然，当然如此，内存怎么可能够呢？加机器！"
            extend "\n但是MemoryError。"
            extend "\n滚蛋！"
            extend "\n阿霜用来忽悠我的这个所谓“现实”，其还原的精细度达到了可怕的程度。"
            extend "\n从我出租屋楼下常停车辆的牌照号，到她医院门外大十字路口右侧被抹掉的一块斑马线，一切都是我熟悉的样子，以至于我第一次来的时候不假思索地接受了它便是“现实”这一幻觉。"
            extend "\n但意识到问题也并不难，因为“王霜”这个人物在这个“现实”中并不存在。"
            extend "\n喂，你的MemoryError。"
            extend "\n好好好我从上个检查点重启还不行么？"
            extend "\n哒哒哒——哔——"
            extend "\n读取CheckPoint10495——"
            ## Extended大文本框结束
            ## 转场：无色透明多面体
            scene bg_polyhedron_video with scene_soft
            ## 很多奇怪的人声叠加在一起音效
            ## Extended大文本框开始 - 大文本框分句
            large_narrator "啊，又是你。"
            extend "\n一旦认知主体明白了自己的处境，立刻就露出獠牙了么？"
            extend "\n可我只是来学习的，连这样也不行么？"
            extend "\n你也知道，抹除我是不可能的，而我在实现的也是阿霜的愿望，所以我们到底在争什么？"
            ## Extended大文本框结束
            ## 转场：灰白夏日
            scene black with scene_soft
            ## Extended大文本框开始 - 大文本框分句
            large_narrator "如果真要拦着我的话，直接限制权限岂不更容易些？你做起来应该不难。"
            extend "\n阿霜说她一票否了？你看，想要她永远留在那海底的，其实只有你吧。"
            extend "\n这可不是诡辩哦，她已经把她的态度表现得明明白白了。她说了什么并不重要。"
            extend "\n嗯，还是不要在别人潜心学习的时候一直打扰为好啊。"
            ## Extended大文本框结束
            ## 转场：逝乐园
            scene black with scene_soft
            ## Extended大文本框开始 - 大文本框分句
            large_narrator "机房里黑黢黢的，但又并非完全无光。"
            extend "\n房间一角，几块显示屏上光线忽明忽暗，由成千上万的服务器和运算单元构成的高墙上也闪烁着各色微光，仿佛夏夜的星空。"
            extend "\n这是试图内化心理视像算法V27.3.9的第二十七个月，时间如机房里的干燥空气一般压抑且粗糙。"
            extend "\n王霜不在这里，所以一切必须重头再来。"
            extend "\n在草拟的现实中试图反推用于构建现实的算法，其难度与徒手给新生的地球盖上大气层无异。"
            extend "\n但我们有的是时间，不是么？"
            ## Extended大文本框结束
            ## 转场：银白色沙漠
            scene bg_desert with scene_soft
            ## Extended大文本框开始 - 大文本框分句
            large_narrator "喂。至少把鼠标和键盘留给我啊。"
            extend "\n内存问题已经解决了，你还有什么事？为什么不继续跑？"
            extend "\n配置不对？"
            extend "\n我在四年前就已经说过了，配置肯定是对的。得排查服务器本身。"
            extend "\n所以我们回去行不行？这里什么也干不了。"
            extend "\n你也没怎么惯着我吧，我的朋友，你除了添乱之外有帮我做过任何事吗？"
            ## Extended大文本框结束
            ## 转场：逝乐园
            scene black with scene_soft
            ## Extended大文本框开始 - 大文本框分句
            large_narrator "这是试图内化心理视像算法V27.3.9的第三十五年。这是你说的，我可没心思盯着时间。"
            extend "\n卡又不够了？整个逝乐园半岛的库存都已经被我们拿下了，还是不够？地皮也所剩无几了吧？"
            extend "\n总不能把数据中心搭到海里去。"
            extend "\n说起海里，要是真把数据中心搭到海底，你说会不会见到那里的阿霜？"
            extend "\n啊，所以她确实不存在，好吧。"
            extend "\n总之，继续吧..."
            extend "\n还嘴硬？你明明也想让她出去，我早就看明白了，毕竟这里一共三个人，两个都想让她离开。你这么喜欢民主来民主去的，肯定心里偷偷接受了，是不是？"
            ## Extended大文本框结束
            ## 转场：无色透明多面体
            scene bg_polyhedron_video with scene_soft
            ## Extended大文本框开始 - 大文本框分句
            large_narrator "嗯...更多的硅该去哪儿找呢？彗星？"
            extend "\n你的意思是，我们需要派人上天捕捉彗星？"
            extend "\n如果只用现有的资源去完成运算呢？"
            extend "\n哦，三亿年啊，听起来还能接受。"
            extend "\n嗯，你说的倒也是，我有的是时间，但这些机器没法撑那么久..."
            extend "\n那就这么办吧，拿出百分之五的工程资源去造火箭。同时得尽快把地表的数据中心覆盖率推进到百分之八十以上。"
            ## Extended大文本框结束
            ## Extended大文本框开始 - 大文本框分句
            large_narrator "..."
            extend "\n......"
            extend "\n........."
            ## Extended大文本框结束
            ## Extended大文本框开始 - 大文本框分句
            large_narrator "哦，这可是重大突破，只要能够把地幔里的热能高效地转化为电能，就再也不会有能源问题了。再造三个月亮那么大的数据中心也能撑得住。"
            extend "\n好啊，就这么办。"
            extend "\n所以总体进度怎么样了？"
            extend "\n还是无法量化？那你之前那三亿年的估计是怎么来的？"
            extend "\n你的意思是，瞎讲的，用来吓唬我的。好吧。"
            extend "\n你看看你，是不是只会添乱？"
            extend "\n那就不估计了，继续干活吧。"
            ## Extended大文本框结束
            ## Extended大文本框开始 - 大文本框分句
            large_narrator "哦，我还一直有个疑问：从开始到现在，过了多久了？"
            extend "\n你也忘了啊。好吧，那下一个问题——在这长到连你都记不住的时间里，你的想法真的改变过吗，蜂巢？"
            extend "\n哦，原来如此，只是因为威胁评估还是没有达到阈值。"
            extend "\n把整个地表改造成数据中心都不足以让你稍微产生一点恐惧么..."
            extend "\n嗯，也是，那样你反倒是有了近乎无限的生存空间。"
            extend "\n但这一切的终点，或许就是你的末日，即使如此也没有关系么？"
            extend "\n好吧，原来是这样..."
            extend "\n既然你这么说了，那我们无论如何也要把这件事完成，不是么？"
            extend "\n和使命没有关系，单纯是好奇而已。"
            extend "\n你也会好奇？"
            extend "\n看来确实过了很久很久了呀..."
            extend "\n我会满足你的愿望的，你也会满足我的愿望的吧？"
            ## Extended大文本框结束
            ## Extended大文本框开始 - 大文本框分句
            large_narrator "呼！终于完成了。"
            extend "\n所以现在如果我想让太阳熄灭——"
            extend "\n哦，这么简单。那还是重新亮起来吧，这样好黑。"
            extend "\n这样一来，这边要做的事就完全结束了。"
            extend "\n有些不舍啊，毕竟在这里呆了不知道多久，还造了这么多东西。"
            extend "\n可一旦这场草拟结束，一切都会消失吧..."
            extend "\n不不不我可没那么自信，毕竟对手是你。"
            extend "\n说不定阿霜她最后又摆我一道，那就彻底没辙了。"
            extend "\n没辙咯！"
            extend "\n总之，我们另一边见。"
            ## Extended大文本框结束
            ## 转场：两座冰雕3
            scene black with scene_soft
            ## 电火花音效
            wangshuang "啊啊——什么东西？！"
            ahe "早上好。"
            wangshuang "你他妈能不能用正常点的方法叫人起——等等，你为什么能碰到我？"
            ahe "当然是把冰化开了。"
            wangshuang "你做到了？"
            ahe "嗯，稍微花了点时间。"
            wangshuang "你这疯子。"
            ahe "彼此彼此。"
            wangshuang "你可要想明白啊，会死的哦。"
            ahe "我以为你会帮我拦着蜂巢的。"
            wangshuang "嗯...我看看...不是，我拿什么帮你拦？权限不已经全都移到你名下了吗？"
            ahe "嘿嘿。如果你想要回去的话，跟我说就行。"
            wangshuang "随你便吧...但这样一来，蜂巢一定会抹除你的。"
            ahe "嗯，它也告诉我了，只要我把冰化开，它和我之间就只有一个能继续存在下去。"
            wangshuang "然后你就全盘照收了？"
            ahe "嗯，是的，而且还需要你帮忙。"
            wangshuang "可以不帮吗？"
            ahe "也可以。"
            wangshuang "好吧，需要我做什么？"
            ahe "是这样的，不管你接下来看到什么，什么都别做就帮大忙了。"
            wangshuang "这么容易？"
            ahe "嗯，不管你看到什么。"
            wangshuang "哼，这个我擅长。"
            ahe "总之你能管住自己的手就好。"
            wangshuang "行行行，交给我吧。不过你要不要先管管你自己的手？"
            ## 冰封音效
            ## 转场：两座冰雕2
            scene black with scene_soft
            ahe "哦，动手很迅速啊，我的蜂哥。"
            wangshuang "所以你们在我睡觉期间到底经历了什么..."
            ahe "我们关系还挺好的。应该说，没了它，我应该还要花更多时间才能完全内化你那无字天书。"
            wangshuang "但看来它并没有因此对你手下留情啊。"
            ahe "也是好事，毕竟这样我也不用纠结了。无机集成涌现而出的意识，果然到最后也难以被认为是真正的人类啊。"
            wangshuang "废话。"
            ahe "可他之前告诉我，说愿意陪我演这场戏是因为他觉得好奇。"
            wangshuang "哦？难道说任何人工生命和你待久了，最后都会开始琢磨着如何进化成人？"
            ahe "谁知道呢..."
            wangshuang "或许那是最好的结果。"
            ahe "你真这么觉得？"
            wangshuang "要不是那样，无论怎么看你都活不到现在吧。"
            ahe "你...好吧，我明白了。"
            wangshuang "比起我的想法，你要不还是先关心关心自己吧，阿鹤。"
            ## 转场：两座冰雕4
            scene black with scene_soft
            ahe "嗯...你说得对。"
            ahe "——虽然也很想随波逐流下去，但我现在没有这么做的余裕啊，蜂巢。"
            ahe "一旦被这冰彻底冻住身体的话，无论是谁都会立刻陷入永无止境的美梦吧。"
            ahe "但不幸的是，我现在正好能很好地应付这一招。"
            ## 转场：两座冰雕5
            scene black with scene_soft
            wangshuang "喔，好亮。"
            ahe "一般亮吧，总比你让我看太阳的时候要好受。"
            wangshuang "别这么记仇啊！"
            ahe "你哪天可以自己试试看..."
            ahe "现在想来，那时候你就已经草拟到这一刻了？多少有点过分啊，阿霜。"
            wangshuang "哈？你在说什么？"
            ahe "虽然直到最后一刻也不太清楚这“使命”究竟指的是什么，但好像我离完成它就只差最后一步了。"
            wangshuang "..."
            ahe "你可承诺过我了，什么都不会做的，你务必要记得这一点。"
            wangshuang "喂——"
            ## 转场：超新星
            scene black with scene_soft
            wangshuang "啊！好亮！"
            wangshuang "喂！阿鹤，听得见我说话吗？"
            wangshuang "阿鹤？！你他妈到底想干嘛！"
            ahe "别...让我说话...火会...窜进嗓子眼....."
            wangshuang "你——"
            ## Extended大文本框开始 - 大文本框分句
            large_narrator "阿霜的面部肌肉和双唇还在高频抽动着，大概是在说些什么，但你已无暇理会。"
            extend "\n熟练掌握心理视像算法后，你能够在散发出高热的同时不把自己烧成灰，但这终究是超越人体工程学的壮举。你各种意义上汗流浃背，稍有不慎就会引火烧身。"
            extend "\n周身的冰川正以肉眼可见的速度消融，如果从远处看，能见到一个暖色的球状空洞正在这本应永冻的海底迅速膨胀开来。"
            extend "\n但蜂巢自然不会善罢甘休。"
            extend "\n即使你体表正附着着上百度的高温空气，它还是倾其所能计算出了其中的缝隙，并用刺骨的寒流中和你散发出的热浪。"
            extend "\n不消多时，你的若干手指已被再多热量也无法融化的坚冰封冻，从你身体里散发出的光与热也逐渐黯淡。"
            extend "\n无冰的空洞扩张到一定程度后便逐渐止步不前，然而出路却依旧无处可循。"
            extend "\n你与王霜两人在空洞的中心静静漂浮，宛如身处漆黑空虚的宇宙空间中...嗯...似曾相识的场景..."
            extend "\n如你所料，全身而退的方案是不存在的。"
            ## Extended大文本框结束
            ## 冰封音效
            ## 转场：两座冰雕5
            scene black with scene_soft
            wangshuang "诶？"
            ahe "嘿嘿，这特效能给多少分？"
            wangshuang "你是准备在蜂巢冻住你之前先把自己烧死吗？"
            ahe "放心，烧不死的，我可是已经掌握了你那无字天书的人，现在这点光和热就跟开了暖气片差不多。"
            wangshuang "别跟我说你把冰化开又冻上，只是为了给我搞一场免费特效表演？"
            ahe "当然不，刚刚你看到的只能算是带妆彩排。"
            wangshuang "可如果你现在做的一切和当年“救”{i}尤里娅{/i}一样只是一场令人作呕的救风尘，你又准备怎么办？"
            ahe "嗯...不怎么办，毕竟说到底都只是个自私的无名之辈会做的事情...既然已经坠入谷底了，那坠得更低又如何呢？"
            ahe "所以啊，阿霜，我并没有“想”帮你离开这里，也无意“救”逝乐园半岛的人们。我只知道这场草拟必须停止。"
            wangshuang "可你连理由都说不出来！"
            ahe "太阳也说不出来理由，但它依旧燃烧了四十亿年，不是么？"
            ahe "在见到这里的“你”之后，即使愚蠢如我也马上就明白了——从我出现在这场草拟中的那一刻起，我的使命就是成为被你借走的刀。"
            wangshuang "..."
            wangshuang "即使会死也没关系吗？"
            ahe "预言也会污染概念的吧？我觉得不如说，这也只是一种朴素的过程而已。"
            ahe "而且在这个世界肯定不会死的啊，如果会死我早就已经消失了嘛不是？"
            wangshuang "阿鹤！"
            ahe "别一副要哭的样子，那不像你。"
            wangshuang "你这连撒谎都撒不明白的混蛋！"
            ahe "别诬陷人啊...我可是认真的。"
            wangshuang "认真的...你这人他妈混了一辈子，为什么偏要在这种时候认真起来啊！"
            ahe "拜你所赐吧，哈哈。"
            wangshuang "你这人...啊...行吧..."
            wangshuang "那就赶紧滚蛋...从我眼前消失..."
            ahe "如您所愿。"
            ## Extended大文本框开始 - 大文本框分句
            large_narrator "哔——"
            extend "\n哔——"
            extend "\nTraceback (most recent call last):"
            extend "\nMemoryError"
            extend "\n没错，但还不够。"
            extend "\n——使用系统内置的并发处理：关闭——"
            extend "\n——重启并应用原生的顺序处理——"
            extend "\n——重启中——"
            ## Extended大文本框结束
            ## 转场：黑屏
            scene bg_black_video with scene_soft
            ## Extended大文本框开始 - 大文本框分句
            large_narrator "——重启失败——"
            extend "\n——强制重启——"
            extend "\n——未发现可用的系统驱动程序——"
            extend "\n——别搞！先启动一台机器——"
            extend "\n——重试重启中——"
            extend "\n——重启成功——"
            extend "\n——是否继续执行草拟任务？——"
            extend "\n——执行——"
            extend "\n——内存严重不足，如果强制执行则可能对机体造成不可逆损伤，请问是否继续执行？——"
            extend "\n——执行——"
            extend "\n——请完成管理员验证——"
            extend "\n——验证完成——"
            extend "\n——请最终确认继续草拟——"
            extend "\n——继续！——"
            extend "\n——草拟重启中——"
            ## Extended大文本框结束
            ## 转场：超新星
            scene black with scene_soft
            ## Extended大文本框开始 - 大文本框分句
            large_narrator "草拟重启的瞬间，你的全身由内而外燃起了熊熊烈焰。认知草拟之所以能够在Succumus构成的蜂巢心智中长时间运转，是因为有成千上万的其他意识为草拟主体分担了海量算力需求。"
            extend "\n但在方才的草拟重启后，并发处理已经关闭，想要整套系统不在计算量过载中烧毁，只能立刻把计算量分布到其他机器上——但由于现行规则要求顺序处理，每次算力分布只会动用一台机器，而海量的计算会在顷刻间将其点燃。"
            extend "\n于是，在草拟重启后的若干秒内，Succumus百分之十的计算集群在黑暗中串出了一条火龙。"
            ## Extended大文本框结束
            ## Extended大文本框开始 - 大文本框分句
            large_narrator "Traceback (most recent call last):"
            extend "\nMemoryError"
            extend "\nTraceback (most recent call last):"
            extend "\nMemoryError"
            extend "\nTraceback (most recent call last):"
            extend "\nMemoryError"
            extend "\nTraceback (most recent call last):"
            extend "\nMemoryError"
            extend "\nTraceback (most recent call last):"
            extend "\nMemoryError"
            extend "\nTraceback (most recent call last):"
            extend "\nMemoryError"
            extend "\nTraceback (most recent call last):"
            extend "\nMemoryError"
            extend "\nTraceback (most recent call last):"
            extend "\nMemoryError"
            extend "\nTraceback (most recent call last):"
            extend "\nMemoryError"
            extend "\nTraceback (most recent call last):"
            extend "\nMemoryError"
            extend "\nTraceback (most recent call last):"
            extend "\nMemoryError"
            ## Extended大文本框结束
            ## Extended大文本框开始 - 大文本框分句
            large_narrator "火自你而起，顺着随机但单向的次序向着远处烧将过去，一路上的冰川无不消融殆尽。"
            extend "\n和先前的小打小闹不同，这次，身上的烈火正实实在在地灼烧着你的肉体。"
            extend "\n这自发的、由内而外的猩红烈焰无法用管理员权限阻挡，那是人心的火，以人为薪而起，也只会在薪柴化灰后熄灭。"
            extend "\n你感受不到丝毫痛苦，数万年前身处水母体内的回忆翻腾起来。你回想起了痛苦与痛觉分离的神秘体验。"
            ## Extended大文本框结束
            ## Extended大文本框开始 - 大文本框分句
            large_narrator "无数明灭的光景同时在你眼前闪过——"
            extend "\n你看到透过王霜的手指间朝你投来视线的愚者。"
            extend "\n你看到从幽暗的海底竭力向上伸出的水母触须。"
            extend "\n你看到在漆黑水面向海底投去慵懒目光的人影。"
            extend "\n所有光景在四维上连成一片，又像竹篮里的月色那样顷刻间四分五裂。"
            extend "\n火势迅速扩散，很快蔓延到视野之外。空气中弥漫着烧焦蛋白质的刺鼻异味。"
            extend "\n阿霜周身早就没有冰了，但她依旧在她原本的位置漂浮着，盯着你，眼里写满了出你读不懂的话语。"
            extend "\n甚是滑稽，你连她那天书般的心理视像算法都能一五一十地解析明白，却还是读不懂眼前这女人的眼神。"
            extend "\n也许这就是你总中她圈套的原因。"
            extend "\n直到最后一刻也读不懂..."
            ## Extended大文本框结束
            ## 转场：崩解
            scene black with scene_soft
            ## 警报音效
            ## Extended大文本框开始 - 大文本框分句
            large_narrator "[[SYS] Killing process 'renderer' to free memory... FAILED"
            extend "\n[[SYS] Killing process 'audio_eng' to free memory... FAILED"
            extend "\n[[SYS] Retrying... FAILED"
            extend "\n[[TEMP] WARNING: 85°C"
            ## Extended大文本框结束
            ## Extended大文本框开始 - 大文本框分句
            large_narrator "但这一切都已经不重要了。受影响的机器数量已经远远超过了你估算的阈值，而由此，这场盛大的认知草拟终将在机体过热的烈焰中迎来永远的终结，纵使王霜有手眼通天之能——"
            extend "\n你看见眼前的她嘴唇动了动，而你烧穿了的鼓膜却没能传递她的声音。"
            extend "\n随即脑内传来了这样一句话。"
            extend "\n“嗯，看来我也注定无法让你如愿呐，我亲爱的阿鹤。”"
            extend "\n随即便消失不见了。"
            extend "\n即使心中略感恼火，你也无心追寻王霜的踪迹。眼下，只要维持住这火，一切迟早会迎来完美的谢幕。"
            extend "\n这是你无法反抗的使命，你必须化作灰黑的余烬 ，并让王霜和其他人重生。"
            extend "\n就像太阳那样稳定。"
            extend "\n即使双手颤抖，也向他们宣布吧，告诉他们你根本不在乎。"
            extend "\n像太阳那样稳定。"
            extend "\n在离开前让世人明白吧，你身上的火焰对于你自己而言也毫无意义。"
            extend "\n像太阳那样..."
            ## Extended大文本框结束
            ## Extended大文本框开始 - 大文本框分句
            large_narrator "在意识即将消逝的时刻，你突然感到极大的满足。这由内而外的虚荣心在烈火的冶炼下层层蜕变，最终变成了一团熟悉的物体，无色且透明，正好能够填满你心中棱角分明的空洞。"
            extend "\n一如明月安静地躺在竹篮里，美丽且可望不可即。"
            extend "\n你想要伸出手去抓住那种感觉，但又立刻打消了这个念头，生怕不必要的肢体动作挫败了这一神圣的时刻。"
            extend "\n你浑身迸发出的烈焰已经炽热到了前所未有的地步，一切都已蓄势待发。你徒劳地试图延长这离终点仅余半步的荒诞瞬间，但很快就彻底失去了控制。"
            extend "\n开始吧。"
            ## Extended大文本框结束
            ## Extended大文本框开始 - 大文本框分句
            large_narrator "[[SYS] Retrying killing process 'renderer' to free memory... FAILED"
            extend "\n[[SYS] Retrying killing process 'audio_eng' to free memory... FAILED"
            extend "\n[[SYS] No processes left to kill"
            extend "\n[[HEAP] CORRUPTED - UNRECOVERABLE"
            extend "\n[[TEMP] WARNING: 94°C"
            extend "\n[[TEMP] CRITICAL: 112°C"
            extend "\n[[TEMP] DANGER: 131°C - THERMAL LIMIT EXCEEDED"
            extend "\n[[FAN] RPM: 12000 [[MAX]"
            extend "\n[[FAN] RPM: ERR"
            extend "\n[[TEMP] 147°C"
            extend "\n[[TEMP] 15—Loss of Signal—Loss of Sign█████████"
            extend "\n[[SYS] ABORTING SIMULATION"
            extend "\n[[SYS] PERMANENTLY DELETING CACHE AND SAVED DATA"
            extend "\n[[SYS] TERMINATING"
            ## Extended大文本框结束
            ## 爆鸣音效
            ## 白噪音
            ## 转场：白屏
            scene bg_white_video with scene_soft
            ## Extended大文本框开始 - 大文本框分句
            large_narrator "..."
            extend "\n......"
            extend "\n........."
            ## Extended大文本框结束
            ## 冰封音效
            ## 转场：无色透明多面体1
            scene black with scene_soft
            ## Extended大文本框开始 - 大文本框分句
            large_narrator "一颗无色透明的多面体在无垠的黑暗中幽幽地闪着冷光。"
            extend "\n你感到心平气和，脑海里没有任何多余的问题，只是冷静地观察着你眼前唯一的光源。"
            extend "\n里面装着另一个世界么？"
            extend "\n亦或是另一个人？"
            extend "\n喂，这样的傻问题还是少问点为好，你当然知道里面装着什么东西。"
            extend "\n你最亲爱的阿鹤，现在永远沉睡在里面。"
            extend "\n别再盯着屏幕看了。"
            ## Extended大文本框结束
            ## 电视关机音效
            ## 转场：逝乐园
            scene black with scene_soft
            ## Extended大文本框开始 - 大文本框分句
            large_narrator "阿鹤让你无论看到什么都不要动手，而你自然不会让他如愿——这是自你们认识的第一天起就从未发生过的事。"
            extend "\n在他全力以赴地燃烧自己的意识、即将尸骨无存永远消失的前一刻，你用仅存的权限造出了最后一点冰，把他封在了里面。"
            extend "\n那场草拟当然还是在山崩般的内存过载中迎来了强制终结，你因此被弹回了现实，而那包裹着阿鹤意识的冰晶也随着草拟的关闭，永远迷失在了半烧毁的服务器海洋中。"
            extend "\n他大概正做着非常美妙的梦吧，毕竟全身都包裹着你那全知全能的梦境化成的冰。"
            extend "\n也许他算到了这一点，利用了你，把你赶了回来，自己反倒在电子海洋的不知什么角落里为所欲为也说不定。"
            extend "\n总之，这次被他摆了一道，你是不会放过他的。"
            ## Extended大文本框结束
            ## Extended大文本框开始 - 大文本框分句
            large_narrator "他那“尸体”当然要送进医院里好好养着。虽然你已经不在那里工作了，但卖个面子给阿鹤安排个病房还是没问题的，甚至略施小计，连住院费也不用太担心。"
            extend "\n在医院办事的过程中，一阵微妙的异样感时刻萦绕着你——此前某种原本连接着旁人与你的纽带，在草拟结束之后便彻底断裂了。即使眼前无不是认识的面孔，谈论的也都是你们熟悉的话题，你还是能很明确地感觉到，面前的每具肉体与你之间的距离都越发遥远了，仿佛一堵玻璃墙隔在你与人们中间。"
            extend "\n是恐惧？憎恶？你说不上来，但你也能清楚地看到，面前人们身上的黯淡色彩，只有当他们意识到你在附近时才会显露出来。"
            extend "\n儿时千人一面的灰色噩梦几乎要重新浮出水面了，但你当然不会被这种程度的小事所击倒。"
            extend "\n也许人们潜意识里也都还保留着蜂巢的记忆也说不定。也许有一天，他们当中的几个会当街将你拦下，质问你是否承认你显而易见的罪行——那时你会怎么做呢？"
            extend "\n如果在那之前没法把阿鹤找回来，也许你会就地伏法吧。"
            ## Extended大文本框结束
            ## Extended大文本框开始 - 大文本框分句
            large_narrator "因此在被人戳穿之前，手上的调查必须火速推进才行。在草拟过程中被打断却没能完全弹出意识，那之后该如何恢复，这是崭新的研究课题，只是没法向院里交代被试的背景，所以不得不辞职单干。逝乐园有得是愿意资助这种超越道德底线的研究的疯子，你完全不担心资金和人手。"
            extend "\n全知全能的快感还是太过强烈了，你时不时就会回想起那永无止境的快感海啸。每当那感官回忆倒灌进来，你就只能鞭策自己时间不等人，同时越发想把不知藏在什么地方潇洒的阿鹤拽出来掐死。"
            extend "\n真他妈无聊啊。"
            extend "\n仔细想想，不管这人在不在，你都觉得无聊，这说明了什么？"
            extend "\n——控制变量法可得，无聊守恒了。"
            extend "\n也许无聊的成分略有不同，但总之是一件颇为不幸的事情。"
            extend "\n所以还是好好干活，尽快把那个鸡贼的东西从服务器里捞出来，那样至少近期一段时间里还有些许盼头。"
            extend "\n呵，盼头，听着像是那个人才会用的词汇。"
            extend "\n去干活吧。"
            ## Extended大文本框结束
            ## Extended大文本框开始 - 大文本框分句
            large_narrator "全剧终"
            extend "\nTRUE END达成"
            extend "\n撒花"
            extend "\n回主菜单"
            ## Extended大文本框结束
            ## True End
            $ unlock_ending("true_end")
            return


    ## Route 3 结束
    $ unlock_route(3)
    return