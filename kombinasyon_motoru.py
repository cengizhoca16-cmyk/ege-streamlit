import pandas as pd
import streamlit as st
from ta.volume import OnBalanceVolumeIndicator
from ta.momentum import RSIIndicator

def kombinasyon_motoru(veri):
    kombinasyon = pd.DataFrame()

    # RSI hesapla ve 14 günlük ortalamasını al
    rsi = RSIIndicator(close=veri['Close']).rsi()
    kombinasyon['RSI'] = rsi.rolling(window=14).mean()

    # OBV hesapla ve 14 günlük ortalamasını al
    obv = OnBalanceVolumeIndicator(close=veri['Close'], volume=veri['Volume']).on_balance_volume()
    kombinasyon['OBV'] = obv.rolling(window=14).mean()

    return kombinasyon

# Streamlit Arayüzü
st.set_page_config(page_title="Ege Kombinasyon Motoru", layout="wide")
st.title("📊 Ege Kombinasyon Motoru")

# Veri yükleme
veri = st.file_uploader("📁 CSV veri dosyasını yükle", type="csv")

if veri is not None:
    df = pd.read_csv(veri)

    # Gerekli sütunlar kontrolü
    if 'Close' in df.columns and 'Volume' in df.columns:
        sonuç = kombinasyon_motoru(df)
        st.subheader("🔍 Kombinasyon Sonuçları")
        st.dataframe(sonuç, use_container_width=True)
    else:
        st.error("❌ CSV dosyasında 'Close' ve 'Volume' sütunları bulunmalı.")
else:
    st.info("📌 Lütfen işlem yapmak için bir CSV dosyası yükleyin.")
