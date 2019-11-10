import xpinyin
import sys

tone = False
word = False
usage = '''
    Usage : python {} 汉字
        or  python {} 汉字 -t  // 自带音标

'''.format(sys.argv[0],sys.argv[0])


if len(sys.argv) == 2:
    word = sys.argv[1]

elif len(sys.argv) == 3:
    for i in sys.argv[1:]:
        if i.startswith('-t'):
            tone = True
        else:
            word = i
else:
    print(usage)

if word:
    
    x = xpinyin.Pinyin()
    if tone:
        pinyin = x.get_pinyin(word,tone_marks='marks')
    else:
        pinyin = x.get_pinyin(word)
    
    print(pinyin)

