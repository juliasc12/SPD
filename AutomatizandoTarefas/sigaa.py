from selenium import webdriver

username = input("digite o login do sigaa: ")
password = input("senha do sigaa: ")

driver=webdriver.Chrome()
driver.get("https://sig.ifsudestemg.edu.br/sigaa/verTelaLogin.do")

nome = driver.find_element_by_name("user.login")
nome.send_keys(username)

senha = driver.find_element_by_name("user.senha")
senha.send_keys(password)

login = driver.find_element_by_xpath("//input[@value='Entrar']")
login.submit()
