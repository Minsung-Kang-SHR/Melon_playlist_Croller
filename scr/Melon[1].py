###############################################################
# 사용자의 멜론 플레이리스트 목록 및 정보를 수집하는 프로그램

# 작성자 : 강민성
# 작성일 : 2020.09.14
# 최종 수정일 : 2020.09.19
###############################################################
#####################     Import     ##########################
import requests
from bs4 import BeautifulSoup as bs
import re
import time
import sys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

#####################     Global     ##########################
global pagebarnum
global playlistnum
global html
global soup
global cnt

#####################     Var     ##########################
chromedriver = '..\exe\chromedriver.exe'
pagebarnum = 2
playlistnum = 1
cnt = 1

#####################     Func     ##########################

def loadmelonpage():
    global soup
    global cnt
    driver.get('https://www.melon.com/mymusic/playlist/mymusicplaylist_list.htm?memberKey=3797669')
    assert "python" not in driver.title
    print (driver.title)
    html = driver.page_source
    soup = bs(html, 'html.parser')
    getnum = str(soup.select('#playlistList > div.wrab_list_info > div > span > span'))
    playlistnum = int(getnum[getnum.find('">')+2:getnum.find('</span')])
    cnt  = int(playlistnum/20)+1
    print(cnt)

def nextpage(nowpagenum):
    global pagebarnum
    global playlistnum
    try:
        search_bar = driver.find_element_by_tag_name('#pageObjNavgation > div > span > a:nth-child('+str(pagebarnum)+')')
        print(nowpagenum, pagebarnum)
        webdriver.ActionChains(driver).click(search_bar).perform()
        time.sleep(2)
        pagebarnum += 1
        playlistnum += 1

    except NoSuchElementException:
        search_bar = driver.find_element_by_tag_name('#pageObjNavgation > div > a.btn_next')
        print(nowpagenum, pagebarnum)
        pagebarnum = 1
        webdriver.ActionChains(driver).click(search_bar).perform()
        time.sleep(1)
        pagebarnum += 1
        playlistnum += 1

def webcrolling():
    global soup
    nowpage = soup.select('#pageObjNavgation > div > span > strong')
    print(nowpage)
    html = driver.page_source
    soup = bs(html, 'html.parser')
    titles = soup.select('#pageList > table > tbody > tr > td > div > div > dl > dt > a')
    for title in titles:
        txt =str(title)
        pnum = txt[txt.find('Detail')+20:txt.find('title')-5]
        fout.write(pnum)
        fout.write(", ")
        plname = txt[txt.find('">')+2:txt.find('<\a>')-3]
        fout.write(plname)
        
        fout.write('\n')

#####################     Main     ##########################

driver = webdriver.Chrome(chromedriver)
extracts = re.compile('[^ 가-힣|a-z|A-Z|0-9|\[|\]|(|)|-|~|?|!|.|,|:|;|%]+')
fout = open('..\csv\melon[1]_csv\melon_play_list.csv', 'w', encoding='utf8')
headers = { "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}
"""
fout.write('"code"')   
fout.write(', ')
fout.write('"playlistname"')
fout.write('\n')
"""
loadmelonpage()
while playlistnum <= cnt:
    webcrolling()
    nextpage(pagebarnum)

print("End Of Program")    
fout.close() 
driver.close()
