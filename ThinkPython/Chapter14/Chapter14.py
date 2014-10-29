import os

def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isfile(path):
            print path
        else:
            walk(path)

def sed(pattern, replacement, fileIn, fileOut):
    try: 
        pathIn = os.path.join(os.getcwd(), fileIn)
        pathOut = os.path.join(os.getcwd(), fileOut)
        fin = open(pathIn)
        fout = open(pathOut, 'w')
        for line in fin:
            fout.write(line.replace(pattern, replacement))

        fin.close()
        fout.close()
    except:
        print 'an error occurred'

def ex_14_2():
    sed('the', 'rgw', 'ex_14_2_in.txt', 'ex_14_2_out.txt')


if __name__ == '__main__':
    #walk(os.path.abspath(os.path.join(os.getcwd(), "..")))
    ex_14_2()