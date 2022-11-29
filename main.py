import pandas as pd
import requests
from bs4 import BeautifulSoup
import json

response_list = []
rest_sirasi = []
rest_adlari = []
rest_linkleri = []
rest_illeri = []



def _responseleri_al():
    Cities = ["Adana", "Adıyaman", "Afyonkarahisar", "Ağrı", "Aksaray", "Amasya", "Ankara", "Antalya", "Ardahan", "Artvin", "Aydın", "Balıkesir", "Bartın", "Batman", "Bayburt", "Bilecik", "Bingöl", "Bitlis", "Bolu", "Burdur", "Bursa", "Çanakkale", "Çankırı", "Çorum", "Denizli", "Diyarbakır", "Düzce", "Edirne", "Elazığ", "Erzincan", "Erzurum", "Eskişehir", "Gaziantep", "Giresun", "Gümüşhane", "Hakkâri", "Hatay", "Iğdır", "Isparta", "İstanbul", "İzmir", "Kahramanmaraş", "Karabük", "Karaman", "Kars", "Kastamonu", "Kayseri", "Kilis", "Kırıkkale", "Kırklareli", "Kırşehir", "Kocaeli", "Konya", "Kütahya", "Malatya", "Manisa", "Mardin", "Mersin", "Muğla", "Muş", "Nevşehir", "Niğde", "Ordu", "Osmaniye", "Rize", "Sakarya", "Samsun", "Şanlıurfa", "Siirt", "Sinop", "Sivas", "Şırnak", "Tekirdağ", "Tokat", "Trabzon", "Tunceli", "Uşak", "Van", "Yalova", "Yozgat", "Zonguldak"]
    for i in Cities:
        url='https://www.yelp.com/search?find_desc=Restaurants&find_loc='+i+'2C+Turkey'
        response = requests.get(url)
        html_content = response.content
        response_list.append(html_content)

def _verileri_cek():
    for city in response_list:       
        soup = BeautifulSoup(city, 'html.parser')
        isim_kismi = soup.find_all(attrs={"data-testid" : "serp-ia-card"})
        for i in isim_kismi:
            baslik = i.findAll('h3')
            for j in baslik:
                spanlar= j.findAll('span')
                for k in spanlar:
                    linkler= j.findAll('a')
                    for n in linkler:
                        rest_adlari.append(n.get_text())
                        link = "https://www.yelp.com/"
                        rest_linkleri.append(link + n.get("href"))

if __name__ == "__main__":
    _responseleri_al()
    _verileri_cek()
    df = pd.DataFrame({
                    'Restoran İsmi': rest_adlari,
                    'Restoran Linki':rest_linkleri
                    })
    result = df.to_json(orient="records")
    with open(f"rest_veriler.json","w") as file:
            file.write(result)

