import requests
from bs4 import BeautifulSoup

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}
url = 'https://www.coches.net/seat-toledo-2.0-tdi-140cv-sport-5p-diesel-2006-en-madrid-58396957-covo.aspx'


#  Function for scraping
def obtener_datos_coche(url):
    # Web request
    response = requests.get(url, headers=headers)
    print(f'Code Response: {response}\n\n')
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup)
    # Get specific data
    name = soup.find('h1',
                     {'class': 'mt-TitleBasic-title mt-TitleBasic-title--s mt-TitleBasic-title--black'}).text.strip()

    if not name:
        print("no hi ha nom")
    else:
        print(f'name: {name}')


if __name__ == '__main__':
    obtener_datos_coche(url)
