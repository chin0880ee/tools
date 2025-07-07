import requests
from bs4 import BeautifulSoup

def download_file(url):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk:
                f.write(chunk)
    return local_filename


httplink = [
"https://www.dmhy.org/topics/view/693073_04_Aharen-san_wa_Hakarenai_S2_01_1080p.html",
"https://www.dmhy.org/topics/view/693539_04_Aharen-san_wa_Hakarenai_S2_02_1080p.html",
"https://www.dmhy.org/topics/view/694060_04_Aharen-san_wa_Hakarenai_S2_03_1080p.html",
"https://www.dmhy.org/topics/view/694522_04_Aharen-san_wa_Hakarenai_S2_04_1080p.html",
"https://www.dmhy.org/topics/view/695250_04_Aharen-san_wa_Hakarenai_S2_05_1080p.html",
"https://www.dmhy.org/topics/view/695459_04_Aharen-san_wa_Hakarenai_S2_06_1080p.html",
"https://www.dmhy.org/topics/view/695714_04_Aharen-san_wa_Hakarenai_S2_07_1080p.html",
"https://www.dmhy.org/topics/view/696132_04_Aharen-san_wa_Hakarenai_S2_08_1080p.html",
"https://www.dmhy.org/topics/view/696581_04_Aharen-san_wa_Hakarenai_S2_09_1080p.html",
"https://www.dmhy.org/topics/view/697117_04_Aharen-san_wa_Hakarenai_S2_10_1080p.html",
"https://www.dmhy.org/topics/view/697713_04_Aharen-san_wa_Hakarenai_S2_11_1080p.html",
"https://www.dmhy.org/topics/view/698212_04_Aharen-san_wa_Hakarenai_S2_12_1080p.html",
# "https://www.dmhy.org/topics/view/698436_Deki_Chau_Made_Kon_01_1080p.html",
# "https://www.dmhy.org/topics/view/693530_Ballpark_de_Tsukamaete_01_1920x1080_AVC_AAC_MP4.html",
# "https://www.dmhy.org/topics/view/693602_Ballpark_de_Tsukamaete_02_1920x1080_AVC_AAC_MP4.html",
# "https://www.dmhy.org/topics/view/693607_Ballpark_de_Tsukamaete_03_1920x1080_AVC_AAC_MP4.html",
# "https://www.dmhy.org/topics/view/693884_Ballpark_de_Tsukamaete_04_1920x1080_AVC_AAC_MP4.html",
# "https://www.dmhy.org/topics/view/694348_Ballpark_de_Tsukamaete_05_1920x1080_AVC_AAC_MP4.html",
# "https://www.dmhy.org/topics/view/694808_Ballpark_de_Tsukamaete_06_1920x1080_AVC_AAC_MP4.html",
# "https://www.dmhy.org/topics/view/695435_Ballpark_de_Tsukamaete_07_1920x1080_AVC_AAC_MP4.html",
# "https://www.dmhy.org/topics/view/695653_Ballpark_de_Tsukamaete_08_1920x1080_AVC_AAC_MP4.html",
# "https://www.dmhy.org/topics/view/696053_Ballpark_de_Tsukamaete_08_1920x1080_AVC_AAC_MP4.html",
# "https://www.dmhy.org/topics/view/696524_Ballpark_de_Tsukamaete_10_1920x1080_AVC_AAC_MP4.html",
# "https://www.dmhy.org/topics/view/696965_Ballpark_de_Tsukamaete_11_1920x1080_AVC_AAC_MP4.html",
# "https://www.dmhy.org/topics/view/697455_Ballpark_de_Tsukamaete_12_1920x1080_AVC_AAC_MP4.html",
# "https://www.dmhy.org/topics/view/693247_04_Apocalypse_Hotel_01_1080p.html",
# "https://www.dmhy.org/topics/view/693683_04_Apocalypse_Hotel_02_1080p.html",
# "https://www.dmhy.org/topics/view/694744_04_Apocalypse_Hotel_03_1080p.html",
# "https://www.dmhy.org/topics/view/694820_04_Apocalypse_Hotel_04_1080p.html",
# "https://www.dmhy.org/topics/view/695362_04_Apocalypse_Hotel_05_1080p.html",
# "https://www.dmhy.org/topics/view/695699_04_Apocalypse_Hotel_06_1080p.html",
# "https://www.dmhy.org/topics/view/695956_04_Apocalypse_Hotel_07_1080p.html",
# "https://www.dmhy.org/topics/view/696849_04_Apocalypse_Hotel_08_1080p.html",
# "https://www.dmhy.org/topics/view/696851_04_Apocalypse_Hotel_09_1080p.html",
# "https://www.dmhy.org/topics/view/698215_04_Apocalypse_Hotel_10_1080p.html",
# "https://www.dmhy.org/topics/view/698216_04_Apocalypse_Hotel_11_1080p.html",
# "https://www.dmhy.org/topics/view/698228_04_Apocalypse_Hotel_12_1080p.html",
]


torrentid = []
magnetlink = []


for httpmount in httplink:
  response = requests.get(
      httpmount)
  soup = BeautifulSoup(response.text, "html.parser")

  titles = soup.find_all("div", id="tabs-1")
  for title in titles:
    myto = "https:"+title.find_all("a")[0].get('href')
    torrentid.append(myto[31:])

    download_file(myto)

    target = ""
    head = 100
    mag1 = title.find_all("p")[0].find_all("p")[0].text[10:]
    mag2 = title.find_all("p")[0].find_all("p")[1].text[16:]
    magnetlink.append([mag1,mag2])

for i in torrentid:
  print(i)
for i in magnetlink:
  print(i)
