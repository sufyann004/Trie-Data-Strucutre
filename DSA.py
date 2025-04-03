#Note: This code is a Trie data structure implementation in Python. It allows for inserting words, searching for words based on prefixes, blocking certain words, and unblocking them. The code also includes a console interface for user interaction.
#*** This code is maintaing a "list" also alongside the Trie DS. You may remove the lst as per your convenience.***
BlockList=[]



dictt={}

def insert_word(dictt, i): #Function to insert a new word into the trie strucuture
    if i not in lst:  #Checking if the word already exists in the list (list contains all the words that are in the strucuture) TC: O(l)
        lst.append(i) #Appending into the list 
    elif i in BlockList: #TC: O(m)
        return
    root=dictt #Giving the dictt(trie strucuture) another name for further use
    for j in i: #Looping over each alphabet in the word(i) TC: O(n)
        if j in root: #Checking if that alphabet exists
            root = root[j] #If it exists then the program starts accessing it's value and makes it the key
        else:
            root[j] = {} #If it doesn't exist then a new key is made with its value being an empty dictionaru
            root = root[j] #Accessing the value and making its value the new key for furhter use.
    root['end'] = True #Once the word ends, the last letter has its value a dictionary which has a key "end" and value=True

#O(l+m+n) or O(n)

def TrieStrucuture(lst): #Defining the Trie strucuture which has nested dictionaries
    dictt = {} #Initialising a dictionary
    for i in lst: #Taking words from the list and putting them into the strucuture TC:O(n)
        insert_word(dictt, i) #Calling the function that inserts word into the strucutre
    return dictt #Returning the final strucuture

#Worst case: O(n*(l+m+n) =  O(n*n)

def blockword(dictt,word,lst): #Function to block a word so it doesn't outputs
    if word not in lst: #Checking if the word exists TC: O(m)
         insert_word(trie,word)
    root = dictt
    s='' #Initialising an empty string
    for i in word:
        if i in root:
            s+=i #Appending each alphabet to string O(1)
            root = root[i] #Value becomes the key for further use
        if 'end' in root and s==word: #end that marks a word. s==word means that if s formed is equal to word since there would be many end vertices in the trie strucuture.
                root['end'] = False #Changing the value of stopping case, end, to False

    return word + " blocked"

#   O(m)

def search(dictt, prefix, output): #Helper Function to search for each available word based on the prefix entered
    if 'end' in dictt and dictt['end']==True: #Base case to check if the end node is found. If the end node has a value "True" then only the word is appended to output list. If the value of "end" is "False" then this means that the word is blocked.
        output.append(prefix) #Appending the word made based on the prefix to the output list
    for x, y in dictt.items(): #Looping over the key and value of an alphabet 
        if x != 'end': #Checking base case again i.e the key isn't "end" which means that a word is completed
            search(y, prefix + x, output) #Recursively calling the function

# O(L)..

def autocomplete(dictt, prefix): #Function that basically autocompletes
    output = [] #Intializing an output list
    root = dictt #Giving the dictt/trie another name (Note: root points towards dictt)
    for i in prefix: #Loop that checks if the word based on the prefix is present. It also filters the strucutre so the search function takes the filtered structure pertaining to the prefix. 
        if i in root:  #TC:O(P) for this loop
            root = root[i]
        else:
            return "No words present"
    search(root, prefix, output) #Calling search function after checking if the prefix is present in the strucutre and providing it with the filtered strucuture
    return output 

# O(P+L)..

#You can decomment the below code and comment the list below to use 91K nouns file for console

# Open the file in read mode
# with open('91K nouns.txt', 'r') as file:
#     # Create an empty list to store the lines
#     lst = []

#     # Iterate over the lines of the file
#     for line in file:
#         # Remove the newline character at the end of the line
#         line = line.strip()




# --------Console----------
# lst = ["apple",  "app", "ape","ali", "banana", "bat", "ball","Dr Salman","dolby","cold","colder","Coldd"]
lst=['trie','trick','try','trip']
output2=[]
trie = TrieStrucuture(lst)

user_input = input("Press Enter to continue...")==''
if user_input==True:
  while True:
    task = int(input("Enter: \n 1 to insert a new word\n 2 to search for a word \n 3 to print the collection of words \n 4 to print the Trie Structure \n 5 to block a word \n 6 to view Block List \n 7 to unblock a word \n 8 to exit \n Enter the option:"))
    if task==1: #Inserting a new word
        Word=input("Enter the word: ") #Taking input
        insert_word(trie,Word) #Insert function called
        print("Word Inserted!")
    elif task==2: #Searching for words using prefix
        prefix=input("Enter the initials/prefix: ")
        output=(autocomplete(trie, prefix)) #Calling autocomplete function for output
        print(output)
        for i in prefix: #Catering for lower/upper case for initals. Another list is output through this.
            if i==i.lower():
                s=i.upper()
                Newprefix=s+prefix[1:len(prefix)] #New Prefix with uppercase initial
                output2=(autocomplete(trie,Newprefix))
                if len(output2)>0 and output2!="No words present":
                    print(output2)
                break
            else:
                s=i.lower()
                Newprefix=s+prefix[1:len(prefix)] #New Prefix with lowercase initial
                output2=(autocomplete(trie,Newprefix))
                if len(output2)>0 and output2!="No words present":
                    print(output2)
                break
    elif task==3: #Words
        print(lst)
    elif task==4: #Trie Structure
        print(trie)
    elif task==5: #Blocking a word
        BlockWord=input("Enter the word to be blocked: ") #Taking input
        print(blockword(trie,BlockWord,lst)) #Calling blockword function
        BlockList.append(BlockWord) #Appending the word to be blocked in a blocklist
        if BlockWord[0].isupper(): #Catering for upper/lowercase initial of word
            NewString=BlockWord[0].lower()+BlockWord[1:]
            BlockList.append(NewString)
            blockword(trie,NewString,lst)
        else:
            NewString=BlockWord[0].upper()+BlockWord[1:]
            BlockList.append(NewString)
            blockword(trie,NewString,lst)
            
    elif task==6:
        print(BlockList)
    elif task==7:
        UnBlockWord=input("Enter the word to be unblocked: ")
        if UnBlockWord in BlockList:
            BlockList.remove(UnBlockWord)
            insert_word(trie,UnBlockWord)
            if UnBlockWord[0].isupper():
                NewStringg=UnBlockWord[0].lower()+BlockWord[1:]
                BlockList.remove(NewStringg)
                
            else:
                NewStringg=UnBlockWord[0].upper()+BlockWord[1:]
                BlockList.remove(NewStringg)
                
        else:
            print("Word is not blocked")
            
    elif task==8: #Exiting
        print("Bye \n Terminating Console...")
        break
    else:
        print("Enter a valid input")





