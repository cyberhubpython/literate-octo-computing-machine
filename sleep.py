import time


count = 0;
# last = int(input('create seconds'));
# last = 130;
# while True:
#     time.sleep(1)
#     if count > last:
#         break;
#     count+=1;

#     print(f'{ (last - count ) // 60 } : {(last - count) % 60}');

# print('время вышло');


seconds = 0;
count = 0;
while True:
    time.sleep(0.001)
    print(f'{(count // (60*60)) % (60*60)}:{(count // 60) % 60}:{count % 60}');
    count+=1
    seconds = count % 60;

    print(seconds);