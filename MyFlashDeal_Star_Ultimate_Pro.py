import streamlit as st

def handle_sign():
    st.info("✋ Sign command triggered")
    st.success("Gesture recognized successfully!")

def handle_lock():
    st.warning("🔒 Lock engaged")
    st.success("Security protocol activated!")

def handle_face():
    st.info("👤 Face recognition triggered")
    st.success("Identity verified!")

def handle_key():
    st.info("🔑 Key command triggered")
    st.success("Access granted!")

# أيقونات قابلة للنقر
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("✋ Sign Icon"): handle_sign()
with col2:
    if st.button("🔒 Lock Icon"): handle_lock()
with col3:
    if st.button("👤 Face Icon"): handle_face()
with col4:
    if st.button("🔑 Key Icon"): handle_key()

# الأزرار النصية المقابلة
tab1, tab2, tab3, tab4 = st.tabs(["Sign","Lock","Face","Key"])
with tab1:
    if st.button("Sign"): handle_sign()
with tab2:
    if st.button("Lock"): handle_lock()
with tab3:
    if st.button("Face"): handle_face()
with tab4:
    if st.button("Key"): handle_key()
