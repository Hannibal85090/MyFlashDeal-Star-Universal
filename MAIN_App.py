import streamlit as st
import sys
import os

# القاعدة الذهبية لضمان عدم التعارض في المسارات
current_dir = os.path.dirname(__file__)
if current_dir not in sys.path:
    sys.path.append(current_dir)

# محاولة استدعاء المحرك مع معالجة الأخطاء المتوقعة
try:
    from agent_engine import FlashDealSovereignAgent
except ImportError as e:
    st.error(f"❌ خطأ في ربط الملفات: {str(e)}")
    st.stop()

# إعداد واجهة المستخدم
st.set_page_config(page_title="My FlashDeal Star", page_icon="⭐")

st.title("🌟 My FlashDeal Star")
st.subheader("تحدث. ادفع. انتهى.")

# تهيئة الوكيل
if 'agent' not in st.session_state:
    st.session_state.agent = FlashDealSovereignAgent()

# مدخلات المستخدم
user_input = st.text_input("بماذا يأمر السيادي اليوم؟", placeholder="مثال: ادفع 10 دولار لمزود الخدمة")

if st.button("تنفيذ الآن"):
    if user_input:
        with st.spinner("جاري المعالجة عبر الشبكة..."):
            result = st.session_state.agent.execute_transaction(user_input)
            st.success(result["message"])
            st.code(f"Transaction Hash: {result['tx_hash']}", language="bash")
            st.info(f"إثبات التوثيق: {result['verification']}")
    else:
        st.warning("الرجاء إدخال أمر للمضي قدماً.")

# ركن رفع السمعة (للعمليات الآلية)
if st.sidebar.button("رفع السمعة (Boost)"):
    st.sidebar.write("جاري توليد معاملات لرفع التصنيف...")
    # هنا يمكن استدعاء وظيفة boost_reputation

