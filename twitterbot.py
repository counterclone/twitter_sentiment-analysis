from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import time, os
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def remove_non_ascii(input_string):
    return ''.join(char if ord(char) < 128 else '' for char in input_string)

def remove_extra_spaces(text):
    cleaned_text = re.sub(r'\s+', ' ', text)
    cleaned_text = cleaned_text.strip()
    return cleaned_text

def keep_alphabets_and_spaces(input_string):
    cleaned_string = re.sub(r'[^a-zA-Z\s]', '', input_string)
    return cleaned_string

def remove_duplicates(input_list):
    seen = set()
    result = []
    for item in input_list:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result



cred =pd.read_csv("cred.csv")
k=1

def listToString(s):
    str1 = " "
    return (str1.join(map(str, s)))

class Twitterbot:
    
    def __init__(self):
       
        print("login")
        self.k=0
        edge_options = Options()  # Use EdgeOptions instead of ChromeOptions
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59'
        
        edge_options.add_argument(f'user-agent={user_agent}')
        #edge_options.add_argument("--headless=new")
        
        self.bot = webdriver.Edge( options=edge_options)  # Specify the path to msedgedriver
        
        

        

    def login(self,k):
        bot=self.bot
        time.sleep(2)
        self.email =cred['username'][k]
        self.password= cred['password'][k]
        print("login started")
        #bot.get('https://twitter.com/i/flow/login?input_flow_data=%7B"requested_variant"%3A"eyJsYW5nIjoiZW4ifQ%3D%3D"%7D')
        #bot.get('https://twitter.com/i/flow/login')
        bot.get('https://twitter.com/i/flow/login')
        time.sleep(3)
        # page_source = bot.page_source
        # soup = BeautifulSoup(page_source,'html.parser')
        # signin=bot.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a/div')
        # signin.click()
        # print("signin clicked")
        # time.sleep(4)
        page_source = bot.page_source
        soup = BeautifulSoup(page_source,'html.parser')
        email=bot.find_element(By.NAME,'text')
        email.send_keys(self.email)
        time.sleep(2)
       
        #button=bot.find_element(By.CSS_SELECTOR,"div[class='css-1rynq56 r-bcqeeo r-qvutc0 r-37j5jr r-q4m81j r-a023e6 r-rjixqe r-b88u0q r-1awozwy r-6koalj r-18u37iz r-16y2uox r-1777fci']")
        #button=bot.find_element(By.CLASS_NAME,'css-1rynq56 r-bcqeeo r-qvutc0 r-37j5jr r-q4m81j r-a023e6 r-rjixqe r-b88u0q r-1awozwy r-6koalj r-18u37iz r-16y2uox r-1777fci')
        #time.sleep(3)
        #bot.execute_script("arguments[0].click();", button)
        #button.submit()
        print("next clicked")
        time.sleep(2)
        page_source=bot.page_source
        soup = BeautifulSoup(page_source,'html.parser')
        #time.sleep(2)
        password = bot.find_element(By.NAME,'password')
        #password = bot.find_element(By.CSS_SELECTOR,'#react-root > div > div > div > main > div > div > div > div.css-175oi2r.r-1ny4l3l.r-6koalj.r-16y2uox > div.css-175oi2r.r-16y2uox.r-1jgb5lz.r-13qz1uu.r-1ye8kvj > div.css-175oi2r.r-1fq43b1.r-16y2uox.r-1wbh5a2.r-1dqxon3 > div > div > div > div.css-175oi2r.r-mk0yit.r-13qz1uu > div > label > div > div.css-175oi2r.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-1pn2ns4.r-ttdzmv')
        password.send_keys(self.password)
        time.sleep(3)
        
        # button1=bot.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div/div/div')
        # bot.execute_script("arguments[0].click();", button1)
        
        print("login finished")

    def get_tweets(self, hashtag_list,l): 
        tweets=[]
        pure_tweets=[]
        username=[]
        bot=self.bot
        
        num=0
        i=0
        while i<len(hashtag_list):
            t=l
            p=0
            hashtag=hashtag_list[i]
            print(hashtag)

                    #https://twitter.com/search?q=hello&src=typed_query
            bot.get('https://twitter.com/search?q=' + hashtag + '&src=typed_query&f=live')
            time.sleep(5)
            if(hashtag==""):
                i+=1
                continue

            while(t>0):
                page_source = bot.page_source
                soup = BeautifulSoup(page_source,'lxml')
                t-=1
                # q= soup.find('div',{'class':'css-1dbjc4n'})
                q= soup.find('div',{'class':'css-175oi2r'})
                a=q.find_all('div',{'data-testid':'cellInnerDiv'})
                k=1 
                for b in a:
                    # u=b.find('div',{'class':'css-1dbjc4n r-zl2h9q'})
                    u=b.find('div',{'class':'css-175oi2r r-zl2h9q'})
                    if(u==None):
                        continue
                    
                    # c=u.find('span',{'class':'css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'})
                    c=u.find('span',{'class':'css-1qaijid r-dnmrzs r-1udh08x r-3s2u2q r-bcqeeo r-qvutc0 r-poiln3'})
                    #user=remove_non_ascii(c.text)
                    user=c.text.encode('utf-8')


                    w=b.find_all('div',{'dir':'auto'})
                    for z in w:
                        # m=z.find('span',{'class':'css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'})
                        m=z.find('span',{'class':'css-1qaijid r-bcqeeo r-qvutc0 r-poiln3'})
                        if m is not None:                
                            k+=1
                            pt=m.text.encode('utf-8')
                            z=keep_alphabets_and_spaces(remove_extra_spaces(remove_non_ascii(m.text)))
                            if z is not None or z !=" " or z != "  " or z !="   ":
                                tweets.append(z)
                                username.append(user)
                                pure_tweets.append(pt)
                                p+=1
                                
                                print(f"{user} : {z}")
                                #user=user.decode('utf-8')
                bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
                time.sleep(2)
            print(f"number of tweets fetched by {hashtag} = {p}")
            if(p==0):
                self.k+=1
                cv=self.k
                i-=1
                self.login(cv)
                continue
            i+=1
            num+=p
            time.sleep(1)
        
        print(f"total tweets fetched {num} ")
        return tweets,username,pure_tweets


       

     

        



            
