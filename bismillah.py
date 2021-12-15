"""
Aplikasi Streamlit untuk menggambarkan statistik penumpang TransJakarta

Sumber data berasal dari Jakarta Open Data
Referensi API Streamlit: https://docs.streamlit.io/library/api-reference
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
import streamlit as st
import json


file_json = pd.read_json('kode_negara_lengkap.json')
df_json = pd.DataFrame.from_dict(file_json)


kode_angka = []
region = []
subregion = []
selain_negara = []


############### title ###############
st.set_page_config(layout="wide")  # this needs to be the first Streamlit command called
st.title("Produksi Minyak Mentah Berbagai Negara")
############### title ###############)

############### sidebar ###############
st.sidebar.title("Pengaturan")
left_col, mid_col, right_col = st.columns(3)

## User inputs on the control panel
st.sidebar.subheader("Pengaturan konfigurasi tampilan")
nama_negara = []
N = st.sidebar.selectbox("Pilih Negara", nama_negara)


n_tampil = st.sidebar.number_input("Jumlah baris dalam tabel yang ditampilkan", min_value=1, max_value=None, value=10)
############### sidebar ###############

############### upper left column ###############
left_col.subheader("Tabel representasi data")


df = pd.read_csv('produksi_minyak_mentah.csv')

left_col.dataframe(df.head(n_tampil))
############### upper left column ###############

############### upper middle column ###############

#membuat list yang dibutuhkan
kode_negara = list(df['kode_negara'].unique())
for i in kode_negara:
    if i not in list(df_json['alpha-3']):
        selain_negara.append(i)

for i in selain_negara:
    df = df[df.kode_negara != i]
    if i in list(kode_negara):
        kode_negara.remove(i)

for i in range(len(kode_negara)):
    for j in range(len(list(df_json['alpha-3']))):
        if list(df_json['alpha-3'])[j] == kode_negara[i] and list(df_json['name'])[j] not in nama_negara:
            nama_negara.append(list(df_json['name'])[j])
            kode_angka.append(list(df_json['country-code'])[j])
            region.append(list(df_json['region'])[j])
            subregion.append(list(df_json['sub-region'])[j])

for i in range(len(nama_negara)):
    if nama_negara[i] == N:
        kodehuruf = kode_negara[i]
        kodeangka = kode_angka[i]
        reg = region[i]
        subreg = subregion[i]
#dataframe yang berisi informasi lengkap negara
df_lengkap = pd.DataFrame(list(zip(nama_negara, kode_negara, kode_angka, region, subregion)), columns=[
                         'Negara', 'alpha-3', 'Kode_Negara', 'Region', 'Sub-Region'])
tulis_kode = []
for i, kode in enumerate(kode_negara):
    tulis_kode.append(f"{str(i+1)}. {kode}\n")
tulis_kode = ' '.join(map(str, tulis_kode))

mid_col.markdown(tulis_kode)
############### upper middle column ###############

############### upper right column ###############
right_col.subheader("Total penumpang perbulan")





############### upper right column ###############

############### lower left column ###############



############### lower left column ###############

############### lower middle column ###############



############### lower middle column ###############

############### lower right column ###############

############### lower right column ###############