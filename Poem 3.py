import random
import unicodedata


class Poem(object):
    def __init__ (self, user_word=""):
            self.user_word = user_word

            
    def word_keeper(self):
        bank = []
        # for each dictionary entry in the dictionary text file, if any of the words match the user word, all of the words are added to the bank
        for line in open('poem.txt'):
            line.decode('utf-8').strip()
            if str(user_word) in line:
                line = line.split(" ")
                for word in line:
                    word = word.replace("\n","").replace("[","").replace("]","").replace(" ","").replace("(","").replace(")","").replace(".","").replace(";","").replace(":","").replace(",","").replace("*","")
                    
                    word = word.lower()
                    
                    if word == "" or word ==" " or word == "n." or word =="v." or word == "adj.":
                        continue
                    else:
                        if "xe2" in word:
                            continue
                        elif len(word) < 2:
                            continue
                        else:
                            bank.append(word)
                if len(bank) == 0:
                    word = "ihateyouletscrymore"
                    cat = 0
                    if cat < 1:
                        bank.append(word)
                        cat +=1
                    else:
                        continue                
                
                else: 
                

                    continue
        return bank
            #Starts empty bank of words
            #bank = {}
            #separates words from their definitions and then gets rid of some of the extra characters
            
    def word_associator(self,other):
        wordnumber = 0
        wordnumlist = []
        sentence_length = random.uniform(4,15)
        
        if len(other) == 0:
            print "ihateyouletscrymore"
        else:   
            for i in range(len(other)):
                if wordnumlist < range(len(other)):
                    wordnumlist.append(i)
                    
            low = min(wordnumlist)
            high = max(wordnumlist)
            
            counter = 0
            
            while counter < sentence_length:
                print other[int(random.uniform(low, high))],
                counter += 1
            print "crying"
           
         
            
                
                    
                    
                    
           
            
     
    
    
   
        
        
if __name__ == "__main__":
    ihateyou = True
    while ihateyou == True:
        user_word = raw_input("\nEnter a word =>")
        user = Poem(user_word)
        if user_word =="I hate you" or user_word == "i hate you" or user_word == "this sucks" or user_word == "crying" or user_word == "dogs" :
            ihateyou = False
        else:
            print "THE GOD OF" , user_word.upper(),  "HAS SPOKEN: \n"
            user.word_associator(user.word_keeper())
                       
            ihateyou = True        
            
            
            