# coding = 'utf-8'


import urllib
import urllib.request
import os


PAGE_PREFIX = 'http://baike.baidu.com'
ENTRANCE_PAGE = 'http://baike.baidu.com/view/163816.htm'

ENTRANCE_ANCHOR = '六十四卦，按周易古经顺序排列'
ENGTRANCE_HREF_PREFIX = '<a target=_blank href="'
ENGTRANCE_HREF_END = '"'
ENGTRANCE_NAME_START = '>'
ENGTRANCE_NAME_END = '卦<'



def fetchPage(url):
    if url is None:
        return None

    page = urllib.request.urlopen(url)
    content = page.read()
    page.close()

    return content.decode()

def fetchEntrances():
    entranceDict = {}

    entrancePageContent = fetchPage(ENTRANCE_PAGE)
    posAnchor = entrancePageContent.index(ENTRANCE_ANCHOR)
    start = posAnchor

    for i in range(0, 64):
        refAnchor = entrancePageContent.index(ENGTRANCE_HREF_PREFIX, start) + len(ENGTRANCE_HREF_PREFIX)
        endAnchor = entrancePageContent.index(ENGTRANCE_HREF_END, refAnchor)
        url = entrancePageContent[refAnchor:endAnchor]
        url = PAGE_PREFIX + url

        nameAnchor = entrancePageContent.index(ENGTRANCE_NAME_START, endAnchor + 1) + len(ENGTRANCE_NAME_START)
        endAnchor = entrancePageContent.index(ENGTRANCE_NAME_END, nameAnchor)
        name = entrancePageContent[nameAnchor:endAnchor]

        start = endAnchor + 1

        #print('name: ' + name + ', url: ' + url)
        entranceDict[name] = url

    return entranceDict



PARSE_LIST_GENERAL = [
    [
        'yi_origin', '〖卦辞原文〗', '</div>'
    ],
    [
        'yi_translate', '〖译文〗', '</div>'
    ],
    [
        'yi_explain', '〖解说〗', '</div>'
    ],
]

PARSE_LIST_ITEM = [
    [
        'ed2_symbol_origin', '〖原文〗', '</div>'
    ],
    [
        'ed2_symbol_trans', '〖译文〗', '</div>'
    ],
    [
        'ed2_symbol_comment', '〖解说〗', '</div>'
    ],
    [
        'ed2_symbol_analyse', '〖结构分析〗', '</div>'
    ],
]


def fetchEd2Items(url):
    if url is None:
        return

    print('fetching url: ' + url)

    itemDict = {}
    entrancePageContent = fetchPage(url)
    startPos = 0
    endPos = 0

    for l in PARSE_LIST_GENERAL:
        id = l[0]
        startMark = l[1]
        endMark = l[2]
        value = None

        try:
            startPos = entrancePageContent.index(startMark, startPos) + len(startMark)
            endPos = entrancePageContent.index(endMark, startPos)
            value = entrancePageContent[startPos:endPos]
        except ValueError:
            print('' + str(startMark) + ' was not found')
            break

        startPos = endPos + 1

        itemDict[id] = value

    itemList = []
    for i in range (0, 6):
        d = {}
        for l in PARSE_LIST_ITEM:
            id = l[0]
            startMark = l[1]
            endMark = l[2]
            value = None

            try:
                startPos = entrancePageContent.index(startMark, startPos) + len(startMark)
                endPos = entrancePageContent.index(endMark, startPos)
                value = entrancePageContent[startPos:endPos]
            except ValueError:
                print('' + str(i) + ': ' + str(startMark) + ' was not found')
                return itemDict

            startPos = endPos + 1

            d[id] = value
        itemList.append(d)

    itemDict['single_symbol_list'] = itemList

    return itemDict






if __name__ == '__main__':
    entranceDict = fetchEntrances()
    itemDict = fetchEd2Items(entranceDict['兑'])
    print(str(itemDict))