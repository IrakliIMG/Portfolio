from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests


Path = "C:\Program Files (x86)\chromedriver.exe"

def send_msg(text):
   token = "5638036248:AAG9PYDy5SXKtHZJHREn5GkWD77jMDUsNMo"
   chat_id = "-865884116"
   url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
   results = requests.get(url_req)
   print(results.json())


driver = webdriver.Chrome(Path)
driver.maximize_window()

driver.get("https://alta.ge/?subcats=Y&pcode_from_q=Y&pshort=Y&pfull=Y&pname=Y&pkeywords=Y&search_performed=Y&q=Positive+vibration&dispatch=products.search")

whiteMarlyAlta = driver.find_element(By.ID, "sec_discounted_price_25739").text
altaMarlyWhite = "ალტაში თეთრი Positive Vibration ღირს "+ whiteMarlyAlta + " ₾"
send_msg(altaMarlyWhite)

blackMarlyAlta = driver.find_element(By.ID,"sec_discounted_price_28329").text
altaMarlyBlack = "ალტაში შავი Positive Vibration ღირს "+ blackMarlyAlta + " ₾"
send_msg(altaMarlyBlack)


driver.get("https://alta.ge/?subcats=Y&pcode_from_q=Y&pshort=Y&pfull=Y&pname=Y&pkeywords=Y&search_performed=Y&q=510+BT&dispatch=products.search")

blackJblAlta = driver.find_element(By.ID, "sec_discounted_price_36569").text
altaJbl = "ალტაში JBL Tune 510BT ფასია - "+ blackJblAlta + " ₾"
send_msg(altaJbl)

driver.get("https://zoommer.ge/jbl-tune-t510-bt-wireless-on-ear-headphones-black")

blackJblZoommer = driver.find_element(By.CSS_SELECTOR, "#pd-r-content > div.form-group.only_for_desktop_laptop > div:nth-child(1) > div.price.new_price.has_old_price").text
zoommerJbl = "ზუმერში JBL Tune 510BT ფასია - "+ blackJblZoommer + " ₾"
send_msg(zoommerJbl)

driver.quit()
