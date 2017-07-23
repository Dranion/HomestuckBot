# BUG:
#
#

import urllib
from bs4 import BeautifulSoup


number = 1926
final = 10029

f = open("chat.txt", 'w')
f.write('')
f.close()
f = open("chat.txt", 'a')
while (number < final):
    text = []
    if(number > 1000, number < 10000):
        hs = urllib.request.urlopen(
            "http://www.mspaintadventures.com/?s=6&p=00" + str(number))
    else:
        hs = urllib.request.urlopen(
            "http://www.mspaintadventures.com/?s=6&p=0" + str(number))
    soup = BeautifulSoup(hs.read(), 'html.parser')
    pesterlog = soup.find(class_="spoiler")
    if pesterlog is not None:
        spans = pesterlog.find_all("span")
        for span in spans:
            value = span.string
            print("VALUE + " + str(value))
            if value is not None:
                if(len(text) > 0) and (text[-1][:2] == value[:2]):
                    text[-1] += (" " + value)
                else:
                    text.append(value)
        del text[:2]
        print(text)
        text += "\n"
        f.write("\n".join(text))
    print(number)
    number += 1

f.close()
print(text)
