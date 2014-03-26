'''
#ex 1.
print "do I really have to start with 'Hello world?'"
# I want to skip to string formatting! :(
# I"m going to skip ahead...

#ex2.
print "I could have code like this." # and the comment after is ignored.
# You can also use a comment to " disable" or comment out a piece of code:
#print this will not run
print "this will run."

#ex3.
+ does addition
- does subtraction
/ divison
% modulo!! determines the reaminder 
* multiplication 
< less than
> greater than
<= less than or equal
>= greater than or equal

print "I will now count my chickens:"

print "Hens", 25 + 30 / 6
print "roosters", 100 - 25 * 3 % 4

print "now I will count the eggs:"
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6


#ex4. 
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

#ex5. 

#print "this string is as silly as {0} and {1}".format('David', 'shakrah')

my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'blue'
my_teeth = 'white'
my_hair = 'brown'

print "lets talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)

#this line is tricky, try to get it exactly righy, ok! 
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

name = 'Zed A. Shaw'
age = round(35 * 2.54) # not a lie
height = round(74 * 2.54)# inches
weight = round(180 / 2.2) # lbs
eyes = 'blue'
teeth = 'white'
hair = 'brown'

print "lets talk about %s." % name
print "He's %d cm tall." % height
print "He's %r kilos heavy." % weight
print "Actually that's not too heavy."
print "He's got %r eyes and %s hair." % (eyes, hair)

#this line is tricky, try to get it exactly righy, ok! 
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

#ex6

#variable set to a string, using formating for digits,nums
x = "there are %d kinds of people." % 10
#set variable to string
binary = "binary"
#set variable to string
do_not = "don't"
#variable set to a string, using formating for smultiple strings
y = "Those who know %s and those who %s." % (binary, do_not)
#print strings set to variables
print x
#print strings set to variables
print y
#printing string inside a string
print "I said: %r." % x
#printing string inside a string
print "I also said: '%s'." % y

#set varaible to boolean
hilarious = False
#variable set to a string, using formating for any varaible type
joke_evaluation = "Isn't that joke so funny?! %r"
#print strings set to variable and boolean
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."
#print and join two strings 
print w + e

#instances of string inside string:
line 78:2
line 84:1
line 86:1

#adding two strings joins them to be one longer string.

#ex7.
#print a string
print "Mary had a little lamb."
#print a string, with string formating
print "It's fleece was white as %s." % 'snow'
#print a string
print "And everywhere that Mary went."
#print and multiple a string"
print "." * 10 
#set variables to string
end1 = "c"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "b"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"
#prints and joins variables to create a word. comma makes next line print on this line
print end1 + end2 + end3 + end4 + end5 + end6,
#prints and joins variables to create a word.
print end7 + end8 + end9 + end10 + end11 + end12

#ex8.
formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

#ex9.
#print string
days = "Mon Tue Wed Thu Fri Sat Sun"
#print string with line breaks after each month.
months = "Jan\nFeb\nMar\nApr\nJun\nJul\nAug"

print "Here are the days: ", days
print "Here are the months: ", months
#how to comment out multiline strings
print """
There's something going on here.
With the tree double qoutes.
we'll be able to type as much as we like.
Even 4 lines if we want, or 5 or 6.
"""
#ex10.
tabby_cat = "\tI'm tabbed in."
persian_cat = "I 'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

my_name = "shakrah"
print "my \"real\" name is %s." % my_name

real_title = "wizard"
print "my job title is costumer\\%s." % real_title

my_name = "shakrah"
print "my \"real\" name is %r." % my_name

real_title = "wizard"
print "my job title is costumer\\%r." % real_title

#ex11.

print "How olds are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So you're %r old, %r tall and %r heavy." % (
    age, height, weight)
print "how much do you earn",
salary = float(raw_input())
print "how much do you pay for rent?",
rent = float(raw_input())
percent_rent = salary/rent
#print string with '%' as a character, escaping with %
print "so you pay %f%% of your income for rent." % (rent / salary * 100)
#print "so you pay {:.0%} percent of your income for rent.".format(rent / salary)	
	
    
#ex12

age = raw_input("How old are you?")
height = raw_input("How tall are you?")
weight = raw_input('How much do you weigh?')

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

#ex13
from sys import argv

script, first, second, third = argv

print "The script is called:", script
print 'Your first variable is:', first
print 'your second variable is:', second
print "Your third variable is:", third

name, age, height, weight = argv

print raw_input("your name:"), name
print raw_input("your age:"), age
print raw_input("your height:"), height
print raw_input("your weight:"), weight

print 'user-provided arguments:', argv[1:]

name, age, height, weight = argv

raw_input("your name:"), name
raw_input("your age:"), age
raw_input("your height:"), height
raw_input("your weight:"), weight

print argv

#ex14

from sys import argv

script, user_name = argv
prompt = 'you entered'
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer =  raw_input(prompt)

print """"
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)

#ex15

#imports argv module
from sys import argv
#arg v is keeping track of two variables, which we will provide when we run on the command line
script, filename = argv
#setting variable to a function open which takes argument filename
txt = open(filename)
#print with formating 
print "Here's your file %r:" % filename
#here we actually print contents of file, by calling method read
print txt.read()
#reseting our variable to open file again without hardcoding

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
#why use argv here? maybe you could make a program that would provide arguments to argv instead of interfacing with prompts in real time?

#ex16

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print " If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "opening the file..."
target = open(filename, "w")

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
#cool writing it on one line: writing the strings on multiple lines
target.write("%s \n %s \n %s" % (line1, line2, line2))


target = open(filename,"r")

f = open(filename)
print f.read()

print "And finally, we close it."
target.close()

#ex17
from sys import argv
from os.path import exists

script, from_file, to_file = argv
#printing what we plan to do later...
print "Copying from %s to %s" % (from_file, to_file)
#seting vafriables to easily call out functions
in_file = open(from_file); indata = in_file.read()
#calling in_file.read and getting data size in formating
print "The input file is %d bytes long" % len(indata)
#checks if file exists
print "Does the output file exist? %r" % exists(to_file)
#oppertunity to escape
print "Ready, hit RETURN to continue, CTRL_C to abort."
raw_input()
#open file in write mode
out_file = open(to_file, 'w')
#data cached!
out_file.write(indata)
print "alright, all done."

#data not writen to file until closed! write to file and close!
out_file.close()
in_file.close()

#ex18.
def print_two(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)
    
def print_one(arg1):
    print "arg1: %r" % arg1
    
def print_none():
    print "I got nothing."
    
print_two("Zed", "Shaw")
print_one("First!")
print_none()

#ex19
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "get a blanket.\n"
    
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "Or we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

#ex20
from sys import argv

script, input_file = argv
#create a function that when called prints whole file
def print_all(f):
    print f.read()
#create function when called returns to char index 0  
def rewind(f):
    f.seek(0)
#create function that when called reads a line at linecount and prints it    
def print_a_line(line_count, f):
    print line_count, f.readline(),
#opens our file
current_file = open(input_file)

print "First let's print the whole file:\n"
#call to print function
print_all(current_file)

print "Now let's rewind, kind of like a tape."
#call to rewind, of our file. 
rewind(current_file)

print "Let's print three lines:"
#line count starts at one
current_line = 1
print_a_line(current_line, current_file)
#incrementing line count resetting value of line count
current_line += 1
print_a_line(current_line, current_file)
#''
current_line += 1
print_a_line(current_line, current_file)


#ex21
def add(a, b):
    print "Adding %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "Subtracting %d - %d" % (a, b)
    return a - b
    
def multiply (a, b):
    print "Multiplying %d * %d" % (a, b)
    return a * b
    
def divide(a, b):
    print "dividing %d / %d" % (a, b)
    return a / b
    
print "Let's do some math with functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

print "Here is a puzzle."

what = add(age, (subtract(height, multiply(weight, divide(iq, 2)))))

print "That becomes: ", what, "can you do it by hand?"

#divide(add(a + b), c - d)= 24 + 34 / 100 - 1023

vacation_spending = 10000
spending_per_year = 48000
years_i_will_live = 62

money_needed = add(vacation_spending, multiply(spending_per_year, years_i_will_live))

print "I need to earn: %d over the years" % money_needed

#ex22 review code-done...only new ideas are argv, target, open
#ex23 read code

#ex24
print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem  = """
\tThe lovely Wind
with ;ogic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explaination
\n\t\twhere there is none.
"""
print "--------------"
print poem
print '--------------'

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates
    
start_point = 10000
beans, jars, crates = secret_formula(start_point)
    
start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)

#ex25
#create funtion that takes 'stuff' a string and slits it into smaller stings (words) when split argument is supplied (' ') in this case, and returns an array of words.
def break_words(stuff):
    words = stuff.split(' ')
    return words
#kind of sorts alphabetically ? and returns an array of sorted words
def sort_words(words):
    return sorted(words)
#prints the word at index zero and removes it from list-mutation!  
def print_first_words(words):
    word = words.pop(0)
    print word
#prints word at last index and removes from list    
def print_last_words(words):
    word = words.pop(-1)
    print word
#this one still confuses me......retuns array of new list, with items popped out    
def sort_sentence(sentence): #continue here
    words = break_words(sentence)
    return sort_words(words)
#gets words from sentence with break words, and prints first and last word   
def print_first_and_last(sentence):
    words = break_words(sentence)
    print_first_words(words)
    print_last_words(words)
#gets words from sort_sentence which is updated list and prints fisrt and last of this newer list  
def print_first_and_last_sorted(sentence):
   words = sort_sentence(sentence)
   print_first_words(words)
   print_last_words(words)


sentence = "cats love to purrrr"
words = stuff.split(' ')
 
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_words(words):
    """Prints the first word after popping it off."""
    words = break_words(words)
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    words = break_words(words)
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    sorted = sort_words(words)
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_words(words)
    print_last_words(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_words(words)
    print_last_words(words)
    
#print break_words(sentence)
#print sort_words(words)
print print_first_words(words)
#print print_last_words(words)
#print sort_sentence(sentence)
#print print_first_A


print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print "--------------"
print poem
print "--------------"

five = 10 - 2 + 3 - 5
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans \ 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates == secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)


sentence = "All good\tthings come to those who wait."

words = exercises.break_words(sentence)
sorted_words = exercises.sort_words(words)

print_first_words(words)
print_last_words(words)
print_first_words(sorted_words)
print_last_words(sorted_words)
sorted_words = exercises.sort_sentence(sentence)
print sorted_words

print_first_and_last(sentence)

print_first_and_last_sorted(sentence)

ex28.
True and True == True
False and True == False
1 == 1 and 2 == 1 == False
"test" == "test" == True
1 == 1 or 2 != 1 == True
True  and 1 == 1 == True
False and 0 != 0 == False!
True or 1 == 1 == True
"test" == "testing" == False
1 != 0 and 2 ==1 = False
"test" != "testing" == True
"test" == 1 == False
not(True and False) == True!
not (1 == 1 and 0 != 1) == False!
not (10 == 1 or 1000 == 1000) == False
not (1 != 0 or 3 == 4) == True 
not ("testing" == "testing" and "Zed" == "cool guy") = False
1 == 1 and not ("testing" == 1 or 1 == 0) == False
"chunky" == "bacon" and not (3 == 4 or 3 == 3) == False
3 == 3 and not ("testing" == "testing" or "Python" == "Fun") == False


#ex29.
people = 20
cats = 30
dogs = 15

if people < cats:
    print "Too many cats the world is doomed!"
    
if people > cats:
    print "Not many cats the world is saved!"
    
if people < dogs:
    print "The world is drooled on!"
    
if people > dogs:
    print "The world is dry!"
    
dogs += 5

if people >= dogs:
    print "People are greater than or equal to dogs."
    
if people <= dogs:
    print "People are less than or equal to dogs."
    
if people == dogs:
    print "People are dogs."
    
#ex30.
people = 30
cars = 40
buses = 15

if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    "We can't decide."
    
if buses > cars:
    print "Thats too many buses."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."
    
if people > buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then."

 
#ex31.
print "You enter a dark room with three doors. Do you go through door #1 or door #2 or #3?"

door = raw_input("> ")

if door ==  "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."
    print "3. Offer the bear a cofee"
    
    bear = raw_input("> ")
    
    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    elif bear == "3":
        print "The bear accepts your kind offer. and offers you some cake."
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear
        
elif door == "2":
    print "You stare into the endless abyss at Cthulu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothspins."
    print "3. Understanding revolvers yelling melodies."
    print "4. blind Cthulu with the bear spray you still have, then cook him, yummy!"
    
    insanity = raw_input("> ")
    
    if insanity == "1" or insanity == "2":
        print "Your  body survives by a mind of jello. Good job!"
    elif insanity == 4:
        print "Time for a nap!"
    else:
        print "The insanity rots your eyes into a pool of muck. Good job!"
        
elif door == "3":
    print "Penquins are dancing the charleston!"
    print "1. You drop your bear spray and frying pan and join in!"
    print "2. You teach them the electric slide!"
    print "3. You run out of the room back into the dark hall."
    
    dance_party = raw_input("> ")
    
    if dance_party == "1" or dance_party == "2":
        print "You are the life of the party. Good job!"
    elif dance_party == "3":
        print "You enter a dark room with three doors Again! Do you go through door #1 or door #2 or Man \t\tup and go back into #3?"
        door = raw_input("> ")
        if door ==  "1":
            print "There's a giant bear here eating a cheese cake. What do you do?"
            print "1. Take the cake."
            print "2. Scream at the bear."
            print "3. Offer the bear a cofee"
    
            bear = raw_input("> ")
    
            if bear == "1":
                print "The bear eats your face off. Good job!"
            elif bear == "2":
                print "The bear eats your legs off. Good job!"
            elif bear == "3":
                print "The bear accepts your kind offer. and offers you some cake."
            else:
                print "Well, doing %s is probably better. Bear runs away." % bear
        
        elif door == "2":
            print "You stare into the endless abyss at Cthulu's retina."
            print "1. Blueberries."
            print "2. Yellow jacket clothspins."
            print "3. Understanding revolvers yelling melodies."
            print "4. blind Cthulu with the bear spray you still have, then cook him, yummy!"
    
        insanity = raw_input("> ")
    
        if insanity == "1" or insanity == "2":
            print "Your  body survives by a mind of jello. Good job!"
        elif insanity == "4":
            print "Time for a nap!"        
        elif door == "3":
            print "Penquins are dancing the charleston!"
            print "1. You drop your bear spray and frying pan and join in!"
            print "2. You teach them the electric slide!"
            print "3. You run out of the room back into the dark hall."
    
        dance_party = raw_input("> ")
    
        if dance_party == "1" or dance_party == "2":
            print "You are the life of the party. Good job!"
        elif dance_party == "3":
            print "You enter a dark room with three doors Again! Do you go through door #1 or door #2 or Man up  \t\tand go back into #3?"
        else:
            print "The insanity rots your eyes into a pool of muck. Good job!"

else:
        print "You stumble around and fall on a knife and die. Good job!" 

#ex32.
#the_count = [1, 2, 3, 4, 5]
the_count = range(0, 6)
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for num in the_count:
    print "This number is count %d" % num
    
for fruit in fruits:
    print "A fruit of type: %s" % fruit
    
for i in change:
    print "I got  %r" % i 
    
elements = range(0, 6)
    
for i in elements:
    print "Element was: %d" % i
    
#ex.33

numbers = []
def less_than(n, j):
  i = 0
  while i < n:
      print "At the top i is %d" % i
      print "At the top j is %d" % j
      numbers.append(i)
    
      i += j
      print "Numbers now:", numbers
      print "At the bottom i is %d" % i
      print "At the bottom j is %d" % j
    
  print "The numbers: "

  for num in numbers:
     print num
     
print less_than(18, 2)

numbers = []
def less_than(n, j):
  #i = 0
  for num in range(0, n, j):
      print "At the top num is %d" % num
      numbers.append(num)
      num += 1
      
      print "Numbers now:", numbers
      print "At the bottom num is %d" % num
    
  print "The numbers: "

  for num in numbers:
      print num
     
print less_than(17, 3)


#ex34.
animals = ['bear', 'python', 'peacock', 'kangoaroo', 'whale', 'platypus']
print "The animal at 1.:"
print animals[1] #'python'
print "The animal at 1.:"
print animals[2] #'peacock'
print "The animal at 1.:"
print animals[0] #'bear'
print "The animal at 1.:"
print animals[3] #kangaroo'
print "The animal at 1.:"
print animals[4] #'whale'
print "The animal at 1.:"
print animals[2] #"peacock"
print "The animal at 1.:"
print animals[5] #'platypus'
print "The animal at 1.:"
print animals[3] #'kangaroo'
#assert animals[3] == 'kangaroo' test, will return nothing if test passes :)

#ex35.
from sys import exit

def gold_room():
    print "This room is full of gold. How much should we take?"
    
    next_ = raw_input("> Enter a number!\n")
    if type(int(next_)) == int:
        how_much = int(next_)
    else:
        dead("Man learn to type a number.")
        
    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print "There is a bear in here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False
    
    print "Enter take honey or taunt bear"
    
    while True:
        next_ = raw_input(">\n")
        
        if next_ == "take honey":
            dead("The bear looks at you the slaps your face off.")
        elif next_ == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
            print "Enter open door."
                        
        elif next_ == "taunt bear" and  bear_moved:
            dead("The bear gets pissed off and chews your legs off.")
              
        elif next_ == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."
            
def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    next_ = raw_input(">Enter flee or head\n")
    
    if "flee" in next_:
        start()
    elif "head" in next_:
        dead("Well that was tasty!")
    else:
        cthulhu_room()
#function prints specified string and exits game        
def dead(why):
    print why, "You are dead. Game over!"
    exit(0)
    
def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print"Which one do you take?"
    
    next_ = raw_input("> Enter left or right\n")
    
    if next_ == "left":
        bear_room()
    elif next_ == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")
             
start()

#ex36.

from sys import exit

def go_sunbathing():
    print "where shall I go sunbathing?."
    print \'''
    1. golden gate park
    2. union square
    3. ocean beach\'''
            
    next_ = raw_input("> Enter a number 1-3!\n")
    
    if next_ == "1" or next_ == "3":
        print "You freeze to death."
        game_over("Maybe they can unfreeze you in the future.")
    
    elif next_ == "2":
        print "A Talent agent spots you, and you fly to Hollywood that day and become rich and famous!"
        game_over("Your reality show is coming out soon!")
       
    else:
        game_over("you didn't enter a number 1-3!")
    

def practice_code():
    print "1. You practice your code for hours"
    print "2. You practice your code for ten minutes and then spend the rest of the day watching downton Abbey."

    next_ = raw_input("> Enter a number 1-2!\n")
     
    if next_ == "1":
        print "You fall asleep and dream of a brilliant app idea."
        print 'Do you build your app?'
        
        next_ = raw_input("> Enter yes or no!\n")
        if next_ == "yes":
            build_app = True
            
            if build_app:
                print "You build your app and make a million dollars."
                game_over("You buy an island where you can sunbath naked all year 'round'.")
          
        else:
            game_over("You become a programmer and live a moderately happy life without a personal jet or private island.")
        
            
    elif next_ == "2": 
        game_over("You never learn to code well, and get a job in a pizza place. You become incredibly fat and never sunbath again.")
            
                
def game_over(why):
    print why, "Game over!"
    exit(0)
    
def start():
    print "You wake up."
    print "What are you going to do today?."
    print\'''
    1. Go sunbathing.
    2. Practice your code.\'''
    
    next_ = raw_input("> Enter numbers 1-2\n")
    
    if next_ == "1":
        go_sunbathing()
        
    elif next_ == "2":
        practice_code()
          
    else:
        "You did not enter a number 1-2!"
        exit(0)#try 1?
             
start()

'''
'''
#ex37
and : False and True = False
del : del list[4]
from : import  ...  from
not : not(False)
while : while (condition): \n do something
as : excetion as 'foo'
elif : if a: ...do something \n efif b: ....do somethinhg else
global : a variable avaible on all levels
or : True or False = True
with : context manager ..with "do something..." will close file
assert : assert b == b
else : if a: ...., if b: ... else: ...do something else
if : if condition:...do something
pass: a null opperation or placeholder
yield: used return value inside generator
break : breaks the loop
except: clause catches all exceptions, use Exeception, raise exceptions but dont catch unless you can do something about it.
import : import modules or files
print : prints results or string on command line
class
exec statement or function eval an expression, exec(expr, globals)
in : for num in numbers: ...do something
raise : raise exception
continue
finally: after try except, you can clean up or do some other task
is: test for object identity, x is y..
return : tells code to run... return 'a' + 'b' \n 'ab'
def : def some_function(variable): ...does some stuff
for : for num in numbers: print num += 1
lambda : anon functions, function which takes functions, keeps it on one line
try : try:...{}[2]
True : condition is true, true or false, not 0, or neg int
False : condition is not true, true and false, false and false, 0
None : no value?
strings : "helloe world"
numbers : 1,2,3
floats : 1.678
lists : list = [4, "cat", []]
\\
\'
\"
\a:no effect??
\b: deletes char its is next to print "the names\b" : the name
\f: same as \v??
\n: new line
\r : does not print anything following \r. print "I am not sure what\r will do"  : will do sure what
\t: tab
\v: cool verticle tab
%d: formats digits, base 10
%i :
/* - not sure about defined below?
%o :octal format, base 8?
%u
%x: hex, base 16, lowercasen muns above 9
%X: hex uppercase
%e: exponent
%E :same
%f: fixed point number to precision 6
%F: same
%g : geneal format, rounds number
%G: switches to e if num gets too big
%c: converts int to char?
*/
%r : degugging mode formatter, placeholder
%s :strings
%% :escapes % "90%% of our students recieved A-"
+: add
- :subtract
* :multipy
**: pow
/ escape
// escape escape
% :modulo returns remainder
< :less than
>: greater than
<= less than or equal
>= greater than or equal
== equal value
!= not equal value
<> : another form of not equal
( ): encapsulate stuff that goes inside functiond ;variables
[ ]: list formater, or braket notation get element of dict
{ }: ecapsulates dict items
@
, 
:end of function : denotes now do somthing
.
= assings value
;
+= adds value to itself n += 1, = n + 1.
-= subtracts value from self
*=  multiplies itself by variable n *= 1 == n * 1
/=
//=
%=
**=

#ex 38.
ten_things = "Apples Oranges Crows Telephone Light Sugar"
print "Wait there's not 10 things in that list, let's fix that."
#call split method on string, splitting it with a specified char ex ' ' the space, great way to find word breaks. 
stuff = ten_things.split(' ')
more_stuff = ["Da", "Night", "Song", "Frisbee", "Corn", "Banana", "girl", "Boy"]
#while legth of items in our new list is less than 10...
while len(stuff) != 10:
# we set a variable to be the value of method pop being called on a second  list. pop removes last item from list, that value is next_one
    next_one = more_stuff.pop()
    #print our variable
    print "Adding:", next_one
    #append adds our variable next_one to our first list stuff
    stuff.append(next_one)
    #we print a string with our new len of list 
    print "There's %d items now." % len(stuff)
    
print "There we go:", stuff

print "Let's do some things with stuff."
#print the first item of list
print stuff[1]
#print last item of list
print stuff[-1]
#print varibale to be added to list
print stuff.pop()
#join transforms or list items back into a single string
print ' '.join(stuff)
#joins items selected by slice starting at index 3 and up to but not including 5. 
print '#'.join(stuff[3:5])

#ex39
#mapping of state to abbrev
states = {
    'Oregon': 'OR',
    'Florida': "FL",
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}
#map state to city
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}
#add city to state dict
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print ______________
print '_' * 10
#get and print cities of ny state
print 'NY State has:', cities['NY']
#get and print cities of OR state
print 'OR State has:', cities['OR']

print '_' * 10
#get and print abbrev or %s state
print "Michigan's abbreviation is:", states['Michigan']
print "Florida's abbreviation is:", states['Florida']

print '_' * 10
#get and print cities and states
print "Michigan has:", cities[states['Michigan']]
print "Florida has:", cities[states['Florida']]

print '_' * 10
#get and print all states in states
for states, abbrev in states.items():
    print "%s is abbreviated %s" % (states, abbrev)
    
print '_' * 10
#get and print all cities in cities
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)
    
print '_' * 10
#get and print all states in states, and cities in cities
for state, abbrev in states.items():
#to get cities -->> dict[key] returns value!
    print "%s state is abbreviated %s and has city %s" % (state, abbrev, 
    cities[abbrev])
    
print '_' * 10
#get an abbrev of state that might not be in dict...
#get- another way to get stuff from dictionsaries that might not be there
#get(key,default) where default returns what you get is value is not therre
state = states.get('Texas', None)

if not state:
    print "Sorry, no Texas."
    
#get a city with a default value
#sets long complex string to variable for easy use.
#we try to get key: 'tx', and return string for default value, cool.
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city

#ex40
#a class is an outside wrapper or name for a new object type
#has all object properties like methods
class Song(object):
#init called when you make an instance of class, an onject, with arguments self the object to be called, and any number of arguments
    def __init__(self, lyrics, platinum=False):
    #properties of the object
        self.lyrics = lyrics
        self.platinum = platinum
    #this is a method on Song objects  
    def sing_me_a_song(self):
    #what the method does. prints lyrics
        for line in self.lyrics:
            print line
#create Song object, setting argument           
happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])
#create Song object, setting argument                    
bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])
#invoking method on song object                        
happy_bday.sing_me_a_song()
#invoking method on song object 
bulls_on_parade.sing_me_a_song()
#setting variable to pass to object
bowie = ["ground control to major tom",
        "eat your protien pills and put your helmet on"]
#create Song object
major_tom = Song(bowie)
#invoking method on song object 
major_tom.sing_me_a_song()

#ex41
 python oop_test.py
class Drug(object):
	def __init__(self, crime)
> class drug has an init with param self and crime
ANSWER:  class Drug has-a __init__ that takes self and crime parameters.


class Authority(object):
	def badge(self, company, degree)
> class Authority has a function badge with args self, company and degree   
ANSWER:  class Authority has-a function named badge that takes self and company, degree parameters.


bubble.cow = 'desire'
> obj bubble of class cow has a propety desire
ANSWER:  From bubble get the cow attribute and set it to 'desire'.


balance = Degree()
>  balance 
ANSWER:  Set balance to an instance of class Degree.


comb.drum(border, aunt)
> from comb set drum attributes to border and aunt
ANSWER:  From comb get the drum function, and call it with parameters self, border, aunt.


class Brick(Drain):
> class brick has a drain param
ANSWER:  Make a class named Brick that is-a Drain.


airplane.cheese = 'attraction'
> from airplane get cheese attribute and set to atrattion
ANSWER:  From airplane get the cheese attribute and set it to 'attraction'.


class Body(object):
	def cast(self, cord)
> class body has a cast function with parameters self and cord
ANSWER:  class Body has-a function named cast that takes self and cord parameters.


class Bone(Crime):
> class Bone has a Crime param
ANSWER:  Make a class named Bone that is-a Crime.


church.addition(back)
> from church call the addition function with back as arg
ANSWER:  From church get the addition function, and call it with parameters self, back.


class Brother(object):
	def __init__(self, battle)
> class Brother is an obj and has an init function with param self and battle
ANSWER:  class Brother has-a __init__ that takes self and battle parameters.


army = Argument()
> instance of argument class set to army 
ANSWER:  Set army to an instance of class Argument.


discovery.apparel(bridge, business)
> from discovery call apparel function with params self, bridge and buisness
ANSWER:  From discovery get the apparel function, and call it with parameters self, bridge, business.


dinner.cobweb = 'crown'
> from dinner get cobweb attribute and set to 'crown'
ANSWER:  From dinner get the cobweb attribute and set it to 'crown'.


class Color(object):
	def brick(self, copper)
> class Color is-a object, has-a brick function with params self and copper
ANSWER:  class Color has-a function named brick that takes self and copper parameters.


class Cough(Duck):
> class Cough is-a Duck 
ANSWER:  Make a class named Cough that is-a Duck.


copper = Drain()
> set copper to instnace of 
ANSWER:  Set copper to an instance of class Drain.


class Advice(object):
	def __init__(self, cave)
> class Advice is-a obj, has-a init function with params self and cave
ANSWER:  class Advice has-a __init__ that takes self and cave parameters.


bell.coast = 'brake'
> from bell get coast attribute and set to 'brake'
ANSWER:  From bell get the coast attribute and set it to 'brake'.


crown.coat(answer)
> from crown get the coat function call with para, answer
ANSWER:  From crown get the coat function, and call it with parameters self, answer.


class Can(object):
	def __init__(self, beggar)
> class Can is-a obj, has-a init function that takes a self and begger parameters
ANSWER:  class Can has-a __init__ that takes self and beggar parameters.


distance = Blow()
> set distance to instance of Blow 
ANSWER:  Set distance to an instance of class Blow.


class Church(object):
	def drink(self, circle, advertisement)
> class Church is-a obj, has-a drink function which takes self, circle and advertisment as params
ANSWER:  class Church has-a function named drink that takes self and circle, advertisement parameters.


class Chain(Bubble):
> make a chain class, chain is-a bubble
ANSWER:  Make a class named Chain that is-a Bubble.


children.angle = 'crib'
> from children get the angle attribute ans ser it to ;crib'
ANSWER:  From children get the angle attribute and set it to 'crib'.


class Drug(object):
	def development(self, beam, account)
> class Drug is-a obj, has-a dev funct which tkaes self, beam ans account as params
ANSWER:  class Drug has-a function named development that takes self and beam, account parameters.


class Apple(Cattle):
> make a class apple, thast is-a Cattle
ANSWER:  Make a class named Apple that is-a Cattle.


account.chicken(bee)
> from account get the chcicken function call it with param bee
ANSWER:  From account get the chicken function, and call it with parameters self, bee.


beginner = Discussion()
> set beginner to instance of Discussion
ANSWER:  Set beginner to an instance of class Discussion.


class Dress(object):
	def __init__(self, amount)
> class dress has an init function that takes paramn self and amount
ANSWER:  class Dress has-a __init__ that takes self and amount parameters.


baseball.coal = 'base'
> from baseball get th e coal attribute and set it to 'base'
ANSWER:  From baseball get the coal attribute and set it to 'base'.


blood.birth(bait, dress)
> from blood get the birth function and call it with params self, bait and dress
ANSWER:  From blood get the birth function, and call it with parameters self, bait, dress.


class Believe(object):
	def __init__(self, beam)
> class Believe is-a obj, that has an init function that takes self and beam as params
ANSWER:  class Believe has-a __init__ that takes self and beam parameters.


chair = Beggar()
> set chair to instance of 'Beggar'
ANSWER:  Set chair to an instance of class Beggar.

> python oop_test.py english
From cause get the club attribute and set it to 'door'.
> clause.club = 'door'
ANSWER:  cause.club = 'door'


Make a class named Bear that is-a Bell.
> class Bear(Bell)
ANSWER:  class Bear(Bell):


Set desire to an instance of class Carriage.
> desire = Carriage() 
ANSWER:  desire = Carriage()


class Company has-a __init__ that takes self and condition parameters.
> class Company():
ANSWER:  class Company(object):
	def __init__(self, condition)


class Argument has-a function named believe that takes self and body, carriage parameters.
> class Argument():\n\tdef believe(body, carriage)
ANSWER:  class Argument(object):
	def believe(self, body, carriage)


From chance get the ant function, and call it with parameters self, boat, competition, balance.
> chance.ant(boat, competion, balance)
ANSWER:  chance.ant(boat, competition, balance)


Make a class named Brass that is-a Chicken.
> class brass(Chicken):
ANSWER:  class Brass(Chicken):


From cry get the coal attribute and set it to 'balloon'.
> cry.coal = 'ballon'
ANSWER:  cry.coal = 'balloon'


Set cook to an instance of class Cheese.
> cook = Cheese()
ANSWER:  cook = Cheese()


From cover get the cakes function, and call it with parameters self, doll, boat, body.
> cover.cakes(self, doll, boat, body)
ANSWER:  cover.cakes(doll, boat, body)


class Deer has-a __init__ that takes self and cap parameters.
> class Deer(object):def __init__(self, cap)
ANSWER:  class Deer(object):
	def __init__(self, cap)


class Cork has-a function named ball that takes self and distribution, cloth parameters.
> class Cork(object):
ANSWER:  class Cork(object):
	def ball(self, distribution, cloth)


Set detail to an instance of class Coat.
> detail = Coat()
ANSWER:  detail = Coat()

#ex42.

class Animal(object):
    pass
    def __init__(self, name):
        self.name = name
    def eats(self, animal):
        print "Animal: %r, eats animal: %r" % (self.name, animal.name)
        
class Dog(Animal):

    def __init__(self, name):
        self.name = name

    def eats(self, animal):
        if type(animal) != Cat:
            raise TypeError('Dogs can only eat cats')
        else:
            super(Dog, self).eats(animal)

class Cat(Animal):
    
    def __init__(self, name):
        self.name = name
    def meow(self):
        print "%r says meow" % self.name
    def eats(self, animal):
        if type(animal) != Fish:
            raise TypeError('Cats can only eat Fish')
        else:
            super(Cat, self).eats(animal)
        
class Person(object):

    def __init__(self, name, pet):
        self.name = name
        self.pet = pet
        
    def eats(self, animal):
        print "Person: %r, eats animal: %r" % (self.name, animal.name)

        
class Employee(Person):
    
    def __init__(self, name, salary, pet):
        super(Employee, self).__init__(name, pet)
    
        self.salary = salary
        
class Fish(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        self.name = name
    def eats(self, animal):
        if type(animal) != Person:
            raise TypeError('Fish can only eat people')
        else:
            super(Fish, self).eats(animal)

    
class Salmon(Fish):
    pass
    
class Halibut(Fish):
    pass
    
rover = Dog('rover')
satan = Cat('satan')
mary = Person('mary','satan')
mary.pet = satan
frank = Employee('frank', 120000, 'rover')
frank.pet = rover
flipper = Fish('flipper')
crouse = Salmon('crouse')
harry = Halibut('harry')

rover.eats(satan)
satan.eats(flipper)
crouse.eats(mary)
mary.eats(rover)

mary.pet.meow()

#why arent there init functions here?
class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
#b calls its own g function whuch returns 'B'
print a.f(), b.f()
print a.g(), b.g()


#ex43.
from sys import exit
from random import randint

class Scene(object):
    
    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)
        
class Engine(object):

    def __init__(self, scene_map):
        print "Engine __init__ has a scene_map", scene_map
        self.scene_map = scene_map
    
    def play(self):
        current_scene = self.scene_map.opening_scene()
        print "Play's first scene", current_scene
        
        while True:
            print "\n---------"
            next_scene_name = current_scene.enter()
            print "next_scene", next_scene_name
            current_scene = self.scene_map.next_scene(next_scene_name)
            print "map returns new scene", current_scene
                    
class Death(Scene):
    
    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud..if she were smarter.",
        "Such a loser.",
        "I have a small puppy that's better at this."
    ]
    
    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)
        
class CentralCorridor(Scene):
    
    def enter(self):
        print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
        print "your entire crew.  You are the last surviving member and your last"
        print "mission is to get the neutron destruct bomb from the Weapons Armory,"
        print "put it in the bridge, and blow the ship up after getting into an "
        print "escape pod."
        print "\n"
        print "You're running down the central corridor to the Weapons Armory when"
        print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
        print "flowing around his hate filled body.  He's blocking the door to the"
        print "Armory and about to pull a weapon to blast you."

        action = raw_input("enter Shoot!, dodge! or tell a joke")

        if action == "shoot!":
            print "Quick on the draw you yank out your blaster and fire it at the Gothon."
            print "His clown costume is flowing and moving around his body, which throws"
            print "off your aim.  Your laser hits his costume but misses him entirely.  This"
            print "completely ruins his brand new costume his mother bought him, which"
            print "makes him fly into an insane rage and blast you repeatedly in the face until"
            print "you are dead.  Then he eats you."
            return 'death'

        elif action == "dodge!":
            print "Like a world class boxer you dodge, weave, slip and slide right"
            print "as the Gothon's blaster cranks a laser past your head."
            print "In the middle of your artful dodge your foot slips and you"
            print "bang your head on the metal wall and pass out."
            print "You wake up shortly after only to die as the Gothon stomps on"
            print "your head and eats you."
            return 'death'

        elif action == "tell a joke":
            print "Lucky for you they made you learn Gothon insults in the academy."
            print "You tell the one Gothon joke you know:"
            print "Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr."
            print "The Gothon stops, tries not to laugh, then busts out laughing and can't move."
            print "While he's laughing you run up and shoot him square in the head"
            print "putting him down, then jump through the Weapon Armory door."
            return 'laser_weapon_armory'

        else:
            print "DOES NOT COMPUTE!"
            return 'central_corridor'
        
class LaserWeaponArmory(Scene):
    
    def enter(self):
        print "You do a dive roll into the Weapon Armory, crouch and scan the room"
        print "for more Gothons that might be hiding.  It's dead quiet, too quiet."
        print "You stand up and run to the far side of the room and find the"
        print "neutron bomb in its container.  There's a keypad lock on the box"
        print "and you need the code to get the bomb out.  If you get the code"
        print "wrong 10 times then the lock closes forever and you can't"
        print "get the bomb.  The code is 3 digits."
        code  = "%d%d%d" % (randint(1, 9), randint(1, 9), randint(1,9))
        guess = raw_input("[keypad]> ")
        guesses = 0
        
        while guess != code and guesses < 10:
            print "BZZZZEDD!"
            guesses += 1
            guess = raw_input("[keypad]> ")
            
        if guess == code:
            print "The container clicks open and the seal breaks, letting gas out."
            print "You grab the neutron bomb and run as fast as you can to the"
            print "bridge where you must place it in the right spot."
            return 'the_bridge'
        else:
            print "The lock buzzes one last time and then you hear a sickening"
            print "melting sound as the mechanism is fused together."
            print "You decide to sit there, and finally the Gothons blow up the"
            print "ship from their ship and you die."
            return 'death'

        
class TheBridge(Scene):

    def enter(self):
        print "You burst onto the Bridge with the netron destruct bomb"
        print "under your arm and surprise 5 Gothons who are trying to"
        print "take control of the ship.  Each of them has an even uglier"
        print "clown costume than the last.  They haven't pulled their"
        print "weapons out yet, as they see the active bomb under your"
        print "arm and don't want to set it off."

        action = raw_input("enter 'throw thw bomb' or 'slowly place the bomb> ")

        if action == "throw the bomb":
            print "In a panic you throw the bomb at the group of Gothons"
            print "and make a leap for the door.  Right as you drop it a"
            print "Gothon shoots you right in the back killing you."
            print "As you die you see another Gothon frantically try to disarm"
            print "the bomb. You die knowing they will probably blow up when"
            print "it goes off."
            return 'death'

        elif action == "slowly place the bomb":
            print "You point your blaster at the bomb under your arm"
            print "and the Gothons put their hands up and start to sweat."
            print "You inch backward to the door, open it, and then carefully"
            print "place the bomb on the floor, pointing your blaster at it."
            print "You then jump back through the door, punch the close button"
            print "and blast the lock so the Gothons can't get out."
            print "Now that the bomb is placed you run to the escape pod to"
            print "get off this tin can."
            return 'escape_pod'
        else:
            print "DOES NOT COMPUTE!"
            return "the_bridge"
                    
class EscapePod(Scene):
    
    def enter(Scene):
        print "You rush through the ship desperately trying to make it to"
        print "the escape pod before the whole ship explodes.  It seems like"
        print "hardly any Gothons are on the ship, so your run is clear of"
        print "interference.  You get to the chamber with the escape pods, and"
        print "now need to pick one to take.  Some of them could be damaged"
        print "but you don't have time to look.  There's 5 pods, which one"
        print "do you take?"

        good_pod = randint(1,5)
        guess = raw_input("[pod #]> ")


        if int(guess) != good_pod:
            print "You jump into pod %s and hit the eject button." % guess
            print "The pod escapes out into the void of space, then"
            print "implodes as the hull ruptures, crushing your body"
            print "into jam jelly."
            return 'death'
        else:
            print "You jump into pod %s and hit the eject button." % guess
            print "The pod easily slides out into space heading to"
            print "the planet below.  As it flies to the planet, you look"
            print "back and see your ship implode then explode like a"
            print "bright star, taking out the Gothon ship at the same"
            print "time.  You won!"

            return 'finished'
                    
class Map(object):
     scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death()
    }
    
    def __init__(self, start_scene):
        self.start_scene = start_scene
        print "start_scene in __init__", self.start_scene

    def next_scene(self, scene_name):
        print "start_scene in next_scene"
        val = Map.scenes.get(scene_name)
        print "next_scene returns", val

    def opening_scene(self):
        return self.next_scene(self.start_scene)
                
a_map = Map('central_corrodor')
a_game = Engine(a_map)
a_game.play()

'''
#ex44.
'''
class Parent(object):

    def implicit(self):
        print "PARENT implicit()"

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

class Parent(object):

    def override(self):
        print "PARENT override()"

class Child(Parent):

    def override(self):
        print "CHILD override()"

dad = Parent()
son = Child()

dad.override()
son.override()

class Parent(object):

    def altered(self):
        print "PARENT altered()"

class Child(Parent):

    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.altered()
son.altered()

class Parent(object):
#why does this class exist only so child can overwrite it? 
    def override(self):
        print "PARENT override()"
#normal attrs of class, will get passed to child
    def implicit(self):
        print "PARENT implicit()"
#use parent and child attributes in the order i specify
    def altered(self):
        print "PARENT altered()"

class Child(Parent):
#overrides parent function of same name
    def override(self):
        print "CHILD override()"
#another kind of override, that can be called before or after parent function is called by child
    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.implicit() #parent implicit
son.implicit() #parent implicict

dad.override() #parrent override
son.override() #child override

dad.altered() #parent alt
son.altered() #child, before parent alt(), parent alt(), child  aft parent alt()

class Other(object):

    def override(self):
        print "OTHER override()"

    def implicit(self):
        print "OTHER implicit()"

    def altered(self):
        print "OTHER altered()"

class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD, BEFORE OTHER altered()"
        self.other.altered()
        print "CHILD, AFTER OTHER altered()"

son = Child()

son.implicit() #other implicit
son.override() #child override 
son.altered() #child, other, child
'''

#ex45



