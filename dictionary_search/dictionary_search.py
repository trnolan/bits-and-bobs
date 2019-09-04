import string

words = open('dictionary', 'r').read().split()

#Main function which takes in the three arguments and iterates via a BST to find the best word transition
#Function works by expanding one level down at a time over all possible letter changes until the answer is found
#This guarantees the correct answer but is slower than other possible solutions
def transformStartEndThroughDict(start, end, dictionary):
	words_tried={}
	words_tried[start]=1
	words_tried_copy=list(words_tried)
	len_Sequence=0
	ladder_bound=10
	while len_Sequence < ladder_bound:
		if wordsTriedTest(words_tried,end):
			return len_Sequence
		for word in words_tried_copy:
			next_level=alphabetLoop(''.join(word),dictionary)
			for word in next_level:
				words_tried[word]=1
		else:
			words_tried_copy=list(words_tried)
			len_Sequence+=1
	return 'No Sequence'

#Helper function to check if the end word has been reached
def wordsTriedTest(words, end):
 	for word in words.keys():
 		if word == end:
 			return True
 	return False

#Helper function to create all possible word changes
def alphabetLoop(start_letters, dictionary):
	step_away_words=[]
	alphabet=list(string.ascii_lowercase)
	for letter in alphabet:
		for letter_change in range(len(start_letters)):
			start_copy=list(start_letters)
			start_copy[letter_change]=letter
			if inDictionary(''.join(start_copy),dictionary) and ''.join(start_copy) != ''.join(start_letters):
				step_away_words.append(''.join(start_copy))
	return step_away_words


#Checks if word is in the dictionary and of correct length
def inDictionary(word, dictionary):
	correct_length_words=[]
	for w in dictionary:
		if len(w) == len(word):
			correct_length_words.append(w)
	if word in correct_length_words:
		return True
