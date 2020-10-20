# TODO Create Variables
#   - Create the following variables
#   - my_first_name
#       -set this equal to your first name
#   - my_last_name
#       -set this equal to your last name
#   - my_year_of_birth
#       -set this equal to your birth year (doesn't have to be real should be less then 100 yrs ago)
#   - current_year
#       -set this equal to 2020
my_first_name = 'Scott' # Python var assignment does not require a keyword
my_last_name = 'Hadzik'
my_year_of_birth = 1980 # string or int or float python loosely typed
current_year = 2020
email_address = '@hmail.com'

# print(my_first_name)
# print(my_first_name + my_last_name) # + is a concat of a string
# print(my_first_name + ' ' + my_last_name) # + is a concat of a string
# print(my_first_name + '.' + my_last_name + email_address) # + is a concat of a string


# TODO String Indexing
#   - Print the following items (one per line) (print using variables)
#       - first name  
#       - last name
#       - first letter of your first name (use the +index)
#       - last letter of your last name (use the -index)
#       - first two letter of your first name (use the +index)
#       - last two letter of your last name (use the -index)

# first_letter = my_first_name[0]
# first_initial = my_first_name[0]
# last_initial = my_last_name[0]
# initials = first_initial + '.' + last_initial + '.'

# print('My initials are ' + initials)

# print ('first letter of your first name:' + my_first_name[0])
# print ('first letter of your first name:' + first_letter)
# print ('last letter of your last name:' + my_last_name[-1])

# first_two_name = my_first_name[0:2] # option to leave 0 blank
# last_two_name = my_last_name[-2:]

# print(' First two letter: ' + first_two_name)
# print(' Last two letter: ' + last_two_name)


# print (my_first_name)
# print (my_last_name)
# print (my_first_name[0])
# print (my_last_name[-1])
# print (my_first_name[:2])
# print (my_last_name[-2:])

#TODO Combining Strings
#   - Print the following items (one per line) (print using variables)
#       -first name and last name combined
#       -first name six times
# print (my_first_name + my_last_name)
# print (my_first_name * 6)
# print (my_first_name, my_last_name)

# print (first_letter * 6 )
# print (my_first_name, my_last_name)


# # TODO Formatting Strings 
# #   - Print the following items (one per line) (print using variables)
# #       - first name last name -was born in- year of birth
# #       - first name last name -was born in- year of birth. first name -enjoyed celebrating- current year
# txt = my_first_name + my_last_name + ' was born in {}'
# print (txt.format(my_year_of_birth))
# txt2 = my_first_name + my_last_name + ' was born in {}. {} enjoyed celebrating {}'
# print (txt2.format(my_year_of_birth, my_first_name, current_year))

birth_year = my_first_name + my_last_name + ' born in {}.'
print (birth_year.format(my_year_of_birth))

birth_year_message = my_first_name + my_last_name + ' was born in {}. {} enjoyed celebrating {}'
print(birth_year_message.format(my_year_of_birth, my_first_name, current_year))

my_birth_year_string = str(my_year_of_birth)
print ('birth year string ' + my_birth_year_string)


# # TODO Escape characters
# #   - Print the following items (one per line) (print using variables)
# #       - possesive first name -birth year is- year of birth 
# #       - tab last name current year

print ('Scott\s birth year is' + my_birth_year_string)
print ('\t' + my_last_name , str(current_year))


# # TODO String methods
# #   - Print the following items (one per line) (print using variables)
# #       - first name and last name in lower case
# #       - length of last name
# #       - first name and last name all in upper case
# print (my_first_name.casefold(), my_last_name.casefold())

# print (str(len(my_last_name))) # scotthadzik  ScotThadzik

# print (my_first_name.upper(), my_last_name.upper())

my_first_name = my_first_name.casefold()
print (my_first_name.casefold() , my_last_name.casefold())
print('first name: ' + my_first_name)
# print('lower name: ' + lower_name)