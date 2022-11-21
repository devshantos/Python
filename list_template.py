person_one =['Mahir', 'male', '32','Bangladesh', 'mahir@gmail.com','13th October 1999','018172299654']

gender= person_one[1]
if gender == 'male':
    pronoun = 'he'
    relative= 'his'
else:
    pronoun = 'she'
    relative= 'her'

sentence= f'{person_one[0].title()} is the best pogrammer in {person_one[3]}. {pronoun.title()} is the most highly coder in our community. We are proud feel on {relative} work. {pronoun.title()} is now available in {person_one[4]}. {relative.title()} contact number {person_one[-1]}.'

i = 0
while i <= 10:
    print(sentence)
    i= i+ 1
print(sentence)
