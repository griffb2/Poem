import re
# Creates a dictionary with keys as words and values as definitions of words
for line in open('poem.txt'):
    #Don't include words that aren't nouns
    if "n." not in line:
        continue
    else:   
        #Starts empty bank of words
        bank = {}
        #separates words from their definitions and then gets rid of some of the extra characters
        word = line.split("n.")[0]
        word = word.replace(" ", "")
     
        definition = line.split("n.")[1]
        if len(word) > 15:
            word = ""
            definition = ""
            
        else: 
            if "[" in line:
                definition = definition.split("[")[0]
                definition = definition.replace(".", "")
                definition = definition.replace(",","")
                
                if len(word) > 1:
                    bank[word] = definition
                    
                else:
                    break

            else:
                if len(word) > 1:
                    bank[word] = definition
                else:
                    break
            
   
      
    print bank.keys()
        
        
