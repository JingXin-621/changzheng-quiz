# -*- coding: utf-8 -*-
"""生成无语法错误的 HTML"""
import json

questions = [
    {"q":"中央红军（红一方面军）长征的出发时间是？","o":["1933年10月","1934年10月","1935年1月","1936年10月"],"a":1,"e":"1934年10月，中央红军从江西瑞金、于都等地出发，开始举世闻名的二万五千里长征。出发时约有8.6万人。","t":"时间节点"},
    {"q":"长征的出发地主要在哪里？","o":["井冈山","江西瑞金","湖南韶山","贵州遵义"],"a":1,"e":"瑞金是当时中华苏维埃共和国临时中央政府所在地，被称为红色故都。于都也是重要出发地。","t":"出发地"},
    {"q":"长征途中被称为「党的历史上生死攸关的转折点」的会议是？","o":["八七会议","古田会议","遵义会议","瓦窑堡会议"],"a":2,"e":"1935年1月召开的遵义会议，纠正了左倾军事路线错误，确立了毛泽东在红军和党中央的领导地位。","t":"重要会议"},
    {"q":"长征行程约多少里？","o":["一万五千里","二万里","二万五千里","三万里"],"a":2,"e":"中央红军长征约二万五千里（约12500公里）。毛泽东《七律·长征》写道：红军不怕远征难，万水千山只等闲。","t":"基本数据"},
    {"q":"中央红军长征历时约多少天？","o":["约180天","约260天","约368天","约500天"],"a":2,"e":"从1934年10月出发到1935年10月到达陕北，历时约368天。整个长征历时约两年。","t":"基本数据"},
    {"q":"中央红军出发时约有多少人？到达陕北时剩多少人？","o":["10万→3万","8.6万→7千","5万→1万","12万→5万"],"a":1,"e":"出发时约8.6万人，到达陕北仅剩约7000人。平均每12人中只有1人走到终点。","t":"基本数据"},
    {"q":"四渡赤水战役发生在哪条河上？","o":["金沙江","大渡河","赤水河","乌江"],"a":2,"e":"1935年1-3月，毛泽东指挥红军四渡赤水河。3万红军面对40万敌军，以灵活机动的运动战成功突围。","t":"经典战役"},
    {"q":"飞夺泸定桥发生在哪年哪月？","o":["1934年12月","1935年5月","1935年8月","1936年1月"],"a":1,"e":"1935年5月29日，红四团一昼夜急行军240里赶到泸定桥。22名勇士冒着枪林弹雨攀爬13根铁索夺桥。","t":"经典战役"},
    {"q":"飞夺泸定桥时，桥上只剩什么？","o":["木板桥面","石桥墩","13根光秃秃的铁索","竹制绳索"],"a":2,"e":"敌军拆除桥板，只留13根铁索悬在大渡河上。22名红军勇士攀索前进，创造了战争史上的奇迹。","t":"经典战役"},
    {"q":"红军翻越的第一座大雪山叫什么？","o":["玉龙雪山","岷山","夹金山","祁连山"],"a":2,"e":"夹金山位于四川宝兴县，海拔4114米。1935年6月翻越，许多南方战士因严寒缺氧而牺牲。","t":"自然环境"},
    {"q":"红军穿越的松潘草地位于今天的哪个省？","o":["甘肃","青海","四川","陕西"],"a":2,"e":"松潘草地位于今四川省阿坝藏族羌族自治州境内（若尔盖、红原一带），表面绿草覆盖，下面却是泥潭。","t":"自然环境"},
    {"q":"半条被子的故事发生在哪个省？","o":["江西","湖南","贵州","四川"],"a":1,"e":"1934年11月，3名红军女战士在湖南汝城县借宿徐解秀老人家中，临走把唯一的被子剪下半条留给老人。","t":"感人故事"},
    {"q":"金色的鱼钩中老班长用什么做鱼钩？","o":["铁丝","铜丝","缝衣针","别针"],"a":2,"e":"老班长用缝衣针做鱼钩钓鱼给伤员吃，自己饿死在草地。鱼钩现存中国人民革命军事博物馆。","t":"感人故事"},
    {"q":"刘伯承与哪位彝族首领歃血为盟？","o":["阿甲","小叶丹","阿旺","博巴"],"a":1,"e":"1935年5月，刘伯承与小叶丹歃血为盟结为兄弟，红军顺利通过大凉山彝区，书写民族团结佳话。","t":"民族团结"},
    {"q":"遵义会议确立了谁在红军和党中央的领导地位？","o":["周恩来","朱德","毛泽东","张闻天"],"a":2,"e":"遵义会议确立了毛泽东的领导地位。会后成立三人军事指挥小组（毛泽东、周恩来、王稼祥）负责指挥。","t":"重要会议"},
    {"q":"红34师师长陈树湘在湘江战役中受伤被俘后？","o":["成功逃脱","绝食抗议","扯断自己肠子牺牲","说服敌军起义"],"a":2,"e":"陈树湘腹部中弹被俘，在押送途中用手从伤口扯断肠子壮烈牺牲，年仅29岁，践行了革命誓言。","t":"英雄人物"},
    {"q":"红军在长征中共翻越了多少座大山？","o":["约10座","约18座","约25座","约30座"],"a":1,"e":"翻越18座大山，其中5座终年积雪；渡过24条大河；途经14个省。这是人类战争史上罕见的远征。","t":"基本数据"},
    {"q":"中央红军到达陕北的标志性事件是？","o":["到达延安","到达吴起镇","到达会宁","到达保安"],"a":1,"e":"1935年10月19日到达陕北吴起镇。毛泽东写道：不到长城非好汉，屈指行程二万。","t":"重要时刻"},
    {"q":"长征精神的核心内涵是？","o":["艰苦奋斗","坚定革命信念、救国救民","团结协作","以上都是"],"a":3,"e":"长征精神内涵丰富：把人民利益看得高于一切；坚定革命信念；不怕牺牲；独立自主；顾全大局；依靠人民。","t":"精神传承"},
    {"q":"巧渡金沙江红军用了什么策略？","o":["搭浮桥","佯攻昆明诱敌回防，抢占皎平渡","武装泅渡","与守军谈判"],"a":1,"e":"佯攻昆明诱使滇军回防，主力抢占皎平渡口。7条小船7天7夜将3万红军全部渡过金沙江，跳出包围圈。","t":"经典战役"},
    {"q":"毛泽东《七律·长征》中「大渡桥横铁索寒」描写的是？","o":["强渡大渡河","飞夺泸定桥","四渡赤水","突破乌江"],"a":1,"e":"铁索寒三字写出铁索冰冷和战斗惊心动魄。全诗以「更喜岷山千里雪，三军过后尽开颜」收尾，展现乐观精神。","t":"诗词文化"},
    {"q":"红军强渡大渡河时，首批勇士有多少人？","o":["8人","12人","18人","22人"],"a":2,"e":"18名勇士乘小木船在敌军火力下冲向对岸。大渡河水湍急，稍有不慎船毁人亡，但勇士们成功了。","t":"经典战役"},
    {"q":"腊子口战役的地势特点是？","o":["开阔平原","密林山地","宽仅30米的险要隘口","沙漠戈壁"],"a":2,"e":"腊子口是川甘交界的险隘，宽仅30米，两侧百丈悬崖。红军正面强攻+侧翼攀登迂回攻克此天险。","t":"经典战役"},
    {"q":"红军长征中跨越的第一条大河是？","o":["赤水河","乌江","金沙江","大渡河"],"a":1,"e":"1935年1月突破乌江天险，随后攻占遵义，为召开遵义会议创造了条件。乌江是长征首个重大江河障碍。","t":"行军路程"},
    {"q":"雪山上的军需处长为什么被冻死？","o":["迷路了","他把棉衣都发给了战士","没有足够棉衣","受伤行动不便"],"a":1,"e":"管被装的军需处长把棉衣全发给了战士，自己穿单衣冻死在雪山上，牺牲时仍保持坐姿。","t":"感人故事"},
    {"q":"长征出发时红军的平均年龄大约多少？","o":["不到20岁","不到30岁","约35岁","约40岁"],"a":1,"e":"平均年龄不到30岁，很多战士十几岁。军团长平均约25岁。正是一群年轻人创造了人类奇迹。","t":"基本数据"},
    {"q":"斯诺写的关于长征的著名书籍是？","o":["《长征记》","《红色中国》","《西行漫记》（红星照耀中国）","《红军长征史》"],"a":2,"e":"1936年美国记者斯诺到陕北，写出《西行漫记》（红星照耀中国），首次向世界客观报道了长征。","t":"文化传播"},
    {"q":"红军三大主力会师的地点是？","o":["延安","吴起镇","甘肃会宁","保安"],"a":2,"e":"1936年10月红一、二、四方面军在甘肃会宁会师，万里长征全部胜利结束。中国革命从此转危为安。","t":"重要时刻"},
    {"q":"参加长征的女战士约多少人？","o":["约500人","约1000人","约2000人","约5000人"],"a":2,"e":"约2000多名女战士参加长征，与男战士一样爬雪山过草地，还承担宣传、医护工作。到陕北仅剩数百人。","t":"人物故事"},
    {"q":"以下哪项不是四渡赤水的特点？","o":["灵活机动","以少胜多","阵地攻坚战为主","调动敌军"],"a":2,"e":"四渡赤水是运动战典范，核心是声东击西调动敌军，而非阵地攻坚。毛泽东称之为得意之笔。","t":"经典战役"},
    {"q":"长征途中红军发布了什么重要宣言？","o":["《抗日宣言》","《八一宣言》","《对日宣战公告》","《北上宣言》"],"a":1,"e":"1935年8月1日草拟《为抗日救国告全体同胞书》（即《八一宣言》），号召停止内战一致抗日。","t":"重要文件"},
    {"q":"长征途中红军共经历了多少次战斗？","o":["约100次","约200次","约380次","约500次"],"a":2,"e":"约380次战斗，攻占700多座县城，击溃国民党军数百个团。平均每天都有遭遇战。","t":"基本数据"},
    {"q":"红军过草地时面临的最大危险不包括？","o":["沼泽泥潭","粮食短缺","极端低温","敌军空袭"],"a":3,"e":"草地偏远高原，敌军难以大规模空袭。真正敌人是沼泽、饥饿和严寒。战士们吃草根啃树皮煮皮带。","t":"自然环境"},
    {"q":"毛泽东遵义会议后创作的词是？","o":["《沁园春·雪》","《忆秦娥·娄山关》","《七律·长征》","《清平乐·六盘山》"],"a":1,"e":"《忆秦娥·娄山关》中「雄关漫道真如铁，而今迈步从头越」成为千古名句，表达不畏艰难的豪迈气概。","t":"诗词文化"},
    {"q":"彭德怀在长征中将自己的骡子主要用于？","o":["自己骑乘","驮运伤员和物资","作为战马冲锋","送给彝族首领"],"a":1,"e":"彭德怀宁可自己走路，把骡子用来驮运伤员。他说：骡子比人金贵，它能救战士的命。","t":"感人故事"},
    {"q":"红军长征共渡过多少条大河？","o":["约12条","约18条","约24条","约36条"],"a":2,"e":"渡过24条大河，包括乌江、赤水河、金沙江、大渡河等著名天险。每条河都是一道生死考验。","t":"基本数据"},
    {"q":"湘江战役后红军还剩多少人？","o":["约1万","约3万","约5万","约7万"],"a":1,"e":"8.6万红军出发，湘江一役锐减至3万余人。鲜血染红湘江，当地百姓说：三年不饮湘江水，十年不食湘江鱼。","t":"经典战役"},
    {"q":"一袋干粮的故事发生在什么时期？","o":["出发阶段","湘江战役","过草地时期","到达陕北后"],"a":2,"e":"13岁小红军谢益先在过草地时把自己仅有的一袋干粮送给一对母女，自己吃野菜。走出草地那天他饿死了。","t":"感人故事"},
    {"q":"以下哪座山不是长征翻越的雪山？","o":["夹金山","梦笔山","长白山","打鼓山"],"a":2,"e":"长白山在东北，不在长征路线上。夹金山(4114m)、梦笔山(4470m)、打鼓山(4800m)均在川西高原。","t":"行军路程"},
    {"q":"毛泽东如何评价长征的意义？","o":["军事演习","宣言书、宣传队、播种机","只是开始","意外事件"],"a":1,"e":"长征是宣言书（宣告红军不可战胜）、宣传队（传播革命思想）、播种机（播下革命种子）。","t":"精神传承"},
    {"q":"遵义会议召开前红军攻占了哪座城市？","o":["贵阳","遵义","重庆","成都"],"a":1,"e":"1935年1月7日突破乌江后攻占遵义，1月15-17日召开遵义会议。遵义因此成为革命历史重要城市。","t":"重要事件"},
    {"q":"长征中负责断后掩护主力的部队通常被称为什么？","o":["先遣队","尖刀连","后卫部队","侦察队"],"a":2,"e":"后卫部队承担最危险任务——阻击追敌、掩护主力。红34师在湘江战役中担任后卫，全师几乎全部牺牲。","t":"军事知识"},
    {"q":"「不到长城非好汉」出自毛泽东哪首词？","o":["《沁园春·雪》","《清平乐·六盘山》","《七律·长征》","《忆秦娥·娄山关》"],"a":1,"e":"出自《清平乐·六盘山》，写于1935年10月翻越六盘山时，这是长征最后一座大山，陕北已近在眼前。","t":"诗词文化"},
    {"q":"中央红军途经多少个省份？","o":["8个","11个","14个","18个"],"a":2,"e":"途经14个省：江西、福建、广东、湖南、广西、贵州、云南、四川、西康、青海、甘肃、河南、湖北、陕西。","t":"基本数据"},
    {"q":"强渡大渡河与飞夺泸定桥的关系是？","o":["同一场战斗","渡河受阻后改道","互不相关","泸定桥就在大渡河上，是配合行动"],"a":3,"e":"泸定桥横跨大渡河。一部分红军在安顺场强渡，但船只太少速度慢，主力北上飞夺泸定桥渡过大渡河。","t":"经典战役"},
    {"q":"长征中红军的粮食主要靠什么？","o":["统一配给","后方运送","打土豪分田地+群众支援","空投补给"],"a":2,"e":"没有后方补给线，靠打土豪没收粮食和沿途群众支援。过雪山草地时粮食极度匮乏。","t":"后勤保障"},
    {"q":"长征途中坚持出版的红军报纸叫什么？","o":["《红色中华》","《红星报》","《新中华报》","《解放日报》"],"a":1,"e":"《红星报》是长征中坚持出版的机关报，编辑带着油印机在极端艰苦条件下坚持出版，鼓舞士气。","t":"文化传播"},
    {"q":"长征出发的决策是在什么背景下做出的？","o":["主动战略进攻","第五次反围剿失败后战略转移","响应共产国际号召","北上抗日主动出击"],"a":1,"e":"由于王明左倾错误导致第五次反围剿失败，中央红军被迫战略转移，最终化危机为转机。","t":"历史背景"},
    {"q":"红二方面军的总指挥是谁？","o":["朱德","彭德怀","贺龙","徐向前"],"a":2,"e":"红二方面军由贺龙、任弼时等率领。贺龙年轻时两把菜刀闹革命。1936年10月在会宁会师。","t":"英雄人物"},
    {"q":"以下关于长征的表述，错误的是？","o":["长征跨越了14个省","长征翻越了18座大山","长征只用了一个月","长征途中召开了遵义会议"],"a":2,"e":"长征用了约368天（中央红军），不是一个月。其他选项都是正确的长征史实。","t":"知识辨析"},
]

qjson = json.dumps(questions, ensure_ascii=False)

# Build JS separately
js_code = f'''\
var Q={qjson};
var R=[{{n:"新兵",e:"⭐",s:0}},{{n:"列兵",e:"🔰",s:100}},{{n:"上等兵",e:"🎖️",s:300}},{{n:"下士",e:"🛡️",s:600}},{{n:"中士",e:"⚔️",s:1000}},{{n:"上士",e:"🏹",s:1500}},{{n:"少尉",e:"⭐",s:2200}},{{n:"中尉",e:"🌟",s:3000}},{{n:"上尉",e:"✨",s:4000}},{{n:"少校",e:"🎯",s:5200}},{{n:"中校",e:"🏅",s:6600}},{{n:"上校",e:"🥇",s:8200}},{{n:"大校",e:"👑",s:10000}},{{n:"少将",e:"💎",s:12500}},{{n:"中将",e:"🔮",s:16000}},{{n:"上将",e:"🏆",s:20000}},{{n:"司令员",e:"🚩",s:25000}}];
var ACH=[{{id:"a1",n:"初露锋芒",d:"首次参与答题",i:"✏️",c:function(){{return D.ta>0}}}},{{id:"a2",n:"答题新星",d:"累计答对10题",i:"📝",c:function(){{return D.tc>=10}}}},{{id:"a3",n:"知识达人",d:"累计答对50题",i:"📚",c:function(){{return D.tc>=50}}}},{{id:"a4",n:"长征学霸",d:"累计答对100题",i:"🎓",c:function(){{return D.tc>=100}}}},{{id:"a5",n:"全对通关",d:"单次5题全对",i:"💯",c:function(){{return D.lr&&D.lr.c===5}}}},{{id:"a6",n:"三日坚持",d:"连续答题3天",i:"🔥",c:function(){{return D.st>=3}}}},{{id:"a7",n:"一周坚持",d:"连续答题7天",i:"📅",c:function(){{return D.st>=7}}}},{{id:"a8",n:"月坚持",d:"连续答题30天",i:"🌟",c:function(){{return D.st>=30}}}},{{id:"a9",n:"闪电答题",d:"5秒内答对一题",i:"⚡",c:function(){{return D.fc<=5}}}},{{id:"a10",n:"千分战士",d:"总积分突破1000",i:"💪",c:function(){{return D.s>=1000}}}},{{id:"a11",n:"五千精英",d:"总积分突破5000",i:"🎯",c:function(){{return D.s>=5000}}}},{{id:"a12",n:"万分开国元勋",d:"总积分突破10000",i:"👑",c:function(){{return D.s>=10000}}}}];
var K="lmq_v3",D;
function ld(){{try{{var r=localStorage.getItem(K);D=r?Object.assign({{s:0,ta:0,tc:0,fc:999,st:0,la:null,sd:null,qh:{{}},ach:[],lr:null}},JSON.parse(r)):{{s:0,ta:0,tc:0,fc:999,st:0,la:null,sd:null,qh:{{}},ach:[],lr:null}}}}catch(e){{D={{s:0,ta:0,tc:0,fc:999,st:0,la:null,sd:null,qh:{{}},ach:[],lr:null}}}}}}
function sv(){{try{{localStorage.setItem(K,JSON.stringify(D))}}catch(e){{}}}}
function td(){{var d=new Date();return d.getFullYear()+"-"+p(d.getMonth()+1)+"-"+p(d.getDate())}}
function p(n){{return n<10?"0"+n:""+n}}
function yd(){{var d=new Date();d.setDate(d.getDate()-1);return d.getFullYear()+"-"+p(d.getMonth()+1)+"-"+p(d.getDate())}}
function uStr(){{var t=td(),y=yd();if(D.la===t)return;if(D.la===y)D.st+=1;else if(D.la!==t)D.st=1;D.la=t;if(!D.sd)D.sd=t}}
function gRk(s){{for(var i=R.length-1;i>=0;i--)if(s>=R[i].s)return R[i];return R[0]}}
function gRkN(s){{return gRk(s).n}}
function ckA(){{var ne=[];for(var i=0;i<ACH.length;i++){{var a=ACH[i];if(D.ach.indexOf(a.id)===-1&&a.c()){{D.ach.push(a.id);ne.push(a)}}}}return ne}}
function toast(m){{var t=document.createElement("div");t.className="toast";t.textContent=m;document.body.appendChild(t);setTimeout(function(){{t.remove()}},3000)}}
function selQ(){{var td_=td(),s=0;for(var i=0;i<td_.length;i++){{s=((s<<5)-s)+td_.charCodeAt(i);s|=0}}var ix=Q.map(function(_,i){{return i}});s=Math.abs(s);for(var i=ix.length-1;i>0;i--){{s=(s*16807+0)%2147483647;var j=s%(i+1),tmp=ix[i];ix[i]=ix[j];ix[j]=tmp}}return ix.slice(0,5).map(function(i){{return Q[i]}})}}
var qs=null,ti=null,ts=0,MT=30;
function startQuiz(){{var td_=td();if(D.qh[td_]&&D.qh[td_].f){{if(!confirm("今天已完成答题！重新挑战不计分，确定吗？"))return}}qs={{q:selQ(),i:0,ans:[],tm:[],sc:0}};switchTab("quiz");rq();document.getElementById("quizResult").style.display="none";document.getElementById("quizCard").style.display="";window.scrollTo(0,0)}}
function rq(){{if(!qs)return;var s=qs,q=s.q[s.i],t_=s.q.length,hd="";for(var i=0;i<t_;i++){{var c="";if(s.ans[i]!=null)c=s.ans[i]===s.q[i].a?"done":"wrong";if(i===s.i&&s.ans[i]==null)c="cur";hd+='<div class="qd '+c+'"></div>'}}document.getElementById("quizDots").innerHTML=hd;document.getElementById("timerFill").style.width="100%";document.getElementById("timerFill").classList.remove("warn");document.getElementById("quizNum").textContent="第 "+(s.i+1)+"/"+t_+" 题";document.getElementById("quizQ").textContent=q.q;var l=["A","B","C","D"],oh="";for(var i=0;i<q.o.length;i++){{var cl="";if(s.ans[s.i]!=null){{if(i===q.a)cl="ok";else if(i===s.ans[s.i])cl="no"}}oh+='<button class="qOpt '+cl+'" onclick="sel('+i+')" '+(s.ans[s.i]!=null?"disabled":"")+'><span class="ol">'+l[i]+'</span>'+q.o[i]+"</button>"}}document.getElementById("quizOpts").innerHTML=oh;var ed=document.getElementById("quizExp"),et=document.getElementById("quizExpT");if(s.ans[s.i]!=null){{ed.classList.add("s");et.textContent=q.e}}else{{ed.classList.remove("s");et.textContent=""}}if(s.ans[s.i]==null)sT()}}
function sT(){{clearInterval(ti);ts=0;ti=setInterval(function(){{ts++;var r=Math.max(0,MT-ts),pct=r/MT*100;document.getElementById("timerFill").style.width=pct+"%";if(r<=8)document.getElementById("timerFill").classList.add("warn");if(r<=0){{clearInterval(ti);if(qs&&qs.ans[qs.i]==null)tUp()}}}},100)}}
function tUp(){{if(!qs)return;qs.ans[qs.i]=-1;qs.tm[qs.i]=MT;rq();setTimeout(an,2000)}}
function sel(x){{if(!qs||qs.ans[qs.i]!=null)return;clearInterval(ti);qs.ans[qs.i]=x;qs.tm[qs.i]=ts;var q=qs.q[qs.i],ok=x===q.a;if(ok){{var bs=100;if(ts<=10)bs+=20;if(ts<=5)bs+=10;var sb=0;for(var i=qs.i-1;i>=0;i--){{if(qs.ans[i]===qs.q[i].a)sb+=10;else break}}qs.sc+=bs+sb;if(ts<D.fc&&ts>0)D.fc=ts}}rq();setTimeout(an,ok?1500:2500)}}
function an(){{if(!qs)return;if(qs.i<qs.q.length-1){{qs.i++;rq()}}else fq()}}
function fq(){{var s=qs,t_=s.q.length,c=0;for(var i=0;i<t_;i++)if(s.ans[i]===s.q[i].a)c++;uStr();var today=td(),ad=!D.qh[today]||!D.qh[today].f;if(ad){{D.s+=s.sc;D.ta+=t_;D.tc+=c;D.lr={{c:c,t:t_,sc:s.sc}};D.qh[today]={{c:c,t:t_,sc:s.sc,f:!0,ts:Date.now()}}}}else{{D.lr={{c:c,t:t_,sc:s.sc}}}}var na=ckA();sv();document.getElementById("quizCard").style.display="none";var rc=document.getElementById("quizResult");rc.style.display="";var pct=Math.round(c/t_*100),ic,mg;if(c===t_){{ic="🎉";mg="太棒了！全部答对！"}}else if(c>=3){{ic="👍";mg="表现不错，继续加油！"}}else{{ic="💪";mg="继续学习，你可以的！"}}document.getElementById("rIcon").textContent=ic;document.getElementById("rScore").textContent="+"+D.lr.sc;document.getElementById("rDetail").innerHTML=mg+'<br>答对 <b>'+c+"</b>/"+t_+" 题 · 正确率 "+pct+'%<br>累计总积分：<b style="color:var(--r)">'+D.s+"</b>";if(na.length)toast(na[na.length-1].i+" 成就解锁："+na[na.length-1].n+"！");uu();qs=null;clearInterval(ti)}}
function uu(){{uH();uL();uK();document.getElementById("streakBadge").textContent="🔥 连续 "+D.st+" 天"}}
function uH(){{var rk=gRk(D.s),nr_i=R.indexOf(rk)+1,nr=nr_i<R.length?R[nr_i]:null;document.getElementById("rankEmoji").textContent=rk.e;document.getElementById("rankName").textContent=rk.n;if(nr){{var p_=D.s-rk.s,nd=nr.s-rk.s,pt=Math.min(100,p_/nd*100);document.getElementById("rankSub").textContent="距"+nr.n+"还需 "+(nd-p_)+" 积分";document.getElementById("expBar").style.width=pt+"%";document.getElementById("expDetail").textContent=p_+"/"+nd+" 积分"}}else{{document.getElementById("rankSub").textContent="已到达最高军衔！";document.getElementById("expBar").style.width="100%";document.getElementById("expDetail").textContent=D.s+" 积分"}}document.getElementById("sScore").textContent=D.s.toLocaleString();document.getElementById("sCorrect").textContent=D.tc;document.getElementById("sAccuracy").textContent=(D.ta>0?Math.round(D.tc/D.ta*100):0)+"%";var t_=td(),done=D.qh[t_]&&D.qh[t_].f;if(done){{document.getElementById("todayIcon").textContent="✅";document.getElementById("todayTitle").textContent="今日已完成";document.getElementById("todayDesc").textContent="答对"+D.qh[t_].c+"/"+D.qh[t_].t+"题，得分+"+D.qh[t_].sc;document.getElementById("startBtn").textContent="🔄 重新挑战";document.getElementById("startBtn").className="btn btn2 btnL"}}else{{document.getElementById("todayIcon").textContent="📝";document.getElementById("todayTitle").textContent="今日挑战";document.getElementById("todayDesc").textContent="每天5道长征知识题，巩固红色记忆";document.getElementById("startBtn").textContent="⚡ 开始今日答题";document.getElementById("startBtn").className="btn btn1 btnL"}}document.getElementById("todayInfo").textContent=done?"今日得分：+"+D.qh[t_].sc+" 分":"";var ag=document.getElementById("achGrid"),ah="";for(var i=0;i<ACH.length;i++){{var a=ACH[i],got=D.ach.indexOf(a.id)!==-1;ah+='<div class="ach'+(got?" got":" lock")+'"><div class="ai">'+(got?a.i:"🔒")+'</div><div class="an">'+a.n+'</div><div class="ad">'+a.d+"</div></div>"}}ag.innerHTML=ah}}
var MU=[{{n:"红色学者",a:"红",ts:15420,ws:320,ds:450}},{{n:"长征铁粉",a:"征",ts:12800,ws:280,ds:380}},{{n:"星火燎原",a:"星",ts:9650,ws:410,ds:520}},{{n:"雪山之鹰",a:"鹰",ts:8420,ws:190,ds:300}},{{n:"赤水行者",a:"赤",ts:7200,ws:350,ds:410}},{{n:"铁索勇士",a:"铁",ts:6100,ws:220,ds:250}},{{n:"草地铁流",a:"草",ts:5300,ws:160,ds:180}},{{n:"遵义先锋",a:"遵",ts:4100,ws:290,ds:350}},{{n:"瑞金传人",a:"瑞",ts:2800,ws:130,ds:200}},{{n:"湘江后浪",a:"湘",ts:1500,ws:95,ds:150}},{{n:"会宁新兵",a:"会",ts:620,ws:60,ds:90}}];
var crt="total";
function swRank(t,b){{crt=t;var bs=document.querySelectorAll(".rtab");for(var i=0;i<bs.length;i++)bs[i].classList.remove("on");b.classList.add("on");uL()}}
function uL(){{var t_=td(),ws_="",d_=new Date();d_.setDate(d_.getDate()-d_.getDay());ws_=d_.getFullYear()+"-"+p(d_.getMonth()+1)+"-"+p(d_.getDate());var mw=0,md=0;for(var dt in D.qh){{if(dt>=ws_)mw+=D.qh[dt].sc||0;if(dt===t_)md=D.qh[dt].sc||0}}var me={{n:"我",a:"我",ts:D.s,ws:mw,ds:md,isMe:!0}};var al=MU.map(function(u){{return Object.assign({{}},u,{{isMe:!1}})}});al.push(me);var key=crt==="total"?"ts":(crt==="weekly"?"ws":"ds");al.sort(function(a,b){{return b[key]-a[key]}});var c=document.getElementById("rankList"),mr=-1,html="";for(var i=0;i<Math.min(20,al.length);i++){{var u=al[i];if(u.isMe)mr=i+1;var mdls=["🥇","🥈","🥉"],num=i<3?mdls[i]:'<span style="color:#999;font-weight:700">'+(i+1)+"</span>";var val=crt==="total"?u.ts.toLocaleString()+"分":(crt==="weekly"?u.ws+"分":u.ds+"分");html+='<div class="ritem'+(u.isMe?" me":"")+'"><div style="font-size:20px;width:32px;text-align:center;flex-shrink:0">'+num+'</div><div class="rav">'+u.a+'</div><div class="rinfo"><div class="rn">'+u.n+(u.isMe?' <span style="color:var(--r);font-size:11px">(我)</span>':"")+'</div><div class="rsub">'+gRkN(u.ts)+'</div></div><div class="rs">'+val+"</div></div>"}}c.innerHTML=html;document.getElementById("myRank").textContent=mr>0?"#"+mr:"-"}}
function uK(){{document.getElementById("kCount").textContent=Q.length;var h="";for(var i=0;i<Q.length;i++){{var q=Q[i];h+='<div class="kitem"><div class="kq">❓ '+q.q+'</div><div class="ka">✅ 正确答案：'+q.o[q.a]+'</div><div class="ke">📖 '+q.e+'</div><span class="kt">'+q.t+"</span></div>"}}document.getElementById("klist").innerHTML=h}}
function shareText(){{var rk=gRk(D.s),pct=D.ta>0?Math.round(D.tc/D.ta*100):0;var t="🚩 长征红色问答挑战\\n\\n⭐ 当前军衔："+rk.n+" | 总积分："+D.s+"\\n✅ 累计答对："+D.tc+"题 | 正确率："+pct+"%\\n🔥 连续打卡："+D.st+"天\\n\\n📖 学习长征历史，传承红色基因！\\n👉 快来加入挑战吧！";if(navigator.share){{navigator.share({{title:"长征红色问答挑战",text:t}}).catch(function(){{}})}}else{{copyText(t);alert("已复制到剪贴板！")}}}}
function copyText(t){{var ta=document.createElement("textarea");ta.value=t;ta.style.position="fixed";ta.style.opacity="0";document.body.appendChild(ta);ta.select();try{{document.execCommand("copy")}}catch(e){{}}document.body.removeChild(ta)}}
function switchTab(n){{var ps=document.querySelectorAll(".page");for(var i=0;i<ps.length;i++)ps[i].classList.remove("on");var pg=document.getElementById("pg-"+n);if(pg)pg.classList.add("on");var ts_=document.querySelectorAll(".tab-i");for(var i=0;i<ts_.length;i++)ts_[i].classList.remove("on");var tb=document.querySelector('[data-tab="'+n+'"]');if(tb)tb.classList.add("on");window.scrollTo(0,0);if(n!=="quiz"){{clearInterval(ti)}}}}
ld();uu();uK();
'''

# Validate JS
import subprocess, tempfile, os
tmp = os.path.join(tempfile.gettempdir(), 'vjs.js')
with open(tmp, 'w', encoding='utf-8') as f:
    f.write(js_code)
r = subprocess.run(['node', '--check', tmp], capture_output=True, text=True)
if r.returncode == 0:
    print('JS syntax: PASSED')
else:
    print('JS syntax FAILED:')
    print(r.stderr[:300])
    exit(1)

# Read CSS from existing file, or use compact version
css = open('index.html', 'r', encoding='utf-8').read()
cs = css.index('<style>') + 7
ce = css.index('</style>', cs)
css_content = css[cs:ce].strip()

html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0,user-scalable=no">
<title>长征红色问答挑战</title>
<style>
{css_content}
</style>
</head>
<body>

<header class="header">
<div class="logo">⭐ 长征红色问答挑战</div>
<div class="streak" id="streakBadge">🔥 连续 1 天</div>
</header>

<main class="main">

<section class="page on" id="pg-home">
<div class="card"><div class="rank-box">
<div class="rank-badge" id="rankEmoji">⭐</div>
<div class="rank-name" id="rankName">新兵</div>
<div class="rank-sub" id="rankSub">开始答题，解锁更高军衔！</div>
<div class="exp-track"><div class="exp-fill" id="expBar" style="width:0%"></div></div>
<div class="exp-info" id="expDetail">0/100 积分</div>
</div></div>

<div class="card"><div class="ct">📊 我的战绩</div>
<div class="stats">
<div class="stat"><div class="sv" id="sScore">0</div><div class="sl">总积分</div></div>
<div class="stat"><div class="sv" id="sCorrect">0</div><div class="sl">答对题数</div></div>
<div class="stat"><div class="sv" id="sAccuracy">0%</div><div class="sl">正确率</div></div>
</div></div>

<div class="card" style="text-align:center">
<div style="font-size:42px;margin-bottom:6px" id="todayIcon">📝</div>
<div style="font-size:17px;font-weight:700" id="todayTitle">今日挑战</div>
<div style="font-size:13px;color:var(--t3);margin:4px 0 14px" id="todayDesc">每天5道长征知识题，巩固红色记忆</div>
<button class="btn btn1 btnL" id="startBtn" onclick="startQuiz()">⚡ 开始今日答题</button>
<div style="font-size:12px;color:var(--t3);margin-top:6px" id="todayInfo"></div>
</div>

<div class="card"><div class="ct">🏅 成就徽章</div>
<div class="ach-grid" id="achGrid"></div></div>

<div style="display:flex;gap:8px">
<button class="btn btn2" style="flex:1" onclick="switchTab('knowledge')">📚 知识库</button>
<button class="btn btn1" style="flex:1" onclick="shareText()">📤 分享战绩</button>
</div>
</section>

<section class="page" id="pg-quiz">
<div class="card" id="quizCard">
<div class="quiz-dots" id="quizDots"></div>
<div class="quiz-timer"><div class="quiz-timer-fill" id="timerFill" style="width:100%"></div></div>
<div class="quiz-num" id="quizNum"></div>
<div class="quizQ" id="quizQ"></div>
<div class="quizOpts" id="quizOpts"></div>
<div class="qExp" id="quizExp"><div class="et">📖 知识解析</div><div id="quizExpT"></div></div>
</div>

<div class="card" id="quizResult" style="display:none"><div class="qRes">
<div class="rIcon" id="rIcon">🎉</div>
<div class="rScore" id="rScore">+500</div>
<div class="rLabel">本次获得积分</div>
<div class="rDetail" id="rDetail"></div>
<button class="btn btnG btnL" style="margin-top:10px" onclick="shareText()">📤 晒出成绩，分享好友</button>
<button class="btn btn2" style="width:100%;margin-top:8px" onclick="switchTab('home')">🏠 返回首页</button>
</div></div>
</section>

<section class="page" id="pg-leaderboard">
<div class="rank-tabs">
<button class="rtab on" onclick="swRank('total',this)">🏆 总榜</button>
<button class="rtab" onclick="swRank('weekly',this)">📅 周榜</button>
<button class="rtab" onclick="swRank('daily',this)">🔥 日榜</button>
</div>
<div class="rlist" id="rankList"></div>
<div class="card" style="margin-top:12px;text-align:center"><div style="color:var(--t2)">我的排名</div><div style="font-size:28px;font-weight:800;color:var(--r)" id="myRank">-</div></div>
</section>

<section class="page" id="pg-knowledge">
<div class="card"><div class="ct">📚 长征红色知识库</div>
<div style="font-size:13px;color:var(--t3);margin-bottom:12px">已收录 <b id="kCount">50</b> 道题目，含详细历史解析</div>
<div class="klist" id="klist"></div></div>
</section>

</main>

<nav class="tab-bar">
<button class="tab-i on" data-tab="home" onclick="switchTab('home')"><span class="ti">🏠</span>首页</button>
<button class="tab-i" data-tab="quiz" onclick="switchTab('quiz')"><span class="ti">✏️</span>答题</button>
<button class="tab-i" data-tab="leaderboard" onclick="switchTab('leaderboard')"><span class="ti">🏆</span>排行</button>
<button class="tab-i" data-tab="knowledge" onclick="switchTab('knowledge')"><span class="ti">📚</span>知识</button>
</nav>

<script>
{js_code}
</script>
</body>
</html>'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print(f'index.html written: {len(html)} bytes, {len(questions)} questions')
print('DONE!')
