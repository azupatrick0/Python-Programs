def power(a,b):
   
    if not isinstance(a,int) and not isinstance(b,int):
        raise TypeError(" Arguments should  be integers")
    else:
         res=1
         for i in range(b): 
             res=res*a
    return res