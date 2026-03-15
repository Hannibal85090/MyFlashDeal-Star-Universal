import streamlit as st
import time

# 1. نظام اللغات المتعددة المبدع
LANG_DICT = {
    'Arabic': {
        'title': "نجم فلاش ديل العالمي 🌟",
        'agent': "الوكيل الذكي (تحدث. ادفع. تم.)",
        'modes': "🎤 صوت | 👋 إشارة | ⌨️ كتابة",
        'saden': "أمان سادن: السند القوي",
        'product': "سماعات الرأس اللاسلكية (إصدار النجم)",
        'buy': "إبرام الصفقة العالمية 🚀",
        'success': "تمت العملية بنجاح! مبروك شريكي",
        'motto': "Talk. Pay. Done.",
        'music': "🎶 موسيقى النجاح الهادئة تعمل الآن"
    },
    'English': {
        'title': "My FlashDeal Star Universal 🌟",
        'agent': "Smart Agent (Talk. Pay. Done.)",
        'modes': "🎤 Voice | 👋 Sign | ⌨️ Text",
        'saden': "Saden Security: Strong Support",
        'product': "Wireless Headphones (Star Edition)",
        'buy': "Global Deal Execution 🚀",
        'success': "Process Completed Successfully!",
        'motto': "Talk. Pay. Done.",
        'music': "🎶 Calm Success Music is playing"
    },
    'Italiano': {
        'title': "Il Mio FlashDeal Star Universale 🌟",
        'agent': "Agente Intelligente",
        'modes': "🎤 Voce | 👋 Segno | ⌨️ Testo",
        'saden': "Sicurezza Saden: Supporto Forte",
        'product': "Cuffie Wireless (Edizione Star)",
        'buy': "Conclui l'Affare 🚀",
        'success': "Operazione completata!",
        'motto': "Parla. Paga. Fatto.",
        'music': "🎶 Musica di successo"
    },
    'Français': {
        'title': "Mon FlashDeal Star Universel 🌟",
        'agent': "Agent Intelligent",
        'modes': "🎤 Voix | 👋 Signe | ⌨️ Texte",
        'saden': "Sécurité Saden: Support Fort",
        'product': "Casque Sans Fil (Édition Star)",
        'buy': "Conclure l'Accord 🚀",
        'success': "Opération réussie!",
        'motto': "Parlez. Payez. Fait.",
        'music': "🎶 Musique de réussite"
    }
}

st.set_page_config(page_title="FlashDeal Star", layout="wide")

with st.sidebar:
    selected_lang = st.selectbox("🌐 Select Language | اختر اللغة", list(LANG_DICT.keys()))
    t = LANG_DICT[selected_lang]

st.title(t['title'])
st.subheader(f"🤖 {t['agent']}")
st.info(t['modes'])

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"### 🛡️ {t['saden']}")
    st.markdown("<h1 style='text-align: center; font-size: 100px;'>🛡️</h1>", unsafe_allow_html=True)
    st.success("✅ Mutual Token: Synchronized")

with col2:
    st.markdown(f"### 🎧 {t['product']}")
    st.markdown("<h1 style='text-align: center; font-size: 100px;'>🎧</h1>", unsafe_allow_html=True)
    st.markdown("## **$99.99**")
    
    if st.button(t['buy'], type="primary", use_container_width=True):
        st.balloons()
        with st.container(border=True):
            st.success(f"🏆 {t['success']}")
            st.markdown(f"### {t['motto']}")
            st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
            with st.status("FlashDeal Star Agent Processing...", expanded=True):
                st.write("Verifying Global Biometrics...")
                time.sleep(1)
                st.write("Transaction Verified by Saden Security.")
