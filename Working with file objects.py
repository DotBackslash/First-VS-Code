#Working with file objects

with open('text_file.txt', 'r') as f:
    #f_contents = f.readlines()
    #common file methods include;
    #read() -> outputs a string
    #readline() -> only returns the first line and steps to the next line once the method is called again.
    #readlines() -> outputs a list of each line
    #print(f_contents)

    '''
    for line in f:
        print(line, end='') #end='' overwrites the '\n' character at the end of hte print method by default
    '''
    '''
    f_contents = f.read(100) #tells .read() to return the first 100 characters, !!!remembers where it stops!!!
    print(f_contents)
    '''
    '''
    size_to_read = 10

    f_contents = f.read(size_to_read) 
    print(f_contents)
    print(f.tell()) #returns the current position in the file as number of characters read

    f_contents = f.read(size_to_read) 
    print(f_contents)
    print(f.tell())

    f.seek(0) #Sets current position to 0
    f_contents = f.read(size_to_read) 
    print(f_contents)
    print(f.tell())

    #while len(f_contents) > 0:
    #    print(f_contents, end='|')
    #    f_contents = f.read(size_to_read) 
    '''

    with open('text_file2.txt', 'w') as f2:

        #f2.write('This is a test of our writting capabilities!\n')
        #f2.write('This is a test of our writting capabilities as well!\n')
        
        #we are gonna make a copy of the first file into the second file.

        for line in f:
            f2.write(line)

