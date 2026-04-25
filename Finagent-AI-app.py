<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>🌟 My FlashDeal Star v3 — Voice & Gesture</title>
<link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@300;400;500;700;800;900&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<!-- MediaPipe Hands for gesture detection -->
<script src="https://cdn.jsdelivr.net/npm/@mediapipe/hands/hands.js" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/@mediapipe/camera_utils/camera_utils.js" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/@mediapipe/drawing_utils/drawing_utils.js" crossorigin="anonymous"></script>
<style>
:root {
  --bg:#00050a; --bg2:#030d1a; --panel:rgba(10,30,60,0.65);
  --gold:#ffd700; --gold2:#ffb300; --gold3:rgba(255,215,0,0.1);
  --cyan:#4facfe; --cyan2:#00d4ff; --green:#00e676;
  --red:#ff4d4d; --purple:#b388ff;
  --border:rgba(255,215,0,0.18); --border2:rgba(79,172,254,0.22);
  --text:#e8f4ff; --text2:#8ab4d4; --text3:#3a5a7a;
  --font:'Tajawal',sans-serif; --mono:'JetBrains Mono',monospace;
  --r:14px; --r2:20px;
}
*,*::before,*::after{margin:0;padding:0;box-sizing:border-box;}
html{scroll-behavior:smooth;}
body{font-family:var(--font);background:var(--bg);color:var(--text);min-height:100vh;overflow-x:hidden;}

/* BG */
.bg-fx{position:fixed;inset:0;pointer-events:none;z-index:0;
  background:
    radial-gradient(ellipse 55% 40% at 15% 25%,rgba(79,172,254,0.06) 0%,transparent 60%),
    radial-gradient(ellipse 45% 55% at 85% 75%,rgba(255,215,0,0.05) 0%,transparent 60%);
}
.scan{position:fixed;top:0;left:0;right:0;height:2px;
  background:linear-gradient(90deg,transparent,var(--gold),transparent);
  z-index:200;opacity:0.35;animation:scan 7s linear infinite;}
@keyframes scan{from{top:0;opacity:.5}to{top:100vh;opacity:0}}

/* LAYOUT */
.app{position:relative;z-index:1;display:flex;min-height:100vh;}

/* SIDEBAR */
.sidebar{width:270px;flex-shrink:0;background:var(--bg2);border-left:1px solid var(--border);
  display:flex;flex-direction:column;position:sticky;top:0;height:100vh;overflow-y:auto;}
.sidebar::-webkit-scrollbar{width:3px;}
.sidebar::-webkit-scrollbar-thumb{background:var(--gold3);}

.s-logo{padding:22px 18px 16px;border-bottom:1px solid var(--border);text-align:center;}
.star-anim{font-size:52px;display:block;line-height:1;
  filter:drop-shadow(0 0 14px gold) drop-shadow(0 0 28px #ffb300);
  animation:starSpin 4s ease-in-out infinite;}
@keyframes starSpin{0%,100%{transform:scale(1) rotate(0deg)}50%{transform:scale(1.07) rotate(6deg)}}
.brand{font-size:17px;font-weight:900;letter-spacing:.8px;margin-top:7px;
  background:linear-gradient(135deg,var(--gold),var(--cyan));
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;}
.brand-sub{font-size:10px;color:var(--text3);font-family:var(--mono);margin-top:2px;}

.live-clk{margin:12px 18px;padding:9px 12px;background:rgba(0,0,0,.3);
  border:1px solid var(--border2);border-radius:10px;
  font-family:var(--mono);font-size:11px;color:var(--cyan);text-align:center;letter-spacing:1px;}
.ldot{width:5px;height:5px;background:var(--green);border-radius:50%;
  display:inline-block;margin-left:5px;animation:blink 1s infinite;}
@keyframes blink{0%,100%{opacity:1}50%{opacity:.2}}

/* Lang tabs */
.lang-tabs{display:flex;gap:4px;padding:0 18px 10px;}
.ltab{flex:1;padding:7px 4px;background:transparent;border:1px solid var(--border);
  border-radius:8px;color:var(--text2);font-family:var(--font);font-size:12px;
  cursor:pointer;transition:all .2s;text-align:center;}
.ltab.active{background:rgba(255,215,0,.1);border-color:var(--gold);color:var(--gold);}

/* Nav */
.nav-sec{padding:6px 14px;}
.nlabel{font-size:10px;font-weight:700;letter-spacing:1.2px;color:var(--text3);
  text-transform:uppercase;padding:5px 4px;}
.nitem{display:flex;align-items:center;gap:10px;padding:9px 12px;border-radius:10px;
  font-size:13px;color:var(--text2);cursor:pointer;transition:all .2s;margin-bottom:2px;
  border:1px solid transparent;}
.nitem:hover{background:rgba(255,215,0,.05);color:var(--gold);border-color:var(--border);}
.nitem.active{background:rgba(255,215,0,.08);color:var(--gold);border-color:var(--border);}
.nicon{font-size:16px;width:20px;text-align:center;}

.sos-btn{margin:10px 18px;padding:11px;width:calc(100% - 36px);
  background:linear-gradient(135deg,#7f0000,#cc0000);
  border:1px solid var(--red);border-radius:12px;color:#fff;
  font-family:var(--font);font-size:13px;font-weight:700;cursor:pointer;
  animation:sosPulse 3s ease-in-out infinite;transition:all .2s;}
.sos-btn:hover{transform:scale(1.02);box-shadow:0 0 20px rgba(255,0,0,.4);}
@keyframes sosPulse{0%,100%{box-shadow:0 0 8px rgba(255,0,0,.3)}50%{box-shadow:0 0 20px rgba(255,0,0,.6)}}

.acc-sec{padding:8px 18px;}
.abadge{padding:7px 12px;border-radius:10px;font-size:12px;font-weight:700;
  text-align:center;cursor:pointer;transition:all .2s;margin-bottom:5px;}
.ab-std{background:rgba(79,172,254,.1);border:1px solid rgba(79,172,254,.3);color:var(--cyan);}
.ab-mst{background:rgba(255,215,0,.1);border:1px solid var(--border);color:var(--gold);}
.abadge.active{opacity:1;transform:scale(1.02);}
.abadge:not(.active){opacity:.35;}

.mem-log{padding:8px 18px;flex:1;overflow:hidden;}
.log-scroll{max-height:140px;overflow-y:auto;}
.log-scroll::-webkit-scrollbar{width:2px;}
.log-entry{font-family:var(--mono);font-size:10px;color:var(--cyan2);
  padding:2px 0;border-bottom:1px solid rgba(79,172,254,.07);animation:logIn .3s ease;}
@keyframes logIn{from{opacity:0;transform:translateX(-8px)}to{opacity:1;transform:none}}
.log-empty{font-size:11px;color:var(--text3);text-align:center;padding:10px;}

/* MAIN */
.main{flex:1;display:flex;flex-direction:column;overflow:hidden;min-height:100vh;}
.mheader{padding:18px 26px;border-bottom:1px solid var(--border);
  background:rgba(0,5,10,.8);backdrop-filter:blur(20px);
  display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:10px;}
.page-title{font-size:21px;font-weight:800;}
.page-title span{background:linear-gradient(90deg,var(--gold),var(--cyan));
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;}

.tabs{display:flex;gap:5px;flex-wrap:wrap;}
.tab-btn{padding:6px 14px;background:transparent;border:1px solid transparent;
  border-radius:8px;color:var(--text2);font-family:var(--font);font-size:12px;cursor:pointer;transition:all .2s;}
.tab-btn.active{background:rgba(255,215,0,.1);border-color:var(--border);color:var(--gold);}
.tab-btn:hover:not(.active){color:var(--text);border-color:var(--border2);}

.status-row{display:flex;gap:8px;padding:9px 26px;background:rgba(0,5,10,.5);
  border-bottom:1px solid var(--border);flex-wrap:wrap;}
.chip{display:flex;align-items:center;gap:5px;padding:3px 10px;border-radius:20px;font-size:11px;}
.chip-g{background:rgba(0,230,118,.1);border:1px solid rgba(0,230,118,.25);color:var(--green);}
.chip-o{background:rgba(255,215,0,.1);border:1px solid var(--border);color:var(--gold);}
.chip-c{background:rgba(79,172,254,.1);border:1px solid var(--border2);color:var(--cyan);}
.chip-r{background:rgba(255,77,77,.1);border:1px solid rgba(255,77,77,.25);color:var(--red);}
.cdot{width:5px;height:5px;border-radius:50%;animation:blink 1.5s infinite;}
.chip-g .cdot{background:var(--green);}
.chip-o .cdot{background:var(--gold);}
.chip-c .cdot{background:var(--cyan);}
.chip-r .cdot{background:var(--red);}

.content{flex:1;overflow-y:auto;}
.content::-webkit-scrollbar{width:4px;}
.content::-webkit-scrollbar-thumb{background:var(--border);border-radius:2px;}

/* VIEWS */
.view{display:none;padding:22px 26px;}
.view.active{display:block;}

/* GLASS CARD */
.glass{background:var(--panel);border:1px solid var(--border);border-radius:var(--r2);
  backdrop-filter:blur(16px);padding:20px;margin-bottom:16px;transition:border-color .2s;}
.glass:hover{border-color:rgba(255,215,0,.28);}
.gtitle{font-size:12px;font-weight:700;letter-spacing:.8px;color:var(--gold);
  text-transform:uppercase;margin-bottom:14px;display:flex;align-items:center;gap:7px;}

/* ===== VOICE COMMAND PANEL ===== */
.voice-panel{text-align:center;padding:10px 0;}
.voice-ring{width:140px;height:140px;border-radius:50%;margin:0 auto 20px;
  background:rgba(255,215,0,.04);border:2px solid var(--border);
  display:flex;align-items:center;justify-content:center;position:relative;cursor:pointer;
  transition:all .3s;}
.voice-ring.listening{border-color:var(--red);background:rgba(255,77,77,.08);
  box-shadow:0 0 0 0 rgba(255,77,77,.4);animation:voicePulse 1.2s ease-in-out infinite;}
.voice-ring.success{border-color:var(--green);background:rgba(0,230,118,.08);}
@keyframes voicePulse{
  0%{box-shadow:0 0 0 0 rgba(255,77,77,.5)}
  70%{box-shadow:0 0 0 24px rgba(255,77,77,0)}
  100%{box-shadow:0 0 0 0 rgba(255,77,77,0)}}
.mic-icon{font-size:52px;transition:all .3s;}
.voice-ring.listening .mic-icon{animation:micBounce .6s ease-in-out infinite alternate;}
@keyframes micBounce{from{transform:scale(1)}to{transform:scale(1.12)}}

.voice-status{font-size:14px;color:var(--text2);margin-bottom:6px;min-height:22px;}
.voice-transcript{font-size:13px;color:var(--cyan);font-family:var(--mono);
  min-height:18px;margin-bottom:14px;}
.voice-result-box{padding:14px 18px;background:rgba(0,0,0,.3);border:1px solid var(--border);
  border-radius:var(--r);margin-bottom:14px;text-align:right;min-height:52px;
  font-size:13px;line-height:1.7;display:none;}
.voice-result-box.show{display:block;}

/* Voice trigger buttons */
.vtrig-row{display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin-bottom:16px;}
.vtrig{padding:8px 18px;background:transparent;border:1px solid var(--border);
  border-radius:20px;color:var(--text2);font-family:var(--font);font-size:12px;
  cursor:pointer;transition:all .2s;}
.vtrig:hover,.vtrig.active{background:rgba(255,215,0,.1);border-color:var(--gold);color:var(--gold);}

/* Mic start button */
.mic-start{padding:13px 36px;font-size:15px;font-weight:700;
  background:linear-gradient(135deg,#3a0000,#990000);
  border:2px solid var(--red);border-radius:14px;
  color:#fff;font-family:var(--font);cursor:pointer;transition:all .3s;
  box-shadow:0 0 16px rgba(255,77,77,.3);margin:0 6px 8px;}
.mic-start:hover{transform:scale(1.04);box-shadow:0 0 30px rgba(255,77,77,.5);}
.mic-start.on{background:linear-gradient(135deg,#004000,#008000);
  border-color:var(--green);box-shadow:0 0 20px rgba(0,230,118,.4);animation:voicePulse2 1.5s infinite;}
@keyframes voicePulse2{
  0%{box-shadow:0 0 0 0 rgba(0,230,118,.5)}
  70%{box-shadow:0 0 0 18px rgba(0,230,118,0)}
  100%{box-shadow:0 0 0 0 rgba(0,230,118,0)}}

/* Keywords display */
.keywords-grid{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;margin-top:14px;}
.kw-card{padding:12px;background:rgba(0,0,0,.25);border:1px solid var(--border);
  border-radius:var(--r);text-align:center;}
.kw-lang{font-size:10px;color:var(--text3);margin-bottom:7px;text-transform:uppercase;letter-spacing:.8px;}
.kw-word{font-family:var(--mono);font-size:12px;color:var(--gold);margin-bottom:3px;}

/* ===== GESTURE PANEL ===== */
.gesture-area{display:grid;grid-template-columns:1fr 1fr;gap:16px;}
.cam-wrap{position:relative;border-radius:var(--r);overflow:hidden;
  border:2px solid var(--border);background:#000;min-height:240px;
  display:flex;align-items:center;justify-content:center;}
.cam-wrap.active-gesture{border-color:var(--gold);box-shadow:0 0 20px rgba(255,215,0,.2);}
.cam-wrap.gesture-buy{border-color:var(--green);box-shadow:0 0 24px rgba(0,230,118,.3);}
#gestureVideo{width:100%;display:block;transform:scaleX(-1);}
#gestureCanvas{position:absolute;top:0;left:0;width:100%;height:100%;transform:scaleX(-1);}
.cam-placeholder{text-align:center;color:var(--text3);padding:20px;}
.cam-placeholder .cp-icon{font-size:40px;margin-bottom:10px;display:block;}

.gesture-info{display:flex;flex-direction:column;gap:10px;}
.gest-detected{padding:16px;background:rgba(0,0,0,.3);border:1px solid var(--border);
  border-radius:var(--r);text-align:center;}
.gest-icon{font-size:48px;margin-bottom:8px;display:block;transition:all .3s;}
.gest-name{font-size:14px;font-weight:700;color:var(--gold);}
.gest-action{font-size:11px;color:var(--text2);margin-top:4px;}

.gesture-list{padding:12px 14px;background:rgba(0,0,0,.25);border:1px solid var(--border);
  border-radius:var(--r);}
.gl-title{font-size:10px;color:var(--text3);text-transform:uppercase;letter-spacing:.8px;margin-bottom:9px;}
.gl-item{display:flex;align-items:center;gap:10px;padding:5px 0;
  border-bottom:1px solid rgba(255,255,255,.04);font-size:12px;}
.gl-item:last-child{border-bottom:none;}
.gl-gest{font-size:18px;width:26px;text-align:center;}
.gl-desc{flex:1;color:var(--text2);}
.gl-cmd{font-family:var(--mono);font-size:11px;color:var(--gold);}

.gest-start-btn{padding:10px;width:100%;
  background:linear-gradient(135deg,rgba(255,215,0,.15),rgba(255,215,0,.05));
  border:1px solid var(--gold);border-radius:var(--r);
  color:var(--gold);font-family:var(--font);font-size:13px;font-weight:700;cursor:pointer;transition:all .2s;}
.gest-start-btn:hover{background:rgba(255,215,0,.2);box-shadow:0 0 14px rgba(255,215,0,.25);}
.gest-start-btn.active{background:rgba(0,230,118,.1);border-color:var(--green);color:var(--green);animation:voicePulse2 2s infinite;}

/* ===== DEAL EXECUTION ===== */
.deal-center{text-align:center;padding:10px 0;}
.deal-price{font-size:52px;font-weight:900;font-family:var(--mono);
  background:linear-gradient(135deg,var(--gold),#fff);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;}
.deal-metrics{display:flex;justify-content:center;gap:24px;margin:14px 0;flex-wrap:wrap;}
.dm{text-align:center;}
.dm-val{font-size:20px;font-weight:700;font-family:var(--mono);}
.dm-lbl{font-size:10px;color:var(--text3);margin-top:2px;}

/* Mode selector */
.mode-row{display:flex;gap:8px;justify-content:center;margin-bottom:16px;flex-wrap:wrap;}
.mode-btn{padding:9px 20px;background:transparent;border:1px solid var(--border);
  border-radius:20px;color:var(--text2);font-family:var(--font);font-size:12px;cursor:pointer;transition:all .2s;}
.mode-btn.active{background:rgba(255,215,0,.1);border-color:var(--gold);color:var(--gold);font-weight:700;}
.mode-btn:hover:not(.active){border-color:var(--border2);color:var(--text);}

/* Live mode panels inside deal */
.mode-panel{display:none;margin-bottom:16px;}
.mode-panel.show{display:block;}

/* mini mic */
.mini-mic{width:64px;height:64px;border-radius:50%;margin:0 auto 10px;
  background:rgba(255,77,77,.1);border:2px solid var(--red);
  display:flex;align-items:center;justify-content:center;font-size:28px;cursor:pointer;transition:all .3s;}
.mini-mic.on{animation:voicePulse 1.2s infinite;border-color:var(--red);background:rgba(255,77,77,.18);}
.mini-mic.done{border-color:var(--green);background:rgba(0,230,118,.12);animation:none;}

.deal-btn{padding:17px 48px;font-size:17px;font-weight:800;
  background:linear-gradient(135deg,#4a2800,#996600,var(--gold));
  border:2px solid var(--gold);border-radius:16px;color:#000;font-family:var(--font);
  cursor:pointer;transition:all .3s;box-shadow:0 0 20px rgba(255,215,0,.4);letter-spacing:.4px;}
.deal-btn:hover{transform:scale(1.05);box-shadow:0 0 40px rgba(255,215,0,.7);}
.deal-btn:disabled{opacity:.45;cursor:not-allowed;transform:none;}

.prog-wrap{margin:12px 0;}
.prog-track{height:5px;background:rgba(255,255,255,.07);border-radius:3px;overflow:hidden;}
.prog-fill{height:100%;border-radius:3px;transition:width .4s ease;}
.prog-lbl{font-family:var(--mono);font-size:10px;color:var(--text3);margin-top:3px;text-align:center;}

.success-card{margin-top:18px;padding:22px;background:rgba(0,230,118,.05);
  border:1px solid rgba(0,230,118,.22);border-radius:var(--r2);text-align:center;
  animation:boom .5s ease;}
@keyframes boom{from{opacity:0;transform:scale(.88)}to{opacity:1;transform:scale(1)}}
.success-card h2{font-size:22px;color:var(--green);margin-bottom:8px;}
.cert-code{font-family:var(--mono);font-size:12px;color:var(--cyan);padding:8px 12px;
  background:rgba(0,0,0,.3);border-radius:8px;margin:8px 0;}

/* CIRCLE */
.circ-hdr{display:flex;align-items:center;gap:12px;margin-bottom:18px;}
.circ-logo{width:46px;height:46px;border-radius:50%;
  background:linear-gradient(135deg,#00c4ff,#0070ff);
  display:flex;align-items:center;justify-content:center;font-size:20px;
  border:2px solid rgba(0,196,255,.4);box-shadow:0 0 16px rgba(0,196,255,.3);}
.wallet-row{display:flex;gap:12px;margin-bottom:16px;flex-wrap:wrap;}
.wallet-card{flex:1;min-width:140px;padding:14px 16px;background:rgba(0,0,0,.3);
  border:1px solid var(--border2);border-radius:var(--r);transition:all .2s;}
.wallet-card:hover{border-color:var(--cyan);}
.wlbl{font-size:10px;color:var(--text3);text-transform:uppercase;letter-spacing:.7px;}
.wval{font-size:18px;font-weight:700;font-family:var(--mono);margin-top:3px;}
.waddr{font-size:10px;font-family:var(--mono);color:var(--cyan2);margin-top:3px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}

.pay-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:14px;}
.field-wrap{display:flex;flex-direction:column;gap:4px;}
.flabel{font-size:11px;color:var(--text3);}
.finput{padding:9px 13px;background:rgba(0,0,0,.4);border:1px solid var(--border);
  border-radius:var(--r);color:var(--text);font-family:var(--mono);font-size:13px;
  outline:none;transition:border-color .2s;}
.finput:focus{border-color:var(--cyan);}
.fsel{cursor:pointer;}
.fsel option{background:#071628;}
.pay-btn{width:100%;padding:14px;background:linear-gradient(135deg,#003399,#0070ff);
  border:1px solid rgba(0,196,255,.4);border-radius:var(--r);color:#fff;
  font-family:var(--font);font-size:14px;font-weight:700;cursor:pointer;transition:all .2s;
  box-shadow:0 0 16px rgba(0,112,255,.3);}
.pay-btn:hover{transform:translateY(-2px);box-shadow:0 8px 24px rgba(0,112,255,.4);}
.pay-btn:disabled{opacity:.4;cursor:not-allowed;transform:none;}

.tx-item{display:flex;align-items:center;gap:10px;padding:9px 12px;
  background:rgba(0,0,0,.2);border:1px solid var(--border);border-radius:var(--r);margin-bottom:5px;
  animation:txIn .3s ease;}
@keyframes txIn{from{opacity:0;transform:translateY(-4px)}to{opacity:1;transform:none}}
.tx-id{font-family:var(--mono);font-size:10px;color:var(--cyan2);}
.tx-desc{font-size:11px;color:var(--text2);margin-top:1px;}
.tx-amt{font-family:var(--mono);font-size:12px;font-weight:600;}
.s-confirmed{background:rgba(0,230,118,.1);color:var(--green);border:1px solid rgba(0,230,118,.2);
  font-size:10px;padding:2px 7px;border-radius:20px;}
.s-pending{background:rgba(255,215,0,.1);color:var(--gold);border:1px solid var(--border);
  font-size:10px;padding:2px 7px;border-radius:20px;}

/* CONFIG */
.cfg-box{padding:14px 16px;background:rgba(255,215,0,.04);
  border:1px solid rgba(255,215,0,.14);border-radius:var(--r);margin-bottom:12px;}
.cfg-box label{font-size:11px;color:var(--text3);display:block;margin-bottom:4px;}
.cfg-inp{width:100%;padding:8px 13px;background:rgba(0,0,0,.5);
  border:1px solid var(--border);border-radius:8px;color:var(--cyan);
  font-family:var(--mono);font-size:12px;outline:none;letter-spacing:1px;margin-bottom:6px;}
.cfg-inp:focus{border-color:var(--gold);}
.cfg-save{padding:6px 16px;background:rgba(255,215,0,.1);border:1px solid var(--gold);
  border-radius:8px;color:var(--gold);font-family:var(--font);font-size:12px;cursor:pointer;}
.cfg-save:hover{background:rgba(255,215,0,.2);}
.cfg-note{font-size:10px;color:var(--text3);margin-top:2px;}

/* SMART HOME */
.dev-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;}
.dev-card{padding:18px 14px;text-align:center;background:rgba(0,0,0,.3);
  border:1px solid var(--border);border-radius:var(--r2);cursor:pointer;transition:all .25s;}
.dev-card:hover{transform:translateY(-3px);border-color:var(--border2);}
.dev-card.on{border-color:var(--green);background:rgba(0,230,118,.05);}
.dev-card.off{border-color:rgba(255,77,77,.3);}
.d-ico{font-size:34px;margin-bottom:8px;transition:transform .2s;}
.dev-card:hover .d-ico{transform:scale(1.1);}
.d-nm{font-size:12px;font-weight:600;}
.d-st{font-size:11px;margin-top:3px;font-family:var(--mono);}
.d-st.on{color:var(--green);}
.d-st.off{color:var(--red);}
.tog{margin-top:10px;width:44px;height:22px;background:var(--text3);
  border-radius:11px;border:none;cursor:pointer;position:relative;transition:background .3s;}
.tog.on{background:var(--green);}
.tog::after{content:'';position:absolute;top:3px;left:3px;width:16px;height:16px;
  border-radius:50%;background:#fff;transition:transform .3s;}
.tog.on::after{transform:translateX(22px);}

/* SOS MODAL */
.sos-modal{position:fixed;inset:0;background:rgba(0,0,0,.88);
  display:flex;align-items:center;justify-content:center;
  z-index:9999;backdrop-filter:blur(10px);animation:fadeIn .3s ease;}
.sos-modal.hidden{display:none;}
@keyframes fadeIn{from{opacity:0}to{opacity:1}}
.sos-card{padding:38px;border-radius:24px;text-align:center;
  background:rgba(18,0,0,.96);border:2px solid var(--red);
  box-shadow:0 0 60px rgba(255,0,0,.4);max-width:380px;width:90%;
  animation:shake .5s ease;}
@keyframes shake{0%{transform:none}20%{transform:translateX(-8px)}40%{transform:translateX(8px)}60%{transform:translateX(-5px)}80%{transform:translateX(5px)}100%{transform:none}}
.sos-emoji{font-size:60px;display:block;animation:sosSpin .5s ease;}
@keyframes sosSpin{from{transform:rotate(-20deg)scale(0)}to{transform:none}}
.sos-card h2{color:var(--red);font-size:22px;margin:14px 0 8px;}
.sos-dismiss{padding:9px 22px;background:rgba(255,77,77,.1);border:1px solid var(--red);
  border-radius:10px;color:var(--red);font-family:var(--font);font-size:13px;cursor:pointer;}

/* TOASTS */
.toast-area{position:fixed;bottom:22px;left:22px;z-index:8888;display:flex;flex-direction:column;gap:7px;}
.toast{padding:9px 15px;border-radius:10px;font-size:13px;min-width:200px;
  animation:toIn .3s ease,toOut .3s ease 2.7s forwards;backdrop-filter:blur(12px);}
@keyframes toIn{from{opacity:0;transform:translateX(-16px)}to{opacity:1;transform:none}}
@keyframes toOut{from{opacity:1}to{opacity:0;transform:translateX(-16px)}}
.toast-s{background:rgba(0,230,118,.15);border:1px solid rgba(0,230,118,.3);color:var(--green);}
.toast-i{background:rgba(79,172,254,.15);border:1px solid var(--border2);color:var(--cyan);}
.toast-w{background:rgba(255,215,0,.12);border:1px solid var(--border);color:var(--gold);}
.toast-e{background:rgba(255,77,77,.12);border:1px solid rgba(255,77,77,.3);color:var(--red);}

/* RESPONSIVE */
@media(max-width:900px){
  .sidebar{display:none;}
  .gesture-area{grid-template-columns:1fr;}
  .dev-grid{grid-template-columns:repeat(2,1fr);}
  .pay-grid{grid-template-columns:1fr;}
  .keywords-grid{grid-template-columns:1fr 1fr;}
}
@media(max-width:600px){
  .main{} .mheader{padding:13px 15px;} .view{padding:15px;}
  .wallet-row{flex-direction:column;} .keywords-grid{grid-template-columns:1fr;}
}
</style>
</head>
<body>

<div class="bg-fx"></div>
<div class="scan"></div>

<!-- SOS MODAL -->
<div class="sos-modal hidden" id="sosModal">
  <div class="sos-card">
    <span class="sos-emoji">🚨</span>
    <h2 id="sosTitle">Emergency Protocol / بروتوكول الطوارئ</h2>
    <p id="sosTxt" style="color:var(--text2);font-size:13px;margin-bottom:16px">جاري تنبيه Master Alpha Hub...</p>
    <div class="prog-wrap"><div class="prog-track"><div class="prog-fill" id="sosBar" style="width:0%;background:var(--red)"></div></div></div>
    <p id="sosSt" style="font-family:var(--mono);font-size:11px;color:var(--red);margin-top:8px;margin-bottom:16px">جاري التحقق من الأمان...</p>
    <button class="sos-dismiss" onclick="closeSOS()">إغلاق / Close</button>
  </div>
</div>

<div class="toast-area" id="toastArea"></div>

<div class="app">
<!-- SIDEBAR -->
<aside class="sidebar">
  <div class="s-logo">
    <span class="star-anim">★</span>
    <div class="brand">My FlashDeal Star</div>
    <div class="brand-sub">Voice · Gesture · Sovereign v3</div>
  </div>
  <div class="live-clk"><span class="ldot"></span><span id="clkTxt">--:--:--</span></div>

  <!-- Lang -->
  <div class="lang-tabs" style="padding:0 18px 10px">
    <button class="ltab active" onclick="setLang('ar',this)">🇸🇦 AR</button>
    <button class="ltab" onclick="setLang('en',this)">🇬🇧 EN</button>
    <button class="ltab" onclick="setLang('it',this)">🇮🇹 IT</button>
  </div>

  <div class="nav-sec">
    <div class="nlabel" id="nl-menu">القائمة</div>
    <div class="nitem active" onclick="nav('voice',this)"><span class="nicon">🎙️</span><span id="n-voice">الأمر الصوتي</span></div>
    <div class="nitem" onclick="nav('gesture',this)"><span class="nicon">👋</span><span id="n-gesture">إشارة اليد</span></div>
    <div class="nitem" onclick="nav('deal',this)"><span class="nicon">🚀</span><span id="n-deal">تنفيذ الصفقة</span></div>
    <div class="nitem" onclick="nav('circle',this)"><span class="nicon">💳</span><span id="n-circle">Circle — الدفع</span></div>
    <div class="nitem" onclick="nav('home',this)"><span class="nicon">🏠</span><span id="n-home">المنزل الذكي</span></div>
    <div class="nitem" onclick="nav('config',this)"><span class="nicon">⚙️</span><span id="n-config">إعدادات API</span></div>
  </div>

  <div class="acc-sec">
    <div class="nlabel">مستوى الوصول</div>
    <div class="abadge ab-std active" id="b-std" onclick="setAccess('standard')">🔵 Standard</div>
    <div class="abadge ab-mst" id="b-mst" onclick="setAccess('master')">🌟 Master Alpha</div>
  </div>

  <button class="sos-btn" onclick="triggerSOS()" id="sosBtnTxt">🔔 SOS — الطوارئ</button>

  <div class="mem-log">
    <div class="nlabel" id="nl-log">📜 سجل الذاكرة</div>
    <div class="log-scroll" id="memLog"><div class="log-empty" id="logEmpty">لا توجد سجلات</div></div>
  </div>
</aside>

<!-- MAIN -->
<div class="main">
  <header class="mheader">
    <div class="page-title">🌟 <span>FlashDeal</span> Star</div>
    <div class="tabs">
      <button class="tab-btn active" onclick="nav('voice',null);setTab(this)">🎙️</button>
      <button class="tab-btn" onclick="nav('gesture',null);setTab(this)">👋</button>
      <button class="tab-btn" onclick="nav('deal',null);setTab(this)">🚀</button>
      <button class="tab-btn" onclick="nav('circle',null);setTab(this)">💳</button>
      <button class="tab-btn" onclick="nav('home',null);setTab(this)">🏠</button>
      <button class="tab-btn" onclick="nav('config',null);setTab(this)">⚙️</button>
    </div>
  </header>

  <div class="status-row">
    <div class="chip chip-g"><div class="cdot"></div><span id="st-on">متصل</span></div>
    <div class="chip chip-o"><div class="cdot"></div><span id="st-acc">Standard</span></div>
    <div class="chip chip-c"><div class="cdot"></div><span id="st-erc">ERC-8004</span></div>
    <div class="chip chip-g"><div class="cdot"></div><span id="st-voice-chip">الصوت: جاهز</span></div>
    <div class="chip chip-r" id="gestChip" style="display:none"><div class="cdot"></div><span id="st-gest">إشارة: نشط</span></div>
  </div>

  <div class="content">

  <!-- ===== VOICE VIEW ===== -->
  <div id="view-voice" class="view active">
    <div class="glass">
      <div class="gtitle">🎙️ <span id="vt-title">الأمر الصوتي الحقيقي — 3 لغات</span></div>

      <div class="voice-panel">
        <div class="voice-ring" id="voiceRing" onclick="toggleMic()">
          <span class="mic-icon" id="micIcon">🎙️</span>
        </div>
        <div class="voice-status" id="voiceStatus">اضغط على الميكروفون للبدء</div>
        <div class="voice-transcript" id="voiceTranscript"></div>

        <div class="vtrig-row">
          <button class="vtrig active" id="vt-ar" onclick="setVoiceLang('ar-SA',this)">🇸🇦 عربي</button>
          <button class="vtrig" id="vt-en" onclick="setVoiceLang('en-US',this)">🇬🇧 English</button>
          <button class="vtrig" id="vt-it" onclick="setVoiceLang('it-IT',this)">🇮🇹 Italiano</button>
        </div>

        <div style="margin-bottom:12px">
          <button class="mic-start" id="mainMicBtn" onclick="toggleMic()">🎙️ <span id="micBtnTxt">ابدأ الاستماع</span></button>
        </div>

        <div class="voice-result-box" id="voiceResultBox">
          <div id="voiceResultText"></div>
        </div>
      </div>

      <div class="gtitle" style="margin-top:4px">📋 <span id="vt-kw">الكلمات المفتاحية للشراء والدفع</span></div>
      <div class="keywords-grid">
        <div class="kw-card">
          <div class="kw-lang">🇸🇦 العربية</div>
          <div class="kw-word">ابرم الصفقة</div>
          <div class="kw-word">اشتر الآن</div>
          <div class="kw-word">نفّذ الدفع</div>
          <div class="kw-word">أكّد الشراء</div>
          <div class="kw-word" style="color:var(--cyan)">ادفع</div>
        </div>
        <div class="kw-card">
          <div class="kw-lang">🇬🇧 English</div>
          <div class="kw-word">execute deal</div>
          <div class="kw-word">buy now</div>
          <div class="kw-word">confirm purchase</div>
          <div class="kw-word">make payment</div>
          <div class="kw-word" style="color:var(--cyan)">pay</div>
        </div>
        <div class="kw-card">
          <div class="kw-lang">🇮🇹 Italiano</div>
          <div class="kw-word">concludi accordo</div>
          <div class="kw-word">acquista ora</div>
          <div class="kw-word">conferma acquisto</div>
          <div class="kw-word">esegui pagamento</div>
          <div class="kw-word" style="color:var(--cyan)">paga</div>
        </div>
      </div>

      <div id="voiceActionResult" style="display:none;margin-top:14px"></div>
    </div>
  </div>

  <!-- ===== GESTURE VIEW ===== -->
  <div id="view-gesture" class="view">
    <div class="glass">
      <div class="gtitle">👋 <span id="gt-title">إشارة اليد — أمر الشراء</span></div>
      <div class="gesture-area">
        <div>
          <div class="cam-wrap" id="gestCamWrap">
            <div class="cam-placeholder" id="gestPlaceholder">
              <span class="cp-icon">👋</span>
              <div style="font-size:12px;color:var(--text3)">اضغط "تفعيل الكاميرا"<br>لبدء التعرف على الإشارات</div>
            </div>
            <video id="gestureVideo" autoplay playsinline style="display:none;width:100%"></video>
            <canvas id="gestureCanvas" style="display:none;position:absolute;top:0;left:0;width:100%;height:100%"></canvas>
          </div>
          <button class="gest-start-btn" id="gestBtn" onclick="toggleGesture()" style="margin-top:10px">
            📷 <span id="gestBtnTxt">تفعيل كاميرا الإشارة</span>
          </button>
        </div>

        <div class="gesture-info">
          <div class="gest-detected">
            <span class="gest-icon" id="gestIcon">🤚</span>
            <div class="gest-name" id="gestName">في انتظار الإشارة...</div>
            <div class="gest-action" id="gestAction">وجّه يدك أمام الكاميرا</div>
          </div>

          <div class="gesture-list">
            <div class="gl-title">الإشارات المدعومة / Supported Gestures</div>
            <div class="gl-item">
              <span class="gl-gest">✋</span>
              <span class="gl-desc">كف مفتوح / Open Palm</span>
              <span class="gl-cmd">→ شراء</span>
            </div>
            <div class="gl-item">
              <span class="gl-gest">👍</span>
              <span class="gl-desc">إبهام للأعلى / Thumbs Up</span>
              <span class="gl-cmd">→ تأكيد</span>
            </div>
            <div class="gl-item">
              <span class="gl-gest">✌️</span>
              <span class="gl-desc">علامة النصر / Victory</span>
              <span class="gl-cmd">→ دفع</span>
            </div>
            <div class="gl-item">
              <span class="gl-gest">👊</span>
              <span class="gl-desc">قبضة / Fist</span>
              <span class="gl-cmd">→ إلغاء</span>
            </div>
            <div class="gl-item">
              <span class="gl-gest">🤙</span>
              <span class="gl-desc">اتصل بي / Call Me</span>
              <span class="gl-cmd">→ SOS</span>
            </div>
          </div>

          <div id="gestureActionResult"></div>
        </div>
      </div>

      <div style="margin-top:14px;padding:12px 14px;background:rgba(255,215,0,.04);border:1px solid var(--border);border-radius:var(--r);font-size:12px;color:var(--text2);line-height:1.7">
        💡 <strong style="color:var(--text)">كيف يعمل؟</strong> يستخدم MediaPipe لتتبع نقاط اليد (21 نقطة) في الوقت الفعلي. احتجت إلى إذن الكاميرا. الكود يعمل محلياً ولا يُرسل صوراً لأي خادم.
      </div>
    </div>
  </div>

  <!-- ===== DEAL VIEW ===== -->
  <div id="view-deal" class="view">
    <div class="glass deal-center">
      <div class="gtitle" style="justify-content:center">🚀 <span id="dt-title">تنفيذ الصفقة — صوت أو إشارة أو نص</span></div>
      <div class="deal-price">$99.99</div>
      <div class="deal-metrics">
        <div class="dm"><div class="dm-val" style="color:var(--green)">100%</div><div class="dm-lbl" id="dm-stab">استقرار</div></div>
        <div class="dm"><div class="dm-val" style="color:var(--gold)">ERC-8004</div><div class="dm-lbl" id="dm-std">المعيار</div></div>
        <div class="dm"><div class="dm-val" style="color:var(--cyan)">✅</div><div class="dm-lbl" id="dm-vfy">موثّق</div></div>
      </div>

      <!-- Mode selector -->
      <div class="mode-row">
        <button class="mode-btn active" onclick="setDealMode('voice',this)">🎙️ <span id="dm-voice">صوتي</span></button>
        <button class="mode-btn" onclick="setDealMode('gesture',this)">👋 <span id="dm-gest">إشارة</span></button>
        <button class="mode-btn" onclick="setDealMode('text',this)">⌨️ <span id="dm-text">نص</span></button>
      </div>

      <!-- Voice mode panel -->
      <div class="mode-panel show" id="mp-voice" style="text-align:center">
        <div class="mini-mic" id="dealMic" onclick="toggleDealMic()">🎙️</div>
        <div id="dealVoiceStatus" style="font-size:12px;color:var(--text2);margin-bottom:8px">اضغط للاستماع</div>
        <div id="dealVoiceText" style="font-family:var(--mono);font-size:12px;color:var(--cyan);min-height:16px;margin-bottom:8px"></div>
        <div style="font-size:11px;color:var(--text3)">قل: "ابرم الصفقة" / "Execute Deal" / "Concludi"</div>
      </div>

      <!-- Gesture mode panel -->
      <div class="mode-panel" id="mp-gesture">
        <div style="text-align:center;padding:14px">
          <div style="font-size:40px;margin-bottom:8px" id="dealGestIcon">✋</div>
          <div style="font-size:13px;color:var(--text2);margin-bottom:10px" id="dealGestStatus">افتح كف يدك أمام الكاميرا لتنفيذ الصفقة</div>
          <button class="gest-start-btn" onclick="nav('gesture',null);setTab(document.querySelectorAll('.tab-btn')[1])" style="display:inline-block;width:auto;padding:8px 20px">
            👋 فتح لوحة الإشارات
          </button>
        </div>
      </div>

      <!-- Text mode panel -->
      <div class="mode-panel" id="mp-text">
        <input class="finput" id="dealTextInput" placeholder="اكتب: 'ابرم الصفقة' أو 'Buy Now' أو 'Acquista Ora'..." style="width:100%;margin-bottom:10px;text-align:right">
      </div>

      <div class="prog-wrap" id="dealProg" style="display:none">
        <div class="prog-track"><div class="prog-fill" id="dealBar" style="width:0%;background:linear-gradient(90deg,var(--gold),var(--gold2))"></div></div>
        <div class="prog-lbl" id="dealLabel">جاري التنفيذ...</div>
      </div>

      <button class="deal-btn" id="dealBtn" onclick="executeDeal()">
        🚀 <span id="deal-btn-txt">إبرام الصفقة العالمية</span>
      </button>

      <div id="dealSuccess" style="display:none"></div>
    </div>
  </div>

  <!-- ===== CIRCLE VIEW ===== -->
  <div id="view-circle" class="view">
    <div class="glass">
      <div class="circ-hdr">
        <div class="circ-logo">◎</div>
        <div>
          <div style="font-size:16px;font-weight:700;color:var(--cyan2)">Circle — Web3 Payments</div>
          <div style="font-size:11px;color:var(--text3);font-family:var(--mono)">Programmable Money Infrastructure</div>
        </div>
        <span style="margin-right:auto;font-size:11px;padding:3px 10px;border-radius:20px;background:rgba(0,230,118,.1);border:1px solid rgba(0,230,118,.25);color:var(--green);font-family:var(--mono)" id="netChip">arc-testnet</span>
      </div>

      <div class="wallet-row">
        <div class="wallet-card">
          <div class="wlbl">USDC Balance</div>
          <div class="wval" style="color:var(--cyan2)" id="usdcBal">1,250.00 USDC</div>
          <div class="waddr" id="wAddr1">0x4fac...8b2d</div>
        </div>
        <div class="wallet-card">
          <div class="wlbl">EVM Wallet</div>
          <div class="wval" style="color:var(--gold)" id="evmBal">0.48 ETH</div>
          <div class="waddr">arc-testnet · ERC-8004</div>
        </div>
        <div class="wallet-card">
          <div class="wlbl" id="wl-txc">المعاملات</div>
          <div class="wval" style="color:var(--green)" id="txCount">12</div>
          <div class="waddr" id="wl-month">هذا الشهر</div>
        </div>
      </div>

      <div class="cfg-box">
        <label>◎ Circle API Key</label>
        <input class="cfg-inp" type="password" id="circleKey" placeholder="xxxxxxxx:yyyyyyyy">
        <input class="cfg-inp" type="text" id="netInput" placeholder="arc-testnet" style="margin-top:5px">
        <button class="cfg-save" onclick="saveCircle()">✅ حفظ / Save</button>
        <div class="cfg-note">⚠️ console.circle.com — مفاتيح testnet آمنة للتطوير</div>
      </div>

      <div class="gtitle">💸 <span id="pt-title">إرسال دفعة</span></div>
      <div class="pay-grid">
        <div class="field-wrap"><div class="flabel">المبلغ / Amount (USDC)</div><input class="finput" type="number" id="payAmt" placeholder="99.99" min="0.01" step="0.01"></div>
        <div class="field-wrap"><div class="flabel">العملة / Currency</div>
          <select class="finput fsel" id="payCur"><option>USDC</option><option>EURC</option><option>ETH</option></select>
        </div>
        <div class="field-wrap" style="grid-column:1/-1"><div class="flabel">عنوان المستلم / Recipient Address</div><input class="finput" type="text" id="payDest" placeholder="0x..." style="font-family:var(--mono)"></div>
        <div class="field-wrap"><div class="flabel">الشبكة / Network</div>
          <select class="finput fsel" id="payNet"><option>arc-testnet</option><option>ethereum</option><option>polygon</option></select>
        </div>
        <div class="field-wrap"><div class="flabel">رسوم الغاز / Gas</div><input class="finput" type="text" value="~$0.12" readonly style="color:var(--text3)"></div>
      </div>
      <div class="prog-wrap" id="payProg" style="display:none">
        <div class="prog-track"><div class="prog-fill" id="payBar" style="width:0%;background:linear-gradient(90deg,#0070ff,#00c4ff)"></div></div>
        <div class="prog-lbl" id="payLbl">جاري المعالجة...</div>
      </div>
      <button class="pay-btn" id="payBtn" onclick="execPayment()">◎ <span id="pb-txt">تنفيذ الدفعة عبر Circle</span></button>

      <div class="gtitle" style="margin-top:18px">📋 <span id="tl-title">سجل المعاملات</span></div>
      <div id="txList">
        <div class="tx-item">
          <div style="font-size:18px;width:28px;text-align:center">✅</div>
          <div style="flex:1"><div class="tx-id">0x4facfe...2026</div><div class="tx-desc">USDC Transfer — arc-testnet</div></div>
          <div style="text-align:left"><div class="tx-amt" style="color:var(--green)">+250 USDC</div><span class="s-confirmed">confirmed</span></div>
        </div>
      </div>
    </div>
  </div>

  <!-- ===== HOME VIEW ===== -->
  <div id="view-home" class="view">
    <div class="glass">
      <div class="gtitle">🏠 <span id="ht-title">التحكم الذكي — المنزل والسيارة</span></div>
      <div class="dev-grid" id="devGrid"></div>
    </div>
  </div>

  <!-- ===== CONFIG VIEW ===== -->
  <div id="view-config" class="view">
    <div class="glass">
      <div class="gtitle">⚙️ إعدادات API</div>
      <div class="cfg-box">
        <label>🔑 Google Gemini API Key</label>
        <input class="cfg-inp" type="password" id="cfgGem" placeholder="AIzaSy...">
        <div class="cfg-note">aistudio.google.com — مجاني للاختبار</div>
      </div>
      <div class="cfg-box">
        <label>◎ Circle API Key</label>
        <input class="cfg-inp" type="password" id="cfgCirc" placeholder="xxxxxxxx:yyyyyyyy">
        <div class="cfg-note">console.circle.com</div>
      </div>
      <div class="cfg-box">
        <label>🌐 Network ID</label>
        <input class="cfg-inp" type="text" id="cfgNet" value="arc-testnet">
      </div>
      <button class="pay-btn" onclick="saveAllCfg()" style="background:linear-gradient(135deg,#1a3a00,#2a6000);border-color:rgba(0,230,118,.4)">✅ <span id="sv-cfg">حفظ الإعدادات</span></button>

      <div style="margin-top:18px;padding:14px;background:rgba(255,215,0,.04);border:1px solid var(--border);border-radius:var(--r);font-size:12px;color:var(--text2);line-height:1.9">
        <div style="color:var(--gold);font-weight:700;margin-bottom:8px">🔐 إرشادات الأمان</div>
        <div>• لا تضع مفاتيح API في كود مكشوف</div>
        <div>• استبدل أي مفتاح مكشوف فوراً</div>
        <div>• استخدم testnet للتطوير دائماً</div>
        <div>• الكود يحفظ المفاتيح في الجلسة فقط (Session)</div>
      </div>
    </div>
  </div>

  </div><!-- /content -->
</div><!-- /main -->
</div><!-- /app -->

<script>
// ================================================================
// STATE
// ================================================================
const APP = {
  lang: 'ar', uiLang: 'ar', access: 'standard',
  geminiKey: '', circleKey: '', network: 'arc-testnet',
  voiceLang: 'ar-SA', logs: [],
  recognition: null, isListening: false,
  dealMicActive: false, dealRecog: null,
  gestureActive: false, gestureStream: null,
  devices: [
    {id:'lights', icon:'💡', ar:'الإضاءة',    en:'Lights',    it:'Luci',    on:true},
    {id:'ac',     icon:'❄️', ar:'التكييف',    en:'AC Unit',   it:'Clima',   on:false},
    {id:'door',   icon:'🚪', ar:'الباب',      en:'Main Door', it:'Porta',   on:false},
    {id:'garage', icon:'🏚️', ar:'المرآب',    en:'Garage',    it:'Garage',  on:false},
    {id:'camera', icon:'📷', ar:'الكاميرات', en:'Cameras',   it:'Camere',  on:true},
    {id:'car',    icon:'🚗', ar:'السيارة',    en:'Car',       it:'Auto',    on:false},
  ]
};

// ================================================================
// TRANSLATIONS
// ================================================================
const T = {
  ar: {
    'n-voice':'الأمر الصوتي','n-gesture':'إشارة اليد','n-deal':'تنفيذ الصفقة',
    'n-circle':'Circle — الدفع','n-home':'المنزل الذكي','n-config':'إعدادات API',
    'nl-menu':'القائمة','nl-log':'📜 سجل الذاكرة',
    'vt-title':'الأمر الصوتي الحقيقي — 3 لغات','vt-kw':'الكلمات المفتاحية للشراء والدفع',
    'gt-title':'إشارة اليد — أمر الشراء','dt-title':'تنفيذ الصفقة — صوت أو إشارة أو نص',
    'pt-title':'إرسال دفعة','tl-title':'سجل المعاملات','ht-title':'التحكم الذكي — المنزل والسيارة',
    'dm-voice':'صوتي','dm-gest':'إشارة','dm-text':'نص',
    'dm-stab':'استقرار','dm-std':'المعيار','dm-vfy':'موثّق',
    'deal-btn-txt':'إبرام الصفقة العالمية','pb-txt':'تنفيذ الدفعة عبر Circle',
    'st-on':'متصل','st-acc':'Standard','st-erc':'ERC-8004','st-voice-chip':'الصوت: جاهز','st-gest':'إشارة: نشط',
    'wl-txc':'المعاملات','wl-month':'هذا الشهر','sosBtnTxt':'🔔 SOS — الطوارئ',
    'micBtnTxt':'ابدأ الاستماع','gestBtnTxt':'تفعيل كاميرا الإشارة','sv-cfg':'حفظ الإعدادات',
    'logEmpty':'لا توجد سجلات',
    buy_trigger:'تنفيذ أمر الشراء...','pay_trigger':'تنفيذ الدفع...',
    deal_trigger:'إبرام الصفقة...',cancel_trigger:'تم الإلغاء',
  },
  en: {
    'n-voice':'Voice Command','n-gesture':'Hand Gesture','n-deal':'Deal Execution',
    'n-circle':'Circle — Payments','n-home':'Smart Home','n-config':'API Settings',
    'nl-menu':'Menu','nl-log':'📜 Memory Log',
    'vt-title':'Real Voice Command — 3 Languages','vt-kw':'Buy & Pay Keywords',
    'gt-title':'Hand Gesture — Buy Command','dt-title':'Execute Deal — Voice, Gesture or Text',
    'pt-title':'Send Payment','tl-title':'Transaction History','ht-title':'Smart Control — Home & Car',
    'dm-voice':'Voice','dm-gest':'Gesture','dm-text':'Text',
    'dm-stab':'Stability','dm-std':'Standard','dm-vfy':'Verified',
    'deal-btn-txt':'Execute Global Deal','pb-txt':'Send Payment via Circle',
    'st-on':'Online','st-acc':'Standard','st-erc':'ERC-8004','st-voice-chip':'Voice: Ready','st-gest':'Gesture: Active',
    'wl-txc':'Transactions','wl-month':'This Month','sosBtnTxt':'🔔 SOS — Emergency',
    'micBtnTxt':'Start Listening','gestBtnTxt':'Enable Gesture Camera','sv-cfg':'Save Settings',
    'logEmpty':'No logs yet',
    buy_trigger:'Executing buy order...','pay_trigger':'Processing payment...',
    deal_trigger:'Executing deal...','cancel_trigger':'Cancelled',
  },
  it: {
    'n-voice':'Comando Vocale','n-gesture':'Gesto Mano','n-deal':'Esecuzione Deal',
    'n-circle':'Circle — Pagamenti','n-home':'Casa Intelligente','n-config':'Impostazioni API',
    'nl-menu':'Menu','nl-log':'📜 Registro Memoria',
    'vt-title':'Comando Vocale Reale — 3 Lingue','vt-kw':'Parole Chiave Acquisto e Pagamento',
    'gt-title':'Gesto Mano — Comando Acquisto','dt-title':'Eseguire Deal — Voce, Gesto o Testo',
    'pt-title':'Invia Pagamento','tl-title':'Storico Transazioni','ht-title':'Controllo Intelligente — Casa & Auto',
    'dm-voice':'Voce','dm-gest':'Gesto','dm-text':'Testo',
    'dm-stab':'Stabilità','dm-std':'Standard','dm-vfy':'Verificato',
    'deal-btn-txt':'Concludi Accordo Globale','pb-txt':'Invia Pagamento via Circle',
    'st-on':'Connesso','st-acc':'Standard','st-erc':'ERC-8004','st-voice-chip':'Voce: Pronto','st-gest':'Gesto: Attivo',
    'wl-txc':'Transazioni','wl-month':'Questo Mese','sosBtnTxt':'🔔 SOS — Emergenza',
    'micBtnTxt':'Inizia Ascolto','gestBtnTxt':'Attiva Camera Gesto','sv-cfg':'Salva Impostazioni',
    'logEmpty':'Nessun log',
    buy_trigger:"Eseguendo acquisto...",'pay_trigger':'Elaborando pagamento...',
    deal_trigger:"Concludendo l'accordo...",'cancel_trigger':'Annullato',
  }
};

// ================================================================
// CLOCK
// ================================================================
function updateClock(){
  const n=new Date();
  const d=n.toLocaleDateString('en-GB',{day:'2-digit',month:'2-digit',year:'numeric'});
  const t=n.toLocaleTimeString('en-GB',{hour:'2-digit',minute:'2-digit',second:'2-digit'});
  document.getElementById('clkTxt').textContent=d+' — '+t;
}
setInterval(updateClock,1000); updateClock();

// ================================================================
// LANG
// ================================================================
function setLang(lang, btn){
  APP.uiLang = lang;
  document.querySelectorAll('.ltab').forEach(b=>b.classList.remove('active'));
  if(btn) btn.classList.add('active');
  const dict = T[lang] || T.ar;
  Object.keys(dict).forEach(id=>{
    const el=document.getElementById(id);
    if(el) el.textContent=dict[id];
  });
  document.getElementById('logEmpty').textContent = dict['logEmpty']||'No logs';
  renderDevices();
}

function t(key){ return (T[APP.uiLang]||T.ar)[key] || (T.ar)[key] || key; }

// ================================================================
// NAV
// ================================================================
function nav(name, navEl){
  document.querySelectorAll('.view').forEach(v=>v.classList.remove('active'));
  document.getElementById('view-'+name).classList.add('active');
  document.querySelectorAll('.nitem').forEach(n=>n.classList.remove('active'));
  if(navEl) navEl.classList.add('active');
}
function setTab(btn){
  document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));
  btn.classList.add('active');
}

// ================================================================
// LOG & TOAST
// ================================================================
function addLog(msg){
  const log=document.getElementById('memLog');
  document.getElementById('logEmpty').style.display='none';
  const el=document.createElement('div'); el.className='log-entry';
  const t2=new Date().toLocaleTimeString('en-GB',{hour:'2-digit',minute:'2-digit',second:'2-digit'});
  el.textContent='['+t2+'] '+msg;
  log.insertBefore(el,log.firstChild);
  APP.logs.unshift(el.textContent);
  if(log.children.length>25) log.removeChild(log.lastChild);
}
function toast(msg,type='i'){
  const area=document.getElementById('toastArea');
  const d=document.createElement('div'); d.className='toast toast-'+type;
  d.textContent=msg; area.appendChild(d);
  setTimeout(()=>d.remove(),3200);
}

// ================================================================
// ACCESS & SOS
// ================================================================
function setAccess(lvl){
  APP.access=lvl;
  document.getElementById('b-std').classList.toggle('active',lvl==='standard');
  document.getElementById('b-mst').classList.toggle('active',lvl==='master');
  document.getElementById('st-acc').textContent=lvl==='master'?'🌟 Master Alpha':'Standard';
  toast(lvl==='master'?'🌟 Master Alpha Activated':'🔵 Standard Mode','w');
  addLog('Access: '+lvl);
}
function triggerSOS(){
  document.getElementById('sosModal').classList.remove('hidden');
  addLog('🚨 SOS Triggered');
  let p=0; const bar=document.getElementById('sosBar'),st=document.getElementById('sosSt');
  const steps=['Verifying links...','Sending alert...','Locating...','Notifying Alpha Hub...','🔒 All links locked'];
  let i=0;
  const iv=setInterval(()=>{ p+=20; bar.style.width=p+'%'; if(steps[i])st.textContent=steps[i++]; if(p>=100)clearInterval(iv); },400);
  toast('🚨 Emergency Protocol Activated','e');
}
function closeSOS(){ document.getElementById('sosModal').classList.add('hidden'); }

// ================================================================
// ===== VOICE COMMAND — REAL WEB SPEECH API =====
// ================================================================
const BUY_KEYWORDS = {
  'ar-SA': ['ابرم الصفقة','اشتر','اشتري','نفذ الدفع','ادفع','أكد الشراء','اشتر الآن','دفع','شراء'],
  'en-US': ['execute deal','buy now','confirm purchase','make payment','pay','buy','purchase','deal','execute'],
  'it-IT': ['concludi accordo','acquista ora','conferma acquisto','esegui pagamento','paga','acquista','pagamento','concludi']
};

function setVoiceLang(lang, btn){
  APP.voiceLang = lang;
  document.querySelectorAll('.vtrig').forEach(b=>b.classList.remove('active'));
  if(btn) btn.classList.add('active');
  if(APP.isListening){ stopMic(); setTimeout(startMic,200); }
  addLog('Voice lang: '+lang);
}

function toggleMic(){
  if(APP.isListening) stopMic(); else startMic();
}

function startMic(){
  const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
  if(!SR){ toast('⚠️ المتصفح لا يدعم التعرف الصوتي. استخدم Chrome','e'); return; }

  APP.recognition = new SR();
  APP.recognition.lang = APP.voiceLang;
  APP.recognition.continuous = true;
  APP.recognition.interimResults = true;

  const ring=document.getElementById('voiceRing');
  const status=document.getElementById('voiceStatus');
  const transcript=document.getElementById('voiceTranscript');
  const micBtn=document.getElementById('mainMicBtn');
  const micTxt=document.getElementById('micBtnTxt');

  APP.recognition.onstart = ()=>{
    APP.isListening=true;
    ring.classList.add('listening'); ring.classList.remove('success');
    document.getElementById('micIcon').textContent='🔴';
    status.textContent = APP.voiceLang==='ar-SA'?'أنا أسمعك...':APP.voiceLang==='it-IT'?'Sto ascoltando...':'Listening...';
    micBtn.classList.add('on');
    micTxt.textContent = APP.voiceLang==='ar-SA'?'إيقاف الاستماع':APP.voiceLang==='it-IT'?'Ferma Ascolto':'Stop Listening';
    toast('🎙️ Microphone Active','i');
  };

  APP.recognition.onresult = (e)=>{
    let interim='', final='';
    for(let i=e.resultIndex;i<e.results.length;i++){
      if(e.results[i].isFinal) final+=e.results[i][0].transcript;
      else interim+=e.results[i][0].transcript;
    }
    transcript.textContent = (final||interim).trim();
    if(final) processVoiceCommand(final.trim().toLowerCase());
  };

  APP.recognition.onerror = (e)=>{
    status.textContent='⚠️ خطأ: '+e.error;
    if(e.error!=='no-speech') stopMic();
  };

  APP.recognition.onend = ()=>{ if(APP.isListening) APP.recognition.start(); };
  APP.recognition.start();
  addLog('Voice started: '+APP.voiceLang);
}

function stopMic(){
  APP.isListening=false;
  if(APP.recognition){ APP.recognition.onend=null; APP.recognition.stop(); }
  const ring=document.getElementById('voiceRing');
  ring.classList.remove('listening');
  document.getElementById('micIcon').textContent='🎙️';
  document.getElementById('voiceStatus').textContent='اضغط للاستماع / Click to listen';
  document.getElementById('mainMicBtn').classList.remove('on');
  document.getElementById('micBtnTxt').textContent=t('micBtnTxt');
  addLog('Voice stopped');
}

function processVoiceCommand(text){
  const kws = BUY_KEYWORDS[APP.voiceLang] || BUY_KEYWORDS['en-US'];
  const matched = kws.find(kw => text.includes(kw));
  const resultBox = document.getElementById('voiceResultBox');
  const resultText = document.getElementById('voiceResultText');

  if(matched){
    const ring=document.getElementById('voiceRing');
    ring.classList.remove('listening'); ring.classList.add('success');
    document.getElementById('micIcon').textContent='✅';
    document.getElementById('voiceStatus').textContent='✅ أمر مُتعرَّف عليه!';
    addLog('🎙️ Voice command: "'+matched+'"');
    toast('🎙️ "'+matched+'" — '+t('deal_trigger'),'s');

    resultBox.classList.add('show');
    resultText.innerHTML = `<strong style="color:var(--green)">✅ ${t('deal_trigger')}</strong><br>
      <span style="color:var(--text2);font-size:12px">الأمر / Command: <span style="color:var(--gold);font-family:var(--mono)">"${matched}"</span></span><br>
      <span style="color:var(--text2);font-size:12px">النص الكامل / Full text: "${text}"</span>`;

    // Auto-execute deal after 1.5s
    setTimeout(()=>{ stopMic(); nav('deal',null); executeDeal(); },1500);

  } else {
    resultBox.classList.add('show');
    resultText.innerHTML = `<span style="color:var(--text2)">سمعت / Heard: <em style="color:var(--cyan)">"${text}"</em><br>
      <span style="font-size:11px;color:var(--text3)">لم يُعرَّف على أمر شراء. تابع الكلام...</span></span>`;
  }
}

// ================================================================
// ===== DEAL MIC (mini mic in deal view) =====
// ================================================================
function toggleDealMic(){
  if(APP.dealMicActive) stopDealMic(); else startDealMic();
}
function startDealMic(){
  const SR=window.SpeechRecognition||window.webkitSpeechRecognition;
  if(!SR){toast('⚠️ Use Chrome for voice','e');return;}
  APP.dealRecog=new SR();
  APP.dealRecog.lang=APP.voiceLang;
  APP.dealRecog.continuous=true; APP.dealRecog.interimResults=true;
  APP.dealRecog.onstart=()=>{
    APP.dealMicActive=true;
    document.getElementById('dealMic').classList.add('on');
    document.getElementById('dealVoiceStatus').textContent='🔴 Listening...';
  };
  APP.dealRecog.onresult=(e)=>{
    let txt='';
    for(let i=e.resultIndex;i<e.results.length;i++) txt+=e.results[i][0].transcript;
    document.getElementById('dealVoiceText').textContent=txt.trim();
    const kws=BUY_KEYWORDS[APP.voiceLang]||BUY_KEYWORDS['en-US'];
    if(kws.find(k=>txt.toLowerCase().includes(k))){
      stopDealMic();
      document.getElementById('dealMic').classList.add('done');
      document.getElementById('dealMic').textContent='✅';
      executeDeal();
    }
  };
  APP.dealRecog.onend=()=>{ if(APP.dealMicActive) APP.dealRecog.start(); };
  APP.dealRecog.start();
}
function stopDealMic(){
  APP.dealMicActive=false;
  if(APP.dealRecog){APP.dealRecog.onend=null;APP.dealRecog.stop();}
  document.getElementById('dealMic').classList.remove('on');
  document.getElementById('dealVoiceStatus').textContent='اضغط للاستماع';
}

// ================================================================
// ===== GESTURE DETECTION — MediaPipe Hands =====
// ================================================================
let handsInstance=null, camInstance=null, lastGesture='', gestureHoldCount=0;

const GESTURE_DEFS = [
  {name:'open_palm', ar:'كف مفتوح', en:'Open Palm', it:'Palmo Aperto', icon:'✋', action:'buy', actionAr:'شراء', actionEn:'Buy', actionIt:'Acquisto'},
  {name:'thumbs_up',  ar:'إبهام للأعلى', en:'Thumbs Up', it:'Pollice Su', icon:'👍', action:'confirm', actionAr:'تأكيد', actionEn:'Confirm', actionIt:'Conferma'},
  {name:'victory',    ar:'علامة النصر', en:'Victory', it:'Vittoria', icon:'✌️', action:'pay', actionAr:'دفع', actionEn:'Pay', actionIt:'Paga'},
  {name:'fist',       ar:'قبضة', en:'Fist', it:'Pugno', icon:'👊', action:'cancel', actionAr:'إلغاء', actionEn:'Cancel', actionIt:'Annulla'},
  {name:'call_me',    ar:'اتصل بي', en:'Call Me', it:'Chiamami', icon:'🤙', action:'sos', actionAr:'طوارئ', actionEn:'SOS', actionIt:'SOS'},
];

function classifyHandGesture(landmarks){
  // Finger extended check: tip y < pip y (in normalized coords, lower y = higher on screen)
  const tips=[4,8,12,16,20], pips=[3,6,10,14,18];
  const thumbUp = landmarks[4].x < landmarks[3].x; // thumb tip left of base (mirrored)
  const fingers = [1,2,3,4].map(i=> landmarks[tips[i]].y < landmarks[pips[i]].y);
  const extCount = fingers.filter(Boolean).length;

  // Open palm: 4 fingers up
  if(extCount >= 4) return 'open_palm';
  // Victory: index + middle up, others down
  if(fingers[0]&&fingers[1]&&!fingers[2]&&!fingers[3]) return 'victory';
  // Thumbs up: thumb up, all fingers down
  if(thumbUp && extCount===0) return 'thumbs_up';
  // Fist: all fingers down
  if(extCount===0&&!thumbUp) return 'fist';
  // Call me: pinky + thumb up
  if(fingers[3]&&thumbUp&&!fingers[0]&&!fingers[1]&&!fingers[2]) return 'call_me';
  return null;
}

async function toggleGesture(){
  if(APP.gestureActive){ stopGesture(); return; }
  const btn=document.getElementById('gestBtn');
  const wrap=document.getElementById('gestCamWrap');
  const vid=document.getElementById('gestureVideo');
  const canvas=document.getElementById('gestureCanvas');
  const placeholder=document.getElementById('gestPlaceholder');

  btn.textContent='⏳ جاري التهيئة...'; btn.disabled=true;

  try{
    APP.gestureStream = await navigator.mediaDevices.getUserMedia({video:{width:640,height:480},audio:false});
    vid.srcObject=APP.gestureStream;
    vid.style.display='block'; canvas.style.display='block';
    placeholder.style.display='none';
    wrap.classList.add('active-gesture');

    // Setup MediaPipe if available
    if(window.Hands){
      handsInstance = new Hands({locateFile:f=>`https://cdn.jsdelivr.net/npm/@mediapipe/hands/${f}`});
      handsInstance.setOptions({maxNumHands:1,modelComplexity:1,minDetectionConfidence:.7,minTrackingConfidence:.5});
      handsInstance.onResults(onHandResults);

      camInstance = new Camera(vid,{
        onFrame:async()=>{ await handsInstance.send({image:vid}); },
        width:640,height:480
      });
      camInstance.start();
    } else {
      // Fallback: simulate gesture detection without MediaPipe
      simulateGestureDetection();
    }

    APP.gestureActive=true;
    btn.textContent='🛑 إيقاف الكاميرا'; btn.disabled=false;
    btn.classList.add('active');
    document.getElementById('gestChip').style.display='flex';
    document.getElementById('gestBtnTxt').textContent='إيقاف';
    toast('👋 كاميرا الإشارة نشطة','s');
    addLog('Gesture camera: started');

  } catch(e){
    btn.textContent='⚠️ فشل الوصول إلى الكاميرا'; btn.disabled=false;
    toast('⚠️ Camera access denied: '+e.message,'e');
  }
}

function onHandResults(results){
  const canvas=document.getElementById('gestureCanvas');
  const ctx=canvas.getContext('2d');
  canvas.width=results.image.width; canvas.height=results.image.height;
  ctx.clearRect(0,0,canvas.width,canvas.height);

  if(results.multiHandLandmarks&&results.multiHandLandmarks.length>0){
    const landmarks=results.multiHandLandmarks[0];
    // Draw landmarks
    if(window.drawConnectors&&window.drawLandmarks){
      drawConnectors(ctx,landmarks,HAND_CONNECTIONS,{color:'rgba(255,215,0,0.6)',lineWidth:2});
      drawLandmarks(ctx,landmarks,{color:'rgba(0,212,255,0.8)',lineWidth:1,radius:3});
    }
    const gesture=classifyHandGesture(landmarks);
    if(gesture){ handleGestureDetected(gesture); }
    else{ setGestureDisplay('🤚','في انتظار الإشارة...','No gesture recognized'); }
  } else {
    setGestureDisplay('🤚','لا يوجد يد / No hand','Move your hand into frame');
  }
}

// Fallback simulation without MediaPipe
function simulateGestureDetection(){
  const gestures=['open_palm','thumbs_up','victory','fist'];
  let idx=0;
  const iv=setInterval(()=>{
    if(!APP.gestureActive){clearInterval(iv);return;}
    const g=gestures[idx%gestures.length]; idx++;
    handleGestureDetected(g);
  },3000);
  setGestureDisplay('🖐️','وضع المحاكاة — Simulation Mode','MediaPipe not loaded; simulating gestures');
  toast('📷 وضع محاكاة الإشارات (demo)','w');
}

function handleGestureDetected(gestureName){
  const def=GESTURE_DEFS.find(g=>g.name===gestureName);
  if(!def) return;

  // Debounce: require same gesture for 3 frames
  if(gestureName===lastGesture){ gestureHoldCount++; }
  else { gestureHoldCount=1; lastGesture=gestureName; }
  if(gestureHoldCount<3) return;

  const nameLoc = APP.uiLang==='it'?def.it:APP.uiLang==='en'?def.en:def.ar;
  const actLoc  = APP.uiLang==='it'?def.actionIt:APP.uiLang==='en'?def.actionEn:def.actionAr;

  setGestureDisplay(def.icon, nameLoc, '→ '+actLoc);

  // Only trigger once per gesture (reset count)
  if(gestureHoldCount===3){
    addLog('👋 Gesture: '+def.name+' → '+def.action);
    const wrap=document.getElementById('gestCamWrap');

    if(def.action==='buy'||def.action==='pay'||def.action==='confirm'){
      wrap.classList.add('gesture-buy');
      toast(def.icon+' '+nameLoc+' — '+t('deal_trigger'),'s');
      showGestureAction('✅ '+t('deal_trigger'));
      setTimeout(()=>{wrap.classList.remove('gesture-buy'); nav('deal',null); executeDeal();},1800);
    } else if(def.action==='cancel'){
      toast('👊 '+t('cancel_trigger'),'w');
      showGestureAction('❌ '+t('cancel_trigger'));
    } else if(def.action==='sos'){
      triggerSOS();
    }
  }
}

function setGestureDisplay(icon,name,action){
  document.getElementById('gestIcon').textContent=icon;
  document.getElementById('gestName').textContent=name;
  document.getElementById('gestAction').textContent=action;
}

function showGestureAction(msg){
  const el=document.getElementById('gestureActionResult');
  el.innerHTML=`<div style="margin-top:8px;padding:10px 14px;background:rgba(0,230,118,.08);border:1px solid rgba(0,230,118,.2);border-radius:10px;font-size:13px;color:var(--green)">${msg}</div>`;
  setTimeout(()=>el.innerHTML='',4000);
}

function stopGesture(){
  APP.gestureActive=false; lastGesture=''; gestureHoldCount=0;
  if(camInstance){try{camInstance.stop();}catch(e){}} camInstance=null;
  if(handsInstance){try{handsInstance.close();}catch(e){}} handsInstance=null;
  if(APP.gestureStream) APP.gestureStream.getTracks().forEach(t2=>t2.stop());
  document.getElementById('gestureVideo').style.display='none';
  document.getElementById('gestureCanvas').style.display='none';
  document.getElementById('gestPlaceholder').style.display='flex';
  document.getElementById('gestCamWrap').classList.remove('active-gesture','gesture-buy');
  const btn=document.getElementById('gestBtn');
  btn.classList.remove('active');
  btn.textContent='📷 '+t('gestBtnTxt');
  document.getElementById('gestChip').style.display='none';
  setGestureDisplay('🤚','في انتظار الإشارة...','وجّه يدك أمام الكاميرا');
  toast('👋 Gesture camera stopped','i');
  addLog('Gesture camera: stopped');
}

// ================================================================
// ===== DEAL EXECUTION =====
// ================================================================
let dealMode='voice';
function setDealMode(mode, btn){
  dealMode=mode;
  document.querySelectorAll('.mode-btn').forEach(b=>b.classList.remove('active'));
  if(btn) btn.classList.add('active');
  document.querySelectorAll('.mode-panel').forEach(p=>p.classList.remove('show'));
  document.getElementById('mp-'+mode).classList.add('show');
  if(mode==='voice') startDealMic();
  else stopDealMic();
}

const delay=ms=>new Promise(r=>setTimeout(r,ms));

async function executeDeal(){
  const btn=document.getElementById('dealBtn');
  const prog=document.getElementById('dealProg');
  const bar=document.getElementById('dealBar');
  const lbl=document.getElementById('dealLabel');
  const succ=document.getElementById('dealSuccess');

  if(btn.disabled) return;
  btn.disabled=true; prog.style.display='block'; succ.style.display='none';

  const cmd=document.getElementById('dealTextInput')?.value||'Deal Command';
  addLog('🚀 Deal: '+cmd.substring(0,40));

  const steps_map={
    ar:['تحليل الأمر...','التحقق من الهوية...','ربط التوكن...','فحص السيولة...','البث على ERC-8004...','✅ الصفقة مُبرمة!'],
    en:['Analyzing command...','Verifying identity...','Linking token...','Checking liquidity...','Broadcasting on ERC-8004...','✅ Deal executed!'],
    it:["Analisi comando...",'Verifica identità...','Collegamento token...','Verifica liquidità...','Trasmissione ERC-8004...','✅ Accordo concluso!']
  };
  const steps=steps_map[APP.uiLang]||steps_map.ar;

  for(let i=0;i<steps.length;i++){
    await delay(480);
    bar.style.width=Math.round((i+1)/steps.length*100)+'%';
    lbl.textContent=steps[i];
  }

  const cert='STAR-UNIV-2026-'+Date.now();
  const now=new Date().toLocaleString();
  succ.style.display='block';
  succ.innerHTML=`<div class="success-card">
    <h2>🏆 ${steps[steps.length-1]}</h2>
    <div class="cert-code">Certificate: ${cert}</div>
    <div style="font-size:12px;color:var(--text2)">Status: ✅ Validated | ERC-8004 · ${APP.network}</div>
    <div style="font-size:11px;color:var(--text3);margin-top:4px;font-family:var(--mono)">${now}</div>
  </div>`;

  toast('🎉 '+(steps[steps.length-1]),'s');
  btn.disabled=false; prog.style.display='none';
  speakConfirmation();
}

// ================================================================
// VOICE OUTPUT (speak confirmation)
// ================================================================
function speakConfirmation(){
  if(!window.speechSynthesis) return;
  const msgs={ar:'تمت الصفقة بنجاح','en':'Deal executed successfully','it':'Accordo concluso con successo'};
  const lang_map={ar:'ar-SA',en:'en-US',it:'it-IT'};
  const utt=new SpeechSynthesisUtterance(msgs[APP.uiLang]||msgs.ar);
  utt.lang=lang_map[APP.uiLang]||'ar-SA'; utt.rate=0.9; utt.pitch=1;
  window.speechSynthesis.speak(utt);
}

// ================================================================
// CIRCLE PAYMENTS
// ================================================================
function saveCircle(){
  const k=document.getElementById('circleKey').value.trim();
  const n=document.getElementById('netInput').value.trim()||'arc-testnet';
  if(k) APP.circleKey=k;
  APP.network=n;
  document.getElementById('netChip').textContent=n;
  toast('✅ Circle configured','s'); addLog('Circle: '+n);
}

async function execPayment(){
  const amt=document.getElementById('payAmt').value;
  const dest=document.getElementById('payDest').value.trim();
  const cur=document.getElementById('payCur').value;
  const net=document.getElementById('payNet').value;
  if(!amt||parseFloat(amt)<=0){toast('Enter valid amount','w');return;}
  if(!dest){toast('Enter recipient address','w');return;}
  const btn=document.getElementById('payBtn');
  const prog=document.getElementById('payProg');
  const bar=document.getElementById('payBar');
  const lbl=document.getElementById('payLbl');
  btn.disabled=true; prog.style.display='block'; bar.style.width='0%';
  addLog('Circle Pay: '+amt+' '+cur+' → '+dest.substring(0,12)+'...');
  const steps_p=['Validating address...','Creating transaction...','Broadcasting...','Awaiting confirmation...','✅ Confirmed!'];
  for(let i=0;i<steps_p.length;i++){ await delay(550); bar.style.width=((i+1)*20)+'%'; lbl.textContent=steps_p[i]; }
  const hash='0x'+[...Array(40)].map(()=>Math.floor(Math.random()*16).toString(16)).join('');
  const shortH=hash.substring(0,10)+'...'+hash.substring(38);
  // Update balance
  const balEl=document.getElementById('usdcBal');
  balEl.textContent=(parseFloat(balEl.textContent)-parseFloat(amt)).toFixed(2)+' '+cur;
  document.getElementById('txCount').textContent=parseInt(document.getElementById('txCount').textContent)+1;
  // Add to tx list
  const list=document.getElementById('txList');
  const div=document.createElement('div'); div.className='tx-item';
  div.innerHTML=`<div style="font-size:18px;width:28px;text-align:center">✅</div>
    <div style="flex:1"><div class="tx-id">${shortH}</div><div class="tx-desc">${cur} Transfer — ${net}</div></div>
    <div style="text-align:left"><div class="tx-amt" style="color:var(--red)">-${parseFloat(amt).toFixed(2)} ${cur}</div><span class="s-confirmed">confirmed</span></div>`;
  list.insertBefore(div,list.firstChild);
  toast('✅ '+amt+' '+cur+' sent!','s');
  addLog('TX confirmed: '+shortH);
  btn.disabled=false; prog.style.display='none';
  document.getElementById('payAmt').value=''; document.getElementById('payDest').value='';
}

// ================================================================
// SMART HOME
// ================================================================
function renderDevices(){
  const grid=document.getElementById('devGrid');
  const lang=APP.uiLang;
  grid.innerHTML=APP.devices.map(d=>{
    const nm=lang==='it'?d.it:lang==='en'?d.en:d.ar;
    const st=d.on?(lang==='it'?'Attivo':lang==='en'?'Active':'نشط'):(lang==='it'?'Spento':lang==='en'?'Off':'متوقف');
    return `<div class="dev-card ${d.on?'on':'off'}" id="dev-${d.id}">
      <div class="d-ico">${d.icon}</div>
      <div class="d-nm">${nm}</div>
      <div class="d-st ${d.on?'on':'off'}">${st}</div>
      <button class="tog ${d.on?'on':''}" onclick="toggleDev('${d.id}')"></button>
    </div>`;
  }).join('');
}

function toggleDev(id){
  const d=APP.devices.find(x=>x.id===id);
  d.on=!d.on; renderDevices();
  const nm=APP.uiLang==='it'?d.it:APP.uiLang==='en'?d.en:d.ar;
  toast(d.icon+' '+nm+': '+(d.on?'ON':'OFF'), d.on?'s':'w');
  addLog('Device '+d.en+': '+(d.on?'ON':'OFF'));
}

// ================================================================
// CONFIG
// ================================================================
function saveAllCfg(){
  const g=document.getElementById('cfgGem').value.trim();
  const c=document.getElementById('cfgCirc').value.trim();
  const n=document.getElementById('cfgNet').value.trim();
  if(g) APP.geminiKey=g;
  if(c) APP.circleKey=c;
  if(n){ APP.network=n; document.getElementById('netChip').textContent=n; }
  toast('✅ All settings saved','s'); addLog('Config saved');
}

// ================================================================
// INIT
// ================================================================
renderDevices();
addLog('FlashDeal Star v3 — Voice+Gesture ready');
toast('🌟 FlashDeal Star v3 — Voice & Gesture Loaded','s');
</script>
</body>
</html>
