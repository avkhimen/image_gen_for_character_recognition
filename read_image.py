import easyocr

reader = easyocr.Reader(['en'])
result = reader.readtext('test2.png')

print(result)

for item in result:
    print(item[1].split())