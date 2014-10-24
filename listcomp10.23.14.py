
sentence = 'the quick brouwn fox jumped over the lazy dog'
words = sentence.split()
word_lengths = []
for word in words:
	if word != 'the':
		word_lengths.append(len(word))

## same text with list comp- 

sentence = 'the quick brown fox jumps over the lazy dog'

words = sentence.split()
word_lenghts = [len(word) for word in words if word != 'the']