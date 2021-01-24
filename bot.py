
from selenium import webdriver
import time
import csv

data = []
i = 0

driver = webdriver.Firefox(executable_path="geckodriver")
# link dos dados
driver.get("url")

login = driver.find_element_by_id('i0116')
login.send_keys('example@hotmail.com')

login = driver.find_element_by_id('idSIButton9')
login.click()

time.sleep(1)
password = driver.find_element_by_id('i0118')
password.send_keys('password')

time.sleep(5)
login = driver.find_element_by_id('idSIButton9')
login.click()

driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="WebApplicationFrame"]'))
time.sleep(30)
topics = driver.find_elements_by_xpath('/html/body/div[2]/form/div[2]/div[2]/div[1]/div[2]/div[1]/div[3]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/div')

with open('dados.csv', 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)

    for topic in topics:
        element = topic.find_element_by_tag_name('content')

        data.append(element.get_attribute('textContent'))

        element.click()


        time.sleep(20)
        element = topic.find_element_by_class_name('sectionList')
        subtopics = element.find_elements_by_tag_name('content')
        for subtopic in subtopics:
            data.append(subtopic.get_attribute('textContent'))

            subtopic.click()
            time.sleep(10)

            subjects = driver.find_elements_by_xpath('/html/body/div[2]/form/div[2]/div[2]/div[1]/div[2]/div[1]/div[3]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div')
            for subject in subjects:
                data.append(subject.get_attribute('textContent'))

                subject.click()
                time.sleep(10)
                text_lines = driver.find_elements_by_xpath('/html/body/div[2]/form/div[2]/div[2]/div[1]/div[2]/div[3]/div/div[3]/div[2]/div/div[3]/div/div[2]/div/div[3]/div')

                text = ''

                for lines in text_lines:
                    elements = lines.find_elements_by_class_name('NormalTextRun')

                    if len(elements) > 1:
                        for element in elements:
                            text += element.get_attribute('textContent')
                    else:
                        try:
                            content = elements[0].get_attribute('textContent')
                            if content == '':
                                text += '\n'
                            else: text += content + '\n'
                        except:
                            pass
                print(text)
                data.append(text)
                print(data)
                # escreve os dados no arquivo csv
                wr.writerow(data)
                data = ['', '',]
            data = ['',]
        data = []

                # print(text.get_attribute('textContent'))
                #print(len(text))
        time.sleep(5)
