from selenium import webdriver
#import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(executable_path="/Users/mudeepak/Downloads/chromedriver_mac64\ \(2\)/chromedriver")
driver.get("https://news.ycombinator.com/")
#time.sleep(10)

# for i in range(30):
#     print(driver.find_element(By.XPATH, "//*[@id=\'hnmain\']/tbody/tr[3]/td/table/tbody/tr['+i=']").getText())
# find web links
#link = driver.find_elements(By.TAG_NAME, 'a')
#value = driver.find_element(by=By.XPATH,value = "//*[@id=\"hnmain\"]/tbody/tr[3]/td/table/tbody/tr[" + str(i) + "]") .text

# print name of all links
#for i in link:
#   print(i.text)

# get text and print


#val = 1;
i = 1
j=1
while(i<30):
    print(j,end=' ')
    title = driver.find_element(by = By.XPATH,value = "/html/body/center/table/tbody/tr[3]/td/table/tbody/tr[" + str(i) + "]/td[3]/span/a").text
    print(title)
    i = i+3
    j=j+1





