import random
mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD','made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
    ],
    'exchnage_rate': 103.25
}

datas = mobile_data.get('data')
for data in datas:
    name= data.get('name')
    price = data.get('price')
    price1= price.split(" ")
    bdt_price = mobile_data.get('exchnage_rate') * float(price1.__getitem__(0))
    final_price = round(bdt_price)
    made= data.get('made')
    first_line = [
        f'{name} is made by {made}',
        f'{made} made is {name}',
    ]
    second_line = [
        f'The price is {price} usd',
        f'They declared thiere price {price} USD',
        f'This price is {price} USD'
    ]
    third_line = [
        f'Which is almost eqaul to {final_price} BDT',
        f'BDT price {final_price}',
        f'This price conatin BDT {final_price}'
    ]
    final_first_line = random.choice(first_line)
    final_second_line = random.choice(second_line)
    final_third_line = random.choice(third_line)
    article = f'{final_first_line}. {final_second_line}. {final_third_line}'
    print(article)



