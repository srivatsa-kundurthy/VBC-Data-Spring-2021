from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import csv

def clicker(l):
    """
    :param l: heterogeneous list of length 3 of the format [number, file, tag]
    :return: void
    """

    dropdown = ActionChains(driver)
    sleep(1)
    for i in range(l[2]):
        sleep(1)
        dropdown.send_keys(Keys.DOWN)

    for i in range(l[0]):

        resume = driver.find_element_by_xpath('//*[@id="resume"]')
        t = resume.text
        data = t.split('\n')
        print(i)
        data.append(i)


        with open(l[1], 'a') as file:
            write = csv.writer(file)
            write.writerow(data)

        next = driver.find_element_by_xpath('//*[@id="v4235ab51262b0c1e2f7c901cfa23a1be"]/a')
        next.click()
        sleep(.25)




if __name__ == "__main__":
    driver = webdriver.Chrome(executable_path="C:\webdrivers\chromedriver.exe")
    creds = open('IGNORE_CREDS.txt', 'r').read().split()


    driver.get(creds[2])
    username = driver.find_elements_by_css_selector('div input')[1]
    sleep(1)
    username.send_keys(creds[0])

    sleep(1)

    password = driver.find_elements_by_css_selector('div input')[2]
    sleep(1)
    password.send_keys(creds[1] + Keys.ENTER)

    sleep(2)
    driver.get(creds[3])

    sleep(10)
    popup = driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/button')
    popup.click()


    sleep(3)
    actions = driver.find_elements_by_css_selector('div button')[7]
    actions.click()

    sleep(2)
    hire = driver.find_element_by_xpath('//*[@id="hireEmployees"]')
    hire.click()

    print('PLEASE CLICK INTENDED JOB TYPE.')
    sleep(10)

    #TODO: Ensure file names are correct
    assembler = [499, 'full_wheel_builders.csv', 0]
    wheel_builder = [836, 'full_wheel_builders.csv', 1]
    finisher = [434, 'full_finishers.csv', 2]
    frame_welder = [842, 'full_frame_welders.csv', 3]
    sys_admin = [678, 'full_sys_admins.csv', 4]
    ar_specialist = [673, 'full_ar_specialist.csv', 5]
    ap_specialist = [676, 'full_ap_specialist.csv', 6]
    purchaser = [677, 'full_purchasers.csv', 7]
    material_handler = [293, 'full_material_handlers.csv', 8]

    clicker(frame_welder)

    driver.close()

