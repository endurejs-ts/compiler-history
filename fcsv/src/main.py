import sys
from src import *

def main():
    args = sys.argv
    if len(args) != 3:
        return
    
    pr = args[1]
    filename = args[2]

    if pr != "pr":
        print("invaild error")
    
    else:
        x_compile(filename, "index.js")

if __name__ == "__main__":
    main()
