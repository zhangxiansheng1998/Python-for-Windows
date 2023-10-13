from selenium.webdriver.common.by import By
'''
    '': (By.XPATH,''),
'''

button = {
    'shop_list':(By.XPATH,'/html/body/div[1]/div/div[2]/div[1]/div/div[1]/div[2]/div/div/p[1]'),
    'add_shop':(By.XPATH,'/html/body/div[1]/div/div[2]/div[1]/div/div[1]/div[2]/div/div/p[2]')
}

shop_list = {
    'shop_status': (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/div/div[1]/div/table/tbody/tr[1]/td[5]/div/div/span'),
    'shop_details': (By.XPATH,'//*[@id="main"]/div[2]/div[1]/div[1]/div[3]/div/div[1]/div/table/tbody/tr[1]/td[8]/div/button[1]/span/span'),
    'shop_details_return': (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[1]/div[2]/button/span'),
    'today_income': (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/div/div[1]/div/table/tbody/tr[1]/td[8]/div/button[2]/span/span'),
    'today_income_close': (By.XPATH, '//*[@id="main"]/div[2]/div[3]/div/div/header/button/i/svg'),
    'custom_income': (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/div/div[1]/div/table/tbody/tr[1]/td[8]/div/button[3]/span/span'),
    'enter_amount': (By.XPATH, '/html/body/div[3]/div/div/div[2]/div[2]/div[1]/div/input'),
    'custom_income_confirm': (By.XPATH, '/html/body/div[3]/div/div/div[3]/button[2]'),
    'custom_income_cancel': (By.XPATH, '/html/body/div[3]/div/div/div[3]/button[1]'),
    'custom_income_close': (By.XPATH, '/html/body/div[3]/div/div/div[1]/button'),
    'income_code': (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/div/div[1]/div/table/tbody/tr[1]/td[8]/div/button[4]/span/span'),
    'shop_code': (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/div/div[1]/div/table/tbody/tr[1]/td[8]/div/button[5]/span/span'),
    'delete_shop': (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/div/div[1]/div/table/tbody/tr[1]/td[8]/div/button[6]/span/span'),
    'add_shop_button': (By.XPATH, '')
}