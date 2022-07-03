from unicodedata import name
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

df = pd.read_csv('school_record.csv')

browser = webdriver.Chrome(executable_path='/Users/saadiqbal/chromedriver/chromedriver')

for index in df.index:
    time.sleep(2)
    browser.get('https://docs.google.com/forms/d/e/1FAIpQLSetyb6UuSRIq37V0y9w9z3D0ntnkQTL-cIN7g7FGYGA4k3-QA/viewform')
    row_data = df.loc[index]
    time.sleep(2)

    # sending name to the input field
    name_input = browser.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    name_input.send_keys(str(row_data['Name']))


    # sending age to the input field 
    age_input = browser.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    age_input.send_keys(str(row_data['Age']))

    #sending gender
    if row_data['Gender'] == "Male":
        radio_gender = browser.find_element(By.XPATH, '//*[@id="i13"]/div[3]/div')
    elif row_data['Gender'] == "Female":
        radio_gender = browser.find_element(By.XPATH, '//*[@id="i16"]/div[3]')
    else:
        radio_gender = browser.find_element(By.XPATH, '//*[@id="i19"]/div[3]')
    radio_gender.click()

    #sending email
    email_input = browser.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
    email_input.send_keys(str(row_data['Email']))

    #Student status
    stu_status = browser.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[1]/div[1]/span')
    stu_status.click()
    time.sleep(2)
    if row_data['Status'] == "Full-time":
        status_select = browser.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[2]/div[3]/span')
    elif row_data['Status'] == "Part-time":
        status_select = browser.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[2]/div[4]/span')
    elif row_data['Status'] == "Graduated":
        status_select = browser.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[2]/div[6]/span')
    else:
        status_select = browser.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[2]/div[5]/span')
    status_select.click()

    submit_btn = browser.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_btn.click()

    # confirmation, Record has been added successfully or not.
    confirmation = browser.find_element(By.CLASS_NAME, "vHW8K")
    if confirmation.text == "Your response has been recorded.":
        print("Record", row_data['Sr. #'],"added successfully!")

print("All records added successfully!")
