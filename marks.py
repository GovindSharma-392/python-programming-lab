num = int(input())
d = {}
sum = 0
for i in range (num):
    r = int(input('roll no:- '))
    name = input('enter name ')
    d1 ={}
    d2 = {}
    for i in range(5):
        sub = input('subject name')
        marks = int(input(f'entermarks of {sub}: '))
        sum+= marks
        d2[sub]= marks
    d1[name]= d2
    d[r]=d1
print(d)
per = (sum/500)*100
print('percentage = ',per,'%')

