############################################################################
# 플레이리스트 목록을 가져와 유튜브 플레이리스트 목록으로 만드는 프로그램입니다. 
# 작성자 : 강민성
# 작성일 : 2020.09.19
# 최종 수정일 : 2020.09.19
############################################################################
##################    Import    ############################
import requests
from bs4 import BeautifulSoup as bs
import re
import csv
from selenium import webdriver

##################    Global    ############################



##################    Var    ############################
chromedriver = '..\exe\chromedriver.exe'

##################    Func    ############################
def songcrawling(plcode, plname):
    fout = open('..\cvs\playlist' + str(plname) +'.csv', 'w', encoding='utf8')    
    driver = webdriver.Chrome(chromedriver)
    driver.get('https://www.melon.com/mymusic/playlist/mymusicplaylistview_inform.htm?plylstSeq='+str(plcode))
    html = driver.page_source
    soup = bs(html, 'html.parser')
    songnum1 = str(soup.select('#songList > div > h3 > span'))
    songnum = int(songnum1[songnum1.find('">')+3:songnum1.find('(<')-8])
    for i in range (songnum):
        titlef = str(soup.select('#frm > div > table > tbody > tr:nth-child('+str(i)+') > td:nth-child(3) > div > div > a.fc_gray'))
        title = titlef[titlef.find('">')+2:titlef.find('<//a')-4]
        singerf = str(soup.select('#frm > div > table > tbody > tr:nth-child('+str(i)+') > td:nth-child(4) > div > div > a.fc_mgray'))
        singer = singerf[singerf.find('">')+2:singerf.find('<//a')-4]
        print(title)
        print('*')
        print(singer)
        fout.write(title)
        fout.write(', ')
        fout.write(singer)
        fout.write('\n')
    fout.close()
    driver.close()

##################    Main    ############################

f = open('..\ws\workspace.csv', 'r', encoding='utf8')
rdr = csv.reader(f)

headers = { "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}

for line in rdr:
    songcrawling(line[0],line[1])

f.close()

PROXY = "117.1.16.131:8080" # IP:Port

webdriver.DesiredCapabilities.CHROME['proxy'] = {
    "httpProxy": PROXY,
    "ftpProxy": PROXY,
    "sslProxy": PROXY,
    "proxyType": "MANUAL"
}

driver = webdriver.Chrome(chromedriver)
driver.get("https://www.google.com")