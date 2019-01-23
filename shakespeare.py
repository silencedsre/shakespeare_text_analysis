import re

words_count={}
bigram_count={}
list_bigram=[]

file=open("shakespeare.txt",'r')
file_read=file.read()
list_words=re.findall('[a-z]+',file_read.lower())

for word in list_words:
    if word in words_count.keys():
        words_count[word]+=1
    else:
        words_count[word]=1

def function_bigram_count():
    for i in range(0,len(list_words)-1):
        bigram = list_words[i]+ " " +list_words[i+1]
        list_bigram.append(bigram)

    for two_words in list_bigram:
        if two_words in bigram_count.keys():
            bigram_count[two_words]+=1
        else:
            bigram_count[two_words]=1
    return bigram_count

def conditional_prob(word1, word2):
    function_bigram_count()
    two_words = word1 + " " + word2

    count_word1 = words_count[word1]
    count_word1_word2 = bigram_count[two_words]

    prob_word1 = count_word1/len(list_words)
    conditional_prob21 = count_word1_word2/count_word1

    return prob_word1, conditional_prob21


def function_sorting():
    listOfTuples1=sorted(words_count.items(), key=lambda x:x[1],reverse=True)
    for i in range(20):
        print(listOfTuples1[i])

    listOfTuples2 = sorted(words_count.items(), key=lambda x: x[1])
    for i in range(20):
        print(listOfTuples2[i])

string_of_three_words=input("enter three words:")
word1_in,word2_in,word3_in=string_of_three_words.split()

prob1, prob21= conditional_prob(word1_in,word2_in)
print("Probability for " + "'" + word1_in + "'" + " is: " + str(prob1))
print("Conditional Probability for "+ "'" + word2_in+ "/" + word1_in + "'" + " is: " + str(prob21))

prob2, prob32=conditional_prob(word2_in,word3_in)
print("Conditional Probability for "+ "'" + word3_in+ "/"+ word2_in + "'"+ " is: " + str(prob32))

print("Conditional Probability for "+ "'" + word1_in + " " + word2_in + " " + word3_in + "'" " is:" +str(prob1*prob21*prob32))

function_sorting()