from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox(executable_path='/etc/geckodriver')


temp = []

master_articles_list = []
master_articles_links = []

zdarticles = []
zdarticles_links = []

bleepingarticles = []
bleepingarticles_links = []





#ZDNET LINKS
def ZDNET():
    print("Checking ZDnet for articles ...")
    driver.get("https://www.zdnet.com/topic/security")

    #main element
    main = driver.find_element_by_id("main")
    article_river =  main.find_element_by_id("articleRiver")

    #latest news element
    latest = article_river.find_element_by_id("topic-river-latest")
    #picking items in latest news
    elements = latest.find_elements_by_class_name("item")

    #iteration to retrieve each article
    for articles in elements:
        new_alert = articles.find_element_by_class_name("content")
        article_linkZD = articles.find_element_by_css_selector('a').get_attribute("href")
    #    print(new_alert.text)
    #    print(article_linkZD)
    #    print('\n')
        zdarticles_links.append(article_linkZD)
    #to create the title for these articles the url is stripped
        zdarticles.append(article_linkZD[30:-1])








#BLEEPINGCOMPUTER LINKS
def BLEEPING():
    print("Checking BleepingComputer for articles ...")
    driver.get("https://www.bleepingcomputer.com/news/security/")



    bleeping = driver.find_element_by_id("bc-home-news-main-wrap")
    b_articles = bleeping.find_elements_by_class_name("bc_latest_news_text")

    for new_article in b_articles:
        bclatest_news = new_article.find_element_by_css_selector('a').get_attribute("href")
    #    print(bclatest_news)
    #    print('\n')
        bleepingarticles_links.append(bclatest_news)
    #to create the title for these articles the url is stripped
        bleepingarticles.append(bclatest_news[47:-1])

    print("Almost done....\n")
    #driver.quit()




#making the master list
def MASTERMAKE():
    temp = zdarticles + bleepingarticles
    master_articles_links = zdarticles_links + bleepingarticles_links

    #print("MASTER ARTICLE LIST \n")
    temp = list(map(lambda x: x.upper(), temp))

    for cleaning in temp:
        cleaning = cleaning.replace("-"," ")
        master_articles_list.append(cleaning)


    return master_articles_links


#making/writing to html file
def htmlwrite():
    #opening the daily news html file
    f = open('news.html','w')

    #making a basic html page
    message = """<!DOCTYPE html>
    <head><link rel="stylesheet" type="text/css" href="beauty.css"/></head>
    <body>
    <h1>Latest News Articles</h1>"""

    f.write(message)
    f.close()

    f = open('news.html','a')
    #creating hyperlinks to pipe into the html file
    for daily_news_links,urls in zip(master_articles_list,master_articles_links):
        temp_combined = "<div><p><a href=\""+urls+"\">"+daily_news_links+"</a><p></div>"
        f.write(temp_combined)





    f.write("""</body>""")

    #finishing touches to the html page
    message_end = """</html>"""
    f.write(message_end)


    f.close()

    #opening the finihed product
    driver.get("file:///home/shreykph/daily_news/news.html")









ZDNET()
BLEEPING()
master_articles_links = MASTERMAKE()
htmlwrite()
