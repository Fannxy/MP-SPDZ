from mpc_nonlinear import *

@types.vectorize
def tanh(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-50.0, -6.25, -3.125, -0.78125, 0.0, 0.1953125, 0.78125, 3.125, 12.5]
    coeffA = [[-4194173.072630944, 16.68433970131, 0.86727673568, 0.0183454618, 0.00013652433], [-3608817.0721267513, 445247.40056726034, 126867.3897902733, 16019.69475278112, 755.41149052651], [443310.5643031813, 6149706.701032153, 3217043.811996814, 775435.898513988, 71768.61553282502], [0.0, 4266818.971802611, 429613.84863511875, -693310.0664538674, 0.0], [7e-11, 4194576.231347561, -8890.0752375404, -1339358.640797975, 0.0], [570.1283871191, 4182674.8934939816, 90919.93937296577, -1745585.3274528827, 669002.271183645], [-443310.56430317473, 6149706.701032141, -3217043.81199681, 775435.8985139898, -71768.61553282566], [4045268.042423117, 76088.81124167377, -13754.89484578199, 1054.42721732424, -29.17683277022], [4194279.0022553257, 0.00015393431, -7.02959e-06, 1.3549e-07, -9.4e-10]]
    scaler = [[2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 1.0], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 1.0], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07]]
    
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



@types.vectorize
def soft_plus(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-20.0, -15.625, -13.4375, -11.25, -9.0625, -6.875, -4.6875, -2.5, -0.3125, 0.78125, 6.25]
    coeffA = [[1894.12485723617, 498.50227010433, 52.60849911548, 2.78175703664, 0.07367378168, 0.00078163101], [17010.56952369148, 5374.60596600781, 682.84167575033, 43.5776181072, 1.39614757895, 0.01795566687], [71972.08970430012, 26288.57037034103, 3870.23665982727, 286.76808129166, 10.68466405909, 0.1600256589], [269223.5547728442, 116199.6357356351, 20295.47153762043, 1789.87231032524, 79.58265755789, 1.42538203651], [844978.6653649877, 443144.7235728793, 94791.16553962637, 10302.26052326674, 567.294037992, 12.63207026607], [2024475.733832817, 1327258.077842914, 361408.21705312515, 50725.01646143635, 3647.45411656206, 106.9620525863], [3020534.8379474785, 2379770.718899766, 811208.9193581154, 147929.28490181145, 14269.454457332, 576.34527953783], [2908169.4207072943, 2103180.324957988, 537550.9278678321, 11432.4404777842, -20052.98859349374, -2897.15607595622], [2907352.281155266, 2099678.5381551534, 523209.29083968734, -19394.89645465312, 0.0, 0.0], [2963597.2178164143, 1914549.34446968, 746152.3312524954, -128034.73985113417, 11375.67432435921, -414.52236363691], [45672.40430575876, 4184613.1327571115, 726.14932093014, -25.12695742367, 0.40732878837, -0.00250459975]]
    scaler = [[2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 1.0, 1.0], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07]]
    
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



@types.vectorize
def sigmoid(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-50.0, -14.0625, -12.5, -10.9375, -9.375, -7.8125, -6.25, -4.6875, -3.125, -1.5625, -0.78125, 0.0, 1.5625, 6.25]
    coeffA = [[39.04050317349, 4.89850230114, 0.22266779325, 0.00436140847, 3.110259e-05], [13199.17733475028, 3638.15329161463, 378.25644554402, 17.56859597785, 0.30738283636], [40012.2430064598, 12326.00868600312, 1434.5748829024, 74.68625393269, 1.46627626567], [114348.25963193768, 39901.1878375304, 5273.66859954668, 312.42739652623, 6.99145300912], [303427.7872428325, 121881.79830384481, 18618.32177702964, 1278.92322584934, 33.26887252545], [727105.1401896989, 342780.98272627854, 61881.56516531322, 5050.85981956463, 156.78091982208], [1486077.5898151868, 838271.7159290379, 183552.65378658805, 18368.32181857447, 704.92482957096], [2298433.5619488554, 1535707.1429087692, 409350.0500425329, 51038.18841377141, 2487.03093801351], [2265248.6629461953, 1433866.8538834178, 329931.63513002236, 27075.5667369432, -37.69601574701], [2099587.2578837527, 1055889.181417289, 2524.40417547048, -100956.99990221234, -19163.74408082196], [2097139.5017196543, 1049670.1684311929, 8264.29721557035, -73582.34760637266, 0.0], [2097139.5017196543, 1066704.742950652, -53701.73107938899, -43331.87915336693, 0.0], [1875484.219568071, 1537426.6752580297, -402130.4764995988, 48464.74365712389, -2242.76923540077], [4166939.6392281144, 4302.39617763188, -223.54909378416, 4.72754763382, -0.03517618631]]
    scaler = [[2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 1.0], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 1.0], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07]]
    
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



@types.vectorize
def elu(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-50.0, -15.0, -6.25, -4.0625, -1.875, -0.78125, 0.0006103515625]
    coeffA = [[-4194271.187065585, 0.6748873599, 0.01834870165, 0.00015955008], [-4106988.741624766, 22268.20921643523, 1849.10976216361, 50.16756652301], [-3088279.8165694713, 511031.7876112814, 80778.67337369535, 4339.18189448651], [-1259837.50422231, 1960090.7000926142, 466169.71244532976, 38674.70724333341], [-155039.09821308983, 3632318.4138106937, 1325100.361010493, 188717.18016915815], [6.24117069782, 4182831.6873808536, 2001476.0606318028, 477670.77184647287], [-1.86e-09, 4194279.0034393077, 1.7e-10, -0.0]]
    scaler = [[2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07]]
    
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



@types.vectorize
def selu(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-50.0, -15.0, -6.25, -4.0625, -2.96875, -1.875, -0.78125, 0.0006103515625]
    coeffA = [[-7373945.31140335, 1.18651900634, 0.03225883984, 0.00028050488], [-7220494.103643818, 39149.72342543688, 3250.91861084873, 88.19956446491], [-5429502.637769774, 898444.6370217857, 142016.93052709778, 7628.7127272183], [-3369490.435327218, 2394409.410392051, 505669.98969854985, 37225.08214847879], [-1576803.2166885303, 4244866.525322428, 1144994.7150078525, 111133.56712792422], [-272574.1327547517, 6385976.524274871, 2329658.04031578, 331783.54565652227], [-1791.01473871581, 7339202.948399305, 3487231.8133979393, 819585.1594297808], [-3.73e-09, 4406933.143192683, 2.7e-10, -1e-11]]
    scaler = [[2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07]]
    
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



@types.vectorize
def gelu(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-20.0, -3.75, -2.5, -1.25, 0.0, 0.3125, 1.25, 2.5, 5.0]
    coeffA = [[-2846.29456290974, -685.23146359561, -50.0054887914, -1.14298260094], [-1916307.361618036, -1581903.5338090858, -437553.98210765066, -40511.57103758872], [-1203980.5555027295, -383499.9956227352, 188181.32542370155, 63626.90145651568], [0.0, 2146329.5646905424, 1950968.8688592135, 471204.06202182453], [1e-11, 2095601.9893701745, 1704585.4234277843, -170739.15500447794], [17204.83322366532, 1960869.5620745495, 2068055.4170300204, -517951.05409748835], [-1203980.555502751, 4577778.999062077, 188181.325423685, -63626.901456513], [-1099094.957902926, 4986962.37709154, -188109.03522665496, 14707.22407252014], [-4.31966047903, 4194279.978923079, -0.06835506716, 0.00151900149]]
    scaler = [[2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07]]
    
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


def soft_sign(x):
    pos_flag = x > 0
    x = (pos_flag * x) + (1 - pos_flag) * (-x)
    return x * mpc_reciprocal(1 + x)


def isru(x):
    """Inverse Square Root Unit.
    """
    return x * mpc_reciprocal(mpc_sqrt(1 + ALPHA1 * x**2))



@types.vectorize
def snormal_dis(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [-10.0, -6.25, -5.0, -3.75, -2.5, -0.625, 0.0, 0.625, 2.5, 3.75, 5.0, 6.25]
    coeffA = [[331.03480203434, 282.83330236082, 103.2218734542, 20.8591591703, 2.52073411727, 0.18216398527, 0.0072892399, 0.00012459125], [1016735.8092646737, 1204986.081093367, 612714.0125857604, 173254.4375527027, 29419.43789307512, 2999.58210646753, 170.0185946801, 4.13235111648], [8359191.832661943, 11700770.825925717, 7062739.246839453, 2382021.957825643, 484577.8140615008, 59434.9181490288, 4067.99311153252, 119.81407808661], [477938.4745855105, -4071940.9306818643, -6490229.555362781, -4099689.298635237, -1378739.5931772164, -262526.5588669827, -26890.80291443462, -1158.03871038332], [1694030.4030138745, 142001.35798397186, -426512.01412515657, 650964.4214264076, 824619.0954110107, 345009.8026994192, 65574.34709759937, 4845.02930330942], [1673275.2445434276, -7935.21093366442, -918882.8872440088, -233892.0379649443, 0.0, 0.0, 0.0, 0.0], [1673275.2445434276, 7935.21093366557, -918882.887244016, 233892.0379649529, 0.0, 0.0, 0.0, 0.0], [1694030.40301464, -142001.3579884378, -426512.01411454537, -650964.4214397267, 824619.0954205763, -345009.8027033676, 65574.34709847107, -4845.0293033892], [477938.48932427465, 4071940.896813153, -6490229.522138587, 4099689.2806017506, -1378739.5873286966, 262526.5577337911, -26890.80279298889, 1158.03870483019], [8359192.127046376, -11700771.290690018, 7062739.560403999, -2382022.0750103216, 484577.84025870153, -59434.92165205342, 4067.99337093439, -119.81408629198], [1016735.793157187, -1204986.0678020075, 612714.0091746122, -173254.43765093136, 29419.43811053068, -2999.58215123504, 170.01859862164, -4.13235124947], [331.0348019478, -282.83330229324, 103.22187343228, -20.85915916653, 2.5207341169, -0.18216398525, 0.0072892399, -0.00012459125]]
    scaler = [[2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 1.0, 1.0, 1.0, 1.0], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 1.0, 1.0, 1.0, 1.0], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07]]
    
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


def scauchy_dis(x):
    """https://www.itl.nist.gov/div898/handbook/eda/section3/eda3663.htm
    """
    return 1 * mpc_reciprocal((PAI * (1 + x**2)))



@types.vectorize
def gamma_dis(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [1e-06, 1.7450580447912214e-06, 2.490116089582443e-06, 3.980232179164886e-06, 6.960464358329773e-06, 1.2920928716659545e-05, 2.484185743331909e-05, 4.868371486663818e-05, 9.636742973327637e-05, 0.00019173485946655274, 0.00038246971893310546, 0.0007639394378662109, 0.0030527577514648436, 0.012208031005859375, 0.048829124023437497, 0.19531349609374998, 0.781250984375, 1.56250096875, 3.1250009375, 4.6875009062499995, 6.250000875, 7.81250084375, 9.3750008125, 10.93750078125, 12.50000075, 14.062500718749998, 15.625000687499998]
    coeffA = [[1018.09213015625, 1536576226.6643891, -188366061843360.62, 2251799813685248.0, 0.0], [1280.28437994181, 1226796097.5668669, -96946937598522.47, 2251799813685248.0, 0.0], [1572.47838452603, 996836253.9848976, -51720800386984.26, 2251799813685248.0, 0.0], [2031.86401855856, 769945076.9148647, -23713795578333.02, 2251799813685248.0, 0.0], [2724.59912581678, 573457866.0168536, -9783267647694.781, 2251799813685248.0, 0.0], [3732.9461455438, 418774225.2159852, -3851510161609.4946, 2251799813685248.0, 0.0], [5118.91023882657, 307589428.98777443, -1621672382887.4348, 2251799813685248.0, 0.0], [6557.70935712717, 247093528.98349407, -986102814793.6405, 2251799813685248.0, 0.0], [8605.58390153626, 189426208.29068333, -452123700474.67224, 632107589048141.4, 0.0], [12146.5415122771, 134190909.33720367, -160790075329.25177, 112784093398543.7, 0.0], [17161.79008557367, 94963128.00450906, -57036402493.92954, 20034779723352.086, 0.0], [25135.05971478719, 65336366.7871133, -19767122574.687077, 4453706503244.261, -422995523529626.44], [50288.09531112885, 32611004.329444617, -2488129853.462147, 139846251058.90067, -3320042214535.9805], [100840.31616099816, 16172663.88419545, -318595463.7723025, 4435212929.162645, -26263440271.653297], [203922.423077235, 7813631.231947995, -43382961.60480171, 147580902.1215608, -216074814.85129198], [428693.14133342734, 3313164.925291549, -6739326.1916817995, 5993850.713961597, -2158916.5737013547], [842389.8643957814, 955788.7366587785, -1507126.2664406751, 694669.7206262839, -115133.79050361452], [1448509.9958317257, -579643.1381818211, -17645.18312313009, 39495.21398652404, -5099.38817966558], [1786429.234080426, -1084428.0002848343, 264611.88981233013, -30469.97836414127, 1383.79942420181], [1381878.8097941175, -743786.9142392682, 156527.42624464803, -15151.70973200181, 565.57883732142], [805781.64640427, -370332.41117463657, 65450.0813786443, -5248.76817780601, 160.56960968238], [390367.20542117464, -154457.72537065446, 23297.3065681282, -1583.42057311523, 40.82611459077], [166128.04294720644, -57412.12661776653, 7526.14145307331, -442.79132467528, 9.85101044306], [64270.57101136386, -19668.8151667197, 2276.30509821549, -117.93970892654, 2.30601190375], [23151.6189496558, -6347.73119810643, 656.81716523685, -30.37368411521, 0.52928997443], [7860.73742435953, -1951.10934543808, 182.51613770693, -7.62176695986, 0.11982299901], [23.62352923613, -2.88514489422, 0.12853298569, -0.00246995199, 1.728724e-05]]
    scaler = [[2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 1.0], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 1.0], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 1.0], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 1.0], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 1.0], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 1.0], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 1.0], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 1.0], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 1.0], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 1.0], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 1.0], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07]]
    
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



@types.vectorize
def chi_square(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [0.0, 0.46875, 3.75, 7.5, 15.0, 22.5]
    coeffA = [[5e-11, 1092435.6671879266, -541075.2836601372, 116921.37732871455, 0.0, 0.0, 0.0], [345.75604404886, 1090911.4680624616, -542334.1798309321, 132192.41753900636, -20076.9262514612, 1885.10717508527, -84.49432284769], [211164.5007638152, 791043.0082889112, -358109.4973974007, 68971.71724962149, -7192.37029473695, 402.52909021413, -9.55233099608], [1762315.1085170861, -390242.3761491093, 26398.04519514483, 460.06483293108, -149.92380781477, 7.3368609086, -0.12057530159], [1705956.8891508654, -440467.9639936565, 48473.28113461802, -2899.76929537908, 99.13799945903, -1.83156605268, 0.01425262613], [439729.22793516814, -89228.77004822598, 7614.19513276209, -349.25856070975, 9.0715463201, -0.12637552994, 0.0007370676]]
    scaler = [[2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 1.0, 1.0, 1.0], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07]]
    
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



@types.vectorize
def sexp_dis(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [0.0, 0.625, 2.5, 5.0, 7.5]
    coeffA = [[4194279.0034393086, -4188015.40340937, 2032363.5441380604, -514562.51801293145, 0.0, 0.0], [4182306.912914592, -4134143.080131629, 1975884.1921842482, -571126.7171068311, 97638.46337939336, -7598.95601638222], [3553111.111434528, -2963087.389371894, 1070877.4344022807, -206355.54200917657, 20886.11601769146, -877.03326557364], [1787780.9462581328, -1121553.5036719583, 290483.1973959177, -38582.5170785156, 2614.32773463139, -71.99127440061], [584378.6269254918, -285232.8904193843, 56567.89195629852, -5682.35447476774, 288.46463423554, -5.90940365977]]
    scaler = [[2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 1.0, 1.0], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07]]
    
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



@types.vectorize
def slog_dis(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [0.0001, 0.0013207000732421874, 0.002541400146484375, 0.00498280029296875, 0.0098656005859375, 0.019631201171875, 0.0782248046875, 0.31259921875, 0.6250984375, 1.250096875, 2.50009375, 5.0000875, 7.500081250000001, 10.000075, 15.000062500000002, 20.00005, 30.000025]
    coeffA = [[-0.02459122122, 320.74795375661, -807927.7641031268, 595709836.704581, 0.0, 0.0], [-0.07949862737, -362.70216737733, 1384734.6661831636, -1594840701.3165936, 716278442048.0255, 0.0], [-1.82626269341, 564.446047639, 2589351.8772282084, -2847813799.364955, 1126358225030.726, -46500449444576.45], [-193.29772568628, 168808.56904080888, -57529942.69456613, 8110294911.208181, 104696253393.51854, -7457270990729.54], [-897.4276326674, 540138.4737227306, -137012007.9448041, 16735640953.756884, -369286632919.43256, 3078063575133.5435], [36516.71206390907, -6183956.879051516, 353569819.26973516, -1721149132.8565352, -5851617517.129607, 54247735065.525955], [-474417.4140013758, 14212197.217270914, 73083255.96330647, -648805318.1762851, 1676091052.6065054, -1532134252.7771869], [-1059722.9426210881, 30968121.55671164, -95322578.06828417, 143564202.21077386, -113118854.80587624, 37203710.10022292], [2083328.2200729633, 6626001.108766764, -18003570.269079514, 17681893.836339492, -8234684.278864408, 1520341.4730176055], [4752582.524529724, -4961797.905622794, 2479175.3432778483, -690963.0506304469, 102528.69040363713, -6264.87758673702], [3597258.022530166, -2979906.6856354894, 1121236.5766157524, -227793.37785527244, 24268.70438025346, -1065.84286909527], [1717608.2950587263, -945740.3995150056, 227656.75644853013, -28993.3319208319, 1916.92091422938, -52.02761520839], [874448.7667292648, -359469.6857280532, 63568.28548109277, -5895.57419015917, 282.52852064954, -5.54480795472], [385791.14485051186, -116409.29455725956, 14885.54258668259, -988.58366295499, 33.69255212264, -0.4678363835], [145966.4121016853, -32177.75675473314, 2981.92986279658, -142.93407615527, 3.50931766379, -0.03508126599], [48648.47578531306, -7757.05873496464, 515.00219776972, -17.56814460267, 0.30543312922, -0.00215341755], [13881.71124188027, -1600.50451393966, 76.51564223096, -1.8760235402, 0.02342901669, -0.00011868091]]
    scaler = [[2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 1.0, 1.0], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 1.0], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07]]
    
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



@types.vectorize
def bs_dis(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    
    breaks = [1e-06, 0.11718849609375, 0.14648537011718749, 0.175782244140625, 0.2343759921875, 0.35156348828125, 0.468750984375, 0.93750096875, 1.8750009375, 2.81250090625, 4.68750084375, 5.6250008125, 6.56250078125, 7.50000075, 8.43750071875, 9.3750006875]
    coeffA = [[-3.76986e-06, 3.76997266924, -115.99778441945, 881.63385732906, 0.0], [1081.44890308131, -36372.48014037528, 461274.51736970973, -2616752.4729524194, 5608821.475496719], [4817.51037592144, -137931.29789547363, 1498457.144980657, -7333208.442629924, 13666526.340092681], [4797.06130800926, -145068.96214311194, 1621486.9305696506, -8025651.552925049, 14959637.724940857], [-85176.58203202933, 1296860.8576165247, -7073896.941815233, 15370559.459322885, -8750136.53904917], [-79897.84277248883, 1381235.0013897996, -8061140.730865777, 18458362.055621576, -11832908.981557794], [874247.8028074881, -6070636.939251488, 13928023.825389998, -10630103.41818287, 2735004.8809206644], [-2397655.1623390843, 6371109.203315468, -3894705.651696122, 780539.6723229192, -22110.39378052662], [-1030190.6678381236, 4530994.105566386, -3335986.7595848385, 928673.8130784504, -91527.17236933637], [4257788.857672036, -3189640.986255052, 919937.1149759737, -120618.59282083157, 6046.20365687008], [2381634.2808185974, -1567866.4819735219, 393038.3705952084, -44368.47793519608, 1899.3972985277], [1044741.7189867033, -605749.5131040326, 133028.75991767427, -13096.67313971696, 487.13375784582], [383180.03853790805, -197217.47375171032, 38331.14053324113, -3331.40585591514, 109.15896031321], [124314.96427032384, -57351.40960067204, 9972.37297896834, -774.13193496283, 22.62474446329], [36712.3631664074, -15329.99637952191, 2409.85553785589, -168.95208101877, 4.45568232193], [73.23007112139, -14.77194594175, 1.06700637475, -0.03296802735, 0.00037007322]]
    scaler = [[2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 1.0], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07], [2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07, 2.3842e-07]]
    
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

