from tools import *

def x_compile(fp: str, fpp: str):
    '''
    <vn> is <im|mut/able> (<to> <value>)?
    '''
    with open(f"../dist/{fp}", "r") as f:
        lines = f.readlines()  # 파일의 각 줄을 읽어옴

    with open(f"../dist/{fpp}", "a") as fx:  # 'a' 모드로 파일 열기
        for line in lines:
            line = line.strip()
            if isnull(line):  # 공백 줄은 건너뜀
                continue
            
            rx = convert_to_array(line)
            varin = rx[0]

            if len(rx) > 1 and isnull(rx[1]):
                if len(rx) > 2 and rx[2] == "is":
                    if len(rx) > 3 and isnull(rx[3]):
                        if len(rx) > 4:
                            if rx[4] == "mutable":
                                if len(rx) > 5 and isnull(rx[5]):
                                    if len(rx) > 6 and rx[6] == "to":
                                        if len(rx) > 7 and isnull(rx[7]):
                                            value = rx[8]
                                            fx.write(f"let {varin} = {value};\n")
                            elif rx[4] == "immutable":
                                if len(rx) > 5 and isnull(rx[5]):
                                    if len(rx) > 6 and rx[6] == "to":
                                        if len(rx) > 7 and isnull(rx[7]):
                                            value = rx[8]
                                            fx.write(f"const {varin} = {value};\n")
                            else:
                                print("invalid error")
                        else:
                            print("invalid error")
                    else:
                        print("invalid error")
                else:
                    print("invalid error")
            else:
                print("invalid error")
