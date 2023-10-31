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

        labels = 'Melankolik', 'Güçlü Klorik', 'Popüler-Optimist', 'Barışçıl-Soğukkanlı'
        sizes = [bir, iki, uc, dort]
        explode = (0.1, 0.1, 0.1, 0)
        colours = {'Melankolik': 'b',
                   'Güçlü Klorik': 'r',
                   'Popüler-Optimist': 'y',
                   'Barışçıl-Soğukkanlı': 'g'}

        fig, ax = plt.subplots()
        ax.title.set_text(ogr_ad.title().strip() + "-" + ogr_no.strip())
        ax.pie(sizes,
               labels=labels,
               explode=explode,
               colors=[colours[key] for key in labels],
               autopct='%1.1f%%',
               shadow=True,
               startangle=90)  # Equal aspect ratio ensures that pie is drawn as a circle.
        with st.empty():
            plt.savefig(file_name, dpi=400)
            st.success("Analiz oluşturuldu, kaydediliyor...")
            # save_file(file_name)
            send_mail.send_analysis(ogr_mail, [file_name])
            st.success("Analiz Kaydedildi, kariyer@sakarya.edu.tr adresiyle iletişime geçebilirsiniz.")
        st.balloons()

version()
