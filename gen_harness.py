# -*- coding: utf-8 -*-
"""生成坦克大战 v3 无头测试 harness.js：DOM 桩 + 游戏脚本 + 测试用例"""
import re

html = open(r'D:\outputs\竞赛训练营\tank-game.html', encoding='utf-8').read()
src = re.findall(r'<script>(.*?)</script>', html, re.S)[-1]

stub = r'''
// ================= 最小 DOM 桩 =================
var __grad={addColorStop(){}};
function __ctx(){return new Proxy({},{get:(t,k)=>{
  if(k==='createLinearGradient')return()=>__grad;
  if(k==='createRadialGradient')return()=>__grad;
  if(k==='measureText')return()=>({width:0});
  return()=>{};
},set:()=>true})}
function __mkCanvas(){return {width:960,height:600,getContext:__ctx}}
var __elems={};
function __mkElem(id){return {classList:{add(){},remove(){},toggle(){}},textContent:'',innerHTML:'',
  dataset:{},style:{},addEventListener(){},querySelectorAll(){return []}}}
var document={
  getElementById(id){return id==='game'?__mkCanvas():(__elems[id]??=__mkElem(id))},
  createElement(t){return t==='canvas'?__mkCanvas():{getContext:__ctx}},
  querySelectorAll(){return []},
  addEventListener(){}
};
function addEventListener(){}
function requestAnimationFrame(){}
var Image=function(){this.src='';this.onload=null;this.onerror=null;};
var __errors=[];
function check(name,cond,extra){
  if(cond){console.log('  OK '+name)}
  else{__errors.push(name);console.log('  FAIL '+name+(extra!==undefined?' | '+extra:''))}
}
'''

test = r'''
console.log('【1】主界面 + 闯关开局');
check('初始为主界面',state==='menu',state);
advance();check('主界面回车无动作',state==='menu');
showSelect('campaign');check('进入坦克选择',state==='select');
startGame(1);check('选坦克后 ready',state==='ready');
check('模式为闯关',mode==='campaign');
check('初始生命 3 / 守护 3',lives===3&&guards===3);
check('营地 7 耐久',baseHp===7&&baseMaxHp===7);
check('金币不重置（=meta.coins）',coins===meta.coins);
advance();check('推进后 playing',state==='playing');
// 规则返回主界面
state='rules';advance();check('规则面板可返回主界面',state==='menu');
showSelect('campaign');startGame(1);advance();

console.log('【2】玩家 3 发血量 + 受击无敌 0.5s');
player.invT=0;player.shieldT=0;
for(let k=0;k<2;k++){bullets.push({x:player.x+10,y:player.y+10,dx:0,dy:0,speed:0,dmg:1,friendly:0});step();player.invT=0}
check('中2发不死',player.hp===1&&lives===3,'hp='+player.hp);
bullets.push({x:player.x+10,y:player.y+10,dx:0,dy:0,speed:0,dmg:1,friendly:0});step();
check('中3发掉命重生满血',lives===2&&player.hp===player.maxHp,'lives='+lives);
player.hp=player.maxHp;player.invT=0;player.shieldT=0;
bullets.push({x:player.x+10,y:player.y+10,dx:0,dy:0,speed:0,dmg:1,friendly:0});step();
check('受击后无敌 0.5 秒(30帧)',player.invT===30,'invT='+player.invT);
player.invT=0;

console.log('【3】击杀得金币（持久化到 meta）');
var cBefore=meta.coins;
enemies=[{x:player.x,y:player.y-80,dir:'down',cool:999,ai:0,kind:'basic',hunter:false,spawnT:0,hp:1,sp:0,color:'#e05a4e',score:100,hitT:0}];
bullets.push({x:enemies[0].x+10,y:enemies[0].y+10,dx:0,dy:0,speed:0,dmg:1,friendly:1});step();
check('击杀得分+100',score>=100,'score='+score);
check('击杀金币持久化',meta.coins>cBefore,'meta.coins='+meta.coins);

console.log('【4】过关进商店 + 局内购买');
foesTotal=0;enemies=[];checkLevelEnd();
check('过关进入商店',state==='shop',state);
coins=2000;meta.coins=2000;
var dmg0=player.dmg,speed0=player.speed,bcool0=player.bcool,maxHp0=player.maxHp,baseMax0=baseMaxHp;
buy('dmg');check('火力+1',player.dmg===dmg0+1);
buy('speed');check('移速提升',player.speed>speed0);
buy('cool');check('射速提升',player.bcool<bcool0);
buy('hp');check('血量上限+1',player.maxHp===maxHp0+1);
buy('life');check('生命+1',lives===3);
buy('base');check('营地加固上限+2',baseMaxHp===baseMax0+2);
buy('wall');check('钢墙护营已购',steelWallNext===true);
coins=0;meta.coins=0;buy('speed');
check('金币不足无法购买',coins===0,'coins='+coins);

console.log('【5】进入下一关 + 生命重置 + 钢墙一次性');
advance();
check('进入第 2 关 ready',state==='ready'&&level===2,'state='+state+',lv='+level);
check('钢墙消耗',steelWallNext===false);
check('营地保护墙为钢墙',map[12][10]===2);
check('生命重置 3',lives===3);

console.log('【6】道具系统（8 种）');
var d0=player.dmg;applyItem('star');check('火力+1',player.dmg===d0+1);
baseHp=baseMaxHp;applyItem('repair');check('修理不超上限',baseHp===baseMaxHp);
baseHp=1;applyItem('repair');check('修理+2',baseHp===3);
applyItem('shield');
bullets.push({x:player.x+10,y:player.y+10,dx:0,dy:0,speed:0,dmg:1,friendly:0});step();
check('护盾期间不掉血',player.hp===player.maxHp);
player.shieldT=0;
enemies=[{x:200,y:200,dir:'down',cool:999,ai:0,kind:'basic',hunter:false,spawnT:0,hp:1,sp:2,color:'#e05a4e',score:100,hitT:0}];
applyItem('freeze');var ey=enemies[0].y;for(var i=0;i<60;i++)step();
check('冻结敌军不动',enemies.length===0||enemies[0].y===ey);
freezeT=0;
enemies=[{x:200,y:200,dir:'down',cool:999,ai:0,kind:'basic',hunter:false,spawnT:0,hp:1,sp:0,color:'#e05a4e',score:100,hitT:0},{x:400,y:200,dir:'down',cool:999,ai:0,kind:'fast',hunter:false,spawnT:0,hp:1,sp:0,color:'#e08a3e',score:150,hitT:0}];
var sc0=score;applyItem('bomb');check('清屏歼灭敌军',enemies.length===0);check('清屏计入得分',score>sc0);
var cn0=coins;applyItem('coin');check('金币+80',coins>cn0);
lives=1;applyItem('life');check('加命+1',lives===2);
lives=5;applyItem('life');check('加命上限5',lives===5);
rapidT=0;player.cool=0;var bc=player.bcool;applyItem('rapid');fire(player,1);
check('速射冷却×0.4',player.cool===Math.round(bc*0.4));
check('道具标签均两字',ITEM_KEYS.every(k=>ITEM_TYPES[k].label.length===2));

console.log('【7】闯关 12 关 + BOSS');
check('闯关共 12 关',LEVELS.length===12&&CAMPAIGN_LEVELS===12,'len='+LEVELS.length);
level=4;setupLevel();state='playing';
check('第4关 BOSS 血量 24',boss&&boss.hp===24);
check('BOSS 出场召唤小怪',enemies.length>=1,'enemies='+enemies.length);
check('BOSS 关无自动刷怪(foesTotal=0)',foesTotal===0);
level=8;setupLevel();
check('第8关 BOSS 血量 42',boss&&boss.hp===42);
level=12;setupLevel();
check('第12关最终 BOSS 血量 54',boss&&boss.hp===54);
level=12;foesTotal=0;enemies=[];boss.hp=1;
bullets.push({x:boss.x+10,y:boss.y+10,dx:0,dy:0,speed:0,dmg:1,friendly:1});step();
enemies=[];checkLevelEnd();   // 清掉 BOSS 濒死召唤的增援，验证仍可通关
check('闯关通关进入 win',state==='win',state);
check('胜利标题为全部通关',winTitle.indexOf('全部通关')>=0,'winTitle='+winTitle);

console.log('【7b】BOSS 防卡死（出生区清空 / 可移动 / 碾砖开路）');
level=8;setupLevel();state='playing';
check('第8关 BOSS 已生成',boss&&!boss.dead);
// 出生区不得有墙（第8关原地图出生格上有钢墙，会导致出生即卡死）
var bc0=Math.floor(boss.x/CELL),bc1=Math.floor((boss.x+boss.size-1)/CELL);
var br0=Math.floor(boss.y/CELL),br1=Math.floor((boss.y+boss.size-1)/CELL);
var embedded=false;
for(var rr=br0;rr<=br1;rr++)for(var cc=bc0;cc<=bc1;cc++)if(map[rr][cc]!==0)embedded=true;
check('BOSS 出生未嵌进墙体',!embedded,'cell='+map[br1][bc0]+','+map[br1][bc1]);
// 连续跑 300 帧，BOSS 必须发生位移（不被墙卡死）
var bx0=boss.x,by0=boss.y;
for(var i=0;i<300;i++){if(boss&&!boss.dead)bossThink();else break}
check('BOSS 300 帧内可移动',boss.x!==bx0||boss.y!==by0,'dx='+(boss.x-bx0).toFixed(1)+',dy='+(boss.y-by0).toFixed(1));
// 前方有砖 → 应整排碾碎
boss.x=11*CELL+4;boss.y=2*CELL+8;boss.dir='down';boss.ai=999;boss.stuck=0; // 车身底部紧贴砖墙，向下即被挡
map[2][11]=0;map[2][12]=0;map[3][11]=0;map[3][12]=0;
map[4][11]=1;map[4][12]=1;                      // 正前方一整排砖
bossThink();
check('BOSS 碾碎前方砖墙',map[4][11]===0&&map[4][12]===0,'map='+map[4][11]+','+map[4][12]);
// 车身嵌入砖墙时（如回溯还原地图）也能碾掉脱困
boss.x=11*CELL+4;boss.y=2*CELL;boss.dir='down';boss.ai=999;boss.stuck=0;
map[2][11]=0;map[2][12]=0;map[3][11]=1;map[3][12]=1;   // 车身覆盖行是砖
bossThink();
check('BOSS 碾掉嵌入车身的砖',map[3][11]===0&&map[3][12]===0,'map='+map[3][11]+','+map[3][12]);
// 长时间被钢墙围住 → 兜底换向（stuck 计数归零且方向改变）
boss.x=11*CELL+4;boss.y=2*CELL;boss.stuck=95;boss.dir='down';
map[4][11]=2;map[4][12]=2;                      // 钢墙不可碾
var dir0=boss.dir;bossThink();
check('卡死兜底触发换向',boss.stuck===0||boss.dir!==dir0||boss.ai===0,'stuck='+boss.stuck+',dir='+boss.dir);

console.log('【7c】敌军任务逻辑：打基地为主 / 打玩家为次要');
startGame(1,'campaign');advance();
// ① 远离玩家 → 不转猎手，始终以基地为目标
player.x=1*CELL;player.y=12*CELL;
enemies=[{x:22*CELL,y:1*CELL,dir:'down',cool:999,ai:0,kind:'fast',hunter:false,chaseT:0,spawnT:0,hp:1,sp:0,color:'#e08a3e',score:150,hitT:0}];
for(i=0;i<60;i++)enemyThink(enemies[0]);
check('远离玩家时不转猎手（主任务=基地）',enemies[0].hunter===false);
// ② 玩家靠近 → 可临时转猎手，但同时最多 2 辆
player.x=11*CELL;player.y=8*CELL;
enemies=[];
for(var k=0;k<5;k++)enemies.push({x:(9+k)*CELL,y:8*CELL,dir:'down',cool:999,ai:0,kind:'fast',hunter:false,chaseT:0,spawnT:0,hp:1,sp:0,color:'#e08a3e',score:150,hitT:0});
for(i=0;i<200;i++)enemies.forEach(enemyThink);
var hn=enemies.filter(e=>e.hunter).length;
check('猎手同时不超过 2 辆',hn<=2,'hunters='+hn);
// ③ 追击超时 → 回归打基地
enemies[0].hunter=true;enemies[0].chaseT=5;
for(i=0;i<12;i++)enemyThink(enemies[0]);
check('追击超时回归打基地',enemies[0].hunter===false);
// ④ 玩家拉开距离 → 立即回归打基地
enemies[0].hunter=true;enemies[0].chaseT=300;enemies[0].ai=0;
player.x=1*CELL;player.y=12*CELL;
enemyThink(enemies[0]);
check('玩家远离后立即回归打基地',enemies[0].hunter===false);

console.log('【7d】贴脸基地不开火修复：左右相邻列(10/13, 第13行)应朝基地开火');
startGame(1,'campaign');advance();
// 旧逻辑：基地只占 11~12 列，紧贴其左(列10)/右(列13)的敌人在第13行既无竖直对位、又不在开火窗口内，永不射击
var eL={x:10*CELL,y:13*CELL,dir:'right',cool:0,ai:0,kind:'basic',hunter:false,chaseT:0,spawnT:0,hp:1,sp:0,color:'#e05a4e',score:100,hitT:0};
check('左贴脸(列10)可朝基地开火',clearShotToBase(eL)===true&&eL.dir==='right','ret='+clearShotToBase(eL)+',dir='+eL.dir);
var eR={x:13*CELL,y:13*CELL,dir:'left',cool:0,ai:0,kind:'basic',hunter:false,chaseT:0,spawnT:0,hp:1,sp:0,color:'#e05a4e',score:100,hitT:0};
check('右贴脸(列13)可朝基地开火',clearShotToBase(eR)===true&&eR.dir==='left','ret='+clearShotToBase(eR)+',dir='+eR.dir);
// 玩家远离 → 主任务=基地；确认 enemyThink 实际产生子弹
enemies=[eL];bullets=[];player.x=1*CELL;player.y=1*CELL;
var b0=bullets.length;for(var i=0;i<20;i++)enemyThink(eL);
check('贴脸敌军 enemyThink 实际开火',bullets.length>b0,'bullets='+(bullets.length-b0));

console.log('【7e】敌军出生保护：出生瞬间不被秒杀，子弹穿过，保护结束可击伤');
startGame(1,'campaign');advance();
enemies=[{x:5*CELL,y:2*CELL,dir:'down',cool:999,ai:0,kind:'basic',hunter:false,chaseT:0,spawnT:24,invT:40,hp:2,sp:0,color:'#e05a4e',score:100,hitT:0}];
var eh=enemies[0].hp;
bullets.push({x:5*CELL+5,y:2*CELL+5,dx:0,dy:0,speed:0,dmg:1,friendly:1});step();
check('出生保护期不受伤',enemies.length===1&&enemies[0].hp===eh,'hp='+(enemies[0]?enemies[0].hp:'gone'));
check('出生保护期子弹穿过不消耗',bullets.length===1,'bullets='+bullets.length);
enemies[0].invT=0;bullets=[];
bullets.push({x:5*CELL+5,y:2*CELL+5,dx:0,dy:0,speed:0,dmg:1,friendly:1});step();
check('保护期结束可被击伤',enemies.length===1&&enemies[0].hp===eh-1,'hp='+(enemies[0]?enemies[0].hp:'gone'));

console.log('【8】生存模式 + 里程碑 + buff（最高 10 天无 BOSS）');
startGame(1,'survival');advance();
check('模式为生存',mode==='survival');
check('第1波敌军数 7',levelCfg().total===7,'total='+levelCfg().total);
check('生存无 BOSS',!levelCfg().boss);
foesTotal=0;enemies=[];checkLevelEnd();
check('生存过关进商店',state==='shop');
advance();
check('进入第2波',level===2&&state==='ready');
check('生存过关营地修复+1',baseHp<=baseMaxHp);
// 里程碑 5 天
level=5;setupLevel();state='playing';foesTotal=0;enemies=[];var c5=meta.coins;checkLevelEnd();
check('生存5天奖励金币(新公式≈185)',meta.coins===c5+185,'+'+(meta.coins-c5));
advance();
// 里程碑 10 天 → 生存通关 + 永久 buff + 庆典
meta.buff=false;saveMeta();var gm0=goldMul();
level=10;setupLevel();state='playing';foesTotal=0;enemies=[];checkLevelEnd();
check('生存10天通关进入 win',state==='win',state);
check('生存10天解锁黄金徽章',meta.buff===true);
check('金币增益 1.15',goldMul()>gm0,'goldMul='+goldMul());
check('胜利标题为生存大师',winTitle.indexOf('生存大师')>=0,'winTitle='+winTitle);
check('胜利庆典彩屑生成',celeb.length>0,'celeb='+celeb.length);
advance();

console.log('【9】永久升级 + 金币持久化');
meta.perm={dmg:0,speed:0,cool:0,hp:0,base:0};saveMeta();
coins=2000;meta.coins=2000;
var pc0=permCost(PERM[0]);
buyPerm('dmg');
check('永久火力+1',meta.perm.dmg===1);
check('金币扣除',meta.coins===2000-pc0,'meta.coins='+meta.coins);
check('费用随等级上涨',permCost(PERM[0])>pc0,'cost='+permCost(PERM[0]));
// 永久升级作用于新开局
coins=500;meta.coins=500;startGame(2,'campaign');
check('永久火力带入新局',player.dmg===TANK_TYPES[2].dmg+meta.perm.dmg,'dmg='+player.dmg);
check('金币跨局保留',coins===500&&meta.coins===500);

console.log('【10】时间倒流：敌军不堆叠可行动 + 砖墙恢复');
startGame(1,'campaign');advance();
enemies=[{x:200,y:400,dir:'down',cool:999,ai:0,kind:'basic',hunter:false,spawnT:0,hp:1,sp:1,color:'#e05a4e',score:100,hitT:0},
 {x:400,y:400,dir:'down',cool:999,ai:0,kind:'basic',hunter:false,spawnT:0,hp:1,sp:1,color:'#e05a4e',score:100,hitT:0},
 {x:600,y:400,dir:'down',cool:999,ai:0,kind:'basic',hunter:false,spawnT:0,hp:1,sp:1,color:'#e05a4e',score:100,hitT:0},
 {x:500,y:300,dir:'down',cool:999,ai:0,kind:'fast',hunter:false,spawnT:0,hp:1,sp:1.5,color:'#e08a3e',score:150,hitT:0}];
map[12][10]=EMPTY;                       // 打掉一块基地旁砖墙
startRewind();
check('基地旁砖墙倒流恢复',map[12][10]===1,'map[12][10]='+map[12][10]);
var tx=rewindList.map(r=>Math.round(r.tx)+','+Math.round(r.ty));
check('回退目标分散到不同位置',new Set(tx).size>=3,'tx='+tx.join(' | '));
for(var i=0;i<110;i++)step();
check('倒流结束回 playing',state==='playing');
var overlap=enemies.some((a,i)=>enemies.some((b,j)=>i<j&&Math.abs(a.x-b.x)<30&&Math.abs(a.y-b.y)<30));
check('回退后敌军不重叠',!overlap);
// 回退后敌军应能正常行动（不卡死）
var before=enemies.map(e=>e.x+','+e.y);
for(i=0;i<80;i++)step();
var moved=enemies.some((e,k)=>e.x+','+e.y!==before[k]);
check('回退后敌军可正常行动',moved);

console.log('【10b】回溯台词（前两次随机/嘲讽 + 最后一次警示）');
startGame(1,'campaign');advance();
check('开局守护 3 次',guards===3,'guards='+guards);
check('嘲讽台词不含敌军/敌人',!REWIND_MSGS.some(m=>m.t.indexOf('敌军')>=0||m.t.indexOf('敌人')>=0),
  REWIND_MSGS.filter(m=>m.t.indexOf('敌军')>=0||m.t.indexOf('敌人')>=0).map(m=>m.t).join('|'));
startRewind();                                  // 第 1 次：3→2
check('第1次回溯有台词',rewindMsg.length>0,'msg='+rewindMsg);
check('第1次非最后警示',rewindMsg!==REWIND_LAST);
for(i=0;i<110;i++)step();
check('第1次后剩余 2 次',guards===2,'guards='+guards);
startRewind();                                  // 第 2 次：2→1
check('第2次回溯有台词',rewindMsg.length>0&&rewindMsg!==REWIND_LAST,'msg='+rewindMsg);
for(i=0;i<110;i++)step();
check('第2次后剩余 1 次',guards===1,'guards='+guards);
startRewind();                                  // 第 3 次：1→0
check('最后一次用警示文案',rewindMsg===REWIND_LAST,'msg='+rewindMsg);
check('最后一次为警示色',rewindColor==='#ff7a6e','color='+rewindColor);
check('最后一次守护归零',guards===0,'guards='+guards);
for(i=0;i<110;i++)step();
baseHp=1;bullets.push({x:BASE.x+10,y:BASE.y+10,dx:0,dy:0,speed:0,dmg:1,friendly:0});step();
check('守护耗尽后失守判负',state==='over',state);

console.log('【11】随机模拟（闯关3轮 + 生存3轮）');
for(var round=0;round<6;round++){
  try{
    var m=(round<3)?'campaign':'survival';
    startGame(round%3,m);advance();
    keys={};
    for(var f=0;f<60*90;f++){
      step();
      if(f%90===0)keys={up:f%180===0,right:f%180!==0,down:0,left:0};
      if(f%20===0&&state==='playing')fire(player,1);
      if(state==='shop'){
        var afford=SHOP.filter(s=>coins>=s.cost&&(bought[s.id]||0)<s.max);
        if(afford.length)buy(afford[0].id);
        advance();
      }
      if(state==='over'||state==='win')break;
      if(state==='ready')advance();
    }
    console.log('  OK '+m+'第'+(round%3+1)+'轮：state='+state+' level='+level+' score='+score+' coins='+coins);
  }catch(err){
    __errors.push(m+'第'+(round%3+1)+'轮异常');
    console.log('  FAIL '+m+'第'+(round%3+1)+'轮：'+err.message+'\n'+err.stack.split('\n')[1]);
  }
}

console.log('');
console.log(__errors.length===0?'ALL PASS':'FAILED '+__errors.length+': '+__errors.join('；'));
'''

with open(r'D:\outputs\竞赛训练营\harness.js', 'w', encoding='utf-8') as f:
    f.write(stub + src + test)
print('harness.js written,', len(stub + src + test), 'chars')
