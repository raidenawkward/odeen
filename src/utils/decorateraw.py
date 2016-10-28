# coding = utf-8
# decorate raw file which was fetched by fetchpage.py

import json
import os


ANCHOR_NAME_START_B = b'<h1>'
ANCHOR_NAME_END_B = b'</h1>'
ANCHOR_EXPLAIN_START_1_B = b'<div class="bookvson2">'
ANCHOR_EXPLAIN_START_2_B = b'</p>'
ANCHOR_EXPLAIN_END_B = b'</div>'
ANCHOR_TRANSLATE_STATR_B = b'<p style="margin-top:10px; font-size:14px;">'
ANCHOR_TRANSLATE_END_B = b'<a style='
ANCHOR_COMMENT_STATR_B = b'<p style="margin-top:10px; font-size:14px;">'
ANCHOR_COMMENT_END_B = b'<a style='

def decorate(bcontent):
    if bcontent is None:
        return None

    try:
        # name
        indexNameStart = bcontent.index(ANCHOR_NAME_START_B) + len(ANCHOR_NAME_START_B)
        indexNameEnd = bcontent.index(ANCHOR_NAME_END_B, indexNameStart + 1)
        byteName = bytearray(indexNameEnd - indexNameStart)

        for i in range(indexNameStart, indexNameEnd):
            byteName[i - indexNameStart] = bcontent[i]

        # explain
        indexExplainStart = bcontent.index(ANCHOR_EXPLAIN_START_1_B, indexNameEnd + 1) + len(ANCHOR_EXPLAIN_START_1_B)
        indexExplainStart = bcontent.index(ANCHOR_EXPLAIN_START_2_B, indexExplainStart + 1) + len(ANCHOR_EXPLAIN_START_2_B)
        indexExplainEnd = bcontent.index(ANCHOR_EXPLAIN_END_B, indexExplainStart + 1)
        byteExplain = bytearray(indexExplainEnd - indexExplainStart)

        for i in range(indexExplainStart, indexExplainEnd):
            byteExplain[i - indexExplainStart] = bcontent[i]

        byteExplain = byteExplain.replace(b'<br />', b'\n')

        # translate
        translateStart = bcontent.index(ANCHOR_TRANSLATE_STATR_B, indexExplainEnd + 1) + len(ANCHOR_TRANSLATE_STATR_B)
        translateEnd = bcontent.index(ANCHOR_TRANSLATE_END_B, translateStart + 1)
        byteTranslate = bytearray(translateEnd - translateStart)

        for i in range(translateStart, translateEnd):
            byteTranslate[i - translateStart] = bcontent[i]

        # comment
        commentStart = bcontent.index(ANCHOR_COMMENT_STATR_B, translateEnd + 1) + len(ANCHOR_COMMENT_STATR_B)
        commentEnd = bcontent.index(ANCHOR_COMMENT_END_B, commentStart + 1)
        byteComment = bytearray(commentEnd - commentStart)

        for i in range(commentStart, commentEnd):
            byteComment[i - commentStart] = bcontent[i]
    except:
        return None

    return [byteName.decode().strip(), byteExplain.decode().strip(), byteTranslate.decode().strip(), byteComment.decode().strip()]

def converContentListtToDict(contentList, index=0):
    if contentList is None:
        return None

    d = {}
    d["index"] = index
    d["name"] = contentList[0]
    d["explain"] = contentList[1]
    d["explaintranslate"] = {}
    d["explaintranslate"]["CN"] = contentList[2]
    d["comment"] = contentList[3]

    #jsonStr = json.dumps(d, ensure_ascii=False)

    return d

def loadJsonFromFolder(folder, ext='.raw'):
    l = []

    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(ext):
                filename = os.path.basename(file)
                nameComp = filename.split('.')
                name = nameComp[0]
                index = int(name)

                path = os.path.join(root, file)
                print('reading content from file ' + path)

                file = open(path, 'rb')
                bcontent = file.read()
                file.close()

                if bcontent is None:
                    continue

                contentList = decorate(bcontent)
                if contentList is None:
                    continue

                itemDict = converContentListtToDict(contentList, index)
                l.append(itemDict)

    l = sorted(l, key = lambda item: item['index'])
    jsonRoot = {}
    jsonRoot['symbolsdict'] = l

    jsonStr = json.dumps(jsonRoot, ensure_ascii=False)
    #jsonStr = jsonStr.replace('\\n', '\n')
    #print(jsonStr)
    return jsonStr


if __name__ == '__main__':
    jsonStr = loadJsonFromFolder('.')

    file = open('symboldict', 'wb')
    file.write(jsonStr.encode())
    file.close()
    print('write to file succeed')

    file = open('symboldict', 'rb')
    content = file.read()

    jsonDict = json.loads(content.decode(), encoding='utf-8')
    file.close()
    print(jsonDict)

