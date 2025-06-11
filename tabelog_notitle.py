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

title_path = root.xpath("//p[@class='rvw-item__title rvw-item__title--rvwlst']")
body_path = root.xpath("//div[@class='rvw-item__rvw-comment rvw-item__rvw-comment--custom']")

#<div class="rvw-item__date">
tabelog_info=[]
for title,body in zip(title_path,body_path):
    print(title.text_content())
    print(body.text_content())
    tabelog_info.append([title.text_content(),body.text_content()])

tabelog_df = pd.DataFrame(tabelog_info, columns = ['タイトル','本文'])
with codecs.open("tabelog_review.csv", "w", "ms932", "ignore") as f: 
    #header=Trueで、見出しを書き出す
    tabelog_df.to_csv(f, index=False, encoding="ms932", mode='w', header=True)
