#Day 30
#File not found
try:
    a_dic = {"key": 'Value'}
    print(a_dic['asdfaf'])
    file = open('a_file.txt', 'r')
except FileNotFoundError:
    file = open('Day 30/a_file.txt', 'w')
    print('noice')

except KeyError as error_message:
    print(f"That key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("file was closed")


#######################
height = float(input("Height: "))
weight = int(input("Weight: "))
if height > 3:
    raise ValueError("Human Height should not be over 3 meters")


########################

#Key Error
# a_dictionary = {"key": "value"}
# something = a_dictionary["non-existent key"]

#Index error
#list = [1,2,3]
#item = list[10]

#TypeError
#text = abc
#print(text + 5)



#NOTES!
#DONT USE MULTIPLE ERRORS IN THE SAME TRY/EXCEPT MODULE... Actually you can, but specifiy the except to specific error