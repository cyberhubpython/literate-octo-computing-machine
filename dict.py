# import random


# userballs = {'r': 0, 'p': 1, 's': 2};
# compballs = {'r': 2, 'p': 0, 's': 1};



# for x in range(15):
#     comp = random.choice([a for a in compballs.keys()]);
#     user = random.choice([b for b in userballs.keys()]);
#     print(comp, user);
#     result =compballs[comp] -  userballs[user]
#     wins = {0: 'comp', 1: 'user', -2: 'user', -1: 'nichya', 2: 'nichya'}


#     print(wins[result]);


wins = {
    'r': 'p',
    'p': 's',
    's': 'r',
};

user = 'r'
comp = 's'

if user == comp: 
    print('nichya');
elif wins[user] == comp:
    print('comp');
else: 
    print('user'); 



1,2,3,4,5,6,7,8,9,10,11,12
