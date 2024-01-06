import easyocr
import re

reader = easyocr.Reader(['en'])
result = reader.readtext('test2.png')

print(result)

result = result[:3]

for item in result:
    print(item[1].split())

def determine_gender(arr):
    for a in arr:
        for elem in a:
            try:
                elem = re.sub(r'[^A-Za-z]', '', elem)
                elem = elem.lower()
                if elem == 'male' or elem == 'female':
                    return elem.lower()
            except Exception as e:
                continue

print(determine_gender(result))