import easyocr

reader = easyocr.Reader(['en'])
result = reader.readtext('test2.png')

print(result)