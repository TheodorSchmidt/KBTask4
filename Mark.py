dictAplpha = {'с': '1', 'е': '2', 'н': '3', 'о': '4', 'в': '5', 'а': '6', 'л': '7', 'б': '82', 'г': '83', 'д': '84', 'ж': '85', 'з': '86', 'и': '87', 'й': '88', 'к': '89', 'м': '80', 'р': '92', 'т': '93', 'у': '94', 'ф': '95', 'х': '96', 'ц': '97', 'ч': '98', 'ш': '99', 'щ': '90', 'ы': '02', 'ь': '03', 'э': '04', 'ъ': '05', 'ю': '06', 'я': '07', '.': '08', ',': '09'}
dictDecode = {'1': 'с', '2': 'е', '3': 'н', '4': 'о', '5': 'в', '6': 'а', '7': 'л', '82': 'б', '83': 'г', '84': 'д', '85': 'ж', '86': 'з', '87': 'и', '88': 'й', '89': 'к', '80': 'м', '92': 'р', '93': 'т', '94': 'у', '95': 'ф', '96': 'х', '97': 'ц', '98': 'ч', '99': 'ш', '90': 'щ', '02': 'ы', '03': 'ь', '04': 'э', '05': 'ъ', '06': 'ю', '07': 'я', '08': '.', '09': ','}
f1 = open('textInputMark.txt', 'r')
new_text = ''
# шифруем текст
for line in f1:
    new_str = ''
    i = 0
    while i != len(line):
        # если встретились цифры то перебираем строку пока они не кончатся
        # и обрамляем слешами с двух сторон
        if line[i].isdigit():
            new_str += '/'
            while line[i].isdigit():
                new_str += line[i]
                i += 1
            new_str += '/'
            i -= 1
        # кодируем символы
        elif line[i].isalpha() or line[i] == '.' or line[i] == ',':
            new_str += dictAplpha[line[i].lower()]
        # переносим без изменений то чего нет в словаре
        else:
            new_str += line[i]
        i += 1
    new_text += new_str
print(new_text)
f2 = open('textOutputMark.txt', 'w')
f2.write(new_text)
# декодируем
decode_text = ''
i = 0
symb = ''
isdigit = False
digit = ''
while i != len(new_text): 
    # если встретили слеш, проверяем запись числа на данный момент
    # если число не записывается, включаем запись числа
    # если запись числа идет, добавляем в число цифры
    # если встретили слеш и запись числа идет, останавливаем запись
    if new_text[i] == '/' and isdigit == False:
        isdigit = True
    elif new_text[i] != '/' and isdigit == True:
        digit += new_text[i]
    elif new_text[i] == '/' and isdigit == True:
        decode_text += digit
        digit = ''
        isdigit = False
    # если на данный момент не записываем составной символ и встретили 8, 9 или 0
    # то начинаем запись составного символа
    # если на данный момент в составном символе записана цифра, то добавляем еще одну,
    # после чего декодируем и обнуляем составной символ
    elif (symb == '') and (new_text[i] == '8' or new_text[i] == '9' or new_text[i] == '0'):
        symb = new_text[i]
    elif symb != '':
        symb += new_text[i] 
        decode_text += dictDecode[symb]
        symb = ''
    # во всех остальных случаях декодируем простой символ, а не транслируемые переписываем в исходном виде
    elif new_text[i].isdigit():
        decode_text += dictDecode[new_text[i]]
    else:
        decode_text += new_text[i] 
    i += 1
f3 = open('textDecodeMark.txt', 'w')
f3.write(decode_text)
f1.close()
f2.close()
f3.close()
    


