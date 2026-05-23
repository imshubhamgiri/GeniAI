fruits = ["apple", "banana", "orange"]  ##this is a list of fruits
fruits[2] = 244.44  ##this will change the third element of the list to 244.44
print(fruits[0])  ##this will print the first element of the list, which is "apple"
print(fruits[2])  ##this will print the third element of the list, which is 244.44
##Lists are mutable, which means you can change their elements after they have been created. In this example, we changed the third element of the list from "orange" to 244.44.
fruits.append("grape")  ##this will add "grape" to the end of the list

print(fruits)  ##this will print the entire list, which is now ["apple", "banana", 244.44, "grape"]