# ==============================
# M2C3 Python Assignment
# ==============================

# Exercise 1:
# Create a string, number, list, and boolean

my_string = "Hola Miguelina, bienvenida a Python"
my_number = 25
my_list = ["python", "javascript", "html", "css"]
my_boolean = True


# Exercise 2:
# Grab the first 3 letters in your string

first_three_letters = my_string[:3]
print("Exercise 2:", first_three_letters)


# Exercise 3:
# Grab the first element from your list

first_element = my_list[0]
print("Exercise 3:", first_element)


# Exercise 4:
# Create a new number variable that adds 10 to your original number

new_number = my_number + 10
print("Exercise 4:", new_number)


# Exercise 5:
# Get the last element in your list

last_element = my_list[-1]
print("Exercise 5:", last_element)


# Exercise 6:
# Use split to transform string into a list

names = 'harry,alex,susie,jared,gail,conner'
names_list = names.split(",")

print("Exercise 6:", names_list)


# Exercise 7:
# Get the first word from your string using indexes
# Transform to uppercase
# Create a new string with uppercase word + rest of original string

first_word = my_string.split(" ")[0]   # get first word
first_word_upper = first_word.upper()

rest_of_string = my_string[len(first_word):]

new_string = first_word_upper + rest_of_string

print("Exercise 7:", new_string)


# Exercise 8:
# Use string interpolation to print sentence with number variable

print(f"Exercise 8: My original number is {my_number} and after adding 10 it becomes {new_number}.")


# Exercise 9:
# Print “hello world”

print("Exercise 9: hello world")


# ==============================
# Extra required exercise:
# Create string with "Hola", search it, replace with "adiós"
# ==============================

cadena = "Hola, este es un ejemplo en Python."

indice = cadena.find("Hola")

if indice != -1:
    seleccion = cadena[indice:indice+4]
    print("Found word:", seleccion)

    nueva_cadena = cadena.replace("Hola", "adiós")
    print("Replaced string:", nueva_cadena)
else:
    print("Word not found.")