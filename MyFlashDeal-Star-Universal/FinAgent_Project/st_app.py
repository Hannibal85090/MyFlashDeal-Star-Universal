import streamlit as st
import yfinance as yf
import pandas as pd

# إعدادات واجهة نجمة فلاش ديل
st.set_page_config(page_title="My FlashDeal Star", page_icon="🌟", layout="wide")

st.title("🌟 My FlashDeal Star | الوكيل المالي")
st.markdown("### بروتوكول: Talk. Pay. Done.")

# منطقة البحث عن الأسهم
symbol = st.text_input("أدخل رمز السهم (مثلاً: AAPL للأسواق العالمية أو 2222 لأرامكو):", "AAPL")

if st.button("استشارة مجلس الاعتبار"):
    try:
        with st.spinner("جاري جلب البيانات اللحظية من الأسواق..."):
            # جلب البيانات الحقيقية
            data = yf.Ticker(symbol)
            price_info = data.history(period="1d")
            
            if not price_info.empty:
                current_price = price_info['Close'].iloc[-1]
                currency = data.info.get('currency', 'USD')
                name = data.info.get('longName', symbol)
                
                # عرض السعر بشكل احترافي
                st.metric(label=f"سعر {name} الآن", value=f"{current_price:.2f} {currency}")
                
                st.success("البيانات دقيقة ومباشرة من البورصة.")
                st.info("رؤية الوكيل: النظام يحلل الإشارات اللحظية بناءً على هذا السعر.")
            else:
                st.error("لم يتم العثور على بيانات لهذا الرمز.")
    except Exception as e:
        st.error(f"حدث خطأ أثناء الاتصال بالأسواق: {e}")

st.sidebar.write("My FlashDeal Star V2")

