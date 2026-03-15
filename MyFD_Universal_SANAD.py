import streamlit as st
import time

# 1. إعدادات اللغات (تعدد اللغات الفوري)
LANG_DICT = {
    'Arabic': {
        'title': "نجم فلاش ديل العالمي 🌟",
        'agent': "الوكيل الذكي متعدد الأنماط",
        'modes': "🎤 صوت | 👋 إشارة | ⌨️ كتابة",
        'saden': "أمان سادن - السند القوي",
        'product': "سماعات الرأس اللاسلكية (Star Edition)",
        'buy': "إبرام الصفقة العالمية 🚀",
        'success': "تمت العملية بنجاح! مبروك شريكي",
        'motto': "تحدث. ادفع. تم. | Talk. Pay. Done.",
        'music': "🎶 موسيقى النجاح الهادئة تعمل الآن"
    },
    'English': {
        'title': "My FlashDeal Star Universal 🌟",
        'agent': "Smart Multimodal Agent",
        'modes': "🎤 Voice | 👋 Sign | ⌨️ Text",
        'saden': "Saden Security - Strong Support",
        'product': "Wireless Headphones (Star Edition)",
        'buy': "Global Deal Execution 🚀",
        'success': "Process Completed Successfully!",
        'motto': "Talk. Pay. Done.",
        'music': "🎶 Calm Success Music is playing"
    },
    'Italiano': {
        'title': "Il Mio FlashDeal Star Universale 🌟",
        'agent': "Agente Multimodale Intelligente",
        'modes': "🎤 Voce | 👋 Segno | ⌨️ Testo",
        'saden': "Sicurezza Saden - Supporto Forte",
        'product': "Cuffie Wireless (Edizione Star)",
        'buy': "Concluire l'Affare 🚀",
        'success': "Operazione completata!",
        'motto': "Parla. Paga. Fatto.",
        'music': "🎶 Musica di successo in corso"
    },
    'Français': {
        'title': "Mon FlashDeal Star Universel 🌟",
        'agent': "Agent Multimodal Intelligent",
        'modes': "🎤 Voix | 👋 Signe | ⌨️ Texte",
        'saden': "Sécurité Saden - Support Fort",
        'product': "Casque Sans Fil (Édition Star)",
        'buy': "Conclure l'Accord 🚀",
        'success': "Opération réussie!",
        'motto': "Parlez. Payez. Fait.",
        'music': "🎶 Musique de réussite activée"
    }
}

# 2. بناء الواجهة (الوضاحة والشفافية)
st.set_page_config(page_title="FlashDeal Star", layout="wide")

# اختيار اللغة من الشريط الجانبي ليكون تفاعلياً
with st.sidebar:
    st.markdown("### 🌐 Language | اللغة")
    selected_lang = st.selectbox("", list(LANG_DICT.keys()))
    t = LANG_DICT[selected_lang]

# 3. الهيدر (الوكيل الذكي)
st.title(t['title'])
st.subheader(f"🤖 {t['agent']}")
st.info(t['modes'])

st.divider()

# 4. الجسم الأساسي (الأمان والمنتج بدون صور خارجية)
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown(f"### 🛡️ {t['saden']}")
    # استخدام رمز تعبيري ضخم بدلاً من صورة الدرع لضمان النجاح
    st.markdown("<h1 style='text-align: center; font-size: 100px;'>🛡️</h1>", unsafe_allow_html=True)
    st.success("✅ Mutual Token: Synchronized")

with col2:
    st.markdown(f"### 🎧 {t['product']}")
    # استخدام أيقونة للسماعات لتجنب خطأ الـ "0"
    st.markdown("<h1 style='text-align: center; font-size: 100px;'>🎧</h1>", unsafe_allow_html=True)
    st.markdown("## **$99.99**")
    
    if st.button(t['buy'], type="primary", use_container_width=True):
        # 5. الاحتفالية وشهادة النجاح
        st.balloons()
        with st.container(border=True):
            st.success(f"🏆 {t['success']}")
            st.markdown(f"### {t['motto']}")
            st.write("---")
            st.write(t['music'])
            # موسيقى هادئة افتراضية
            st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
            
            # محاكاة ذكاء الوكيل
            with st.status("FlashDeal Star Processing...", expanded=True):
                st.write("Verifying Global Biometrics...")
                time.sleep(1)
                st.write("Confirming Talk. Pay. Done. Protocol...")
                time.sleep(1)
                st.write("Transaction Verified by Saden Security.")

st.divider()
st.markdown(f"<p style='text-align: center; opacity: 0.5;'>FlashDeal Universal - {selected_lang}</p>", unsafe_allow_html=True)
