message = 'find you will pain only go you recordings security the into if'

def reverse_words(message):
    if message:
        words = message.split(" ")    
        end = len(words)-1
        for i in range((len(words)//2)):
            print i, end
            words[i],words[end] = words[end],words[i]
            end = end - 1
        return " ".join(words)
print reverse_words(message)
