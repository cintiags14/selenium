from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from time import sleep
from urllib.parse import urlparse
from json import loads

url = 'https://my-simple-book-list.herokuapp.com'

firefox = Firefox()

firefox.get(url)


sleep(1)

def preenche_form(browser, titulo, autor, codigo):
    browser.find_element_by_class_name('btn-add').click()
    browser.find_element_by_name('title').send_keys('O dilema das redes')
    browser.find_element_by_name('author').send_keys('Cintia')
    browser.find_element_by_name('isbn').send_keys('9898')
    browser.find_element_by_class_name('save').click()


sleep(2)

estrutura = {
    'titulo': 'titulo',
    'autor': 'cintia',
    'codigo': '65'
}

preenche_form(firefox, **estrutura)

url_parseada = urlparse(firefox.current_url)

sleep(2)

firefox.quit()