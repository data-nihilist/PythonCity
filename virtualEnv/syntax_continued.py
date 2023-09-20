print("Hello!\n\n\n\t\t-From: TuplesAndLists.py")

# Two of Python's most common built-in data structures - called "collections"
#are Tuples and Lists:

#-------------------------------------Lists (mutable)

cheeses = [ "Red Leicester", "Tilsit", "Caephilly", "Bel Paese" ]

print(cheeses[1])
cheeses[1] = "Cheddar"
print(cheeses[1])

# We can assign and reassign the values of individual items with bracket notation

#--------------------------------------Tuples (immutable)

# Tuples cannot have items added, reassigned, or removed after its creation.
#       # Attempting to do so using bracket notation will throw a TypeError exception

answers = ("Sir Lancelot", "To seek the holy grail", 0x0000FF)

print(answers[0])
# answers[0] = "King Arthur" # raises TypeError: 'tuple' object does not support item assignment
print(answers[0])

# Lists are for collections of items of the same type (homogenous)
# Tuples are for collections of different types (heterogenous)

#                                          L00ping

#------------------------------------------------------------------------------------------------------------------------------------------the while l00p
# Ideal for when we don't know how many iterations of the l00p are required until True
n = 0

while n < 10: # as long as n is less than 10, add 1 to n and print it to console in that exact order
    n += 1
    print(n)

# We can manually control the loop using continue break
while True:
    command = input("Enter command: ")
    if command == "exit":
        break
    elif command == "sing":
        print("La la LAAA")
        continue            # here the keyword continue is basically telling us, "Okay now stop here (line 47) and go back to line 42"

    print("Command unknown.")

# True is always True - so this 'while True:' l00p is inherently infinite

# That's the behavior we expected here, since we want to keep iterating until the user
#enters 'exit', where we've implemented the break keyword

# The 'sing' has a different behavior, as we want to immediately go to the top and prompt the user for input.
            # We are also skipping the final print statement
# continue abandons the current iteration and jumps back to the top of the l00p

#------------------------------------------------------------------------------------------------------------------------------------------the for l00p

# Technically this is a 'for-in' (or "for-each") l00p, meaning the loop iterates once for each item in the given range, list, or other collection
# This means that the l00p needs something to iterate over--in this case, a special object called range()--

for i in range(1, 11):
    print(i)

# range() iterates over a range of values, returning each one in turn.
# We specified that we want the range to start with the value 1 and end before 11.

#                                                       Structural Pattern Matching

#----------------Python's equivalent to the switch-statement: match case
# for fun: look up "Duff's Device" on wikipedia
# In the most basic use case, we can check a variable against different possible values.
#These are called literal patterns.

lunch_order = input("What would you like for lunch? ")

match lunch_order:
    case "pizza":
        print("Pizza time!")
    case "sandwich":
        print("Here's your sandwich")
    case "taco":
        print("Taco, taco, TACO, tacotacotaco!")
    case 'salad' | 'soup':                          # or patterns
        print("Eating healthy, eh?")
    case order:                                     # capture patterns
        print(f"Enjoy your {order}.")
# The value of lunch_order is captured as order; Now, no matter what the user enters,
#if it doesn't match any of the previous case patterns, the value will be captured and displayed in the message here

# We can end our match case statements either by using the above irrefutable ending case statement
#or by a wildcard:

    # case _:
    #     print("Yummy.")

# The underscore (_) in the last case is the 'wildcard'
# The wildcard will match any value - this serves as a fallback case
# The wildcard must come last (irrefutable ending case statement)

#       On match case Statements

# Despite the superficial similarity, match statements are not the same as a C or C++ switch statement. Python's match statements do not have jump tables,
#and they therefore have none of the potential performance gains of a switch.

# But don't feel too disappointed! As this also means they're not limited to working with integer types

# Capture patterns don't just have to capture the entire value.

#We can write a pattern that matches a tuple or list (a 'sequence') and then capture only part of the sequence

if ' ' in lunch_order:
    lunch_order = lunch_order.split(maxsplit=1)

match lunch_order:
    case (flavor, 'ice cream'):
        print(f"Here's your very grown-up {flavor}...lunch.")

# Here, if the lunch order has a space, we split the string into two parts, which are stored in a list.
# Then, if the second item in the sequence as the value "ice cream", the fist part is captured as flavor.

# The capture pattern feature has one surprising downside: all unqualified names in patterns-that is, any bare variable names with no dots-will be used to capture.
# 
# This means that if we want to use the value assigned to some variable, it must be qualified
#meaning we must access it within some class or module with the dot operator:

class Special:
    TODAY = "lasagna"

lunch_order = input("What would you like for lunch? ")

match lunch_order:
    case Special.TODAY:
        print("Today's special is awesome!")
    case "pizza":
        print("Pizza time!")
    case ice_cream if 'ice cream' in ice_cream:
        flavor = ice_cream.replace('ice cream', '').strip()
        print(f"Here's your very grown-up, adult ass, bougie {flavor}...lunch.")
    case order:
        print(f"Enjoy your {order}.")


print("\n\n\t\t-From: TuplesAndLists.py")

#                               Importing & Exporting Functions

# go to syntax_wrapup.py to see this import in action

class smart_door:
    def open():
        print("Ahhhhhhhhhhhhhh.")
    
    def close():
        print("Thank you for making a simple door very happy.")