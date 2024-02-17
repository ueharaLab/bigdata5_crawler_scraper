# クローラーで収集したデータをcsvに書き出す

[tabelog_scraper2csv.py](/tabelog_scraper2csv.py)を実行すると、タイトルと本文がcsvに書き出される。  
（サーバーへの負荷を考慮してダウンロード済のhtmlファイルからスクレイピングしている。また、タイトルの省略によって、タイトル～本文のペアがずれる問題への対処は簡単化するために考慮していない）

以下のコメントに注目！
``` python
f = open('tabelog_kuchikomi.html', 'r', encoding='UTF-8')
bodyHtml = f.read()
root = lxml.html.fromstring(bodyHtml)

body_path = root.xpath("//div[@class='rvw-item__rvw-comment rvw-item__rvw-comment--custom']")
title_path = root.xpath("//a[@class='rvw-item__title-target']")

# dataframeを作成してからcsvに書き出していることに注億
tabelog_info=[]
for title,body in zip(title_path,body_path):
    print(title.text_content())
    print(body.text_content())
    # 書き出したいデータを2次元配列にする
    tabelog_info.append([title.text_content(),body.text_content()])

# 2次元配列からDataframeを作る
tabelog_df = pd.DataFrame(tabelog_info, columns = ['タイトル','本文'])
# Dataframeをcsvに書き出す
with codecs.open("tabelog_kuchikomi.csv", "w", "ms932", "ignore") as f: 
   
    tabelog_df.to_csv(f, index=False, encoding="ms932", mode='w', header=True)
```