def CWSF():

    fileName = input("Enter the file name :- ")

    count = 0
    file = open(fileName, 'r')
    for line in file:
        word=line.split( )
        count = count + len(word)
    print("The number of words are - ")
    print(count)

CWSF()