##---- First_30_min 

# print("amulya")
# print(" * ")
# print('*  *')
# print("*" * 4)
# print('*  *')


# #variables
# customer_name = "Manasa"
# bill_amount = 119.6
# payment_method = 'cash'
# is_new_customer = True

# print(customer_name)
# print(bill_amount)
# print(payment_method)
# print(is_new_customer)

# ##receiving_input

# name = input("what is your name? " )
# fovorite_game = input('what is your favorite game? ')
# print(name + " likes " + fovorite_game)



#type convertsion

#birth_year = input("Birth year: ")
#print(type(birth_year))
#age = 2022-int(birth_year)
#print(type(age))
#print(age)



#converting_weight

#weight_lbs = input('weight (lbs): ')
#weight_kg =float(weight_lbs) * 0.45
#print(weight_kg)


###---- second_30_min


#strings

# course = ''' 
# Hi Ammu,

# Here is the message to you..

# Thank you,
# The support team.

# '''
# print(course)


# ##
# course = "Python for Beginner's"
# print(course[0:])


#         ####in_strings_dot_methods

# course = "Python for Beginners"
# print(course.upper())
# print(course.find("e"))
# print(course.replace("Beginners" , "Students"))
# print('for' in course)


#  ###Augmented_assigment-opertor

# x = 90
# x /= 3
# print(x)


# ##
# x = 8.9
# print(round(x))
# print(abs(-8.9))

# is_hot = False
# is_cool = False

# if is_hot:
#         print("It's a hot day")
#         print('Eating ice cream is good')
# elif is_cool:
#         print("Its a cool day")
#         print("Drinking hot tea is good")
# else:
#         print("It's a lovely day")
#         print('we can eat anything')
# print('Enjoy your day😊')


###-----second hour(next_15_minutes_approximatly)
           #logical_operater(first_15_minutes)

has_high_score = True
has_high_experience = True

if has_high_score and has_high_experience:
        print("Eligible for the job")

has_high_experience = True
has_criminal_record = False

if has_high_experience and not has_criminal_record:
        print("Eligible for the job")


                ###comparison_operators

ice_cream = -10

if ice_cream  < -10:
    print("ice cream is very nice")
elif ice_cream > -10:
    print("ice is not bad")
else:
    print("ice cream is ready good to eat")


        ######(next_15_minutes_approximatly)
        #---weight_converter_program--

# weight = int(input("weight: "))
# unit = input('(L)bs or (K)g: ')
# if unit.upper() == "L":
#     converted = weight * 0.45
#     print(f"You are {converted} kilos")
# else:
#     converted = weight / 0.45
#     print(f"You are {converted} pounds")


        ######(next_15_minutes_approximatly)
        #---while_loops

i = 1
while i <= 3:
    print('1' * i)
    i = i + 1
print('finish')

secret_number = 2
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print('You won!')
else:
    print('Better luck next time')



        ######(next_15_minutes_approximatly)
        #---car_game_using_while_loops

# command = ""
# while True:
#     command = input(" -> ").lower
#     if command == "start":
#         print("Car started..Ready to go....")
#     elif command == "stop":
#         print("Car stoped!")
#     elif command == 'help' :
#         print('''
#         start - To start the car.
#         stop - To stop the car.
#         quit - To quit the game.
#         ''')
#     elif command == 'quit':
#         break
#     else:
#         print("Sorry i don't understand that!")


        ######(next_15_minutes_approximatly)
        #---for_loops

# for item in range(3, 33,3):
#         print(item)

# prices = [30, 40, 50]

# total = 0
# for price in prices:
#         total += price
# print(f"Total : {total}")