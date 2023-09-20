# Skapar en lista med [0,1,...8,9]!!! Kallas list comprehensions
list_of_numbers =  [i for i in range(10)]

# Vi kan skriva kod som tex loopar igenom något och 
# vi kan då skriva varje objekt för sig till filen
with open('my_file2.txt', 'w') as f:
    for i in list_of_numbers:
        f.write(f'{i}->{i**2}->{i**3}->{i**4}\n')