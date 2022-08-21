from re import I
from select import kqueue
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
    mavi, sari, kirmizi, yesil = 0, 0, 0, 0
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
                        key="choose7",
                        horizontal=True)

    choose8 = st.radio("------------------------------------------- 8 -------------------------------------------",
                        ("Emin", "Kendiliğinden", "Programa bağlı", "Utangaç"),
                        key="choose8",
                        horizontal=True)

    choose9 = st.radio("------------------------------------------- 9 -------------------------------------------",
                        ("Düzenli", "İyiliksever", "Dobra", "İyimser"),
                        key="choose9",
                        horizontal=True)

    choose10 = st.radio("------------------------------------------- 10 -------------------------------------------",
                        ("Arkadaşçıl", "Sadık", "Komik", "Baskıcı"),
                        key="choose10",
                        horizontal=True)

    choose11 = st.radio("------------------------------------------- 11 -------------------------------------------",
                        ("Cesaretli", "Hoş", "Diplomatik", "Detaycı"),
                        key="choose11",
                        horizontal=True)

    choose12 = st.radio("------------------------------------------- 12 -------------------------------------------",
                        ("Esin Kaynağı", "Tutarlı", "Kültürlü", "Güvenli"),
                        key="choose12",
                        horizontal=True)

    choose13 = st.radio("------------------------------------------- 13 -------------------------------------------",
                        ("İdealist", "Bağımsız", "Zararsız", "Heyecanlandırıcı"),
                        key="choose13",
                        horizontal=True)

    choose14 = st.radio("------------------------------------------- 14 -------------------------------------------",
                        ("Coşkun", "Kesin", "Kuru esprili", "Derin düşünceli"),
                        key="choose14",
                        horizontal=True)

    choose15 = st.radio("------------------------------------------- 15 -------------------------------------------",
                        ("Aracı", "Ahenkli", "Harekete geçiren", "Kolay kaynaşır"),
                        key="choose15",
                        horizontal=True)

    choose16 = st.radio("------------------------------------------- 16 -------------------------------------------",
                        ("İnce düşünceli", "İş Bitirici", "Konuşma yanlısı", "Hoşgörülü"),
                        key="choose16",
                        horizontal=True)

    choose17 = st.radio("------------------------------------------- 17 -------------------------------------------",
                        ("Destekleyen", "Samimi", "Lider", "Canlı"),
                        key="choose17",
                        horizontal=True)

    choose18 = st.radio("------------------------------------------- 18 -------------------------------------------",
                        ("Halinden memnun", "Başkan, Şef", "Araştırmacı", "Şirin"),
                        key="choose18",
                        horizontal=True)

    choose19 = st.radio("------------------------------------------- 19 -------------------------------------------",
                        ("Mükemmeliyetçi", "Cana yakın", "Üretici", "Popüler"),
                        key="choose19",
                        horizontal=True)

    choose20 = st.radio("------------------------------------------- 20 -------------------------------------------",
                        ("Cömert", "Atılgan", "Terbiyeli", "Dengeli"),
                        key="choose20",
                        horizontal=True)

    st.markdown("""
            <p style='text-align: center; margin-bottom: 25px; margin-top: 25px;'>
            Zayıf Yönler. Her dört seçenekten birini seçiniz.
            </p>
        """, unsafe_allow_html=True
            )

    choose21 = st.radio("------------------------------------------- 21 -------------------------------------------",
                        ("İfadesiz", "Çekingen", "Utanması olmayan", "Zorba"),
                        key="choose21",
                        horizontal=True)

    choose22 = st.radio("------------------------------------------- 22 -------------------------------------------",
                        ("Disiplinsiz", "Sevimsiz", "Donuk", "Affetmez"),
                        key="choose22",
                        horizontal=True)

    choose23 = st.radio("------------------------------------------- 23 -------------------------------------------",
                        ("Ketum", "Kinci", "Dayanıksız", "Tekrarlayan"),
                        key="choose23",
                        horizontal=True)

    choose24 = st.radio("------------------------------------------- 24 -------------------------------------------",
                        ("Titiz", "Korkak", "Unutkan", "Açıksözlü"),
                        key="choose24",
                        horizontal=True)

    choose25 = st.radio("------------------------------------------- 25 -------------------------------------------",
                        ("Sabırsız", "Güvensiz", "Kararsız", "Laf kesici"),
                        key="choose25",
                        horizontal=True)

    choose26 = st.radio("------------------------------------------- 26 -------------------------------------------",
                        ("Sevilmeyen", "İşe karışmayan", "Ne yapacağı belirsiz", "Şefkatsiz"),
                        key="choose26",
                        horizontal=True)

    choose27 = st.radio("------------------------------------------- 27 -------------------------------------------",
                        ("Dik kafalı", "Gelişigüzel", "Zor beğenen", "Tereddütlü"),
                        key="choose27",
                        horizontal=True)

    choose28 = st.radio("------------------------------------------- 28 -------------------------------------------",
                        ("Sade", "Karamsar", "Kibirli", "Toleranslı"),
                        key="choose28",
                        horizontal=True)

    choose29 = st.radio("------------------------------------------- 29 -------------------------------------------",
                        ("Kolay sinirlenir", "Amaçsız", "Tartışmacı", "Soğuk"),
                        key="choose29",
                        horizontal=True)

    choose30 = st.radio("------------------------------------------- 30 -------------------------------------------",
                        ("Saf", "Olumsuz tavırlı", "Sinirli", "Kayıtsız"),
                        key="choose30",
                        horizontal=True)

    choose31 = st.radio("------------------------------------------- 31 -------------------------------------------",
                        ("Kaygılanan", "İçine Kapanık", "İşkolik", "Tanınmak isteyen"),
                        key="choose31",
                        horizontal=True)

    choose32 = st.radio("------------------------------------------- 32 -------------------------------------------",
                        ("Çok hassas", "Kaba", "Ürkek", "Çok konuşan"),
                        key="choose32",
                        horizontal=True)

    choose33 = st.radio("------------------------------------------- 33 -------------------------------------------",
                        ("Kuşkulu", "Organize olmamış", "Otoriter", "Kederli"),
                        key="choose33",
                        horizontal=True)

    choose34 = st.radio("------------------------------------------- 34 -------------------------------------------",
                        ("Tutarsız", "İçe dönük", "Hoşgörüsüz", "Sıradan"),
                        key="choose34",
                        horizontal=True)

    choose35 = st.radio("------------------------------------------- 35 -------------------------------------------",
                        ("Dağınık", "Huysuz", "Ağzında kelimeleri yuvarlayan", "İnsan kullanan"),
                        key="choose35",
                        horizontal=True)

    choose36 = st.radio("------------------------------------------- 36 -------------------------------------------",
                        ("Uyuşuk", "İnatçı", "Hava atan", "Kuşkucu"),
                        key="choose36",
                        horizontal=True)

    choose37 = st.radio("------------------------------------------- 37 -------------------------------------------",
                        ("Yalnız", "Denetleyici", "Tembel", "Gürültücü"),
                        key="choose37",
                        horizontal=True)

    choose38 = st.radio("------------------------------------------- 38 -------------------------------------------",
                        ("Miskin", "Şüpheci", "Çabuk öfkelenen", "Dikkatsiz"),
                        key="choose38",
                        horizontal=True)

    choose39 = st.radio("------------------------------------------- 39 -------------------------------------------",
                        ("İntikamcı", "Patavatsız", "İsteksiz", "Kötü dinleyici"),
                        key="choose39",
                        horizontal=True)

    choose40 = st.radio("------------------------------------------- 40 -------------------------------------------",
                        ("Uzlaşmacı", "Eleştirici", "Kurnaz", "Çabuk sıkılan"),
                        key="choose40",
                        horizontal=True)

    if choose1 == "Hareketli":
        sari += 1
    elif choose1 == "Sonuç odaklı":
        kirmizi += 1
    elif choose1 == "Analitik":
        mavi += 1
    else:
        yesil += 1

    if choose2 == "Neşeli":
        sari += 1
    elif choose2 == "İkna Edici":
        kirmizi += 1
    elif choose2 == "Mantıklı":
        mavi += 1
    else:
        yesil += 1

    if choose3 == "Sosyal":
        sari += 1
    elif choose3 == "İradeli":
        kirmizi += 1
    elif choose3 == "Uysal":
        mavi += 1
    else:
        yesil += 1 

    if choose4 == "İnandırıcı":
        sari += 1
    elif choose4 == "Yarışçıl":
        kirmizi += 1
    elif choose4 == "İnsaflı":
        mavi += 1
    else:
        yesil += 1 

    if choose5 == "Ferahlatıcı":
        sari += 1
    elif choose5 == "Becerikli":
        kirmizi += 1
    elif choose5 == "Saygılı":
        mavi += 1
    else:
        yesil += 1

    if choose6 == "Cesur":
        sari += 1
    elif choose6 == "Kendine güvenen":
        kirmizi += 1
    elif choose6 == "Duyarlı":
        mavi += 1
    else:
        yesil += 1

    if choose7 == "Teşvik edici":
        sari += 1
    elif choose7 == "Olumlu":
        kirmizi += 1
    elif choose7 == "Planlı":
        mavi += 1
    else:
        yesil += 1 

    if choose8 == "Kendiliğinden":
        sari += 1
    elif choose8 == "Emin":
        kirmizi += 1
    elif choose8 == "Programa bağlı":
        mavi += 1
    else:
        yesil += 1

    if choose9 == "İyimser":
        sari += 1
    elif choose9 == "Dobra":
        kirmizi += 1
    elif choose9 == "Düzenli":
        mavi += 1
    else:
        yesil += 1

    if choose10 == "Komik":
        sari += 1
    elif choose10 == "Baskıcı":
        kirmizi += 1
    elif choose10 == "Sadık":
        mavi += 1
    else:
        yesil += 1

    if choose11 == "Hoş":
        sari += 1
    elif choose11 == "Cesaretli":
        kirmizi += 1
    elif choose11 == "Detaycı":
        mavi += 1 
    else:
        yesil += 1

    if choose12 == "Esin kaynağı":
        sari += 1
    elif choose12 == "Güvenli":
        kirmizi += 1
    elif choose12 == "Kültürlü":
        mavi += 1
    else:
        yesil += 1

    if choose13 == "Heyecanlandırıcı":
        sari += 1
    elif choose13 == "Bağımsız":
        kirmizi += 1
    elif choose13 == "İdealist":
        mavi += 1
    else:
        yesil += 1

    if choose14 == "Coşkun":
        sari += 1
    elif choose14 == "Kesin":
        kirmizi += 1
    elif choose14 == "Derin düşünceli":
        mavi += 1

    if choose15 == "Kolay Kaynaşır":
        sari += 1
    elif choose15 == "Harekete geçiren":
        kirmizi += 1
    elif choose15 == "Ahenkli":
        mavi += 1
    else:
        yesil += 1

    if choose16 == "Konuşma yanlısı":
        sari += 1
    elif choose16 == "İş Bitirici":
        kirmizi += 1
    elif choose16 == "İnce düşünceli":
        mavi += 1
    else:
        yesil += 1

    if choose17 == "Canlı":
        sari += 1
    elif choose17 == "Lider":
        kirmizi += 1
    elif choose17 == "Samimi":
        mavi += 1
    else:
        yesil += 1

    if choose18 == "Şirin":
        sari += 1
    elif choose18 == "Başkan, Şef":
        kirmizi += 1
    elif choose18 == "Araştırmacı":
        mavi += 1
    else:
        yesil += 1

    if choose19 == "Popüler":
        sari += 1
    elif choose19 == "Üretici":
        kirmizi += 1
    elif choose19 == "Mükemmeliyetçi":
        mavi += 1
    else:
        yesil += 1

    if choose20 == "Cömert":
        sari += 1
    elif choose20 == "Atılgan":
        kirmizi += 1
    elif choose20 == "Terbiyeli":
        mavi += 1
    else:
        yesil += 1

    if choose21 == "Utanması olmayan":
        sari += 1
    elif choose21 == "Zorba":
        kirmizi += 1
    elif choose21 == "Çekingen":
        mavi += 1
    else:
        yesil += 1

    if choose22 == "Disiplinsiz":
        sari += 1
    elif choose22 == "Sevimsiz":
        kirmizi += 1
    elif choose22 == "Affetmez":
        mavi += 1
    else:
        yesil += 1

    if choose23 == "Tekrarlayan":
        sari += 1
    elif choose23 == "Dayanıksız":
        kirmizi += 1
    elif choose23 == "Kinci":
        mavi += 1
    else:
        yesil += 1

    if choose24 == "Unutkan":
        sari += 1
    elif choose24 == "Açıksözlü":
        kirmizi += 1
    elif choose24 == "Titiz":
        mavi += 1
    else:
        yesil += 1

    if choose25 == "Laf kesici":
        sari += 1
    elif choose25 == "Sabırsız":
        kirmizi += 1
    elif choose25 == "Güvensiz":
        mavi += 1
    else:
        yesil += 1

    if choose26 == "Ne yapacağı belirsiz":
        sari += 1
    elif choose26 == "Şefkatsiz":
        kirmizi += 1
    elif choose26 == "Sevilmeyen":
        mavi += 1
    else:
        yesil += 1

    if choose27 == "Gelişigüzel":
        sari += 1
    elif choose27 == "Dik kafalı":
        kirmizi += 1
    elif choose27 == "Zor beğenen":
        mavi += 1
    else:
        yesil += 1

    if choose28 == "Toleranslı":
        sari += 1
    elif choose28 == "Kibirli":
        kirmizi += 1
    elif choose28 == "Karamsar":
        mavi += 1
    else:
        yesil += 1

    if choose29 == "Kolay sinirlenir":
        sari += 1
    elif choose29 == "Tartışmacı":
        kirmizi += 1
    elif choose29 == "Soğuk":
        mavi += 1
    else:
        yesil += 1

    if choose30 == "Saf":
        sari += 1
    elif choose30 == "Sinirli":
        kirmizi += 1
    elif choose30 == "Olumsuz tavırlı":
        mavi += 1
    else:
        yesil += 1

    if choose31 == "Tanınmak isteyen":
        sari += 1
    elif choose31 == "İşkolik":
        kirmizi += 1
    elif choose31 == "İçine kapanık":
        mavi += 1
    else:
        yesil += 1

    if choose32 == "Çok konuşan":
        sari += 1
    elif choose32 == "Kaba":
        kirmizi += 1
    elif choose32 == "Çok hassas":
        mavi += 1
    else:
        yesil += 1

    if choose33 == "Organize olmamış":
        sari += 1
    elif choose33 == "Otoriter":
        kirmizi += 1
    elif choose33 == "Kederli":
        mavi += 1
    else:
        yesil += 1

    if choose34 == "Tutarsız":
        sari += 1
    elif choose34 == "Hoşgörüsüz":
        kirmizi += 1
    elif choose34 == "İçe dönük":
        mavi += 1
    else:
        yesil += 1

    if choose35 == "İnsan kullanan":
        sari += 1
    elif choose35 == "Dağınık":
        kirmizi += 1
    elif choose35 == "Huysuz":
        mavi += 1
    else:
        yesil += 1

    if choose36 == "Hava atan":
        sari += 1
    elif choose36 == "İnatçı":
        kirmizi += 1
    elif choose36 == "Kuşkucu":
        mavi += 1
    else:
        yesil += 1

    if choose37 == "Gürültücü":
        sari += 1
    elif choose37 == "Denetleyici":
        kirmizi += 1
    elif choose37 == "Yalnız":
        mavi += 1
    else:
        yesil += 1

    if choose38 == "Dikkatsiz":
        sari += 1
    elif choose38 == "Çabuk öfkelenen":
        kirmizi += 1
    elif choose38 == "Şüpheci":
        mavi += 1   
    else:
        yesil += 1

    if choose39 == "Kötü dinleyici":
        sari += 1
    elif choose39 == "Patavatsız":
        kirmizi += 1
    elif choose39 == "İntikamcı":
        mavi += 1
    else:
        yesil += 1

    if choose40 == "Çabuk sıkılan":
        sari += 1
    elif choose40 == "Kurnaz":
        kirmizi += 1
    elif choose40 == "Eleştirici":
        mavi += 1
    else:
        yesil += 1






    return mavi, sari, kirmizi, yesil

