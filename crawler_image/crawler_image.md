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

以上の流れが実現できるように、[tabelog_scraper_image]()を完成させてください。





