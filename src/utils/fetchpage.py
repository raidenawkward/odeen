#coding=utf-8
# fetch raw content from website http://so.gushiwen.org/guwen/book_6.aspx

import urllib
import urllib.request
import os

# http://so.gushiwen.org/guwen/book_6.aspx
targetlist = [
    [218,'乾'],
    [219,'坤'],
    [220,'屯'],
    [221,'蒙'],

    [222,'需'],
    [223,'讼'],
    [224,'师'],
    [225,'比'],

    [226,'小畜'],
    [227,'履'],
    [228,'泰'],
    [229,'否'],

    [230,'同人'],
    [231,'大有'],
    [232,'谦'],
    [233,'豫'],

    [234,'随'],
    [235,'蛊'],
    [236,'临'],
    [237,'观'],

    [238,'噬嗑'],
    [239,'贲'],
    [240,'剥'],
    [241,'复'],

    [242,'无妄'],
    [243,'大畜'],
    [244,'颐'],
    [245,'大过'],

    [246,'习坎'],
    [247,'离'],
    [248,'咸'],
    [249,'恒'],

    [250,'遯'],
    [251,'大壮'],
    [252,'晋'],
    [253,'明夷'],

    [254,'家人'],
    [255,'睽'],
    [256,'蹇'],
    [257,'解'],

    [258,'损'],
    [259,'益'],
    [260,'夬'],
    [261,'姤'],

    [262,'萃'],
    [263,'升'],
    [264,'困'],
    [265,'并'],

    [266,'革'],
    [267,'鼎'],
    [268,'震'],
    [269,'艮'],

    [270,'渐'],
    [271,'归妹'],
    [272,'丰'],
    [273,'旅'],

    [274,'巽'],
    [275,'兑'],
    [276,'涣'],
    [277,'节'],

    [278,'中孚'],
    [279,'小过'],
    [280,'既济'],
    [281,'未济'],
]   


def fetchPage(url):
    page = urllib.request.urlopen(url)
    page = page.read()
    return page

def generatePageUrl(index):
    url = 'http://so.gushiwen.org/guwen/bookv_' + str(index) + '.aspx'
    return url

def fetchIntoDir(dir):
    if dir is None:
        return

    try:
        os.mkdir(dir)
    except FileExistsError:
        print('dir exists, move on')

    for i in range(0, len(targetlist)):
        item = targetlist[i]
        urlIndex = item[0]
        name = item[1]
        url = generatePageUrl(urlIndex)
        print('fetching url ' + url)

        pageContent = fetchPage(url)

        dirPath = os.path.join(os.path.curdir, dir)
        filePath = os.path.join(dirPath, str(i) + '.raw')

        file = open(filePath, 'wb')
        file.write(pageContent)
        file.close()

if __name__ == '__main__':
    fetchIntoDir('raw')
