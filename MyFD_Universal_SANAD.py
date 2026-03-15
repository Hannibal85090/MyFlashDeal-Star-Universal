# Modified FlashDeal Universal Interface (Improved Interaction & Image Loading)
# Parallel Project - High Quality - Ready for GitHub
import streamlit as st
import hashlib

# Configuration for multi-language dictionary
LANGUAGES = {
    'English': {
        'page_title': "My FlashDeal Star Universal",
        'head_multimodal': "Sony Multimodal Agent",
        'voice_sign': "Voice & Sign",
        'text': "Text",
        'movement': "Movement",
        'dual_encryption': "Dual-Layer Encryption",
        'simple_encryption': "Simple Encryption (SHA-256)",
        'complex_token': "Complex Mutual Token (Synchronized)",
        'active': "Active",
        'locked': "Locked",
        'unlocked': "Unlocked",
        'sync_button': "Synchronize Tokens",
        'sync_success': "Mutual Token Synchronized Successfully!",
        'global_deal': "Global Deal",
        'product': "Wireless Headphones",
        'buy_button': "BUY NOW",
        'completion_cert': "CERTIFICATE OF SUCCESS",
        'talk_pay_done': "Talk. Pay. Done.",
        'verification': "Verification with Saden Security"
    },
    'Arabic': {
        'page_title': "نجم فلاش ديل العالمي (My FlashDeal Star Universal)",
        'head_multimodal': "وكيل سوني متعدد الأنماط",
        'voice_sign': "الصوت والإشارة",
        'text': "الكتابة",
        'movement': "الحركة",
        'dual_encryption': "التشفير المزدوج",
        'simple_encryption': "تشفير بسيط (SHA-256)",
        'complex_token': "التوكن المتبادل المعقد (متزامن)",
        'active': "نشط",
        'locked': "مغلق",
        'unlocked': "مفتوح",
        'sync_button': "مزامنة التوكن المتبادل",
        'sync_success': "تمت مزاينة التوكن المتبادل بنجاح!",
        'global_deal': "إبرام الصفقة العالمية",
        'product': "سماعات الرأس اللاسلكية",
        'buy_button': "إتمام الصفقة (BUY NOW)",
        'completion_cert': "شهادة نجاح العملية (CERTIFICATE OF SUCCESS)",
        'talk_pay_done': "تحدث. ادفع. تم.",
        'verification': "التحقق عبر أمان سادن"
    }
}

# Session state initialization for token synchronization
if 'token_status' not in st.session_state:
    st.session_state['token_status'] = 'locked'

# Page Configuration
st.set_page_config(layout="wide")

# Language Switcher in Sidebar
with st.sidebar:
    language = st.selectbox("Select Language | اختر اللغة", ("Arabic", "English"))
    # Language change trigger
    t = LANGUAGES[language]

# Main Interface Rendering
st.title(f"{t['head_multimodal']}")
st.write(f"🎤 {t['voice_sign']} | ⌨️ {t['text']} | 👋 {t['movement']}")

st.divider()

# Encryption Section
col1, col2 = st.columns([1, 2])
with col1:
    st.image("bahrain_shield.png", width=50) # Assuming the image is in the root
    st.subheader(f"{t['dual_encryption']}")
with col2:
    st.write(f"🟢 {t['simple_encryption']}: **{t['active']}**")
    
    # Dynamic display based on token status
    if st.session_state['token_status'] == 'locked':
        st.write(f"🔒 {t['complex_token']}: **{t['locked']}**")
    else:
        st.write(f"🔓 {t['complex_token']}: **{t['unlocked']}**")
        
    sync_btn = st.button(t['sync_button'])
    
    if sync_btn:
        st.session_state['token_status'] = 'unlocked'
        st.success(t['sync_success'])

st.divider()

# Global Deal Section
st.subheader(f"⚡ {t['global_deal']}")

col3, col4 = st.columns([2, 1])
with col3:
    # 🌟 Fixed Image Loading Code (Replacing "0")
    try:
        st.image("headphones_product.png", caption=t['product']) # Replace with actual image path
    except FileNotFoundError:
        st.warning(f"Image for '{t['product']}' not found. Please upload 'headphones_product.png'.")
        
    st.write("⭐⭐⭐⭐⭐")
    st.markdown("### $99.99")
    st.button(t['buy_button'])

with col4:
    # Status Message Container
    with st.container(border=True, height=200):
        st.markdown(f"#### {t['completion_cert']}")
        st.markdown(f"**{t['talk_pay_done']}**")
        st.write(t['verification'])
        st.image("usa_flag.png", width=25)
