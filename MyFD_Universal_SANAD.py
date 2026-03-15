import streamlit as st
import time

# 1. نظام اللغات المتعددة (عربي، إنجليزي، إيطالي، فرنسي)
LANG_DICT = {
    'Arabic': {
        'title': "نجم فلاش ديل العالمي",
        'agent': "الوكيل الذكي (تحدث. ادفع. تم.)",
        'modes': "🎤 صوت | 👋 إشارة | ⌨️ كتابة",
        'saden': "أمان سادن: السند القوي",
        'product': "سماعات الرأس اللاسلكية (Star Edition)",
        'buy': "إبرام الصفقة العالمية",
        'success': "تمت العملية بنجاح! مبروك شريكي",
        'cert': "شهادة نجاح الصفقة الرقمية",
        'motto': "Talk. Pay. Done.",
        'music': "تشغيل موسيقى النجاح الهادئة"
    },
    'English': {
        'title': "My FlashDeal Star Universal",
        'agent': "Smart Agent (Talk. Pay. Done.)",
        'modes': "🎤 Voice | 👋 Sign | ⌨️ Text",
        'saden': "Saden Security: Strong Support",
        'product': "Wireless Headphones (Star Edition)",
        'buy': "Global Deal Execution",
        'success': "Process Completed Successfully!",
        'cert': "Digital Success Certificate",
        'motto': "Talk. Pay. Done.",
        'music': "Play Calm Success Music"
    },
    'Italiano': {
        'title': "Il Mio FlashDeal Star Universale",
        'agent': "Agente Intelligente",
        'modes': "🎤 Voce | 👋 Segno | ⌨️ Testo",
        'saden': "Sicurezza Saden: Supporto Forte",
        'product': "Cuffie Wireless (Edizione Star)",
        'buy': "Concludi l'Affare Globale",
        'success': "Operazione Completata con Successo!",
        'cert': "Certificato di Successo",
        'motto': "Parla. Paga. Fatto.",
        'music': "Riproduci Musica"
    },
    'Français': {
        'title': "Mon FlashDeal Star Universel",
        'agent': "Agent Intelligent",
        'modes': "🎤 Voix | 👋 Signe | ⌨️ Texte",
        'saden': "Sécurité Saden: Support Fort",
        'product': "Casque Sans Fil (Édition Star)",
        'buy': "Conclure l'Accord Mondial",
        'success': "Opération Terminée avec Succès!",
        'cert': "Certificat de Réussite",
        'motto': "Parlez. Payez. Fait.",
        'music': "Jouer de la Musique"
    }
}

# 2. إعداد الواجهة الشفافة والوضاحة
st.set_page_config(page_title="FlashDeal Star", layout="wide")

with st.sidebar:
    st.markdown("### 🌐 Select Language | اختر اللغة")
    selected_lang = st.selectbox("", list(LANG_DICT.keys()))
    t = LANG_DICT[selected_lang]

# 3. الهيكل الأساسي (الوكيل الذكي)
st.title(f"✨ {t['title']}")
st.subheader(f"🤖 {t['agent']}")
st.markdown(f"### `{t['modes']}`")

st.divider()

# 4. قسم المنتج والأمان (استبدال الدرع بأيقونة قياسية لسرعة التنزيل)
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown(f"### 🛡️ {t['saden']}")
    # استخدام أيقونة Emoji بدلاً من ملف صورة لضمان الظهور الفوري
    st.markdown("<h1 style='text-align: center; font-size: 100px;'>🛡️</h1>", unsafe_allow_html=True)
    st.success("✅ Mutual Token: Synchronized")
    st.info("🔗 SIM & Car Device Linked")

with col2:
    st.markdown(f"### 🎧 {t['product']}")
    # محاولة عرض صورة المنتج من المجلد، وإذا فشلت نضع أيقونة
    try:
        st.image("assets/images/headphones_small.png", width=250)
    except:
        st.markdown("<h1 style='text-align: center; font-size: 100px;'>🎧</h1>", unsafe_allow_html=True)
    
    st.markdown("## **$99.99**")
    if st.button(f"🚀 {t['buy']}", type="primary", use_container_width=True):
        # 5. الاحتفالية وشهادة النجاح
        st.balloons()
        
        with st.container(border=True):
            st.success(f"### 🏆 {t['success']}")
            st.markdown(f"## **{t['motto']}**")
            st.write(f"📜 {t['cert']}")
            st.write("---")
            st.write(f"🎼 {t['music']}")
            # تشغيل الموسيقى الهادئة
            st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
            
            # محاكاة ذكاء الوكيل في معالجة الإشارة والصوت
            with st.status("FlashDeal Star Agent Processing...", expanded=True):
                st.write("Verifying Sign Language Input...")
                time.sleep(1)
                st.write("Confirming Global Payment via Mutual Token...")
                time.sleep(1)
                st.write("Transaction Secured by Saden.")

st.divider()
st.markdown(f"<p style='text-align: center; opacity: 0.5;'>FlashDeal - Universal Protocol - {selected_lang}</p>", unsafe_allow_html=True)
