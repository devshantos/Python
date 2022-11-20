# Number count
number = int(input("Enter your number: "))
start = 1
while start<= 10:
    print(number, 'x', start, '=', number*start)
    start= start+ 1


# Calculate leaf year
year= [1992, 1254,2020,2021,2020]
i = 0
while i < len(year):
    if year[i] % 4 == 0:
        print(year[i])
    i = i+1


number1= int(input('Enter your number: '))
namota= 1
while namota<= number1:
    print(number1*namota)
    namota= namota+1

