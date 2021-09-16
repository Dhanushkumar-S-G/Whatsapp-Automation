from selenium import webdriver
import time

browser = webdriver.Chrome()

browser.get("https://web.whatsapp.com/")

name = input("Enter the name of the person/group : ")
count = int(input("Enter the number of times to be sent :"))
msg = input("Enter the msg : ")
delay = int(input('Enter the time delay'))
input("Press enter after scanning the QR code :")

grp_name =user = browser.find_element_by_xpath(f'//span[@title = "{name}"]')
grp_name.click()

msg_box = browser.find_elements_by_class_name("_13NKt")


status = 'y'
while status =='y': 
    for i in range(count):
        msg_box[1].send_keys(msg)
        time.sleep(delay)
        button = browser.find_element_by_class_name('_4sWnG')
        button.click()

    status = input("press y to continue")