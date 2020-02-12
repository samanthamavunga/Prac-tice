
import string
import random
def main():
    filename = open('score.txt','a+')
    abc = string.ascii_lowercase
    num = string.digits
    filename = open('score.txt','a+')
    for i in abc:
        out = i +''+':'+str(random.randrange(0,10))
        filename.write(out+'\n\n')



main()
