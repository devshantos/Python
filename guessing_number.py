import random
person= ['Moris', 'Chittaghong']
name= person[0]
location = person[1]

person_group_one= [
    f'My name is {name.title()}',
    f'Is it  {name.title()}',
    f'{name.title()} is my name'
]
person_group_two= [
    f'I live in {location.title()}',
    f'{location.title()} is my home town',
    f'{location.title()} is the best city, where I live'
]

sentence_one=random.choice(person_group_one)
sentence_two= random.choice(person_group_two)
paragraph = f'{sentence_one}. {sentence_two}'
print(paragraph)
