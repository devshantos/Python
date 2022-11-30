post= {
    'id': '100',
    'Author': 'devshants',
    'Name': 'devshantos theme',
    'Future': 'Awesome future',
    'Catagory': 'devloper theme',
    'Slug':'devetol-theme',
    'Descrtiption':'This is awsome theme. Hundred of people using the theme and very smooth and handy theme for you.'

}

id= post.get('id')
author=post.get('Author')
name= post.get('Name')
future= post.get('Future')
catagory= post.get('Catagory')

final = id,author,name,future,catagory
value= post.values()
keys= post.keys()
print(list(keys))
print(list(value))

post['Catagory']= 'Genius'
print(post)

car= {
    'name': 'Volbo',
    'color': 'red',
}


car.update({'model':'02020'})
car.update({'Price': '758100014BDT'})
car.update({'Suspansion': 'Yes'})
car.update({'hedlight': 'Right indicator'})
keys= car.keys()
value= car.values()
print(car)
print(list(keys))
print(list(value))

my_company={
    'staf':'50',
    'catagory':'tech',
}

my_company['catagory']= 'tech and developer'
my_company.update({'salary':'20k'})
my_company.update({'agreement': '4years'})
my_company.update({'working_style': 'offline online two'})
print(my_company)
print(my_company)
