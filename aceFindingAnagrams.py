# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def main():

	print('Hello! I can tell you if two words are anagrams.')



	word = input('First word: ')
	print('and')
	anagram = input('Second word: ')

	
	def find_anagram(word, anagram):
    # [assignment] Add your code here
    	
		if len(word) != len(anagram):
			print('Unequal length!')
			return False
		return sorted(word.lower()) == sorted(anagram.lower())
    
	print(find_anagram(word, anagram))

	Repeat = input ('Would you like to find more anagrams? (y/n)')
	
	if Repeat == 'y':
		 main ()
	else: 
		print('Have a nice day!')
    
main()