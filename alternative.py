#Setting the input and the new string as string variables.

string = input("Please enter whatever you want")
new_string = ""

#Using a for loop to separate every character, then an if statement to switch the even/odd index of string over to upper or lower case.
#% or modulo provides the method for generating either 0 or 1 in any situation, so we can use this to create a 2 part conditional

for i in range(len(string)):
    char = string[i]
    if i % 2 == 0:
        char = char.upper()
    else:
        char = char.lower()
    new_string += char
print(new_string)

#By starting with the unspecified split attribute, this will remove any of the whitespace in the string and take th ein between as items in a list.
#String_list is a list
#for every component in that list, w ewill use the same method as above to change either to lower or upper case.
#Then we can use the join function at the end to bring together all the separated components in the list, to one string

string_list = string.split()
string_list2 = []
for i in range(len(string_list)):
    word = string_list[i]
    if i % 2 == 0:
        word = word.lower()
    else:
        word = word.upper()
    string_list2.append(word)

print(" ".join(string_list2))
