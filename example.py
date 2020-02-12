def main():

    x = eval(input('Enter  a number betwen 0 and 1: '))
    y = eval(input('Enter a number betwen 0 and 1: '))
    c = eval(input('Enter number of iterations: '))
    line = '--'*16
    print()
    print("{0:<10} {1:^10} {2:>10}".format('Index',x,y))
    header="{0:<10} {1:^10} {2:>10}".format('Index',x,y)
    filename = open('q.txt','a+')
    file = filename.write(header+'\n')
    fileLine = filename.write(line+'\n\n')

    print(line)


    for i in range(1,c+1):
        resultX = 3.9*x*(i-x)
        resultY = 3.9*y*(i-y)
        fileOutput = "{0:<10}{1:^10.06f}{2:>10.06f}".format(i,resultX,resultY)
        filename.write(fileOutput+'\n')





        print("{0:<10}{1:^10.06f}{2:>10.06f}".format(i,resultX,resultY))


main()
