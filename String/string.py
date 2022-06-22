text = "Rays"
text=text.split(' ')
reverse_text=' '.join(reversed(text))
print(reverse_text)


text="Rays"[::-1]
print((text))

# print(------------------------------------------------------------------------------>)

strt1 = "Hari is a good boy"
strt2 = "Hari"
if strt1.startswith(strt2):
    print("start1 Is begin With:", strt2)
else:
    print("Start1 is not begin with", strt2)


if strt1.endswith(strt2):
    print("Strt11 Is End with :", strt2)
else:
    print("Strt1 Is not end With:", strt2)

# print(------------------------------------------------------------------------------>)

strt1 = "HARI IS A GOOD BOY"
strt2 = "Hari"
if strt1.isupper():
    print("All the character are in strt1 is upper cased")
else:
    print("All the character are in strt1 is Not upper cased")

if strt2.islower():
    print("All the characters are lower cased")
else:
    print("All the characters are Not lower cased")

# print(------------------------------------------------------------------------------>)

string1 = "HaRRY Is a gOOd Boy"

string2 = string1.swapcase()
print("The swapcase convert the string in:", string2)

string3 = string1.upper()
print("The uppercase convert the string in:", string3)

string4 = string1.lower()
print("The lowercase convert the string in:", string4)

string5 = string1.title()
print("The tile is convert the string in a title:", string5)


s = text[::-1]
print(s)

# print(------------------------------------------------------------------------------>)

text = "HariomPatidar"
mi = int(len(text)/2)
ras = text[mi-1:mi+2]
print(ras)

# print(------------------------------------------------------------------------------>)

text1 = "HariomPatidar"
text2 = "MansiGupta"
mi = int(len(text1)/2)
x = text1[:mi:]
x = x+text2
x = x+text1[mi:]
print(x)

# print(------------------------------------------------------------------------------>)

text1 = "Hariom Patidar"
text2 = "MsGupta"
ar = text1.split(" ")
print(ar[0]+" "+text2+" "+ar[1])

# print(------------------------------------------------------------------------------>)

text1 = "Hjhshds65454545484@#$$#@@#$#"

char_count = 0
digit_count = 0
special_count = 0
for char in text1:
    if char.isalpha():
        char_count += 1
    elif char.isdigit():
        digit_count += 1
    else:
        special_count += 1

print("Alfabetic=", char_count, "Digit=",
      digit_count, "Special=", special_count)

# print(------------------------------------------------------------------------------>)

s1 = "Abc"
s2 = "Xyz"

length_s1 = len(s1)
length_s2 = len(s2)

length = length_s1 if length_s1 > length_s2 else length_s2
result = ""

s2 = s2[::-1]

for i in range(length):
    if i < length_s1:
        result = result+s1[i]
    if i < length_s2:
        result = result+s2[i]
print(result)

# print(------------------------------------------------------------------------------>)

s1 = "yessssss"
s2 = "RaysClasses"


def test(s1, s2):
    flag = True
    for char in s1:
        if char in s2:
            continue
        else:
            flag = False
    return flag


flag = test(s1, s2)
print("s1 and s2 are Balanced", flag)

# print(------------------------------------------------------------------------------>)

s1 = "Wlcome INDIA ,india awesome India ,isn't it "
s2 = "INDIA"

low_s1 = s1.lower()
count = low_s1.count(s2.lower())
print("The india in string s1 is:", count)

# print(------------------------------------------------------------------------------>)

str1 = "PYnative29@#84962"

sum = 0
cnt = 0

for chr in str1:
    if chr.isdigit():
        sum += int(chr)
        cnt += 1
avg = sum/cnt
print("Sum is:-", sum, "Avrage is:-", avg)

# print(------------------------------------------------------------------------------>)

s1 = "Apple"

dic = dict()

for chr in s1:
    count = s1.count(chr)
    dic[chr] = count
print(dic)

# print(------------------------------------------------------------------------------>)

str1 = "Emma is a data scientist who knows Python. Emma works at google."

print("The given string is:-", str1)

# print(------------------------------------------------------------------------------>)

find = str1.rfind("Emma")
print("Last Fomate of Emma at index", find)

# print(------------------------------------------------------------------------------>)

str1 = "Emma-isa-a-data-scientist"
hyp = str1.split("-")
for i in hyp:
    print(i)

# print(------------------------------------------------------------------------------>)