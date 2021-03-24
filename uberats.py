from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

numero_faturas = 0

browser = webdriver.Chrome()

cliente = "20239 Expo"
mail = "sushiboy@ubereats.pt"
password = "0a23cd59"
pin = "1234"
data = "2020/10/01 – 2020/10/31"

url = "https://auth.uber.com/login/?breeze_local_zone=dca11&next_url=https%3A%2F%2Frestaurant.uber.com%2F&state=GkeCtzq_4LUTHdtUQpiO8ldPqDyui02qg9ZTmud9HhY%3D"
browser.get(url)

try:
    user_element = browser.find_element_by_xpath('//*[@id="useridInput"]')

except:
    print("User_element not found")

user_element.send_keys(mail)
user_element.submit()

sleep(5)

try:
    password_btn = browser.find_element_by_xpath('/html/body/div[1]/div/div/div/div/form/input[2]')
except:
    print("password_btn not found")

password_btn.send_keys(password)
password_btn.submit()

sleep(5)

try:
    pin_element = browser.find_element_by_xpath('/html/body/div/div/div/div/form/input')
except:
    print("pin_element not found")


pin_element.send_keys(pin)
enviar_btn = browser.find_element_by_xpath('/html/body/div/div/div/div/form/button')
enviar_btn.click()

sleep(10)
try:
    pagamentos_btn = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[1]/ul/li[8]/a')
except:
    pagamentos_btn = browser.find_element_by_xpath('/html/body/div/div/main/div/div/div[1]/ul/li[5]/a/div')


pagamentos_btn.click()

sleep(5)

faturas_btn = browser.find_element_by_xpath('//*[@id="app-content"]/div/main/div/div[2]/div[1]/div/span/ul/li[2]/a')
faturas_btn.click()

sleep(5)
try:
    opcoes_faturas = browser.find_element_by_xpath('/html/body/div/div/div[1]/div/div[2]/div[2]/div[2]/div[1]/div/div[1]/div/div/div[1]/div[1]')

except:
    print("opcoes_faturas not found")


opcoes_faturas.click()
sleep(5)

try:
    estafeta_restaurante = browser.find_element_by_xpath('//*[@id="bui-8"]/div')
except:
    print("estafeta_btn not found")


estafeta_restaurante.click()
sleep(5)

try:
    data_input = browser.find_element_by_xpath('//*[@id="wrapper"]/div[1]/div/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div/div/input')

except:
    print("data not found")


browser.execute_script("arguments[0].value = '{}';".format(data), data_input)
sleep(2)
data_input.send_keys(Keys.TAB)
sleep(10)

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

print("Numero de Faturas do cliente ",cliente," = ", numero_faturas)