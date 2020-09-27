###################################################################################################
# 사용자의 최근 5개의 멜론 플레이리스트 중 기존 항목에 없는 플레이리스트 목록 및 정보를 수집하는 프로그램

# 작성자 : 강민성
# 작성일 : 2020.09.19
# 최종 수정일 : 2020.09.19
###################################################################################################
##################    Import    ############################
import requests
from bs4 import BeautifulSoup as bs
import re
import csv
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

##################    Global    ############################



##################    Var    ############################
chromedriver = '..\exe\chromedriver.exe'

##################    Func    ############################
def songcrawling(plcode, plname):
    fout = open('..\csv\melon[3]_csv\playlist' + str(plname) +'.csv', 'w', encoding='utf8')    
    driver = webdriver.Chrome(chromedriver)
    driver.get('https://www.melon.com/mymusic/playlist/mymusicplaylistview_inform.htm?plylstSeq='+str(plcode))
    html = driver.page_source
    soup = bs(html, 'html.parser')
    songnum1 = str(soup.select('#songList > div > h3 > span'))
    songnumf = int(songnum1[songnum1.find('">')+3:songnum1.find('(<')-8])
    songnum = songnumf
    maxpage = songnum//50
    nowpage = 1
    pagebar = 1
    while nowpage>maxpage:
        if songnumf > 50:
            songnum = 50
            songnumf -= 50
        for i in range (songnum):
        
            titlef = str(soup.select('#frm > div > table > tbody > tr:nth-child('+str(i+1)+') > td:nth-child(3) > div > div > a.fc_gray'))
            title = titlef[titlef.find('">')+2:titlef.find('<//a')-4]
        
        
            singerf = str(soup.select('#frm > div > table > tbody > tr:nth-child('+str(i+1)+') > td:nth-child(4) > div > div > a.fc_mgray'))
            singer = singerf[singerf.find('">')+2:singerf.find('<//a')-4]
        
            print(singer)
            print('*')
            fout.write(singer)
            fout.write('\n')
        
            
        try:
            search_bar = driver.find_element_by_tag_name('#pageObjNavgation > div > span > a:nth-child('+str(nowpage)+')')
            webdriver.ActionChains(driver).click(search_bar).perform()
            time.sleep(2)
            nowpage += 1
            pagebar += 1
        except NoSuchElementException:
            search_bar = driver.find_element_by_tag_name('#pageObjNavgation > div > a.btn_next')
            pagebar = 1
            webdriver.ActionChains(driver).click(search_bar).perform()
            time.sleep(1)
            pagebar += 1
            nowpage += 1
        
    fout.close()
    driver.close()

##################    Main    ############################

f = open('..\ws\workspace.csv', 'r', encoding='utf8')
rdr = csv.reader(f)

headers = { "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}

for line in rdr:
    songcrawling(line[0],line[1])

f.close()
