
def frequency(input):
    try:
        #print('You are in frequency Function')
        print (input)
        ss = input.split()
        
        word = sorted(set(ss))     # split words are stored and sorted as a set
        for i in word:
            print("('{0}':{1})".format(i,ss.count(i)))
    except Exception as e:
        print('error in execution')
        raise

def main():
    try:
        frequency('which is better python 2 or python 3')
    except Exception as e:
        print('error in execution')
        raise

if __name__=='__main__':
    main()