from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from random import randrange
from datetime import datetime
import time

ua = UserAgent()
userAgent = ua.random
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={userAgent}")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(executable_path=r"chromedriver.exe", options=options)

def translate_term(text, target_lang, source_lang="auto"):
    translation = 'N/A'

    try:
        browser.get(f"https://translate.google.com/?sl={source_lang}&tl={target_lang}&text={text}&op=translate")
        condition = EC.presence_of_element_located((By.XPATH, f"//span[@data-language-for-alternatives='{target_lang}']/span[1]"))
        element = WebDriverWait(browser, 10).until(condition)
        translation = element.text
        time.sleep(randrange(2))
    except Exception:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Something went wrong at: ", current_time)        

    return translation
    
if __name__ == "__main__":
    print(translate_term(text="maison", target_lang="en"))
    print(translate_term(text="book", target_lang="pt") )
    browser.close()
