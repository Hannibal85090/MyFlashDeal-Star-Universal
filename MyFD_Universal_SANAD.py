import streamlit as st
import time

# 1. إعدادات الصفحة واللغات (العربية، الإنجليزية، الإيطالية، الفرنسية)
LANG_DICT = {
    'Arabic': {
        'title': "نجم فلاش ديل العالمي",
        'agent': "الوكيل الذكي متعدد الأنماط",
        'modes': "صوت | إشارة | كتابة",
        'saden': "أمان سادن - السند القوي",
        'product': "سماعات الرأس اللاسلكية (إصدار النجم)",
        'buy': "إبرام الصفقة العالمية",
        'success': "تمت العملية بنجاح!",
        'cert': "شهادة نجاح الصفقة",
        'motto': "تحدث. ادفع. تم.",
        'music': "تشغيل موسيقى النجاح الهادئة"
    },
    'English': {
        'title': "My FlashDeal Star Universal",
        'agent': "Smart Multimodal Agent",
        'modes': "Voice | Sign | Text",
        'saden': "Saden Security - Strong Support",
        'product': "Wireless Headphones (Star Edition)",
        'buy': "Global Deal Execution",
        'success': "Process Completed Successfully!",
        'cert': "Success Certificate",
        'motto': "Talk. Pay. Done.",
        'music': "Play Calm Success Music"
    },
    'Italiano': {
        'title': "Il Mio FlashDeal Star Universale",
        'agent': "Agente Multimodale Intelligente",
        'modes': "Voce | Segno | Testo",
        'saden': "Sicurezza Saden - Supporto Forte",
        'product': "Cuffie Wireless (Edizione Star)",
        'buy': "Concludi l'Affare Globale",
        'success': "Operazione Completata con Successo!",
        'cert': "Certificato di Successo",
        'motto': "Parla. Paga. Fatto.",
        'music': "Riproduci Musica di Successo"
    },
    'Français': {
        'title': "Mon FlashDeal Star Universel",
        'agent': "Agent Multimodal Intelligent",
        'modes': "Voix | Signe | Texte",
        'saden': "Sécurité Saden - Support Fort",
        'product': "Casque Sans Fil (Édition Star)",
        'buy': "Conclure l'Accord Mondial",
        'success': "Opération Terminée avec Succès!",
        'cert': "Certificat de Réussite",
        'motto': "Parlez. Payez. Fait.",
        'music': "Jouer de la Musique de Réussite"
    }
}

# 2. واجهة المستخدم والتصميم الشفاف
st.set_page_config(page_title="FlashDeal Star", layout="wide")

# اختيار اللغة من الشريط الجانبي
with st.sidebar:
    st.markdown("### 🌐 Select Language | اختر اللغة")
    selected_lang = st.selectbox("", list(LANG_DICT.keys()))
    t = LANG_DICT[selected_lang]

# 3. الهيدر (الوكيل الذكي والشفافية)
st.title(f"✨ {t['title']}")
st.subheader(f"🤖 {t['agent']}")
st.info(f"⚡ {t['modes']}")

st.divider()

# 4. قسم أمان سادن والمنتج (تجاوز خطأ الصفر)
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown(f"### 🛡️ {t['saden']}")
    # استدعاء الدرع من المجلد الذي أريتني إياه
    st.image("assets/images/bahrain_shield.png", width=200, use_container_width=False)
    st.write("✅ **Mutual Token: Synchronized**")

with col2:
    st.markdown(f"### 🎧 {t['product']}")
    # حل مشكلة الصفر: التأكد من المسار الصحيح لصورة المنتج
    try:
        st.image("assets/images/headphones_small.png", width=250)
    except:
        st.write("📦 [Image: Headphones Star Edition]")
    
    st.markdown("## **$99.99**")
    if st.button(f"🚀 {t['buy']}", type="primary"):
        # 5. الاحتفالية (بالونات، موسيقى، وشهادة)
        st.balloons()
        st.toast(t['success'])
        
        with st.container(border=True):
            st.success(f"### 🏆 {t['cert']}")
            st.write(f"**{t['motto']}**")
            st.write("---")
            st.write(f"🎼 {t['music']}")
            # تشغيل صوت هادئ (رابط افتراضي لموسيقى هادئة)
            st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
            
            # محاكاة التفاعل مع لغة الإشارة والكتابة
            with st.status("FlashDeal Agent Processing...", expanded=True):
                st.write("Analyzing Sign Language cues...")
                time.sleep(1)
                st.write("Verifying Biometric Tokens...")
                time.sleep(1)
                st.write("Deal Secured!")

# 6. التذييل الشفاف
st.divider()
st.markdown(f"<p style='text-align: center; opacity: 0.6;'>FlashDeal Star - Universal Protocol - {selected_lang}</p>", unsafe_allow_html=True)
