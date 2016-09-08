def increment(x):
    """Increments the string x"""
    length_of_string = len(x)
    if length_of_string == 0:
        return "a"
    bt = ord(x[-1:])
    if bt < 122:
        x = x[:-1] + chr(bt+1)
    else:
        x = increment(x[:-1]) + "a"
    return x
    
def main():
    """Displays all possible words using alphabet a-z"""
    a = "a"
    
    for i in range(10000000):
        a = increment(a)
        print a
  
if __name__ == "__main__":
    main()
