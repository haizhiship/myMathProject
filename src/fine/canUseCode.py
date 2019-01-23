'''
根据用户鼠标选择的范围，获取所选的文字
text：文本全文
font：字体类Surface
textPos：文本的起始位置，元祖类型(100,100)
beginPos：鼠标选择的起始位置
endPos：鼠标选择的结束位置
返回值：所选择的文本，所选择文本的起始位置和结束位置
'''
def getTextListByArea(text, font, textPos, beginPos, endPos):

    wordWidths = []
    for word in text:
        wordWidths.append(font.size(word)[0])
    wordHeight = font.size(word)[1]

    beginIndex = -1
    endIndex = -1
    beginSelPos = 0
    endSelPos = 0
    if (textPos[1] < beginPos[1] and textPos[1] + wordHeight > beginPos[1]) \
        and (textPos[1] < endPos[1] and textPos[1] + wordHeight > endPos[1]):
       totalLength = 0
       for i in range(len(wordWidths)):
           totalLength += wordWidths[i]
           if totalLength + textPos[0] > beginPos[0] and beginIndex == -1:
               beginIndex = i
               beginSelPos = totalLength - wordWidths[i]
           if totalLength + textPos[0] > endPos[0] and endIndex == -1:
               endIndex = i + 1
               endSelPos = totalLength + textPos[0]

    if endIndex >= len(text):
        endIndex = len(text)

    if beginIndex > -1 and endIndex > -1:
        return text[beginIndex:endIndex], beginSelPos, endSelPos
    return '',0,0