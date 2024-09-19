my_input= input("please provide a number: ")#asking the user to input a number
my_number =int(my_input) # converting text to int (aka number)
if(my_number == 0):
    print("the number is neutral")#skipping this line to go to else ifs if the number is not equal to 0

elif(my_number > 0):#elif is combined for else if to make things easier for the code
            
            print("The number is positive") #you have to indent in order to show that the number is really positive
    #if you dont indent and its a negative number it will still print that the number is positive. 
else:
            print("the number is negative")

print("program finished") # this is when the number is not ositive and it will print this 