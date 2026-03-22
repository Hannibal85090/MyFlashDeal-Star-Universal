# --- النجمة المركزية مع الرموز ---
st.markdown('<div class="star">★</div>', unsafe_allow_html=True)
st.markdown("""
<div style="text-align:center;">
    <span class="icon-circle">🔒</span>
    <span class="icon-circle">👤</span>
    <span class="icon-circle">✋</span>
    <span class="icon-circle">🔑</span>
</div>
""", unsafe_allow_html=True)

# --- عرض السعر مع تقييم ---
col1, col2 = st.columns([1,2])
with col1:
    st.metric("Price", "$99.99")
with col2:
    st.write("Rating:")
    st.markdown(
        "<span style='color:green;'>★ ★ ★ ★ ☆</span> "
        "<span style='color:red;'>★ ☆ ☆ ☆ ☆</span>",
        unsafe_allow_html=True
    )

# --- شهادة الصفقة ---
if st.button(t['buy'], type="primary", use_container_width=True):
    st.balloons(); st.snow()
    add_to_memory("Deal Concluded Successfully")
    st.markdown(
        f"""
        <div class='glass-card' style='text-align:center;'>
            <h2>🏆 {t['success']}</h2>
            <p>Certificate Code: STAR-UNIV-2026-{int(time.time())}</p>
            <p>Status: ✅ Validated</p>
            <p>Date: 22/03/2026</p>
        </div>
        """,
        unsafe_allow_html=True
    )
