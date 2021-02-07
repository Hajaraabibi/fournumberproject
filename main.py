#w

numbers = open("numbers.txt", "a")
numbers.write("3, 45, 83, 21, 32")
numbers.close()

#r
numbers = open("numbers.txt", "r")
print(numbers.read())

#w

numbers = open("numbers.txt", "w")
numbers.write("i used the W feature, it removed all of the text in my file and replaced it with what i just wrote")
numbers.close()


