from typing import List

def insert(data, s: str)-> None:
    if s == "":
        return
    if len(s) == 1:
        if s in data:
            data[s][1] = True
        else:
            data[s] = [{}, True]
    if s[0] in data:
        insert(data[s[0]][0], s[1:])
    else:
        data[s[0]]= [{}, False]
        insert(data[s[0]][0], s[1:])


def count_words(data)->int:
    """
    Returns the number of words encoded in data. You may assume
    data is a valid trie.
    """
    if not data:
        return 0
    count=0
    for key in data:
        if data[key][1]==True:
            count+=1
        count+=count_words(data[key][0])        
    return count
    


def contains(data, s: str)-> bool:
    """
    Returns True if and only if s is encoded within data. You may
    assume data is a valid trie.
    """
    if s=="":
        return False
    if s[0] not in data.keys():
            return False
    if len(s)==1:
        return True
    return contains(data[s[0]][0],s[1:])


def height(data)->int:
    """
    Returns the length of longest word encoded in data. You may
    assume that data is a valid trie.
    """
    if data=={}:
        return 0
    maxheight=0
    for key in data:
        if data[key][0]=={} and data[key][1]:
            ch=1
            maxheight=max(maxheight,ch)
        else:
            ch=1+height(data[key][0])
            maxheight=max(maxheight,ch)
    return maxheight
    

def count_from_prefix(data, prefix: str)-> int:
    """
    Returns the number of words in data which starts with the string
    prefix, but is not equal to prefix. You may assume data is a valid
    trie.
    """
    if not data:
        return 0
    if prefix=="":
        return count_words(data)
    count=0
    for key in data:    
        if key==prefix[0]:
            count+=count_from_prefix(data[prefix[0]][0],prefix[1:])        
    return count
    

def get_suggestions(data, prefix:str)-> List[str]:
    """
    Returns a list of words which are encoded in data, and starts with
    prefix, but is not equal to prefix. You may assume data is a valid
    trie.
    """
    if not data:
        return []
    if prefix=="":
        return create(data,prefix)
    ends=[]
    for key in data:        
        if key==prefix[0]:
            ends += get_suggestions(data[key][0],prefix[1:])
    return add(ends,prefix[0])    


def add(end,prefix):
    return [prefix + w for w in end]

def create(data,prefix):    
    words=[]
    for key in data:
        word=prefix+key
        if data[key][1]:
            words.append(word)
        words+=create(data[key][0],word)
    return words
       


    




    

    
