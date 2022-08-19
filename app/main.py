import streamlit as st
from utils import head, body
import matplotlib.pyplot as plt

head()
bir, iki, uc, dort = body()

if st.button('Analiz Et'):

    labels = 'Mavi', 'Kırmızı', 'Sarı', 'Yeşil'
    sizes = [bir, iki, uc, dort]
    explode = (0, 0.1, 0, 0)
    colours = {'Mavi': 'b',
               'Kırmızı': 'r',
               'Sarı': 'y',
               'Yeşil': 'g'}

    fig, ax = plt.subplots()
    ax.pie(sizes,
           labels=labels,
           explode=explode,
           colors=[colours[key] for key in labels],
           autopct='%1.1f%%',
           shadow=True,
           startangle=90)  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.pyplot(fig)

