def longest_string(strr):
   
    splittedString=(strr.split( ))
    lengthOfSplittedString=len(splittedString)
    count=[]
    for k in range(lengthOfSplittedString+1):
          count.append(k)

    for i in range(len(splittedString)):
        count[i+1]=len(splittedString[i])
        if count[i+1] >count[i]:
            longestWord=splittedString[i]
    return longestWord