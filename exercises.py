#ex 1.
print "do I really have to start with 'Hello world?'"
# I want to skip to string formatting! :(
# I"m going to skip ahead...
'''hey what about this thingy?'''

#ex2.
'''+ does addition
- does subtraction
/ divison
% modulo!! determines the reaminder 
* multiplication 
< less than
> greater than
<= less than or equal
>= greater than or equal'''

print "I will now count my chickens:"

print "Hens", 25 + 30 / 6
print "roosters", 100 - 25 * 3 % 4

print "now I will count the eggs:"
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6


#ex3. skip

#ex4. skip

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

'''instances of string inside string:
line 78:2
line 84:1
line 86:1'''

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
'''
print "How olds are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()
'''

print "So you're %r old, %r tall and %r heavy." % (
    age, height, weight)
print "how much do you earn",
salary = int(raw_input())
print "how much do you pay for rent?",
rent = int(raw_input())
percent_rent = salary/rent
print "so you pay %d percent of your income for rent." % percent_rent
    
    
#ex12