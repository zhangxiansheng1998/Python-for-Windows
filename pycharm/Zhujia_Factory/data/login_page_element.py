from selenium.webdriver.common.by import By

website={'url':'http://admin.huijinwei.com/login'}

login_element={
    'username_ele':(By.XPATH,'/html/body/div/div/div/div[2]/form/div[1]/div/div/div/input'),
    'password_ele':(By.XPATH,'/html/body/div/div/div/div[2]/form/div[2]/div/div/div/input'),
    'login_button': (By.XPATH, '//*[@id="app"]/div/div/div[2]/form/button')
}