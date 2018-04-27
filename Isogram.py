def is_isogram(word):
    count=0
    if word==" ":
        return (word,False)
    elif not isinstance(word,str):
            raise TypeError("Argument should be a string")
    else:  
        for alphabet in "abcdefghijklmnopqrstuvwxyz":
            if ((word.count(alphabet))>1):
                count=count+1
        if (count>0):
            a=[word,False]
            return tuple(a)
        else:
            b=[word,True]
            return tuple(b)