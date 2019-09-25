r = open('1.txt','r+')
read = r.read()
wite = r.write('11111')
print(read)
print(wite)
# r.write(read+"dddddxcvxvxc")
# print(r)

r.close()