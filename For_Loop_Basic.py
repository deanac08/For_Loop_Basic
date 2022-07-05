
for a in range (0,150):
    print(a)

for b in range (5,1000,5):
    print(b)

for e in range (1,100):
    if e % 5 == 0:
        print('Coding')
    if e % 10 == 0:
        print('Coding Dojo')
print(e)

odds= 0
for num in range (0,500000):
    if num % 2 ==1:
        odds = odds + num
print(odds)

for i in range (2018,0,-4):
    print(i)

lowNum= 2
highNum= 39
mult= 3
for num in range (lowNum,highNum):
    if num % mult == 0:
        print(num)
