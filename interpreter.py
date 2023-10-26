# Написать программу,
# которая будет выполнять обработку естественного языка.
# Например, перевод текста, генерация текста, понимание текста и т.д.

def dictionary(text: str):
	words= {
		"grab": "взяла",
		"a cup":"чашку",
		"of coffee": "кофе",
		"I did":"Я" 
	}
	for (wkey, wvalue) in words.items():
		text =  text.replace(wkey, wvalue);
	return text;

print(dictionary("I did grab a cup of coffee"));