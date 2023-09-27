import requests
from bs4 import BeautifulSoup
from mail import mail

class products_list():
    def organize_products_list(productsList:str):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
        }

        page = requests.get('https://ofertas.canaltech.com.br/samsung/celulares-e-smartphones/samsung-galaxy-s23-ultra-512gb/', headers=headers)
                            
        soup = BeautifulSoup(page.text, 'html.parser')

        products = soup.find_all(class_='card-ofertas card-ofertas-item')

        productLinks = [];
        productPrices = [];

        for product in products:
            values = product.find_all(class_='valor')

            links = product.find('a', href=True)
            productLinks.append(links['href'])

            for value in values:
                price = value.find('span').text
                productPrices.append(price)

        for index, link in enumerate(productLinks):
            price = productPrices[index]
            productsList += f"<p> {link} - {price}</p>"

        mail.send_mail(productsList)
        print('Finalizou :)')