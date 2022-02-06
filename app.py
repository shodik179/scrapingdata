import bs4
import requests
 
url = 'https://www.jadwalsholat.org/adzan/monthly.php?id=36'
contents = requests.get(url)
response = bs4.BeautifulSoup(contents.text,"html.parser")
data = response.find_all('tr','table_highlight')
data = data[0]
print("Jadwal Sholat untuk Bekasi, GMT +7")
print("februari 2022")
sholat = {}
i=0
for d in data:
    if i == 1:
        sholat['imsak'] = d.get_text()
    elif i ==2:
        sholat['subuh'] = d.get_text()
    elif i ==3:
        sholat['terbit'] = d.get_text()
    elif i ==4:
        sholat['dhuha'] = d.get_text()
    elif i ==5:
        sholat['dhuhur'] = d.get_text()
    elif i ==6:
        sholat['ashar'] = d.get_text()
    elif i ==7:
        sholat['magrib'] = d.get_text()
    elif i ==8:
        sholat['iysa'] = d.get_text()

    i += 1
print(sholat)