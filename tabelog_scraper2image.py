from urllib.request import urlopen
import urllib.request
import urllib.parse
import urllib
import lxml.html
import pandas as pd
import codecs




f = open('tabelog_kuchikomi.html', 'r', encoding='UTF-8')
bodyHtml = f.read()
root = lxml.html.fromstring(bodyHtml)

img_paths = root.xpath("")

for i,img_path in enumerate(img_paths):

    print('image count {}'.format(i))
    # href属性から画像へのURLを取り出す
    # 画像URLでhttpリクエストして画像を取得
    
    # 以下、物理ファイル名を代えながら画像を imagesフォルダーの中に書き出すように完成させる
    # 
    img_file = open('', 'wb')
    img_file.write(image)
    img_file.close()

    