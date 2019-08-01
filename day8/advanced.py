f = dict()
input = raw_input("enter a word\n")

def wordCount(word):
    for i in word:
        if(f.has_key(i)):
            f[i]= f[i]+1
        else:
            f[i]=1
    print f   


wordCount(input)