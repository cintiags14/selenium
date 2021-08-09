
from selenium.webdriver import Firefox
from time import sleep # importando sleep para que o selenium espere antes de procurar em elemento

booklist = 'https://my-simple-book-list.herokuapp.com'

browser = Firefox()

browser.get(booklist)

# sleep(3) 

botao = browser.find_element_by_tag_name('button')
botao.click()

sleep(1)
botaocancel = browser.find_element_by_class_name('cancel')

botaocancel.click()

# browser.quit()