from utils import *
import matplotlib.pyplot as plt
import send_mail

head()
bir, iki, uc, dort = body()


ogr_ad = st.text_input("Adınız-Soyadınız")
ogr_mail = st.text_input("Mail Adresiniz")
ogr_no = st.text_input("Öğrenci Numaranız")


if st.button('Analiz Et'):
    if ogr_no == "" or ogr_ad == "" or ogr_mail == "":
        st.error("Adınızı, öğrenci numaranızı veya mail adresini girmediniz. Lütfen Kontrol edin.")
    else:
        file_name = ogr_ad.title().strip() + "-" + ogr_no.strip() + ".png"

        labels = 'Ciddi', 'Dominant', 'İz Bırakan', 'Sadık'
        sizes = [bir, iki, uc, dort]
        explode = (0.1, 0.1, 0.1, 0)
        colours = {'Ciddi': 'b',
                   'Dominant': 'r',
                   'İz Bırakan': 'y',
                   'Sadık': 'g'}

        # Grafiğe en yüksek skoru alan rengi belirlemek ve yazmak
        max_score = max(sizes)
        max_score_index = sizes.index(max_score)
        max_score_label = labels[max_score_index]
        max_score_colour = colours[max_score_label]
        max_score_text = f"{max_score_label} (%{max_score})"

        fig, ax = plt.subplots()
        ax.title.set_text(ogr_ad.title().strip() + "-" + ogr_no.strip())
        ax.pie(sizes,
               labels=labels,
               explode=explode,
               colors=[colours[key] for key in labels],
               autopct='%1.1f%%',
               shadow=True,
               startangle=90)  # Equal aspect ratio ensures that pie is drawn as a circle.

        # texti en alta yaz
        ax.text(0, -1.5, max_score_text, color=max_score_colour, fontsize=12, ha='center')
        with st.empty():
            plt.savefig(file_name, dpi=400)
            st.success("Analiz oluşturuldu, kaydediliyor...")
            send_mail.send_analysis(ogr_mail, [file_name])
            st.success("Analiz Kaydedildi ve mail adresinize gönderildi, kariyer@sakarya.edu.tr adresiyle iletişime "
                       "geçebilirsiniz.")
        st.balloons()

version()
