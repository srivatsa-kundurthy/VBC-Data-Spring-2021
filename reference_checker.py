from csv import reader
import csv
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def get_differences(filename):
    """

    :param l: list with [file, tag]
    :return: list with differences between elements, first number
    """

    employees = []
    with open(filename, 'r') as file:
        csv_parser = reader(file)
        rows = list(csv_parser)


        for elem in rows:
            if elem != []:
                employees.append(elem)

    first_num = employees[0][-1]

    positions = []
    for employee in employees:
        num = int(employee[-1])
        positions.append(num)

    return [positions[i+1] - positions[i] for i in range(len(positions)-1)], int(first_num)

def reference_good(text):
    """

    :param text: reference data from site
    :return: boolean describing whether the reference indicates the applicant is good or bad
    """
    blacklisted = open('bad_references.txt', 'r').read().split()
    lines = text.split('\n')
    flag = True
    for elem in lines:
        for word in elem.split():
            if word in blacklisted:
                flag = False
                print('word', word)
                break
    print('flag', flag)
    return flag









if __name__ == "__main__":
    write_to = 'best_assemblers.csv'
    read_from = 'assemblers.csv'


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

    sleep(7)
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

    """

    #click to correct elem

    #references link
    references = driver.find_element_by_xpath('//*[@id="vb77b2c7ad55285dba8b792b253f109ca"]')
    references.click()

    sleep(1)

    #reference text
    reference_text = driver.find_element_by_xpath('//*[@id="v7d8e32b7401f6b564f2c7e8904036c38"]')
    t = reference_text.text

    print(t)

    sleep(1)

    #exit references
    close_box = driver.find_element_by_xpath('/html/body/div[9]/div[1]/button/span[1]')
    close_box.click()
    """

    employees = []
    with open(read_from, 'r') as file:
        csv_parser = reader(file)
        rows = list(csv_parser)

        for elem in rows:
            if elem != []:
                employees.append(elem)

    print('full employees list', employees)

    previous = 0
    #current = int(employees[0][-1])

    best_candidates = []

    for employee in employees:
        current = int(employee[-1])

        #next button
        for i in range(current - previous):
            next = driver.find_element_by_xpath('//*[@id="v4235ab51262b0c1e2f7c901cfa23a1be"]/a')
            next.click()
            sleep(.25)

        # references link
        references = driver.find_element_by_xpath('//*[@id="vb77b2c7ad55285dba8b792b253f109ca"]')
        references.click()
        sleep(.25)

        # reference text
        reference_text = driver.find_element_by_xpath('//*[@id="v7d8e32b7401f6b564f2c7e8904036c38"]')
        t = reference_text.text

        if reference_good(t) == True:
            best_candidates = employee
            with open(write_to, 'a') as file:
                write = csv.writer(file)
                write.writerow(best_candidates)
            print(employee)


        # exit references
        close_box = driver.find_element_by_xpath('/html/body/div[9]/div[1]/button/span[1]')
        close_box.click()


        previous = current













