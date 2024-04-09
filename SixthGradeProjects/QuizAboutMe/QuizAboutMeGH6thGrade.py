print("Welcome To Quiz About Rishi!")
print("I hope you enjoy it, its not that long!")
name =  input("What is your name? ")
print("Hello " + str(name))
correct = 0
i = input("Do you want to play? Type y for yes and n for no. ")
if i.lower() == 'y' or 'n' :

	print("You entered " + i.lower())
if i.lower() == 'y' :
	print("Lets get started!")
elif i.lower() == 'n' :
	print("See you later!")
e = input("What is my favorite color? Type b for blue, o for orange, and g for green. ")
if e.lower() == 'b' :
	print("You are correct!")

elif e.lower() == 'o' or 'g ':
	print("You are wrong.")
easy = input("Whats my favorite sport? Type b for basketball, s for soccer, and f for football. ")
if easy.lower() == 'b' :
	print("You are correct!")
	correct += 1
elif easy.lower() == 's' or 'f' :
	print("You are wrong.")
bango = input("What is my favorite movie series? Type a for avengers, s for star wars, or h for harry potter. ")
if bango.lower() == 'a' :
	print("You are correct.")
	correct += 1
elif bango.lower() == 'h' or 's' :
	print("You are wrong.")
easybuckets = input("Whos my favorite youtuber? Type o for theodd1sout and type b for mrbeast. ")
if easybuckets.lower() == 'b' :
	print("You are correct!!!")
	correct += 1
elif easybuckets.lower() == 'o' :
	print("You are wrong...")
haaaa = input("What is my favorite season of the year? Type s for summer, f for fall, w for winter, and sp for spring. ")
if haaaa.lower() == 's' :
	print("You are correct!")
	correct += 1
elif haaaa.lower() == 'f' or 'w' or 'sp' :
	print("You are wrong...")
ittothe = input("What is my favorite shoe brand. u for under armour, n for nike, and p for puma. ")
if ittothe.lower() == 'u' :
	print(" You are correct! ")
	correct += 1
elif ittothe.lower() == 'n' or 'p' :
	print("You are wrong...")
sprite = input("Whats my favorite t.v show? Type n for nicky, ricky, dicky, and dawn, type h for henry danger. ")
if sprite.lower() == 'h' :
	print("You are correct!! ")
	correct += 1
elif sprite.lower() == 'n' :
	print("You are wrong...")
upthetube = input("Whats my favorite video game? Type n for nba2kmobile and nba for nba2k22. ")
if upthetube.lower() == 'nba' :
	print("You are correct!!!")
	correct += 1
elif upthetube.lower() == 'n' :
	print("You are wrong.")
beyblade = input("Whats my favorite vacation spot? Type h for hawaii, type c for cancun, and type i for india.")
if beyblade.lower() == 'c' :
	print("You are correct!!")
	correct += 1
elif beyblade.lower() == 'h' or 'i' :
	print("You are wrong....")
scientist = input("Whats your favorite weather? type r for rainy and s for sunny. ")
if scientist.lower() == 'r' or 's' :
	print("You are correct.")
	correct += 1
	print(str(correct) + " out of 9!")
