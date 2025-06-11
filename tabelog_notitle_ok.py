from urllib.request import urlopen
import urllib.request
import urllib.parse
import urllib
import lxml.html
import pandas as pd
import codecs




f = open('tabelog_review.html', 'r', encoding='UTF-8')
bodyHtml = f.read()
root = lxml.html.fromstring(bodyHtml)


titlebody_path = root.xpath("//div[@class='rvw-item__contents']")

tabelog_info=[]
for titlebody in titlebody_path:
    #print(titlebody.text_content().replace(' ','').replace('\n',''))
    
    
    title_path = titlebody.xpath(".//p[@class='rvw-item__title rvw-item__title--rvwlst']")
    body_path = titlebody.xpath(".//div[@class='rvw-item__rvw-comment rvw-item__rvw-comment--custom']")
    title =''
    body = ''
    if len(title_path) !=0 :
        title = title_path[0].text_content().replace(' ','').replace('\n','')
        print(title)  
    if len(body_path) !=0:
        body = body_path[0].text_content().replace(' ','').replace('\n','')      
        print(body)
    print('\n')
    tabelog_info.append([title,body])

tabelog_df = pd.DataFrame(tabelog_info, columns = ['タイトル','本文'])
with codecs.open("tabelog_review.csv", "w", "ms932", "ignore") as f: 
    #header=Trueで、見出しを書き出す
    tabelog_df.to_csv(f, index=False, encoding="ms932", mode='w', header=True)
