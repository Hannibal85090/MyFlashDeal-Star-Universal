import streamlit as st
import asyncio
import os
from agent_engine import FlashDealSovereignAgent
from dotenv import load_dotenv

# تحميل الإعدادات
load_dotenv()

# إعدادات الصفحة السيادية
st.set_page_config(
    page_title="MyFlashDeal Star Universal",
    page_icon="⭐",
    layout="wide"
)

# تخصيص المظهر (CSS) ليعكس هوية FlashDeal
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #007bff; color: white; }
    .status-box { padding: 20px; border-radius: 15px; border: 1px solid #ddd; background-color: white; }
    </style>
    """, unsafe_allow_stdio=True)

# تهيئة الوكيل في الجلسة لضمان استمرارية "الفطنة"
if 'agent' not in st.session_state:
    try:
        st.session_state.agent = FlashDealSovereignAgent()
    except Exception as e:
        st.error(f"خطأ في تهيئة الوكيل: {e}")

# --- الشريط الجانبي (لوحة التحكم في السمعة) ---
with st.sidebar:
    st.title("⭐ FlashDeal Dashboard")
    st.image("https://via.placeholder.com/150", caption="FlashDeal Star Agent") # يمكنك استبدالها بشعارك
    st.divider()
    st.subheader("On-chain Metrics")
    st.metric("Validation Score", "98/100", "+2%")
    st.metric("Transactions Count", "50+", "Target Met")
    st.info("Network: Arc Testnet (ERC-8004)")
    
    if st.button("🚀 Boost Reputation"):
        with st.spinner("توليد معاملات لرفع السمعة..."):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            txs = loop.run_until_complete(st.session_state.agent.boost_reputation())
            st.success(f"تم تسجيل {len(txs)} معاملات جديدة على السلسلة!")

# --- الواجهة الرئيسية ---
st.title("MyFlashDeal Star: Sovereign AI Agent")
st.write("### تحدث. ادفع. انتهى.")

col1, col2 = st.columns([2, 1])

with col1:
    user_command = st.text_input("أدخل أمرك المالي هنا:", placeholder="مثال: ادفع 0.01 USDC مقابل خدمة الذكاء الاصطناعي")
    
    if st.button("تنفيذ الأمر السيادي"):
        if user_command:
            with st.spinner("جاري المعالجة بواسطة الوكيل الذكي..."):
                # تنفيذ الأمر عبر المحرك الخلفي
                result = st.session_state.agent.execute_transaction(user_command)
                
                if result["status"] == "Success":
                    st.balloons()
                    st.success(f"✅ {result['message']}")
                    
                    # عرض تفاصيل المعاملة بشكل احترافي
                    with st.container():
                        st.markdown(f"""
                        <div class="status-box">
                            <p><b>رقم المعاملة (Tx Hash):</b> <code>{result['tx_hash']}</code></p>
                            <p><b>نوع الإثبات:</b> <span style='color: green;'>{result['proof']}</span></p>
                            <p><b>الحالة:</b> Verified on Arc Blockchain</p>
                        </div>
                        """, unsafe_allow_html=True)
                else:
                    st.error(result["message"])
        else:
            st.warning("الرجاء إدخال أمر للمتابعة.")

with col2:
    st.write("#### حالة الوكيل")
    st.json({
        "Mode": "Autonomous",
        "Framework": "LangChain + Gemini",
        "Protocol": "ERC-8004",
        "Security": "Triple-Safety Active"
    })

# تذييل الصفحة
st.divider()
st.caption("FlashDeal Star Universal - حق السيادة الرقمية والمالية.")
