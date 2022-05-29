n = int(input('How many numbers: '))
total_sum = 0

for i in range (n):
    num = float(input('Enter number: '))
    total_sum += num
avg = total_sum / n
print('The average value of numbers = %0.2f' %avg)