from selenium.webdriver import Firefox
from time import sleep
from selenium.webdriver.common.keys import Keys
url = "https://my-simple-book-list.herokuapp.com"

browser = Firefox()
browser.get(url)

botao = browser.find_element_by_class_name('btn-add')
botao.click()

sleep(1)


titulo = browser.find_element_by_name('title').send_keys('O dilema das redes')
autor = browser.find_element_by_name('author').send_keys('Cintia')
cod = browser.find_element_by_name('isbn').send_keys('9898')
salvar = browser.find_element_by_class_name('save')
salvar.click()








