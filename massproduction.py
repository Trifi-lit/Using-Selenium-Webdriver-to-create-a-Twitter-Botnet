from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
import pyperclip

size=12
#mails=[""]*size
#passwords=[""]*size
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
#options.add_experimental_option('useAutomationExtension', False)
options.add_argument("window-size=1920,1080")
options.add_argument("user-agent=Chrome/74.0.3729.169")

f1 = open("data.txt", "r")
f2 = open('LoginData.txt', 'w')
for i in range(size):
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
    username=f1.readline()
    password=f1.readline()
    date=f1.readline()
    bio=f1.readline()
    f1.readline()
    [month,day,year]=date.split()

    driver.get("https://twitter.com")
    time.sleep(2)
    try:
        driver.find_element("xpath","//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/a").click()
    except:
        driver.quit()
        time.sleep(3)
        continue
    time.sleep(2.3)
    driver.find_element("xpath","//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/span").click()
    time.sleep(1)
    driver.find_element("xpath","//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/label/div/div[2]/div/input").send_keys(username)
    time.sleep(1)
    original_window = driver.current_window_handle
    driver.execute_script("window.open('about:blank','secondtab');")
    driver.switch_to.window("secondtab")



    driver.get("https://temp-mail.org/el/10minutemail")

    time.sleep(6.1)
    driver.find_element("xpath","/html/body/div[1]/div/div/div[2]/div[1]/form/div[2]/button").click()
    email=pyperclip.paste()
    time.sleep(0.6)

    driver.switch_to.window(original_window)
    time.sleep(0.8)


    mail=driver.find_element("xpath","//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/label/div/div[2]/div/input")
    mail.send_keys(Keys.CONTROL, 'v') #paste


    x=driver.find_element("xpath","//*[@id='SELECTOR_1']")
    drop=Select(x)
    drop.select_by_value(month)

    x=driver.find_element("xpath","//*[@id='SELECTOR_2']")
    drop=Select(x)
    drop.select_by_value(day)

    x=driver.find_element("xpath","//*[@id='SELECTOR_3']")
    drop=Select(x)
    drop.select_by_value(year)

    #click three times next
    time.sleep(1)
    driver.find_element("xpath","//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div").click()
    time.sleep(1)
    driver.find_element("xpath","//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div").click()
    time.sleep(1)
    driver.find_element("xpath",'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div').click()

    #go to mail tab to get the verification code
    driver.switch_to.window("secondtab")
    time.sleep(12)
    source=driver.find_element("xpath","/html/body/main/div[1]/div/div[2]/div[2]/div/div[1]/div/div[4]/ul/li[2]/div[2]/span/a")
    content=source.get_attribute("innerHTML").split() #get the verification code directly from inner HTML since clicking on the mail detects sus activity
    content=content[0]
    content=content.strip()
    print(content)
    time.sleep(0.6)

    driver.switch_to.window(original_window)
    time.sleep(0.5)

    #textbox to type in verification code
    verif=driver.find_element("xpath","//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")
    verif.send_keys(content)
    time.sleep(1)

    #click next after typing verification code
    driver.find_element("xpath","//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div").click()
    time.sleep(2)

    #textbox to write in the password
    try:
        pas=driver.find_element("xpath","//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div/label/div/div[2]/div[1]/input")
    except:
        break
    pas.send_keys(password)
    time.sleep(1)

    #click next after typing password
    driver.find_element("xpath","//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div").click()
    time.sleep(2.3)

    #skip photo
    try:
        driver.find_element("xpath","//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div").click()
    except:
        pass

    time.sleep(1.1)

    #bio text box
    try:
        biot=driver.find_element("xpath","//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/textarea")
        biot.send_keys(bio)
    except:
        pass
    time.sleep(1)
    #click next
    try:
        driver.find_element("xpath","//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div").click()
    except:
        pass
    time.sleep(1)

    #username
    try:
        usrn=driver.find_element("xpath","//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")
        usrn.send_keys(Keys.CONTROL, 'a')
        usrn.send_keys(username)
    except:
        pass
    #next
    try:
        driver.find_element("xpath","//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div").click()
    except:
        pass
    time.sleep(1)
    driver.quit()
    f2.write(email)
    f2.write('\n')
    f2.write(password)
    f2.write('\n\n')
    f2.flush()
    time.sleep(1)
    

f1.close()
f2.close()