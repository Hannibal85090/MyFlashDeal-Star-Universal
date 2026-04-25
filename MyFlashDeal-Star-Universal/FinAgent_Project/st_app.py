import streamlit as st
import yfinance as yf # هذه هي "الروح" التي تجلب الأسعار

st.set_page_config(page_title="My FlashDeal Star", page_icon="🌟")

st.title("🌟 My FlashDeal Star")
st.subheader("وكيل تحليل السوق - مباشر")

# مدخل لرمز السهم (مثلاً: AAPL لآبل، أو 2222 لأرامكو)
symbol = st.text_input("أدخل رمز السهم للاستعلام (مثال: AAPL):", "AAPL")

if st.button("استشارة مجلس الاعتبار"):
    try:
        with st.spinner("جاري جلب الأسعار اللحظية..."):
            stock = yf.Ticker(symbol)
            price = stock.history(period="1d")['Close'].iloc[-1]
            currency = stock.info.get('currency', 'USD')
            
            st.metric(label=f"السعر الحالي لـ {symbol}", value=f"{price:.2f} {currency}")
            st.success("تم جلب البيانات بنجاح من البورصة الآن.")
            st.info("نصيحة الوكيل: التزم ببروتوكول Talk. Pay. Done.")
    except Exception as e:
        st.error(f"عذراً، لم أجد بيانات لهذا الرمز. تأكد من الرمز الصحيح.")

st.sidebar.write("Talk. Pay. Done.")

