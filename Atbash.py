codeAlph = {'а': 'я', 'б': 'ю', 'в': 'э', 'г': 'ь', 'д': 'ы', 'е': 'ъ', 'ё': 'щ', 'ж': 'ш', 'з': 'ч', 'и': 'ц', 'й': 'х', 'к': 'ф', 'л': 'у', 'м': 'т', 'н': 'с', 'о': 'р', 'п': 'п', 'р': 'о', 'с': 'н', 'т': 'м', 'у': 'л', 'ф': 'к', 'х': 'й', 'ц': 'и', 'ч': 'з', 'ш': 'ж', 'щ': 'ё', 'ъ': 'е', 'ы': 'д', 'ь': 'г', 'э': 'в', 'ю': 'б', 'я': 'а', 'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'u', 'f': 't', 'g': 's', 'h': 'r', 'i': 'q', 'j': 'p', 'k': 'o', 'l': 'n', 'm': 'm', 'n': 'l', 'o': 'k', 'p': 'j', 'q': 'i', 'r': 'h', 's': 'g', 't': 'f', 'u': 'e', 'w': 'd', 'x': 'c', 'y': 'b', 'z': 'a'}
f1 = open('textInputAtbash.txt', 'r')
# сначала шифруем текст и выводим в файл
new_text = ''
for line in f1:
    new_str = ''
    for c in line:
        if c.isalpha():
            if c.isupper():
                new_str += codeAlph[c.lower()].upper()
            else:
                new_str += codeAlph[c]
        else:
            new_str += c
    new_text += new_str
f2 = open('textOutputAtbash.txt', 'w')
f2.write(new_text)
# теперь дешифруем его обратно
decode_text = ''
for line in new_text:
    decode_str = ''
    for c in line:
        if c.isalpha():
            if c.isupper():
                decode_str += codeAlph[c.lower()].upper()
            else:
                decode_str += codeAlph[c]
        else:
            decode_str += c
    decode_text += decode_str
f4 = open('textDecodeAtbash.txt', 'w')
f4.write(decode_text)
f1.close()
f2.close()
f4.close()

    