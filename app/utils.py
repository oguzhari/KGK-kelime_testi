import pandas as pd
import streamlit as st

choose1, choose2, choose3, choose4, choose5 = "", "", "", "", ""
choose6, choose7, choose8, choose9, choose10 = "", "", "", "", ""
choose11, choose12 = "", ""

def head():
    st.markdown("""
        <h1 style='text-align: center'>
        Kelime Testi Analizi
        </h1>
    """, unsafe_allow_html=True
                )

    st.caption("""
        <p style='text-align: center;margin-bottom: 50px;'>
        Sakarya Üniversitesi Kariyer ve Yetenek Yönetimi Koordinatörlüğü
        </p>
    """, unsafe_allow_html=True
               )



def body():
    bir, iki, uc, dort = 0, 0, 0, 0
    st.markdown("""
            <p style='text-align: center'>
            Güçlü Yönler. Her dört seçenekten birini seçiniz.
            </p>
        """, unsafe_allow_html=True
            )

    choose1 = st.radio("------------------------------------------- 1 -------------------------------------------",
                       ("Sonuç Odaklı", "Uyum Sağlayan", "Hareketli", "Analitik"),
                       key="choose1",
                       horizontal=True)

    choose2 = st.radio("------------------------------------------- 2 -------------------------------------------",
                       ("Mantıklı", "Neşeli", "İkna Edici", "Barışçıl"),
                       key="choose2",
                       horizontal=True)

    choose3 = st.radio("------------------------------------------- 3 -------------------------------------------",
                       ("Uysal", "Fedakar", "Sosyal", "İradeli"),
                       key="choose3",
                       horizontal=True)

    choose4 = st.radio("------------------------------------------- 4 -------------------------------------------",
                       ("İnsaflı", "Denetimli", "Yarışçıl", "İnandırıcı"),
                       key="choose4",
                       horizontal=True)

    choose5 = st.radio("------------------------------------------- 5 -------------------------------------------",
                       ("Ferahlatıcı", "Saygılı", "İyi dinleyici", "Becerikli"),
                       key="choose5",
                       horizontal=True)

    choose6 = st.radio("------------------------------------------- 6 -------------------------------------------",
                       ("Hoşnut", "Duyarlı", "Kendine güvenen", "Cesur"),
                       key="choose6",
                       horizontal=True)

    choose7 = st.radio("------------------------------------------- 7 -------------------------------------------",
                       ("Planlı", "Sabırlı", "Olumlu", "Teşvik edici"),
                       key="choose7")

    choose8 = st.radio("------------------------------------------- 8 -------------------------------------------",
                       ("Emin", "Kendiliğinden", "Programa bağlı", "Utangaç"),
                       key="choose8")

    choose9 = st.radio("------------------------------------------- 9 -------------------------------------------",
                       ("Düzenli", "İyiliksever", "Dobra", "iyimser"),
                       key="choose9")

    choose10 = st.radio("------------------------------------------- 10 -------------------------------------------",
                        ("Arkadaşçıl", "Sadık", "Komik", "Baskıcı"),
                        key="choose10")

    choose11 = st.radio("------------------------------------------- 11 -------------------------------------------",
                        ("Cesaretli", "Hoş", "Diplomatik", "Detaycı"),
                        key="choose11")

    choose12 = st.radio("------------------------------------------- 12 -------------------------------------------",
                        ("Esin Kaynağı", "Tutarlı", "Kültürlü", "Güvenli"),
                        key="choose12",
                        horizontal=True)
    bir = 5
    iki = 10
    uc = 2
    dort = 1
    if choose1 == "Hareketli":
        bir += 1
    return bir, iki, uc, dort


