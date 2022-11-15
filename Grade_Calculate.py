'''Enter users all subject number
and python store the number'''
Bangla= int(input("Bengali: "))
English= int(input("English: "))
Math= int(input("Math: "))
Grammar= int(input("Grammer: "))
Agriculture= int(input("Agriculture: "))
Social_science= int(input("Social Science: "))
Physical_exercise= int(input("Physical for today: "))
ICT= int(input("Information and Communication Technology: "))
Science= int(input("Science: "))
Religion= int(input("Religion: "))

'''Python calculated the number first they addition the all number 
which user put here and finally python divide the number'''

All= Bangla+English+Math+Grammar+Agriculture+Social_science+Physical_exercise+ICT+Science+Religion
number = All/10
print("Your subtotal number: ")

#Your number list
print(f"Bengali: {Bangla} \nEnglish: {English}\nGrammar: {Grammar}\nAgrciculture: {Agriculture}\nSocila Science: {Social_science}\nPysical Exercise: {Physical_exercise}\nICT: {ICT}\nScience: {Science}\nReligion: {Religion}\nTotal Number: {All}")

'''There is main part. Python calculate logically all input number .Here's processing all 
data and they give output for users defend their input data '''
if number>=80 and number<=100:
    print("You have A+")
elif number>=70 and number <= 79:
    print('You have A-')
elif number>=50 and number<= 69:
    print('You have B')
elif number>=40 and number<=49:
    print('You have C')
elif number>=33 and number<=39:
    print('You have D')
elif number>=0 and number<=32:
    print('You are failed, Next time better luck')
else:
    print('Invalid number, Please try again.')

print("Thanks for using us, hope you are well.")
