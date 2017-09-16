import nltk
from cleaner import *
import itertools
import pickle
import numpy as np
from init import *
#******************************************************
# # To avoid performing millions of expensive calculations we use a smaller vocabulary size for checking.
# grad_check_vocab_size = 100
# np.random.seed(10)
# model = RNN(grad_check_vocab_size, 10, bptt_truncate=1000)
# model.gradient_check([0,1,2,3], [1,2,3,4])
 
# vocabulary_size = 8000
# unknown_token = "UNKNOWN_TOKEN"
# sentence_start_token = "SENTENCE_START"
# sentence_end_token = "SENTENCE_END"

# lines = data2.split('\n')
# new_lines = []

# for line in lines:
# 	if line != '':
# 		temp = ["%s %s %s"%(sentence_start_token, line, sentence_end_token)]
# 		new_lines += temp
# 		print temp
lines = nltk.sent_tokenize(data2)

lines = ["%s %s %s"%(sentence_start_token, line, sentence_end_token) for line in lines]
print "parsed", len(lines), "lines"

# print lines

for line in lines:
	print line

tokenized_lines = [nltk.word_tokenize(line) for line in lines]
print "tokenized", len(tokenized_lines), "lines into words"
for line in tokenized_lines:
 	print line


# freq = list(Set(itertools.chain(*tokenized_lines)))
freq = nltk.FreqDist(itertools.chain(*tokenized_lines))
# print freq
print "Found %d unique words tokens." % len(freq.items())

vocab = freq.most_common(vocabulary_size-1)
index_to_word = [x[0] for x in vocab]
index_to_word.append(unknown_token)
word_to_index = dict([(w,i) for i,w in enumerate(index_to_word)])

print "Using vocabulary size %d." % vocabulary_size
# print "The least frequent word in our vocabulary is '%s' and appeared %d times." % (vocab[-1][0], vocab[-1][1])
 
for i, line in enumerate(tokenized_lines):
	tokenized_lines[i] = [word if word in word_to_index else unknown_token for word in line]

#print tokenized_lines

# print "\nExample sentence: '%s'" % lines[0]
# print "\nExample sentence after Pre-processing: '%s'" % tokenized_lines[0]

# Create the training data
X_train = np.asarray([[word_to_index[word] for word in line[:-1]] for line in tokenized_lines])
y_train = np.asarray([[word_to_index[word] for word in line[1:]] for line in tokenized_lines])

pickle.dump(X_train, open("./model_data/X_train.p",'wb'))
pickle.dump(y_train, open("./model_data/y_train.p", 'wb'))
pickle.dump(index_to_word, open("./model_data/index_to_word.p", "wb"))
pickle.dump(word_to_index, open("./model_data/word_to_index.p", "wb"))

