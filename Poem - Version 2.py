class Poem(object):
    def __init__ (self, user_word="", user_number = 0, user_name = ""):
            self.user_word = user_word
            self.user_number = user_number
            self.user_name = user_name
            
    def word_keeper(self):
        bank = []
        # for each dictionary entry in the dictionary text file, if any of the words match the user word, all of the words are added to the bank
        for line in open('poem.txt'):
            if str(user_word) in line:
                line = line.split(" ")
                for word in line:
                    word = word.replace("\n","").replace("[","").replace("]","").replace(" ","").replace("(","").replace(")","").replace(".","")
                    
                    word = word.lower()
                    
                    if word == "" or word ==" " or word == "n." or word =="v." or word == "adj.":
                        continue
                    else:
                        if "xe2" in word:
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
        number = user_number
        name = user_name
        if len(other) == 0:
            print "ihateyouletscrymore"
        else:     
            for word in other:
                if number < len(other) - 1:
                    print "%s" %(other[number]),
                    number += number + (1/2 * len(user_name))
                else:
                    print "crying"
                    break
            
     
    
    
   
        
        
if __name__ == "__main__":
    ihateyou = True
    user_name = raw_input("Enter your name =>")        
    while ihateyou == True:
        user_word = raw_input("Enter a word =>")
        user_number = int(raw_input("Enter a number between 1 and 10 =>"))
        user = Poem(user_word, user_number, user_name)
      
        if user_word =="I hate you" or user_word == "i hate you" or user_word == "this sucks" or user_word == "crying" or user_word == "dogs" :
            ihateyou = False
        else:
            print "THE GOD OF" , user_word.upper(),  "HAS SPOKEN:" 
            user.word_associator(user.word_keeper())            
            ihateyou = True        