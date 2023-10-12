

'{"asdf": [], "asd":"sdf", "sdf": 433}'

{"sad":["ads"], "sdf": "dsfs", 'asff': 342, }



user = {
    'name': 'Sasha',
    'surname': 'Raimov',
    'age': 24,
    'name': 'Sasha 2',
    2: 'asd',
    'cars': [
        {
            'color': 'red',
            'brand': 'tesla'
        },
        {
            'color': 'black',
            'brand': 'rolls royce'
        },
    ], 
};

user['age'] = 32;

print(user);

for car in user['cars']:

    print(car['brand']);


for key, value in user.items():
    print(key, value);



print(user.items());


user2 = dict(name = 'ddffsf', surname = "sd");

print(user2.get('age'))

print('age' in user2);

print(user.keys());

print(user.values());


user.update({'name': 'Oybek', 'surname': "Noone", 'gender': 'man'});

print(user);

# user.pop('gender');
user.popitem();
# user.clear();
# user = {};

user3 = user.copy();

user3['name'] = "Mokhinur"
# print(user.fromkeys(['name', 'surname'], 'afgfd'));

print(user3.setdefault('awf', 'fdga'))


print(user3);


