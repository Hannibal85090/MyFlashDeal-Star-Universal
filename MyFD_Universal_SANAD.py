import streamlit as st
import time

# 1. نظام اللغات المتعددة (عربي، إنجليزي، إيطالي، فرنسي)
LANG_DICT = {
    'Arabic': {
        'title': "نجم فلاش ديل العالمي 🌟",
        'agent': "الوكيل الذكي (تحدث. ادفع. تم.)",
        'saden': "أمان سادن: التوكن المتبادل",
        'home_car': "التحكم الذكي (المنزل والسيارة) 🏠🚗",
        'product': "سماعات الرأس (إصدار النجم)",
        'buy': "إبرام الصفقة العالمية 🚀",
        'success': "تمت العملية بنجاح! مبروك شريكي",
        'input_label': "اكتب أمرك هنا...",
        'voice_btn': "ابدأ التحدث 🎤",
        'sign_btn': "تفعيل كاميرا الإشارة 👋",
        'sync_btn': "مزامنة التوكن وربط الـ SIM 🛡️",
        'car_btn': "تشغيل السيارة عن بعد 🔑",
        'home_btn': "إدارة المنزل الذكي 🏠",
        'motto': "تحدث. ادفع. تم."
    },
    'English': {
        'title': "My FlashDeal Star Universal 🌟",
        'agent': "Smart Agent (Talk. Pay. Done.)",
        'saden': "Saden Security: Mutual Token",
        'home_car': "Smart Control (Home & Car) 🏠🚗",
        'product': "Headphones (Star Edition)",
        'buy': "Global Deal Execution 🚀",
        'success': "Process Completed Successfully!",
        'input_label': "Type your command here...",
        'voice_btn': "Start Listening 🎤",
        'sign_btn': "Activate Sign Camera 👋",
        'sync_btn': "Sync Token & Link SIM 🛡️",
        'car_btn': "Start Car Remote 🔑",
        'home_btn': "Manage Smart Home 🏠",
        'motto': "Talk. Pay. Done."
    },
    'Italiano': {
        'title': "Il Mio FlashDeal Star Universale 🌟",
        'agent': "Agente Intelligente",
        'saden': "Sicurezza Saden: Token Reciproco",
        'home_car': "Controllo Intelligente (Casa e Auto) 🏠🚗",
        'product': "Cuffie (Edizione Star)",
        'buy': "Concludi l'Affare 🚀",
        'success': "Operazione completata con successo!",
        'input_label': "Scrivi il tuo comando...",
        'voice_btn': "Inizia ad ascoltare 🎤",
        'sign_btn': "Attiva telecamera gestuale 👋",
        'sync_btn': "Sincronizza Token e SIM 🛡️",
        'car_btn': "Avvia Auto a distanza 🔑",
        'home_btn': "Gestisci Casa Intelligente 🏠",
        'motto': "Parla. Paga. Fatto."
    },
    'Français': {
        'title': "Mon FlashDeal Star Universel 🌟",
        'agent': "Agent Intelligent",
        'saden': "Sécurité Saden: Token Mutuel",
        'home_car': "Contrôle Intelligent (Maison & Voiture) 🏠🚗",
        'product': "Casque (Édition Star)",
        'buy': "Conclure l'Accord 🚀",
        'success': "Opération terminée avec succès!",
        'input_label': "Écrivez votre commande...",
        'voice_btn': "Commencer l'écoute 🎤",
        'sign_btn': "Activer caméra gestuelle 👋",
        'sync_btn': "Synchroniser Token et SIM 🛡️",
        'car_btn': "Démarrer voiture à distance 🔑",
        'home_btn': "Gérer Maison Intelligente 🏠",
        'motto': "Parlez. Payez. Fait."
    }
}

st.set_page_config(page_title="FlashDeal Star", layout="wide")

with st.sidebar:
    selected_lang = st.selectbox("🌐 Choose Language | اختر اللغة", list(LANG_DICT.keys()))
    t = LANG_DICT[selected_lang]
    st.divider()
    st.markdown(f"**Slogan:** `{t['motto']}`")

st.title(t['title'])
st.write(f"### 🤖 {t['agent']}")

# --- قسم التفاعل الشفاف (صوت، إشارة، كتابة) ---
tab1, tab2, tab3, tab4 = st.tabs(["⌨️ Text", "🎤 Voice", "👋 Sign", "🏠 Smart Hub"])

with tab1:
    user_text = st.text_input(t['input_label'])
    if user_text:
        st.write(f"💬 **Agent:** {user_text} ... Processing")

with tab2:
    if st.button(t['voice_btn']):
        with st.spinner("Listening..."):
            time.sleep(1.5)
            st.success("✅ Voice Match Confirmed")

with tab3:
    if st.button(t['sign_btn']):
        st.info("👋 Camera Active: Analyzing Gestures...")
        time.sleep(1.5)
        st.success("✅ Gesture Approved")

with tab4:
    st.markdown(f"### {t['home_car']}")
    c1, c2 = st.columns(2)
    with c1:
        if st.button(t['car_btn']):
            with st.status("Linking to My FlashDeal Star Device..."):
                time.sleep(1)
                st.write("SIM Card Verified...")
                time.sleep(1)
                st.success("🚗 Engine Started! | تم تشغيل المحرك")
    with c2:
        if st.button(t['home_btn']):
            st.toast("🏠 Home Lights & AC Adjusted")
            st.write("✅ Smart Home Connected")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"### 🛡️ {t['saden']}")
    st.markdown("<h1 style='text-align: center;'>🛡️</h1>", unsafe_allow_html=True)
    if st.button(t['sync_btn']):
        with st.status("Verifying Multi-Layer Security..."):
            time.sleep(1)
            st.write("Biometrics Checked...")
            time.sleep(1)
            st.success("✅ Secure Token Synchronized")

with col2:
    st.markdown(f"### 🎧 {t['product']}")
    st.markdown("<h1 style='text-align: center;'>🎧</h1>", unsafe_allow_html=True)
    st.markdown("## **$99.99**")
    
    if st.button(t['buy'], type="primary", use_container_width=True):
        st.balloons()
        with st.container(border=True):
            st.success(f"🏆 {t['success']}")
            st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
            st.info(f"Certificate issued to SIM: **FD-STAR-2026**")
