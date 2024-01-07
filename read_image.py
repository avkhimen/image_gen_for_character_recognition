import easyocr
import re
import math

def countDigit(n): 
    return math.floor(math.log10(n)+1) 

reader = easyocr.Reader(['en'])
result = reader.readtext('test2.png')

print(result)

result = result[:3]

for item in result:
    print(item[1].split())

def determine_gender(arr):
    gender = None
    DOB = None
    first_name = None
    last_name = None
    for a in arr:
        a = a[1].split()
        for elem in a:
            try:
                elem = re.sub(r"[^a-zA-Z]+", "", elem)
                elem = elem.lower()
                # Gender test
                if elem == 'male' or elem == 'female':
                    gender = elem.lower()

            except Exception as e:
                continue

print(determine_gender(result))