# クローラーで収集したデータをcsvに書き出す

[tabelog_scraper2csv.py](/tabelog_scraper2csv.py)を実行すると、タイトルと本文がcsvに書き出される。  
（サーバーへの負荷を考慮してダウンロード済のhtmlファイルからスクレイピングしている。また、タイトルは省略が多いので取得しない）

とりあえず実行して.csvの中身を見てください。

``` python
f = open('tabelog_kuchikomi.html', 'r', encoding='UTF-8')
bodyHtml = f.read()
root = lxml.html.fromstring(bodyHtml)

body_path = root.xpath("//div[@class='rvw-item__rvw-comment rvw-item__rvw-comment--custom']")
date_path = root.xpath("//div[@class='rvw-item__date']")
#<div class="rvw-item__date">
tabelog_info=[]
for date,body in zip(date_path,body_path):
    print(date.text_content())
    print(body.text_content())
    tabelog_info.append([date.text_content(),body.text_content()])

tabelog_df = pd.DataFrame(tabelog_info, columns = ['訪問日','本文'])
with codecs.open("tabelog_kuchikomi.csv", "w", "ms932", "ignore") as f: 
    #header=Trueで、見出しを書き出す
    tabelog_df.to_csv(f, index=False, encoding="ms932", mode='w', header=True)
```