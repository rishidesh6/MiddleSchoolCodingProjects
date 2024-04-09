import random

class wordle:
	print("YOU HAVE SIX GUESSES IN TOTAL!!")
	print("When you type your first word, these are the keys: ")
	print("   g means the letter is in the right place!")
	print("   y means the letter is in the word but not the right place")
	print("   b means the letter is not in the word...")
	print("IMPORTANT: NO DUPLICATE LETTERS, OR YOU LOSE A GUESS :)")
	wordList = ["fling","tubes","champ","pedal","round","slump","fruit","snack","flout","month","stare","grace","egypt","lunch","whirl","cargo","shack","stump","grant","spent","swept","brown","final","great","grape","lunar",	"solar","outer","rinse","drink","feast","short","pants","wharf","found","jumpy","shark"]
	choice = random.choice(wordList)
	choiceList = list(choice)
	#print(choiceList)
	choiceMap = {}
	for i in range(len(choiceList)):
		ch = choiceList[i]
		choiceMap[ch] = i

	#print(choiceMap)

	def play_game(self):
	  	result = False
	  	
	  	guess1 = input("Type a five letter word!!  ")
	  	guess1List = list(guess1)
	  	isInputOkay = False
	  
	  	while (isInputOkay == False):
	  		if len(guess1List) != 5:
	  			print("Please Type A Five Letter Word")
	  			guess1= input("Type a five letter word!!! ")
	  			guess1List = list(guess1)
	  		else:
	  			isInputOkay = True   	
	  		
	  	guess1Map = {}
	  	for z in range(len(guess1List)):
	  		g1 = guess1List[z]
	  		if g1 in guess1Map.keys():
	  			print("No Duplicate Letters, So You Lose A Guess, Sorry :( ")
	  			return
	  		guess1Map[g1] = z
	  	
	  	#print(guess1Map)
	  	
	  	outputVal = ""
	  	for k, v in guess1Map.items():
	  		val = self.choiceMap.get(k)
	  		if val == None:
	  			#print("b")
	  			outputVal = outputVal + "b"
	  		elif val == v:
	  			#print("g")
	  			outputVal = outputVal + "g"
	  		else:
	  			#print("y")
	  			outputVal = outputVal + "y"
	  	print("\n\n")
	  	print("\t" + guess1)
	  	print("\t" + outputVal)
	  	print("\n\n")
	  	if outputVal == "ggggg":
	  		result = True
	  	else:
	  		result = False
	  	return result
	  	
game = wordle()
e = False
for i in range (0,6):
	print ("Guess"+ str(i+1))
	e = game.play_game()
	if e == True:
		print("You Won!!!")
		break
if e ==	 False:
	print("That's Sad!! You LOSE")	
	print("\n\n")
	print("The word was actually... "+ game.choice)
