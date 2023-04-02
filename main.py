from selenium import webdriver

proxy_host = "" # endereco.do.proxy
proxy_port = "" # porta
proxy_user = ""#usuario
proxy_pass = ""#senha

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=http://%s:%s@%s:%s' % (proxy_user, proxy_pass, proxy_host, proxy_port))

driver = webdriver.Chrome(options=chrome_options)

# Agora você pode usar o navegador como quiser, usando o endereço IP do proxy
driver.get("https://www.exemplo.com")
