#-------------------------------------
# file: myscript.py

def square(x):
    """square a number"""
    return x ** 2
if __name__=='__main__':
    for N in range(1, 4):
        print(N, "squared is", square(N))