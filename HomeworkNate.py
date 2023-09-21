#Initial list
countries = ['Japan', 'Canada', 'Italy', 'Germany', 'United Kingdom']
print(countries)
#List in order
print(sorted(countries))
#Intial list (again)
print(countries)
#Reversed sorted list
sorting_countries = sorted(countries, reverse=True)
print(sorting_countries)
#Original list
print(countries)
#Revesing the list / Reversing the reverse
countries.reverse()
print(countries)
countries.reverse()
print(countries)
#Permanent sorted list
countries.sort()
print(countries)
#Reversed permanent sorted list
countries.sort(reverse=True)
print(countries)
#Done