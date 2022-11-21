person = [
    ['moris', '86', 'australian', '13th november 1996', 'nahid@gmail.com','0152845255862','male'],
    ['angel doly', '86','UK', '13th november 1997', 'angeldoly@gmail.com','0154871414','female'],
    ['Smith', '86', 'Brazil', '13th november 1996', 'nahid@gmail.com','0152845255862','male'],
    ['john', '86', 'australian', '13th november 1996', 'nahid@gmail.com','0152845255862','male'],
    ['Rose', '86', 'Spain', '13th november 1996', 'nahid@gmail.com','0152845255862','female'],
    ['jack', '86', 'australian', '13th november 1996', 'nahid@gmail.com', '0152845255862','male'],
    ['Neo', '86', 'australian', '13th november 1996', 'nahid@gmail.com', '0152845255862','male'],
    ['Juti', '86', 'australian', '13th november 1996', 'nahid@gmail.com', '0152845255862','female'],
    ['jetly', '86', 'african', '13th november 1996', 'nahid@gmail.com', '0152845255862','male'],
    ['nency', '86','North Afcica', '13th november 1996', 'nahid@gmail.com', '0152845255862','female']
]


i = 0
while i < len(person):
    single_name= person[i]
    name= single_name[0]
    age = single_name[1]
    country= single_name[2]
    birth = single_name[3]
    gmail= single_name[4]
    number = single_name[5]
    gender = single_name[6]
    i = i+1
    if gender == 'male':
        pronoun = 'he'
        realtive = 'him'
    else:
        pronoun= 'she'
        realtive= 'his'
    sentence = f'{name.title()} is the best football palyer in the {country}. {pronoun.title()} is the top fifa ranking in the fifa federation. Now {pronoun} staying in {country.title()}. we are proud of {realtive}. Now {pronoun} is available to {gmail}. Lets chat with {realtive} to {number}.'

    print(sentence)
