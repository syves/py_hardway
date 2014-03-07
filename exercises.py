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
'''
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
