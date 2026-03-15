import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="FlashDeal Star - Secure Login", layout="centered")

st.title("⭐ FlashDeal Star - Secure Login")

# اختيار اللغة
languages = {
    "English": "🇬🇧",
    "عربي": "🇦🇪",
    "Français": "🇫🇷",
    "Italiano": "🇮🇹"
}
lang_choice = st.radio("اختر اللغة / Choose Language:", list(languages.keys()), horizontal=True)

# دوال الرسائل حسب اللغة
def get_message(method, lang):
    messages = {
        "English": {
            "fingerprint": "Welcome! Login with fingerprint.",
            "face": "Welcome! Login with face recognition.",
            "gesture": "Welcome! Login with gesture.",
            "keypad": "Welcome! Login with secret code."
        },
        "عربي": {
            "fingerprint": "مرحبًا بك! الدخول بالبصمة.",
            "face": "مرحبًا بك! الدخول بالتعرف على الوجه.",
            "gesture": "مرحبًا بك! الدخول بالإشارة.",
            "keypad": "مرحبًا بك! الدخول بالكود السري."
        },
        "Français": {
            "fingerprint": "Bienvenue! Connexion par empreinte digitale.",
            "face": "Bienvenue! Connexion par reconnaissance faciale.",
            "gesture": "Bienvenue! Connexion par geste.",
            "keypad": "Bienvenue! Connexion par code secret."
        },
        "Italiano": {
            "fingerprint": "Benvenuto! Accesso con impronta digitale.",
            "face": "Benvenuto! Accesso con riconoscimento facciale.",
            "gesture": "Benvenuto! Accesso con gesto.",
            "keypad": "Benvenuto! Accesso con codice segreto."
        }
    }
    return messages[lang][method]

# خيارات الدخول الآمن
col1, col2 = st.columns(2)
with col1:
    if st.button("🔒 بصمة / Fingerprint"):
        st.success(get_message("fingerprint", lang_choice))
    if st.button("🙂 وجه / Face"):
        st.success(get_message("face", lang_choice))
with col2:
    if st.button("🤟 إشارة / Gesture"):
        st.success(get_message("gesture", lang_choice))
    if st.button("🔢 كود / Code"):
        st.success(get_message("keypad", lang_choice))

# زر SOS وزر اليد
st.markdown("---")
col3, col4 = st.columns(2)
with col3:
    if st.button("🚨 SOS"):
        st.warning("Emergency SOS Activated!")
with col4:
    if st.button("✋ Hand"):
        st.info("Sign language support enabled.")
