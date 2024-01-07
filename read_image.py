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
        a = a[1].split()
        for elem in a:
            try:
                elem = re.sub(r"[^a-zA-Z]+", "", elem)
                elem = elem.lower()
                #print(elem)
                if elem == 'male' or elem == 'female':
                    return elem.lower()
            except Exception as e:
                continue

print(determine_gender(result))