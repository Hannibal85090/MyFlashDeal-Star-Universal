import streamlit as st
import time

# 1. نظام اللغات المتعددة المطور
LANG_DICT = {
    'Arabic': {
        'title': "نجم فلاش ديل العالمي 🌟",
        'agent': "الوكيل الذكي (تحدث. ادفع. تم.)",
        'saden': "أمان سادن: التوكن المتبادل",
        'product': "سماعات الرأس (إصدار النجم)",
        'buy': "إبرام الصفقة العالمية 🚀",
        'success': "تمت العملية بنجاح! مبروك شريكي",
        'motto': "Talk. Pay. Done.",
        'input_label': "اكتب أمرك هنا...",
        'voice_btn': "ابدأ التحدث 🎤",
        'sign_btn': "تفعيل كاميرا الإشارة 👋",
        'sync_btn': "مزامنة التوكن الآمن 🛡️"
    },
    'English': {
        'title': "My FlashDeal Star Universal 🌟",
        'agent': "Smart Agent (Talk. Pay. Done.)",
        'saden': "Saden Security: Mutual Token",
        'product': "Headphones (Star Edition)",
        'buy': "Global Deal Execution 🚀",
        'success': "Process Completed Successfully!",
        'motto': "Talk. Pay. Done.",
        'input_label': "Type your command here...",
        'voice_btn': "Start Listening 🎤",
        'sign_btn': "Activate Sign Camera 👋",
        'sync_btn': "Sync Secure Token 🛡️"
    }
}

st.set_page_config(page_title="FlashDeal Star", layout="wide")

# اختيار اللغة
with st.sidebar:
    selected_lang = st.selectbox("🌐 Language | اللغة", list(LANG_DICT.keys()))
    t = LANG_DICT[selected_lang]
    st.divider()
    st.markdown(f"**Slogan:** {t['motto']}")

st.title(t['title'])
st.write(f"### 🤖 {t['agent']}")

# --- القسم التفاعلي الجديد (صوت، إشارة، كتابة) ---
tab1, tab2, tab3 = st.tabs(["⌨️ Text | كتابة", "🎤 Voice | صوت", "👋 Sign | إشارة"])

with tab1:
    user_text = st.text_input(t['input_label'])
    if user_text:
        st.write(f"💬 **FlashDeal Agent:** Processing command: '{user_text}'...")

with tab2:
    if st.button(t['voice_btn']):
        with st.spinner("Listening / جاري الاستماع..."):
            time.sleep(2)
            st.success("✅ Voice recognized: 'Execute FlashDeal'")

with tab3:
    if st.button(t['sign_btn']):
        st.warning("📸 Camera request: Waiting for Sign Language input...")
        time.sleep(1.5)
        st.info("👋 Gesture detected: [YES/APPROVE]")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"### 🛡️ {t['saden']}")
    st.markdown("<h1 style='text-align: center;'>🛡️</h1>", unsafe_allow_html=True)
    if st.button(t['sync_btn']):
        with st.status("Syncing Token..."):
            time.sleep(1)
            st.success("✅ Token Synchronized with Saden Cloud")

with col2:
    st.markdown(f"### 🎧 {t['product']}")
    st.markdown("<h1 style='text-align: center;'>🎧</h1>", unsafe_allow_html=True)
    st.markdown("## **$99.99**")
    
    if st.button(t['buy'], type="primary", use_container_width=True):
        st.balloons()
        with st.container(border=True):
            st.success(f"🏆 {t['success']}")
            st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
            st.toast("Deal Done! | تمت الصفقة")
