import easyocr
import re
import math

def count_digit(n): 
    return math.floor(math.log10(n)+1) 

reader = easyocr.Reader(['en'])
result = reader.readtext('test2.png')

print(result)

result = result[:3]

for item in result:
    print(item[1].split())

def get_info_from_img(arr):
    gender = None
    DOB = None
    first_name = None
    last_name = None
    MRN = None
    for a in arr:
        a = a[1].split()
        for elem in a:
            try:
                elem = re.sub(r"[^a-zA-Z]+", "", elem)
                elem = elem.lower()
                print(elem)
                # Gender test
                if elem == 'male' or elem == 'female':
                    gender = elem.lower()
                if count_digit(int(elem)) == 10:
                    MRN = int(elem)
            except Exception as e:
                continue

    print(gender, DOB, first_name, last_name, MRN)

print(get_info_from_img(result))