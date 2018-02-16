
# coding: utf-8

# In[39]:


#Programme to define a user defined function for longestword
def longestWord(l):
    longest_word=''
    for n in l:
            if(len(n)>len(longest_word)):
                longest_word=n
    return(longest_word)

wordlist=input("Enter the list of words ")
listwords=wordlist.split(',')
longestWord(listwords)
        
    

