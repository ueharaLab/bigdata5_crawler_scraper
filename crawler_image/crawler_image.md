# 画像のクローリング

## 1. 画像を1枚取得して保存する
サンプルプログラム[tabelog_crawler_image.py](../tabelog_crawler_image.py)を動かしてみる。

``` python
img_url = "ページソースを見て適当に画像リンクURLを貼り付ける"
# 画像URLで普通にhttp リクエスト
res = urllib.request.urlopen(img_url)
image=res.read() # html 取得		

# 取得した画像をファイルとして書き出す
img_file = open('image.jpg', 'wb')
img_file.write(image)
img_file.close()

# 画像を画面に表示
img_data =io.BytesIO(image)
img = Image.open(img_data)
img.show()
```

## 2. webページ中の画像を連続的に収集するプログラムを書いてみる（演習）

1. 画像リンクのタグ <a class="js-imagebox-trigger" data-id="189628664" href=" へのxpathを書く
2. 画像リンク(href属性中のURL)を取り出す
3. リンクを繰り返し取り出して次々に画像を取得してファイルに保存（上記サンプルプログラムを応用する）

注意：ファイル保存する際に物理ファイル名を変える必要がある

以上の流れが実現できるように、[tabelog_scraper2image](../tabelog_scraper2image.py)を完成させてください。

``` python

f = open('tabelog_kuchikomi.html', 'r', encoding='UTF-8')
bodyHtml = f.read()
root = lxml.html.fromstring(bodyHtml)

img_paths = root.xpath("")

for i,img_path in enumerate(img_paths):

    print('image count {}'.format(i))
    # href属性から画像へのURLを取り出す
    # 画像URLでhttpリクエストして画像を取得
    
    # 以下、物理ファイル名を代えながら画像を imagesフォルダーの中に書き出すように完成させる
    img_file = open('', 'wb')
    img_file.write(image)
    img_file.close()
```





