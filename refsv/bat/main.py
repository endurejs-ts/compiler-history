import sys

def main():
    args = sys.argv
    if len(args) != 2:
        return
    
    reads(args[1])
    
def reads(fp: str):
    with open(fp, "r") as f:
        data = f.read()
        print(data)

if __name__ == "__main__":
    main()