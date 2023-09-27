from products_list import products_list

links = [
    'https://ofertas.canaltech.com.br/samsung/celulares-e-smartphones/samsung-galaxy-s23-ultra-256gb/',
    'https://ofertas.canaltech.com.br/samsung/celulares-e-smartphones/samsung-galaxy-s23-ultra-512gb/',
    'https://ofertas.canaltech.com.br/samsung/celulares-e-smartphones/galaxy-s23-ultra-1tb-5g/'
]

productsNames =[
    's23 Ultra 256gb',
    's23 Ultra 512gb',
    's23 Ultra 1tb',
]

productsList = ''

products_list.organize_products_list(productsList, links, productsNames)