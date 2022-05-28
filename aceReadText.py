# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(story):
    # [assignment] Add your code here 
    
    #File is being read
    with open(story, 'r') as file:
        text = file.read()
        return text


			#Strip punctuations
def strip_punctuations(line):
	for character in string.punctuation:
		line = line.replace(character, ' ')
	return line
	

		#Assign file a function
def count_words(story):
    text = read_file_content("story.txt")

    # Split the line into words
    words = story.split(" ")
    wordCount = dict()
    
    for word in words:
        if word in wordCount:
            wordCount[word] += 1
        else:
            wordCount[word] = 1
    return wordCount

print(count_words(read_file_content("story.txt")))