"""
Aplikasi Streamlit untuk menggambarkan statistik penumpang TransJakarta

Sumber data berasal dari Jakarta Open Data
Referensi API Streamlit: https://docs.streamlit.io/library/api-reference
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import streamlit as st
import json

df = pd.read_csv('produksi_minyak_mentah.csv')
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


############### sidebar ###############

############### upper left column ###############





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
        kodenegarahuruf = kode_negara[i]
        kodenegaraangka = kode_angka[i]
        reg = region[i]
        subreg = subregion[i]
#dataframe yang berisi informasi lengkap negara
df_lengkap = pd.DataFrame(list(zip(nama_negara, kode_negara, kode_angka, region, subregion)), columns=[
                         'Negara', 'alpha-3', 'Kode_Negara', 'Region', 'Sub-Region'])


list_produksi = []
list_tahun = []

# Mengambil data produksi dan tahun berdasarkan negara yang dipilih pada
# option dan memasukkannya ke list yang telah dibuat
for i in range(len(list(df['kode_negara']))):
    if kodenegarahuruf == list(df['kode_negara'])[i]:
        list_produksi.append(list(df['produksi'])[i])
        list_tahun.append(list(df['tahun'])[i])

fig = plt.plot(x=list_tahun, y=list_produksi) ,plt.title('grafik'), plt.xlabel('Tahun'),plt.ylabel('Produksi')
st.plotly_chart(fig)

############### upper middle column ###############
tl1 = st.columns(2)
opt1, opt2 = st.columns((1, 1))
cg1 = st.columns(2)

title2 = 'Grafik Jumlah Produksi Minyak Terbesar pada Tahun'
tl1.markdown(title2)
T = int(opt1.selectbox("Tahun",list_tahun))

# Membuat dataframe baru berdasarkan tahun yang dipilih dan diurutkan
# berdasarkan produksi minyak terbesar
df2 = df.loc[df['tahun'] == T].sort_values(
    by=['produksi'], ascending=False)
############### upper right column ###############






############### upper right column ###############

############### lower left column ###############



############### lower left column ###############

############### lower middle column ###############



############### lower middle column ###############

############### lower right column ###############

############### lower right column ###############
