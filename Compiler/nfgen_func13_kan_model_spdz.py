from Compiler import types
from Compiler.library import for_range_opt
from Compiler.types import Array, floatingpoint, regint, sfix

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
    
    breaks = [-4.199999809265137, -2.0999999046325684, -1.0499999523162842, -0.7874999642372131, -0.26249998807907104, -0.13124999403953552, 2.0999999046325684]
    coeffA = [[-23796858.903247528, -35188824.93766592, -20672458.476391494, -6032691.056304159, -874547.6934496904, -50387.37078936057], [-24401728.15051753, -90330313.5222751, -126089216.52067278, -82610149.03963725, -25756345.69024533, -3096724.9475123635], [3827611.2203954286, 23432719.534423515, 56330130.20881416, 62719122.66812166, 31675179.735180058, 5888020.04122026], [-66215.21125635918, -758866.8418636606, -4054325.856843373, -12979304.972902773, -15983078.001987124, -6165918.705175538], [-10474.31329177162, 11589.82233164364, 200758.0150774764, -1147511.9780267607, 748148.2303697936, 3563765.522562291], [-6389.72073935785, -3592.29728471551, 3354.83388897187, -463.97230571293, 0.0, 0.0], [-13145213.006224422, 20115732.455784336, -11887181.834145896, 3403264.0385550824, -476508.89097560494, 26218.14386417001]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    pre_muls = floatingpoint.PreOpL(lambda a, b, _: a * b, [x] * degree)

    poss_res = [0] * m
    for i in range(m):
        poss_res[i] = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res[i] += coeffA[i][j + 1] * pre_muls[j] * scaler[i][j + 1]

    comp = sfix.Array(m)
    for i in range(m):
        comp[i] = x >= breaks[i]

    cipher_index = Array(m, sfix)
    @for_range_opt(m - 1)
    def _(i):
        cipher_index[i] = comp[i + regint(1)]
        cipher_index[i] = comp[i] * (comp[i] - cipher_index[i])

    cipher_index[m - 1] = comp[m - 1]

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
    
    breaks = [-4.199999809265137, -2.0999999046325684, 0.0, 2.0999999046325684]
    coeffA = [[-7072336.015771392, -10479119.62737347, -6164184.178305724, -1800680.2511065884, -261270.14599195073, -15064.94948369828], [-199036.10776721267, -374648.48677337216, -516306.9721924788, -178070.47561444764, 0.0, 0.0], [-199036.10776721267, -5491.6773925661, 3196.20246342771, -330.22869978726, 0.0, 0.0], [13863587.424215907, -22821883.206375197, 14360750.05086185, -4389403.434224648, 655858.4713618796, -38515.40341707552]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    pre_muls = floatingpoint.PreOpL(lambda a, b, _: a * b, [x] * degree)

    poss_res = [0] * m
    for i in range(m):
        poss_res[i] = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res[i] += coeffA[i][j + 1] * pre_muls[j] * scaler[i][j + 1]

    comp = sfix.Array(m)
    for i in range(m):
        comp[i] = x >= breaks[i]

    cipher_index = Array(m, sfix)
    @for_range_opt(m - 1)
    def _(i):
        cipher_index[i] = comp[i + regint(1)]
        cipher_index[i] = comp[i] * (comp[i] - cipher_index[i])

    cipher_index[m - 1] = comp[m - 1]

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
    
    breaks = [-4.199999809265137, -3.1499998569488525, -2.0999999046325684, -1.5749999284744263, -1.0499999523162842, 0.0, 2.0999999046325684]
    coeffA = [[91722.4743823934, 62968.00834144936, 24799.12097534213, 6312.57505243085, 885.29037640609, 50.47283391896], [-2274720.0555422427, -4862269.260299936, -3934858.3631816767, -1546393.887379363, -297937.74568879965, -22621.38922075141], [399693.28631799977, 4820313.040245128, 8327922.032295037, 5697434.447199892, 1753340.9443926378, 203333.623665918], [1462367.522754741, 5329965.544634851, 5240886.987767229, 1288446.98733647, -453788.099406675, -183957.010512939], [-175517.46557814837, -37236.03040296225, -552245.818307867, -501814.04543909326, 0.0, 0.0], [-175517.46557814837, 3171.41036579932, -1217.00350821146, -164.46996482944, 0.0, 0.0], [-7441846.292402725, 11287300.399972443, -6751338.295488021, 1956063.7955623819, -278619.2902683992, 15662.6562336762]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    pre_muls = floatingpoint.PreOpL(lambda a, b, _: a * b, [x] * degree)

    poss_res = [0] * m
    for i in range(m):
        poss_res[i] = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res[i] += coeffA[i][j + 1] * pre_muls[j] * scaler[i][j + 1]

    comp = sfix.Array(m)
    for i in range(m):
        comp[i] = x >= breaks[i]

    cipher_index = Array(m, sfix)
    @for_range_opt(m - 1)
    def _(i):
        cipher_index[i] = comp[i + regint(1)]
        cipher_index[i] = comp[i] * (comp[i] - cipher_index[i])

    cipher_index[m - 1] = comp[m - 1]

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
    
    breaks = [-4.199999809265137, -3.1499998569488525, -2.625, -2.0999999046325684, 0.0, 2.0999999046325684]
    coeffA = [[-228630.8540804383, -384567.5326993664, -215111.11545200317, -57054.40678628218, -7434.3427057774, -385.24300619659], [-12206057.642160334, -19679549.41984676, -12668776.155740919, -4082368.838329896, -658940.9481052706, -42623.87761785524], [8109926.960481664, 20957735.79725666, 19839765.0913653, 8918654.471776567, 1940462.090868969, 165241.57499465873], [-208708.1094674928, -537801.0828733632, -667054.0291970636, -216724.85609969645, 0.0, 0.0], [-208708.1094674928, -21490.71283558223, 15717.68379246822, -3330.47947669587, 0.0, 0.0], [-14710256.109264141, 22273323.336530466, -13196119.255264986, 3788484.9131612773, -533690.3301326135, 29624.63375357714]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    pre_muls = floatingpoint.PreOpL(lambda a, b, _: a * b, [x] * degree)

    poss_res = [0] * m
    for i in range(m):
        poss_res[i] = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res[i] += coeffA[i][j + 1] * pre_muls[j] * scaler[i][j + 1]

    comp = sfix.Array(m)
    for i in range(m):
        comp[i] = x >= breaks[i]

    cipher_index = Array(m, sfix)
    @for_range_opt(m - 1)
    def _(i):
        cipher_index[i] = comp[i + regint(1)]
        cipher_index[i] = comp[i] * (comp[i] - cipher_index[i])

    cipher_index[m - 1] = comp[m - 1]

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
    
    breaks = [-4.199999809265137, -1.0499999523162842, -0.5249999761581421, 0.0, 1.0499999523162842, 2.0999999046325684, 3.1499998569488525]
    coeffA = [[1912718.9719677817, 4618970.362100124, 3850972.1811580276, 1476798.87866336, 267323.92112114653, 18531.86381463043], [132886.1105230593, 546464.8045680746, 1657043.2425941876, 2647242.4391948353, 1661519.5424161602, 345426.88493309106], [62218.61704372639, 1152.34940553745, -5382.15862010084, 193724.37549051532, 0.0, 0.0], [62218.61704372639, -1917.12671668589, 3219.57551486106, -1448.67642513177, 0.0, 0.0], [-473364.58678455546, 1902545.5840383063, -2662004.290047276, 1833139.2844851415, -621506.6163420065, 83043.55470486452], [-36147280.56440154, 72378350.69672981, -57053765.94083281, 22131577.095146403, -4220967.638283944, 317152.3452850969], [-29942270.683955282, 38323541.31918448, -19542456.829509616, 4993516.96245276, -637784.9775829386, 32570.75930417645]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    pre_muls = floatingpoint.PreOpL(lambda a, b, _: a * b, [x] * degree)

    poss_res = [0] * m
    for i in range(m):
        poss_res[i] = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res[i] += coeffA[i][j + 1] * pre_muls[j] * scaler[i][j + 1]

    comp = sfix.Array(m)
    for i in range(m):
        comp[i] = x >= breaks[i]

    cipher_index = Array(m, sfix)
    @for_range_opt(m - 1)
    def _(i):
        cipher_index[i] = comp[i + regint(1)]
        cipher_index[i] = comp[i] * (comp[i] - cipher_index[i])

    cipher_index[m - 1] = comp[m - 1]

    return sfix.dot_product(cipher_index, poss_res)


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
    
    breaks = [-4.199999809265137, -2.0999999046325684, -1.0499999523162842, -0.5249999761581421, 0.0, 0.13124999403953552, 2.0999999046325684]
    coeffA = [[17336028.172787085, 26422292.96779516, 15564216.810764337, 4521025.468258041, 651469.6675967266, 37321.31498353324], [30153465.513348352, 122619505.12587088, 173232155.16327074, 113203327.22263727, 35158833.990322195, 4217305.489803573], [-1350333.666841081, -4243401.765406883, -28043328.807548955, -42968575.2998978, -23401266.812544193, -4084654.048843117], [-166559.68685557222, 4745948.091174219, -1424179.950633468, -5539315.788252692, 0.0, 0.0], [-166559.68685557222, 4794790.319481473, -850248.4159240148, -2029970.5146789157, 0.0, 0.0], [-180132.85964582703, 5012489.736281039, -2019896.842178308, 243012.37990153843, 34564.08194723384, -7529.44141003045], [-57378377.65487586, 104245657.98575464, -69064663.84153886, 22231207.65667817, -3466186.7688463796, 211032.49212955468]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    pre_muls = floatingpoint.PreOpL(lambda a, b, _: a * b, [x] * degree)

    poss_res = [0] * m
    for i in range(m):
        poss_res[i] = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res[i] += coeffA[i][j + 1] * pre_muls[j] * scaler[i][j + 1]

    comp = sfix.Array(m)
    for i in range(m):
        comp[i] = x >= breaks[i]

    cipher_index = Array(m, sfix)
    @for_range_opt(m - 1)
    def _(i):
        cipher_index[i] = comp[i + regint(1)]
        cipher_index[i] = comp[i] * (comp[i] - cipher_index[i])

    cipher_index[m - 1] = comp[m - 1]

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
    
    breaks = [-4.199999809265137, -3.1499998569488525, -2.0999999046325684, -1.5749999284744263, -1.0499999523162842, -0.5249999761581421, 2.625, 3.1499998569488525]
    coeffA = [[138603.968125985, 193249.9623275475, 103544.83252379845, 27348.26146626526, 3591.03946732622, 188.09787073011], [6768365.653261141, 10562402.475240206, 6567295.915367569, 2033229.989068826, 313203.7619043803, 19183.43220625698], [-8685719.936769301, -22572964.24467161, -21697579.45348494, -9939018.817893863, -2199856.303197653, -189360.94771085813], [2105262.121551831, 9727640.085489696, 16950874.738180418, 13161263.686098602, 4694913.56021858, 632406.7811811578], [-164477.4050993829, -439546.4481074176, -1376735.3551547998, -3470069.971127577, -2907746.8018403244, -769021.7190766447], [-93268.04905692975, -132303.91619013224, 77639.63830390674, -7832.17579978618, 0.0, 0.0], [23709755.92574104, -33228153.549774222, 17033014.511817597, -3781433.9352742005, 299027.3597299338, 2398.28708960804], [-36042553.24746671, 46140860.26644919, -23604392.01287333, 6037974.414887138, -771943.6450876193, 39459.10659061829]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    pre_muls = floatingpoint.PreOpL(lambda a, b, _: a * b, [x] * degree)

    poss_res = [0] * m
    for i in range(m):
        poss_res[i] = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res[i] += coeffA[i][j + 1] * pre_muls[j] * scaler[i][j + 1]

    comp = sfix.Array(m)
    for i in range(m):
        comp[i] = x >= breaks[i]

    cipher_index = Array(m, sfix)
    @for_range_opt(m - 1)
    def _(i):
        cipher_index[i] = comp[i + regint(1)]
        cipher_index[i] = comp[i] * (comp[i] - cipher_index[i])

    cipher_index[m - 1] = comp[m - 1]

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
    
    breaks = [-4.199999809265137, -3.1499998569488525, -2.0999999046325684, -1.0499999523162842, -0.5249999761581421, 0.0, 2.0999999046325684]
    coeffA = [[239085.46072479253, 112402.958460894, 29806.09789088433, 7066.41541782958, 1120.0923994109, 72.64286272752], [7140118.212126906, 10596696.072398782, 6339830.248728534, 1882860.4359968912, 275568.7646717377, 15802.04621263108], [653182.1773730305, 6267617.168472952, 13655673.674093183, 11308326.722831959, 4074447.335895114, 541223.0930743762], [-514398.4244213296, -487661.1491711355, -978368.9563570272, -3934097.991571362, -3672316.641935157, -1010000.8284773871], [-479480.1512662462, -110303.69039395855, 745451.5337417433, -128833.25563898, 0.0, 0.0], [-479480.15126624634, -29411.43984666384, 27792.84754995247, -8548.41466557476, 0.0, 0.0], [-38152490.416733526, 59529777.598113105, -36338756.815686256, 10762689.59306102, -1565402.447615432, 89783.90737002502]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    pre_muls = floatingpoint.PreOpL(lambda a, b, _: a * b, [x] * degree)

    poss_res = [0] * m
    for i in range(m):
        poss_res[i] = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res[i] += coeffA[i][j + 1] * pre_muls[j] * scaler[i][j + 1]

    comp = sfix.Array(m)
    for i in range(m):
        comp[i] = x >= breaks[i]

    cipher_index = Array(m, sfix)
    @for_range_opt(m - 1)
    def _(i):
        cipher_index[i] = comp[i + regint(1)]
        cipher_index[i] = comp[i] * (comp[i] - cipher_index[i])

    cipher_index[m - 1] = comp[m - 1]

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
    
    breaks = [-4.199999809265137, -3.1499998569488525, -2.0999999046325684, -1.0499999523162842, -0.5249999761581421, 2.0999999046325684]
    coeffA = [[-108110.28978336605, -223094.63748920587, -129497.36714999109, -34466.35847031394, -4462.68775839375, -229.17538606019], [-2482218.8783371486, -3144677.9379862086, -1376052.941961388, -212198.53344338475, 6270.15288131008, 3226.78243912693], [-4044483.0939100324, -14818998.55247638, -20512078.244499993, -13405451.091958921, -4182250.674432522, -503913.5274408345], [-31614.39862707572, 1110615.6706138253, 4301361.811666913, 5369512.001994793, 2597608.8443170413, 397287.60591510567], [-191902.3185359887, -194524.32300656423, 206354.78016297627, -57243.6675146292, 0.0, 0.0], [-11833753.0182228, 18650745.203475595, -11555277.8938401, 3472534.99091109, -512850.6249284376, 29878.66542381922]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    pre_muls = floatingpoint.PreOpL(lambda a, b, _: a * b, [x] * degree)

    poss_res = [0] * m
    for i in range(m):
        poss_res[i] = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res[i] += coeffA[i][j + 1] * pre_muls[j] * scaler[i][j + 1]

    comp = sfix.Array(m)
    for i in range(m):
        comp[i] = x >= breaks[i]

    cipher_index = Array(m, sfix)
    @for_range_opt(m - 1)
    def _(i):
        cipher_index[i] = comp[i + regint(1)]
        cipher_index[i] = comp[i] * (comp[i] - cipher_index[i])

    cipher_index[m - 1] = comp[m - 1]

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
    
    breaks = [-4.199999809265137, -1.0499999523162842, -0.5249999761581421, -0.26249998807907104, 0.0, 0.5249999761581421, 1.0499999523162842, 1.5749999284744263, 2.0999999046325684, 2.625, 3.1499998569488525]
    coeffA = [[6609825.519271175, 15717420.778426362, 13063291.639100708, 5002807.632498056, 904614.3068477908, 62649.65676429111], [362076.6225647852, 2106146.59997968, 7099956.686656442, 10650519.110290825, 6333101.494467914, 1261397.9377949224], [77702.83134807133, -115074.16978253517, 151359.00974263478, -258682.06862277343, -2287947.214379471, -1491055.0607103005], [78286.25511164921, -99913.44854393703, 334250.4611859991, 748125.798568647, 0.0, 0.0], [78286.25511164921, -108904.68840169784, 343962.27642182424, -314394.7641510715, 0.0, 0.0], [33149.57004520422, 139703.85307418494, -30958.27935144277, -422371.148365106, 544834.0038181181, -195853.25185658527], [1488592.166902636, -5545951.810277565, 8483993.582205107, -6353021.13515568, 2330202.2378855078, -335239.5275836134], [-7401156.84113234, 22263741.806885432, -26273287.79316025, 15338240.654955184, -4428141.991704249, 505610.12429356907], [9242689.777625626, -25833284.926460527, 27531361.122749746, -14072014.121687245, 3474782.236624845, -332936.3121532904], [2659186.753973777, 5219305.988910919, -10302214.95462311, 5778747.794344223, -1351621.0325087097, 115326.66159748253], [-28624714.885261495, 36544649.154591225, -18602553.169718448, 4742577.179678707, -604363.472877293, 30794.83147430518]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    pre_muls = floatingpoint.PreOpL(lambda a, b, _: a * b, [x] * degree)

    poss_res = [0] * m
    for i in range(m):
        poss_res[i] = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res[i] += coeffA[i][j + 1] * pre_muls[j] * scaler[i][j + 1]

    comp = sfix.Array(m)
    for i in range(m):
        comp[i] = x >= breaks[i]

    cipher_index = Array(m, sfix)
    @for_range_opt(m - 1)
    def _(i):
        cipher_index[i] = comp[i + regint(1)]
        cipher_index[i] = comp[i] * (comp[i] - cipher_index[i])

    cipher_index[m - 1] = comp[m - 1]

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
    
    breaks = [-4.199999809265137, -2.0999999046325684, 0.0, 2.0999999046325684, 3.1499998569488525]
    coeffA = [[-5012441.11270074, -7420843.201399889, -4372080.368301955, -1279843.0278403184, -186079.78463624715, -10749.38824034634], [-73995.72599187437, -154427.43124214973, -327942.55258137494, -125161.84913634388, 0.0, 0.0], [-73995.72599187437, -1248.99173862793, -143.26460292567, 434.09729362275, 0.0, 0.0], [-28476318.01781968, 57010880.9784728, -45148076.63937326, 17601182.6594901, -3374582.6225975887, 254840.01024474963], [-27019534.09749234, 34586128.00614598, -17685747.18347442, 4523095.839300058, -578161.7988353982, 29548.32936137916]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    pre_muls = floatingpoint.PreOpL(lambda a, b, _: a * b, [x] * degree)

    poss_res = [0] * m
    for i in range(m):
        poss_res[i] = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res[i] += coeffA[i][j + 1] * pre_muls[j] * scaler[i][j + 1]

    comp = sfix.Array(m)
    for i in range(m):
        comp[i] = x >= breaks[i]

    cipher_index = Array(m, sfix)
    @for_range_opt(m - 1)
    def _(i):
        cipher_index[i] = comp[i + regint(1)]
        cipher_index[i] = comp[i] * (comp[i] - cipher_index[i])

    cipher_index[m - 1] = comp[m - 1]

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
    
    breaks = [-4.199999809265137, -2.0999999046325684, -1.0499999523162842, -0.5249999761581421, 2.0999999046325684]
    coeffA = [[834160.5097387193, 1021163.6595721124, 580709.1710809777, 172359.92832152708, 25662.22688320068, 1515.88481799327], [-791125.0971205268, 6305.26406455737, 2598670.119546762, 2707026.830650488, 1046711.9865900541, 143261.9497663616], [-464329.1931164031, -42168.52782369026, -190208.32513803965, -2256397.1143982084, -2327607.0806788434, -681608.8326129188], [-463073.6864060763, -168158.8551728905, 180416.23250789748, -50536.15294270784, 0.0, 0.0], [-41444202.47082939, 64433436.756275326, -39141347.163228594, 11535334.227065524, -1668959.3624995525, 95200.81851057323]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    pre_muls = floatingpoint.PreOpL(lambda a, b, _: a * b, [x] * degree)

    poss_res = [0] * m
    for i in range(m):
        poss_res[i] = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res[i] += coeffA[i][j + 1] * pre_muls[j] * scaler[i][j + 1]

    comp = sfix.Array(m)
    for i in range(m):
        comp[i] = x >= breaks[i]

    cipher_index = Array(m, sfix)
    @for_range_opt(m - 1)
    def _(i):
        cipher_index[i] = comp[i + regint(1)]
        cipher_index[i] = comp[i] * (comp[i] - cipher_index[i])

    cipher_index[m - 1] = comp[m - 1]

    return sfix.dot_product(cipher_index, poss_res)


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
    
    breaks = [-4.199999809265137, -2.0999999046325684, -1.5749999284744263, -1.0499999523162842, -0.26249998807907104, 0.0, 0.5249999761581421, 1.0499999523162842, 2.0999999046325684, 3.1499998569488525]
    coeffA = [[1989492.6419209107, 2980996.145478863, 1757251.2433020272, 513130.90563265426, 74383.09253908029, 4284.99900167941], [-2079446.1826128173, -4251471.260061666, -2921046.352743573, -714466.3599176895, 9911.65794645624, 19046.67354426276], [1377273.6692918772, 5137222.262770954, 6986104.779443298, 4286723.897783079, 1182633.2241557175, 114202.1929579438], [52993.75087683968, -43554.10957135629, -690110.6374646683, -834971.0981328096, -137372.38698644025, 96208.4163864732], [63578.22341988525, 71893.36617898739, -245396.98539191487, -188393.47798766455, 0.0, 0.0], [63578.22341988525, 74118.8973563977, -228824.20083767627, 204600.1742014644, 0.0, 0.0], [77771.60283954802, 8428.29613166806, -207347.80703756347, 498229.8538707198, -440303.19914770813, 133765.55511512133], [-422798.070667928, 1835581.0837323382, -2664496.192515331, 1886272.4246103514, -652441.6983690155, 88390.16972350444], [-16407665.595672976, 33481704.98152768, -26790630.511231985, 10529246.984088695, -2030351.5776436634, 153995.8296406149], [-14896682.043867564, 19086852.770411942, -9725612.342307044, 2486373.1191911465, -317742.879934331, 16235.8258511812]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    pre_muls = floatingpoint.PreOpL(lambda a, b, _: a * b, [x] * degree)

    poss_res = [0] * m
    for i in range(m):
        poss_res[i] = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res[i] += coeffA[i][j + 1] * pre_muls[j] * scaler[i][j + 1]

    comp = sfix.Array(m)
    for i in range(m):
        comp[i] = x >= breaks[i]

    cipher_index = Array(m, sfix)
    @for_range_opt(m - 1)
    def _(i):
        cipher_index[i] = comp[i + regint(1)]
        cipher_index[i] = comp[i] * (comp[i] - cipher_index[i])

    cipher_index[m - 1] = comp[m - 1]

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
    
    breaks = [-4.199999809265137, -2.625, -1.5749999284744263, -1.0499999523162842, -0.5249999761581421, -0.26249998807907104, 0.0, 0.26249998807907104, 1.0499999523162842, 2.0999999046325684, 2.625, 3.1499998569488525]
    coeffA = [[5819418.340461029, 8191331.651474354, 4591690.18172584, 1281357.766694526, 178021.50730719868, 9851.4578948352], [-30237611.94840222, -70620135.26367147, -62991184.34644158, -27283352.847596698, -5793113.782014806, -485215.3128546605], [8571047.637723982, 30187230.69116835, 38007035.77598954, 20415015.490829244, 4307427.069913002, 172319.3576395864], [-467235.4149379627, -3904857.8640533867, -10333935.005424928, -10033687.127102112, -2770360.961246884, 256605.95021125887], [108153.38569093162, 206024.14384444323, 1009840.8908866805, 4775423.3881426975, 5966788.813219746, 1877142.8534093543], [95994.65466519597, 10485.32094200542, -276259.4378829839, 604607.1867943536, 0.0, 0.0], [95994.65466519597, 9848.3673486535, -152794.60612089405, 357704.7205864505, 0.0, 0.0], [114068.88963441834, -203555.76348373853, 763170.1361899881, -1266205.3659311738, 955294.1383181099, -268012.8126393744], [353156.50671410304, -1103812.997372365, 1793533.7679617223, -1396293.9573485025, 524415.2233813638, -76412.1490381756], [12333657.462940231, -26576495.902530912, 22718015.407624096, -9535570.330169851, 1963256.2169768242, -158920.2928057088], [-18065104.087102417, 29879346.076254107, -19256843.98895608, 6082200.557217241, -944844.8541298631, 57880.49810000563], [13954679.960175702, -17919899.23377236, 9202449.697091741, -2361584.9512304296, 302875.4560940989, -15529.63936876486]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    pre_muls = floatingpoint.PreOpL(lambda a, b, _: a * b, [x] * degree)

    poss_res = [0] * m
    for i in range(m):
        poss_res[i] = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res[i] += coeffA[i][j + 1] * pre_muls[j] * scaler[i][j + 1]

    comp = sfix.Array(m)
    for i in range(m):
        comp[i] = x >= breaks[i]

    cipher_index = Array(m, sfix)
    @for_range_opt(m - 1)
    def _(i):
        cipher_index[i] = comp[i + regint(1)]
        cipher_index[i] = comp[i] * (comp[i] - cipher_index[i])

    cipher_index[m - 1] = comp[m - 1]

    return sfix.dot_product(cipher_index, poss_res)


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
    
    breaks = [-4.199999809265137, -1.0499999523162842, -0.5249999761581421, 0.0, 0.13124999403953552, 2.0999999046325684, 3.1499998569488525]
    coeffA = [[-6944701.090870756, -8636829.615981994, -4463120.751510226, -1146592.0710933632, -143802.7558719245, -6971.06374490064], [-592582.4476126801, 2436951.2392365, -9462274.180854363, -23475026.025728337, -16709870.595580632, -3983463.1787766693], [-369004.7953612669, 4725396.509588421, 74231.33278602926, -4393184.634664723, 0.0, 0.0], [-369004.79536126694, 4691360.136768431, -294633.70645366, -3052477.137480041, 0.0, 0.0], [-389525.31897093344, 5018271.539877484, -2027295.8332723826, 242580.98266252223, 38690.3420749916, -8910.23225235444], [89228964.85385795, -178808505.634163, 147237377.88137493, -59615939.814270444, 11865862.337495157, -927245.3021715312], [173721699.74966136, -222290808.36768305, 114898364.49949902, -29470123.475355797, 3776514.982856534, -193467.0968568614]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    pre_muls = floatingpoint.PreOpL(lambda a, b, _: a * b, [x] * degree)

    poss_res = [0] * m
    for i in range(m):
        poss_res[i] = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res[i] += coeffA[i][j + 1] * pre_muls[j] * scaler[i][j + 1]

    comp = sfix.Array(m)
    for i in range(m):
        comp[i] = x >= breaks[i]

    cipher_index = Array(m, sfix)
    @for_range_opt(m - 1)
    def _(i):
        cipher_index[i] = comp[i + regint(1)]
        cipher_index[i] = comp[i] * (comp[i] - cipher_index[i])

    cipher_index[m - 1] = comp[m - 1]

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
    
    breaks = [-4.199999809265137, -2.625, -1.5749999284744263, -1.0499999523162842, -0.5249999761581421]
    coeffA = [[3391766.889361135, 4738995.03278066, 2652191.2178901983, 740244.8823220552, 102909.11448194773, 5698.75341312991], [-18186437.530796286, -42471997.73113723, -37889356.50598647, -16424972.934658967, -3492568.946046533, -293083.05463957036], [5012282.087321468, 18666040.20305435, 24690860.038446575, 14173743.530425359, 3424916.130004788, 239575.3966847436], [-381007.34427433216, -2228182.8177799117, -6278519.345439976, -7079460.571056627, -2798227.7591807647, -198514.39536959567], [-82605.3733783234, 53666.44567501057, -38579.15721246478, 3842.35035384237, 0.0, 0.0]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    pre_muls = floatingpoint.PreOpL(lambda a, b, _: a * b, [x] * degree)

    poss_res = [0] * m
    for i in range(m):
        poss_res[i] = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res[i] += coeffA[i][j + 1] * pre_muls[j] * scaler[i][j + 1]

    comp = sfix.Array(m)
    for i in range(m):
        comp[i] = x >= breaks[i]

    cipher_index = Array(m, sfix)
    @for_range_opt(m - 1)
    def _(i):
        cipher_index[i] = comp[i + regint(1)]
        cipher_index[i] = comp[i] * (comp[i] - cipher_index[i])

    cipher_index[m - 1] = comp[m - 1]

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
    
    breaks = [-4.199999809265137, -3.1499998569488525, -2.625, -2.0999999046325684, -1.0499999523162842, 0.0]
    coeffA = [[-414085.45655826107, -660643.6537619088, -365442.1965854691, -96822.79983593171, -12640.89084034397, -656.84764766082], [-20822628.37216849, -33506117.274629954, -21545067.09398353, -6936236.587853159, -1118614.1270735727, -72296.20720459991], [18283743.761504207, 44344982.61873056, 40456777.90664453, 17756968.82966145, 3799314.6620864742, 319541.8073315586], [-13825558.911037348, -49012639.568536475, -66419580.562698305, -42691023.043008104, -13134649.947045837, -1563556.120771327], [-454652.3857639003, 62822.13968952611, 1866660.5955790288, 1448455.5261005831, 0.0, 0.0], [-454652.3857639003, -6990.95654436625, 5207.05557872794, -6053.84759450079, 0.0, 0.0]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    pre_muls = floatingpoint.PreOpL(lambda a, b, _: a * b, [x] * degree)

    poss_res = [0] * m
    for i in range(m):
        poss_res[i] = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res[i] += coeffA[i][j + 1] * pre_muls[j] * scaler[i][j + 1]

    comp = sfix.Array(m)
    for i in range(m):
        comp[i] = x >= breaks[i]

    cipher_index = Array(m, sfix)
    @for_range_opt(m - 1)
    def _(i):
        cipher_index[i] = comp[i + regint(1)]
        cipher_index[i] = comp[i] * (comp[i] - cipher_index[i])

    cipher_index[m - 1] = comp[m - 1]

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
    
    breaks = [-4.199999809265137, -3.1499998569488525, -2.0999999046325684, -1.5749999284744263, -1.0499999523162842, -0.5249999761581421, 0.0, 2.0999999046325684]
    coeffA = [[-197777.92370928393, -400484.0895296396, -231752.35944451852, -61664.29428722854, -7988.33437668424, -410.53136000412], [-1454952.7382621043, -303873.0386720868, 1326072.55748412, 966749.568800654, 250220.90386034807, 22722.17050536548], [722776.2663690961, -3436860.996667687, -9276399.792337498, -7593027.753094097, -2602244.2700653924, -325036.8471432073], [-4504292.122321471, -12456655.588242348, -10881480.057521695, -2170311.765369758, 1237849.2831217577, 442734.33310137497], [-163742.0471326831, 2365607.552810404, 6356344.568902304, 3767441.6765051796, -997481.9327356142, -974566.9250532251], [-531105.1520528721, -42353.65027506902, 1044056.2615743296, 101490.95425570016, 0.0, 0.0], [-531105.1520528721, -17294.61181401008, 14906.94178214423, -3856.20041755454, 0.0, 0.0], [-5253025.30065682, 6364620.897765528, -3125446.361036469, 687748.4355699515, -68194.36461505061, 2207.48545264845]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    pre_muls = floatingpoint.PreOpL(lambda a, b, _: a * b, [x] * degree)

    poss_res = [0] * m
    for i in range(m):
        poss_res[i] = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res[i] += coeffA[i][j + 1] * pre_muls[j] * scaler[i][j + 1]

    comp = sfix.Array(m)
    for i in range(m):
        comp[i] = x >= breaks[i]

    cipher_index = Array(m, sfix)
    @for_range_opt(m - 1)
    def _(i):
        cipher_index[i] = comp[i + regint(1)]
        cipher_index[i] = comp[i] * (comp[i] - cipher_index[i])

    cipher_index[m - 1] = comp[m - 1]

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
    
    breaks = [-4.199999809265137, -3.1499998569488525, -2.0999999046325684, -1.5749999284744263, -1.0499999523162842, -0.7874999642372131, -0.26249998807907104, 0.0, 0.5249999761581421, 1.0499999523162842, 2.0999999046325684, 3.1499998569488525]
    coeffA = [[434081.68074060685, 662016.2823867555, 362527.7933909099, 95956.26446176985, 12550.15679417749, 653.77074610349], [5926020.298332312, 5919844.901937399, 1220740.6692270457, -518276.00069846376, -243005.44643642064, -26809.05174410402], [-7916835.206588488, -11930699.745503599, -2008842.0702185866, 4256803.254339481, 2350213.849705577, 355453.96247528587], [7508443.484094372, 25024717.6611662, 29439227.523262434, 14188312.810507193, 2230364.985170119, -89086.28567264277], [-2194856.4907533135, -14719389.928193493, -35052822.667354554, -37498237.30489214, -18149188.582310244, -3232831.8471287526], [282938.09894105117, 581842.5555676828, 2861660.535653443, 9613449.636665242, 11198851.603933992, 4097015.2669842667], [241518.7719499389, 10283.02013283389, -304005.61621193634, 901229.4237775491, 0.0, 0.0], [241518.7719499389, -9884.90343681018, 16401.18310529113, 3053.13641825166, 0.0, 0.0], [238074.12886764016, -84001.94711423277, 515423.30676993023, -1040755.5069990051, 872430.2531117358, -261316.28098445793], [-387698.808852663, 2002882.6120522425, -2499515.871958124, 1526652.2603722513, -456497.5943905403, 53456.95949753149], [-55781369.97154484, 109905410.64866152, -85031241.6926109, 32393595.151919834, -6075022.909176457, 449484.31560785475], [-34333147.92115159, 43874570.205792196, -22288921.570153374, 5682771.8096453585, -724286.753479998, 36911.99323005385]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    pre_muls = floatingpoint.PreOpL(lambda a, b, _: a * b, [x] * degree)

    poss_res = [0] * m
    for i in range(m):
        poss_res[i] = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res[i] += coeffA[i][j + 1] * pre_muls[j] * scaler[i][j + 1]

    comp = sfix.Array(m)
    for i in range(m):
        comp[i] = x >= breaks[i]

    cipher_index = Array(m, sfix)
    @for_range_opt(m - 1)
    def _(i):
        cipher_index[i] = comp[i + regint(1)]
        cipher_index[i] = comp[i] * (comp[i] - cipher_index[i])

    cipher_index[m - 1] = comp[m - 1]

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
    
    breaks = [-4.199999809265137, -1.0499999523162842, -0.7874999642372131, -0.5249999761581421, 0.0]
    coeffA = [[7573989.220934761, 17207943.60308106, 13959975.580641743, 5262472.86114993, 940867.2587832874, 64607.18498150131], [1868705.2772268716, 12407031.999255879, 30565032.606775817, 34144196.63172708, 17223183.322617583, 3198555.2295255526], [-147298.73042959382, -103922.98292280563, -638416.7815691497, -4961075.416241768, -7406688.647045174, -3039073.6903921077], [-166221.35356917934, -34729.05190859146, 896754.8800876419, 632115.6003275961, 0.0, 0.0], [-166221.35356917934, -43945.21226026112, 45182.42107050644, -7704.81010363855, 0.0, 0.0]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    pre_muls = floatingpoint.PreOpL(lambda a, b, _: a * b, [x] * degree)

    poss_res = [0] * m
    for i in range(m):
        poss_res[i] = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res[i] += coeffA[i][j + 1] * pre_muls[j] * scaler[i][j + 1]

    comp = sfix.Array(m)
    for i in range(m):
        comp[i] = x >= breaks[i]

    cipher_index = Array(m, sfix)
    @for_range_opt(m - 1)
    def _(i):
        cipher_index[i] = comp[i + regint(1)]
        cipher_index[i] = comp[i] * (comp[i] - cipher_index[i])

    cipher_index[m - 1] = comp[m - 1]

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
    
    breaks = [-4.199999809265137, -3.1499998569488525, -2.0999999046325684, -1.5749999284744263, 0.0, 2.0999999046325684]
    coeffA = [[-81127.72032886371, -308717.0981851465, -192343.53668934203, -51515.02900476364, -6594.11452799933, -333.02623692499], [-5387497.071275668, -8347709.629342871, -5015500.604351049, -1480123.7731652977, -214706.76452371496, -12195.04141937], [4279360.963255487, 10940156.202898012, 9971869.74141375, 4114897.760310139, 763987.5378377832, 48403.19676910543], [-400063.3154940033, -146525.71837777106, 69300.42002121775, 15944.44231321729, 0.0, 0.0], [-400063.3154940033, -14433.25763859878, 16904.15093118105, -6150.59697313339, 0.0, 0.0], [-45998993.49178681, 72152100.17192082, -44124059.15029916, 13095328.05250309, -1907322.8748739846, 109494.60780156007]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    pre_muls = floatingpoint.PreOpL(lambda a, b, _: a * b, [x] * degree)

    poss_res = [0] * m
    for i in range(m):
        poss_res[i] = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res[i] += coeffA[i][j + 1] * pre_muls[j] * scaler[i][j + 1]

    comp = sfix.Array(m)
    for i in range(m):
        comp[i] = x >= breaks[i]

    cipher_index = Array(m, sfix)
    @for_range_opt(m - 1)
    def _(i):
        cipher_index[i] = comp[i + regint(1)]
        cipher_index[i] = comp[i] * (comp[i] - cipher_index[i])

    cipher_index[m - 1] = comp[m - 1]

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
    
    breaks = [-4.199999809265137, -2.0999999046325684, -1.5749999284744263, -1.0499999523162842, -0.26249998807907104, 0.0, 0.5249999761581421, 1.0499999523162842, 2.0999999046325684, 3.1499998569488525]
    coeffA = [[2111147.065479564, 3131164.565021458, 1839022.696390263, 536088.3866405468, 77622.7147317948, 4467.3068260865], [-1972080.501889753, -3530196.6712011136, -1767041.7330105382, 51591.42760324456, 241733.83439719013, 45638.24503014013], [1505913.8355113447, 5562090.292652656, 7286946.12892928, 4197017.312262156, 1038798.4783559231, 79255.91029609501], [26551.55993159576, -22917.34790495124, -496665.80150165973, -356480.95049131813, 334970.1078672465, 251004.24810235665], [34831.01119818694, 61409.56752751155, -216200.55734838577, -124733.30477192099, 0.0, 0.0], [34831.01119818695, 62559.78082154156, -189705.93160722777, 167361.3185393492, 0.0, 0.0], [43759.23004131594, 23005.56081798352, -194113.783769414, 408542.5040303734, -339715.8329331296, 99311.23896998951], [-270596.94256010756, 1123118.6794471042, -1578244.5011147289, 1079894.6231323285, -360496.26308329473, 47070.61888680488], [-6054993.850641826, 12255182.400506422, -9701816.549516842, 3773732.1209111125, -720791.5713136739, 54206.72899469745], [-4451661.081071695, 5700435.72307228, -2896781.7893443494, 739673.7040538735, -94418.80560733729, 4819.27403500142]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    pre_muls = floatingpoint.PreOpL(lambda a, b, _: a * b, [x] * degree)

    poss_res = [0] * m
    for i in range(m):
        poss_res[i] = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res[i] += coeffA[i][j + 1] * pre_muls[j] * scaler[i][j + 1]

    comp = sfix.Array(m)
    for i in range(m):
        comp[i] = x >= breaks[i]

    cipher_index = Array(m, sfix)
    @for_range_opt(m - 1)
    def _(i):
        cipher_index[i] = comp[i + regint(1)]
        cipher_index[i] = comp[i] * (comp[i] - cipher_index[i])

    cipher_index[m - 1] = comp[m - 1]

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
    
    breaks = [-4.199999809265137, -1.0499999523162842, -0.5249999761581421, -0.26249998807907104, 0.0, 0.5249999761581421, 1.0499999523162842, 2.0999999046325684, 3.1499998569488525]
    coeffA = [[-125425.77493662175, 352681.30640868196, 506755.2522457203, 241399.466526858, 49576.27256195465, 3741.40756390918], [173858.7227772318, -729283.3061662787, -2929612.2902422, -2118733.242113851, 43051.42214555897, 294405.9112039987], [307094.5129924705, 230103.7608800119, -249817.31107700572, 1452411.7297165983, 2236261.9945705724, 746633.5535686518], [304236.9182745211, 181430.80412283613, -611976.1412951569, 85569.03862199301, 0.0, 0.0], [304236.9182745211, 180084.4711692221, -518264.3162919924, 436345.92632751935, 0.0, 0.0], [287185.44287695293, 345851.0817021496, -1195521.4302654741, 1797236.653654637, -1215649.7692526728, 303875.86711655406], [-2211959.2797820484, 8686624.731863666, -11632852.471840417, 7607953.7656671535, -2432328.351194349, 304454.8049234011], [-102188059.49725048, 202162028.58652577, -157211170.26762867, 60189698.86373926, -11341936.134803481, 842970.7570368722], [-67971793.80526409, 86897861.11418666, -44217248.02561319, 11282315.867996303, -1439014.8870748733, 73388.91105989816]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    pre_muls = floatingpoint.PreOpL(lambda a, b, _: a * b, [x] * degree)

    poss_res = [0] * m
    for i in range(m):
        poss_res[i] = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res[i] += coeffA[i][j + 1] * pre_muls[j] * scaler[i][j + 1]

    comp = sfix.Array(m)
    for i in range(m):
        comp[i] = x >= breaks[i]

    cipher_index = Array(m, sfix)
    @for_range_opt(m - 1)
    def _(i):
        cipher_index[i] = comp[i + regint(1)]
        cipher_index[i] = comp[i] * (comp[i] - cipher_index[i])

    cipher_index[m - 1] = comp[m - 1]

    return sfix.dot_product(cipher_index, poss_res)


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
    
    breaks = [-4.199999809265137, -1.0499999523162842, -0.5249999761581421, 0.0, 0.13124999403953552, 2.0999999046325684, 3.1499998569488525]
    coeffA = [[-9821798.207535958, -15068615.13009234, -9630146.653243698, -3083596.331899761, -489012.7878409403, -30631.6554568854], [-760612.3365968326, 1052232.4399187802, -13376596.446428115, -27571785.65907589, -18124498.280316938, -4014131.7104288335], [-337382.0450293881, 4736574.4780310765, -273960.43541844364, -4647826.64233554, 0.0, 0.0], [-337382.04502938816, 4720543.412458118, -437658.5410936537, -2812415.561109675, 0.0, 0.0], [-355509.72710141464, 5012475.935535643, -2008051.8438393984, 216573.00636286632, 53871.06453143667, -12071.07965115261], [117720163.44912486, -235905072.46369678, 192424017.79747325, -77217246.3723111, 15237032.225213407, -1181564.2915416684], [199836272.95457807, -255719443.3843462, 131978301.71098779, -33837319.6045294, 4334641.063090627, -221986.24231599865]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    pre_muls = floatingpoint.PreOpL(lambda a, b, _: a * b, [x] * degree)

    poss_res = [0] * m
    for i in range(m):
        poss_res[i] = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res[i] += coeffA[i][j + 1] * pre_muls[j] * scaler[i][j + 1]

    comp = sfix.Array(m)
    for i in range(m):
        comp[i] = x >= breaks[i]

    cipher_index = Array(m, sfix)
    @for_range_opt(m - 1)
    def _(i):
        cipher_index[i] = comp[i + regint(1)]
        cipher_index[i] = comp[i] * (comp[i] - cipher_index[i])

    cipher_index[m - 1] = comp[m - 1]

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
    
    breaks = [-4.199999809265137, -3.1499998569488525, -2.0999999046325684, -1.5749999284744263, -1.0499999523162842, 0.0, 2.0999999046325684]
    coeffA = [[242674.4004846571, 183845.0906502723, 77229.92803540599, 19833.39749046484, 2738.56664426656, 153.20999504402], [-581095.6913315373, -3257011.240578344, -3631907.0291563966, -1700921.825178373, -366921.5769196252, -30157.75888582916], [-3296984.0860536555, -1998198.7488796029, 4627438.4805256585, 5478590.74913778, 2093844.7531392758, 274244.18375470507], [3827482.5538236955, 14388154.309726086, 17396410.432367492, 8367264.298189669, 1306889.2268122712, -49488.65012816878], [-243412.4358021921, -15410.68196482697, -735018.6150557634, -779692.4096523125, 0.0, 0.0], [-243412.4358021921, 7117.7690038557, -1764.51306303715, -938.98754219654, 0.0, 0.0], [-35411436.631818965, 55587997.83525478, -33960953.35620589, 10070149.861584071, -1464910.881655541, 83973.88677994834]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    pre_muls = floatingpoint.PreOpL(lambda a, b, _: a * b, [x] * degree)

    poss_res = [0] * m
    for i in range(m):
        poss_res[i] = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res[i] += coeffA[i][j + 1] * pre_muls[j] * scaler[i][j + 1]

    comp = sfix.Array(m)
    for i in range(m):
        comp[i] = x >= breaks[i]

    cipher_index = Array(m, sfix)
    @for_range_opt(m - 1)
    def _(i):
        cipher_index[i] = comp[i + regint(1)]
        cipher_index[i] = comp[i] * (comp[i] - cipher_index[i])

    cipher_index[m - 1] = comp[m - 1]

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
    
    breaks = [-4.199999809265137, -1.0499999523162842, 0.0]
    coeffA = [[7134262.469564876, 17225409.445329864, 14435378.345148426, 5552779.0677285865, 1006502.0390775452, 69801.18545817939], [-185754.95005797103, -7136.41405406518, 497510.91978880786, 605869.1303629759, 0.0, 0.0], [-185754.95005797103, -41762.87058923766, 46313.6532129448, -8068.56393049266, 0.0, 0.0]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    pre_muls = floatingpoint.PreOpL(lambda a, b, _: a * b, [x] * degree)

    poss_res = [0] * m
    for i in range(m):
        poss_res[i] = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res[i] += coeffA[i][j + 1] * pre_muls[j] * scaler[i][j + 1]

    comp = sfix.Array(m)
    for i in range(m):
        comp[i] = x >= breaks[i]

    cipher_index = Array(m, sfix)
    @for_range_opt(m - 1)
    def _(i):
        cipher_index[i] = comp[i + regint(1)]
        cipher_index[i] = comp[i] * (comp[i] - cipher_index[i])

    cipher_index[m - 1] = comp[m - 1]

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
    
    breaks = [-4.199999809265137, -3.1499998569488525, -2.0999999046325684, -1.5749999284744263, -1.0499999523162842, -0.5249999761581421, 2.0999999046325684]
    coeffA = [[337812.19420700043, 286237.8960728064, 127928.31173457122, 33113.82546330663, 4508.75570883524, 247.84769556], [6821767.3862452675, 8944327.739960294, 4447072.814559815, 980775.0127654262, 79046.36401057485, -440.94877345418], [-12984950.985325402, -29201650.359953847, -23728004.687387694, -8727964.239350008, -1384669.976177712, -61803.8701848088], [4549189.127337209, 21091121.551145438, 33424094.446701676, 23340262.184823263, 7461489.445996371, 891658.9873003684], [-776533.8897510864, -1652653.8117157447, -5295629.8534959955, -9466571.24234494, -6348730.075386843, -1413202.737130485], [-554975.5426012118, -152661.02892048858, 159732.57836779946, -42862.76690411246, 0.0, 0.0], [-12954238.925415337, 17724593.14956846, -9594877.95935215, 2465291.1850319766, -305995.0064117334, 14638.95792837672]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    pre_muls = floatingpoint.PreOpL(lambda a, b, _: a * b, [x] * degree)

    poss_res = [0] * m
    for i in range(m):
        poss_res[i] = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res[i] += coeffA[i][j + 1] * pre_muls[j] * scaler[i][j + 1]

    comp = sfix.Array(m)
    for i in range(m):
        comp[i] = x >= breaks[i]

    cipher_index = Array(m, sfix)
    @for_range_opt(m - 1)
    def _(i):
        cipher_index[i] = comp[i + regint(1)]
        cipher_index[i] = comp[i] * (comp[i] - cipher_index[i])

    cipher_index[m - 1] = comp[m - 1]

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
    
    breaks = [-4.199999809265137, -0.5249999761581421, -0.26249998807907104, 0.0, 0.26249998807907104, 1.0499999523162842, 1.5749999284744263, 2.0999999046325684, 2.625]
    coeffA = [[535505.4135978239, 1870007.2550820033, 1819700.4803600209, 758804.1702495157, 144754.8397981267, 10406.69571465892], [22433.75541331485, 34120.87179140286, 27851.2394250587, 620556.5273937922, 416356.0609321337, -51562.1478228655], [21168.95717559356, 14225.67932110768, -97325.15830033385, 249650.9193284588, 0.0, 0.0], [21168.95717559356, 13612.72634778196, -78289.05021934456, 130031.12282573282, 0.0, 0.0], [24600.34468550546, -25404.0791400298, 78165.7554645274, -104706.91379477816, 61319.71433339507, -12375.52375305362], [-74600.67707045545, 454893.91187820974, -835053.254902401, 744392.8007944147, -322372.64271268994, 54344.46467244453], [-544207.6480420317, 751619.7007516874, 236236.0297453068, -817474.0103175505, 443116.4912973784, -76018.97606486765], [11202485.684839716, -18860848.50514647, 11113204.017319452, -2344108.6024002405, -51242.34070068881, 51905.48104734271], [-32158305.849005107, 51433344.06851995, -31918869.850860037, 9646734.941038007, -1430164.0458266304, 83513.61632981578]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    pre_muls = floatingpoint.PreOpL(lambda a, b, _: a * b, [x] * degree)

    poss_res = [0] * m
    for i in range(m):
        poss_res[i] = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res[i] += coeffA[i][j + 1] * pre_muls[j] * scaler[i][j + 1]

    comp = sfix.Array(m)
    for i in range(m):
        comp[i] = x >= breaks[i]

    cipher_index = Array(m, sfix)
    @for_range_opt(m - 1)
    def _(i):
        cipher_index[i] = comp[i + regint(1)]
        cipher_index[i] = comp[i] * (comp[i] - cipher_index[i])

    cipher_index[m - 1] = comp[m - 1]

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
    
    breaks = [-4.199999809265137, -2.0999999046325684]
    coeffA = [[-2114764.252668953, -3175116.60680346, -1882821.3636864964, -553392.6935206943, -80713.7242031439, -4675.49001420307], [-113958.8947598051, -9285.13482784965, 13640.57670184253, -3264.92505708293, 0.0, 0.0]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    pre_muls = floatingpoint.PreOpL(lambda a, b, _: a * b, [x] * degree)

    poss_res = [0] * m
    for i in range(m):
        poss_res[i] = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res[i] += coeffA[i][j + 1] * pre_muls[j] * scaler[i][j + 1]

    comp = sfix.Array(m)
    for i in range(m):
        comp[i] = x >= breaks[i]

    cipher_index = Array(m, sfix)
    @for_range_opt(m - 1)
    def _(i):
        cipher_index[i] = comp[i + regint(1)]
        cipher_index[i] = comp[i] * (comp[i] - cipher_index[i])

    cipher_index[m - 1] = comp[m - 1]

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
    
    breaks = [-4.199999809265137, -3.1499998569488525, -2.625, -2.0999999046325684, -1.0499999523162842, 0.0, 2.0999999046325684]
    coeffA = [[-333121.85418646014, -569567.0076009064, -319646.687954425, -84807.35466371775, -11044.26695820089, -571.84124806453], [-17846194.127844185, -28779249.140727356, -18525340.597635448, -5968736.023547926, -963281.7681525489, -62301.88178293358], [11988553.842544178, 30863752.13489403, 29161181.919425294, 13092504.597760314, 2845919.527631505, 242164.77376086955], [-10124623.536123449, -36367366.77084457, -50414926.72384428, -33098359.814988002, -10366732.332550239, -1252554.5319160656], [-315087.4652539996, 70472.84602269452, 1061599.4778557464, 854682.2404703437, 0.0, 0.0], [-315087.46525399963, -9465.85163949048, 10335.88200855677, -3395.83322417854, 0.0, 0.0], [-23550711.84085602, 36353767.903817214, -21954698.068985242, 6430030.141478645, -924638.610604401, 52426.21156699317]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    pre_muls = floatingpoint.PreOpL(lambda a, b, _: a * b, [x] * degree)

    poss_res = [0] * m
    for i in range(m):
        poss_res[i] = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res[i] += coeffA[i][j + 1] * pre_muls[j] * scaler[i][j + 1]

    comp = sfix.Array(m)
    for i in range(m):
        comp[i] = x >= breaks[i]

    cipher_index = Array(m, sfix)
    @for_range_opt(m - 1)
    def _(i):
        cipher_index[i] = comp[i + regint(1)]
        cipher_index[i] = comp[i] * (comp[i] - cipher_index[i])

    cipher_index[m - 1] = comp[m - 1]

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
    
    breaks = [-4.199999809265137, -1.0499999523162842, 0.0, 0.5249999761581421, 1.0499999523162842, 2.0999999046325684, 3.1499998569488525]
    coeffA = [[790406.1498447718, 1961096.835401832, 1644264.920618412, 631474.0122890892, 114351.60526511187, 7927.78741301512], [44862.65702585774, 36143.38485922354, -117862.87806544625, -56110.71270320896, 0.0, 0.0], [44862.65702585774, 36873.09036278944, -114342.49734801715, 102711.45710877197, 0.0, 0.0], [52934.08690151587, -1455.62818945291, -93764.55601685985, 245673.47187400993, -225051.92359719193, 69935.74466405126], [-348346.01657645847, 1493076.181186822, -2201205.0373294987, 1588143.1160126217, -561267.5129629236, 77826.29406368289], [-21909511.815193124, 44552560.10773814, -35619181.9614435, 13995064.549385935, -2699039.5536616803, 204773.02770810627], [-20865070.262603752, 26729957.651941802, -13636494.080119288, 3487063.067998409, -445716.2308092496, 22779.24983425603]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    pre_muls = floatingpoint.PreOpL(lambda a, b, _: a * b, [x] * degree)

    poss_res = [0] * m
    for i in range(m):
        poss_res[i] = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res[i] += coeffA[i][j + 1] * pre_muls[j] * scaler[i][j + 1]

    comp = sfix.Array(m)
    for i in range(m):
        comp[i] = x >= breaks[i]

    cipher_index = Array(m, sfix)
    @for_range_opt(m - 1)
    def _(i):
        cipher_index[i] = comp[i + regint(1)]
        cipher_index[i] = comp[i] * (comp[i] - cipher_index[i])

    cipher_index[m - 1] = comp[m - 1]

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
    
    breaks = [-4.199999809265137, -1.0499999523162842, 0.0, 2.0999999046325684, 3.1499998569488525]
    coeffA = [[6611691.993989665, 15814789.51127594, 13144946.192023752, 5028250.051937749, 907984.5364194555, 62802.44374515101], [-15664.5238160986, 212417.62160304736, 450910.16574748635, 481399.39227052056, 0.0, 0.0], [-15664.52381609859, 27461.13431592188, -25140.6444189121, 7853.56185061746, 0.0, 0.0], [-30038077.635324374, 63509730.95236747, -52716070.72471488, 21407641.930615924, -4246295.201295134, 329952.2165826933], [-41467273.37210089, 53199094.70164088, -27200725.719691943, 6967023.355951498, -891935.6326391869, 45654.78212285017]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    pre_muls = floatingpoint.PreOpL(lambda a, b, _: a * b, [x] * degree)

    poss_res = [0] * m
    for i in range(m):
        poss_res[i] = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res[i] += coeffA[i][j + 1] * pre_muls[j] * scaler[i][j + 1]

    comp = sfix.Array(m)
    for i in range(m):
        comp[i] = x >= breaks[i]

    cipher_index = Array(m, sfix)
    @for_range_opt(m - 1)
    def _(i):
        cipher_index[i] = comp[i + regint(1)]
        cipher_index[i] = comp[i] * (comp[i] - cipher_index[i])

    cipher_index[m - 1] = comp[m - 1]

    return sfix.dot_product(cipher_index, poss_res)


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
    
    breaks = [-4.199999809265137, -1.0499999523162842, -0.5249999761581421, 0.0, 0.13124999403953552, 1.0499999523162842, 2.0999999046325684]
    coeffA = [[-10822023.699762626, -17510172.834145274, -11691254.747017693, -3876838.364819309, -632370.062647352, -40530.19421405214], [-842693.4015903698, 1257878.7928843999, -12711654.554325107, -27368886.83399243, -18386450.43595458, -4144113.5520978062], [-454615.97679093754, 4716414.155785931, -69520.50746398224, -4644053.481230953, 0.0, 0.0], [-454615.9767909376, 4693174.036746747, -315338.7716886712, -2996113.8296255954, 0.0, 0.0], [-466940.80776686576, 4904445.505886428, -1517555.4978858347, -768911.191785154, 950279.1870974088, -312266.4687653801], [-859416.5943625971, 6459478.720873891, -4134623.6892456184, 1748311.411013007, -488287.77539549576, 63509.47650201712], [-50092471.80360228, 91488982.40156484, -60729074.78664252, 19589800.88084416, -3059229.5899824947, 186487.00209800687]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    pre_muls = floatingpoint.PreOpL(lambda a, b, _: a * b, [x] * degree)

    poss_res = [0] * m
    for i in range(m):
        poss_res[i] = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res[i] += coeffA[i][j + 1] * pre_muls[j] * scaler[i][j + 1]

    comp = sfix.Array(m)
    for i in range(m):
        comp[i] = x >= breaks[i]

    cipher_index = Array(m, sfix)
    @for_range_opt(m - 1)
    def _(i):
        cipher_index[i] = comp[i + regint(1)]
        cipher_index[i] = comp[i] * (comp[i] - cipher_index[i])

    cipher_index[m - 1] = comp[m - 1]

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
    
    breaks = [-4.199999809265137, -2.0999999046325684, 0.0, 0.26249998807907104, 1.0499999523162842, 1.5749999284744263, 2.0999999046325684, 2.625, 3.1499998569488525]
    coeffA = [[2190660.9244907345, 3320422.8577536293, 1957306.6554675926, 569843.5619208715, 82317.9425147475, 4726.77006488052], [15513.68131082816, 354958.75196199253, 415785.98399343126, 121332.57165757121, 0.0, 0.0], [15513.68131082815, 69437.76020191921, -235087.99821589913, 244195.4097268818, 0.0, 0.0], [12937.08738915237, 105282.60300578854, -431132.3416720486, 757882.6287933429, -596208.6184010132, 172762.6911776714], [-271290.99418392277, 1037066.5968223735, -1391923.5798141076, 870367.4237120113, -246050.7484290387, 23338.71792950012], [3212017.5664973287, -7986304.560270168, 7586641.471434255, -3312539.088703914, 615032.6177328163, -28259.56780536497], [-20658779.56570534, 37789484.00747716, -25709913.153705914, 7733354.254152484, -888547.7959025067, 9085.5182008211], [48103227.88547717, -67395131.92707498, 34856227.96353481, -7895281.188661045, 669782.2899773434, -1284.86123861249], [-67238334.16247128, 86109477.52911049, -43969332.14987253, 11244070.781447483, -1437219.3501168494, 73451.39965245809]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    pre_muls = floatingpoint.PreOpL(lambda a, b, _: a * b, [x] * degree)

    poss_res = [0] * m
    for i in range(m):
        poss_res[i] = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res[i] += coeffA[i][j + 1] * pre_muls[j] * scaler[i][j + 1]

    comp = sfix.Array(m)
    for i in range(m):
        comp[i] = x >= breaks[i]

    cipher_index = Array(m, sfix)
    @for_range_opt(m - 1)
    def _(i):
        cipher_index[i] = comp[i + regint(1)]
        cipher_index[i] = comp[i] * (comp[i] - cipher_index[i])

    cipher_index[m - 1] = comp[m - 1]

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
    
    breaks = [-4.199999809265137, -2.0999999046325684, -1.0499999523162842, -0.5249999761581421, 2.0999999046325684]
    coeffA = [[1445711.254140176, 1935908.320122942, 1121086.9173685997, 330626.1990998168, 48672.42071138138, 2845.01549255705], [-938602.4213492033, -506330.5224364044, 2131342.888832449, 2549924.33404588, 1033524.7923398378, 144864.13081982415], [-441064.5112443864, 6570.15146794698, -17710.78277129029, -2176085.6383337695, -2391877.798791819, -719357.7357995737], [-447118.8917438535, -184869.2629046768, 197871.9370745128, -55264.31687891552, 0.0, 0.0], [-40001529.50408952, 62216555.07651189, -37813684.725840054, 11149850.316886188, -1614065.6651619498, 92121.33192915982]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    pre_muls = floatingpoint.PreOpL(lambda a, b, _: a * b, [x] * degree)

    poss_res = [0] * m
    for i in range(m):
        poss_res[i] = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res[i] += coeffA[i][j + 1] * pre_muls[j] * scaler[i][j + 1]

    comp = sfix.Array(m)
    for i in range(m):
        comp[i] = x >= breaks[i]

    cipher_index = Array(m, sfix)
    @for_range_opt(m - 1)
    def _(i):
        cipher_index[i] = comp[i + regint(1)]
        cipher_index[i] = comp[i] * (comp[i] - cipher_index[i])

    cipher_index[m - 1] = comp[m - 1]

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
    
    breaks = [-4.199999809265137, -3.1499998569488525, -2.0999999046325684, -1.0499999523162842, 0.0, 2.0999999046325684]
    coeffA = [[-193146.20798458447, -397585.5470415316, -230690.21202644095, -61397.03478480802, -7950.18417457798, -408.30997948951], [-3898848.840391133, -4669283.496879298, -1787076.5425620356, -141771.39000045002, 53128.24981605453, 8725.12886739831], [-8944928.204158437, -30352536.026233748, -39905553.49610723, -25184253.369359985, -7662385.612785953, -905732.9601605344], [-534363.7904747205, 69674.6413266323, 1698040.4057725493, 1156671.2165918008, 0.0, 0.0], [-534363.7904747205, -22478.13364690334, 19064.81423361199, -5086.66432956084, 0.0, 0.0], [-5786007.45603691, 7438119.278508711, -3933774.0640570214, 973848.2336490864, -116694.37929330692, 5386.16508483587]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    pre_muls = floatingpoint.PreOpL(lambda a, b, _: a * b, [x] * degree)

    poss_res = [0] * m
    for i in range(m):
        poss_res[i] = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res[i] += coeffA[i][j + 1] * pre_muls[j] * scaler[i][j + 1]

    comp = sfix.Array(m)
    for i in range(m):
        comp[i] = x >= breaks[i]

    cipher_index = Array(m, sfix)
    @for_range_opt(m - 1)
    def _(i):
        cipher_index[i] = comp[i + regint(1)]
        cipher_index[i] = comp[i] * (comp[i] - cipher_index[i])

    cipher_index[m - 1] = comp[m - 1]

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
    
    breaks = [-4.199999809265137, -2.0999999046325684, -1.0499999523162842, -0.26249998807907104, 0.26249998807907104, 0.5249999761581421, 2.0999999046325684]
    coeffA = [[-2606888.0498440615, -5224748.930539334, -3187454.7242987724, -909497.5542269988, -127215.88945977596, -7074.53457844609], [1566443.4002791904, 5123144.640154445, 7828414.024855902, 5271102.882996271, 1662613.6155614816, 203326.20437595545], [563799.7209986232, -156607.5999929666, -2980560.1493762177, -5583187.720073273, -3716642.821817086, -853744.2370821572], [581543.3708326895, 70964.50147321023, -1787449.9751242911, -2442880.912517412, 0.0, 0.0], [587015.6871442399, -5848.00678880138, -1313542.8384083994, -4299896.111677493, 3336664.6315306257, -174450.74963972214], [-1498717.1666762352, 11809732.178310657, -26502063.08535071, 20365003.146013312, -7021328.606862365, 902151.5097431167], [-9996163.31303526, 13899715.042818343, -9855577.742180761, 2887474.770514748, -418149.39765124826, 24053.30585731844]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    pre_muls = floatingpoint.PreOpL(lambda a, b, _: a * b, [x] * degree)

    poss_res = [0] * m
    for i in range(m):
        poss_res[i] = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res[i] += coeffA[i][j + 1] * pre_muls[j] * scaler[i][j + 1]

    comp = sfix.Array(m)
    for i in range(m):
        comp[i] = x >= breaks[i]

    cipher_index = Array(m, sfix)
    @for_range_opt(m - 1)
    def _(i):
        cipher_index[i] = comp[i + regint(1)]
        cipher_index[i] = comp[i] * (comp[i] - cipher_index[i])

    cipher_index[m - 1] = comp[m - 1]

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
    
    breaks = [-4.199999809265137, -3.1499998569488525, -2.0999999046325684, -1.5749999284744263, -1.0499999523162842, -0.26249998807907104, -0.13124999403953552, 0.0, 1.0499999523162842]
    coeffA = [[-105826.08412091147, -586233.8395505844, -374504.84128208255, -100513.37765479436, -12816.3924722775, -643.56957810464], [-3694748.61483363, -4629339.903138754, -1756291.9460331777, -115393.72853402451, 60380.75042431741, 9377.42625138665], [5790217.079073167, 10302410.349985983, 5498244.056619657, 149707.9099268763, -611223.5993765558, -122738.32933878087], [-4251931.841818233, -15821620.288943384, -20309821.54979749, -11493621.84332646, -2770971.891004138, -196681.31971915343], [17039.46699788998, 83818.81058117638, 1290050.4633714969, 318222.7298775637, -1656630.047930949, -930906.4139778796], [-10530.1040464816, -202904.2756530895, 227676.35016223945, -1259292.4753926245, -2138701.8730931794, -340363.618472915], [-10452.57832736865, -199721.96901931585, 292602.92772684357, -640216.553547405, 0.0, 0.0], [-10452.57832736861, 40643.36711869838, -1071119.4166221293, 352999.5065245649, 0.0, 0.0], [1414293.276885837, -4000274.0391784506, 2841798.945818623, -1147966.3856491495, 214894.34996842145, -15219.88122456187]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    pre_muls = floatingpoint.PreOpL(lambda a, b, _: a * b, [x] * degree)

    poss_res = [0] * m
    for i in range(m):
        poss_res[i] = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res[i] += coeffA[i][j + 1] * pre_muls[j] * scaler[i][j + 1]

    comp = sfix.Array(m)
    for i in range(m):
        comp[i] = x >= breaks[i]

    cipher_index = Array(m, sfix)
    @for_range_opt(m - 1)
    def _(i):
        cipher_index[i] = comp[i + regint(1)]
        cipher_index[i] = comp[i] * (comp[i] - cipher_index[i])

    cipher_index[m - 1] = comp[m - 1]

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
    
    breaks = [-4.199999809265137, 0.5249999761581421, 1.0499999523162842, 2.0999999046325684]
    coeffA = [[-76.45729711631, 24264.43326905014, 10437.3406803093, 1157.25483922906, 0.0, 0.0], [-6257.73656271089, 93998.82312417217, -117053.68246128249, -20660.85916116651, 132308.79305899184, -54753.95330192662], [234466.111110524, -702109.3285783008, 808762.4162250392, -397610.3597488374, 92194.4228207824, -8053.52457725549], [-100740.75851828195, 179244.0532838164, -70754.23669027553, 21783.33283162431, -3352.16211992231, 203.56207708601]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    pre_muls = floatingpoint.PreOpL(lambda a, b, _: a * b, [x] * degree)

    poss_res = [0] * m
    for i in range(m):
        poss_res[i] = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res[i] += coeffA[i][j + 1] * pre_muls[j] * scaler[i][j + 1]

    comp = sfix.Array(m)
    for i in range(m):
        comp[i] = x >= breaks[i]

    cipher_index = Array(m, sfix)
    @for_range_opt(m - 1)
    def _(i):
        cipher_index[i] = comp[i + regint(1)]
        cipher_index[i] = comp[i] * (comp[i] - cipher_index[i])

    cipher_index[m - 1] = comp[m - 1]

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
    
    breaks = [-4.199999809265137, -1.0499999523162842, -0.5249999761581421, -0.26249998807907104, 0.0, 0.5249999761581421, 1.0499999523162842, 2.0999999046325684]
    coeffA = [[4647801.120607702, 10945950.991761133, 8596044.424413063, 3145923.5973398923, 550960.9164238796, 37315.54075352731], [356256.5666873912, 841187.1301867954, 2642473.3256926397, 5605604.683429097, 4040445.1865628264, 937388.8721661126], [254537.34263845373, 15758.43257791164, -62647.44989108729, 1113704.3070195606, 246934.25774914672, -370556.12491734454], [253440.2816628476, -1612.8454329183, -174100.93269161708, 790214.2341680693, 0.0, 0.0], [253440.2816628476, -11592.25011842486, -43221.61940701919, 395964.0356995764, 0.0, 0.0], [492605.29872826085, -1821123.63338244, 5289426.07963868, -7138256.395006989, 4984500.842476914, -1188830.2803905378], [-4698282.106570578, 22050064.883257657, -37698192.09061936, 30757471.17591574, -11345139.515667371, 1553297.2282204982], [-18076011.751029596, 33471723.385083534, -21944837.83860749, 7259716.396105829, -1164433.0697952847, 72855.49855224058]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    pre_muls = floatingpoint.PreOpL(lambda a, b, _: a * b, [x] * degree)

    poss_res = [0] * m
    for i in range(m):
        poss_res[i] = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res[i] += coeffA[i][j + 1] * pre_muls[j] * scaler[i][j + 1]

    comp = sfix.Array(m)
    for i in range(m):
        comp[i] = x >= breaks[i]

    cipher_index = Array(m, sfix)
    @for_range_opt(m - 1)
    def _(i):
        cipher_index[i] = comp[i + regint(1)]
        cipher_index[i] = comp[i] * (comp[i] - cipher_index[i])

    cipher_index[m - 1] = comp[m - 1]

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
    
    breaks = [-4.199999809265137, -0.5249999761581421, -0.26249998807907104, 0.0, 0.5249999761581421, 1.0499999523162842, 2.0999999046325684]
    coeffA = [[476510.52296091954, 1606258.3875400275, 1597045.6520834956, 696223.7370232834, 139277.1217464863, 10459.70867159354], [192124.32484701995, 19228.78297005558, -1215018.5798267715, -296034.034430338, 1913921.2620068316, 1317509.967360575], [194616.3965896244, 49955.92589055147, -1155816.6123193468, -790273.4800826492, 0.0, 0.0], [194616.39658962435, 76244.46654300606, -1302505.1261415435, 1510424.4104110214, 0.0, 0.0], [-9380.65096591779, 1754891.7119290126, -6756512.834539309, 10028503.168955546, -6016700.903645077, 1265152.8031196266], [4299626.457119128, -16800433.388040867, 25089722.296744585, -17179016.661379423, 5540397.1156867165, -684267.911878945], [5863456.661616043, -8459956.345526133, 5014848.276608357, -1445213.6196087778, 207045.10215290845, -11802.27598491742]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    pre_muls = floatingpoint.PreOpL(lambda a, b, _: a * b, [x] * degree)

    poss_res = [0] * m
    for i in range(m):
        poss_res[i] = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res[i] += coeffA[i][j + 1] * pre_muls[j] * scaler[i][j + 1]

    comp = sfix.Array(m)
    for i in range(m):
        comp[i] = x >= breaks[i]

    cipher_index = Array(m, sfix)
    @for_range_opt(m - 1)
    def _(i):
        cipher_index[i] = comp[i + regint(1)]
        cipher_index[i] = comp[i] * (comp[i] - cipher_index[i])

    cipher_index[m - 1] = comp[m - 1]

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
    
    breaks = [-4.199999809265137, -2.0999999046325684, -1.0499999523162842, -0.5249999761581421, 0.26249998807907104, 0.5249999761581421, 1.0499999523162842, 2.0999999046325684, 3.1499998569488525]
    coeffA = [[-12035046.548828403, 3730568.7591749774, 4548385.838268031, 1176791.6244683429, 122088.84336957501, 4292.72553153076], [-135074625.48984957, -481520591.338309, -654673900.7693357, -414654881.52897996, -125425668.90910552, -14731646.693158487], [3074696.788579976, 37545457.95505549, 92437379.99726406, 83920054.1678056, 16673883.581404038, -5031403.287642249], [-1910441.341648535, 3073535.505509655, 6964964.248093813, 1592284.4826863324, 0.0, 0.0], [-1963376.9645085458, 3927068.3025567527, 2689513.808678213, 8774423.371722333, -2592827.6693311217, 4725494.603314712], [4086681.8524228255, -41654094.28515906, 138609220.90214297, -191341589.93679821, 142370211.16862655, -36346889.91157016], [-97599276.93752594, 493794910.7661824, -924333356.6748574, 818902731.4639726, -320910636.24189246, 45919736.27241807], [-2764434260.0774765, 5196953939.50995, -3768864189.413794, 1352061830.8029425, -239272404.96697003, 16764901.22772461], [632795566.9360067, -808286783.267854, 443172179.0084578, -115427582.70489673, 14988265.802311027, -777304.6808085757]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    pre_muls = floatingpoint.PreOpL(lambda a, b, _: a * b, [x] * degree)

    poss_res = [0] * m
    for i in range(m):
        poss_res[i] = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res[i] += coeffA[i][j + 1] * pre_muls[j] * scaler[i][j + 1]

    comp = sfix.Array(m)
    for i in range(m):
        comp[i] = x >= breaks[i]

    cipher_index = Array(m, sfix)
    @for_range_opt(m - 1)
    def _(i):
        cipher_index[i] = comp[i + regint(1)]
        cipher_index[i] = comp[i] * (comp[i] - cipher_index[i])

    cipher_index[m - 1] = comp[m - 1]

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
    
    breaks = [-4.199999809265137, -1.0499999523162842, -0.5249999761581421, 0.0, 0.5249999761581421, 1.0499999523162842, 2.0999999046325684]
    coeffA = [[1003423.0729268219, 2163609.8732234645, 1603891.2767866228, 565006.1965126849, 96514.06403174678, 6430.69066986697], [334008.6610654875, -358250.94107599446, -1749553.0412728323, -1192568.8683979157, -69288.02288503211, 96102.4731838795], [376017.7065323346, -53196.30132999858, -978460.3793747444, -477418.74265525426, 0.0, 0.0], [376017.7065323346, -25437.04717174842, -953360.7586137783, 780899.6204156162, 0.0, 0.0], [287988.39645422203, 634682.0256634882, -2822307.0132651655, 3161322.4808340715, -1223287.4288992097, 127183.88327722978], [1940595.839154141, -5770990.5768180955, 6816569.656971512, -3748512.847775616, 1046877.9491735133, -118776.5941028905], [-1766036.3323193004, 2487385.419874855, -1070556.9082427488, 276483.9323075844, -35772.51408129698, 1844.07677973128]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    pre_muls = floatingpoint.PreOpL(lambda a, b, _: a * b, [x] * degree)

    poss_res = [0] * m
    for i in range(m):
        poss_res[i] = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res[i] += coeffA[i][j + 1] * pre_muls[j] * scaler[i][j + 1]

    comp = sfix.Array(m)
    for i in range(m):
        comp[i] = x >= breaks[i]

    cipher_index = Array(m, sfix)
    @for_range_opt(m - 1)
    def _(i):
        cipher_index[i] = comp[i + regint(1)]
        cipher_index[i] = comp[i] * (comp[i] - cipher_index[i])

    cipher_index[m - 1] = comp[m - 1]

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
    
    breaks = [-4.199999809265137, -2.0999999046325684, -1.5749999284744263, -1.0499999523162842, 0.26249998807907104, 0.5249999761581421, 1.0499999523162842, 1.5749999284744263, 2.0999999046325684]
    coeffA = [[5239437.005977137, 8250206.838752019, 5095859.838253729, 1549528.4118546722, 232465.6173132952, 13785.77469963145], [7678672.274153037, 23620384.94552148, 28063405.93405614, 16128877.808001302, 4504217.640379454, 491414.640584847], [-940505.6560987701, -5143685.746422461, -10402003.412541388, -9636055.844483735, -4139642.1941329483, -670481.7225392449], [-84804.1707577941, 99128.39081467837, 502262.0869610758, 340177.26910974196, 0.0, 0.0], [-83665.53326966739, 5619.86268040054, 1240404.2380455465, -860067.130058129, -1586347.8892977335, 1433545.6549973523], [-6268.06952539779, -779520.254008954, 4410398.268696785, -7248777.3210354755, 4856872.0953764105, -1172727.2169867014], [-1462068.7888289215, 6462120.176214907, -10114136.107408866, 7428245.123776052, -2611228.8214787357, 357039.18175175023], [2920961.8785642455, -7206290.284706968, 6999518.582467376, -3326808.0794216064, 781636.3121381917, -72812.01403730302], [-360562.9809073101, 568412.9885344197, -317927.0523308507, 95640.7049728158, -14270.72022394655, 843.47584522492]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    pre_muls = floatingpoint.PreOpL(lambda a, b, _: a * b, [x] * degree)

    poss_res = [0] * m
    for i in range(m):
        poss_res[i] = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res[i] += coeffA[i][j + 1] * pre_muls[j] * scaler[i][j + 1]

    comp = sfix.Array(m)
    for i in range(m):
        comp[i] = x >= breaks[i]

    cipher_index = Array(m, sfix)
    @for_range_opt(m - 1)
    def _(i):
        cipher_index[i] = comp[i + regint(1)]
        cipher_index[i] = comp[i] * (comp[i] - cipher_index[i])

    cipher_index[m - 1] = comp[m - 1]

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
    
    breaks = [-4.199999809265137, -2.0999999046325684, -1.0499999523162842, -0.5249999761581421, 0.0, 0.26249998807907104, 0.5249999761581421, 2.0999999046325684]
    coeffA = [[-17457048.02394341, -29131029.54773837, -17546699.427722156, -5121582.75212138, -738364.1568820545, -42294.28824288559], [-8850158.259606985, -40157529.35351516, -60148858.90939809, -41888722.19734856, -13751591.889683546, -1724306.0658187196], [2122252.8883944754, -128880.73162015616, -5834634.647275474, -10108597.552990964, -7828989.513544102, -2325070.2429516665], [1821042.3231265468, -1634159.3984254675, -6988841.847521152, -5457963.059657818, 0.0, 0.0], [1821042.3231265468, -1611498.0116606513, -7504176.2538124975, 960383.3121072372, 0.0, 0.0], [1825472.2253323458, -1722804.0518568314, -6170873.208833136, -6171456.321402484, 14777098.896442337, -6617434.274120291], [2553290.654825394, -3298040.191812049, -11234055.93665605, 12915827.783472035, -5871711.84964275, 939595.1103281869], [333498.7736380207, -2790957.1817348646, -1854411.1847719343, 510423.18358429737, -65728.23534419424, 3325.07850670968]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    pre_muls = floatingpoint.PreOpL(lambda a, b, _: a * b, [x] * degree)

    poss_res = [0] * m
    for i in range(m):
        poss_res[i] = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res[i] += coeffA[i][j + 1] * pre_muls[j] * scaler[i][j + 1]

    comp = sfix.Array(m)
    for i in range(m):
        comp[i] = x >= breaks[i]

    cipher_index = Array(m, sfix)
    @for_range_opt(m - 1)
    def _(i):
        cipher_index[i] = comp[i + regint(1)]
        cipher_index[i] = comp[i] * (comp[i] - cipher_index[i])

    cipher_index[m - 1] = comp[m - 1]

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

def func13_kan_model_evaluate(x):
    # dim_list required
    input_x = x
    dim_list = [(4, 9), (9, 1)]
    for l in range(len(dim_list)):
        in_dim, out_dim = dim_list[l]
        partial_result = [0]*out_dim
        for i in range(in_dim):
            for j in range(out_dim):
                partial_result[j] += neuron_func_dict[f"neuron{l}{i}{j}"](input_x[i])
        input_x = partial_result
    return input_x

def func13_kan_model_evaluate_vectorized(x):
    dim_list = [(4, 9), (9, 1)]
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
