
(function(){if(QZONE.namecard&&QZONE.namecard.funInit){return;}
if(!window.QZONE.namecardData){window.QZONE.namecardData={initData:[],pd:{}}}
var _top=(function(){var _t=window;try{do{_t=_t.parent;}
while(_t!=top)}catch(e){}
return _t;})();window.QZONE.namecard={init:function(root,opt){var p=QZONE.namecard;if(typeof(root)=="string"){root=$(root);}
opt=opt||{};root=root||document.body;QZONE.namecardData.initData.push(Array.prototype.slice.call(arguments,0));QZFL.event.delegate(root,'.q_namecard','mouseenter',p._countDown,[opt]);QZFL.event.delegate(root,'.q_namecard','mouseleave',p._clearCountDown);},_countDown:function(evt,opt){var p=QZONE.namecard,evt=getEvent(evt),el=this,pos,mx,my,quin,mh,ln;if(!_top||!_top.checkLogin||_top.checkLogin()<=10000){return;}
if(p.loadMainJs){if(!(quin=el.quin)){ln=el.getAttribute("link");if(ln){mh=ln.match(/nameCard_(\w{1,48}?)(\s|$)/);mh&&(el.quin=quin=mh[1]);}}
if(quin){QZONE.namecardData.pd={uin:el.quin,mX:typeof(mx)!="undefined"?mx:evt.clientX,mY:typeof(my)!="undefined"?my:evt.clientY}
el.loadtimer=setTimeout((function(o){o.from=el.getAttribute("data-from");o.index=el.getAttribute("data-index");return function(){QZONE.namecard.loadMainJs(o);}})(opt),300);}}},_clearCountDown:function(evt){var el=this;QZONE.namecardData.pd=null;if(el&&el.loadtimer){clearTimeout(el.loadtimer);}},loadMainJs:function(o){var _l=new QZFL.JsLoader(),_d=_top.siDomain||"qzonestyle.gtimg.cn";_l.onload=function(){var p=QZONE.namecard,tmp=QZONE.namecardData;for(var i=0,len=tmp.initData.length;i<len;i++){QZFL.event.undelegate(tmp.initData[i][0],'.q_namecard','mouseenter');QZFL.event.undelegate(tmp.initData[i][0],'.q_namecard','mouseleave');p.init.apply(QZONE.namecard,tmp.initData[i]);}
if(tmp.pd&&tmp.pd.mX){var pp=tmp.pd;p.showNC(pp.uin,pp.mX,pp.mY,o);}}
_l.load(location.protocol+"//"+_d+"/qzone/v5/namecard.js",document,"utf-8");}};})();