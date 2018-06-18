types_of_people = 10 #gives value to variable types_of_people
x = f"There are {types_of_people} types of people." #f-string using variable above

binary = "binary" #sets variable binary
do_not = "don't" #sets variable do_not
y = f"Those who know {binary} and those who {do_not}." #f-string using above variables

print(x) #prints first part of the joke
print(y) #prints second part of the joke

print(f"I said: {x}") #f-string that prints the part of the joke? Dunno
print(f"I also said: '{y}'") #another f-string?

hilarious = False #sets variable hilarious with the value False
joke_evaluation = "Isn't that joke so funny?! {}" #sets variable joke_evaluation with space for value?

print(joke_evaluation.format(hilarious)) #instruction to print joke_evaluation variable with hilarious value attached

w = "This is the left side of..." #sets string for left side of string
e = "a string with a right side." #same for right side of string

print (w + e) #prints both sides of string but as variables? Nope, they're strings.
