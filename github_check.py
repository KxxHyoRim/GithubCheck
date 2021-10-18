from multiprocessing import Pool
import time
from datetime import date
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

git_home = 'https://github.com/'
login = 'https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2FKxxHyoRim'
git_page = 'https://github.com/' # 뒤에 아이디 붙여서 사용
git_id = ['KxxHyoRim', 'yeseul106', 'HoyeonYu', 'LeeHyewon225']

def isUserExist(id):
    # id로 검색
    driver.get('https://github.com/search?q=' + id + '&type=users')
    time.sleep(1)
    try :
        id_href = driver.find_element_by_css_selector('#user_search_results > div > div > div.flex-auto > div:nth-child(1) > div.f4.text-normal > a > em')
        print(id_href.text) # id print
        return True
    except:
        return False




def getOnePersonInfo(id):

    '''repository 접근'''
    driver.get(git_page + id)
    name_xpath = '//*[@id="js-pjax-container"]/div[2]/div/div[1]/div/div[2]/div[1]/div[2]/h1/span[1]'
    id_xpath = '//*[@id="js-pjax-container"]/div[2]/div/div[1]/div/div[2]/div[1]/div[2]/h1/span[2]'

    print("*******************")

    ''' 이름가져오기 : 설정 안해둔 사람도 있으므로 우선 주석처리 '''
    # try :
    #     print( driver.find_element_by_xpath(name_xpath).text)
    # except: # 이름 지정 안되어 있음
    #     pass


    ''' 아이디 가져오기 '''
    try :
        print('ID : ',driver.find_element_by_xpath(id_xpath).text)
    except: # 이름 지정 안되어 있음
        pass


    ''' Commit 수 가져오기 : class 속성 사용 '''
    # Commit : css, xpath 사람마다 다름 -> 불가능
    today = str(date.today())                                               # 오늘 날짜
    rect = driver.find_elements_by_class_name('ContributionCalendar-day')   # 잔디 정보 전체 

    # 오늘의 Data 검사하기
    for day in rect : 
        if (day.get_attribute('data-date') == today):
            print('Today Commit : ', end="")
            print(day.get_attribute('data-count'))



if __name__ == "__main__":

    options = webdriver.ChromeOptions()
    options.add_argument('--disable-extensions')
    # options.add_argument('--headless')        # background
    # options.add_argument('--disable-gpu')     # background
    # options.add_argument("--start-maximized") # 화면 최대화
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver', chrome_options=options)

    # for person in git_id:
    #     if (isUserExist(person)):
    #         getOnePersonInfo(person)
    #     else:
    #         print('user not exist ')

    for person in git_id:
        getOnePersonInfo(person)
