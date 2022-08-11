from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

size=5

#mail="15jjsnpqnm@edu.email.edu.pl"
#password="uxkrzmiv886"
f = open('LoginData.txt', 'r')

for i in range(size):
    mail=f.readline()
    password=f.readline()
    f.readline()
    f.readline()
    mail=mail.strip() #remove the newline to avoid moving to next page instantly after pasting
    password=password.strip() 
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    #options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("window-size=1920,1080")
    options.add_argument("user-agent=Chrome/74.0.3729.169")
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
    driver.get("https://twitter.com/i/flow/login")



    time.sleep(3)
    m=driver.find_element("xpath","//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
    m.send_keys(mail)
    time.sleep(1)
    #click next
    driver.find_element("xpath","//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]").click()
    time.sleep(4)

    #box to type password
    p=driver.find_element("xpath","//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
    p.send_keys(password)

    driver.find_element("xpath","//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div").click()

    time.sleep(3.5)
    #t=driver.find_element("xpath","//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div")
    #t.send_keys('we are taking over #EktelionArmy')
    
    #t.send_keys(Keys.RETURN)


    #search
    driver.find_element("xpath","//*[@id='react-root']/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[2]").click()

    time.sleep(3)



    e=driver.find_element("xpath","//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/label/div[2]/div/input")
    e.send_keys('EktelionLeader')
    time.sleep(2)
    try:
        driver.find_element("xpath","//*[@id='typeaheadDropdown-2']/div[3]/div").click()
    except:
        pass
    time.sleep(2)    
    #click on followers
    #driver.find_element("xpath","//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div/div[2]/div[4]/div[2]/a").click()
    #time.sleep(1.3)
    #click follow?
    try:
        flist=driver.find_element("xpath","//*[@aria-label='Follow MHenderson257']")
    except:
        print("one")
        pass

    time.sleep(2)
    driver.find_element("xpath","//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div[2]/div[1]/div").click()
    time.sleep(3)    
    driver.quit()
    time.sleep(1)

f.close()


