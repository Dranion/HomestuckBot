import urllib
import pdb
from urllib import request
from bs4 import BeautifulSoup
dave = []

number = 1926
final = 10029

input('start')
f = open("dave.txt", 'w')
f.write('')
f.close()
f = open("dave.txt", 'a')
while (number < final):
    if(number > 1000, number < 10000):
        hs = urllib.request.urlopen(
            "http://www.mspaintadventures.com/?s=6&p=00" + str(number))
    else:
        hs = urllib.request.urlopen(
            "http://www.mspaintadventures.com/?s=6&p=0" + str(number))
    soup = BeautifulSoup(hs.read(), 'html.parser')
    temp = soup.find_all(style="color: #e00707")
    num = len(temp) - 1
    while (num >= 0):
        temp[num] = str(temp[num]).replace("[TG]", '')
        temp[num] = str(temp[num]).replace('<span style="color: #e00707">', '')
        temp[num] = str(temp[num]).replace('</span>', '')
        if((str(temp[num]).find('TG') != -1) or (str(temp[num]).find('Dave') != -1)):
            print("good")
            f.write(str(temp[num]) + '\n')
        else:
            print("bad: " + str(temp[num]))
        num -= 1
    number += 1
    print(temp)
    dave += temp
    dave += "\n"
f.close()
print(dave)
input("End")
