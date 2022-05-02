"""Some functions pre-computed before multi-party computation.
"""
import random

def generate_random_config(k, m):
    breaks = [10*random.random() for i in range(m)]
    breaks.sort()
    
    coeffA = []
    scalerA = []
    for i in range(m):
        coeffA.append([random.random() for i in range(k)])
        scalerA.append([random.random() for i in range(k)])
    
    return breaks, coeffA, scalerA

code_templet = '''
@types.vectorize
def general_non_linear_func(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    # insert here
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res[i] = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res[i] += coeffA[i][j+1] * pre_muls[j] * scaler[i][j+1]

    comp = sfix.Array(m)
    for i in range(m):
        comp[i] = (x >= breaks[i])
    cipher_index = bb.get_last_one(comp) 

    return sfix.dot_product(cipher_index, poss_res)
'''

def generate_config(file_name, func_name, km_config):
    """Using to generate the config file for cipher-text computation.
    """
    templet = code_templet.split("# insert here")
    templet[0] = templet[0].replace("general_non_linear_func", func_name)
    config_code = "\n    breaks = " + str(km_config['breaks']) + "\n    coeffA = " + str(km_config['coeffA']) + "\n    scaler = " + str(km_config['scaler'])
    exec_code = templet[0] + config_code + templet[1]
    exec_code += "\n\n"    
    
    with open(file_name, 'a') as f:
        f.write(exec_code)
        # f.write(func_name+"_config = {\n")
        # # write breaks
        # string_breaks = "    \'breaks\': " + "["
        # for i in range(len(breaks)-1):
        #     string_breaks += str(breaks[i]) + ", "
        # string_breaks += str(breaks[-1]) + '], \n'
        # f.write(string_breaks)
        
        # # write scaler_list
        # string_scaler = "    \'scaler\': " + "[\n"
        # f.write(string_scaler)
        # for i in range(len(breaks)-1):
        #     each_line = "    ["
        #     for j in range(len(scaler[0])):
        #         each_line += str(scaler[i][j]) + ", "
        #     each_line += "], \n"
        #     f.write(each_line)
        # f.write("    ], \n")
        
        # # write coeffA
        # string_config = "    \'coeffA\': " + "[\n"
        # f.write(string_config)
        # for i in range(len(breaks)-1):
        #     each_line = "    ["
        #     for j in range(len(coeffA[0])):
        #         each_line += str(coeffA[i][j]) + ", "
        #     each_line += "], \n"
        #     f.write(each_line)
        # f.write("    ], \n")
        # f.write("}, \n\n")
        
    print("Write config for %s function SUCCESS!!"%(func_name))


if __name__ == '__main__':
    file_path = './Compiler/random_config.py'
    
    k_list = [i for i in range(3, 20, 2)]
    m_list = [i for i in range(2, 50, 2)]
    
    for k in k_list:
        for m in m_list:
            func_name = 'func_'+str(k)+'_'+str(m)
            breaks, coeffA, scalerA = generate_random_config(k, m)
            kmconfig = {
                'breaks': breaks,
                'coeffA': coeffA,
                'scaler': scalerA
            }
            generate_config(file_path, func_name, kmconfig)
            