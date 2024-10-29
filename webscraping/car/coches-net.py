import requests
from bs4 import BeautifulSoup

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

url = 'https://www.coches.net/seat-toledo-1.0-tsi-70kw-stsp-reference-edition-5p-gasolina-2018-en-guipuzcoa-58932064-covo.aspx0'140
1
#0.
#  Function for scraping
def obtener_datos_coche(url,):
  
  # Web request
  response = requests.get(url, headers=headers)
  print(response)
  soup = BeautifulSoup(response.text, 'html.parser')
  print(soup)
  # Get specific data
  name = soup.find('h1', {'class': 'mt-TitleBasic-title mt-TitleBasic-title--s mt-TitleBasic-title--black'}).text.strip()
  
  print(f'name: {name}')

  
if __name__ == '__main__':
  obtener_datos_coche(url)
