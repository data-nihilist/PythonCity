spam = True
if spam:
    print("Spam, spam, spam, spam, spam...")
    print("This is my first python code!")

eggs = True
if eggs:
    print("Eggs, eggs, eggs, eggs, eggs...")
    print("And this is my second python code! B)")

print("Hello, World!")

print()
                                #                                   Essential Syntax
                                # Each line of code in Python that ends with a line break is a statement.
                                # A section of code that evaluates to a single value is called an expression.
                                # In Python, we can put expressions nearly anywhere a value is expected.
                                # The expression is evaluated down to a value, and that value is used in the position in the statement.
print()


myName = input("What is your name? ")
print("Hello there, " + myName)

# Myth, with a caveat: Python doesn't use semi-colons

mythMessage = "Python doesn't use semi-colons" ; print(mythMessage)

# The Python philosophy places a high value on readability, and the placement of multiple statements on the same line often detracts from that philosophy.
# Stick to placing one statement per line, unless you have a specific reason to do otherwise.

print()

#                                                   The Importance of Whitespace
    
    # When looking at a sample of Python source code, the first thing that jumps out to us is the use of indentation for nesting.
    # A 'compound statement' is made up of one or more 'clauses,' each of which consists of a line of code called a 'header' and a block of code called a 'suite'

    # For example: This program prints different messages, depending on whether a name is specified:
weatherName = "Jason"
if weatherName != "":                       # header
    message = "Hello, " + weatherName + "!" # suite
    print(message)                   # suite
print("I am a computer.")            # this line of code is separate from my if's suite, so it will run as it's own independent statement

raining = True                  # statement
hailing = False                 # statement

if raining:                     # header

    # pass  # We can employ the 'pass' keyword as a placeholder in our 'if raining' conditional until we're able to write the final code.
# Heads up: 'pass' does absolutely nothing. That's the only reason it exists.

    if hailing:                 # suite/header
        print("Nope.")          # suite         This being indented twice is how Python knows it belongs to both preceding conditional statements
    else:                       # suite/header
        print("Umbrella time.") # suite

#                                                   Comments and Docstrings

# As we can ascertain by now, the hash (#) is used to write comments in Python.
# Everything between the hash and the end of the line is a comment and will be ignored by the interpreter.

# This is a comment
print("Hello, comment section!")
print("How are you?") # This is an inline comment.
# Here's another comment
# And another
# And... I think we get the idea.

# Officially, there is no syntax for "multiline" comments; We just comment each line.
# There is one special exception: the docstring. It looks like this:
def make_tea():
    """Will produce a concoction almost,
    but not entirely unlike tea.
    """
    #   ...function logic...

                        # There are three important distinctions between comments and docstrings:

# 1. Dosctrings are string literals, and they are seen by the interpreter; comments are ignored
# 2. Docstrings are used in automatic documentation generation.
# 3. Docstrings are generally only dosctrings when they appear at the top of the module, function, class, or method they define.
                        # Comments can live anywhere
    
    # It's perfectly possible to use a triple-quoted string literal to write a sort of "multiline comment," but it's not recommended since
    #a string literal can easily get left in a place where Python will try to use it as a value.
    
    # In short, use docstrings as intended, and stick with comments for everything else.
    # We can access these dosctrings later in our code. For instance, given the previous example, we can do this:

print(make_tea.__doc__) # This always works
help(make_tea)          # Intended for use in the interactive shell.

                                                # Declaring Variables

    # By now it may have been noticed that Python doesn't have a distinct keyword for declaring a new variable (technically called a 'name' in this language).
name = "Charlie"
points = 4571
print(name)     # Displays "Charlie"
print(points)   # Displays 4571
points = 42
print(points)   # Displays 42

    # Python is dynamically typed, meaning the data type of the value is determined when it is evaluated.
    # This contrasts with statically typed languages in which you declare the data type initially. (C++ and Java are strictly typed)

    # With Python, we can assign a value to a name anytime, by using the assignment operator (=).
            # From here, Python infers the data type.
            # If the name is a new variable, Python will create it
            # If the name already exists, Python will change the value.

                                # In general, there are two rules to follow with Python variables:
                                    # 1. Define a variable before you access it; otherwise, you'll get an error.
                                    # 2. Don't change what kind of data you're storing in the variable, even when replacing a value.

    # Python is considered a 'strongly typed language,' meaning you usually can't magically combine data of different types.
            # Example: It won't allow you to add an integer and a string together
    # 'Weakly typed' languages let you do practically anything with different data types, then try to figure out how to do what you asked for (JavaScript).

    # There's an entire spectrum between those last two terms and plenty of debate about what behaviors qualify under which name.
    # While Python is decidedly in the 'strongly typed' camp, it still has weaker typing than some languages.

    # Python is however 'weakly bound,' so it is possible to assign a value of a different type ot an existing variable.
        # While this is technically permissible, it is strongly discouraged, as it can produce confusing code.
    
    # Python doesn't have any formally defined constants. Instead, we indicate a variable as intending to be constant by using all-caps names with underscores.
            # This naming convention is sometimes humorously referred to as 'screaming snake case'
            # For example: INTEREST_RATE indicates that you don't want the variable redefined or changed in any way.
            # While the interpreter itself won't prevent the variable from being modified, a linter will usually complain if you do.


#                                                           On Math
                        # Python has all the math functionality you would expect from a good programming language.
                        # Its excellent support for both simple and complicated mathematics is one of the reasons Python is so popular for scientific programming.

        # Meet the number types:

# Integers (int) store whole numbers;
            # Are always signed and effectively have no maximum value.
            # Use decimal base (base-10) by default, but they can also be specified in binary (0b101010), octal (0o52), or hexadecimal (0x2A).

# Floating-point numbers (float) store numbers with a decimal part (for example: 3.141592);
            # We can use scientific notation (2.49e4).
            # Internally, values are stored as double-precision, IEEE 754 floating-point numbers, which are subject to the limits inherent in that format.
            # We can also specify:
            # An invalid number with --> float("nan")
            # A number larger than the largest possible value with --> float("inf")
            # Or a number smaller than the smallest possible value with --> float("-inf")

    # Notice we're wrapping these special values in quotes: Because we haven't imported the 'math' module (more on that soon), we need to use this syntax.

    # For fun & more insight into floating-point arithmetic, read: "What Every Computer Scientist Should Know About Floating-Point Arithmetic" by David Goldberg

# Complex numbers can store imaginary numbers by appending j to the value, as in 42j. We can combine a real part with the imaginary part using --> 24+42j
    # An imaginary number has the square root of negative one as one of its factors, even though this value is utterly impossible;
    # There's no value that you can multiply by itself to get negative one! Yet, imaginary numbers still show up in real-world math.

# Decimal & Fractions are two of the additional object types for storing numeric data:
    # Decimal stores fixed-point decimal numbers
    # Fractional does the same for fractions.
        # To use either, we need to import them first.

from decimal import Decimal
from fractions import Fraction

third_fraction = Fraction(1, 3)
third_fixed = Decimal("0.333")
third_float = 1 / 3

print(third_fraction)               # 1/3
print(third_fixed)                  # 0.333
print(third_float)                  # 0.333333333333333333

third_float = float(third_fraction)
print(third_float)                  # 0.333333333333333333

third_float = float(third_fixed)
print(third_float)                  # 0.333

# The float() function turns Fraction and Decimal objects into floats.

print()
#                                                               Operators

# Python has the usual operators, with a couple of additions that may not be familiar to some developers:

print(-42)          # negative (unary),                  evaluates to -42
print(abs(-42))     # absolute value,                    evaluates to 42

# The unary (one-operand) negative operator flips the sign of whatever follows it. The abs() function is technically considered a unary operator
# The rest of the operators here are binary, meaning they accept two operands

print(40 + 2)       # addition,                          evaluates to 42
print(44 - 2)       # subtraction,                       evaluates to 42
print(21 * 2)       # multiplication,                    evaluates to 42
print(680 / 16)     # division,                          evaluates to 42.5
print(680 // 16)    # floor division (discard remainder) evaluates to 42
print(1234 % 149)   # modulo,                            evaluates to 42
print(7 ** 2)       # exponent,                          evaluates to 49
print((9 + 5) * 3)  # parentheses,                       evaluates to 42

print()
# Python offers augmented assignment operators, informally called 'compound assignment operators'
# These allow us to perform an operation with the current value of the variable as the left operand
print()

foo = 10
print(foo)

foo += 10           # value is now 20    (10 + 10)
print(foo)
foo -= 5            # value is now 15    (20 - 5)
print(foo)
foo *= 16           # value is now 240   (15 * 16)
print(foo)
foo //= 5           # value is now 48    (240 // 5)
print(foo)
foo /= 4            # value is now 12.0  (48 / 4)
print(foo)
foo **= 2           # value is now 144.0 (122.0 ** 2)
print(foo)
foo %= 51           # value is now 42.0  (144.0 % 15)
print(foo)

# If you need both floor division (//) and modulo (%) on the same operands: Python provides the divmod() function to efficiently perform the calculation
        # Example: c = divmod(a, b) is the same as c = (a // b, a % b)

# There's ALSO 'bitwise' operators, which we'll list here but we won't be using them for some time:

print(9 & 8)       # bitwise AND,                               evaluates to 8
print(9 | 8)       # bitwise OR,                                evaluates to 9
print(9 ^ 8)       # bitwise XOR,                               evaluates to 1
print(~8)          # unary bitwise ones complement (flip),      evaluates to -9
print(1 << 3)      # bitwise left shift,                        evaluates to 8
print(8 >> 3)      # bitwise right shift,                       evaluates to 1

# Python ALSO has a binary operator for matrix multiplication, @, although none of the built-in types support it.
# If you have variables that support this operator, you can use it via x @ y.
# The related augmented assignment @= also exists.

# Python provides plenty of additional functions in the math module, along with the five most common math constants: pi, tau, e, inf, and nan
import math

print(math.pi)     # PI
print(math.tau)    # TAU
print(math.e)      # Euler's number
print(math.inf)    # Infinity
print(math.nan)    # Not-a-Number

# All five constants are floats and can be directly used as such.
# Official documentation provides everything available in the math module.

infinity_1 = float('inf')
infinity_2 = math.inf
print(infinity_1 == infinity_2) # evaluates to True

# We might recall a trick from high school trigonometry;
# Where we could calculate the height of something using our distance to it and the angle from our vantage point to the top of the object:

distance_ft = 65    # the distance to the object
angle_deg = 74      # the angle to the otp of the object

# Convert from degrees to radians
angle_rad = math.radians(angle_deg)

# Calculate the height of the object
height_ft = distance_ft * math.tan(angle_rad)

# Round to one decimal place
height_ft = round(height_ft, 1)

print(height_ft) # outputs: 226.7

# We can tell by the syntax above that the first two functions (radians() & tan()) are both imported from the math module.

# round() is a built in function.
    # Fun fact about round(): it can behave in surprising ways with floats
    # Because of how floating-point numbers are stored we should consider string formatting instead.

print()
#                                                   Conditionals
#                   Conditionals are compound statements composed of [if], [elif], and [else] clauses, each made up of a header and a suite.
#                   We can have as many [elif] conditionals in Python as we want, sandwiched between [if] and (optionally) [else] statements.
command = "greet"

if command == "greet":
    print("Hello!")
elif command == "exit":
    print("Goodbye")
else:
    print("I don't understand")

print()
# Notice we don't need to wrap the conditional expressions in parentheses? We may do so if it helps clarify our code!
# If you're looking for something similar to the [switch] statement from your favorite programming language, see the "Structural Pattern Matching" below (line__)

#                                                   Comparison Operators
score = 98
high_score = 100

print(score == high_score)  # False
print(score != high_score)  # True
print(score < high_score)   # True
print(score <= high_score)  # True
print(score > high_score)   # False
print(score >= high_score)  # False

#                                               Boolean, None, and Identity Operators
spam = True
eggs = False
potatoes = None

if spam is True:                                                # True
    print("We have spam.")
if spam is not False:                                           # True
    print("I DON'T LIKE SPAM.")
if spam:                                                        # Implicitly evaluates to True (preferred)
    print("Spam, spam, spam, spam...")

if eggs is False:                                               # True
    print("We're all out of eggs.")
if eggs is not True:                                            # True
    print("No eggs, but we have spam, spam, spam, spam...")
if not eggs:                                                    # Implicitly evaluates to True (preferred)
    print("Would you like spam instead?")

if potatoes is not None:                                        # preferred False       We never reach this - potatoes is None!
    print("Yum")                                                
if potatoes is None:                                            # Implicitly evaluates to None (preferred)
    print("Yes, we have no potatoes.")

if eggs is spam:                                                # CAUTIONARY False
    print("This won't work")

# Most expressions and values in Python can be evaluated to a True or False
# This is typically done by using the value as an expression by itself - we can even pass it to the bool() function to convert it explicitly:
answer = 42

if answer:
    print("Evaluated to True")  # This runs

print(bool(answer))             # True

# When an expression will evaluate to True, it is considered 'truthy'
# When an expression will evaluate to False, it is considered 'falsey'
# None constant, values representing zero, and empty collections are all considered 'falsey' while most other values are 'truthy'


#                                                               Logical Operators
spam = True
eggs = False

if spam and eggs:                                   #          a && b    :  False
    print("I do not like green eggs and spam.")

if spam or eggs:                                    #          a || b    :  True
    print("Here's your meal.")

# if (not eggs) and spam:                             #        a !&& b   :  True
if eggs != spam:                    # The previous line's format is less readable, so for this logic the != is preferred
    print("But I DON'T LIKE SPAM!")

                                                            # Assignment Expressions
#             The Walrus Operator allows us to assign a value to a variable and use that variable in another expression at the same time.

if eggs := 7 + 5 == 12:
    print("We have one dozen eggs")
    print(eggs)


print(eggs)                                         # Reads value of eggs: True         # Recall: "Most other types evaluate to 'truthy'"

# One seldom-used piece of syntax is the Ellipsis:  ...
# When you see it come up, consult the documentation for whatever module you're using.
print()
                                                                # STRINGS #

danger = "Cuidado, lammas!"
print(danger)

danger = 'Cuidado, llamas!'
print(danger)

danger = '''Cuidado, llamas!'''
print(danger)

danger = """Cuidado, lammas!"""
print(danger)

quote = "Shout, \"Cuidado, llamas!\""
print(quote)

quote = 'Shout, "Cuidado, llamas!"'
print(quote)

question = "What do you mean, \"it's fine\"?"
print(question)

question = """What do you mean, "it's fine"?"""
print(question)

print()
# Each of the above formats are valid - though some may be decided to be more readable

parrot = """\
    This parrot is no more!
    He has ceased to be!
    He's expired
        and gone to meet his maker!
        He's a stiff!
        Bereft of life,
            he rests in peace!"""

print(parrot)

# The built-in textwrap module has some functions for working with multiline strings, 
#including tools that allow you to remove leading indentation (textwrap.dedent)
print("\nimport textwrap\n")
import textwrap

print(textwrap.dedent(parrot))

spam = ("Hello"
                "dear"
            "Wold"
                    "!!!")
print(spam)                 # outputs: "HellodearWorld!!!"
print(r"I love backslashes: \ Aren't they cool?")
print("A\nB")                                               # "A\nB" is treated as a normal escape sequence, specifically the newline character
print(r"A\nB")                                              # r"A\nB" is a raw string, so the backslash is treated as a literal character in its own right

                            # ALWAYS use raw strings for regular expression (regex) patterns
    
                                                                    # Formatted Strings
in_stock = 0
print("This cheese shop has " + str(in_stock) + " types of cheese.")#   The str() function converts the value passed to it into a string, they concatenation

# Using f-strings
in_stock = 0
print(f"This cheese shop has {in_stock} types of cheese.")#                     The f tells Python to interpret and evaluate as an expression anything 
#                                                                                               in the string that wrapped in curly braces

print()

# We can put just about any valid Python code in the curly braces - meaning we aren't just limited to variables.

# For expressions, we must use two pairs of curly braces ({{}})
answer = 42
print(f"{answer}")              # 1
print(f"{{answer}}")            # 2
print(f"{{{{answer}}}}")        # 4
print(f"{{{{{{answer}}}}}}")    # 6

# We can't use backslashes within an expression in an f-string.
# This makes it difficult to escape quotes inside expressions.

# print(f"{ord('\"')}")           # SyntaxError

# Instead, we must use triple quotes on the outside of th string

print(f"""{ord('"')}""")        # prints 34

from string import Template

s = Template("$greeting, $user!")

print(s.substitute(greeting="Hi", user="Angelo"))

s = Template("A ${thing}ify subscription costs $$$price/mo.")
print(s.substitute(thing="Code", price=19.95))

# See the Python documentation for more additional abilities contained within string templates.

# Quick note on string concatenation

greeting = "Heya"
name = "Matthew"
message = "".join((greeting, ", ", name, "!"))      # first time uncovering tuples
print(message)

print()

# In practice, f-strings are the fastest, but join() is our next-best option!

                                                                    # FUNCTIONS
print("Before creating a Joke class")
                                                # Functions are 'first-class citizens', which means they can be treated like any other object
                                                # Even so, you call them as you would in any other programming language

# We declare the function using the 'def' keyword, followed by the name of the function. Parameters are named in the parens after the name
def tell_joke(joke_type):                                           # header
    if joke_type == "funny":                                        # suite
        print("How can you tell an elephant is in your fridge?")    
        print("There're footprints in the butter!")                 
    elif joke_type == "lethal":                                     # suite
        print("Wenn ist das Nunstück git und Slotermeyer?")         
        print("Ja Beiherhund das Oder die Flipperwaldt gersput!")   
    elif joke_type == "":                                           # suite
        print("You're boo-ing me?!")                                
    else:                                                           # suite
        print("Why did the chicken cross the road?")                
        print("To get to the other side!")                          

tell_joke("funny")
tell_joke("lethal")
tell_joke("")
tell_joke("fart")

print()
# We declare a class using the class keyword, the name of the class, and a colon at the end of the header.
class Joke:                                                             # header
    def __init__(self, joke_type):
        if joke_type == "funny":                                        # suite
            self.question = "How can you tell an elephant is in your fridge?"  
            self.answer = "There're footprints in the butter!"               
        elif joke_type == "lethal":                                     # suite
            self.question = "Wenn ist das Nunstück git und Slotermeyer?"        
            self.answer = "Ja Beiherhund das Oder die Flipperwaldt gersput!"
        elif joke_type == "":                                           # suite
            self.question = "You're boo-ing me?!"
            self.answer = "You're booing me!!"                              
        else:                                                           # suite
            self.question = "Why did the chicken cross the road?"              
            self.answer = "To get to the other side!"
    
    def tell(self):
        print(self.question)
        print(self.answer)
# Functions that belong to the class are called methods and are part of the class suite. Methods must accept at least one parameter: self.
print()
print("""We created a new instance of the Joke class by passing the string "lethal" to its initializer, the __init__() from earlier.""")
print()

print("After creating a Joke class")
lethal_joke = Joke("lethal")
lethal_joke.tell()

#                                       Error Handling

#                                The 'try' compound statement

num_from_user = input("Enter a number: ")

try:
    num = int(num_from_user)
except ValueError:
    print("You didn't enter a valid number. :c")
    num = 0

print(f"Your number squared is {num**2}")

# We get a string from the user, then in the try-clause we 
#attempt to convert it to an integer with the in() function.
# This will raise a ValueError: 'if the string it's trying to convert is NOT a valid whole number...'
# If that exception type (ValueError) is raised (I enter "abc" not "5"), the except-clause handles the failure.
# In any case, the last line would always be run.

                                # There're also the finally and else clauses.. more on this later