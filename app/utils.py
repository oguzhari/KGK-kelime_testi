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
                       key="choose7",
                       horizontal=True)

    choose8 = st.radio("------------------------------------------- 8 -------------------------------------------",
                       ("Emin", "Kendiliğinden", "Programa bağlı", "Utangaç"),
                       key="choose8",
                       horizontal=True)

    choose9 = st.radio("------------------------------------------- 9 -------------------------------------------",
                       ("Düzenli", "İyiliksever", "Dobra", "iyimser"),
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
                        ("Sade", "Karamsar", "Kibirli", "Töleranslı"),
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
                        ("Kaygılanan", "İçine Kapanık", "İş kolik", "Tanınmak istenen"),
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
                        ("Uyuşuk", "İnatçı", "Hava atan", "Kukucu"),
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
    bir = 5
    iki = 10
    uc = 2
    dort = 1
    if choose1 == "Hareketli":
        bir += 1
    return bir, iki, uc, dort


