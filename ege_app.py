import streamlit as st

st.set_page_config(page_title="Ege Giriş", layout="centered")
st.markdown("### 🔐 Ege'ye Giriş")

pin = st.text_input("Lütfen 4 haneli PIN kodunu girin:", type="password")

if pin == "1995":
    st.success("✅ Giriş başarılı. Modüller yükleniyor...")

    st.markdown("### 📊 Strateji Modülleri")
    
    if st.button("KAMA + EMA Kombinasyonu"):
        st.write("⏳ Arka planda test başlatıldı...")

    if st.button("OBV-MACD Analizi"):
        st.write("📈 OBV-MACD stratejisi çalıştırılıyor...")

    if st.button("RSI Ters Dönüş Tespiti"):
        st.write("🔍 RSI sinyali analiz ediliyor...")

else:
    if pin != "":
        st.error("❌ PIN hatalı. Lütfen tekrar deneyin.")
    st.stop()
