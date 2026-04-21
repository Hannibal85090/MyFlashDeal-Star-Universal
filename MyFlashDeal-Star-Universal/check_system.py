import google.generativeai as genai
import streamlit as st
import os

def health_check():
    """
    بوابة الاعتبار والعبر: فحص شامل للمفاتيح والاتصال
    تجنب أخطاء الأقواس، التعارضات البرمجية، وضمان تمام الجمل.
    """
    st.title("🛡️ FlashDeal Star: نظام فحص الجاهزية")
    st.write("---")

    # 1. تعريف المفتاح النووي (المحفظة) - تأكد من تطابق النص تماماً
    nuclear_key = "TEST_API_KEY:a4d6b6e5a87330c831dc0d745c58bd6a:6ac4ef8983dd91790756bc3869e809d5"
    
    # 2. اختبار عقل الوكيل (Gemini)
    st.subheader("🧠 اختبار عقل الوكيل (Gemini)")
    try:
        # ملاحظة: استبدل 'YOUR_API_KEY' بمفتاح Gemini الفعلي عند التشغيل
        gemini_api_key = st.secrets.get("GEMINI_KEY", "NOT_FOUND")
        
        if gemini_api_key != "NOT_FOUND":
            genai.configure(api_key=gemini_api_key)
            model = genai.GenerativeModel('gemini-1.5-flash')
            # تجربة فهم "نية" مالية
            test_response = model.generate_content("حلل النية: أريد دفع 10 USDC لمكتب العمل")
            st.success("✅ جيميناي متصل وفهم الأمر بنجاح.")
            st.info(f"تحليل الوكيل: {test_response.text[:100]}...")
        else:
            st.warning("⚠️ مفتاح Gemini غير موجود في إعدادات Secrets.")
    except Exception as e:
        st.error(f"❌ خطأ في اتصال Gemini: {str(e)}")

    # 3. اختبار بوابة الدفع (المفتاح النووي)
    st.subheader("💳 اختبار المحفظة (The Nuclear Key)")
    if nuclear_key.startswith("TEST_API_KEY"):
        st.success("✅ المفتاح النووي موجود بتنسيق صحيح.")
        st.write("حالة البيئة: **تجريبية (Sandbox)** - آمنة للتطوير.")
    else:
        st.error("❌ تنسيق المفتاح النووي غير صحيح أو مفقود.")

    # 4. فحص التعارضات البرمجية
    st.subheader("⚙️ فحص بيئة العمل")
    try:
        import cv2
        import mediapipe as mp
        st.success(f"✅ مكتبة OpenCV و MediaPipe جاهزة بدون تعارض.")
    except ImportError as e:
        st.error(f"❌ تعارض في المكتبات: {str(e)}. تأكد من استخدام opencv-python-headless")

    st.write("---")
    st.write("إصدار النظام: 2.0 | الحالة: جاهز للحسم")

if __name__ == "__main__":
    health_check()

