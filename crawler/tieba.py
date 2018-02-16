import re
import os
import urllib


def download_images(url, start_page, end_page):
    os.chdir(os.path.join(os.getcwd(), 'tieba_images'))
    temp = 1
    for x in range(end_page - start_page + 1):
        html_content = urllib.urlopen(url + '?pn=' + str(end_page + x - 1)).read()
        r = re.compile('<img class="BDE_Image" pic_type="1" width="450" height="450" src="(.*?)" ')
        image_list = r.findall(html_content.decode('utf-8'))
        for i in range(len(image_list)):
            image_name = str(temp) + '.jpg'
            urllib.urlretrieve(image_list[i], image_name)
            print("OK!" + image_list[i])
            temp += 1


if __name__ == '__main__':
    download_images("https://tieba.baidu.com/p/4341640851", 1, 3)
