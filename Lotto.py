from random import randint

#help("modules")
#help("_random")

numbers = [] #THIS IS AN EMPTY LIST
while len(numbers) < 6: #WHILE THE LIST HAS LESS THAN 6 ITEMS IN IT
    numbers.append(randint(1, 50)) #ADD A RANDOM NUMBER(INTEGER) TO THE LIST BETWEEN 1 AND 50
numbers.sort(reverse=True) #USE TO SORT INTO NUMERIC ORDER IF NEEDED, DEFAULT LOW TO HIGH (reverse=True TO GO HIGH TO LOW
print(numbers)