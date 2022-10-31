from utils import *
import matplotlib.pyplot as plt

head()
bir, iki, uc, dort = body()


ogr_ad = st.text_input("Adınız-Soyadınız")
ogr_no = st.text_input("Öğrenci Numaranız")



if st.button('Analiz Et'):
    if ogr_no == "" or ogr_ad == "":
        st.error("Adınızı ya da numaranızı girmediniz. Lütfen Kontrol edin.")
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
            save_file(file_name)
            st.success("Analiz Kaydedildi, kariyer@sakarya.edu.tr adresiyle iletişime geçebilirsiniz.")
            st.balloons()

version()
