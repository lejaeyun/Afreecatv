# -*- coding: utf-8 -*-
import re
import sys

BASE_CODE, CHOSUNG, JUNGSUNG = 44032, 588, 28

# 초성 리스트. 00 ~ 18
First = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
First_dict = {'ㄱ' : ['g', 'г'], 'ㄲ' : ['k', 'к'], 'ㄴ' : ['n', 'н'], 'ㄷ' : ['d', 'д'], 'ㄸ' : ['tt', 'т'], 'ㄹ' : ['l','р'], 'ㅁ' : ['m', 'м'], \
              'ㅂ' : ['b', 'б'], 'ㅃ' : ['pp', 'п'], 'ㅅ' : ['s', 'с'], 'ㅆ' : ['ss', 'с'], 'ㅇ' : ['#', '#'], 'ㅈ' : ['z', 'ж'], 'ㅉ' : ['ch', 'ц'], \
              'ㅊ' : ['ch', 'ц'], 'ㅋ' : ['k', 'к'], 'ㅌ' : ['t', 'т'], 'ㅍ' : ['p', 'ф'], 'ㅎ' : ['h', 'х'], ' ' : [' ', ' '], '.' : ['.', '.']}

# 중성 리스트. 00 ~ 20
Second = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
Second_dict = {'ㅏ': ['aa', 'аа'], 'ㅐ': ['ae', 'аэ'], 'ㅑ': ['ya', 'а'], 'ㅒ': ['wae', 'аэ'], 'ㅓ': ['uu', 'уу'], 'ㅔ': ['e', 'э'], 'ㅕ': ['yu', 'о'],\
               'ㅖ': ['we', 'э'], 'ㅗ': ['o', 'о'], 'ㅘ': ['wa', 'а'], 'ㅙ': ['wae', 'аэ'], 'ㅚ': ['wae', 'аэ'], 'ㅛ': ['yo', 'о'], 'ㅜ': ['woo', 'оо'],\
               'ㅝ': ['wa', 'а'], 'ㅞ': ['wae', 'аэ'], 'ㅟ': ['wi', 'и'], 'ㅠ': ['yoo', 'оо'], 'ㅡ': ['we', 'э'], 'ㅢ': ['wi', 'и'], 'ㅣ': ['i', 'и']}

# 종성 리스트. 00 ~ 27 + 1(1개 없음)
Last = ['', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
Last_dict = {'' : ['', ''],'ㄱ' : ['g', 'г'], 'ㄲ' : ['k', 'к'], 'ㄳ' : ['g', 'г'], 'ㄴ' : ['n', 'н'], 'ㄵ' : ['n', 'н'], 'ㄶ' : ['n', 'н'], 'ㄷ' : ['d', 'д'], 'ㄹ' : ['l','р'], \
             'ㄺ' : ['l','р'], 'ㄻ' : ['l','р'], 'ㄼ' : ['l','р'], 'ㄽ' : ['l','р'], 'ㄾ' : ['l','р'], 'ㄿ' : ['l','р'], 'ㅀ' : ['l','р'], 'ㅁ' : ['m', 'м'],\
             'ㅂ' : ['b', 'б'], 'ㅄ' : ['b', 'б'], 'ㅅ' : ['s', 'с'], 'ㅆ' : ['ss', 'с'], 'ㅇ' : ['ng', 'нг'], 'ㅈ' : ['z', 'дь'], 'ㅊ' : ['ch', 'ц'], 'ㅋ' : ['k', 'к'],\
             'ㅌ' : ['t', 'т'],'ㅍ' : ['p', 'ф'], 'ㅎ' : ['h', 'х']}
'''
a = 'а'
e = 'э'
i = 'и'
o = 'о'
u = 'о'

for key in Second_dict.keys() :
    Second_dict[key][1] = ''
    for s in Second_dict[key][0] :
        if s == 'a' :
            Second_dict[key][1] += a
        if s == 'e' :
            Second_dict[key][1] += e
        if s == 'i' :
            Second_dict[key][1] += i
        if s == 'o' :
            Second_dict[key][1] += o
        if s == 'u' :
            Second_dict[key][1] += u
print(Second_dict)
'''

def convert(test_keyword) :
    result = list()
    for keyword in test_keyword:
        if re.match('.*[ㄱ-ㅎㅏ-ㅣ가-힣]+.*', keyword) is not None:
            char_code = ord(keyword) - BASE_CODE
            char1 = int(char_code / CHOSUNG)
            result.append(First[char1])
            char2 = int((char_code - (CHOSUNG * char1)) / JUNGSUNG)
            result.append(Second[char2])
            char3 = int((char_code - (CHOSUNG * char1) - (JUNGSUNG * char2)))
            result.append(Last[char3])
        else:
            result.append(keyword)
            
    return result

def convert_to_other(lanlist,lantype) :
    result = list()
    index = 0
    for i in range(len(lanlist)) :
        lan = lanlist[i]
        if lan == '' :
            if index % 3 == 2 :
                result.append(' ')
            index = index + 1
            continue
            
        if index % 3 == 0 :
            if lan == 'ㅇ' :
                result.append(' ')
            else :
                result.append(First_dict[lan][lantype])
        elif index % 3 == 1 :
            result.append(Second_dict[lan][lantype])
        elif index % 3 == 2 :
            result.append(Last_dict[lan][lantype])
            result.append('.')
            
        if lan == ' ' or lan == '.' :
            index = index - 1
        index = index + 1
        
    return result

def main() :
    test_keyword = input()
    result = convert(test_keyword)
    print(result)
    lanresult = convert_to_other(result,1)
    print(lanresult)
    print(''.join(lanresult))

main()
