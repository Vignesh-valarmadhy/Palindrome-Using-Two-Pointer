def isPalindrome(s):
    
    # the first pointer is placed at the starting of the string
    
    i  = 0
    
    #2nd pointer is placed at the ending of the string 
    
    j = len(s)-1
    
    while i < j :
        if s[i]!= s[j]:
            return False
        
        i = i+1 
        j = j-1
        
    return True


t = int(input())

for i in range (t):
    s = str(input())
    
    print(isPalindrome(s))




        
