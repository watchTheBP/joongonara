from lxml import html
from time import sleep
import requests
from datetime import datetime
import json

def main():
    joongonara_index = dict()
    joongonara = dict()
    cookie = {'Cookie':"ncvid=#vid#_210.57.236.92SzQw; WMONID=j2Y5SRWoyrC; NNB=WSMDQAO7Z73FG; nid_inf=2045810834; NID_AUT=8mmvoHcg+T1i063ormAnXPkE/8ZI+Vl1a4hQEgk6Akf3LELrYTyDQOw5XlHQV7WhGhjSBW1T6Y3+RR4IVzfUzGD8PCJyJePTo4nALeqURhYQSCNHnKTqiQQMkuQOs8Pv; NID_SES=AAABQ8yPygIgEO/Ihk9KOruk8asXNS28tcn+ictUEY4x6uHnI5Hz/yzHrM8pkNWh732JjaPAiCieMFO8kMU+QhaTAX4hLBHsP5KW7ReqvbFGSsYmP68G8vrlrOi7V39eI6UlDNY9npdjg4VQYSX6x+QunA/hVzMBSzxlsj4rHxb7I1r7FTsN5zJWwNhBqukn99lIcwSH4IAovsPF4HIG6aeplS4luC949udkN3zOftqknBOuunexz8FbyrrK2DGZ30w17mSR1rGGmfDRYcP1K6ZmhhNMah4CNFnU4U7bg0zW162GtNYpIafVaPLSJlX0csiLVFN9+v2MjhSpS0PewVwcOXt1fTP+qZmja+8DtpQJKwTtwRvamHbjFBo0SCgKxp4uFhhTIvTT71R/Ht7Kxyivx81sjMf6fA1yv7EC2sQG8NuuGnuD0FVzp8aU4cDHN8xR9w==; npic=DkmujVzw51p+goyLrc97euE9wHLh9fenNaf7Tn1byAN+pTaJokfC69TpJE/LwFyJCA==; ncu=89bb4b7e623b42fed6317e415a9ad0168f981988b80a; rmvc=10050146; ncvc2=1e7e86a2f6c0c27359a7ddeeca304b378fca3fa6fd9d43fe1fdae73488aa4c8752ae68b1744fddfe801a49e157d572ba384b7f63ce8b89a3904bf628f1dc66a3d2c4ccac82a88dd7c5c5c6c2c1c3d8dfc7d5cad5d3d5d5dbecebe89894b398aeb3b6bea3afbdaca3a3a5e9f6f0f1f78c8f8b8f98849a8581879b959e999e15; personaconmain|bernardjin=EAE11B32508CF3CEC41B74A48AE63E092C27FF2A39B7B9A218767A543203FB65; personacon|bernardjin=2ADD4716060F468BDB07BB69C1DC016B3FC4000403616BCC07C24AC6543D6F22; JSESSIONID=E13F1DCE6D8D4D3BD0812F2471F1CD6C; BMR="}
    id = 1
    for i in range(225490014, 225490042):
        url = "http://m.cafe.naver.com/ArticleRead.nhn?clubid=10050146&articleid={0}&page=1&boardtype=L".format(i)
        page = requests.get(url, cookies=cookie)
        tree = html.fromstring(page.text)

        if tree.xpath( ('//*[@id="ct"]/p/text()').encode('utf-8') ) != [u'\uac8c\uc2dc\ubb3c\uc774 \uc874\uc7ac\ud558\uc9c0 \uc54a\uac70\ub098 \uc0ad\uc81c\ub418\uc5c8\uc2b5\ub2c8\ub2e4.']:

            if tree.xpath('//*[@id="ct"]/p') != None:
                #title
                #article_id
                if tree.xpath('//*[@id="ct"]/div[1]/h2/text()')[0].strip() != None:
                    title = tree.xpath('//*[@id="ct"]/div[1]/h2/text()')[0].strip()
                    title = title.encode('utf-8')
                    joongonara.update({"title":title})
                    joongonara.update({"article_id":i})
                    joongonara_index.update({"index":{"_index":"joongo","_type":"text","_id":id}})

                #category
                if tree.xpath('//*[@id="ct"]/div[1]/p/span/span[1]/a/text()')[0].strip() != None:
                    category = tree.xpath('//*[@id="ct"]/div[1]/p/span/span[1]/a/text()')[0].strip()
                    if isinstance(category, unicode) == True:
                        category = category.encode('utf-8')
                        joongonara.update({"category":category})

                #views
                if tree.xpath('//*[@id="ct"]/div[1]/p/span/span[2]/text()')[1].strip().split()[1] != None:
                    views = tree.xpath('//*[@id="ct"]/div[1]/p/span/span[2]/text()')[1].strip().split()[1]
                    views = views.encode('utf-8')
                    joongonara.update({"views":views})

                #date
                if tree.xpath('//*[@id="ct"]/div[1]/p/span/span[1]/text()')[2].strip() != None:
                    date = tree.xpath('//*[@id="ct"]/div[1]/p/span/span[1]/text()')[2].strip()
                    date = date.split()[0]
                    date_time = datetime.strptime(date, '%Y.%m.%d')
                    date_time = str(date_time).split()[0]
                    joongonara.update({"datetime":date_time})

                #comments
                if tree.xpath('//*[@id="ct"]/div[1]/a/text()') != None:
                    comments = tree.xpath('//*[@id="ct"]/div[1]/a/text()')[1].strip()
                    comments = comments.encode('utf-8')
                    joongonara.update({"comments":comments})

                #body
                if tree.xpath('//*[@id="postContent"]/div/text()') != None:
                    body = tree.xpath('//*[@id="postContent"]/div/text()')

                if tree.xpath('//*[@id="phoneNumber"]/text()'):
                    phone = tree.xpath('//*[@id="phoneNumber"]/text()')[0]
                    joongonara.update({"phone":phone})

                if tree.xpath('//*[@id="seller_info"]/div/ul/li[2]/p/a/text()') != None:
                    email = tree.xpath('//*[@id="seller_info"]/div/ul/li[2]/p/a/text()')
                    if email == []:
                        email = "None"
                    else:
                        email = email[0].strip()

                    joongonara.update({"email":email})

                print json.dumps(joongonara_index)
                print json.dumps(joongonara, ensure_ascii=False)
                sleep(0.3)

if __name__ == '__main__':
    main()