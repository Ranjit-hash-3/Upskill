try:
    fileName = 'sample.txt'
    file1 = open(fileName,'r')
    Lines = file1.readlines()
    count = 0
    print('Reading file content:')
    for line in Lines:
        count+=1
        print('Line {}: {}'.format(count,line.strip()))
except FileNotFoundError:
    print('Error: The file {} was not found'.format(fileName))
finally:
    try:
        file1.close()
    except NameError:
        print()


