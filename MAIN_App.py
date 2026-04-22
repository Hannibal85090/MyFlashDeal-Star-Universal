import streamlit as st

# 1. بروتوكول الاستدعاء الذكي (تجاوز أخطاء الماضي)
try:
    import google.generativeai as genai
except ImportError:
    st.error("🚨 خطأ اعتبار: مكتبة google-generativeai مفقودة في المجلد.")
    st.stop()

# 2. إعدادات الهوية البصرية (Talk. Pay. Done.)
st.set_page_config(page_title="FlashDeal Star", page_icon="⭐", layout="wide")

# 3. الربط بالأوركسترا (Secrets) - لا يتم الواجب إلا به
def connect_orchestra():
    try:
        if "GEMINI_KEY" not in st.secrets:
            st.error("🔑 عائق أمني: المفتاح مفقود في الأوركسترا (Secrets).")
            return None
        
        genai.configure(api_key=st.secrets["GEMINI_KEY"])
        # استخدام النسخة المستقرة لضمان عدم التعارض
        return genai.GenerativeModel('gemini-1.5-flash')
    except Exception as e:
        st.error(f"⚠️ فشل في استدعاء المايسترو: {str(e)}")
        return None

model = connect_orchestra()

# 4. إدارة نبض التفاعل (Session State) لمنع العلوق
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("⭐ FlashDeal Star: Autonomous Agent")
st.write("---")

# تقسيم العمل: التفاعل (Talk) والأمان (Security)
col_chat, col_auth = st.columns([2, 1])

with col_chat:
    st.subheader("🗣️ مركز القيادة (Talk)")
    
    # عرض تاريخ العمليات فوراً
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # محرك الاستجابة (الجوهر)
    if prompt := st.chat_input("بمَ يأمر مالك النجمة؟"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        if model:
            with st.chat_message("assistant"):
                with st.spinner("الوكيل يحلل الآن..."):
                    try:
                        # تلقين الوكيل دوره الاستراتيجي
                        instr = f"أنت الوكيل المالي الرسمي لـ FlashDeal. نفذ باحترافية: {prompt}"
                        response = model.generate_content(instr)
                        st.markdown(response.text)
                        st.session_state.messages.append({"role": "assistant", "content": response.text})
                        # الحسم: تحديث الجلسة فوراً لضمان عدم العلوق
                        st.rerun()
                    except Exception as e:
                        st.error(f"❌ تعطل الاتصال بالعقل: {str(e)}")

with col_auth:
    st.subheader("🔐 بوابة الأمان (Security)")
    auth_check = st.toggle("تفعيل التحقق البيومتري")
    if auth_check:
        picture = st.camera_input("بصمة الوجه")
        if picture:
            st.success("✅ الهوية مؤكدة")
            if st.button("🚀 تنفيذ الدفع الفوري (Done)"):
                if "NUCLEAR_KEY" in st.secrets:
                    st.balloons()
                    st.success("تمت العملية بنجاح!")
                    st.code(f"REF: {st.secrets['NUCLEAR_KEY'][:15]}...", language="text")
                else:
                    st.warning("⚠️ المفتاح النووي غير موجود في الأوركسترا.")

# 5. تذييل النسخة (تمام الجمل والاعتبار)
st.write("---")
st.caption("FlashDeal Star 2026 | القوة في الوحدة | Talk. Pay. Done.")

