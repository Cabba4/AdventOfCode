from re import A
from xml.etree.ElementTree import tostring


file = open('./input2.txt','r')
lines = file.readlines()
numbers=[]
c=''

for line in lines:
   # print(line)
    for char in line:
        if char!='x' and char !='\n':
            c=c+char
        if char == 'x' or char == '\n':
           # print(c)
            numbers.append(int(c))
            c=''
        if not char:
            break
#print(numbers)
total = 0
ribbon = 0
small = []
for i in range(0,len(numbers),3):
    small.append(numbers[i])
    small.append(numbers[i+1])
    small.append(numbers[i+2])
    small.sort()
    #print(small)
    a = small[0]
    b = small[1]
    c = small[2]
    total = total + 2*((a*b) + (b*c) + (a*c)) + a*b
    ribbon = ribbon + 2*(a+b) + a*b*c
    #print(total)
    #print(small)
    #print("Big",a,"Small",c)
    #print(small)
    small.clear()

print("Total = ", total)
print("Ribbon = ",ribbon)




# while line:
#     print(line)

#     char = line.read(1)
#     if char != 'x':
#         c=c+char
#     if char == 'x':
#         print(c)
#         numbers.append(int(c))
#     if not char:
#         break
#print(numbers)

