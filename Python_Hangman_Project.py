'''
Name:Arvind Chandramouli
December 12, 2016
Hangman Game
'''

#Importing the random library to use later
import random

#EasyDict and HardDict are 2 dictionaries with different categories as keys, and each key has its own set of words
EasyDict = {}
HardDict = {}

#Just a buch of random words I decided to use.
EasyDict["animals"] = ["cow", "dog", "cat", "mouse", "goat", "bat", ]
EasyDict["colors"] = ["red", "blue", "green", "pink", "orange", "yellow", "purple"]
EasyDict["fruits and veggies"] = ["apple", "orange", "grape", "lime", "lemon", "carrot", "banana", "pear", "plum"]
EasyDict["miscellaneous"] = ["hello", "nice", "great", "old", "boat", "row", "time"]
HardDict["animals"] = ["platypus", "alligator", "dragonfly", "seahorse", "zebra"]
HardDict["colors"] = ["magenta", "aquamarine", "amethyst", "fuchsia", "azure", "sapphire", "turquoise", "goldenrod"]  
HardDict["fruits and veggies"] = ["pineapple", "avocado", "strawberry", "blueberry", "passionfruit"]
HardDict["miscellaneous"] = ["kaleidoscope", "superficial","magnanimous", "oscillatory", "euphemism", "jazz", "fuzzy", "xylophone"]


#First class of project is the Game class
class Game:
	
	def __init__(self):
		self.mainDict = {}
		self.mainDict["easy"] = EasyDict
		self.mainDict["hard"] = HardDict
		
#Sets the word based on what the user chooses as the category (c) and difficulty (d)	
	def SetWord(self, d, c):
		self.dict = self.mainDict[d]
		self.list = self.dict[c]
		
#Here is where I use a random library function to create a random number and use that index to choose the word. 
		k = random.randint(0,(len(self.list)-1))
		self.word = self.list[k]
		
	def GetWord(self):
		return self.word	
		
#Sets up the blanks that will be displayed for the game	
	def GetBlanks(self):
		self.blanks = ["_"]
		for x in range(1,len(self.word)):
			self.blanks = self.blanks+["_"]
		return self.blanks
		
#Uses the chosen random word to create a list of the letters in the word. This is important for later	
	def GetWordList(self):
		self.WordList = []
		for x in self.word:
			self.WordList = self.WordList + [x]
		return self.WordList
		
		

		
#Class player mainly deals with the stats of the user		
class Player:
	
#Takes 1 parameter from the user, which is their name
	def __init__(self, name):
		self.name = name
		self.tries = 0
		self.wins = 0
		self.loses = 0
		
#Also creates a variable for the name of the customized .txt file
		self.filename = "%s_HangmanStats.txt" %name
		
	def Win(self):
		self.wins = self.wins+1
		
	def Loss(self): 
		self.loses = self.loses+1
		
	def AddTry(self):
		self.tries = self.tries+1
		
		
#This method takes all of the data and puts it into a .txt file that the user can use later
	def PrintTextStats(self):
		data = open(self.filename, "w")
		data.write("Name: %s\n" %self.name)
		data.write("Total tries: %s\n" %self.tries)
		data.write("Total wins: %s\n" %self.wins)
		data.write("Total loses: %s\n" %self.loses)
		data.close()
		
		print "Your stats have been printed to a file called %s" %self.filename
		
		
		
	
		
#This method takes a name of a custom .txt file and opens it to read in the data and store it into the class variables
	def GetStats(self, filename):
		data = open(filename, "r")
		k = 0
		print "Here are your previous stats:"
		for x in data.readlines():
			new = x.split()
			
			if k ==0:
				self.name = new[1].strip()
				print "Name: %s" %self.name
			if k == 1:
				self.tries = int(new[2].strip())
				print "Total tries: %s" %self.tries
			if k==2:
				self.wins = int(new[2].strip())
				print "Total wins: %s" %self.wins
			if k==3:
				self.loses = int(new[2].strip())
				print "Total loses: %s" %self.loses
			k = k+1
			
				
		
		
		
		
		
		
		
def main(): 
	print ""
	print""
	input0 = raw_input("Welcome to my simple game of hangman. If you would like to play, enter 'yes' otherwise enter anything else to quit. ")
	print""
	if input0 == "yes":
		name1 = raw_input("What is your name?  ")
		print""
		print "If you have used this program before and would like to import your stats from a .txt file, enter yes."
		statsInput = raw_input("Otherwise enter anything else to continue. ")
		if statsInput == "yes":
			player1 = Player(name1)
			print ""
			filename = raw_input("Enter in the name of your stats file: ")
			print""
			
#Here is one of many instances where I use an infinite loop and a break conditional.
#I try to open the filename given by the user, and if it works, then I break the infinite loop.
#If it does not work, then I grab that error and ask the user to try again or just skip and break the loop
			while 1==1:
				try:
					player1.GetStats(filename)
					break
				except:
					print""
					filename = raw_input( "Sorry this is not a valid stats file. Please enter a valid file or enter quit to skip this.  ")
					print""
					if filename == "quit":
						break
					else:
						continue
						
		else:
			player1 = Player(name1)
					
		
		print ""
	
		while 1==1:
			Tries = 7
			Difficulty = raw_input("Type in easy for an easy word and hard for a more challenging word:  ")
			
#Using the infinite loop and break method again here 
			while 1==1:
				if Difficulty != "easy" and Difficulty != "hard":
					print""
					Difficulty = raw_input("Please enter in either easy or hard:  ")
				else:
					break
			
			print""
			print "Here are your choices for categories: "
			print''
			print "colors"
			print "animals"
			print "fruits and veggies"
			print "miscellaneous"
			print ""
	
			Category = raw_input("Choose one of these categories: ")
	
	
	
	
			Game1 = Game()
#Once again I use the infinite loop and break to make sure the user inputs are valid
			while 1==1:
				try:
					Game1.SetWord(Difficulty, Category)
					break
				except:
					print""
					Category = raw_input("Please enter in one of the valid categories: ")
	
	
	
			Word = Game1.GetWord()
			Blanks = Game1.GetBlanks()
			WordList = Game1.GetWordList()
	
	
			print""
			print "the category of your word is",Category,"and it has",len(Word),"letters."
			print""
			print "every time you guess a correct letter, those letters will show up in these blanks:"
			print ""
			
#Because strings are immutable, I have to break up the strings into a list of single characters and then rejoin them again
			print "".join(Blanks)
			print""
			print "You have 7 tries to guess. If you run out of tries, you have 1 chance to guess the word."
			print""
	
	
#Here is the main core of the whole project
#It begins with an infinite loop that be broken in multiple cases 
			while 1==1:
				k2 = 0
				input = raw_input("Enter a lowercase letter to guess or enter the word 'solve' to try to solve the word:  ")
				
#If the user at any time decides to solve before running out of tries, then the program will validate the guess and then break the loop
				if input == "solve":
					print ""
					input2 = raw_input("What is your guess?  ")
					if  input2 == Word:
						print ""
						print "Nice job, the correct word was %s." %Word
						player1.Win()
						print""
						break
					else:
						print ""
						print "Oh no, that's incorrect! the correct word was %s." %Word
						player1.Loss()
						print""
						break
				player1.AddTry()
				
#Instead, if the player decides to guess a letter, then a nested loop is created where the program will then run through the chosen random
#word and find all the places it matches ad fill out the blanks with those letters, while still in the infinite while loop.

				
				for i in WordList:
					if i == input:
						Blanks[k2] = input
					k2 = k2+1
				print ""
				print "".join(Blanks) 
				print ""
				Tries = Tries-1
				 
#There are some conditions here that can once again break this infinite while loop.
# If the player fills out the word before running out of tries, then they win and the infinite loop is broken. 
				if Blanks == WordList:
					print "Nice job, the correct word was %s." %Word
					player1.Win()
					print""
					break
					
#If the player runs out of tries before filling out the word and attempting to solve, they will be given 1 chance to guess the entire word
#After this the user either wins or loses, and the infinite loop is broken.
				elif Tries==0 and Blanks != WordList:
					print "Oh no you ran out of tries!"
					print""
					
					Guess = raw_input("You have 1 chance to solve this word. What is your guess? ")
					print""
					if Guess == Word:
						print "Nice job, the correct word was %s." %Word
						player1.Win()
						print""
							
					else:
						print "Oh no, that's incorrect! the correct word was %s." %Word
						player1.Loss()
						print""
					break
#If none of these conditionals are met The program will then subtract a try 
#print out the number of tries left, and and go back to the beginning of the loop.
				else:
					print "You have ",Tries,"tries left."
					print "" 
				
#After the inner infinite while loop is broken, the program asks if the user wants to play again.
#If yes, then the outer infinite while loop continues
			input3 = raw_input("Would you like to play again? Enter yes or no.  ")
			if input3 == "yes":
				print ""
				print""
				continue
				
#If no, then the outer infinite loop breaks, the user stats get printed to a .txt file, and the program ends there.
			else:
				print ""
				print "Okay have a good day!"
				print ""
				player1.PrintTextStats()
				print ""
				break
			
			
		
#End of main() 

if __name__ == '__main__':
	main()	
		
		
		

		
		

	