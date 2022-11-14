#Check your health and take good adviced
normal_tempreture= 90.00
your_tempreture= float(input("Enter your normal tempreture: "))
if your_tempreture > normal_tempreture:
    print("You should take some medicine for now. Pls go the doctor chamber and take advised. I hope you are well soon.\nThanks,\nYour docotor\nPicaso.")
else:
    print("Don't worry. You should take some rest and some vitamins.\nThanks,\nYour doctor \nPicaso")

#Your favourite hero
your_actress=input("Enter your favourite actress name: ")
gender=input("Enter your gender: ")
nationality=input("Enter country name: ")

if gender== "Male":
    profession="Actor"
    pronoun="He"
    tag="hero"
else:
    profession= "Actress"
    pronoun="She"
    tag="heroen"

print(f"{pronoun} is the {profession} in {nationality}. {pronoun} is one of the number {tag} in the {nationality} ")


