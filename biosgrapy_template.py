person= [
    ['shajeed khan','male', ' Actor , Director, Scriptwriter', 'indian', 'Mumvai', 'islam','32'],
    ['Shaleen Bhanot','male', ' Actors', 'indian', 'Mumvai', 'islam','32'],
    ['Shaleen Bhanot', 'female',' Actors', 'indian', 'Mumvai', 'islam','32'],
    ['Shaleen Bhanot','male', ' Actors', 'indian', 'Mumvai', 'islam','32'],
    ['Shaleen Bhanot','female', ' Actors', 'indian', 'Mumvai', 'islam','32']
]

i = 0
while i <= len(person):
    single_person = person[i]
    name= single_person[0]
    gender = single_person[1]
    passion = single_person[2]
    country = single_person[3]
    home_town = single_person[4]
    religion = single_person[5]
    age = single_person[6]
    i = i + 1

    if gender == 'male':
        pronoun= 'he'
        relative = 'him'
    else:
        pronoun= 'she'
        relative='her'

    sentence = f'Are you a follower of {name.title()} {pronoun.title()} is one of the experienced {passion} in the industry. We have added the detailed biography of this actor. If you want to know more about {name.title()}, we have some good news for you. We have added details of {name.title()}s net worth, age, height, and other details. Let’s move on to the next section.{name.title()}, a {age}-year-old actor from {home_town.title()}, will compete and enter the Bigg Boss house. {name.title()} is a television actor who debuted in 2004’s wildly successful reality series MTV Roadies. In addition, the reality star competed in Nach Baliye 4 with his ex-wife Dalljiet Kaur and won. Popular television programs like Kulvaddhu and Naagin 4: Bhagya Ka Zehreela Khel have featured the actor. {relative} appearance on Fear Factor: Khatron Ke Khiladi 10 was as a guest contestant.'
    print(sentence)
