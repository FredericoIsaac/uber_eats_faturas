import csv
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


numero_faturas = 0
edge_driver_path = "msedgedriver.exe"
browser = webdriver.Edge(executable_path=edge_driver_path)
browser.get('https://auth.uber.com/login/?breeze_local_zone=dca1&next_url=https%3A%2F%2Frestaurant.uber.com%2F&state=suD9oATJlqpRX5ebqOwtuGnqY2WIoyABn_6oLa4y7J0%3D')

continue_ = input("Primeiro vai até pagamentos e colocar tudo pronto para fazer download ")

try:
    seguinte_btn = browser.find_element_by_xpath('/html/body/div/div/div[1]/div/div[2]/div[2]/div[2]/div[3]/button[2]')  
except:
    print("seguinte button not found")

while seguinte_btn.is_enabled():
    sleep(3)
    try:
        donwload_elements = browser.find_elements_by_xpath('//*[@id="wrapper"]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div[2]//a[@href]')
    except:
        print("donwload_elements not found")

    sleep(2)
    for donwload_href in donwload_elements:
        donwload_href.click()
        numero_faturas += 1
    sleep(2)
    try:
        seguinte_btn = browser.find_element_by_xpath('/html/body/div/div/div[1]/div/div[2]/div[2]/div[2]/div[3]/button[2]')  
    except:
        print("seguinte button 2 not found")
    
    seguinte_btn.click()

sleep(5)
try:
    donwload_elements = browser.find_elements_by_xpath('//*[@id="wrapper"]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div[2]//a[@href]')
except:
    print("donwload_elements final not found")

print(donwload_elements)
sleep(2)
for donwload_href in donwload_elements:
    donwload_href.click()
    numero_faturas += 1

print("Numero de Faturas do cliente  = ", numero_faturas)
