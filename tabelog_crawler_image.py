from urllib.request import urlopen
import urllib.request
import urllib.parse
import urllib
from PIL import Image
import io
#img_url='https://tabelog.com/restaurant/images/Rvw/153468/640x640_rect_153468428.jpg'


img_url = "ページソースを見て適当に画像リンクURLを貼り付ける"
res = urllib.request.urlopen(img_url)
image=res.read() # html 取得		

img_file = open('image.jpg', 'wb')
img_file.write(image)
img_file.close()



img_data =io.BytesIO(image)
img = Image.open(img_data)
img.show()

