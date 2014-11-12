import csv
from random import shuffle

countries = list()
ffname = list()
mfname = list()
lname = list()

with open('Countries.csv', 'rt', encoding='utf8') as f:
    reader = csv.reader(f, delimiter=',', quotechar='|')
    for row in reader:
        row = "".join(row)
        countries.append(row)



with open('mfname.csv', 'rt', encoding='utf8') as f:
    reader = csv.reader(f, delimiter=',', quotechar='|')
    for row in reader:
        row = "".join(row)
        mfname.append(row)

with open('ffname.csv', 'rt', encoding='utf8') as f:
    reader = csv.reader(f, delimiter=',', quotechar='|')
    for row in reader:
        row = "".join(row)
        ffname.append(row)



with open('lname.csv', 'rt', encoding='utf8') as f:
    reader = csv.reader(f, delimiter=',', quotechar='|')
    for row in reader:
        row = "".join(row)
        lname.append(row)

#print(countries)
#print(fname)
#print(lname)

print("[XComGame.XGCharacterGenerator]")
for x in countries:
    b = len(mfname)*.8
    print("m_arr%sMFirstNames=\"%s\"" % (x, b))
    for a in mfname:
        print("m_arr%sMFirstNames=\"%s\"" % (x, a))
    b = len(ffname)*.8
    print("m_arr%sFFirstNames=\"%s\"" % (x, b))
    for a in ffname:
        print("m_arr%sFFirstNames=\"%s\"" % (x, a))
    b = len(lname)*.8
    print("m_arr%sLastNames=\"%s\"" % (x, b))
    for c in lname:
        print("m_arr%sLastNames=\"%s\"" % (x, c))
    shuffle(ffname)
    shuffle(mfname)
    shuffle(lname)
