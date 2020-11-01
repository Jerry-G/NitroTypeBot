from selenium import webdriver
import time
#Following are optional required
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options

username = "YOUR_USERNAME_HERE"
passwd = "YOUR_PASSWORD_HERE"
# ublock origin extension  sorry nitrotype but this makes bot consistent
path_to_extension = '/home/jg/code/bots/typer/1.30.2_0u'
chrome_options = Options()
chrome_options.add_argument('load-extension=' + path_to_extension)
#chrome_options.add_argument("--headless")
lines = 1


# run forever
while True:
  browser = webdriver.Chrome(executable_path="/usr/lib/chromium/chromedriver", options=chrome_options)
  browser.create_options()
  # open browser
  browser.get("https://nitrotype.com/login")
  time.sleep(3)
  usernameBox = browser.find_element_by_id("username")
  passwordBox = browser.find_element_by_id("password")

  usernameBox.send_keys(username)
  passwordBox.send_keys(passwd)
    
  # login
  browser.find_elements_by_xpath("//*[contains(text(), 'Log In')]")[0].click()
  time.sleep(6)
  browser.find_elements_by_xpath("//*[contains(text(), 'Race Now')]")[0].click()

  # race 12 times then re-open browse
  counter = 1
  while counter < 13:
    time.sleep(1)
    # wait for text box to appear
    try:
      dash = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "dash-copy")))
    except:
      break
    # grab text and clean it
    text = dash.get_attribute('innerHTML')
    text = text.replace('<span class="dash-word">','')
    text = text.replace('</span>','')
    text = text.replace('<span class="dash-letter is-waiting">','')
    text = text.replace('<span class="dash-letter">','')
    text = text.replace('&nbsp;',' ')
    text = text.replace('<img alt="Finish" src="/dist/site/images/track/textures/finish_flag.png">',' ')
    print(f'{lines} - {text}')
    lines= lines +1 

    try:
      element = browser.find_element_by_class_name("dash-copy-input")
    except:
      break
    # race starts 4 seconds after textbox appears
    time.sleep(4.05)
    for letter in text:
      try:
        element.send_keys(letter)
      except:
        break
      # this delay makes WPM
      time.sleep(1.0 / 32.0)
    time.sleep(1.0)
    time.sleep(5.0)

    try:
      WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(@class,'animate--iconSlam')]"))).click();
    except:
      break
    counter = counter + 1
  browser.close()
