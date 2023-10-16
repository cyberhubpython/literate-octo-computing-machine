try:
    x = int(input('введите число:'));
    # x += 'asd';

    if x < 0: 
       raise Exception('chislo menshe nulya')
    
    print('vsye ok');
except ValueError as error:
    print("это не число", )
    print(error);
    pass
except Exception as error:
  print("Something else went wrong", error)
else:
   print('net oshibok');
finally: 
   print('код завершился с ошибкой или без');

