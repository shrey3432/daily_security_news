# daily_security_news
This project uses the concept of web scraping to go to my two favorite news websites (Bleeping Computer and ZDNet) to pull security news titles that might be of interest. Rather than going to the websites manually and reading through a bunch of things the scraper makes it easier to sift through these articles based on their headings. 

The tool was built using Tech With Tim's youtube tutorial (big shout out to Tim - https://www.youtube.com/watch?v=Xjv1sY630Uc). And the actual "scraping" parameters were tweaked to meet the goals of the project. 

The code requires the python package Selenium and webdriver for the browser you want to use (in this case I used Firefox - if you want to use Firefox too, get the Gecko Driver). 

The program will re-write hyperlinks to the html file so this process takes place with minimum user interaction. 
You can change the background image if you'd like. There's a couple of generic pictures that can be set as background images using - background-image: url(".jpg");. 


