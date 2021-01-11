

def ispalindromic(s):
    '''Check if a sequence is palindromic.
    A palindromic sequence reads the same both from left and right
    '''
    return all(s[i] == s[~i] for i in range(len(s)//2))


print(max(i*j 
          for i in range(100,1000) 
          for j in range(100,1000) 
          if ispalindromic(str(i*j))))
