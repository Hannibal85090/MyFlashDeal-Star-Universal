<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>FinAgent AI — الوكيل المالي الذكي</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #0a0c0f;
    --bg2: #0f1218;
    --bg3: #141820;
    --panel: #1a1f2e;
    --border: rgba(99,179,255,0.12);
    --border2: rgba(99,179,255,0.22);
    --accent: #3b82f6;
    --accent2: #60a5fa;
    --green: #10b981;
    --red: #ef4444;
    --amber: #f59e0b;
    --purple: #8b5cf6;
    --text: #e8edf5;
    --text2: #94a3b8;
    --text3: #4a5568;
    --glow: rgba(59,130,246,0.15);
    --font: 'IBM Plex Sans Arabic', sans-serif;
    --mono: 'JetBrains Mono', monospace;
  }

  * { margin:0; padding:0; box-sizing:border-box; }

  body {
    font-family: var(--font);
    background: var(--bg);
    color: var(--text);
    min-height: 100vh;
    overflow-x: hidden;
  }

  /* Background grid */
  body::before {
    content: '';
    position: fixed; inset: 0;
    background-image:
      linear-gradient(rgba(59,130,246,0.04) 1px, transparent 1px),
      linear-gradient(90deg, rgba(59,130,246,0.04) 1px, transparent 1px);
    background-size: 40px 40px;
    pointer-events: none; z-index: 0;
  }

  /* Ambient glow */
  body::after {
    content: '';
    position: fixed;
    top: -200px; left: 50%; transform: translateX(-50%);
    width: 800px; height: 600px;
    background: radial-gradient(ellipse, rgba(59,130,246,0.08) 0%, transparent 70%);
    pointer-events: none; z-index: 0;
  }

  /* ===== LAYOUT ===== */
  .app { position: relative; z-index: 1; display: flex; flex-direction: column; height: 100vh; }

  /* ===== HEADER ===== */
  header {
    display: flex; align-items: center; justify-content: space-between;
    padding: 0 28px; height: 60px;
    border-bottom: 1px solid var(--border);
    background: rgba(10,12,15,0.8);
    backdrop-filter: blur(20px);
    position: sticky; top: 0; z-index: 100;
  }

  .logo {
    display: flex; align-items: center; gap: 10px;
  }

  .logo-icon {
    width: 36px; height: 36px;
    background: linear-gradient(135deg, var(--accent), var(--purple));
    border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    font-size: 18px;
    box-shadow: 0 0 20px rgba(59,130,246,0.3);
  }

  .logo-text { font-size: 17px; font-weight: 700; letter-spacing: -0.3px; }
  .logo-text span { color: var(--accent2); }

  .header-center {
    display: flex; gap: 6px;
  }

  .tab-btn {
    padding: 6px 16px;
    background: transparent;
    border: 1px solid transparent;
    border-radius: 8px;
    color: var(--text2);
    font-family: var(--font);
    font-size: 13px;
    cursor: pointer;
    transition: all 0.2s;
  }

  .tab-btn.active {
    background: rgba(59,130,246,0.12);
    border-color: var(--border2);
    color: var(--accent2);
  }

  .tab-btn:hover:not(.active) { color: var(--text); }

  .status-badge {
    display: flex; align-items: center; gap: 6px;
    padding: 5px 12px;
    background: rgba(16,185,129,0.1);
    border: 1px solid rgba(16,185,129,0.25);
    border-radius: 20px;
    font-size: 12px; color: var(--green);
  }

  .status-dot {
    width: 6px; height: 6px;
    background: var(--green);
    border-radius: 50%;
    animation: pulse 2s infinite;
  }

  @keyframes pulse {
    0%,100% { opacity:1; transform:scale(1); }
    50% { opacity:0.5; transform:scale(0.8); }
  }

  /* ===== MAIN LAYOUT ===== */
  .main { display: flex; flex: 1; overflow: hidden; }

  /* ===== SIDEBAR ===== */
  .sidebar {
    width: 280px;
    border-left: 1px solid var(--border);
    background: var(--bg2);
    display: flex; flex-direction: column;
    overflow: hidden;
    flex-shrink: 0;
  }

  .sidebar-section { padding: 16px; border-bottom: 1px solid var(--border); }
  .sidebar-label {
    font-size: 10px; font-weight: 600; letter-spacing: 1.2px;
    color: var(--text3); text-transform: uppercase; margin-bottom: 12px;
  }

  /* Market Cards */
  .market-card {
    padding: 10px 12px;
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 10px;
    margin-bottom: 6px;
    cursor: pointer;
    transition: all 0.2s;
  }

  .market-card:hover { border-color: var(--border2); }

  .market-card-top { display: flex; justify-content: space-between; align-items: center; }
  .market-symbol { font-size: 13px; font-weight: 600; }
  .market-change {
    font-size: 11px; font-family: var(--mono);
    padding: 2px 6px; border-radius: 4px; font-weight: 500;
  }
  .up { background: rgba(16,185,129,0.15); color: var(--green); }
  .down { background: rgba(239,68,68,0.15); color: var(--red); }

  .market-price { font-size: 15px; font-family: var(--mono); font-weight: 600; margin-top: 3px; }
  .market-name { font-size: 11px; color: var(--text2); margin-top: 1px; }

  /* Spark line mini */
  .spark { margin-top: 6px; }
  .spark svg { width: 100%; height: 28px; }

  /* Agent capabilities */
  .capability-item {
    display: flex; align-items: center; gap: 8px;
    padding: 7px 10px;
    border-radius: 8px;
    font-size: 12px; color: var(--text2);
    cursor: pointer; transition: all 0.15s;
    margin-bottom: 3px;
  }

  .capability-item:hover { background: rgba(59,130,246,0.08); color: var(--text); }
  .capability-icon { font-size: 15px; width: 20px; text-align: center; }

  /* ===== CHAT AREA ===== */
  .chat-area {
    flex: 1;
    display: flex; flex-direction: column;
    overflow: hidden;
  }

  /* Context bar */
  .context-bar {
    padding: 10px 24px;
    border-bottom: 1px solid var(--border);
    background: var(--bg2);
    display: flex; align-items: center; gap: 12px;
    font-size: 12px; color: var(--text2);
    flex-wrap: wrap; gap: 8px;
  }

  .ctx-tag {
    padding: 3px 10px;
    background: rgba(59,130,246,0.1);
    border: 1px solid rgba(59,130,246,0.2);
    border-radius: 20px;
    font-size: 11px; color: var(--accent2);
    cursor: pointer; transition: all 0.15s;
  }
  .ctx-tag:hover { background: rgba(59,130,246,0.2); }

  /* Messages */
  .messages {
    flex: 1; overflow-y: auto;
    padding: 24px;
    display: flex; flex-direction: column; gap: 16px;
    scroll-behavior: smooth;
  }

  .messages::-webkit-scrollbar { width: 4px; }
  .messages::-webkit-scrollbar-track { background: transparent; }
  .messages::-webkit-scrollbar-thumb { background: var(--border2); border-radius: 2px; }

  /* Welcome screen */
  .welcome {
    display: flex; flex-direction: column; align-items: center;
    justify-content: center; flex: 1;
    padding: 40px;
    text-align: center;
  }

  .welcome-icon {
    width: 80px; height: 80px;
    background: linear-gradient(135deg, rgba(59,130,246,0.2), rgba(139,92,246,0.2));
    border: 1px solid var(--border2);
    border-radius: 24px;
    display: flex; align-items: center; justify-content: center;
    font-size: 36px; margin-bottom: 24px;
    box-shadow: 0 0 40px rgba(59,130,246,0.1);
    animation: float 4s ease-in-out infinite;
  }

  @keyframes float {
    0%,100% { transform: translateY(0); }
    50% { transform: translateY(-8px); }
  }

  .welcome h2 { font-size: 26px; font-weight: 700; margin-bottom: 10px; }
  .welcome p { color: var(--text2); font-size: 14px; max-width: 400px; line-height: 1.7; margin-bottom: 28px; }

  .suggestions-grid {
    display: grid; grid-template-columns: 1fr 1fr;
    gap: 10px; width: 100%; max-width: 520px;
  }

  .suggestion-card {
    padding: 14px 16px;
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 12px;
    cursor: pointer;
    text-align: right;
    transition: all 0.2s;
    font-size: 13px;
    line-height: 1.5;
  }

  .suggestion-card:hover {
    border-color: var(--accent);
    background: rgba(59,130,246,0.05);
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(59,130,246,0.1);
  }

  .suggestion-card .s-icon { font-size: 20px; margin-bottom: 8px; display: block; }
  .suggestion-card .s-text { color: var(--text2); font-size: 12px; }

  /* Message bubbles */
  .message { display: flex; gap: 12px; animation: msgIn 0.3s ease; max-width: 100%; }
  @keyframes msgIn { from { opacity:0; transform: translateY(10px); } to { opacity:1; transform:none; } }

  .message.user { flex-direction: row-reverse; }

  .msg-avatar {
    width: 34px; height: 34px; border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    font-size: 16px; flex-shrink: 0;
  }

  .ai-avatar {
    background: linear-gradient(135deg, var(--accent), var(--purple));
    box-shadow: 0 0 12px rgba(59,130,246,0.3);
  }

  .user-avatar { background: var(--panel); border: 1px solid var(--border); }

  .msg-content { flex: 1; max-width: 75%; }

  .msg-bubble {
    padding: 12px 16px;
    border-radius: 14px;
    font-size: 14px; line-height: 1.7;
  }

  .ai-bubble {
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 14px 14px 14px 2px;
  }

  .user-bubble {
    background: rgba(59,130,246,0.15);
    border: 1px solid rgba(59,130,246,0.25);
    border-radius: 14px 14px 2px 14px;
    text-align: right;
  }

  .msg-time {
    font-size: 10px; color: var(--text3);
    margin-top: 4px;
    text-align: left;
  }

  .message.user .msg-time { text-align: right; }

  /* Financial data cards inside messages */
  .fin-card {
    margin-top: 12px;
    padding: 14px;
    background: rgba(15,18,24,0.8);
    border: 1px solid var(--border);
    border-radius: 10px;
    font-size: 13px;
  }

  .fin-card-title {
    font-size: 11px; font-weight: 600; letter-spacing: 0.8px;
    color: var(--accent2); text-transform: uppercase; margin-bottom: 10px;
  }

  .fin-row {
    display: flex; justify-content: space-between;
    padding: 5px 0; border-bottom: 1px solid var(--border);
  }

  .fin-row:last-child { border-bottom: none; }
  .fin-key { color: var(--text2); }
  .fin-val { font-family: var(--mono); font-weight: 500; }
  .fin-val.pos { color: var(--green); }
  .fin-val.neg { color: var(--red); }
  .fin-val.neu { color: var(--accent2); }

  /* Thinking indicator */
  .thinking {
    display: flex; align-items: center; gap: 8px;
    padding: 10px 14px;
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 10px;
    font-size: 12px; color: var(--text2);
  }

  .thinking-dots { display: flex; gap: 4px; }
  .thinking-dots span {
    width: 5px; height: 5px;
    background: var(--accent);
    border-radius: 50%;
    animation: blink 1.2s infinite;
  }
  .thinking-dots span:nth-child(2) { animation-delay: 0.2s; }
  .thinking-dots span:nth-child(3) { animation-delay: 0.4s; }
  @keyframes blink { 0%,80%,100%{opacity:0.2} 40%{opacity:1} }

  /* ===== INPUT AREA ===== */
  .input-area {
    padding: 16px 24px 20px;
    border-top: 1px solid var(--border);
    background: var(--bg2);
  }

  .input-toolbar {
    display: flex; gap: 6px; margin-bottom: 10px;
    flex-wrap: wrap;
  }

  .tool-chip {
    display: flex; align-items: center; gap: 5px;
    padding: 4px 10px;
    background: transparent;
    border: 1px solid var(--border);
    border-radius: 6px;
    color: var(--text2); font-family: var(--font);
    font-size: 11px; cursor: pointer;
    transition: all 0.15s;
  }

  .tool-chip:hover, .tool-chip.active {
    border-color: var(--accent);
    color: var(--accent2);
    background: rgba(59,130,246,0.08);
  }

  .input-box {
    display: flex; gap: 10px; align-items: flex-end;
  }

  textarea {
    flex: 1;
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 12px 16px;
    color: var(--text);
    font-family: var(--font);
    font-size: 14px;
    resize: none;
    height: 50px; max-height: 120px;
    outline: none;
    transition: border-color 0.2s;
    line-height: 1.5;
  }

  textarea::placeholder { color: var(--text3); }
  textarea:focus { border-color: var(--accent); }

  .send-btn {
    width: 46px; height: 46px;
    background: linear-gradient(135deg, var(--accent), var(--purple));
    border: none; border-radius: 12px;
    cursor: pointer; display: flex;
    align-items: center; justify-content: center;
    transition: all 0.2s;
    box-shadow: 0 4px 14px rgba(59,130,246,0.3);
    flex-shrink: 0;
  }

  .send-btn:hover { transform: scale(1.05); box-shadow: 0 6px 20px rgba(59,130,246,0.4); }
  .send-btn:active { transform: scale(0.97); }
  .send-btn:disabled { opacity: 0.4; cursor: not-allowed; transform: none; }

  .send-btn svg { width: 18px; height: 18px; fill: white; }

  /* ===== DASHBOARD TAB ===== */
  .dashboard {
    display: none; flex: 1; padding: 24px; overflow-y: auto; gap: 20px;
    flex-direction: column;
  }

  .dashboard.active { display: flex; }

  .dash-grid {
    display: grid; grid-template-columns: repeat(4, 1fr);
    gap: 14px;
  }

  .kpi-card {
    padding: 18px;
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 14px;
    transition: all 0.2s;
  }

  .kpi-card:hover { border-color: var(--border2); transform: translateY(-2px); }

  .kpi-label { font-size: 11px; color: var(--text2); margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.6px; }
  .kpi-value { font-size: 24px; font-weight: 700; font-family: var(--mono); }
  .kpi-change { font-size: 12px; margin-top: 4px; }

  .chart-row { display: grid; grid-template-columns: 2fr 1fr; gap: 14px; }

  .chart-card {
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 20px;
  }

  .chart-title { font-size: 13px; font-weight: 600; margin-bottom: 16px; color: var(--text2); }

  /* SVG Chart */
  .chart-svg { width: 100%; }

  /* Portfolio donut */
  .portfolio-items { display: flex; flex-direction: column; gap: 8px; margin-top: 12px; }
  .port-item {
    display: flex; align-items: center; gap: 8px;
    font-size: 12px;
  }
  .port-dot { width: 8px; height: 8px; border-radius: 50%; flex-shrink: 0; }
  .port-name { flex: 1; color: var(--text2); }
  .port-pct { font-family: var(--mono); font-size: 11px; }

  /* Alerts */
  .alerts-section { }
  .alert-card {
    display: flex; align-items: center; gap: 12px;
    padding: 12px 16px;
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 10px;
    margin-bottom: 8px;
    font-size: 13px;
    cursor: pointer; transition: all 0.15s;
  }
  .alert-card:hover { border-color: var(--border2); }
  .alert-icon { font-size: 18px; width: 28px; text-align: center; }
  .alert-text { flex: 1; }
  .alert-text strong { display: block; font-size: 13px; }
  .alert-text span { color: var(--text2); font-size: 11px; }
  .alert-time { font-size: 10px; color: var(--text3); font-family: var(--mono); }

  /* ===== AGENTS TAB ===== */
  .agents-view {
    display: none; flex: 1; padding: 24px; overflow-y: auto;
  }
  .agents-view.active { display: block; }

  .agents-grid {
    display: grid; grid-template-columns: repeat(3, 1fr);
    gap: 16px; margin-bottom: 24px;
  }

  .agent-card {
    padding: 20px;
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 16px;
    cursor: pointer; transition: all 0.25s;
    position: relative; overflow: hidden;
  }

  .agent-card::before {
    content: ''; position: absolute;
    top: 0; right: 0; left: 0; height: 2px;
  }

  .agent-card.a1::before { background: linear-gradient(90deg, var(--accent), var(--purple)); }
  .agent-card.a2::before { background: linear-gradient(90deg, var(--green), #34d399); }
  .agent-card.a3::before { background: linear-gradient(90deg, var(--amber), #fcd34d); }
  .agent-card.a4::before { background: linear-gradient(90deg, var(--red), #f87171); }
  .agent-card.a5::before { background: linear-gradient(90deg, var(--purple), #c084fc); }
  .agent-card.a6::before { background: linear-gradient(90deg, #06b6d4, #22d3ee); }

  .agent-card:hover {
    border-color: var(--border2);
    transform: translateY(-3px);
    box-shadow: 0 12px 32px rgba(0,0,0,0.3);
  }

  .agent-icon { font-size: 28px; margin-bottom: 12px; }
  .agent-name { font-size: 15px; font-weight: 600; margin-bottom: 6px; }
  .agent-desc { font-size: 12px; color: var(--text2); line-height: 1.6; margin-bottom: 12px; }
  .agent-status {
    display: flex; align-items: center; gap: 5px;
    font-size: 11px; color: var(--green);
  }
  .agent-status-dot { width: 5px; height: 5px; background: var(--green); border-radius: 50%; }

  /* ===== RESPONSIVE ===== */
  @media (max-width: 900px) {
    .sidebar { display: none; }
    .dash-grid { grid-template-columns: repeat(2,1fr); }
    .agents-grid { grid-template-columns: repeat(2,1fr); }
    .chart-row { grid-template-columns: 1fr; }
    .suggestions-grid { grid-template-columns: 1fr; }
  }

  @media (max-width: 600px) {
    .dash-grid { grid-template-columns: 1fr 1fr; }
    .agents-grid { grid-template-columns: 1fr; }
    header { padding: 0 14px; }
    .messages { padding: 16px; }
    .input-area { padding: 12px 16px 16px; }
  }

  /* Typing animation */
  .typing-cursor::after {
    content: '▋';
    animation: cursor-blink 0.7s infinite;
    color: var(--accent);
  }
  @keyframes cursor-blink { 0%,100% { opacity:1; } 50% { opacity:0; } }

  .section-title {
    font-size: 18px; font-weight: 700;
    margin-bottom: 16px;
    display: flex; align-items: center; gap: 10px;
  }

  .badge {
    font-size: 10px; padding: 2px 8px;
    background: rgba(59,130,246,0.15);
    border: 1px solid rgba(59,130,246,0.3);
    border-radius: 20px; color: var(--accent2);
    font-weight: 500;
  }

  /* Disclaimer */
  .disclaimer {
    font-size: 11px; color: var(--text3);
    text-align: center; padding: 0 24px 8px;
  }

  /* Loading overlay */
  #loading {
    position: fixed; inset: 0;
    background: var(--bg);
    display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    z-index: 1000;
    transition: opacity 0.5s;
  }

  .load-logo { font-size: 48px; margin-bottom: 20px; animation: float 2s ease-in-out infinite; }
  .load-text { font-size: 20px; font-weight: 700; margin-bottom: 8px; }
  .load-sub { font-size: 13px; color: var(--text2); }
  .load-bar-wrap { margin-top: 28px; width: 200px; height: 3px; background: var(--panel); border-radius: 2px; overflow: hidden; }
  .load-bar { height: 100%; background: linear-gradient(90deg, var(--accent), var(--purple)); border-radius: 2px; animation: loadProgress 1.5s ease forwards; }
  @keyframes loadProgress { from{width:0} to{width:100%} }
</style>
</head>
<body>

<!-- Loading screen -->
<div id="loading">
  <div class="load-logo">🤖</div>
  <div class="load-text">FinAgent AI</div>
  <div class="load-sub">تهيئة الوكيل المالي الذكي...</div>
  <div class="load-bar-wrap"><div class="load-bar"></div></div>
</div>

<div class="app">
  <!-- Header -->
  <header>
    <div class="logo">
      <div class="logo-icon">🤖</div>
      <div class="logo-text">Fin<span>Agent</span> AI</div>
    </div>

    <div class="header-center">
      <button class="tab-btn active" onclick="switchTab('chat',this)">💬 المحادثة</button>
      <button class="tab-btn" onclick="switchTab('dashboard',this)">📊 لوحة التحكم</button>
      <button class="tab-btn" onclick="switchTab('agents',this)">🤖 الوكلاء</button>
    </div>

    <div class="status-badge">
      <div class="status-dot"></div>
      الوكيل نشط
    </div>
  </header>

  <!-- Main -->
  <div class="main">

    <!-- Sidebar -->
    <aside class="sidebar">
      <div class="sidebar-section">
        <div class="sidebar-label">السوق المباشر</div>
        <div class="market-card" onclick="askAbout('تحليل مفصل لسهم أرامكو السعودية')">
          <div class="market-card-top">
            <span class="market-symbol">2222.SR</span>
            <span class="market-change up">+1.24%</span>
          </div>
          <div class="market-price">29.85 ر.س</div>
          <div class="market-name">أرامكو السعودية</div>
          <div class="spark">
            <svg viewBox="0 0 100 28"><polyline points="0,22 12,18 24,20 36,14 48,16 60,10 72,12 84,8 100,6" fill="none" stroke="#10b981" stroke-width="1.5"/></svg>
          </div>
        </div>
        <div class="market-card" onclick="askAbout('تحليل سهم سابك وتوقعات السعر')">
          <div class="market-card-top">
            <span class="market-symbol">2010.SR</span>
            <span class="market-change down">-0.85%</span>
          </div>
          <div class="market-price">81.40 ر.س</div>
          <div class="market-name">سابك</div>
          <div class="spark">
            <svg viewBox="0 0 100 28"><polyline points="0,8 12,10 24,8 36,14 48,12 60,16 72,14 84,18 100,20" fill="none" stroke="#ef4444" stroke-width="1.5"/></svg>
          </div>
        </div>
        <div class="market-card" onclick="askAbout('ما هو مؤشر تداول اليوم وأبرز التحركات')">
          <div class="market-card-top">
            <span class="market-symbol">TASI</span>
            <span class="market-change up">+0.63%</span>
          </div>
          <div class="market-price">11,420</div>
          <div class="market-name">مؤشر تداول السعودي</div>
          <div class="spark">
            <svg viewBox="0 0 100 28"><polyline points="0,16 15,14 30,12 45,15 60,11 75,9 90,7 100,5" fill="none" stroke="#10b981" stroke-width="1.5"/></svg>
          </div>
        </div>
      </div>

      <div class="sidebar-section" style="flex:1;overflow-y:auto">
        <div class="sidebar-label">قدرات الوكيل</div>
        <div class="capability-item" onclick="askAbout('حلل محفظتي الاستثمارية وقدم توصيات')">
          <span class="capability-icon">📈</span> تحليل المحافظ الاستثمارية
        </div>
        <div class="capability-item" onclick="askAbout('ما هي أفضل استراتيجيات إدارة المخاطر المالية')">
          <span class="capability-icon">🛡️</span> إدارة المخاطر
        </div>
        <div class="capability-item" onclick="askAbout('اعطني تقرير الأخبار المالية اليوم')">
          <span class="capability-icon">📰</span> تحليل الأخبار المالية
        </div>
        <div class="capability-item" onclick="askAbout('ما هي أفضل توزيع للأصول لمحفظة متوازنة')">
          <span class="capability-icon">⚖️</span> تخصيص الأصول
        </div>
        <div class="capability-item" onclick="askAbout('اعطني تقرير الاقتصاد الكلي والتوقعات')">
          <span class="capability-icon">🌍</span> الاقتصاد الكلي
        </div>
        <div class="capability-item" onclick="askAbout('ما هو الفرق بين ETF والصناديق المشتركة')">
          <span class="capability-icon">🎓</span> التعليم المالي
        </div>
        <div class="capability-item" onclick="askAbout('احسب عائد الاستثمار لمدة 5 سنوات')">
          <span class="capability-icon">🔢</span> الحسابات المالية
        </div>
        <div class="capability-item" onclick="askAbout('قارن بين الاستثمار في الذهب والعقارات')">
          <span class="capability-icon">🔍</span> المقارنة والتقييم
        </div>
      </div>
    </aside>

    <!-- Chat View -->
    <div id="view-chat" class="chat-area">
      <div class="context-bar">
        <span style="color:var(--text3)">سياق الوكيل:</span>
        <span class="ctx-tag" onclick="askAbout('ما هي فرص الاستثمار في السوق السعودي حالياً')">🇸🇦 السوق السعودي</span>
        <span class="ctx-tag" onclick="askAbout('اشرح لي كيف تعمل أسواق الأسهم العالمية')">🌐 الأسواق العالمية</span>
        <span class="ctx-tag" onclick="askAbout('ما هي أفضل استراتيجيات التداول اليومي')">📊 استراتيجيات التداول</span>
        <span class="ctx-tag" onclick="askAbout('اشرح لي العملات الرقمية والبلوكشين')">₿ العملات الرقمية</span>
        <span class="ctx-tag" onclick="askAbout('ما هي مؤشرات الركود الاقتصادي')">📉 الاقتصاد الكلي</span>
      </div>

      <div class="messages" id="messages">
        <!-- Welcome shown by JS -->
      </div>

      <div class="disclaimer">
        ⚠️ هذا الوكيل للأغراض التعليمية فقط — لا يُعد نصيحة استثمارية مرخصة
      </div>

      <div class="input-area">
        <div class="input-toolbar">
          <button class="tool-chip active" onclick="toggleTool(this,'analyze')">📊 تحليل السوق</button>
          <button class="tool-chip" onclick="toggleTool(this,'portfolio')">💼 المحفظة</button>
          <button class="tool-chip" onclick="toggleTool(this,'risk')">🛡️ المخاطر</button>
          <button class="tool-chip" onclick="toggleTool(this,'news')">📰 الأخبار</button>
          <button class="tool-chip" onclick="toggleTool(this,'calc')">🔢 الحاسبة</button>
          <button class="tool-chip" onclick="toggleTool(this,'predict')">🔮 التوقعات</button>
        </div>
        <div class="input-box">
          <textarea id="userInput" placeholder="اسألني عن أسهم، محافظ، مخاطر، اقتصاد..." rows="1"
            onkeydown="handleKey(event)" oninput="autoResize(this)"></textarea>
          <button class="send-btn" id="sendBtn" onclick="sendMessage()">
            <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
              <path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/>
            </svg>
          </button>
        </div>
      </div>
    </div>

    <!-- Dashboard View -->
    <div id="view-dashboard" class="dashboard">
      <div>
        <div class="section-title">📊 لوحة التحليل المالي <span class="badge">مباشر</span></div>
        <div class="dash-grid">
          <div class="kpi-card">
            <div class="kpi-label">قيمة المحفظة</div>
            <div class="kpi-value" style="color:var(--accent2)">$128,450</div>
            <div class="kpi-change" style="color:var(--green)">▲ +3.2% هذا الأسبوع</div>
          </div>
          <div class="kpi-card">
            <div class="kpi-label">الأرباح الإجمالية</div>
            <div class="kpi-value" style="color:var(--green)">$24,180</div>
            <div class="kpi-change" style="color:var(--green)">▲ +23.2% منذ البداية</div>
          </div>
          <div class="kpi-card">
            <div class="kpi-label">نسبة المخاطر</div>
            <div class="kpi-value" style="color:var(--amber)">متوسطة</div>
            <div class="kpi-change" style="color:var(--text2)">بيتا: 0.87</div>
          </div>
          <div class="kpi-card">
            <div class="kpi-label">تنبيهات نشطة</div>
            <div class="kpi-value" style="color:var(--purple)">7</div>
            <div class="kpi-change" style="color:var(--red)">3 تحتاج مراجعة</div>
          </div>
        </div>
      </div>

      <div class="chart-row">
        <div class="chart-card">
          <div class="chart-title">أداء المحفظة — 30 يوماً</div>
          <svg class="chart-svg" viewBox="0 0 500 140">
            <defs>
              <linearGradient id="chartGrad" x1="0" y1="0" x2="0" y2="1">
                <stop offset="0%" stop-color="#3b82f6" stop-opacity="0.3"/>
                <stop offset="100%" stop-color="#3b82f6" stop-opacity="0"/>
              </linearGradient>
            </defs>
            <!-- Grid lines -->
            <line x1="0" y1="35" x2="500" y2="35" stroke="rgba(255,255,255,0.05)" stroke-width="1"/>
            <line x1="0" y1="70" x2="500" y2="70" stroke="rgba(255,255,255,0.05)" stroke-width="1"/>
            <line x1="0" y1="105" x2="500" y2="105" stroke="rgba(255,255,255,0.05)" stroke-width="1"/>
            <!-- Area fill -->
            <path d="M0,100 C30,95 60,88 90,80 C120,72 150,68 180,60 C210,52 240,55 270,48 C300,41 330,38 360,30 C390,22 420,18 450,14 C470,10 490,8 500,7 L500,140 L0,140 Z" fill="url(#chartGrad)"/>
            <!-- Line -->
            <path d="M0,100 C30,95 60,88 90,80 C120,72 150,68 180,60 C210,52 240,55 270,48 C300,41 330,38 360,30 C390,22 420,18 450,14 C470,10 490,8 500,7" fill="none" stroke="#3b82f6" stroke-width="2" stroke-linecap="round"/>
            <!-- Dot at end -->
            <circle cx="500" cy="7" r="4" fill="#3b82f6"/>
            <circle cx="500" cy="7" r="7" fill="rgba(59,130,246,0.3)"/>
            <!-- Labels -->
            <text x="5" y="135" font-size="9" fill="#4a5568" font-family="JetBrains Mono">1 يونيو</text>
            <text x="240" y="135" font-size="9" fill="#4a5568" font-family="JetBrains Mono">15 يونيو</text>
            <text x="470" y="135" font-size="9" fill="#4a5568" font-family="JetBrains Mono" text-anchor="end">30 يونيو</text>
          </svg>
        </div>
        <div class="chart-card">
          <div class="chart-title">توزيع الأصول</div>
          <svg viewBox="0 0 120 120" width="120" style="display:block;margin:0 auto">
            <circle cx="60" cy="60" r="45" fill="none" stroke="#3b82f6" stroke-width="18" stroke-dasharray="141 141" stroke-dashoffset="0" transform="rotate(-90 60 60)"/>
            <circle cx="60" cy="60" r="45" fill="none" stroke="#10b981" stroke-width="18" stroke-dasharray="70 212" stroke-dashoffset="-141" transform="rotate(-90 60 60)"/>
            <circle cx="60" cy="60" r="45" fill="none" stroke="#f59e0b" stroke-width="18" stroke-dasharray="42 240" stroke-dashoffset="-211" transform="rotate(-90 60 60)"/>
            <circle cx="60" cy="60" r="45" fill="none" stroke="#8b5cf6" stroke-width="18" stroke-dasharray="30 252" stroke-dashoffset="-253" transform="rotate(-90 60 60)"/>
            <circle cx="60" cy="60" r="30" fill="#141820"/>
          </svg>
          <div class="portfolio-items">
            <div class="port-item">
              <div class="port-dot" style="background:#3b82f6"></div>
              <span class="port-name">أسهم</span>
              <span class="port-pct" style="color:#3b82f6">50%</span>
            </div>
            <div class="port-item">
              <div class="port-dot" style="background:#10b981"></div>
              <span class="port-name">سندات</span>
              <span class="port-pct" style="color:#10b981">25%</span>
            </div>
            <div class="port-item">
              <div class="port-dot" style="background:#f59e0b"></div>
              <span class="port-name">ذهب</span>
              <span class="port-pct" style="color:#f59e0b">15%</span>
            </div>
            <div class="port-item">
              <div class="port-dot" style="background:#8b5cf6"></div>
              <span class="port-name">عملات رقمية</span>
              <span class="port-pct" style="color:#8b5cf6">10%</span>
            </div>
          </div>
        </div>
      </div>

      <div>
        <div class="section-title" style="font-size:14px;margin-bottom:12px">🔔 تنبيهات الوكيل الذكي</div>
        <div class="alert-card" onclick="switchTabByName('chat');askAbout('أخبرني أكثر عن فرصة أرامكو الشرائية')">
          <div class="alert-icon">🟢</div>
          <div class="alert-text">
            <strong>فرصة شراء — أرامكو (2222)</strong>
            <span>الوكيل رصد نقطة دعم قوية عند 29.50 ر.س</span>
          </div>
          <div class="alert-time">منذ 12 د</div>
        </div>
        <div class="alert-card" onclick="switchTabByName('chat');askAbout('ما هو تأثير قرار الفيدرالي على محفظتي')">
          <div class="alert-icon">🔴</div>
          <div class="alert-text">
            <strong>خطر — قرار الفيدرالي قادم</strong>
            <span>تقرير الفائدة الأمريكية اليوم الساعة 9م</span>
          </div>
          <div class="alert-time">منذ 45 د</div>
        </div>
        <div class="alert-card" onclick="switchTabByName('chat');askAbout('اشرح أهمية إعادة التوازن في المحفظة الاستثمارية')">
          <div class="alert-icon">🟡</div>
          <div class="alert-text">
            <strong>تنبيه توازن المحفظة</strong>
            <span>حصة الأسهم تجاوزت الحد المستهدف بـ 5%</span>
          </div>
          <div class="alert-time">منذ 2 س</div>
        </div>
      </div>
    </div>

    <!-- Agents View -->
    <div id="view-agents" class="agents-view">
      <div class="section-title">🤖 الوكلاء الماليون المتخصصون <span class="badge">6 وكلاء</span></div>
      <div class="agents-grid">
        <div class="agent-card a1" onclick="switchTabByName('chat');askAbout('أنت وكيل تحليل السوق. قدم لي تحليلاً شاملاً للسوق السعودي اليوم')">
          <div class="agent-icon">📈</div>
          <div class="agent-name">وكيل تحليل السوق</div>
          <div class="agent-desc">يتابع حركة الأسواق ويحلل الاتجاهات والفرص والمخاطر في الوقت الفعلي.</div>
          <div class="agent-status"><div class="agent-status-dot"></div> نشط — يراقب 47 سهم</div>
        </div>
        <div class="agent-card a2" onclick="switchTabByName('chat');askAbout('أنت وكيل المحفظة الذكية. قيّم محفظتي الحالية وقدم توصيات التحسين')">
          <div class="agent-icon">💼</div>
          <div class="agent-name">وكيل المحفظة الذكية</div>
          <div class="agent-desc">يدير ويوازن المحافظ الاستثمارية تلقائياً بناءً على أهدافك وتحملك للمخاطر.</div>
          <div class="agent-status"><div class="agent-status-dot"></div> نشط — 4 محافظ تحت الإدارة</div>
        </div>
        <div class="agent-card a3" onclick="switchTabByName('chat');askAbout('أنت وكيل إدارة المخاطر. قيّم مخاطر محفظتي الاستثمارية')">
          <div class="agent-icon">🛡️</div>
          <div class="agent-name">وكيل إدارة المخاطر</div>
          <div class="agent-desc">يحسب VaR والانحراف المعياري ويطبق استراتيجيات التحوط لحماية رأس المال.</div>
          <div class="agent-status"><div class="agent-status-dot"></div> نشط — مراقبة 24/7</div>
        </div>
        <div class="agent-card a4" onclick="switchTabByName('chat');askAbout('أنت وكيل الأخبار المالية. قدم ملخصاً للأخبار الاقتصادية المؤثرة اليوم')">
          <div class="agent-icon">📰</div>
          <div class="agent-name">وكيل الأخبار المالية</div>
          <div class="agent-desc">يجمع ويحلل الأخبار الاقتصادية العالمية ويقيّم تأثيرها على أصولك.</div>
          <div class="agent-status"><div class="agent-status-dot"></div> نشط — 230 مصدر مراقب</div>
        </div>
        <div class="agent-card a5" onclick="switchTabByName('chat');askAbout('أنت وكيل التوقعات. استخدم الذكاء الاصطناعي لتوقع حركة سهم أرامكو خلال الأسبوع القادم')">
          <div class="agent-icon">🔮</div>
          <div class="agent-name">وكيل التوقعات الذكية</div>
          <div class="agent-desc">يستخدم نماذج ML لتوقع حركات الأسعار وتحديد نقاط الدخول والخروج المثلى.</div>
          <div class="agent-status"><div class="agent-status-dot"></div> نشط — دقة 78% تاريخية</div>
        </div>
        <div class="agent-card a6" onclick="switchTabByName('chat');askAbout('أنت المستشار المالي الشخصي. أنا 30 سنة ولدي 100,000 ريال للاستثمار. ما هي خطتي المثلى؟')">
          <div class="agent-icon">👨‍💼</div>
          <div class="agent-name">المستشار المالي الشخصي</div>
          <div class="agent-desc">يبني خطط مالية مخصصة للأهداف الشخصية كالتقاعد والتعليم والثروة.</div>
          <div class="agent-status"><div class="agent-status-dot"></div> نشط — متاح للاستشارة</div>
        </div>
      </div>
      <div style="margin-top:8px;padding:16px 20px;background:var(--panel);border:1px solid var(--border);border-radius:12px;font-size:13px;color:var(--text2);line-height:1.7">
        💡 <strong style="color:var(--text)">كيف تعمل الوكلاء معاً؟</strong><br>
        عند إرسال استفسار، يتعاون وكيل الأخبار + وكيل السوق + وكيل المخاطر معاً لتقديم إجابة شاملة ومتكاملة. اضغط على أي وكيل لبدء محادثة مخصصة معه.
      </div>
    </div>

  </div>
</div>

<script>
// ===== STATE =====
const conversationHistory = [];
let isLoading = false;
let activeTools = ['analyze'];

// ===== INIT =====
window.addEventListener('load', () => {
  setTimeout(() => {
    const loading = document.getElementById('loading');
    loading.style.opacity = '0';
    setTimeout(() => loading.style.display = 'none', 500);
    showWelcome();
  }, 1800);
});

function showWelcome() {
  const messages = document.getElementById('messages');
  messages.innerHTML = `
    <div class="welcome" id="welcomeScreen">
      <div class="welcome-icon">🤖</div>
      <h2>مرحباً بك في FinAgent AI</h2>
      <p>وكيلك المالي الذكي المدعوم بالذكاء الاصطناعي. اسألني عن أي موضوع مالي — تحليل أسهم، إدارة محافظ، استراتيجيات استثمار، أو الاقتصاد الكلي.</p>
      <div class="suggestions-grid">
        <div class="suggestion-card" onclick="askAbout(this.querySelector('.s-main').textContent)">
          <span class="s-icon">📊</span>
          <span class="s-main">حلل لي سهم أرامكو وهل هو فرصة شراء الآن</span>
          <span class="s-text">تحليل تقني وأساسي متكامل</span>
        </div>
        <div class="suggestion-card" onclick="askAbout(this.querySelector('.s-main').textContent)">
          <span class="s-icon">💼</span>
          <span class="s-main">كيف أبني محفظة استثمارية متوازنة برأس مال 50,000 ريال</span>
          <span class="s-text">خطة استثمارية مخصصة</span>
        </div>
        <div class="suggestion-card" onclick="askAbout(this.querySelector('.s-main').textContent)">
          <span class="s-icon">🌍</span>
          <span class="s-main">ما تأثير رفع الفائدة الأمريكية على الأسواق الناشئة</span>
          <span class="s-text">تحليل اقتصاد كلي</span>
        </div>
        <div class="suggestion-card" onclick="askAbout(this.querySelector('.s-main').textContent)">
          <span class="s-icon">₿</span>
          <span class="s-main">قارن بين الاستثمار في البيتكوين والذهب على المدى الطويل</span>
          <span class="s-text">مقارنة أصول استثمارية</span>
        </div>
      </div>
    </div>`;
}

// ===== TAB SWITCHING =====
function switchTab(name, btn) {
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  document.getElementById('view-chat').style.display = name === 'chat' ? 'flex' : 'none';
  const dash = document.getElementById('view-dashboard');
  const agents = document.getElementById('view-agents');
  dash.classList.toggle('active', name === 'dashboard');
  agents.classList.toggle('active', name === 'agents');
}

function switchTabByName(name) {
  const btns = document.querySelectorAll('.tab-btn');
  const names = ['chat','dashboard','agents'];
  switchTab(name, btns[names.indexOf(name)]);
}

// ===== TOOLS =====
function toggleTool(el, tool) {
  el.classList.toggle('active');
  if (el.classList.contains('active')) activeTools.push(tool);
  else activeTools = activeTools.filter(t => t !== tool);
}

// ===== INPUT =====
function autoResize(el) {
  el.style.height = '50px';
  el.style.height = Math.min(el.scrollHeight, 120) + 'px';
}

function handleKey(e) {
  if (e.key === 'Enter' && !e.shiftKey) {
    e.preventDefault();
    sendMessage();
  }
}

// ===== SEND MESSAGE =====
function askAbout(text) {
  switchTabByName('chat');
  document.getElementById('userInput').value = text;
  sendMessage();
}

async function sendMessage() {
  const input = document.getElementById('userInput');
  const text = input.value.trim();
  if (!text || isLoading) return;

  // Remove welcome
  const welcome = document.getElementById('welcomeScreen');
  if (welcome) welcome.remove();

  isLoading = true;
  input.value = '';
  input.style.height = '50px';
  document.getElementById('sendBtn').disabled = true;

  // Add user message
  addMessage('user', text);
  conversationHistory.push({ role: 'user', content: text });

  // Add thinking
  const thinkingId = addThinking();

  // Build system prompt
  const toolsContext = activeTools.join(', ');
  const systemPrompt = `أنت FinAgent AI، وكيل مالي ذكي متخصص ومحترف يتحدث العربية بطلاقة تامة.

أدواتك النشطة حالياً: ${toolsContext}

تعمل كـ:
1. محلل أسواق متخصص بالأسواق العربية والخليجية والعالمية
2. مستشار محافظ استثمارية (أسهم، سندات، ETFs، عقارات، عملات رقمية)
3. خبير في إدارة المخاطر المالية (VaR، تحوط، تنويع)
4. محلل اقتصاد كلي (سياسة نقدية، تضخم، نمو)
5. مستشار مالي شخصي (تخطيط تقاعد، ثروة، ادخار)

أسلوبك:
- دقيق ومهني في المعلومات المالية
- تستخدم أرقاماً ومؤشرات حقيقية ومعقولة
- تُقدم آراءً تحليلية واضحة (شراء/بيع/انتظار)
- تُنبه دائماً أن المعلومات تعليمية وليست نصيحة استثمارية مرخصة
- تُنسّق ردودك بشكل واضح مع فقرات وعناوين فرعية ونقاط مرقمة
- تُقدم بيانات في جداول عند الإمكان
- ردودك شاملة وتتراوح بين 150-400 كلمة
- تُكمل دائماً بخلاصة قابلة للتطبيق

السوق الافتراضي المرجعي: السوق السعودي (تداول) + الأسواق العالمية.
التاريخ الحالي: ${new Date().toLocaleDateString('ar-SA', {year:'numeric',month:'long',day:'numeric'})}.`;

  try {
    const response = await fetch('https://api.anthropic.com/v1/messages', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        model: 'claude-sonnet-4-20250514',
        max_tokens: 1000,
        system: systemPrompt,
        messages: conversationHistory
      })
    });

    const data = await response.json();
    removeThinking(thinkingId);

    if (data.content && data.content[0]) {
      const reply = data.content[0].text;
      conversationHistory.push({ role: 'assistant', content: reply });
      addMessage('assistant', reply);
    } else {
      addMessage('assistant', 'عذراً، حدث خطأ في الاتصال. يرجى المحاولة مرة أخرى.');
    }
  } catch (err) {
    removeThinking(thinkingId);
    addMessage('assistant', '⚠️ تعذّر الاتصال بالوكيل. تحقق من الاتصال وحاول مجدداً.');
  }

  isLoading = false;
  document.getElementById('sendBtn').disabled = false;
}

// ===== MESSAGE HELPERS =====
function addMessage(role, text) {
  const messages = document.getElementById('messages');
  const div = document.createElement('div');
  div.className = `message ${role}`;

  const now = new Date().toLocaleTimeString('ar-SA', { hour: '2-digit', minute: '2-digit' });

  if (role === 'assistant') {
    div.innerHTML = `
      <div class="msg-avatar ai-avatar">🤖</div>
      <div class="msg-content">
        <div class="msg-bubble ai-bubble">${formatMessage(text)}</div>
        <div class="msg-time">${now} · FinAgent AI</div>
      </div>`;
  } else {
    div.innerHTML = `
      <div class="msg-avatar user-avatar">👤</div>
      <div class="msg-content">
        <div class="msg-bubble user-bubble">${escapeHtml(text)}</div>
        <div class="msg-time">${now}</div>
      </div>`;
  }

  messages.appendChild(div);
  messages.scrollTop = messages.scrollHeight;
}

function formatMessage(text) {
  // Convert markdown-like to HTML
  let html = escapeHtml(text);
  // Bold
  html = html.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
  // Headers
  html = html.replace(/^### (.*$)/gm, '<h4 style="color:var(--accent2);font-size:13px;margin:10px 0 4px">$1</h4>');
  html = html.replace(/^## (.*$)/gm, '<h3 style="color:var(--accent2);font-size:14px;margin:12px 0 6px">$1</h3>');
  // Bullets
  html = html.replace(/^[\-•] (.*$)/gm, '<li style="margin:3px 0;padding-right:4px">$1</li>');
  html = html.replace(/(<li.*<\/li>\n?)+/g, '<ul style="padding-right:16px;margin:8px 0">$&</ul>');
  // Numbered
  html = html.replace(/^\d+\. (.*$)/gm, '<li style="margin:3px 0">$1</li>');
  // Line breaks
  html = html.replace(/\n\n/g, '<br><br>');
  html = html.replace(/\n/g, '<br>');
  return html;
}

function escapeHtml(text) {
  return text
    .replace(/&/g,'&amp;')
    .replace(/</g,'&lt;')
    .replace(/>/g,'&gt;')
    .replace(/"/g,'&quot;');
}

let thinkingCounter = 0;
function addThinking() {
  const id = 'thinking-' + (++thinkingCounter);
  const messages = document.getElementById('messages');
  const div = document.createElement('div');
  div.className = 'message';
  div.id = id;
  div.innerHTML = `
    <div class="msg-avatar ai-avatar">🤖</div>
    <div class="msg-content">
      <div class="thinking">
        <div class="thinking-dots"><span></span><span></span><span></span></div>
        الوكيل يحلل استفسارك...
      </div>
    </div>`;
  messages.appendChild(div);
  messages.scrollTop = messages.scrollHeight;
  return id;
}

function removeThinking(id) {
  const el = document.getElementById(id);
  if (el) el.remove();
}
</script>
</body>
</html>
