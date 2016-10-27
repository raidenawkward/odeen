# coding = utf-8
# decorate raw file which was fetched by fetchpage.py

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

def convertToJson(l):
    pass

def decorateFromFolder():
    pass

if __name__ == '__main__':
    f = open('0.raw', 'rb')
    bcontent = f.read()
    l = decorate(bcontent)
    print(l)
