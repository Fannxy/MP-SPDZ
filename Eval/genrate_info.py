import numpy as np

if __name__ == '__main__':
    num = 50
    n_list = (10**np.linspace(1, 7, num)).astype("int").tolist()
    repeats = []
    
    for n in n_list:
        repeats.append(int(np.ceil(1000 / n)))
    
    n_string = "n_list=("
    for n in n_list[:-1]:
        n_string += (str(n)+" ")
    n_string += (str(n_list[-1])+")\n")
    
    repeat_string = "repeats_list=("
    for repeat in repeats[:-1]:
        repeat_string += (str(repeat)+" ")
    repeat_string += (str(repeats[-1])+")\n")
    
    
    with open("./Eval/tmp.info", "w") as f:
        f.write(n_string)
        f.write(repeat_string)