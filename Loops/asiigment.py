name = "HariPatidar2207"
size = len(name)
i = 0
while i < size:
    if name[i].isdigit():
        break
    else:
        print(name[i])
        i = i+1

# print(--------------------------------------------------------------------------------->)

a = "HariommmPamtidaeaa"
i = 0
while i < len(a):
    if a[i] == 'm' or a[i] == 'a':
        i += 1
        continue
    print("Current Latter", a[i])
    i += 1

# print(--------------------------------------------------------------------------------->)
