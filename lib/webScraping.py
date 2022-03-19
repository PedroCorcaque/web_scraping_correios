from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')
DRIVER = webdriver.Chrome('/home/pedro/Workspace/DevChallenge/web_scraping_correios/lib/chromedriver', chrome_options=options)
URL_CORREIOS = 'https://buscacepinter.correios.com.br/app/endereco/index.php'
XPATH_TO_INPUT = '//*[@id="endereco"]'
XPATH_TO_BUTTON = '//*[@id="btn_pesquisar"]'

XPATH_TO_RUA = '/html/body/main/form/div[1]/div[2]/div/div[3]/table/tbody/tr/td[1]'
XPATH_TO_BAIRRO = '/html/body/main/form/div[1]/div[2]/div/div[3]/table/tbody/tr/td[2]'
XPATH_TO_CIDADE = '/html/body/main/form/div[1]/div[2]/div/div[3]/table/tbody/tr/td[3]'
XPATH_TO_CEP = '/html/body/main/form/div[1]/div[2]/div/div[3]/table/tbody/tr/td[4]'

def getAddressFromResults():
    rua = DRIVER.find_element_by_xpath(XPATH_TO_RUA)
    bairro = DRIVER.find_element_by_xpath(XPATH_TO_BAIRRO)
    cidade = DRIVER.find_element_by_xpath(XPATH_TO_CIDADE)
    return [rua.text, bairro.text, cidade.text]

def sendCEPToFindAddress(cep: str):
    DRIVER.get(URL_CORREIOS)
    DRIVER.implicitly_wait(0.5)
    input_layer = DRIVER.find_element_by_xpath(XPATH_TO_INPUT)
    button_layer = DRIVER.find_element_by_xpath(XPATH_TO_BUTTON)
    input_layer.send_keys(cep)
    button_layer.click()
    DRIVER.implicitly_wait(0.5)
    return getAddressFromResults()