
def lastNline(fname, N):
    with open(fname) as file:
        for line in (file.readlines()[-N:]):
            print(line, end = '')



if __name__ == '__main__':
    fname = 'file.txt'
    N = 3
    try:
        lastNline(fname, N)
    except:
        print('File Not found')