import time
import pymysql as p
from datetime import datetime
from selenium import webdriver
from bs4 import BeautifulSoup as bs

conn = p.connect(host="sejongwinterproject.ckkpavqulpya.ap-northeast-2.rds.amazonaws.com", port=3306, user="admin",
                 password="no0431**", db="demo",
                 charset="utf8")  # DB 연결 host, port, user, password, db, charset 지정해줘야됨
cursor = conn.cursor()  # 커서 객체 생성
tmp_cal = datetime.today().strftime("%Y%m%d")  # 날짜 받아 오기
cal = int(tmp_cal)
print(cal)

driver = webdriver.Chrome()

print('CPU')
# CPU
driver.get('https://prod.danawa.com/info/?pcode=28798964&cate=112747')
html = driver.page_source
soup = bs(html, 'html.parser')
price = soup.select_one("#blog_content > div.summary_info >\
 div.detail_summary > div.summary_left > div.lowest_area >\
  div.lowest_top > div.row.lowest_price > span.lwst_prc > a > em")
realPrice1 = int(price.get_text().replace(',', ''))
print(realPrice1)

driver.get('https://prod.danawa.com/info/?pcode=28799435&cate=112747')
html = driver.page_source
soup = bs(html, 'html.parser')
price = soup.select_one("#blog_content > div.summary_info >\
 div.detail_summary > div.summary_left > div.lowest_area >\
  div.lowest_top > div.row.lowest_price > span.lwst_prc > a > em")
realPrice2 = int(price.get_text().replace(',', ''))
print(realPrice2)

driver.get('https://prod.danawa.com/info/?pcode=28799654&cate=112747')
html = driver.page_source
soup = bs(html, 'html.parser')
price = soup.select_one("#blog_content > div.summary_info >\
 div.detail_summary > div.summary_left > div.lowest_area >\
  div.lowest_top > div.row.lowest_price > span.lwst_prc > a > em")
realPrice3 = int(price.get_text().replace(',', ''))
print(realPrice3)

query = "INSERT INTO CPU (CALENDAR, CPU1, CPU2, CPU3) VALUES (%s, %s, %s, %s)"
values = (cal, realPrice1, realPrice2, realPrice3)
cursor.execute(query, values)
conn.commit()

print('\n')
print('RAM')
# RAM
driver.get('https://prod.danawa.com/info/?pcode=28241219&cate=112752')
html = driver.page_source
soup = bs(html, 'html.parser')
price = soup.select_one("#blog_content > div.summary_info >\
 div.detail_summary > div.summary_left > div.lowest_area >\
  div.lowest_top > div.row.lowest_price > span.lwst_prc > a > em")
realPrice1 = int(price.get_text().replace(',', ''))
print(realPrice1)

driver.get('https://prod.danawa.com/info/?pcode=9593742&cate=112752')
html = driver.page_source
soup = bs(html, 'html.parser')
price = soup.select_one("#blog_content > div.summary_info >\
 div.detail_summary > div.summary_left > div.lowest_area >\
  div.lowest_top > div.row.lowest_price > span.lwst_prc > a > em")
realPrice2 = int(price.get_text().replace(',', ''))
print(realPrice2)

driver.get('https://prod.danawa.com/info/?pcode=4848365&cate=112752')
html = driver.page_source
soup = bs(html, 'html.parser')
price = soup.select_one("#blog_content > div.summary_info >\
 div.detail_summary > div.summary_left > div.lowest_area >\
  div.lowest_top > div.row.lowest_price > span.lwst_prc > a > em")
realPrice3 = int(price.get_text().replace(',', ''))
print(realPrice3)

query = "INSERT INTO RAM (CALENDAR, RAM1, RAM2, RAM3) VALUES (%s, %s, %s, %s)"
values = (cal, realPrice1, realPrice2, realPrice3)
cursor.execute(query, values)
conn.commit()

print('\n')
print('그래픽 카드')
# 그래픽 카드
driver.get('https://prod.danawa.com/info/?pcode=18668606&cate=112753')
html = driver.page_source
soup = bs(html, 'html.parser')
price = soup.select_one("#blog_content > div.summary_info >\
 div.detail_summary > div.summary_left > div.lowest_area >\
  div.lowest_top > div.row.lowest_price > span.lwst_prc > a > em")
realPrice1 = int(price.get_text().replace(',', ''))
print(realPrice1)

driver.get('https://prod.danawa.com/info/?pcode=19756001&cate=112753')
html = driver.page_source
soup = bs(html, 'html.parser')
price = soup.select_one("#blog_content > div.summary_info >\
 div.detail_summary > div.summary_left > div.lowest_area >\
  div.lowest_top > div.row.lowest_price > span.lwst_prc > a > em")
realPrice2 = int(price.get_text().replace(',', ''))
print(realPrice2)

driver.get('https://prod.danawa.com/info/?pcode=18108812&cate=112753')
html = driver.page_source
soup = bs(html, 'html.parser')
price = soup.select_one("#blog_content > div.summary_info >\
 div.detail_summary > div.summary_left > div.lowest_area >\
  div.lowest_top > div.row.lowest_price > span.lwst_prc > a > em")
realPrice3 = int(price.get_text().replace(',', ''))
print(realPrice3)

query = "INSERT INTO GC (CALENDAR, GC1, GC2, GC3) VALUES (%s, %s, %s, %s)"
values = (cal, realPrice1, realPrice2, realPrice3)
cursor.execute(query, values)
conn.commit()

print('\n')
print('SSD')
# SSD
driver.get('https://prod.danawa.com/info/?pcode=17454494&cate=112760')
html = driver.page_source
soup = bs(html, 'html.parser')
price = soup.select_one("#blog_content > div.summary_info >\
 div.detail_summary > div.summary_left > div.lowest_area >\
  div.lowest_top > div.row.lowest_price > span.lwst_prc > a > em")
realPrice1 = int(price.get_text().replace(',', ''))
print(realPrice1)

driver.get('https://prod.danawa.com/info/?pcode=14905265&cate=112760')
html = driver.page_source
soup = bs(html, 'html.parser')
price = soup.select_one("#blog_content > div.summary_info >\
 div.detail_summary > div.summary_left > div.lowest_area >\
  div.lowest_top > div.row.lowest_price > span.lwst_prc > a > em")
realPrice2 = int(price.get_text().replace(',', ''))
print(realPrice2)

driver.get('https://prod.danawa.com/info/?pcode=29666111&cate=112760')
html = driver.page_source
soup = bs(html, 'html.parser')
price = soup.select_one("#blog_content > div.summary_info >\
 div.detail_summary > div.summary_left > div.lowest_area >\
  div.lowest_top > div.row.lowest_price > span.lwst_prc > a > em")
realPrice3 = int(price.get_text().replace(',', ''))
print(realPrice3)

query = "INSERT INTO SSD (CALENDAR, SSD1, SSD2, SSD3) VALUES (%s, %s, %s, %s)"
values = (cal, realPrice1, realPrice2, realPrice3)
cursor.execute(query, values)
conn.commit()

print('\n')
print('HDD')
# HDD
driver.get('https://prod.danawa.com/info/?pcode=6545078&cate=112763')
html = driver.page_source
soup = bs(html, 'html.parser')
price = soup.select_one("#blog_content > div.summary_info >\
 div.detail_summary > div.summary_left > div.lowest_area >\
  div.lowest_top > div.row.lowest_price > span.lwst_prc > a > em")
realPrice1 = int(price.get_text().replace(',', ''))
print(realPrice1)

driver.get('https://prod.danawa.com/info/?pcode=5764992&cate=112763')
html = driver.page_source
soup = bs(html, 'html.parser')
price = soup.select_one("#blog_content > div.summary_info >\
 div.detail_summary > div.summary_left > div.lowest_area >\
  div.lowest_top > div.row.lowest_price > span.lwst_prc > a > em")
realPrice2 = int(price.get_text().replace(',', ''))
print(realPrice2)

driver.get('https://prod.danawa.com/info/?pcode=9721383&cate=112763')
html = driver.page_source
soup = bs(html, 'html.parser')
price = soup.select_one("#blog_content > div.summary_info >\
 div.detail_summary > div.summary_left > div.lowest_area >\
  div.lowest_top > div.row.lowest_price > span.lwst_prc > a > em")
realPrice3 = int(price.get_text().replace(',', ''))
print(realPrice3)

query = "INSERT INTO HDD (CALENDAR, HDD1, HDD2, HDD3) VALUES (%s, %s, %s, %s)"
values = (cal, realPrice1, realPrice2, realPrice3)
cursor.execute(query, values)
conn.commit()

time.sleep(3)
driver.close()
conn.close()
