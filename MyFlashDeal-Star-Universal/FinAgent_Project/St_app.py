import streamlit as st
import time
# استدعاء النواة المحكمة من الملف الذي أنشأته توًا
from FD_Core import FlashDealStarUniversal

# [Strategic UI: Cyber-Tech Identity]
st.set_page_config(page_title="FlashDeal Star Universal", page_icon="⚡", layout="wide")

# تخصيص المظهر ليكون عصرياً (Dark Theme)
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #2e7d32; color: white; }
    .success-text { color: #00ff00; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# تهيئة المحرك العالمي
if 'engine' not in st.session_state:
    st.session_state.engine = FlashDealStarUniversal()

st.title("⚡ FlashDeal Star Universal")
st.subheader("Global Sovereign AI Financial Agent")

# تقسيم الواجهة إلى أعمدة (Professional Layout)
col1, col2 = st.columns([1, 1])

with col1:
    st.write("### 🎙️ Command Center")
    user_input = st.text_input("Enter Command (e.g., Pay 250 USDC for Groceries)", "Pay 150 USDC for Server Fees")
    
    if st.button("Execute (Talk. Pay. Done.)"):
        with st.spinner("Encrypting & Generating Universal Token..."):
            # تنفيذ العملية عبر النواة المحكمة
            u_token = st.session_state.engine.execute_universal_deal("Hannibal_85090", 150.0, "USDC")
            st.session_state.current_token = u_token
            st.success(f"Token Generated: {u_token[:20]}...")
            time.sleep(1)

with col2:
    st.write("### 🔐 Security & Verification")
    if 'current_token' in st.session_state:
        st.info("Biometric Authentication Required")
        # محاكاة التحقق الحيوي (الوجه/الحركة)
        bio_confirm = st.checkbox("Confirm Biometric Identity (Face/Gesture)")
        
        if st.button("Finalize Transaction"):
            result = st.session_state.engine.verify_and_finalize(st.session_state.current_token, bio_confirm)
            if "SUCCESS" in result:
                st.balloons()
                st.markdown(f"<p class='success-text'>{result}</p>", unsafe_allow_html=True)
            else:
                st.error(result)
    else:
        st.write("Waiting for command...")

# [Axis: Future Vision]
st.sidebar.markdown("---")
st.sidebar.write("### 🛠️ System Status")
st.sidebar.success("Core Engine: FD_Core.py (Linked)")
st.sidebar.info(f"Version: {st.session_state.engine.SLOGAN}")
