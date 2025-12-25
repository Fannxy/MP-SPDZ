from Compiler import types
from Compiler.types import floatingpoint, sfix

@types.vectorize
def neuron000(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-4.199999809265137, -1.0499999523162842, 0.0, 2.0999999046325684]
    coeffA = [[-23188807.459396254, -96280414.24036087, -163558858.04510197, -147794379.681152, -78517091.56747204, -25385803.814801957, -4920589.693554168, -526295.5137635162, -23904.56531927995], [-110647.1863949596, -15571.50822185905, 504506.06569361733, 619264.2972007997, 0.0, 0.0, 0.0, 0.0, 0.0], [-110647.1863949596, -2597.41535408069, 3581.2624393358, -1666.35237233788, 0.0, 0.0, 0.0, 0.0, 0.0], [-93829790.90120853, 204134863.8587886, -180858933.0396633, 81819019.10843106, -18531373.161873896, 1131660.256783248, 368107.3985330948, -79417.85478918302, 4778.4877994408]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[i][j+1]))
            poss_res[i] += tmp.mul_no_reduce(x.coerce(scaler[i][j+1]))
        poss_res[i].reduce_after_mul()
        poss_res[i] += poss_res0

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    return sfix.dot_product(cipher_index, poss_res)

@types.vectorize
def neuron001(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-4.199999809265137, -2.0999999046325684, -1.0499999523162842, 0.0, 2.0999999046325684]
    coeffA = [[-11089949.579285152, -26770639.91464838, -28074452.931954943, -16772075.754535373, -6245193.310224831, -1483781.1834989379, -219601.9093357368, -18507.05450148137, -679.87695458827], [-3515527.9821557063, -18466755.19373563, -42748131.41274588, -53265591.68068622, -39014601.69755887, -17400132.9153524, -4663979.417598874, -692268.6782172575, -43781.73830905957], [-146027.13090727016, -32421.09524962616, -351807.0556804968, -302677.49648315756, 0.0, 0.0, 0.0, 0.0, 0.0], [-146027.13090727016, -982.29935208067, 4153.18320052018, -2221.77283853852, 0.0, 0.0, 0.0, 0.0, 0.0], [221424754.47957984, -547706817.8564466, 576887178.6618493, -337739696.4568784, 120100378.6832153, -26534985.81345189, 3549281.3197389133, -261659.70168625852, 8076.24802751836]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[i][j+1]))
            poss_res[i] += tmp.mul_no_reduce(x.coerce(scaler[i][j+1]))
        poss_res[i].reduce_after_mul()
        poss_res[i] += poss_res0

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    return sfix.dot_product(cipher_index, poss_res)

@types.vectorize
def neuron002(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-4.199999809265137, -1.0499999523162842, 0.0]
    coeffA = [[-15480057.317280443, -61699199.946889356, -101591037.00356193, -89810676.70866843, -46969698.04151314, -15010025.33757333, -2883515.4009866603, -306246.85821158794, -13831.02537354863], [-253870.30786233884, 79936.20703114326, 889297.2594345903, 660163.6548753795, 0.0, 0.0, 0.0, 0.0, 0.0], [-253870.30786233884, -8196.05438330481, 12636.59401417006, -4532.95550996447, 0.0, 0.0, 0.0, 0.0, 0.0]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[i][j+1]))
            poss_res[i] += tmp.mul_no_reduce(x.coerce(scaler[i][j+1]))
        poss_res[i].reduce_after_mul()
        poss_res[i] += poss_res0

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    return sfix.dot_product(cipher_index, poss_res)

@types.vectorize
def neuron003(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-4.199999809265137, -1.0499999523162842, 0.0, 2.0999999046325684]
    coeffA = [[-24050353.082308643, -99371051.6279319, -167565125.9177244, -150489518.95167705, -79574242.81004655, -25635518.558895968, -4955245.47104712, -528850.9421863173, -23979.02375301346], [-122032.89419763348, -41334.98451482164, 753111.4430769571, 802659.964371384, 0.0, 0.0, 0.0, 0.0, 0.0], [-122032.89419763348, -2945.96975485306, 5658.76211117981, -3275.99125453358, 0.0, 0.0, 0.0, 0.0, 0.0], [87537707.73921925, -256875734.32312325, 320626631.78450096, -223087736.05737165, 94870155.16320291, -25315599.891738754, 4148860.928064205, -382528.45696395694, 15216.36921013885]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[i][j+1]))
            poss_res[i] += tmp.mul_no_reduce(x.coerce(scaler[i][j+1]))
        poss_res[i].reduce_after_mul()
        poss_res[i] += poss_res0

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    return sfix.dot_product(cipher_index, poss_res)

@types.vectorize
def neuron004(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-4.199999809265137]
    coeffA = [-1.42242803933, -0.88832236242, -0.07862504038, 0.0112844342, 0.0, 0.0, 0.0, 0.0, 0.0]
    scaler = [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0]
    
    m = 1
    k = len(coeffA)
    degree = k-1
    
    m = 1
    k = len(coeffA)
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for j in range(degree):
        tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[j+1]))
        poss_res[0] += tmp.mul_no_reduce(x.coerce(scaler[j+1]))
    poss_res[0].reduce_after_mul()
    poss_res[0] += coeffA[0] * scaler[0]

    return poss_res[0]

@types.vectorize
def neuron005(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-4.199999809265137, -1.0499999523162842, -0.26249998807907104, 0.5249999761581421, 2.0999999046325684, 3.1499998569488525]
    coeffA = [[-6102039.357022393, -26279715.651505522, -45638863.81145642, -41824857.82746805, -22431175.44156701, -7300870.9140548855, -1422079.310351828, -152666.9485577246, -6954.22913958656], [88662.14921344788, 55054.73832440913, 333379.33393939317, 1413312.658088999, 3370759.4856993137, 5372249.872429778, 4605243.233920503, 1894142.7707839, 294193.14804697945], [85955.82434225417, 8023.01399147609, -20246.50470528965, 9777.30149458928, 0.0, 0.0, 0.0, 0.0, 0.0], [99643.8384412322, -178637.5678898421, 953172.0638700916, -2600950.829141304, 3954579.578806458, -3461892.1823820225, 1726282.881657871, -453856.56783457287, 48658.22392418844], [-224454031.7781045, 679395128.082199, -885544702.2574319, 647954606.9243456, -290428998.8945199, 81476397.63847871, -13939823.172428504, 1326212.4786505077, -53502.07727159961], [-1448008297.5377295, 3147028394.9883738, -2975979305.3763595, 1600538739.4929557, -535804221.09121853, 114385277.037907, -15213855.070213469, 1153043.7308637092, -38135.68838459093]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[i][j+1]))
            poss_res[i] += tmp.mul_no_reduce(x.coerce(scaler[i][j+1]))
        poss_res[i].reduce_after_mul()
        poss_res[i] += poss_res0

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    return sfix.dot_product(cipher_index, poss_res)

@types.vectorize
def neuron006(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-4.199999809265137, -1.0499999523162842, -0.13124999403953552, 0.0, 0.5249999761581421, 2.0999999046325684]
    coeffA = [[65491748.77912165, 273104986.26730084, 447863230.80862325, 390560883.62306243, 201502153.55616093, 63667466.72776115, 12121932.617331738, 1278556.6042096284, 57438.51224176726], [179765.60739446245, 3703970.6089800852, -2396735.2691597883, -6558868.423585217, -14792074.18355881, -32710306.186628245, -29383242.44916916, -10152784.37866571, -907431.9676291747], [183842.9566383375, 3805386.703387181, -1411879.811460717, -1697619.610545529, 0.0, 0.0, 0.0, 0.0, 0.0], [183842.95663833723, 3824804.7894274658, -1606322.480338636, 131802.00627522453, 0.0, 0.0, 0.0, 0.0, 0.0], [117000.40120730548, 4338872.646308707, -3153398.340069473, 2443830.449346326, -1897022.6428877357, 937539.1653771683, -217037.09345101743, 4946.41567764562, 4278.56240070089], [290395906.99722683, -804581704.8063139, 966205088.9110935, -649641978.5231239, 267568089.5965792, -69190308.7649931, 10989003.061289508, -981912.6365931373, 37859.3145276611]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[i][j+1]))
            poss_res[i] += tmp.mul_no_reduce(x.coerce(scaler[i][j+1]))
        poss_res[i].reduce_after_mul()
        poss_res[i] += poss_res0

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    return sfix.dot_product(cipher_index, poss_res)

@types.vectorize
def neuron007(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-4.199999809265137, -3.1499998569488525, -2.0999999046325684, -1.0499999523162842, -0.5249999761581421, 2.0999999046325684]
    coeffA = [[41211223.4181133, 86120662.1097358, 78822651.78266566, 41215711.194611646, 13463031.506959492, 2813048.1232361337, 367172.823747689, 27372.18698303316, 892.30160547914], [-110569997.41282177, -297087130.5386518, -331246585.1906696, -199700444.67227632, -70176095.97277704, -14171662.793607412, -1434560.2926319202, -32570.18919267056, 3620.3626244118], [-36131168.46981951, -203674522.46703732, -494319008.04082114, -664918172.7307373, -538028476.0120769, -268623607.6883812, -81239256.5660189, -13684641.09336416, -987998.2419036753], [-288976.9456462841, -923874.9329902723, -5586531.731800287, -17969922.277690973, -37108011.25400197, -50546406.15482131, -39692665.11056658, -16012464.846193764, -2581298.635196397], [-218874.64071687104, -2276.4896802711, 3664.88389922951, -1136.35914823106, 0.0, 0.0, 0.0, 0.0, 0.0], [204602964.19006073, -457868789.7842725, 421747133.92222846, -204071732.1855505, 53737088.59772467, -6597763.615809183, -40586.69232763836, 95714.14673585646, -7075.13006791448]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[i][j+1]))
            poss_res[i] += tmp.mul_no_reduce(x.coerce(scaler[i][j+1]))
        poss_res[i].reduce_after_mul()
        poss_res[i] += poss_res0

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    return sfix.dot_product(cipher_index, poss_res)

@types.vectorize
def neuron008(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-4.199999809265137, -1.0499999523162842, -0.26249998807907104, 0.0, 0.5249999761581421, 2.0999999046325684, 3.1499998569488525]
    coeffA = [[-24942404.456196163, -105358128.38273388, -180219779.0520737, -163212818.40562838, -86745041.86369334, -28039061.72037972, -5432277.519830068, -580715.3830948075, -26362.7249649455], [245947.7759051035, 432028.408578763, 1683870.902053077, 4721184.884831987, 11665849.45900998, 20477720.710822195, 18351490.924153674, 7701184.598417381, 1212321.572194541], [235791.15133715057, 262390.05793117714, 525446.7354918454, 260369.51855638815, 0.0, 0.0, 0.0, 0.0, 0.0], [235791.15133715048, 262390.89638243825, 380154.0489091694, -639154.3559115992, 0.0, 0.0, 0.0, 0.0, 0.0], [367520.5083085093, -1191495.5062891734, 6941194.476105039, -16111439.937271278, 20357689.927355908, -15268894.539347608, 6752358.277964297, -1623188.1877674544, 163514.19003604108], [425159261.0585726, -1199254953.1296694, 1441470231.8237085, -956789382.130594, 379499859.0372358, -90469730.9854575, 12210969.47776053, -775713.1939984944, 11041.64568611586], [2420096522.346004, -5227493495.837661, 4917678283.644761, -2632979709.5840335, 878012234.2676986, -186807417.07191324, 24772699.855596725, -1872586.3477153452, 61790.05262529569]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[i][j+1]))
            poss_res[i] += tmp.mul_no_reduce(x.coerce(scaler[i][j+1]))
        poss_res[i].reduce_after_mul()
        poss_res[i] += poss_res0

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    return sfix.dot_product(cipher_index, poss_res)

@types.vectorize
def neuron010(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-4.199999809265137, -2.0999999046325684, -1.0499999523162842, 0.0, 2.0999999046325684, 3.1499998569488525]
    coeffA = [[-30593430.67189432, -82192918.3772568, -94583704.22051126, -61120852.01300547, -24328151.905409146, -6120354.059481664, -951829.0414845808, -83761.91935457352, -3196.35133676855], [-10958851.498031018, -61150775.03332229, -145317194.89693454, -188430882.5618743, -146033308.23690176, -69760546.50096028, -20210780.450527407, -3267602.2086854293, -226864.0827891906], [6723.69009219181, -43147.18452329251, -846533.2151639744, -655492.4942714892, 0.0, 0.0, 0.0, 0.0, 0.0], [6723.69009219181, 3277.89091511078, -4653.10169219615, 2181.31293652822, 0.0, 0.0, 0.0, 0.0, 0.0], [67878435.72330122, -227074921.2027577, 326680834.3667665, -263664018.94996163, 130519589.46246754, -40594371.39115537, 7755925.300307718, -833581.2881791512, 38651.30812062921], [479818977.8095745, -1047498520.2244436, 994350881.3345737, -536508741.5562806, 180103848.44326654, -38542015.12602871, 5137119.157827701, -390060.92765572725, 12922.06780721118]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[i][j+1]))
            poss_res[i] += tmp.mul_no_reduce(x.coerce(scaler[i][j+1]))
        poss_res[i].reduce_after_mul()
        poss_res[i] += poss_res0

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    return sfix.dot_product(cipher_index, poss_res)

@types.vectorize
def neuron011(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-4.199999809265137, -1.0499999523162842, -0.13124999403953552, 2.0999999046325684]
    coeffA = [[-33944018.581134506, -140678899.9399745, -236992819.34522462, -212361039.9462084, -112019995.09183112, -36008911.485254176, -6947055.347174194, -740208.9739784222, -33515.12534920918], [-53772.27265615037, -87299.89393345537, 999409.3261475966, 1761362.14005802, 5916685.909054825, 14018968.253958803, 12792278.88434212, 4556242.970706283, 450343.1386619192], [-37279.050176898, -65152.72869029378, 51742.3602554755, -12547.20106946975, 0.0, 0.0, 0.0, 0.0, 0.0], [-74884746.12877715, 151121257.16805306, -116940503.93688142, 38530492.03478893, -505019.2117867252, -3599054.5323087526, 1133012.8341776533, -149163.82066675313, 7527.25047639397]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[i][j+1]))
            poss_res[i] += tmp.mul_no_reduce(x.coerce(scaler[i][j+1]))
        poss_res[i].reduce_after_mul()
        poss_res[i] += poss_res0

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    return sfix.dot_product(cipher_index, poss_res)

@types.vectorize
def neuron012(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-4.199999809265137]
    coeffA = [5.6633990916, 21.20878054129, 6.19832793974, 0.39718404693, 0.0, 0.0, 0.0, 0.0, 0.0]
    scaler = [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0]
    
    m = 1
    k = len(coeffA)
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for j in range(degree):
        tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[j+1]))
        poss_res[0] += tmp.mul_no_reduce(x.coerce(scaler[j+1]))
    poss_res[0].reduce_after_mul()
    poss_res[0] += coeffA[0] * scaler[0]

    return poss_res[0]

@types.vectorize
def neuron013(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-4.199999809265137, -2.0999999046325684, -1.0499999523162842, -0.5249999761581421]
    coeffA = [[-10316729.911655527, -29626561.616508156, -35723674.145744495, -23902342.705413923, -9773374.97016071, -2511848.0222657956, -397469.1315200357, -35481.3194092475, -1370.25149401212], [-4004625.228864354, -22613002.768896833, -54945249.1903388, -73969274.71696547, -59887132.92235081, -29909598.241012592, -9046529.563604401, -1523818.171318265, -110000.42699709695], [-28813.42619447338, -100646.59993221652, -596648.3801290331, -1847728.3109447148, -3793095.2372486624, -5247787.074046884, -4184395.904659501, -1705829.9971746823, -276866.10310565284], [-24786.58130300969, -1826.90513637538, 4671.22423734189, -1157.94767612878, 0.0, 0.0, 0.0, 0.0, 0.0]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[i][j+1]))
            poss_res[i] += tmp.mul_no_reduce(x.coerce(scaler[i][j+1]))
        poss_res[i].reduce_after_mul()
        poss_res[i] += poss_res0

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    return sfix.dot_product(cipher_index, poss_res)

@types.vectorize
def neuron014(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-4.199999809265137]
    coeffA = [0.16827514118, 0.25686572624, 0.05461723634, 0.00117894295, 0.0, 0.0, 0.0, 0.0, 0.0]
    scaler = [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0]
    
    m = 1
    k = len(coeffA)
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for j in range(degree):
        tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[j+1]))
        poss_res[0] += tmp.mul_no_reduce(x.coerce(scaler[j+1]))
    poss_res[0].reduce_after_mul()
    poss_res[0] += coeffA[0] * scaler[0]

    return poss_res[0]

@types.vectorize
def neuron015(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-4.199999809265137, -2.0999999046325684, -1.0499999523162842, -0.26249998807907104, 0.26249998807907104, 2.0999999046325684, 3.1499998569488525]
    coeffA = [[-28224815.050547037, -79021382.647194, -93699037.930764, -61935923.49341868, -25091947.256876763, -6402298.999713444, -1007210.0858738472, -89485.31448270936, -3442.22312158423], [-12574929.883481374, -71158744.21421577, -170123139.29834056, -223326485.21857807, -176142238.26758063, -85879332.00989132, -25426221.38768126, -4202655.518485234, -298294.8094444887], [111498.7400176368, -107924.67136478252, -1130666.6320341835, -3522140.5299019893, -9623631.921108315, -14937389.114068506, -11650163.166321304, -4336035.465709588, -608078.9568634074], [119246.46064171204, 25083.38686136279, -170049.32436776347, 323236.60831488756, 0.0, 0.0, 0.0, 0.0, 0.0], [106612.58092670952, 195384.4276468226, -1127007.4778805224, 3301688.5837254515, -5345329.606913056, 4946913.7385496395, -2594961.2443562048, 715877.5361060328, -80516.78945129972], [-156234998.3997025, 415200155.47039217, -458982541.77585965, 269749957.1050636, -87804642.03373519, 13978707.90357435, -227181.3616009152, -233119.42040997776, 22737.9633150943], [-814801011.306747, 1756301395.3569827, -1649107238.8085997, 881559998.6333585, -293565847.47133416, 62383568.531882375, -8263805.42019763, 624065.1113898983, -20574.59769031408]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[i][j+1]))
            poss_res[i] += tmp.mul_no_reduce(x.coerce(scaler[i][j+1]))
        poss_res[i].reduce_after_mul()
        poss_res[i] += poss_res0

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    return sfix.dot_product(cipher_index, poss_res)

@types.vectorize
def neuron016(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-4.199999809265137, -2.0999999046325684, -1.0499999523162842, -0.5249999761581421, 0.0, 0.13124999403953552, 2.0999999046325684]
    coeffA = [[-161134866.73058215, -446480669.4912494, -526452942.4147273, -346636608.9939697, -140018979.77725276, -35644853.251155995, -5597628.003120752, -496618.13048765104, -19081.9447880769], [-111188666.70143886, -625447182.9999267, -1523853058.2827656, -2041891110.1769187, -1641390365.5059536, -814630463.1588991, -245335297.61308727, -41229828.05276902, -2974367.0341679086], [-262026.42136809588, 646030.0986521739, -19832896.984368175, -62257872.05370894, -124490211.75486854, -169500121.2634201, -132805279.96634483, -53269271.539026685, -8533530.226588197], [-23798.89026643268, 3705163.7942431592, -2696139.9841272063, -4919250.611855962, 0.0, 0.0, 0.0, 0.0, 0.0], [-23798.89026643265, 3815361.963012023, -1431471.460635782, -447691.298616995, 0.0, 0.0, 0.0, 0.0, 0.0], [-24152.88435631673, 3823286.824907521, -1478140.8768413623, -552777.3688839881, 1351249.6793482264, -1257182.0673551373, 688396.0783703056, -204059.42765374927, 24984.18445423186], [192561268.75462005, -557097351.0843469, 697615415.7516197, -486721563.4293766, 207151831.12198108, -55157814.66828658, 8994426.51925278, -823239.9665694351, 32451.45060410948]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[i][j+1]))
            poss_res[i] += tmp.mul_no_reduce(x.coerce(scaler[i][j+1]))
        poss_res[i].reduce_after_mul()
        poss_res[i] += poss_res0

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    return sfix.dot_product(cipher_index, poss_res)

@types.vectorize
def neuron017(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-4.199999809265137, -1.0499999523162842, -0.26249998807907104]
    coeffA = [[-23894572.781879555, -99528384.91135809, -168992365.40075397, -152485717.3777009, -80887035.57619923, -26116429.172710862, -5056276.026375122, -540270.2883748513, -24518.62291414183], [-15928.85361074319, 167575.0641097552, 1760042.4563211082, 5927030.322969678, 14844755.019204201, 23860257.017119635, 19947270.61210216, 7963244.201457002, 1200580.7725760739], [-10309.9210450305, -37219.18035406108, 18340.57367944147, -2424.94024798234, 0.0, 0.0, 0.0, 0.0, 0.0]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[i][j+1]))
            poss_res[i] += tmp.mul_no_reduce(x.coerce(scaler[i][j+1]))
        poss_res[i].reduce_after_mul()
        poss_res[i] += poss_res0

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    return sfix.dot_product(cipher_index, poss_res)

@types.vectorize
def neuron018(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-4.199999809265137, -2.0999999046325684, -0.5249999761581421, -0.26249998807907104, 0.0, 0.26249998807907104, 2.0999999046325684, 3.1499998569488525]
    coeffA = [[-1484407.4866918684, -7742477.800255744, -12166667.916909596, -9495880.876949308, -4297203.473814148, -1186820.3728064925, -198154.81151657947, -18438.57073444897, -735.96149687304], [-174918.58970528317, -1516660.6215357373, -6536514.474614611, -14134309.453935394, -15759159.34537139, -9738450.710805552, -3397511.455560977, -628962.3072426494, -48138.54963936023], [34196.14117540242, 312896.5005997612, 208434.0824424117, -616680.8619855468, -86738.31458785721, 263185.7811547329, -890552.3695651306, -1187934.731815192, -392195.219842737], [34197.67532532074, 314053.854142393, 233951.6619377283, -484321.6927457772, 0.0, 0.0, 0.0, 0.0, 0.0], [34197.67532532074, 313658.0388967004, 193918.52493061376, -530050.2475315115, 0.0, 0.0, 0.0, 0.0, 0.0], [42398.56660165606, 207697.6685436082, 756956.137059417, -2106307.4867807217, 2330969.2367236014, -1556464.1776997938, 652390.3255258532, -156317.10128765457, 16209.63961501945], [167544119.99674907, -482924603.2524945, 596475233.117264, -409965127.9059331, 170366233.52867964, -43441273.789227456, 6541654.693997217, -517102.5057221104, 15341.47410597032], [959193496.3668934, -2073043552.4797916, 1951065336.7047486, -1045052791.669757, 348616114.2954928, -74195592.36987393, 9841890.008833904, -744140.2592309705, 24559.97589028884]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[i][j+1]))
            poss_res[i] += tmp.mul_no_reduce(x.coerce(scaler[i][j+1]))
        poss_res[i].reduce_after_mul()
        poss_res[i] += poss_res0

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    return sfix.dot_product(cipher_index, poss_res)

@types.vectorize
def neuron020(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-4.199999809265137, -2.0999999046325684, -1.0499999523162842, -0.5249999761581421, 2.0999999046325684, 3.1499998569488525]
    coeffA = [[-16909930.76516003, -47817827.50062502, -57079144.60806674, -37912222.01685754, -15415342.959558489, -3944445.2620554925, -621941.5852922709, -55357.27803324199, -2132.62402492515], [-4996785.606882788, -28103906.11828723, -67804094.00562234, -90450608.68021265, -72473047.07810047, -35790598.14561393, -10698505.871266754, -1780455.943632576, -126971.697711251], [-30705.68577020882, -153540.19711924135, -950594.1141857184, -3078520.3961195573, -6394877.002486836, -8524621.053974124, -6521249.84464315, -2575664.927325593, -408734.5041954065], [-18824.4929333772, 5114.27824952314, -5077.54830642439, 941.56942821309, 0.0, 0.0, 0.0, 0.0, 0.0], [207804008.45862892, -578962667.2166904, 683700981.2483355, -443105946.2458144, 169922345.1094184, -38424296.47816415, 4694708.866109139, -225484.76472224423, -2475.14957649714], [1142038874.7998457, -2467189018.822754, 2321176247.5689607, -1242902646.5404706, 414500278.4426356, -88195648.92154585, 11696349.024955157, -884176.0512223849, 29176.42093602176]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[i][j+1]))
            poss_res[i] += tmp.mul_no_reduce(x.coerce(scaler[i][j+1]))
        poss_res[i].reduce_after_mul()
        poss_res[i] += poss_res0

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    return sfix.dot_product(cipher_index, poss_res)

@types.vectorize
def neuron021(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-4.199999809265137, -2.0999999046325684, -0.5249999761581421, 2.0999999046325684]
    coeffA = [[-7573270.321740432, -21436817.083329238, -25517408.68906156, -16914013.472300474, -6869086.120572718, -1756475.3478859805, -276852.16682862607, -24637.10197821716, -949.0487222236], [-44384.47297243018, 972372.2782280499, 4118837.5248233173, 8199347.202656922, 9986302.750906933, 7432596.781438427, 3242943.8512410466, 759476.3626756243, 73719.08724200644], [-143769.8332581594, -70121.00260645182, 73613.68285299391, -19082.01392792054, 0.0, 0.0, 0.0, 0.0, 0.0], [192785708.31830126, -463258616.262881, 471194347.54196024, -264344996.9048376, 89089866.41497917, -18342320.270057123, 2223333.5503187524, -141130.73368265174, 3354.26346024985]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[i][j+1]))
            poss_res[i] += tmp.mul_no_reduce(x.coerce(scaler[i][j+1]))
        poss_res[i].reduce_after_mul()
        poss_res[i] += poss_res0

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    return sfix.dot_product(cipher_index, poss_res)

@types.vectorize
def neuron022(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-4.199999809265137, -1.0499999523162842, 0.0, 2.0999999046325684]
    coeffA = [[-7231125.371325579, -30008205.45512333, -50845275.243069604, -45868602.74774434, -24344004.428913724, -7865955.000742794, -1524067.5992435243, -162967.37061512138, -7400.69702979448], [-130385.3115239295, -118028.10338689967, 306635.96836157923, 334762.9722194681, 0.0, 0.0, 0.0, 0.0, 0.0], [-130385.31152392951, 4526.87296379243, -11016.08921263673, 4251.20772998262, 0.0, 0.0, 0.0, 0.0, 0.0], [90296750.92942458, -218168223.71453914, 223246520.6663172, -126254968.03202675, 43034093.81622958, -9009102.691315783, 1120919.293833807, -74424.83415753813, 1939.82491633942]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[i][j+1]))
            poss_res[i] += tmp.mul_no_reduce(x.coerce(scaler[i][j+1]))
        poss_res[i].reduce_after_mul()
        poss_res[i] += poss_res0

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    return sfix.dot_product(cipher_index, poss_res)

@types.vectorize
def neuron023(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-4.199999809265137, -3.1499998569488525, -2.0999999046325684, -1.0499999523162842, -0.5249999761581421, 0.0]
    coeffA = [[-18541225.780824967, -38849213.10107533, -35516749.28257466, -18543271.985089786, -6049644.625319717, -1262885.166758048, -164724.6838789148, -12273.48888049146, -399.93199008148], [41345869.55722057, 99203230.6244263, 94082686.41391589, 42733196.60417653, 7272487.183281856, -1436246.8912929313, -894150.3696764725, -156173.5689073802, -9824.98310245893], [24972237.939997055, 141236053.5404525, 337625473.18977493, 441821248.7971813, 346829105.6908621, 168236423.21022967, 49565302.869359635, 8155667.036475477, 576513.5008607158], [-173284.4526921284, 927133.0978626478, 6555361.161483356, 19028311.302213468, 41138303.98361943, 55871071.18154632, 42207176.593633965, 16320265.65150842, 2538356.9362676525], [-250293.43269297233, -51748.04690587358, 1112268.2698105832, 512766.798754058, 0.0, 0.0, 0.0, 0.0, 0.0], [-250293.43269297227, 17619.09512775262, -17522.45702586103, -455.15629390102, 0.0, 0.0, 0.0, 0.0, 0.0]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[i][j+1]))
            poss_res[i] += tmp.mul_no_reduce(x.coerce(scaler[i][j+1]))
        poss_res[i].reduce_after_mul()
        poss_res[i] += poss_res0

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    return sfix.dot_product(cipher_index, poss_res)

@types.vectorize
def neuron024(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-4.199999809265137]
    coeffA = [0.42431477069, 0.48530476067, 0.08895074018, 0.0002135364, 0.0, 0.0, 0.0, 0.0, 0.0]
    scaler = [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0]
    
    m = 1
    k = len(coeffA)
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for j in range(degree):
        tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[j+1]))
        poss_res[0] += tmp.mul_no_reduce(x.coerce(scaler[j+1]))
    poss_res[0].reduce_after_mul()
    poss_res[0] += coeffA[0] * scaler[0]

    return poss_res[0]

@types.vectorize
def neuron025(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-4.199999809265137, -1.0499999523162842, -0.13124999403953552, 2.0999999046325684, 3.1499998569488525]
    coeffA = [[-30059220.809463874, -123536956.9063126, -205570472.9915456, -182206330.2377054, -95266952.96925463, -30408125.70598853, -5833395.754700358, -618704.747770275, -27908.61386798607], [-41285.29768739232, -165108.59270418694, 1084196.2565678912, 1544595.021314235, 4955298.668733569, 12289246.45523895, 11318367.572390413, 4027276.7300131386, 395692.6993075097], [-19496.26827642703, -109356.85498552443, 98686.40134626212, -26564.22664575155, 0.0, 0.0, 0.0, 0.0, 0.0], [302264583.95258766, -842006162.6380285, 993777143.8047663, -643418534.8219217, 246325444.88124642, -55540550.9754803, 6745584.741887756, -317410.44835260324, -4160.54583721604], [1644010049.1466908, -3550758996.707026, 3339908786.919065, -1788076225.3931334, 596219577.8999852, -126843844.3035727, 16819783.427339938, -1271342.6756747125, 41948.34007106344]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[i][j+1]))
            poss_res[i] += tmp.mul_no_reduce(x.coerce(scaler[i][j+1]))
        poss_res[i].reduce_after_mul()
        poss_res[i] += poss_res0

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    return sfix.dot_product(cipher_index, poss_res)

@types.vectorize
def neuron026(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-4.199999809265137, -1.0499999523162842, -0.5249999761581421, 0.0, 0.26249998807907104, 2.0999999046325684]
    coeffA = [[49122207.12011385, 202033710.30883163, 320185233.42475885, 269837437.6346558, 135131279.5967205, 41646429.51427811, 7768011.556603436, 805591.8458077204, 35689.3800779093], [-177890.6159199142, 1563312.6928963263, -14511284.654759733, -44318911.99959204, -87915045.17771322, -120257956.8259146, -94025990.90808953, -37501511.75762277, -5971785.811280109], [-8269.08813574742, 3726354.489850926, -2485303.7730136, -4083474.8359890343, 0.0, 0.0, 0.0, 0.0, 0.0], [-8269.08813574735, 3819983.7785819285, -1515720.2395128761, -102354.299260172, 0.0, 0.0, 0.0, 0.0, 0.0], [-14574.83131371572, 3901435.304494975, -1894574.924348713, 608513.0874954212, -487316.55053538986, 443831.0798711415, -219608.7701014662, 54617.9571421334, -5441.44452197796], [484809066.8336824, -1270930950.2712615, 1439022399.6450152, -913458780.7195233, 355682741.1468201, -87066314.6425862, 13102131.42065161, -1109831.2958554504, 40570.92832746749]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[i][j+1]))
            poss_res[i] += tmp.mul_no_reduce(x.coerce(scaler[i][j+1]))
        poss_res[i].reduce_after_mul()
        poss_res[i] += poss_res0

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    return sfix.dot_product(cipher_index, poss_res)

@types.vectorize
def neuron027(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-4.199999809265137, -0.5249999761581421, -0.26249998807907104, 0.26249998807907104, 2.0999999046325684]
    coeffA = [[-770149.8917741873, -5972682.273770436, -16589299.098403897, -20996384.648412418, -14249051.24805695, -5558938.675700043, -1251722.956997051, -151404.77109721163, -7623.57502231191], [103559.46175566153, 56622.18928737926, -281750.9005332226, 569622.5884947126, 64051.2995814543, 143356.05090584527, 3216349.130698916, 3779703.8269044557, 1258790.0621204847], [103674.22459571969, 57308.73851834964, -295169.91427837306, 466148.8227245894, 0.0, 0.0, 0.0, 0.0, 0.0], [125373.15160354726, -212112.02495024644, 1022552.2454268968, -2690990.7426832695, 4039756.9483254342, -3518189.9435102297, 1751879.3579235754, -461750.2426771819, 49890.50618522357], [42561892.32004593, -121785623.29675421, 149401338.49823126, -102454025.11897485, 43017020.71198137, -11344609.184672883, 1838725.5409867677, -167757.28863338727, 6606.67463169114]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[i][j+1]))
            poss_res[i] += tmp.mul_no_reduce(x.coerce(scaler[i][j+1]))
        poss_res[i].reduce_after_mul()
        poss_res[i] += poss_res0

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    return sfix.dot_product(cipher_index, poss_res)

@types.vectorize
def neuron028(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-4.199999809265137, -2.0999999046325684, -0.5249999761581421, 0.0, 0.5249999761581421, 2.0999999046325684]
    coeffA = [[8341732.058426334, 19815132.514161814, 20218115.868301675, 11767120.434091961, 4281465.922420771, 996659.8865575152, 144837.92364711783, 12006.42811194361, 434.48491443779], [460618.3650007195, -735390.0791576323, -4466067.338641568, -9050984.681054197, -10888761.116253916, -7840375.23863786, -3275289.316315909, -732924.808774155, -68130.4515494737], [582366.3065038155, 375917.6242714464, -191712.9749477896, -123370.7196939597, 0.0, 0.0, 0.0, 0.0, 0.0], [582366.3065038155, 373924.67659050995, -145730.38794581196, -50849.32285389262, 0.0, 0.0, 0.0, 0.0, 0.0], [405380.7890885768, 2217510.588928345, -8185225.91667855, 18884757.010937955, -25948736.98032864, 20945808.040561397, -9762081.345854798, 2428702.8281115615, -249195.25494258857], [-602635522.9323168, 1531013253.053648, -1661262607.802212, 1006678264.5904816, -372931431.9549051, 86594618.94623394, -12320106.186586132, 982566.2762852745, -33638.58094409478]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[i][j+1]))
            poss_res[i] += tmp.mul_no_reduce(x.coerce(scaler[i][j+1]))
        poss_res[i].reduce_after_mul()
        poss_res[i] += poss_res0

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    return sfix.dot_product(cipher_index, poss_res)

@types.vectorize
def neuron030(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-4.199999809265137, -2.0999999046325684, -1.0499999523162842, 0.0, 2.0999999046325684]
    coeffA = [[33031543.866967328, 94947170.78137155, 114806912.92682998, 76974544.09202896, 31517290.956785414, 8107869.0180510385, 1283840.8655757254, 114664.83384734755, 4430.02590685568], [16374813.880949637, 94740204.1978881, 230313399.65058663, 307052395.6377857, 245866212.85018638, 121638368.31505935, 36520182.81239599, 6117253.583078959, 439736.8301096875], [-368034.7079832627, -65888.75170611976, 1170001.446241334, 893839.6593481537, 0.0, 0.0, 0.0, 0.0, 0.0], [-368034.7079832627, 13964.45595351408, -23534.9060034214, 7543.74777827187, 0.0, 0.0, 0.0, 0.0, 0.0], [433623528.78865236, -1108176639.7475328, 1211738715.3186073, -741339003.155268, 277854566.8248161, -65427003.78182186, 9465085.512355713, -770001.8706338931, 26993.07449192915]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[i][j+1]))
            poss_res[i] += tmp.mul_no_reduce(x.coerce(scaler[i][j+1]))
        poss_res[i].reduce_after_mul()
        poss_res[i] += poss_res0

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    return sfix.dot_product(cipher_index, poss_res)

@types.vectorize
def neuron031(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-4.199999809265137, -3.1499998569488525, -2.0999999046325684, -1.0499999523162842, -0.13124999403953552, 0.26249998807907104, 1.0499999523162842, 2.0999999046325684, 3.1499998569488525]
    coeffA = [[33691419.61078293, 70508452.09885319, 64490540.95347187, 33691978.68069884, 10997494.81481052, 2296632.682077581, 299643.83500827383, 22330.75339567474, 727.76335886241], [-77148214.40548588, -192059629.3214502, -192497307.74773628, -97531014.69969293, -23956690.27385283, -955534.0080911763, 905653.8732288497, 202581.77341322773, 13903.40097778096], [-36436459.04480691, -205388965.71884543, -493474176.6015126, -651848823.881161, -516845453.89817286, -253016257.35844392, -75141101.31724826, -12449506.929518873, -885328.3249556568], [84750.41411338, 49408.19526750073, -1086101.2974531336, -1778175.684404872, -7759892.944181783, -16431318.103274688, -13235685.19423947, -3983471.996757758, -225435.5898825252], [86713.34631675937, 99088.92150408823, -574841.719429776, 865533.2305648904, 0.0, 0.0, 0.0, 0.0, 0.0], [89253.41079094862, 55256.20436396997, -263700.02539282636, -407516.9262357399, 3726206.3029656583, -7206827.325879455, 6291313.162985504, -2614141.7248472758, 419106.4115117702], [15487467.9984192, -88818789.69356108, 220505739.01308304, -306929354.2224343, 261495053.77886078, -139497385.05083552, 45495522.51092513, -8297981.14359183, 648735.216060324], [-133191889.71284059, 309524685.10084754, -270793248.3944134, 91633813.56564362, 12320842.975032244, -20680242.00150223, 7047562.34284349, -1084690.1591942732, 65492.08392168125], [-644185198.8935286, 1377661342.420493, -1284766221.0440676, 682724652.6960089, -226168868.57250977, 47840566.2491573, -6311464.582286866, 474893.78587302216, -15605.58823746412]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[i][j+1]))
            poss_res[i] += tmp.mul_no_reduce(x.coerce(scaler[i][j+1]))
        poss_res[i].reduce_after_mul()
        poss_res[i] += poss_res0

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    return sfix.dot_product(cipher_index, poss_res)

@types.vectorize
def neuron032(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-4.199999809265137, -1.0499999523162842, 0.0, 2.0999999046325684]
    coeffA = [[-25816984.711684603, -105417136.5897875, -175887632.0003747, -156644616.81825432, -82291555.97928642, -26376154.37976659, -5077768.49716573, -540151.3307554505, -24425.44792909609], [-216396.49913431317, -59129.36143092342, 1064644.1212351513, 1012484.5085886016, 0.0, 0.0, 0.0, 0.0, 0.0], [-216396.49913431317, -2338.95469112249, -181.79061238855, -246.72497468553, 0.0, 0.0, 0.0, 0.0, 0.0], [-125268761.21304053, 273680725.8281312, -244280030.2636415, 111953890.12425083, -26135323.61414384, 1927059.1797364675, 418572.5891851544, -99060.19358632472, 6097.93570471281]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[i][j+1]))
            poss_res[i] += tmp.mul_no_reduce(x.coerce(scaler[i][j+1]))
        poss_res[i].reduce_after_mul()
        poss_res[i] += poss_res0

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    return sfix.dot_product(cipher_index, poss_res)

@types.vectorize
def neuron033(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-4.199999809265137, -2.0999999046325684, -1.0499999523162842, -0.26249998807907104, 0.0, 0.26249998807907104, 2.0999999046325684, 3.1499998569488525]
    coeffA = [[-49366985.49417527, -138008986.82484502, -163451243.2227241, -107946917.56934428, -43702301.3438843, -11144719.943794787, -1752508.3826010413, -155643.470391099, -5985.2450221605], [-18405784.217743423, -103685949.71773747, -248465157.78589904, -327505940.56573653, -259203442.4987862, -126654186.36972062, -37536353.718251, -6204818.734245226, -440144.6953999812], [45732.74125695909, -150395.73529192488, -1505670.650368848, -4855907.875880197, -12922216.731263198, -20168205.787890986, -15969174.373359168, -6037674.018993296, -860763.0445629547], [56139.15883608656, 26630.64047796246, -239645.77768837853, 236899.52924235913, 0.0, 0.0, 0.0, 0.0, 0.0], [56139.15883608656, 27291.46139291623, -175976.23020976092, 290780.45227821317, 0.0, 0.0, 0.0, 0.0, 0.0], [51127.31024357201, 100510.35908834905, -636844.8781027098, 1871301.5513117602, -2915042.26691043, 2558169.496338804, -1268058.069019995, 330654.5387235246, -35182.500885243], [123138522.51605797, -370667018.4967424, 480503280.3538877, -349347650.85820955, 155419526.69073498, -43217752.63101236, 7316162.881322596, -686978.4830111164, 27247.81062550131], [751135238.6108125, -1629778618.482506, 1539086324.192864, -826761245.3576415, 276485878.1866401, -58972455.26912968, 7837541.345077317, -593593.364782831, 19620.60154062212]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[i][j+1]))
            poss_res[i] += tmp.mul_no_reduce(x.coerce(scaler[i][j+1]))
        poss_res[i].reduce_after_mul()
        poss_res[i] += poss_res0

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    return sfix.dot_product(cipher_index, poss_res)

@types.vectorize
def neuron034(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-4.199999809265137]
    coeffA = [-0.66579411622, -0.98038295321, -0.15645290214, 0.00793222592, 0.0, 0.0, 0.0, 0.0, 0.0]
    scaler = [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0]
    
    m = 1
    k = len(coeffA)
    degree = k-1
    
    m = 1
    k = len(coeffA)
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for j in range(degree):
        tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[j+1]))
        poss_res[0] += tmp.mul_no_reduce(x.coerce(scaler[j+1]))
    poss_res[0].reduce_after_mul()
    poss_res[0] += coeffA[0] * scaler[0]

    return poss_res[0]

@types.vectorize
def neuron035(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-4.199999809265137, -1.0499999523162842, -0.26249998807907104, 0.0]
    coeffA = [[-28704648.23871814, -117300900.26637025, -194687924.7601774, -172374539.43878874, -90086681.76920408, -28749745.8649463, -5514962.530885817, -584929.1921931016, -26385.53714937986], [-81504.76831646853, 110899.29062657373, 2413336.4006525404, 6647498.413162203, 16957522.926640756, 28472171.02307899, 24122877.66464339, 9637067.7024317, 1448924.992987361], [-95798.8862741778, -129394.9932142503, 744253.9330331824, 104274.39728732091, 0.0, 0.0, 0.0, 0.0, 0.0], [-95798.88627417776, 11391.53027243123, -16289.18515469364, 1094.15190325856, 0.0, 0.0, 0.0, 0.0, 0.0]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[i][j+1]))
            poss_res[i] += tmp.mul_no_reduce(x.coerce(scaler[i][j+1]))
        poss_res[i].reduce_after_mul()
        poss_res[i] += poss_res0

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    return sfix.dot_product(cipher_index, poss_res)

@types.vectorize
def neuron036(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-4.199999809265137, -1.0499999523162842, -0.5249999761581421, 0.0, 0.13124999403953552, 2.0999999046325684]
    coeffA = [[59111895.85050275, 244787813.13823006, 394352024.1750819, 337865545.4826765, 171680525.5378506, 53568037.49434845, 10095339.534410212, 1055989.2522618684, 47119.00547985172], [-247009.6830246187, 1141076.7492534986, -17048499.403999593, -52561773.659904696, -105077729.08250983, -143253737.5710774, -111774493.58468658, -44582561.19615333, -7106343.200923566], [-45268.33579676309, 3721165.1385383015, -2653779.9633559524, -4357807.274593363, 0.0, 0.0, 0.0, 0.0, 0.0], [-45268.33579676309, 3822836.998317445, -1489058.3235459751, -315421.57306970115, 0.0, 0.0, 0.0, 0.0, 0.0], [-46414.76063117645, 3846016.8036830747, -1649468.2080686188, 31015.03893648124, 310669.644366291, -221565.7179678752, 109012.811806701, -33736.18921726478, 4511.57145516866], [393959413.7276186, -1048130373.1127697, 1206363027.2493322, -778641685.7361187, 308356936.1399029, -76786191.46183039, 11758620.563023824, -1014019.113711535, 37759.67566788019]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[i][j+1]))
            poss_res[i] += tmp.mul_no_reduce(x.coerce(scaler[i][j+1]))
        poss_res[i].reduce_after_mul()
        poss_res[i] += poss_res0

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    return sfix.dot_product(cipher_index, poss_res)

@types.vectorize
def neuron037(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-4.199999809265137, -2.0999999046325684, -1.0499999523162842, -0.5249999761581421, 2.0999999046325684, 3.1499998569488525]
    coeffA = [[-59169847.072477765, -166356335.75093615, -197715624.04120797, -130913826.706919, -53108366.9033844, -13565706.229569133, -2136099.054596705, -189925.21572976853, -7310.5067653904], [-22818424.792686664, -128745259.19351727, -311524084.45029825, -415589191.69989777, -332797681.34297985, -164388009.22597054, -49208941.95319291, -8210391.31341938, -587548.6408115936], [-62108.75451281205, -535801.7445074287, -4382393.862521566, -13138040.099271648, -26959269.930209335, -36756070.62466583, -28632834.09892945, -11426685.54164425, -1823726.1306480097], [-15687.6455037326, 158454.88085531033, -174323.70980978847, 49936.03047519862, 0.0, 0.0, 0.0, 0.0, 0.0], [-400295158.1808496, 1149449124.6623447, -1409020001.0896888, 958432294.5525569, -393089828.8700432, 98550582.59802708, -14492808.509669168, 1102225.1520902636, -30098.4394192924], [-2091963165.1070428, 4521104057.599722, -4254974915.83133, 2279041553.0198174, -760239590.2113118, 161796938.2572294, -21461496.23196245, 1622653.1394289853, -53553.55752157784]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[i][j+1]))
            poss_res[i] += tmp.mul_no_reduce(x.coerce(scaler[i][j+1]))
        poss_res[i].reduce_after_mul()
        poss_res[i] += poss_res0

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    return sfix.dot_product(cipher_index, poss_res)

@types.vectorize
def neuron038(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-4.199999809265137, -1.0499999523162842, -0.26249998807907104, 0.5249999761581421, 2.0999999046325684]
    coeffA = [[7144012.075727272, 27221945.04698444, 43159097.158599906, 37188143.16291078, 19108977.63375798, 6029867.439870675, 1147484.5377006186, 120985.3532666969, 5432.65649401304], [419416.6260664869, 318470.9699605453, -778401.7603227438, -1975226.2487012204, -5080788.908943089, -8373484.828399177, -6836953.509237568, -2629877.8941273936, -380505.22710734047], [423818.4003812526, 394550.8533578243, -246166.569850902, 59959.11317964381, 0.0, 0.0, 0.0, 0.0, 0.0], [385537.46208985813, 1016848.4911588163, -3792594.9749018047, 10074798.10907525, -15466527.239390256, 13404193.33559688, -6558273.961092658, 1692508.7539246713, -178971.3620776039], [-271055914.3376865, 710905364.9350709, -797278417.7993873, 500665152.9004306, -192889298.32857847, 46784421.86553109, -6989396.256386239, 588989.3149999934, -21464.42844010011]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[i][j+1]))
            poss_res[i] += tmp.mul_no_reduce(x.coerce(scaler[i][j+1]))
        poss_res[i].reduce_after_mul()
        poss_res[i] += poss_res0

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    return sfix.dot_product(cipher_index, poss_res)

@types.vectorize
def neuron040(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-4.199999809265137, -2.0999999046325684, -1.0499999523162842, -0.5249999761581421, 0.0, 2.0999999046325684]
    coeffA = [[40911891.49756089, 110060715.44707343, 126860994.22693145, 82084868.18325014, 32704401.816404607, 8233781.309415584, 1281267.9403071266, 112807.48424129272, 4306.46295024483], [17923298.715115495, 101434587.6842052, 240344293.10828322, 309624119.747104, 238616774.9494183, 113559874.66292562, 32832374.694631726, 5304309.89878215, 368352.1930225603], [-249818.51837714127, 793922.790652488, 5731564.8179442715, 16319705.614053812, 35714341.64041303, 48358066.538900815, 36095822.07128548, 13776530.864569519, 2118438.133926178], [-316414.51076616184, -50725.61429019627, 1041429.945923923, 307958.73052635015, 0.0, 0.0, 0.0, 0.0, 0.0], [-316414.51076616184, -3263.63510760506, 3465.51696690048, -1905.76693265603, 0.0, 0.0, 0.0, 0.0, 0.0], [76012097.75234877, -210756449.47490907, 249291295.05869842, -165195220.03040594, 67215426.0533369, -17236052.879706927, 2725306.424242801, -243296.50105854828, 9400.41877022722]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[i][j+1]))
            poss_res[i] += tmp.mul_no_reduce(x.coerce(scaler[i][j+1]))
        poss_res[i].reduce_after_mul()
        poss_res[i] += poss_res0

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    return sfix.dot_product(cipher_index, poss_res)

@types.vectorize
def neuron041(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-4.199999809265137, -1.0499999523162842, -0.26249998807907104, 2.0999999046325684, 3.1499998569488525]
    coeffA = [[-6314913.752861371, -27685584.339590233, -49015727.125822455, -45567346.56322592, -24694455.918257568, -8100242.0176736, -1587206.8279201498, -171192.44488278785, -7827.34428737127], [-6260.91593034605, -38669.51330716879, 183296.0139528335, -139139.40153761758, -997271.7155751253, 266518.5384351136, 1758855.2574984226, 1193910.523719526, 248406.11184719813], [5861.98384240926, -29485.81480215888, 12725.54114626659, 1705.6664562271, 0.0, 0.0, 0.0, 0.0, 0.0], [-288991955.95419866, 798275173.2965802, -930595026.466431, 591688873.8467385, -220405090.71813717, 47467276.27385699, -5224698.674121787, 159184.15729837742, 11114.33153332947], [-1254912129.6077702, 2697441751.826447, -2526821951.74846, 1347964517.9448159, -448072747.73813045, 95066285.6527969, -12575679.616384912, 948518.5900182376, -31237.14477986357]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[i][j+1]))
            poss_res[i] += tmp.mul_no_reduce(x.coerce(scaler[i][j+1]))
        poss_res[i].reduce_after_mul()
        poss_res[i] += poss_res0

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    return sfix.dot_product(cipher_index, poss_res)

@types.vectorize
def neuron042(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-4.199999809265137, -2.0999999046325684, -1.0499999523162842, 0.0, 2.0999999046325684]
    coeffA = [[24748688.70127384, 69128228.89514287, 81887738.4482442, 54088591.4128973, 21898578.74242371, 5584291.216413159, 878077.7966678056, 77978.16762766689, 2998.4213495823], [10479329.137909524, 60014654.163500145, 143518527.73417443, 187583752.21009853, 147116444.068373, 71310051.2003137, 20993061.702890784, 3451042.375402657, 243670.8541722448], [-243808.9344627764, 22342.64623688958, 862277.641828326, 601145.1546842257, 0.0, 0.0, 0.0, 0.0, 0.0], [-243808.9344627764, -1953.02218409444, 693.44008480067, -282.82937806564, 0.0, 0.0, 0.0, 0.0, 0.0], [37553015.8574977, -93661291.3251955, 98783560.47546518, -57908898.73536488, 20652814.617238827, -4593034.006347981, 621884.3213455534, -46794.74836892431, 1493.06612835271]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[i][j+1]))
            poss_res[i] += tmp.mul_no_reduce(x.coerce(scaler[i][j+1]))
        poss_res[i].reduce_after_mul()
        poss_res[i] += poss_res0

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    return sfix.dot_product(cipher_index, poss_res)

@types.vectorize
def neuron043(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-4.199999809265137, -1.0499999523162842, -0.26249998807907104, 0.0]
    coeffA = [[-38658946.491358936, -157293710.94214973, -259931750.18006912, -229364030.57781222, -119571267.65106896, -38088984.25959984, -7296444.422593089, -773074.3395757708, -34844.83687189334], [-228705.25309219863, 78578.47582956881, 3449440.7081694803, 8693624.619955977, 22156512.57849552, 38122102.83669278, 32732850.806463487, 13177573.392516954, 1993692.638671847], [-247665.38637011388, -238791.2907702375, 1268373.2704856622, 221175.11121895604, 0.0, 0.0, 0.0, 0.0, 0.0], [-247665.38637011385, -35650.0482780688, 32706.11773437312, -6973.4580761472, 0.0, 0.0, 0.0, 0.0, 0.0]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[i][j+1]))
            poss_res[i] += tmp.mul_no_reduce(x.coerce(scaler[i][j+1]))
        poss_res[i].reduce_after_mul()
        poss_res[i] += poss_res0

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    return sfix.dot_product(cipher_index, poss_res)

@types.vectorize
def neuron044(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-4.199999809265137]
    coeffA = [-3.17813592927, 0.6235763367, 0.73370662912, 0.10045801924, 0.0, 0.0, 0.0, 0.0, 0.0]
    scaler = [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0]
    
    m = 1
    k = len(coeffA)
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for j in range(degree):
        tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[j+1]))
        poss_res[0] += tmp.mul_no_reduce(x.coerce(scaler[j+1]))
    poss_res[0].reduce_after_mul()
    poss_res[0] += coeffA[0] * scaler[0]

    return poss_res[0]

@types.vectorize
def neuron045(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-4.199999809265137, -2.0999999046325684, -1.0499999523162842, -0.26249998807907104, 0.0, 0.26249998807907104, 2.0999999046325684]
    coeffA = [[-77461065.30372204, -213539417.20665982, -250488107.55204353, -164254516.83948687, -66133869.28544469, -16791710.101694126, -2631194.0531574883, -233003.47141003405, -8938.43387961759], [-32113731.51765947, -181995393.36923137, -435874776.26412594, -571183462.2414155, -448665333.68245393, -217611219.07881045, -64065705.659526326, -10529160.335554386, -743175.0907144753], [341510.9487978913, -150613.94634624282, -3132035.152356579, -8013570.976013739, -21926819.47624664, -36109520.96012574, -29291238.92830987, -11203194.033946522, -1611665.1781531961], [359647.11491399887, 155016.87260855202, -994425.3108772426, 443165.28315173305, 0.0, 0.0, 0.0, 0.0, 0.0], [359647.11491399887, 159790.30732335543, -833673.2300769503, 1150629.092022322, 0.0, 0.0, 0.0, 0.0, 0.0], [249750.3069512942, 1560820.3596870096, -8061437.549767059, 20662503.83718563, -29358856.018964075, 24188168.69917038, -11482083.989791084, 2910316.396395606, -304712.73137874843], [-111774055.41710255, 332954375.4807304, -420067569.0321082, 294974881.4332027, -126481195.00984474, 34010772.2967789, -5614192.727233655, 521156.239346838, -20863.26048899656]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[i][j+1]))
            poss_res[i] += tmp.mul_no_reduce(x.coerce(scaler[i][j+1]))
        poss_res[i].reduce_after_mul()
        poss_res[i] += poss_res0

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    return sfix.dot_product(cipher_index, poss_res)

@types.vectorize
def neuron046(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-4.199999809265137, -1.0499999523162842, -0.26249998807907104, 0.0, 0.5249999761581421, 2.0999999046325684]
    coeffA = [[48754320.56642335, 200217817.15049154, 319237375.6434612, 271114871.8991754, 136766203.8011039, 42418969.57997969, 7954501.887193323, 828599.5715876471, 36843.6064391949], [237153.859402395, 3277751.6180385305, -5184055.3266390525, -16471665.738297794, -36075390.48355719, -59180689.85205627, -50280372.47100284, -20108981.08143936, -3017970.2737345346], [267747.5637073995, 3793636.484037169, -1577065.3860224567, -2316505.577862909, 0.0, 0.0, 0.0, 0.0, 0.0], [267747.5637073996, 3821397.811279533, -1590559.1761172377, 113625.29643859447, 0.0, 0.0, 0.0, 0.0, 0.0], [148703.01666996887, 4730787.276330487, -4352876.74882915, 4381210.698796859, -3685435.5973575865, 1883392.6717458016, -482451.66797881416, 34977.96591666899, 4501.02419020887], [148118693.63092944, -460969177.80959934, 614607922.0384771, -451078745.44450396, 200150364.00939703, -55187814.081061035, 9272181.49675699, -871023.5953602887, 35133.38124040002]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[i][j+1]))
            poss_res[i] += tmp.mul_no_reduce(x.coerce(scaler[i][j+1]))
        poss_res[i].reduce_after_mul()
        poss_res[i] += poss_res0

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    return sfix.dot_product(cipher_index, poss_res)

@types.vectorize
def neuron047(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-4.199999809265137, -2.0999999046325684, -1.0499999523162842, 0.0]
    coeffA = [[-32723863.71300872, -91731510.68968768, -108769780.85835628, -71897669.13712117, -29130417.227485083, -7433805.829501534, -1169676.800586322, -103936.43582392344, -3998.72462144539], [-12631113.588757433, -70613952.35408445, -170976262.76499116, -228806952.31820342, -183816514.19838122, -91054208.5099768, -27323071.706397884, -4568528.8379789805, -327561.1816103859], [-150518.81437845633, 32184.69058119644, -166604.3826137723, -313078.16793403804, 0.0, 0.0, 0.0, 0.0, 0.0], [-150518.81437845636, 5052.13130330091, -2154.71778348833, -1511.26591289489, 0.0, 0.0, 0.0, 0.0, 0.0]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[i][j+1]))
            poss_res[i] += tmp.mul_no_reduce(x.coerce(scaler[i][j+1]))
        poss_res[i].reduce_after_mul()
        poss_res[i] += poss_res0

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    return sfix.dot_product(cipher_index, poss_res)

@types.vectorize
def neuron048(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-4.199999809265137, -2.0999999046325684, -0.5249999761581421, 0.26249998807907104, 1.0499999523162842, 2.0999999046325684]
    coeffA = [[-7534148.277950299, -27521585.824923284, -37881902.65970748, -27594188.899872966, -11972712.787710214, -3214705.550456255, -526026.4194216493, -48215.08426725586, -1902.14242970691], [-514338.54442459875, -3375553.90077363, -13307554.796774581, -27201499.675477944, -28636757.341350798, -16562487.132164188, -5327338.223661668, -887912.0545646661, -58876.06864322178], [-82543.98674762201, 339374.6966355715, 201534.85861051365, -789057.4831028841, 0.0, 0.0, 0.0, 0.0, 0.0], [-81364.32264328703, 321485.8965636767, 349506.6203147651, -1667390.3549964135, 2325097.0431311955, -1540514.4348288367, 208337.41461417635, 248169.73050666007, -88596.41500417361], [-6955570.547112865, 40893259.43475966, -103517321.02670099, 148600265.28236324, -131451694.55159809, 72895284.65699345, -24668127.511361316, 4653518.290712536, -374906.6863778909], [21960816.316870026, -98333582.81322703, 158962855.04843295, -132346444.25026271, 64286256.46115312, -19015164.11599232, 3383518.4473132263, -333667.48210615397, 14037.06448929504]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[i][j+1]))
            poss_res[i] += tmp.mul_no_reduce(x.coerce(scaler[i][j+1]))
        poss_res[i].reduce_after_mul()
        poss_res[i] += poss_res0

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    return sfix.dot_product(cipher_index, poss_res)

@types.vectorize
def neuron100(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-4.199999809265137, -1.0499999523162842, -0.13124999403953552, 0.0, 0.13124999403953552, 1.0499999523162842]
    coeffA = [[-2615172.30890024, -7724628.924813087, -6236555.159324077, -1510146.4835126135, 632057.14670838, 522546.8071221606, 145574.28157541435, 19097.04043146714, 990.08855875019], [29843.5132436543, -38377.64335858755, 151245.29724211388, -1728136.8441239966, 491070.0947100004, 5146292.66651351, 4840108.316966976, 1697857.7977379875, 186633.27622841115], [29521.26220142167, -45897.4648841207, 97379.1935555421, -1830794.0799934529, 0.0, 0.0, 0.0, 0.0, 0.0], [29521.26220142167, -46673.18874593632, 75456.22992992547, -2323013.91544593, 0.0, 0.0, 0.0, 0.0, 0.0], [28361.79672759262, -17381.88025298455, -227845.4092283404, -614302.1987446598, -5737988.91160256, 10544130.462125, -6283741.94887018, 967730.1994266604, 179393.10759761868], [10389621.141286323, -38840445.26007253, 58953201.25460816, -51015952.763581775, 26182083.945680242, -8229019.867130884, 1557994.3009210615, -163367.77646943557, 7295.49694283634]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[i][j+1]))
            poss_res[i] += tmp.mul_no_reduce(x.coerce(scaler[i][j+1]))
        poss_res[i].reduce_after_mul()
        poss_res[i] += poss_res0

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    return sfix.dot_product(cipher_index, poss_res)

@types.vectorize
def neuron110(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-4.199999809265137, -0.5249999761581421, -0.26249998807907104, 0.5249999761581421, 2.0999999046325684]
    coeffA = [[-450451.55183743493, -3033528.082462054, -7266505.4702574285, -8071942.86785696, -4908466.655551031, -1746614.2339419723, -363974.34801038064, -41228.28975998662, -1962.92299144307], [50507.33964108981, -6039.49140830009, -140301.41243465967, 180240.40387996248, 37091.10006511298, 88984.31367093371, 762900.9422138353, 782201.843241706, 238279.86744945633], [50528.98182718268, -5694.27054106367, -141363.46245116935, 158393.85140542686, 0.0, 0.0, 0.0, 0.0, 0.0], [148704.8242391365, -892128.3838997425, 3240312.427474793, -6883410.281058616, 8613489.649734871, -6217271.953537799, 2558305.0371063957, -559746.3860342309, 50711.62461298051], [-13685336.940582454, 35976228.093544, -40365539.1731654, 25520327.248154875, -9946017.299531419, 2452389.6120115374, -374220.0602116616, 32349.87298252374, -1214.05964337113]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[i][j+1]))
            poss_res[i] += tmp.mul_no_reduce(x.coerce(scaler[i][j+1]))
        poss_res[i].reduce_after_mul()
        poss_res[i] += poss_res0

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    return sfix.dot_product(cipher_index, poss_res)

@types.vectorize
def neuron120(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-4.199999809265137, -2.0999999046325684, -0.5249999761581421, 0.0, 0.26249998807907104, 1.0499999523162842]
    coeffA = [[-19930326.19769347, -59447537.8134559, -72220967.42074208, -48529762.82218905, -19924257.250840016, -5140189.813474586, -816075.4183746249, -73053.20824509728, -2827.74835028779], [127072.16755161762, -1204273.7521089464, -2935035.885557148, -2745790.0112104737, 1884386.7374087654, 4974515.308038323, 3362420.4952081265, 990617.5235014962, 110513.98572109891], [234940.25860946512, -431641.988743618, -890735.2537002811, -943545.4521499092, 0.0, 0.0, 0.0, 0.0, 0.0], [234940.25860946512, -428677.79166343255, -938063.5415129574, -153750.76201609644, 0.0, 0.0, 0.0, 0.0, 0.0], [237331.7404036547, -472760.5166045314, -565496.9160720361, -1833741.787342727, 3790246.2851010696, -3832435.4660653314, 2236068.941918662, -668155.893344229, 72338.144019641], [-2042433.6635087228, 9293736.903704597, -18137194.265738983, 15986012.975446882, -8335836.897497199, 2656128.2950233608, -508695.4938225956, 53859.25021041099, -2425.21009506991]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[i][j+1]))
            poss_res[i] += tmp.mul_no_reduce(x.coerce(scaler[i][j+1]))
        poss_res[i].reduce_after_mul()
        poss_res[i] += poss_res0

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    return sfix.dot_product(cipher_index, poss_res)

@types.vectorize
def neuron130(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-4.199999809265137, -1.0499999523162842, -0.26249998807907104, 0.0, 0.26249998807907104, 2.0999999046325684]
    coeffA = [[-575514.6312835637, -15122415.79711171, -39685672.95906436, -44076666.75859715, -26441047.375307966, -9268150.62548238, -1903796.6434089958, -212763.87051869335, -10002.54034478668], [693651.6278607955, -672149.5285264258, -1068943.199022229, -4779992.383235401, -18948988.663732737, -25090532.91707925, -14445256.336062549, -3494268.0712211826, -207387.8745446262], [706794.5562565012, -441967.01590498566, 696383.752234118, 2821326.8983819718, 0.0, 0.0, 0.0, 0.0, 0.0], [706794.5562565012, -457150.94504196354, 833110.4225277365, 192302.51827988672, 0.0, 0.0, 0.0, 0.0, 0.0], [668839.9764407923, 80163.94461009199, -2474956.522263544, 11530888.335386291, -21440528.093531113, 19652599.94068118, -9559831.706499835, 2383690.754471391, -240919.7150060302], [12648526.47130323, -31735670.40134007, 35047557.8137656, -21725525.806051906, 8368755.372152229, -2051081.2209681605, 312303.8460063364, -27009.60036704061, 1015.90296323857]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[i][j+1]))
            poss_res[i] += tmp.mul_no_reduce(x.coerce(scaler[i][j+1]))
        poss_res[i].reduce_after_mul()
        poss_res[i] += poss_res0

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    return sfix.dot_product(cipher_index, poss_res)

@types.vectorize
def neuron140(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-4.199999809265137, -3.1499998569488525, -2.0999999046325684, -1.0499999523162842, -0.5249999761581421, -0.26249998807907104, 0.13124999403953552, 1.0499999523162842, 1.5749999284744263]
    coeffA = [[859867212.6231312, 1797513359.9124393, 1644315522.1321552, 859430856.2984313, 280688120.53143466, 58654983.362624764, 7658426.058759587, 571211.303854816, 18632.8911210918], [-5540114835.702766, -16575115016.52953, -21072452075.645836, -14993645060.439291, -6564576639.097378, -1817197230.8747509, -311326846.8827645, -30231219.577397496, -1275428.8734338342], [-1498064735.966816, -8534525123.733503, -20863233546.247566, -28396563142.784027, -23356206716.223892, -11885578048.342396, -3667994238.8649507, -630599209.6903471, -46445676.37943464], [-3615209.288342933, -29883696.627098102, -176119077.55922008, -611299880.5016724, -1282108561.1536255, -1740847229.7017484, -1373037305.485849, -559330186.6499275, -91154182.39272001], [-1224828.2708337002, 2017634.129567865, 10109943.008699568, 9827421.398843916, 12501080.58275703, -14085296.503016913, 66326054.847074255, 126224547.83521892, 51692373.00830483], [-1227887.1152442426, 2100432.9281972456, 10161939.151879761, 3737875.1957745505, 0.0, 0.0, 0.0, 0.0, 0.0], [-1206968.9608501971, 1557599.3787633772, 14624470.409107594, -16042976.885149349, 82689377.44438528, -181806652.2422801, 147121999.2735229, -45798890.860423766, 3352456.0438775057], [-37776550.27560073, 319656132.07411486, -1158943735.3621435, 2391448952.6556454, -2919141477.333287, 2135946577.5805306, -922656341.4180152, 217641338.055972, -21684434.998906497], [204702612.39470658, -507682057.81833285, 544812621.6374153, -331636102.4699591, 125077042.94940516, -29940622.176495023, 4444104.054861865, -374107.61968102347, 13679.61046302063]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[i][j+1]))
            poss_res[i] += tmp.mul_no_reduce(x.coerce(scaler[i][j+1]))
        poss_res[i].reduce_after_mul()
        poss_res[i] += poss_res0

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    return sfix.dot_product(cipher_index, poss_res)

@types.vectorize
def neuron150(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-4.199999809265137, -1.0499999523162842, -0.5249999761581421, 0.0, 0.5249999761581421, 2.0999999046325684]
    coeffA = [[-17522724.158822387, -89104426.86783363, -169424611.83210856, -162980981.56625274, -90021896.58188066, -29893569.23973243, -5909540.424933038, -641777.3021450827, -29507.9021827359], [1634522.4295815788, 209458.6866984385, -1144410.0841794275, 2159253.5879015555, 3913097.240435339, 8214979.895409033, 10508040.184007652, 5727220.809345382, 1109770.9997872957], [1625221.2925251801, 94943.31542017528, -1732747.4594739208, 469970.55689845857, 0.0, 0.0, 0.0, 0.0, 0.0], [1625221.2925251801, 141578.3543072943, -2334431.717758241, 1144099.475134359, 0.0, 0.0, 0.0, 0.0, 0.0], [3174857.264027503, -13987894.709034914, 52313920.29080412, -113681264.82463798, 139285875.8821954, -97617601.88741186, 39267831.951011, -8481676.256600678, 765308.1430263051], [-31931275.547605123, 76320813.3832553, -77303511.24340536, 45761087.28654243, -16853667.817926724, 3955614.916518625, -578063.3131865173, 48106.45901781041, -1745.7718714578]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[i][j+1]))
            poss_res[i] += tmp.mul_no_reduce(x.coerce(scaler[i][j+1]))
        poss_res[i].reduce_after_mul()
        poss_res[i] += poss_res0

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    return sfix.dot_product(cipher_index, poss_res)

@types.vectorize
def neuron160(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-4.199999809265137, -2.0999999046325684, -0.5249999761581421, -0.26249998807907104, 0.0, 0.26249998807907104, 1.0499999523162842, 2.0999999046325684]
    coeffA = [[-264362966.07523197, -764706087.0243995, -960916038.623397, -661725279.872276, -275395986.94125354, -71558860.42381151, -11403628.151545132, -1022842.4577524107, -39633.1880604443], [-10275116.414120987, -101480721.96395971, -415032089.9238533, -917411259.6874403, -1183180669.105795, -890804411.4175558, -385858054.1506037, -89339574.13852938, -8584256.480744954], [583500.1261714532, 2004673.7438393421, 2104706.9364525005, 1591298.5943678569, 2763958.8584113675, -14235448.114211591, -71783842.25911607, -77285327.68764792, -25521753.30102731], [583622.3487882399, 2005241.2034272272, 2034377.4815803755, 578719.7742349727, 0.0, 0.0, 0.0, 0.0, 0.0], [583622.34878824, 2039403.2742980756, 1467352.204966072, 7101482.031530262, 0.0, 0.0, 0.0, 0.0, 0.0], [879924.0206298056, -3081549.9429292753, 39355155.40614393, -147965671.69266993, 376348251.2242931, -546167108.5775223, 465856542.8460727, -201308073.7178623, 33305124.81706652], [1163117467.386722, -6645481749.798838, 16320008733.699696, -22327254706.861736, 18505814311.88285, -9432894690.348536, 2885175724.9500127, -485951617.1645276, 34693853.33179702], [5949992101.818577, -22589531386.951775, 33428312880.744476, -26109835705.21648, 12064527781.206589, -3423469418.0671873, 587853711.2881225, -56194831.05782103, 2299880.9669387634]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[i][j+1]))
            poss_res[i] += tmp.mul_no_reduce(x.coerce(scaler[i][j+1]))
        poss_res[i].reduce_after_mul()
        poss_res[i] += poss_res0

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    return sfix.dot_product(cipher_index, poss_res)

@types.vectorize
def neuron170(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-4.199999809265137, -2.0999999046325684, -0.26249998807907104, -0.13124999403953552, 0.0, 0.13124999403953552, 1.0499999523162842]
    coeffA = [[-78682873.94194187, -194604711.2098354, -203624378.8139552, -118842255.19932997, -42516158.678987846, -9574567.796417879, -1327900.7690660548, -103821.88346462083, -3505.97871781344], [-11423.30677221674, -352458.9348392397, -1434099.052776433, -8289098.001166359, -16754346.689554507, -16542140.912536921, -8712134.819298979, -2348250.609376214, -254871.05621554767], [17585.54544080957, 54122.29062343585, 943545.0349629862, -682610.7424441349, -2174256.1319253263, 332581.1081924251, 1764011.9786127836, -1008064.0395287875, -1944598.8796871547], [17586.56328222996, 55078.81083822647, 988419.9808532048, -108893.5770125448, 0.0, 0.0, 0.0, 0.0, 0.0], [17586.56328222996, 53375.84670695227, 982990.2587535747, -1185851.832019472, 0.0, 0.0, 0.0, 0.0, 0.0], [16922.82439085164, 70803.22211808321, 776750.6719359069, 205890.6157157184, -4713489.571523623, 4743087.211132168, -539336.1225313785, -1170928.7255431209, 426171.7778805909], [-2868670.589481771, 13164291.742353616, -22519635.138152663, 19236384.43517257, -9680759.928885251, 2984953.1906387983, -555681.3535697195, 57442.88204552012, -2535.1743264662]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[i][j+1]))
            poss_res[i] += tmp.mul_no_reduce(x.coerce(scaler[i][j+1]))
        poss_res[i].reduce_after_mul()
        poss_res[i] += poss_res0

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    return sfix.dot_product(cipher_index, poss_res)

@types.vectorize
def neuron180(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-4.199999809265137, -2.0999999046325684, -1.0499999523162842, -0.13124999403953552, 0.0, 0.26249998807907104, 1.0499999523162842, 2.0999999046325684]
    coeffA = [[-69292640.05342874, -183208003.03164148, -209359494.35677302, -134478361.29843733, -53209128.71398657, -13308987.702565268, -2058529.6651103722, -180235.3650466561, -6845.62528781286], [-108099887.35227998, -549836910.1083986, -1055050847.181073, -1047342521.0892861, -593851187.0194881, -192875738.08886752, -32299580.785352003, -1690034.8195746779, 117029.700819295], [-1210209.769845386, -9653051.217861162, 31803733.291915987, -2959144.04776055, -204860483.86538446, -269554104.901047, -103689886.53375474, 14532506.349687805, 12884434.349063797], [-1177878.322902838, -8816569.039482389, 41230729.16026111, 57090299.8347424, 0.0, 0.0, 0.0, 0.0, 0.0], [-1177878.3229028382, -9133568.7087321, 47029652.35707772, -3809279.4258400365, 0.0, 0.0, 0.0, 0.0, 0.0], [-1118757.8877261556, -9860713.710492393, 47515963.50482806, 9361759.140246253, 5424553.246555079, -188747985.6916038, 241236390.8958135, -114841478.66472347, 19495203.58158978], [323662662.7569832, -1839660062.9891353, 4434462504.684958, -5755451613.926818, 4424670753.605901, -2086052751.3106785, 594991559.5396382, -94617830.75338972, 6461082.294171195], [1124820113.9488173, -2854512315.987274, 3112382446.521703, -1909824224.4414904, 723905600.0276426, -173909051.45629752, 25896244.315263525, -2187613.229883537, 80332.56138264106]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0, 1.0, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[i][j+1]))
            poss_res[i] += tmp.mul_no_reduce(x.coerce(scaler[i][j+1]))
        poss_res[i].reduce_after_mul()
        poss_res[i] += poss_res0

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    return sfix.dot_product(cipher_index, poss_res)

neuron_func_dict = {
    "neuron000": neuron000,
    "neuron001": neuron001,
    "neuron002": neuron002,
    "neuron003": neuron003,
    "neuron004": neuron004,
    "neuron005": neuron005,
    "neuron006": neuron006,
    "neuron007": neuron007,
    "neuron008": neuron008,
    "neuron010": neuron010,
    "neuron011": neuron011,
    "neuron012": neuron012,
    "neuron013": neuron013,
    "neuron014": neuron014,
    "neuron015": neuron015,
    "neuron016": neuron016, 
    "neuron017": neuron017,
    "neuron018": neuron018,
    "neuron020": neuron020,
    "neuron021": neuron021,
    "neuron022": neuron022,
    "neuron023": neuron023,
    "neuron024": neuron024,
    "neuron025": neuron025,
    "neuron026": neuron026,
    "neuron027": neuron027,
    "neuron028": neuron028,
    "neuron030": neuron030,
    "neuron031": neuron031,
    "neuron032": neuron032,
    "neuron033": neuron033,
    "neuron034": neuron034,
    "neuron035": neuron035,
    "neuron036": neuron036,
    "neuron037": neuron037,
    "neuron038": neuron038,
    "neuron040": neuron040,
    "neuron041": neuron041,
    "neuron042": neuron042,
    "neuron043": neuron043,
    "neuron044": neuron044,
    "neuron045": neuron045,
    "neuron046": neuron046,
    "neuron047": neuron047,
    "neuron048": neuron048,
    "neuron100": neuron100,
    "neuron110": neuron110,
    "neuron120": neuron120,
    "neuron130": neuron130,
    "neuron140": neuron140,
    "neuron150": neuron150,
    "neuron160": neuron160,
    "neuron170": neuron170,
    "neuron180": neuron180
}

def func14_kan_model_evaluate(x):
    # dim_list required
    input_x = x
    dim_list = [(5, 9), (9, 1)]
    for l in range(len(dim_list)):
        in_dim, out_dim = dim_list[l]
        partial_result = [0]*out_dim
        for i in range(in_dim):
            for j in range(out_dim):
                partial_result[j] += neuron_func_dict[f"neuron{l}{i}{j}"](input_x[i])
        input_x = partial_result
    return input_x

def func14_kan_model_evaluate_vectorized(x):
    dim_list = [(5, 9), (9, 1)]
    input_x = x

    for l in range(len(dim_list)):
        in_dim, out_dim = dim_list[l]
        
        # 1. 创建一个 sfix 矩阵来存储所有中间激活值
        # 矩阵维度是 in_dim x out_dim
        activations = sfix.Matrix(in_dim, out_dim)

        # 2. 并行计算所有激活值
        # 编译器会将这个嵌套循环完全展开，实现最大化的向量化
        for i in range(in_dim):
            for j in range(out_dim):
                activations[i][j] = neuron_func_dict[f"neuron{l}{i}{j}"](input_x[i])
                
        output = sfix.Array(out_dim)

        for j in range(out_dim):
            sum_val = sfix(0)
            for i in range(in_dim):
                sum_val += activations[i][j]
            output[j] = sum_val
            
        input_x = output
        
    return input_x
