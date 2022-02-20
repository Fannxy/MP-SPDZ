"""Some functions pre-computed before multi-party computation.
"""
import random

def generate_random_config(k, m):
    breaks = [10*random.random() for i in range(m)]
    breaks.sort()
    
    coeffA = []
    scalerA = []
    for i in range(m+1):
        coeffA.append([random.random() for i in range(k)])
        scalerA.append([random.random() for i in range(k)])
    
    return breaks, coeffA, scalerA


def generate_config(file_name, func_name, coeffA, breaks, scaler):
    """Using to generate the config file for cipher-text computation.
    """
    with open(file_name, 'a') as f:
        f.write(func_name+"_config = {\n")
    
        # write breaks
        string_breaks = "    \'breaks\': " + "["
        for i in range(len(breaks)-1):
            string_breaks += str(breaks[i]) + ", "
        string_breaks += str(breaks[-1]) + '], \n'
        f.write(string_breaks)
        
        # write scaler_list
        string_scaler = "    \'scaler\': " + "[\n"
        f.write(string_scaler)
        for i in range(len(breaks)-1):
            each_line = "    ["
            for j in range(len(scaler[0])):
                each_line += str(scaler[i][j]) + ", "
            each_line += "], \n"
            f.write(each_line)
        f.write("    ], \n")
        
        # write coeffA
        string_config = "    \'coeffA\': " + "[\n"
        f.write(string_config)
        for i in range(len(breaks)-1):
            each_line = "    ["
            for j in range(len(coeffA[0])):
                each_line += str(coeffA[i][j]) + ", "
            each_line += "], \n"
            f.write(each_line)
        f.write("    ], \n")
        f.write("}, \n\n")
        
    print("Write config for %s function SUCCESS!!"%(func_name))


if __name__ == '__main__':
    file_path = './Compiler/random_config.py'
    
    k_list = [i for i in range(3, 20, 2)]
    m_list = [i for i in range(2, 100, 15)]
    
    for k in k_list:
        for m in m_list:
            func_name = 'func_'+str(k)+'_'+str(m)
            breaks, coeffA, scalerA = generate_random_config(k, m)
            generate_config(file_path, func_name, coeffA, breaks, scalerA)
            