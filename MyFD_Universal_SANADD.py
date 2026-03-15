import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="FlashDeal Star - Secure Login", layout="centered")

# عرض الصورة النهائية
st.image("assets/images/star_interface_clean.png", use_column_width=True)

# اختيار اللغة
languages = {
    "English": "🇬🇧",
    "عربي": "🇦🇪",
    "Français": "🇫🇷",
    "Italiano": "🇮🇹"
}
lang_choice = st.radio("اختر اللغة / Choose Language:", list(languages.keys()), horizontal=True)

# الرسائل حسب اللغة
messages = {
    "English": {
        "fingerprint": "Welcome! Login with fingerprint.",
        "face": "Welcome! Login with face recognition.",
        "gesture": "Welcome! Login with gesture.",
        "keypad": "Welcome! Login with secret code.",
        "sos": "Emergency SOS Activated!",
        "hand": "Sign language support enabled.",
        "assistant": "Smart Assistant: Choose the login method that suits you best."
    },
    "عربي": {
        "fingerprint": "مرحبًا بك! الدخول بالبصمة.",
        "face": "مرحبًا بك! الدخول بالتعرف على الوجه.",
        "gesture": "مرحبًا بك! الدخول بالإشارة.",
        "keypad": "مرحبًا بك! الدخول بالكود السري.",
        "sos": "تم تفعيل نداء الطوارئ!",
        "hand": "تم تفعيل دعم لغة الإشارة.",
        "assistant": "الوكيل الذكي: اختر وسيلة الدخول الأنسب لك لضمان الأمان والسهولة."
    },
    "Français": {
        "fingerprint": "Bienvenue! Connexion par empreinte digitale.",
        "face": "Bienvenue! Connexion par reconnaissance faciale.",
        "gesture": "Bienvenue! Connexion par geste.",
        "keypad": "Bienvenue! Connexion par code secret.",
        "sos": "SOS d'urgence activé!",
        "hand": "Support de langue des signes activé.",
        "assistant": "Assistant intelligent : Choisissez la méthode de connexion la plus adaptée."
    },
    "Italiano": {
        "fingerprint": "Benvenuto! Accesso con impronta digitale.",
        "face": "Benvenuto! Accesso con riconoscimento facciale.",
        "gesture": "Benvenuto! Accesso con gesto.",
        "keypad": "Benvenuto! Accesso con codice segreto.",
        "sos": "SOS di emergenza attivato!",
        "hand": "Supporto per la lingua dei segni attivato.",
        "assistant": "Assistente intelligente: Scegli il metodo di accesso più adatto."
    }
}

# تفاعل الأزرار
st.markdown("### 🔐 اختر وسيلة الدخول:")
col1, col2 = st.columns(2)
with col1:
    if st.button("🔒 Fingerprint"):
        st.success(messages[lang_choice]["fingerprint"])
    if st.button("🙂 Face"):
        st.success(messages[lang_choice]["face"])
with col2:
    if st.button("🤟 Gesture"):
        st.success(messages[lang_choice]["gesture"])
    if st.button("🔢 Code"):
        st.success(messages[lang_choice]["keypad"])

# أزرار SOS و اليد
st.markdown("---")
col3, col4 = st.columns(2)
with col3:
    if st.button("🚨 SOS"):
        st.error(messages[lang_choice]["sos"])
with col4:
    if st.button("✋ Hand"):
        st.info(messages[lang_choice]["hand"])

# الوكيل الذكي
st.markdown("### 🤖 Smart Assistant")
st.write(messages[lang_choice]["assistant"])
