import streamlit as st
import pandas as pd
from kombinasyon_motoru import kombinasyon_motoru

# Sayfa ayarları
st.set_page_config(page_title="Ege Giriş", layout="centered")
st.markdown("### Ege'ye Giriş")

# PIN doğrulama
pin = st.text_input("Lütfen 4 haneli PIN kodunu girin:", type="password")

if pin == '1995':
    st.success("✅ Giriş başarılı. Modüller yükleniyor...")
    st.markdown("### Strateji Modülleri")

    # Modül tetikleme butonları
    if st.button("KAMA - EMA Kombinasyonu"):
        st.write("📈 Anka planı testi başlatıldı...")

    if st.button("OBV-MACD Analizi"):
        st.write("📉 OBV-MACD sinyali çalıştırılıyor...")

    if st.button("RSI Ters Dönüş Tespiti"):
        st.write("📊 RSI sinyali analiz ediliyor...")

    if st.button("Aho Planı Testi"):
        st.write("📌 Aho planı testi başladı...")

        ven1 = st.file_uploader("📂 CSV veri dosyasını yükleyin", type=["csv"])
        if ven1 is not None:
            df = pd.read_csv(ven1)
            st.write("📄 İlk 5 satır:")
            st.dataframe(df.head(5))
            st.write("📊 Sütunlar:", df.columns.tolist())

            if 'Volume' in df.columns:
                st.success("✅ Volume sütunu bulundu.")
                # Buraya özel analiz fonksiyonu eklenebilir
                # örn: sonuç = aho_analiz(df)
                # st.dataframe(sonuç)
            else:
                st.error("❌ CSV dosyasında 'Volume' sütunu bulunamadı.")
        else:
            st.warning("⚠ Lütfen işlem yapmak için bir CSV yükleyin.")

        st.info("ℹ Bu dosya genellikle PMF analizleri için kullanılır.")

    st.markdown("### CSV Yükle ve Kombinasyon Hesapla")

    ven2 = st.file_uploader("📂 Kombinasyon için CSV yükleyin", type=["csv"], key="kombinasyon")
    if ven2 is not None:
        df2 = pd.read_csv(ven2)
        st.write("🔍 Yüklenen sütunlar:", df2.columns)

        if 'Close' in df2.columns and 'Volume' in df2.columns:
            st.success("✅ 'Close' ve 'Volume' sütunları bulundu.")
            sonuç = kombinasyon_motoru(df2)
            st.subheader("📊 Kombinasyon Sonuçları")
            st.dataframe(sonuç, use_container_width=True)
        else:
            st.error("❌ CSV dosyasında 'Close' ve 'Volume' sütunları bulunmalı.")
    else:
        st.info("📂 Lütfen işlem yapmak için bir CSV dosyası yükleyin.")
else:
    st.warning("🔒 Giriş için doğru PIN kodunu girin.")
