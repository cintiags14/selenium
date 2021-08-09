from selenium.webdriver import Firefox
from time import sleep 

booklist = 'https://my-simple-book-list.herokuapp.com'

browser = Firefox()

browser.get(booklist)

sleep(2)

def find_bay_text(browser, tag, text):

   elementos = browser.find_elements_by_tag_name(tag)

   for elemento in elementos:
       if elemento.text == text:
           return elemento


tablevazia = find_bay_text(browser, 'td', 'No Book Available.')

print ('Resultado é:',tablevazia.text)

browser.quit()