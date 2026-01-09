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
    
    breaks = [
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-3.28125),
        sfix(-3.1499998569488525),
        sfix(-2.625),
        sfix(-2.0999999046325684),
        sfix(-1.5749999284744263),
        sfix(-1.0499999523162842),
        sfix(-0.26249998807907104),
        sfix(0.0),
        sfix(0.26249998807907104),
        sfix(0.5249999761581421),
        sfix(0.7874999642372131),
        sfix(1.181249976158142),
        sfix(1.3125),
        sfix(2.0999999046325684),
        sfix(3.1499998569488525)
    ]
    coeffA = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(3616439230.3690863), sfix(4624928127.146165), sfix(2363706851.7517104), sfix(603641091.9030477), sfix(77036745.13873388), sfix(3930507.56702495), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-7186355036.278823), sfix(-11653778454.127869), sfix(-7448294335.067922), sfix(-2353457220.2450824), sfix(-368569186.7050532), sfix(-22929722.267498165), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-2510729300.9303265), sfix(-3544173707.31419), sfix(-1841353300.0830054), sfix(-421096639.42458916), sfix(-36506136.65795512), sfix(-161599.22208519757), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(458637812.0703772), sfix(733414521.7931905), sfix(370709911.76757395), sfix(23055973.759639528), sfix(-27915241.65703419), sfix(-5318066.818051443), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(452970628.00341153), sfix(1265304031.9390502), sfix(1386932862.9483528), sfix(745812234.3810833), sfix(200304637.85718715), sfix(21711268.85457817), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-104523374.40839706), sfix(-499161535.437906), sfix(-847741909.1743182), sfix(-669843993.9294755), sfix(-248282104.04362053), sfix(-35170307.899812736), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(12398382.497104283), sfix(16235906.859019797), sfix(57338903.198912345), sfix(119170671.61681134), sfix(91648028.00040062), sfix(22348454.53480076), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(11145037.89750133), sfix(1632778.6599629961), sfix(-6007692.439678688), sfix(-2031783.7873236388), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(11145037.89750133), sfix(1484860.457050944), sfix(-8462813.29381221), sfix(-30374393.695657022), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(11404858.510622248), sfix(-2562314.6283055013), sfix(16284967.734756349), sfix(-101096049.75548463), sfix(80260996.36859906), sfix(-3685339.6462765355), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(13558249.315357734), sfix(-24877855.641143996), sfix(109106763.6765696), sfix(-294826737.3999501), sfix(283128036.06976515), sfix(-88931432.94970682), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-36472863.68018481), sfix(272271191.9783357), sfix(-600187977.8876967), sfix(556213343.8130045), sfix(-230405944.73437592), sfix(35798778.83758546), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-359002.1337601275), sfix(133130076.62615383), sfix(-390047059.0823701), sfix(401912218.80507004), sfix(-176034899.47201332), sfix(28621771.198557623), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(63822945.74625695), sfix(-154709544.29813477), sfix(104560607.08392636), sfix(-10836251.190897442), sfix(-7375890.735649839), sfix(1479650.001122026), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(766647883.9582278), sfix(-1755060622.9977746), sfix(1545414704.2090461), sfix(-650728001.790702), sfix(132390188.49510106), sfix(-10478952.99239032), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1398246818.555918), sfix(-1789446999.9775398), sfix(920606517.087938), sfix(-235828302.11825967), sfix(30187642.930144534), sfix(-1544888.7286717019), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    scaler = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    # pre_muls[j] 对应 x^(j+1)
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    col_c0 = [coeffA[i][0] for i in range(m)]
    col_s0 = [scaler[i][0] for i in range(m)]

    # 使用 dot_product 选出当前区间对应的 c 和 s
    # 此时 selected_c0 和 selected_s0 变成了 sfix (Secret)
    selected_c0 = sfix.dot_product(cipher_index, col_c0)
    selected_s0 = sfix.dot_product(cipher_index, col_s0)

    # 计算常数项结果
    final_res = selected_c0 * selected_s0

    # 4. 处理高阶项 (x^1 到 x^degree)
    for j in range(degree):
        # 提取第 j+1 列 (对应 x^(j+1))
        col_c = [coeffA[i][j+1] for i in range(m)]
        col_s = [scaler[i][j+1] for i in range(m)]

        # 选出当前区间的 c 和 s
        selected_c = sfix.dot_product(cipher_index, col_c)
        selected_s = sfix.dot_product(cipher_index, col_s)


        term = selected_c * pre_muls[j] * selected_s
        final_res += term

    return final_res


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
    
    breaks = [
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-3.674999713897705),
        sfix(-3.1499998569488525),
        sfix(-2.625),
        sfix(-2.0999999046325684),
        sfix(-1.5749999284744263),
        sfix(-1.3125),
        sfix(-1.181249976158142),
        sfix(-1.0499999523162842),
        sfix(-0.9187499284744263),
        sfix(-0.5249999761581421),
        sfix(-0.13124999403953552),
        sfix(0.0),
        sfix(0.13124999403953552),
        sfix(0.26249998807907104),
        sfix(0.7874999642372131),
        sfix(0.9187499284744263),
        sfix(1.0499999523162842),
        sfix(1.3125),
        sfix(1.5749999284744263),
        sfix(2.0999999046325684),
        sfix(2.625),
        sfix(3.1499998569488525)
    ]
    coeffA = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1717470716.3020182), sfix(2124924693.090373), sfix(1054216461.3029021), sfix(261717602.29408482), sfix(32492041.924459554), sfix(1613407.6924926646), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1880246954.1298363), sfix(-3651515422.521434), sfix(-2582064274.728873), sfix(-865472739.4901572), sfix(-140129344.5551657), sfix(-8859066.54775034), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(3508937402.7364755), sfix(8179672484.5788), sfix(7048128339.688423), sfix(2877280431.501571), sfix(565023317.1674308), sfix(43118119.11691), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-6495880114.156333), sfix(-15519325313.347488), sfix(-14580269452.431328), sfix(-6739189431.6668825), sfix(-1532656712.0760472), sfix(-137292498.65284902), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(4020794851.986863), sfix(11672624731.973312), sfix(13368239598.188519), sfix(7550505156.480912), sfix(2104919695.2685559), sfix(231787328.97753665), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1000264058.2072657), sfix(-3974092715.862406), sfix(-6162178564.092921), sfix(-4655872182.744816), sfix(-1715083018.7976696), sfix(-247112648.45341688), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-559885928.3442876), sfix(-2243717140.2358217), sfix(-3446317766.3160744), sfix(-2527238788.6925735), sfix(-881829421.3423765), sfix(-116772806.92245227), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-5545592.224364388), sfix(94658771.29879367), sfix(501773929.7710787), sfix(807847604.0970918), sfix(527703903.7453331), sfix(121669323.8066472), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(148487753.8189578), sfix(811878520.0247794), sfix(1837973637.0844972), sfix(2052898166.2061896), sfix(1107938844.3222065), sfix(229866708.3254925), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(2376676.591996944), sfix(-41181007.44804209), sfix(-161558143.79638985), sfix(-298362786.8046362), sfix(-278637026.6800961), sfix(-98066276.21156432), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(2499434.093704477), sfix(-15503500.164343465), sfix(26940150.229774263), sfix(233920095.55293152), sfix(399250474.21534574), sfix(229696957.85467264), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(2524641.482549283), sfix(-15299022.342697239), sfix(20794079.49628996), sfix(137927086.27049258), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(2524641.482549283), sfix(-15181680.311909366), sfix(24437260.60082674), sfix(216179684.09338635), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(2516212.202976983), sfix(-14967948.6923408), sfix(23221029.61469183), sfix(202670944.6668986), sfix(187596062.8438725), sfix(-611014280.2412113), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-6518874.454478913), sfix(109809182.85837619), sfix(-665077372.9857906), sfix(2113423552.8861864), sfix(-2508405885.145576), sfix(952308571.0020142), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(397997613.4913181), sfix(-2506298298.428139), sfix(6120698653.827374), sfix(-6709110880.443797), sfix(3239946803.922864), sfix(-548894923.6055914), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(842583690.090453), sfix(-4945832033.466432), sfix(11480452051.718197), sfix(-12602617424.529697), sfix(6483243588.09504), sfix(-1263499204.103663), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-352169884.9231499), sfix(398436397.3306933), sfix(1921050366.315667), sfix(-4055498902.1014395), sfix(2663286085.0038276), sfix(-580784475.1193098), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-5567331452.468433), sfix(20488521836.241257), sfix(-29089178286.665367), sfix(19918191279.338165), sfix(-6619023773.08595), sfix(859141523.0691112), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(7718741346.465064), sfix(-19286778910.803215), sfix(18580679323.683964), sfix(-8673268404.497694), sfix(1963770288.690483), sfix(-172544343.24613342), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-4425582951.576676), sfix(7219062029.585284), sfix(-4363544611.227509), sfix(1151000148.1625502), sfix(-110482824.72569048), sfix(-564835.7606725233), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1740390441.0520554), sfix(4083292530.230579), sfix(-3494236703.0421653), sfix(1404798498.9713936), sfix(-271644045.42273664), sfix(20436176.46888228), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1158821094.7879956), sfix(1450995309.7229815), sfix(-739431789.3092693), sfix(186014867.48244765), sfix(-23374702.555662986), sfix(1174188.472349832), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    scaler = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    # pre_muls[j] 对应 x^(j+1)
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    col_c0 = [coeffA[i][0] for i in range(m)]
    col_s0 = [scaler[i][0] for i in range(m)]

    # 使用 dot_product 选出当前区间对应的 c 和 s
    # 此时 selected_c0 和 selected_s0 变成了 sfix (Secret)
    selected_c0 = sfix.dot_product(cipher_index, col_c0)
    selected_s0 = sfix.dot_product(cipher_index, col_s0)

    # 计算常数项结果
    final_res = selected_c0 * selected_s0

    # 4. 处理高阶项 (x^1 到 x^degree)
    for j in range(degree):
        # 提取第 j+1 列 (对应 x^(j+1))
        col_c = [coeffA[i][j+1] for i in range(m)]
        col_s = [scaler[i][j+1] for i in range(m)]

        # 选出当前区间的 c 和 s
        selected_c = sfix.dot_product(cipher_index, col_c)
        selected_s = sfix.dot_product(cipher_index, col_s)


        term = selected_c * pre_muls[j] * selected_s
        final_res += term

    return final_res


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
    
    breaks = [
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-3.674999713897705),
        sfix(-3.1499998569488525),
        sfix(-2.625),
        sfix(-2.362499952316284),
        sfix(-2.0999999046325684),
        sfix(-1.8374998569488525),
        sfix(-1.5749999284744263),
        sfix(-1.0499999523162842),
        sfix(-0.9187499284744263),
        sfix(-0.26249998807907104),
        sfix(-0.13124999403953552),
        sfix(0.0),
        sfix(0.26249998807907104),
        sfix(0.5249999761581421),
        sfix(0.7874999642372131),
        sfix(1.3125),
        sfix(1.5749999284744263),
        sfix(1.9687498807907104),
        sfix(2.0999999046325684),
        sfix(3.1499998569488525)
    ]
    coeffA = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(21684058.195801962), sfix(26812053.858045414), sfix(13299277.202466512), sfix(3301485.092371536), sfix(409879.42272990406), sfix(20353.2710417972), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-111402185.1824308), sfix(-170283163.18835956), sfix(-102959599.76112403), sfix(-30859490.61783421), sfix(-4592581.455058332), sfix(-271818.9629100772), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(212241449.5380361), sfix(415983156.0164697), sfix(316432807.670567), sfix(117625624.94517496), sfix(21475337.15454795), sfix(1546209.4991737097), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(411411463.10686165), sfix(732865239.6326922), sfix(511762281.53034157), sfix(175017797.9551719), sfix(29263705.358472034), sfix(1907183.1488622834), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-286244071.46981776), sfix(-742263659.9588622), sfix(-736630910.3912853), sfix(-353568511.59046096), sfix(-82711969.11576755), sfix(-7587149.198363127), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-442858645.28698), sfix(-1099258949.433917), sfix(-1061699196.1106453), sfix(-501349505.23010075), sfix(-116249118.48140386), sfix(-10625998.10104879), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-11101263.071203966), sfix(90394855.039907), sfix(250684535.5748311), sfix(223189075.49820122), sfix(83927284.206245), sfix(11514861.606061507), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(94009096.87029429), sfix(351922586.9109276), sfix(484717409.86094266), sfix(304991746.42196155), sfix(87112178.87581842), sfix(8806218.688711258), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-28894620.59157112), sfix(-169947548.314845), sfix(-401093015.39974004), sfix(-446445299.1961128), sfix(-231531911.3241921), sfix(-45239569.15397305), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1138946.58236595), sfix(7847398.8874943275), sfix(22984293.39988211), sfix(62779251.84042559), sfix(76110689.79616275), sfix(29511801.415968534), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(784268.2633753059), sfix(3036675.3839014363), sfix(-3023501.4773124405), sfix(-7777587.29528493), sfix(-20777594.72517712), sfix(-24863046.19724394), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(784517.1462196787), sfix(3051320.6724579944), sfix(-2627739.8368042475), sfix(-3203586.2609077976), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(784517.1462196785), sfix(3026038.67434625), sfix(-2296344.476840771), sfix(-10703326.697290497), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(864964.8601042475), sfix(1816917.6864164672), sfix(4544532.96883726), sfix(-27471001.845369745), sfix(12622374.730245624), sfix(7162626.043760577), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(2334552.0151086547), sfix(-12182331.944668844), sfix(58497201.35690675), sfix(-132642206.2288075), sfix(116298000.73052743), sfix(-34163216.73693686), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-24470425.353261728), sfix(135554221.7205078), sfix(-267297359.2932939), sfix(226923096.5493667), sfix(-82447612.34087925), sfix(9883414.495590732), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-26892909.76687446), sfix(190154179.3910632), sfix(-424709454.08454597), sfix(407764599.8622508), sfix(-176405385.873651), sfix(28335914.05001109), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(655879056.4945782), sfix(-1944000113.7393115), sfix(2248168602.125755), sfix(-1268952120.2983186), sfix(350434034.8151254), sfix(-37997489.806510836), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-233118450.587404), sfix(314195100.76731855), sfix(-46680174.68014055), sfix(-102720902.8355847), sfix(54053645.07998011), sfix(-7865031.946220033), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(397786434.3194352), sfix(-644294681.2693826), sfix(405435216.85453814), sfix(-123376010.28139178), sfix(17981493.602263376), sfix(-986736.333100216), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(45394510.650543936), sfix(-55278978.60906178), sfix(26671875.524298754), sfix(-6447728.05345418), sfix(777298.5655166404), sfix(-37372.57984099926), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    scaler = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    # pre_muls[j] 对应 x^(j+1)
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    col_c0 = [coeffA[i][0] for i in range(m)]
    col_s0 = [scaler[i][0] for i in range(m)]

    # 使用 dot_product 选出当前区间对应的 c 和 s
    # 此时 selected_c0 和 selected_s0 变成了 sfix (Secret)
    selected_c0 = sfix.dot_product(cipher_index, col_c0)
    selected_s0 = sfix.dot_product(cipher_index, col_s0)

    # 计算常数项结果
    final_res = selected_c0 * selected_s0

    # 4. 处理高阶项 (x^1 到 x^degree)
    for j in range(degree):
        # 提取第 j+1 列 (对应 x^(j+1))
        col_c = [coeffA[i][j+1] for i in range(m)]
        col_s = [scaler[i][j+1] for i in range(m)]

        # 选出当前区间的 c 和 s
        selected_c = sfix.dot_product(cipher_index, col_c)
        selected_s = sfix.dot_product(cipher_index, col_s)


        term = selected_c * pre_muls[j] * selected_s
        final_res += term

    return final_res


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
    
    breaks = [
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-3.1499998569488525),
        sfix(-2.625),
        sfix(-2.0999999046325684),
        sfix(-1.3125),
        sfix(-1.0499999523162842),
        sfix(-0.5249999761581421),
        sfix(-0.26249998807907104),
        sfix(0.0),
        sfix(0.26249998807907104),
        sfix(0.39374998211860657),
        sfix(0.5249999761581421),
        sfix(0.7874999642372131),
        sfix(0.9187499284744263),
        sfix(1.0499999523162842),
        sfix(1.5749999284744263),
        sfix(2.0999999046325684),
        sfix(2.625),
        sfix(3.1499998569488525)
    ]
    coeffA = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(389229983.3322691), sfix(494725894.8688026), sfix(249741552.90932104), sfix(62855003.45751845), sfix(7899305.148129828), sfix(396811.6957526831), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1434029558.3578422), sfix(2760676390.635263), sfix(2074781615.8132033), sfix(765352545.3951309), sfix(139068638.2940593), sfix(9983718.212350242), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1755983899.8482854), sfix(-4079324217.2516165), sfix(-3727809409.14771), sfix(-1674368093.9732244), sfix(-370155870.1001553), sfix(-32278520.776931882), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(597396584.3328961), sfix(1742179367.6366584), sfix(2004291898.9821327), sfix(1134501524.1709127), sfix(314931349.0321603), sfix(34259817.465209365), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-104738982.10658826), sfix(-503982545.8101714), sfix(-839283559.9001642), sfix(-641365575.973208), sfix(-229957976.82818395), sfix(-31036612.34512762), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(14566219.706130296), sfix(56839722.0374122), sfix(219197127.29999098), sfix(361446153.1415161), sfix(247019548.13894665), sfix(60092192.15946249), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(7221454.807973992), sfix(-7038343.030208091), sfix(-6144583.855889663), sfix(-42365717.96456648), sfix(-121080490.06201985), sfix(-76554615.32868578), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(7128972.8959309), sfix(-7943307.090573911), sfix(-4346221.8420335455), sfix(-985931.3372335639), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(7128972.8959309), sfix(-8101964.951269725), sfix(-12301175.145982893), sfix(-37141062.09808268), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(7402027.371347465), sfix(-13064747.084333783), sfix(24425081.194308363), sfix(-164396031.0448222), sfix(166068587.79531616), sfix(9849174.34581782), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(9623419.062032394), sfix(-40730232.46329313), sfix(162992188.90258807), sfix(-513374223.8853005), sfix(608063811.8611598), sfix(-215386313.74466938), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(9615388.033345278), sfix(-46621811.56514427), sfix(206358609.74164477), sfix(-632814308.5881702), sfix(754427050.366694), sfix(-282769454.4479879), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-87151510.2128543), sfix(575239495.4922997), sfix(-1397149258.1414886), sfix(1441042705.0860372), sfix(-590857875.2483575), sfix(67379867.27340285), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-231402304.81094226), sfix(1362039331.75473), sfix(-3115579800.0624213), sfix(3319622985.6318226), sfix(-1618766995.5461938), sfix(292592510.9980768), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(269229481.8133899), sfix(-692107183.9754382), sfix(235914722.46254298), sfix(604043253.6261169), sfix(-527361111.7015406), sfix(118815541.6028429), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1862477932.3933094), sfix(-6684110213.298701), sfix(9058205595.696407), sfix(-5790473159.330803), sfix(1763318204.2456622), sfix(-206518383.05943555), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-8361927761.79148), sfix(19681623006.625732), sfix(-18015513615.625103), sfix(8058166868.659677), sfix(-1767591693.3522656), sfix(152647590.9099045), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(9083876910.487204), sfix(-16314730441.017508), sfix(11568379625.418869), sfix(-4055076928.1728716), sfix(704662751.3189495), sfix(-48643291.44226636), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-558365472.3811022), sfix(755480439.5683209), sfix(-399921738.42959243), sfix(106957589.07030365), sfix(-14267446.829479126), sfix(759206.57075868), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    scaler = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    # pre_muls[j] 对应 x^(j+1)
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    col_c0 = [coeffA[i][0] for i in range(m)]
    col_s0 = [scaler[i][0] for i in range(m)]

    # 使用 dot_product 选出当前区间对应的 c 和 s
    # 此时 selected_c0 和 selected_s0 变成了 sfix (Secret)
    selected_c0 = sfix.dot_product(cipher_index, col_c0)
    selected_s0 = sfix.dot_product(cipher_index, col_s0)

    # 计算常数项结果
    final_res = selected_c0 * selected_s0

    # 4. 处理高阶项 (x^1 到 x^degree)
    for j in range(degree):
        # 提取第 j+1 列 (对应 x^(j+1))
        col_c = [coeffA[i][j+1] for i in range(m)]
        col_s = [scaler[i][j+1] for i in range(m)]

        # 选出当前区间的 c 和 s
        selected_c = sfix.dot_product(cipher_index, col_c)
        selected_s = sfix.dot_product(cipher_index, col_s)


        term = selected_c * pre_muls[j] * selected_s
        final_res += term

    return final_res


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
    
    breaks = [
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-3.4124999046325684),
        sfix(-3.1499998569488525),
        sfix(-2.8874998092651367),
        sfix(-2.362499952316284),
        sfix(-2.0999999046325684),
        sfix(-1.5749999284744263),
        sfix(-1.0499999523162842),
        sfix(-0.5249999761581421),
        sfix(-0.26249998807907104),
        sfix(0.0),
        sfix(0.13124999403953552),
        sfix(0.5249999761581421),
        sfix(1.0499999523162842),
        sfix(1.5749999284744263),
        sfix(2.0999999046325684),
        sfix(2.625),
        sfix(3.1499998569488525)
    ]
    coeffA = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(3137004841.4970493), sfix(3980689985.172318), sfix(2018467213.2387803), sfix(511424736.80025077), sfix(64758308.41032018), sfix(3278465.815726379), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-10713031188.610281), sfix(-16617765152.219448), sfix(-10230585233.180504), sfix(-3129253878.4816437), sfix(-476109125.0877615), sfix(-28853214.1329445), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-9157536384.980827), sfix(-13680014922.156458), sfix(-8065945285.864704), sfix(-2346405355.9415817), sfix(-336559564.43125314), sfix(-19015290.837828673), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(16592982334.500963), sfix(30261582612.4434), sfix(21908161426.86294), sfix(7869514972.058027), sfix(1402992017.496073), sfix(99365303.0311725), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-17227846390.77798), sfix(-38826003618.02408), sfix(-34571625902.20835), sfix(-15229060476.83979), sfix(-3322945881.0140324), sfix(-287627322.26333463), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(6148980159.508625), sfix(18203033536.288494), sfix(21148008609.439613), sfix(12024272631.597258), sfix(3349971511.3002815), sfix(366663145.6475606), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-879517033.8401076), sfix(-4038157374.101683), sfix(-7059204307.94199), sfix(-5898133059.027227), sfix(-2355346780.084597), sfix(-361301240.9945366), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(32779761.653149523), sfix(182975120.98425466), sfix(812116440.6936592), sfix(1499980357.9608068), sfix(1150638894.0922663), sfix(309040853.7259203), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(15094974.332790047), sfix(12528356.343539597), sfix(151574299.86040947), sfix(211784933.55000743), sfix(-114827434.19888626), sfix(-192231591.868756), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(14255784.639454182), sfix(619375.6006812444), sfix(96401487.47878978), sfix(144932668.63234276), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(14255784.639454182), sfix(-298994.0716474716), sfix(82860466.37308031), sfix(-77649898.96324164), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(14322619.039294789), sfix(-1527707.205595356), sfix(85889406.55677144), sfix(-13609156.018264985), sfix(-389016910.46319914), sfix(331285039.52265245), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(44064633.89144496), sfix(-267849928.3119221), sfix(1059426033.2378017), sfix(-1834616646.467992), sfix(1356857531.1736405), sfix(-355234017.338795), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1254012774.063825), sfix(5605454544.284028), sfix(-9628637041.976192), sfix(7948863827.920726), sfix(-3150018167.5678678), sfix(480969590.97197205), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(8583588647.199743), sfix(-25407023271.854435), sfix(29544435025.873444), sfix(-16834868139.225626), sfix(4703868541.612967), sfix(-516361031.66826063), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-17369219420.76371), sfix(39717890006.03846), sfix(-35706872310.595245), sfix(15804960360.536776), sfix(-3449395134.3760796), sfix(297448203.18996924), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(13439963023.393871), sfix(-25173513621.21955), sfix(18549576441.167927), sfix(-6735359596.898551), sfix(1208187407.7292473), sfix(-85813884.45267282), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(2570680533.897), sfix(-3220489343.385949), sfix(1618464811.2755566), sfix(-405501147.99991), sfix(50766296.96823479), sfix(-2540830.4320435748), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    scaler = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    # pre_muls[j] 对应 x^(j+1)
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    col_c0 = [coeffA[i][0] for i in range(m)]
    col_s0 = [scaler[i][0] for i in range(m)]

    # 使用 dot_product 选出当前区间对应的 c 和 s
    # 此时 selected_c0 和 selected_s0 变成了 sfix (Secret)
    selected_c0 = sfix.dot_product(cipher_index, col_c0)
    selected_s0 = sfix.dot_product(cipher_index, col_s0)

    # 计算常数项结果
    final_res = selected_c0 * selected_s0

    # 4. 处理高阶项 (x^1 到 x^degree)
    for j in range(degree):
        # 提取第 j+1 列 (对应 x^(j+1))
        col_c = [coeffA[i][j+1] for i in range(m)]
        col_s = [scaler[i][j+1] for i in range(m)]

        # 选出当前区间的 c 和 s
        selected_c = sfix.dot_product(cipher_index, col_c)
        selected_s = sfix.dot_product(cipher_index, col_s)


        term = selected_c * pre_muls[j] * selected_s
        final_res += term

    return final_res


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
    
    breaks = [
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-3.674999713897705),
        sfix(-3.28125),
        sfix(-3.1499998569488525),
        sfix(-2.625),
        sfix(-2.0999999046325684),
        sfix(-1.4437499046325684),
        sfix(-1.3125),
        sfix(-1.181249976158142),
        sfix(-1.0499999523162842),
        sfix(-0.5249999761581421),
        sfix(0.0),
        sfix(0.26249998807907104),
        sfix(0.5249999761581421),
        sfix(1.0499999523162842),
        sfix(1.5749999284744263),
        sfix(1.8374998569488525),
        sfix(2.625),
        sfix(3.1499998569488525)
    ]
    coeffA = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1144425455.7497973), sfix(-1423656113.526964), sfix(-707575040.9710205), sfix(-175737359.30574697), sfix(-21816154.269331887), sfix(-1083033.1080991342), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-3446754420.483639), sfix(-4307035764.993263), sfix(-2141488910.6715515), sfix(-529149236.0624719), sfix(-64898125.00556309), sfix(-3155294.7358619883), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(8939326368.449236), sfix(14303640980.645718), sfix(9046642034.652264), sfix(2834662609.500768), sfix(440910469.01443315), sfix(27275447.607184313), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1974084092.2097132), sfix(2358851961.4968615), sfix(871036996.6594124), sfix(42425435.96981518), sfix(-35023416.902207874), sfix(-5117818.058600978), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-177050711.23875928), sfix(57772755.14315656), sfix(486489640.93200374), sfix(418452018.55683357), sfix(136556602.531991), sfix(15619548.059613049), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-580103350.7421774), sfix(-1610183881.397942), sfix(-1761944547.7370594), sfix(-960450070.510129), sfix(-263933308.93411323), sfix(-29303289.919429205), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(272716620.46670055), sfix(1099718604.3288624), sfix(1683308109.0512595), sfix(1230467947.912758), sfix(433056128.87606245), sfix(59446752.096556306), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(140925774.61987796), sfix(593924227.7445321), sfix(906484568.289321), sfix(633655587.2425817), sfix(203696228.0743936), sfix(24173263.029975228), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(13568665.297705028), sfix(56364095.211216), sfix(-1689312.563395282), sfix(-133989823.45019116), sfix(-120944599.79190736), sfix(-30779192.82486516), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-13089008.919675186), sfix(-49163653.85047841), sfix(-155693689.02391446), sfix(-229114502.9794915), sfix(-138025524.7492259), sfix(-27869667.639329243), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-5584224.739085414), sfix(6982923.987504337), sfix(6864173.869938853), sfix(-6541741.939129969), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-5584224.739085414), sfix(7274357.395993634), sfix(11108350.177624738), sfix(2907399.4233912877), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-5653492.892748831), sfix(8404257.844914714), sfix(3465277.448746468), sfix(28366528.82971789), sfix(-35910967.240301885), sfix(7486267.804912958), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-4484433.137063849), sfix(1331441.527453024), sfix(17475834.0129299), sfix(22387093.090704948), sfix(-46983891.82411776), sfix(17238417.077540852), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(29987007.568710506), sfix(-180393365.68953922), sfix(399235600.00823003), sfix(-377757837.23730016), sfix(162528124.14391539), sfix(-26635855.39660931), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-626398893.8277651), sfix(1951430594.232265), sfix(-2377246617.003178), sfix(1434777015.4086049), sfix(-430540042.7103453), sfix(51169823.8283509), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(2289526376.9154344), sfix(-5577345521.959752), sfix(5400746994.002108), sfix(-2584383156.3847795), sfix(608296656.1936427), sfix(-56281928.41907331), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(280306795.0527111), sfix(600929452.5422661), sfix(-1144805687.828865), sfix(629766477.2960238), sfix(-145522100.43324468), sfix(12308221.180011172), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-2581919963.4332666), sfix(3287083215.5989285), sfix(-1676614669.788579), sfix(426867267.5824492), sfix(-54317291.867978536), sfix(2763544.5491800974), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    scaler = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    # pre_muls[j] 对应 x^(j+1)
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    col_c0 = [coeffA[i][0] for i in range(m)]
    col_s0 = [scaler[i][0] for i in range(m)]

    # 使用 dot_product 选出当前区间对应的 c 和 s
    # 此时 selected_c0 和 selected_s0 变成了 sfix (Secret)
    selected_c0 = sfix.dot_product(cipher_index, col_c0)
    selected_s0 = sfix.dot_product(cipher_index, col_s0)

    # 计算常数项结果
    final_res = selected_c0 * selected_s0

    # 4. 处理高阶项 (x^1 到 x^degree)
    for j in range(degree):
        # 提取第 j+1 列 (对应 x^(j+1))
        col_c = [coeffA[i][j+1] for i in range(m)]
        col_s = [scaler[i][j+1] for i in range(m)]

        # 选出当前区间的 c 和 s
        selected_c = sfix.dot_product(cipher_index, col_c)
        selected_s = sfix.dot_product(cipher_index, col_s)


        term = selected_c * pre_muls[j] * selected_s
        final_res += term

    return final_res


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
    
    breaks = [
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-3.1499998569488525),
        sfix(-2.8874998092651367),
        sfix(-2.625),
        sfix(-2.0999999046325684),
        sfix(-1.5749999284744263),
        sfix(-1.0499999523162842),
        sfix(-0.9187499284744263),
        sfix(-0.65625),
        sfix(-0.5249999761581421),
        sfix(-0.13124999403953552),
        sfix(0.0),
        sfix(0.13124999403953552),
        sfix(0.5249999761581421),
        sfix(0.7874999642372131),
        sfix(0.9187499284744263),
        sfix(1.181249976158142),
        sfix(1.3125),
        sfix(1.5749999284744263),
        sfix(2.0999999046325684),
        sfix(2.625),
        sfix(3.1499998569488525)
    ]
    coeffA = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(524439115.9432063), sfix(671363686.9701082), sfix(343297911.17474246), sfix(87705713.09929557), sfix(11197556.95901687), sfix(571578.0481851717), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-893805316.7490195), sfix(-1412264738.4813015), sfix(-877698543.8182479), sfix(-268886604.2121896), sfix(-40680723.260102764), sfix(-2434439.767378893), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1765599087.2103062), sfix(3190589630.1387873), sfix(2310126622.6273327), sfix(835437042.5397922), sfix(150671231.21070582), sfix(10833208.672690999), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-719998532.3954556), sfix(-1826918910.8678958), sfix(-1739225883.4131455), sfix(-797779380.9541445), sfix(-178537503.1592481), sfix(-15698528.192135913), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-313320650.01688397), sfix(-422059956.0948365), sfix(23233051.357215438), sfix(248549179.96938515), sfix(121247045.94304864), sfix(17824371.12843536), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(274808251.8007342), sfix(856403543.1343194), sfix(886251981.1781448), sfix(302230079.04026324), sfix(-23297037.203478266), sfix(-21777018.022699013), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-193321001.06792137), sfix(-1089680395.2122953), sfix(-2337293481.3121834), sfix(-2356142771.6074004), sfix(-1114176471.4033303), sfix(-199850489.98358986), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-17560648.867685594), sfix(-102532444.39287965), sfix(-114205694.79780358), sfix(152951760.45116305), sfix(304946603.7190158), sfix(121890781.85595177), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(16824362.938984495), sfix(134663998.27602145), sfix(539583471.376989), sfix(1052988678.3753682), sfix(923760236.8697866), sfix(291871022.75850576), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(6070969.081743761), sfix(22769148.899964783), sfix(66480999.361787885), sfix(38035220.81022305), sfix(-179081126.93870157), sfix(-192597382.1400587), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5953742.833968919), sfix(20300825.838110723), sfix(50488374.21877637), sfix(27811735.733714946), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5953742.833968921), sfix(20108468.915252846), sfix(50530184.029090926), sfix(-95359824.07260275), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(6035326.235554615), sfix(18483600.00314223), sfix(58715204.25029781), sfix(-69761881.09939384), sfix(-261321235.70057434), sfix(265796721.86941957), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(23845555.484331578), sfix(-152527289.9227029), sfix(727807929.4709991), sfix(-1404396009.789366), sfix(1095764181.726507), sfix(-296313178.6265189), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(2577068.715283048), sfix(-25436635.899316296), sfix(425843177.1876353), sfix(-1048309670.7141709), sfix(887747994.6681919), sfix(-248276725.01986745), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-223950429.68286446), sfix(1153018016.1518414), sfix(-2030325212.597963), sfix(1515707046.8254921), sfix(-453019211.1511933), sfix(32716266.555718333), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-759130885.9890696), sfix(3480396491.907554), sfix(-6084717989.101111), sfix(5052140800.999053), sfix(-1997429862.405813), sfix(302852187.3407518), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-415762693.600783), sfix(2288624332.8113704), sfix(-4438371596.50333), sfix(3921587958.739288), sfix(-1611915351.3836045), sfix(250701172.18531966), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5135689376.175609), sfix(-15105142851.822086), sfix(17394182603.65294), sfix(-9801811160.429733), sfix(2707998173.699223), sfix(-294104977.89757913), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-9723076787.939379), sfix(21876175406.00577), sfix(-19387282653.28776), sfix(8475407404.588698), sfix(-1830295570.7243776), sfix(156425727.54002592), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(6762744963.813578), sfix(-12523673256.064476), sfix(9150848399.166061), sfix(-3302197969.342451), sfix(589568659.3302234), sfix(-41722853.57777357), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1310555449.7632854), sfix(-1646447759.498839), sfix(828526790.9891926), sfix(-208096167.60953614), sfix(26119342.58147298), sfix(-1310716.013421729), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    scaler = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    # pre_muls[j] 对应 x^(j+1)
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    col_c0 = [coeffA[i][0] for i in range(m)]
    col_s0 = [scaler[i][0] for i in range(m)]

    # 使用 dot_product 选出当前区间对应的 c 和 s
    # 此时 selected_c0 和 selected_s0 变成了 sfix (Secret)
    selected_c0 = sfix.dot_product(cipher_index, col_c0)
    selected_s0 = sfix.dot_product(cipher_index, col_s0)

    # 计算常数项结果
    final_res = selected_c0 * selected_s0

    # 4. 处理高阶项 (x^1 到 x^degree)
    for j in range(degree):
        # 提取第 j+1 列 (对应 x^(j+1))
        col_c = [coeffA[i][j+1] for i in range(m)]
        col_s = [scaler[i][j+1] for i in range(m)]

        # 选出当前区间的 c 和 s
        selected_c = sfix.dot_product(cipher_index, col_c)
        selected_s = sfix.dot_product(cipher_index, col_s)


        term = selected_c * pre_muls[j] * selected_s
        final_res += term

    return final_res


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
    
    breaks = [
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-3.1499998569488525),
        sfix(-2.625),
        sfix(-1.5749999284744263),
        sfix(-0.7874999642372131),
        sfix(-0.5249999761581421),
        sfix(0.5249999761581421),
        sfix(1.0499999523162842),
        sfix(2.0999999046325684),
        sfix(3.1499998569488525)
    ]
    coeffA = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1678878438.6972497), sfix(2142371953.303184), sfix(1095076112.8819544), sfix(279945390.6995123), sfix(35775756.51381536), sfix(1828105.5002378537), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1176301526.3134785), sfix(-1627687656.243131), sfix(-818395598.4751405), sfix(-175858798.59722745), sfix(-12578389.668560863), sfix(280036.41186926817), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-480637178.06097734), sfix(-1266839994.5207195), sfix(-1303818017.6351368), sfix(-661639651.2455014), sfix(-164825633.36287525), sfix(-16075327.251699088), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(2160533.9905364797), sfix(24404111.87793137), sfix(45179344.129935734), sfix(17834632.05093615), sfix(-3739003.526550007), sfix(-2455921.2659229483), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-6374464.232776794), sfix(-10043170.424269715), sfix(-2013789.3013385034), sfix(-1352539.0054402351), sfix(4521251.425748792), sfix(3726515.4510599156), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-6171905.2214190755), sfix(-8749250.58114936), sfix(450984.85031258094), sfix(-1298936.3252836515), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-5764173.865164688), sfix(-12517887.550859584), sfix(14776294.913585087), sfix(-28623502.99804778), sfix(24323095.26526642), sfix(-6806397.460680919), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(47256842.299476735), sfix(-186510304.681652), sfix(226226158.87230453), sfix(-139269945.00358433), sfix(43019235.95943307), sfix(-5310365.2256423505), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(2218542312.5323744), sfix(-4414152219.920319), sfix(3437731973.3144846), sfix(-1317576117.2114017), sfix(248340706.34539908), sfix(-18453946.08526357), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1389830709.0863621), sfix(-1777894625.643091), sfix(901160801.5060817), sfix(-229768671.64564866), sfix(29288683.894743837), sfix(-1492889.4385139043), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    scaler = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    # pre_muls[j] 对应 x^(j+1)
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    col_c0 = [coeffA[i][0] for i in range(m)]
    col_s0 = [scaler[i][0] for i in range(m)]

    # 使用 dot_product 选出当前区间对应的 c 和 s
    # 此时 selected_c0 和 selected_s0 变成了 sfix (Secret)
    selected_c0 = sfix.dot_product(cipher_index, col_c0)
    selected_s0 = sfix.dot_product(cipher_index, col_s0)

    # 计算常数项结果
    final_res = selected_c0 * selected_s0

    # 4. 处理高阶项 (x^1 到 x^degree)
    for j in range(degree):
        # 提取第 j+1 列 (对应 x^(j+1))
        col_c = [coeffA[i][j+1] for i in range(m)]
        col_s = [scaler[i][j+1] for i in range(m)]

        # 选出当前区间的 c 和 s
        selected_c = sfix.dot_product(cipher_index, col_c)
        selected_s = sfix.dot_product(cipher_index, col_s)


        term = selected_c * pre_muls[j] * selected_s
        final_res += term

    return final_res


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
    
    breaks = [
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-3.674999713897705),
        sfix(-3.1499998569488525),
        sfix(-2.625),
        sfix(-2.0999999046325684),
        sfix(-1.9687498807907104),
        sfix(-1.0499999523162842),
        sfix(-0.5249999761581421),
        sfix(0.0),
        sfix(0.5249999761581421),
        sfix(1.0499999523162842),
        sfix(2.0999999046325684),
        sfix(3.1499998569488525)
    ]
    coeffA = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(147188397.14744556), sfix(181578135.4113617), sfix(89997345.91606744), sfix(22337338.07443113), sfix(2773267.5640262393), sfix(137725.65148739595), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-177146533.69488972), sfix(-336044412.18450534), sfix(-234375814.134825), sfix(-77859898.0434927), sfix(-12528152.772860924), sfix(-788443.104750221), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(111415274.82930219), sfix(396805298.95097), sfix(408386750.8945408), sfix(183563927.93562096), sfix(38253287.545809336), sfix(3037628.498587371), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-305269929.3673249), sfix(-768607322.4870267), sfix(-764768426.1692442), sfix(-373005447.58242536), sfix(-88881142.17140035), sfix(-8279382.399202606), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-279936745.4750572), sfix(-615163197.4471374), sfix(-535440199.5783692), sfix(-226667036.49338567), sfix(-45755394.51092583), sfix(-3433473.1390374526), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-7520498.428554039), sfix(-44758995.25692896), sfix(-100522939.58736596), sfix(-91291950.0295716), sfix(-36544010.114039056), sfix(-5444420.554491154), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-117317.32623742719), sfix(8667164.06140134), sfix(24870869.260594606), sfix(41698399.943435684), sfix(29639656.988927215), sfix(7128114.894755943), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1338063.7671894243), sfix(-673174.6380393185), sfix(-3474043.9907682464), sfix(-436407.4929891172), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1338063.7671894243), sfix(-608837.0233397323), sfix(-3825972.2198007563), sfix(1786473.959097091), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1136907.5485479701), sfix(-2298336.836457273), sfix(2205279.0824288023), sfix(-9302214.151434023), sfix(9703037.796776727), sfix(-2735348.1873896243), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-45450467.389988065), sfix(167492346.51664796), sfix(-256592790.32053387), sfix(186886299.1325061), sfix(-64267941.99526223), sfix(8357560.167532316), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1069573091.1724659), sfix(2019994476.0782409), sfix(-1501982367.8523257), sfix(549505619.8533298), sfix(-99271027.52032375), sfix(7098094.9147649), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-231361304.6337547), sfix(290758718.2920795), sfix(-148036270.97217333), sfix(37327594.64772389), sfix(-4702375.659466738), sfix(236828.04697902987), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    scaler = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    # pre_muls[j] 对应 x^(j+1)
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    col_c0 = [coeffA[i][0] for i in range(m)]
    col_s0 = [scaler[i][0] for i in range(m)]

    # 使用 dot_product 选出当前区间对应的 c 和 s
    # 此时 selected_c0 和 selected_s0 变成了 sfix (Secret)
    selected_c0 = sfix.dot_product(cipher_index, col_c0)
    selected_s0 = sfix.dot_product(cipher_index, col_s0)

    # 计算常数项结果
    final_res = selected_c0 * selected_s0

    # 4. 处理高阶项 (x^1 到 x^degree)
    for j in range(degree):
        # 提取第 j+1 列 (对应 x^(j+1))
        col_c = [coeffA[i][j+1] for i in range(m)]
        col_s = [scaler[i][j+1] for i in range(m)]

        # 选出当前区间的 c 和 s
        selected_c = sfix.dot_product(cipher_index, col_c)
        selected_s = sfix.dot_product(cipher_index, col_s)


        term = selected_c * pre_muls[j] * selected_s
        final_res += term

    return final_res


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
    
    breaks = [
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-3.937499761581421),
        sfix(-3.674999713897705),
        sfix(-3.4124999046325684),
        sfix(-3.1499998569488525),
        sfix(-2.625),
        sfix(-2.0999999046325684),
        sfix(-1.5749999284744263),
        sfix(-1.0499999523162842),
        sfix(-0.5249999761581421),
        sfix(-0.39374998211860657),
        sfix(0.0),
        sfix(0.39374998211860657),
        sfix(1.0499999523162842),
        sfix(1.5749999284744263),
        sfix(2.0999999046325684),
        sfix(2.625),
        sfix(3.1499998569488525),
        sfix(3.4124999046325684)
    ]
    coeffA = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(107815449.343234), sfix(131034683.65238065), sfix(63704724.2660541), sfix(15485368.105163895), sfix(1882027.3811575253), sfix(91489.39270282524), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1854328314.573992), sfix(2368529222.810737), sfix(1210510283.3079095), sfix(309428894.5844), sfix(39559605.37060899), sfix(2023616.3120681955), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(3672660555.669171), sfix(4806871087.481933), sfix(2518368935.601835), sfix(660165178.4334154), sfix(86587224.20509341), sfix(4545739.787631272), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-2715415470.736259), sfix(-4636001689.623619), sfix(-3066295953.986497), sfix(-991634766.4507664), sfix(-157746550.8950784), sfix(-9914104.670011844), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-2619241304.180907), sfix(-3987537362.166164), sfix(-2328279007.3513536), sfix(-649940874.1738858), sfix(-85828185.65965538), sfix(-4183277.8239233154), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1765282940.9760368), sfix(3579690281.3984976), sfix(2846751151.315481), sfix(1098757770.7919853), sfix(205158164.97461358), sfix(14797569.382843453), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-727996798.1074991), sfix(-2010027295.6376424), sfix(-2158085257.738129), sfix(-1137673197.4419215), sfix(-293422147.0834754), sfix(-29546435.85495797), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(119374831.28259142), sfix(471142618.0041103), sfix(733445122.0075243), sfix(536557094.9465524), sfix(187358347.71920207), sfix(25100270.57256498), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-9026299.104332004), sfix(-22235789.030517835), sfix(12324891.687337387), sfix(54770693.0957639), sfix(55294285.319962785), sfix(18686664.852299917), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-4283584.9441987835), sfix(8887755.50116054), sfix(87543731.71517125), sfix(131715706.27077271), sfix(78191703.88023788), sfix(12176738.716893217), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-5052175.8145010015), sfix(-534029.6228437171), sfix(43914989.840072885), sfix(40192608.55451725), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-5052175.8145010015), sfix(-1381768.9927433897), sfix(45675387.41911158), sfix(-40223522.9764344), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-2460825.494853012), sfix(-28053267.769301336), sfix(151912498.03121036), sfix(-239021651.94157082), sfix(165417819.34196734), sfix(-42321879.498960085), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-52175038.771261185), sfix(232418004.5283147), sfix(-394662753.8137652), sfix(335532476.83470917), sfix(-137240504.98646653), sfix(21600891.4891021), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(197502211.01561746), sfix(-649376064.8210936), sfix(837884629.1054538), sfix(-518874514.61888653), sfix(157024833.79561102), sfix(-18737130.53111653), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(213308393.84620443), sfix(-109752850.44332911), sfix(-218379817.30267447), sfix(239687535.02782977), sfix(-84004273.70598373), sfix(9950365.67576534), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1673286923.981911), sfix(2189925105.465688), sfix(-985141787.5544311), sfix(155756531.3635277), sfix(3885211.5927452357), sfix(-2257183.359111653), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-3950972848.1272383), sfix(6542936052.741792), sfix(-4235309338.2099895), sfix(1347921878.912633), sfix(-211790464.82637686), sfix(13180808.830273904), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(2443686121.7285547), sfix(-3099488372.1889157), sfix(1571864299.6387353), sfix(-398415955.23296356), sfix(50471046.30974972), sfix(-2556319.591870558), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    scaler = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    # pre_muls[j] 对应 x^(j+1)
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    col_c0 = [coeffA[i][0] for i in range(m)]
    col_s0 = [scaler[i][0] for i in range(m)]

    # 使用 dot_product 选出当前区间对应的 c 和 s
    # 此时 selected_c0 和 selected_s0 变成了 sfix (Secret)
    selected_c0 = sfix.dot_product(cipher_index, col_c0)
    selected_s0 = sfix.dot_product(cipher_index, col_s0)

    # 计算常数项结果
    final_res = selected_c0 * selected_s0

    # 4. 处理高阶项 (x^1 到 x^degree)
    for j in range(degree):
        # 提取第 j+1 列 (对应 x^(j+1))
        col_c = [coeffA[i][j+1] for i in range(m)]
        col_s = [scaler[i][j+1] for i in range(m)]

        # 选出当前区间的 c 和 s
        selected_c = sfix.dot_product(cipher_index, col_c)
        selected_s = sfix.dot_product(cipher_index, col_s)


        term = selected_c * pre_muls[j] * selected_s
        final_res += term

    return final_res


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
    
    breaks = [
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-3.1499998569488525),
        sfix(-2.0999999046325684),
        sfix(-1.0499999523162842),
        sfix(-0.5249999761581421),
        sfix(0.0),
        sfix(0.13124999403953552),
        sfix(0.26249998807907104),
        sfix(1.0499999523162842),
        sfix(2.0999999046325684),
        sfix(3.1499998569488525)
    ]
    coeffA = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1572147444.28442), sfix(-2002492494.5059175), sfix(-1021572075.4070663), sfix(-260636206.3547066), sfix(-33242279.132628366), sfix(-1695329.6083342498), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-2596495063.8420277), sfix(-5086976880.026803), sfix(-3934951757.7987714), sfix(-1499013184.323009), sfix(-281396393.9481827), sfix(-20854442.758180074), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-37875455.1619063), sfix(-97672695.95366862), sfix(-165766587.90181178), sfix(-143419250.7462367), sfix(-57227688.328953855), sfix(-8399133.590805296), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-4232495.751008144), sfix(23496550.941794705), sfix(3902291.9214052293), sfix(-29455272.074338093), sfix(-21457802.760327026), sfix(-4461006.622038804), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-4318141.106580573), sfix(23527022.96025839), sfix(8864292.905515775), sfix(-10670485.693140266), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-4318141.106580573), sfix(23181675.122693114), sfix(4827830.05662008), sfix(-21597333.97216287), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-4317778.055725045), sfix(23169789.882001724), sfix(4992978.3639322715), sfix(-22512124.26721278), sfix(-738830.8578835113), sfix(16419643.426988672), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-4232684.544004348), sfix(21672537.963734224), sfix(15007505.239167115), sfix(-54822581.793223895), sfix(50295811.25298907), sfix(-15686805.192113228), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(12431716.859698828), sfix(-42871570.58092947), sfix(95214554.19904283), sfix(-76657298.06370862), sfix(27952266.192063894), sfix(-3844768.4258152386), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-287535252.49773234), sfix(544056245.7556132), sfix(-383304255.03980345), sfix(132775430.79162684), sfix(-22403683.054260876), sfix(1479721.306925988), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(162406491.01576486), sfix(-207228512.38685703), sfix(112859302.42547843), sfix(-29321928.114453744), sfix(3798954.1469519953), sfix(-196605.12737792116), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    scaler = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    # pre_muls[j] 对应 x^(j+1)
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    col_c0 = [coeffA[i][0] for i in range(m)]
    col_s0 = [scaler[i][0] for i in range(m)]

    # 使用 dot_product 选出当前区间对应的 c 和 s
    # 此时 selected_c0 和 selected_s0 变成了 sfix (Secret)
    selected_c0 = sfix.dot_product(cipher_index, col_c0)
    selected_s0 = sfix.dot_product(cipher_index, col_s0)

    # 计算常数项结果
    final_res = selected_c0 * selected_s0

    # 4. 处理高阶项 (x^1 到 x^degree)
    for j in range(degree):
        # 提取第 j+1 列 (对应 x^(j+1))
        col_c = [coeffA[i][j+1] for i in range(m)]
        col_s = [scaler[i][j+1] for i in range(m)]

        # 选出当前区间的 c 和 s
        selected_c = sfix.dot_product(cipher_index, col_c)
        selected_s = sfix.dot_product(cipher_index, col_s)


        term = selected_c * pre_muls[j] * selected_s
        final_res += term

    return final_res


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
    
    breaks = [
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-3.1499998569488525),
        sfix(-2.8874998092651367),
        sfix(-2.362499952316284),
        sfix(-2.0999999046325684),
        sfix(-1.8374998569488525),
        sfix(-1.5749999284744263),
        sfix(-0.5249999761581421),
        sfix(-0.26249998807907104),
        sfix(0.26249998807907104),
        sfix(1.0499999523162842),
        sfix(2.0999999046325684),
        sfix(3.1499998569488525)
    ]
    coeffA = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-342217222.916916), sfix(-437102714.3522922), sfix(-222694854.97260487), sfix(-56659225.937957056), sfix(-7202898.7653946625), sfix(-366096.54962056864), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1013198198.4067419), sfix(1559660268.2848713), sfix(951282884.2391059), sfix(287577273.1555715), sfix(43120249.341992415), sfix(2566836.4568930566), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1247758275.5496867), sfix(-2350454110.6280828), sfix(-1754166070.889586), sfix(-648578803.2012544), sfix(-118878800.90347427), sfix(-8648649.109839428), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(732589662.7986346), sfix(1721976083.938176), sfix(1598067955.8098073), sfix(732141783.5569079), sfix(165685090.72116414), sfix(14829152.83994152), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-313466.96895954217), sfix(-45274738.05515694), sfix(-107386891.70197046), sfix(-91196820.25826864), sfix(-33157069.45672721), sfix(-4389169.295869607), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-142685611.00367427), sfix(-396788718.10251427), sfix(-451208440.692198), sfix(-257339437.66616878), sfix(-72689089.05516647), sfix(-8076588.975313046), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-17758299.205809444), sfix(-90531832.81995456), sfix(-196524918.13835797), sfix(-195407505.50263762), sfix(-90074464.69094664), sfix(-15773947.60443618), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-6408086.74839271), sfix(-13692470.989020241), sfix(6691100.962261253), sfix(65032067.294357665), sfix(69001085.16094385), sfix(19813824.070041373), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-6510411.226366391), sfix(-15210047.417660588), sfix(-3104436.8779816367), sfix(27334958.459180072), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-6771265.24840001), sfix(-11634289.270197606), sfix(-23232815.145198397), sfix(84846053.17774954), sfix(-75432705.59514487), sfix(21738386.528186128), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-59513241.90882605), sfix(146865610.80320287), sfix(-172530699.35734805), sfix(99264100.30707274), sfix(-27513809.04620051), sfix(2919332.939260855), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-703819792.6109754), sfix(1336697797.3004153), sfix(-1018516955.8436779), sfix(384286646.773327), sfix(-71756034.38000427), sfix(5301540.672679554), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-591273510.240295), sfix(755207166.2104633), sfix(-388089120.035583), sfix(99248680.3444002), sfix(-12683259.552996447), sfix(648009.7029494287), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    scaler = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    # pre_muls[j] 对应 x^(j+1)
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    col_c0 = [coeffA[i][0] for i in range(m)]
    col_s0 = [scaler[i][0] for i in range(m)]

    # 使用 dot_product 选出当前区间对应的 c 和 s
    # 此时 selected_c0 和 selected_s0 变成了 sfix (Secret)
    selected_c0 = sfix.dot_product(cipher_index, col_c0)
    selected_s0 = sfix.dot_product(cipher_index, col_s0)

    # 计算常数项结果
    final_res = selected_c0 * selected_s0

    # 4. 处理高阶项 (x^1 到 x^degree)
    for j in range(degree):
        # 提取第 j+1 列 (对应 x^(j+1))
        col_c = [coeffA[i][j+1] for i in range(m)]
        col_s = [scaler[i][j+1] for i in range(m)]

        # 选出当前区间的 c 和 s
        selected_c = sfix.dot_product(cipher_index, col_c)
        selected_s = sfix.dot_product(cipher_index, col_s)


        term = selected_c * pre_muls[j] * selected_s
        final_res += term

    return final_res


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
    
    breaks = [
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-3.674999713897705),
        sfix(-3.1499998569488525),
        sfix(-2.625),
        sfix(-2.0999999046325684),
        sfix(-1.5749999284744263),
        sfix(-1.0499999523162842),
        sfix(-0.26249998807907104),
        sfix(0.0),
        sfix(0.13124999403953552),
        sfix(0.26249998807907104),
        sfix(1.0499999523162842),
        sfix(1.5749999284744263),
        sfix(2.0999999046325684),
        sfix(2.625),
        sfix(3.1499998569488525)
    ]
    coeffA = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(992282676.2976699), sfix(1230449407.2851386), sfix(610903530.5800586), sfix(151688832.99396724), sfix(18831513.679192282), sfix(934995.3934081424), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-799309900.1236391), sfix(-1701013344.7743957), sfix(-1260323278.1111803), sfix(-434577621.6788053), sfix(-71709402.2118297), sfix(-4595330.060797974), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1598703720.182317), sfix(3908545000.5147624), sfix(3466318268.728909), sfix(1442778480.329573), sfix(287303491.5826767), sfix(22156038.417430293), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-2921331042.3734684), sfix(-7224968077.567493), sfix(-6957040271.274744), sfix(-3275673302.875675), sfix(-755754198.0722752), sfix(-68477661.44964364), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1624691095.4665434), sfix(4839671261.114002), sfix(5714956902.425318), sfix(3323377128.7036242), sfix(950836893.9379537), sfix(107079584.37503956), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-252575087.43759212), sfix(-1106291245.4581501), sfix(-1822900075.9735045), sfix(-1457660275.1084993), sfix(-566397595.4341769), sfix(-85644512.3574866), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(4441565.383212715), sfix(-17365008.95228551), sfix(-1553410.6194425167), sfix(35338108.13388152), sfix(26608528.245528556), sfix(3794372.142881914), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(4209457.475106673), sfix(-19485757.200551398), sfix(-9230238.352751493), sfix(17314839.948454853), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(4209457.475106673), sfix(-19374416.35281617), sfix(-7026769.067546377), sfix(37906090.22884787), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(4209302.850841724), sfix(-19379011.901971348), sfix(-6665457.723079145), sfix(32226576.82182519), sfix(32784734.55446008), sfix(-60439931.37637207), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(3805308.1825277363), sfix(-13024840.934075171), sfix(-45789461.763121404), sfix(150619815.44571683), sfix(-144614903.38492742), sfix(46057743.15343494), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-165780814.2285), sfix(640879965.8216997), sfix(-992782196.480687), sfix(756126216.9798087), sfix(-282777713.6230483), sfix(41383207.7286286), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(975622039.8374114), sfix(-2892807643.9348216), sfix(3380883394.6094995), sfix(-1948614273.898668), sfix(552791610.3973237), sfix(-61752453.88158009), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1838405982.2661264), sfix(4431851621.065304), sfix(-4190584835.8708925), sfix(1941770937.4691653), sfix(-441865429.6167428), sfix(39561166.89919389), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1203924130.7232976), sfix(-2655362689.784648), sfix(2204390049.472737), sfix(-878383892.2758933), sfix(169526721.18298912), sfix(-12770453.479447542), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1272153697.861192), sfix(-1618428135.0310955), sfix(820003674.3447512), sfix(-208249044.55063197), sfix(26437195.093914866), sfix(-1342022.6055400257), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    scaler = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    # pre_muls[j] 对应 x^(j+1)
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    col_c0 = [coeffA[i][0] for i in range(m)]
    col_s0 = [scaler[i][0] for i in range(m)]

    # 使用 dot_product 选出当前区间对应的 c 和 s
    # 此时 selected_c0 和 selected_s0 变成了 sfix (Secret)
    selected_c0 = sfix.dot_product(cipher_index, col_c0)
    selected_s0 = sfix.dot_product(cipher_index, col_s0)

    # 计算常数项结果
    final_res = selected_c0 * selected_s0

    # 4. 处理高阶项 (x^1 到 x^degree)
    for j in range(degree):
        # 提取第 j+1 列 (对应 x^(j+1))
        col_c = [coeffA[i][j+1] for i in range(m)]
        col_s = [scaler[i][j+1] for i in range(m)]

        # 选出当前区间的 c 和 s
        selected_c = sfix.dot_product(cipher_index, col_c)
        selected_s = sfix.dot_product(cipher_index, col_s)


        term = selected_c * pre_muls[j] * selected_s
        final_res += term

    return final_res


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
    
    breaks = [
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-3.937499761581421),
        sfix(-3.674999713897705),
        sfix(-3.4124999046325684),
        sfix(-3.1499998569488525),
        sfix(-2.625),
        sfix(-2.0999999046325684),
        sfix(-1.5749999284744263),
        sfix(-1.0499999523162842),
        sfix(-0.5249999761581421),
        sfix(-0.06562499701976776),
        sfix(0.0),
        sfix(0.06562499701976776),
        sfix(0.5249999761581421),
        sfix(1.0499999523162842),
        sfix(1.5749999284744263),
        sfix(2.0999999046325684),
        sfix(2.625),
        sfix(3.1499998569488525),
        sfix(3.4124999046325684),
        sfix(3.674999713897705)
    ]
    coeffA = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(227585496.1943855), sfix(276615589.0314401), sfix(134484225.30662), sfix(32690670.508924082), sfix(3973088.531330491), sfix(193139.95520110408), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(3911677936.455554), sfix(4996319745.000673), sfix(2553488522.1186137), sfix(652709394.7987496), sfix(83445782.80489823), sfix(4268487.643043905), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(6482914055.181864), sfix(8391269354.549377), sfix(4345005819.708306), sfix(1124977793.9719715), sfix(145634022.7049692), sfix(7540669.7040446), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-12382704841.5567), sfix(-19451686080.792423), sfix(-12095932098.035112), sfix(-3730292738.8041067), sfix(-571457195.2263424), sfix(-34833185.32007941), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(3432965680.9561667), sfix(7919297406.825629), sfix(6780947967.246407), sfix(2757672130.3553658), sfix(540235210.0277363), sfix(41161405.87618847), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-5602123209.013252), sfix(-13726728139.34735), sfix(-13125364088.80739), sfix(-6142084859.052309), sfix(-1409248300.4418068), sfix(-127057187.46276419), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(2905442355.346589), sfix(8847904817.367804), sfix(10590186505.390404), sfix(6213532573.254283), sfix(1788140782.373083), sfix(202126249.88564453), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-418941901.5228827), sfix(-2064562513.6464705), sfix(-3749305807.09641), sfix(-3216484906.6186075), sfix(-1315759395.314279), sfix(-206991398.47785223), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(9717755.180191742), sfix(121381662.7326817), sfix(727187512.8852022), sfix(1385486703.034048), sfix(1059004775.828714), sfix(285012468.7874504), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(727471.7099282013), sfix(69469.14791752923), sfix(132350002.51524486), sfix(-8306798.959324286), sfix(-538269353.4610907), sfix(-439861768.02168995), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(713513.4938890431), sfix(-318855.4956337714), sfix(131172040.13137512), sfix(47953645.96469735), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(713513.4938890431), sfix(-363414.5431972577), sfix(131144153.0592609), sfix(-63195056.44026212), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(735201.8187259538), sfix(-1023664.3524785823), sfix(135762112.7470975), sfix(-26999426.29032065), sfix(-484948531.07370085), sfix(425059098.0966266), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-2961679.390220846), sfix(-28755127.63908854), sfix(461972530.1328049), sfix(-1052583324.9874189), sfix(881310871.6756793), sfix(-253015841.06629047), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-111891134.62349586), sfix(835003844.3240525), sfix(-1858743906.996381), sfix(1827875383.1166744), sfix(-827032629.6667782), sfix(140771558.55299717), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1519609219.416125), sfix(-5025390120.448141), sfix(6464827107.6081085), sfix(-4031465843.043425), sfix(1221363120.9847994), sfix(-144159842.28433368), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-3524396543.1822057), sfix(9389700642.269754), sfix(-9554641829.335972), sfix(4691377555.677826), sfix(-1117873065.4321787), sfix(103865848.90993552), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(2055835211.7631142), sfix(-5712864560.646599), sfix(5388112610.825458), sfix(-2323434268.532015), sfix(473246285.180158), sfix(-37065540.43612102), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-12932957662.92019), sfix(20410582190.56535), sfix(-12739122684.992897), sfix(3940422715.0845084), sfix(-605142987.013631), sfix(36963165.639508374), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(7343282438.806025), sfix(-9518695915.56261), sfix(4936367780.774863), sfix(-1280192739.943206), sfix(166018717.00190887), sfix(-8612306.835701598), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1812846592.6682243), sfix(-2251896464.1032248), sfix(1118656219.8023841), sfix(-277803263.5042037), sfix(34487313.944537066), sfix(-1712184.8862103089), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    scaler = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    # pre_muls[j] 对应 x^(j+1)
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    col_c0 = [coeffA[i][0] for i in range(m)]
    col_s0 = [scaler[i][0] for i in range(m)]

    # 使用 dot_product 选出当前区间对应的 c 和 s
    # 此时 selected_c0 和 selected_s0 变成了 sfix (Secret)
    selected_c0 = sfix.dot_product(cipher_index, col_c0)
    selected_s0 = sfix.dot_product(cipher_index, col_s0)

    # 计算常数项结果
    final_res = selected_c0 * selected_s0

    # 4. 处理高阶项 (x^1 到 x^degree)
    for j in range(degree):
        # 提取第 j+1 列 (对应 x^(j+1))
        col_c = [coeffA[i][j+1] for i in range(m)]
        col_s = [scaler[i][j+1] for i in range(m)]

        # 选出当前区间的 c 和 s
        selected_c = sfix.dot_product(cipher_index, col_c)
        selected_s = sfix.dot_product(cipher_index, col_s)


        term = selected_c * pre_muls[j] * selected_s
        final_res += term

    return final_res


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
    
    breaks = [
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-3.937499761581421),
        sfix(-3.674999713897705),
        sfix(-3.4124999046325684),
        sfix(-2.8874998092651367),
        sfix(-2.4937500953674316),
        sfix(-2.0999999046325684),
        sfix(-1.5749999284744263),
        sfix(-0.9187499284744263),
        sfix(-0.7874999642372131),
        sfix(-0.26249998807907104),
        sfix(0.0),
        sfix(0.26249998807907104),
        sfix(0.9187499284744263),
        sfix(1.0499999523162842),
        sfix(1.5749999284744263),
        sfix(2.0999999046325684),
        sfix(2.625),
        sfix(2.8874998092651367),
        sfix(3.1499998569488525)
    ]
    coeffA = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(27615827.06100246), sfix(33545541.781326897), sfix(16305747.465747124), sfix(3963405.573892923), sfix(481695.77227582154), sfix(23416.6906163974), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(473972674.32157624), sfix(605363926.4604441), sfix(309375922.86189914), sfix(79079228.84378484), sfix(10109698.465544065), sfix(517129.70396143314), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(569199298.7072195), sfix(717566615.8938106), sfix(360955187.0560209), sfix(90522961.39735325), sfix(11312499.776028933), sfix(563221.309999999), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-3406838074.6718297), sfix(-5188790755.840319), sfix(-3149961742.727801), sfix(-953380024.3281288), sfix(-143938889.8024074), sfix(-8675959.883386103), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(4241525054.397314), sfix(8012568975.246359), sfix(5970913877.518385), sfix(2199683846.4650726), sfix(401451533.4149725), sfix(29085637.86140962), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1515947963.2313569), sfix(-3686009630.25723), sfix(-3544134211.6062593), sfix(-1672632693.0722096), sfix(-387058781.46736735), sfix(-35183831.356961735), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(323313691.0101761), sfix(959863804.5295986), sfix(1143476995.3824499), sfix(689436634.8351479), sfix(207457722.23290637), sfix(24618441.747339632), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-17072397.792392027), sfix(-84534601.3734167), sfix(-127675075.81458513), sfix(-76339580.76516479), sfix(-20330719.67760757), sfix(-2056865.9567180737), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(17398966.205107514), sfix(56222937.78779316), sfix(91672185.85768762), sfix(81894683.98268877), sfix(28729647.782660067), sfix(1829455.0303322761), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(7030816.8664225675), sfix(-7513893.908651471), sfix(-63186244.62873631), sfix(-103095317.40858841), sfix(-79162819.77566116), sfix(-22479710.69438771), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(7606479.159887518), sfix(67080.19401594707), sfix(-25456174.22640983), sfix(-18323301.04512774), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(7606479.159887518), sfix(284636.8020982767), sfix(-25541436.675561283), sfix(20008721.09118542), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(6852525.871885745), sfix(9811550.264240604), sfix(-71095877.90088761), sfix(118706770.50842908), sfix(-89401433.892158), sfix(25168380.750827383), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(28987328.939885426), sfix(-116941535.56955881), sfix(219723098.33546382), sfix(-215296610.33023733), sfix(102522421.23406604), sfix(-18953038.011966597), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-37440226.08957171), sfix(165159668.77060008), sfix(-258934004.53457007), sfix(190349139.807937), sfix(-69188833.80766647), sfix(10093208.263480784), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(297767807.247791), sfix(-883745278.1001465), sfix(1052097909.7963918), sfix(-627716176.0544556), sfix(185600760.53628412), sfix(-21587378.887791067), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-692309183.7803516), sfix(1768335482.0085285), sfix(-1754156371.2072918), sfix(842477109.72457), sfix(-196506996.27220201), sfix(17885166.46832612), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(2660156903.507386), sfix(-4984669567.750744), sfix(3684428498.829473), sfix(-1346552710.7523396), sfix(243848484.0350963), sfix(-17534022.227716286), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1341977241.4812865), sfix(1938244216.2663825), sfix(-1107512531.3665884), sfix(312536107.9293495), sfix(-43470046.14345307), sfix(2376538.5041252174), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(177305805.93066126), sfix(-218814753.80423966), sfix(107840789.3843876), sfix(-26545044.072831064), sfix(3262717.9966531317), sfix(-160196.24654127273), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    scaler = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    # pre_muls[j] 对应 x^(j+1)
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    col_c0 = [coeffA[i][0] for i in range(m)]
    col_s0 = [scaler[i][0] for i in range(m)]

    # 使用 dot_product 选出当前区间对应的 c 和 s
    # 此时 selected_c0 和 selected_s0 变成了 sfix (Secret)
    selected_c0 = sfix.dot_product(cipher_index, col_c0)
    selected_s0 = sfix.dot_product(cipher_index, col_s0)

    # 计算常数项结果
    final_res = selected_c0 * selected_s0

    # 4. 处理高阶项 (x^1 到 x^degree)
    for j in range(degree):
        # 提取第 j+1 列 (对应 x^(j+1))
        col_c = [coeffA[i][j+1] for i in range(m)]
        col_s = [scaler[i][j+1] for i in range(m)]

        # 选出当前区间的 c 和 s
        selected_c = sfix.dot_product(cipher_index, col_c)
        selected_s = sfix.dot_product(cipher_index, col_s)


        term = selected_c * pre_muls[j] * selected_s
        final_res += term

    return final_res


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
    
    breaks = [
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-3.674999713897705),
        sfix(-3.1499998569488525),
        sfix(-2.625),
        sfix(-2.0999999046325684),
        sfix(-1.5749999284744263),
        sfix(-1.3125),
        sfix(-1.0499999523162842),
        sfix(-0.5249999761581421),
        sfix(0.0),
        sfix(0.5249999761581421),
        sfix(1.181249976158142),
        sfix(1.3125),
        sfix(1.5749999284744263),
        sfix(1.8374998569488525),
        sfix(2.0999999046325684),
        sfix(2.625),
        sfix(2.8874998092651367),
        sfix(3.1499998569488525)
    ]
    coeffA = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(9589136.064289954), sfix(11596776.49044896), sfix(5709461.545201118), sfix(1414803.4216677572), sfix(175701.79450437732), sfix(8733.64034486429), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(314781277.81985986), sfix(440133582.52366567), sfix(246515835.1669935), sfix(69102240.29559967), sfix(9692566.640020568), sfix(544161.9619757078), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-615019306.7237543), sfix(-1131523393.3776236), sfix(-814199988.6134105), sfix(-288257032.9609285), sfix(-50417308.77761842), sfix(-3494819.8770080972), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(429224659.0365422), sfix(1043389690.6077615), sfix(987566887.2512835), sfix(454541988.4978954), sfix(102082830.42709944), sfix(8985795.62192988), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-108180531.62939309), sfix(-353022592.7360857), sfix(-454777248.5808316), sfix(-286543539.0838223), sfix(-87499440.86560632), sfix(-10345237.916601636), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-7215867.438127211), sfix(-22181130.627925243), sfix(-22193688.38224025), sfix(-4316352.163585359), sfix(4408536.658047309), sfix(1609812.996878676), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1118912.0880726834), sfix(-3423983.586396363), sfix(-312149.82337099954), sfix(7321967.517398292), sfix(6947796.708457093), sfix(1710933.5513566316), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1297217.9344636018), sfix(46107.93479940875), sfix(15359320.122721525), sfix(31797227.272525292), sfix(23651434.295900483), sfix(5962422.519621451), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1335026.184607257), sfix(-1558661.0685950436), sfix(5141402.082675109), sfix(7121925.634185878), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1335026.1846072567), sfix(-1685664.1946510614), sfix(6050407.377215428), sfix(-4543364.925124018), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-982518.9465912314), sfix(-5862303.367546206), sfix(23822028.822781544), sfix(-39008114.204148576), sfix(29723919.030754704), sfix(-8249427.167308206), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-46367871.09231282), sfix(199859907.4554944), sfix(-351092918.87091565), sfix(304288952.4073846), sfix(-128161557.80443645), sfix(20915145.966121916), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(11107629.758683529), sfix(-5735454.735202642), sfix(-57220664.69872372), sfix(94492507.45468926), sfix(-53362324.06137725), sfix(10261315.389942719), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(464252352.3973721), sfix(-1444384736.1031325), sfix(1772103491.3168144), sfix(-1070048753.6821818), sfix(317785140.40119463), sfix(-37114057.881817654), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-452734815.2341942), sfix(969456179.650865), sfix(-769137492.5385125), sfix(267402412.36951786), sfix(-34096859.602620706), sfix(-89969.0519251364), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-626875295.8502966), sfix(1755226568.4619517), sfix(-1855940482.554571), sfix(939407136.7576861), sfix(-229395227.41037348), sfix(21740301.17117388), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(3947865346.959453), sfix(-7606652821.165198), sfix(5793211833.103081), sfix(-2180232242.463966), sfix(405793030.5861153), sfix(-29919715.480599537), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-4296161454.298347), sfix(6679652615.718621), sfix(-4113452810.7163043), sfix(1255915563.9216692), sfix(-190353103.8925092), sfix(11466875.150799796), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1451842594.8039975), sfix(-1850262937.1744184), sfix(942416649.2381072), sfix(-240009821.71339923), sfix(30551371.57964045), sfix(-1554976.1137827623), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    scaler = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    # pre_muls[j] 对应 x^(j+1)
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    col_c0 = [coeffA[i][0] for i in range(m)]
    col_s0 = [scaler[i][0] for i in range(m)]

    # 使用 dot_product 选出当前区间对应的 c 和 s
    # 此时 selected_c0 和 selected_s0 变成了 sfix (Secret)
    selected_c0 = sfix.dot_product(cipher_index, col_c0)
    selected_s0 = sfix.dot_product(cipher_index, col_s0)

    # 计算常数项结果
    final_res = selected_c0 * selected_s0

    # 4. 处理高阶项 (x^1 到 x^degree)
    for j in range(degree):
        # 提取第 j+1 列 (对应 x^(j+1))
        col_c = [coeffA[i][j+1] for i in range(m)]
        col_s = [scaler[i][j+1] for i in range(m)]

        # 选出当前区间的 c 和 s
        selected_c = sfix.dot_product(cipher_index, col_c)
        selected_s = sfix.dot_product(cipher_index, col_s)


        term = selected_c * pre_muls[j] * selected_s
        final_res += term

    return final_res


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
    
    breaks = [
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-3.1499998569488525),
        sfix(-2.0999999046325684),
        sfix(-0.5249999761581421),
        sfix(0.0),
        sfix(0.5249999761581421),
        sfix(2.0999999046325684),
        sfix(3.1499998569488525),
        sfix(3.4124999046325684),
        sfix(3.674999713897705)
    ]
    coeffA = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-573963893.4895847), sfix(-736555428.5593098), sfix(-377937116.66807103), sfix(-96921183.15701672), sfix(-12421860.6370686), sfix(-636500.3327710418), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-322549371.1687946), sfix(-629998957.5753233), sfix(-503314834.5421464), sfix(-200588110.26728863), sfix(-39467495.57424636), sfix(-3057704.0554997474), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-12800267.1281917), sfix(1874346.5800617125), sfix(9757366.174470397), sfix(7104034.553223403), sfix(2599556.4582705246), sfix(373916.5612972518), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-13206073.547167128), sfix(-46934.56317004929), sfix(6135733.697206698), sfix(3110208.406679627), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-13206073.547167128), sfix(-141091.58777381788), sfix(6372669.705910435), sfix(-3037978.6157487947), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-13176519.389016991), sfix(-394152.30942883086), sfix(7539137.997299414), sfix(-5569560.115470584), sfix(2117158.5451943474), sfix(-318827.76650990685), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-326758465.4148294), sfix(638525241.2718774), sfix(-510032300.5955157), sfix(203186361.0061416), sfix(-39962602.07853797), sfix(3094997.4738750276), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(329103991.9938456), sfix(-615274956.2690774), sfix(431254166.40360814), sfix(-145188778.9085215), sfix(23786779.757530812), sfix(-1528924.2042205252), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-771148346.2076886), sfix(1012131676.1006796), sfix(-531807158.23795956), sfix(139830538.7876523), sfix(-18397973.09575699), sfix(969038.2372060305), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-154583951.04220787), sfix(192024522.85207933), sfix(-95388127.87006903), sfix(23688367.5279257), sfix(-2940747.393703214), sfix(145998.94494096693), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    scaler = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    # pre_muls[j] 对应 x^(j+1)
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    col_c0 = [coeffA[i][0] for i in range(m)]
    col_s0 = [scaler[i][0] for i in range(m)]

    # 使用 dot_product 选出当前区间对应的 c 和 s
    # 此时 selected_c0 和 selected_s0 变成了 sfix (Secret)
    selected_c0 = sfix.dot_product(cipher_index, col_c0)
    selected_s0 = sfix.dot_product(cipher_index, col_s0)

    # 计算常数项结果
    final_res = selected_c0 * selected_s0

    # 4. 处理高阶项 (x^1 到 x^degree)
    for j in range(degree):
        # 提取第 j+1 列 (对应 x^(j+1))
        col_c = [coeffA[i][j+1] for i in range(m)]
        col_s = [scaler[i][j+1] for i in range(m)]

        # 选出当前区间的 c 和 s
        selected_c = sfix.dot_product(cipher_index, col_c)
        selected_s = sfix.dot_product(cipher_index, col_s)


        term = selected_c * pre_muls[j] * selected_s
        final_res += term

    return final_res


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
    
    breaks = [
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-3.674999713897705),
        sfix(-3.1499998569488525),
        sfix(-2.625),
        sfix(-2.0999999046325684),
        sfix(-1.5749999284744263),
        sfix(-1.0499999523162842),
        sfix(-0.5249999761581421),
        sfix(-0.26249998807907104),
        sfix(0.0),
        sfix(0.26249998807907104),
        sfix(0.5249999761581421),
        sfix(0.65625),
        sfix(1.0499999523162842),
        sfix(1.5749999284744263),
        sfix(2.0999999046325684),
        sfix(2.625),
        sfix(3.1499998569488525)
    ]
    coeffA = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(2468138216.787015), sfix(3061200643.382098), sfix(1519958666.3065975), sfix(377415991.35249615), sfix(46854442.62258521), sfix(2326327.9980970086), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1117173052.5921245), sfix(-2997072406.490334), sfix(-2435884841.567584), sfix(-882993804.4404773), sfix(-150336404.06896785), sfix(-9842579.24300845), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-89156203.27747607), sfix(2697952299.252354), sfix(3800162932.5624533), sfix(1942637247.4085686), sfix(434909932.7878296), sfix(36167235.167320356), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1909937024.7119834), sfix(-6090356606.924085), sfix(-6970478364.832826), sfix(-3724254719.071394), sfix(-945195437.625669), sfix(-92159035.69392997), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1196791334.6008651), sfix(3909721630.265686), sfix(5013533808.56897), sfix(3148797330.907362), sfix(968676657.1746992), sfix(116599234.43592164), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-132965567.55600439), sfix(-607683652.4677737), sfix(-1088538136.334865), sfix(-952825029.3384349), sfix(-404511226.9166373), sfix(-66724840.51034581), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(9422752.662072131), sfix(2925651.4260354894), sfix(-49789432.668605626), sfix(-79309838.51163244), sfix(-43053069.18534881), sfix(-8257629.067545149), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(7808523.851425725), sfix(-3911459.0357979727), sfix(-48227489.919936284), sfix(-31211991.213588074), sfix(40273148.027277805), sfix(36273659.4999088), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(7960060.723904998), sfix(-1830560.6196756514), sfix(-39854923.325637706), sfix(-29209890.24181233), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(7960060.723904998), sfix(-1464953.2744240048), sfix(-39096766.82880126), sfix(34353717.656270444), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(7744131.943437989), sfix(1693342.4078886327), sfix(-55118871.24264117), sfix(63627536.47196756), sfix(-2300703.1250897804), sfix(-22207259.21062564), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5518601.045124801), sfix(24144742.9307327), sfix(-146446007.46444568), sfix(250781494.2420838), sfix(-195389690.88421348), sfix(57966384.16631232), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(21434533.856227964), sfix(-81839943.83841023), sfix(135624760.7620421), sfix(-124389736.26861699), sfix(54075826.959348), sfix(-8400157.084065251), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-135388166.4017749), sfix(568461835.5972418), sfix(-930473508.7418721), sfix(735693495.9939427), sfix(-285179384.96068853), sfix(43384773.92616856), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(912405476.0821447), sfix(-2791367462.72321), sfix(3374590409.214843), sfix(-2019904233.93109), sfix(595998468.1401532), sfix(-69243099.33006342), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1403201466.3645968), sfix(3934681438.499403), sfix(-4178535423.3358145), sfix(2121403416.5834956), sfix(-519699604.3886311), sfix(49405942.51199281), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(229043539.95764908), sfix(-1707802442.1355174), sfix(2062285663.2369146), sfix(-1001777407.4853927), sfix(218683694.88265434), sfix(-17918395.922685523), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(3564985555.6928935), sfix(-4548292395.730059), sfix(2313149025.845304), sfix(-589285058.9811809), sfix(75040342.49927387), sfix(-3820886.369562685), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    scaler = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    # pre_muls[j] 对应 x^(j+1)
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    col_c0 = [coeffA[i][0] for i in range(m)]
    col_s0 = [scaler[i][0] for i in range(m)]

    # 使用 dot_product 选出当前区间对应的 c 和 s
    # 此时 selected_c0 和 selected_s0 变成了 sfix (Secret)
    selected_c0 = sfix.dot_product(cipher_index, col_c0)
    selected_s0 = sfix.dot_product(cipher_index, col_s0)

    # 计算常数项结果
    final_res = selected_c0 * selected_s0

    # 4. 处理高阶项 (x^1 到 x^degree)
    for j in range(degree):
        # 提取第 j+1 列 (对应 x^(j+1))
        col_c = [coeffA[i][j+1] for i in range(m)]
        col_s = [scaler[i][j+1] for i in range(m)]

        # 选出当前区间的 c 和 s
        selected_c = sfix.dot_product(cipher_index, col_c)
        selected_s = sfix.dot_product(cipher_index, col_s)


        term = selected_c * pre_muls[j] * selected_s
        final_res += term

    return final_res


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
    
    breaks = [
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-2.0999999046325684),
        sfix(-1.0499999523162842),
        sfix(-0.26249998807907104),
        sfix(-0.13124999403953552),
        sfix(0.0),
        sfix(0.5249999761581421),
        sfix(1.0499999523162842),
        sfix(1.5749999284744263),
        sfix(2.0999999046325684),
        sfix(2.625)
    ]
    coeffA = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-7320910.804578875), sfix(-6344961.558236066), sfix(-3251163.9757827534), sfix(-985155.1998264602), sfix(-153635.22561887492), sfix(-9460.96748384326), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(158014148.34617907), sfix(585680066.98892), sfix(773621813.8716178), sfix(483489936.1332916), sfix(145989439.44249177), sfix(17217675.21612601), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(4486070.022338452), sfix(8265624.34562653), sfix(-43082737.81805081), sfix(-26537123.26852552), sfix(33287019.18951959), sfix(21738540.214208078), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5098062.469104756), sfix(14612948.73442349), sfix(-19639295.999612022), sfix(8204768.363321503), sfix(44198836.86673324), sfix(9400303.119124949), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5096646.713805641), sfix(14553224.622597799), sfix(-20910704.128678255), sfix(-4280502.307127657), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5096646.713805642), sfix(14602780.550428959), sfix(-21375791.02477172), sfix(13861204.955819467), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(6574545.574542729), sfix(5618896.977934047), sfix(-3945338.1432126043), sfix(6071114.474346002), sfix(-7198015.963660132), sfix(2719123.054305423), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-47467255.37229461), sfix(227932622.89794293), sfix(-363021598.1696432), sfix(288220557.38574237), sfix(-113415895.17101496), sfix(17589832.7431715), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(420118937.1915359), sfix(-1242186387.8959436), sfix(1487175633.6855965), sfix(-876885157.8086377), sfix(253688713.80225667), sfix(-28709564.356059853), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1173433700.7218416), sfix(2755905368.544725), sfix(-2518537549.497471), sfix(1127020691.9765332), sfix(-246976009.27306864), sfix(21278440.671420496), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-361963461.8832332), sfix(462445802.4363061), sfix(-229414532.0893149), sfix(57855523.40761845), sfix(-7283225.114532346), sfix(365938.78409589495), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    scaler = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    # pre_muls[j] 对应 x^(j+1)
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    col_c0 = [coeffA[i][0] for i in range(m)]
    col_s0 = [scaler[i][0] for i in range(m)]

    # 使用 dot_product 选出当前区间对应的 c 和 s
    # 此时 selected_c0 和 selected_s0 变成了 sfix (Secret)
    selected_c0 = sfix.dot_product(cipher_index, col_c0)
    selected_s0 = sfix.dot_product(cipher_index, col_s0)

    # 计算常数项结果
    final_res = selected_c0 * selected_s0

    # 4. 处理高阶项 (x^1 到 x^degree)
    for j in range(degree):
        # 提取第 j+1 列 (对应 x^(j+1))
        col_c = [coeffA[i][j+1] for i in range(m)]
        col_s = [scaler[i][j+1] for i in range(m)]

        # 选出当前区间的 c 和 s
        selected_c = sfix.dot_product(cipher_index, col_c)
        selected_s = sfix.dot_product(cipher_index, col_s)


        term = selected_c * pre_muls[j] * selected_s
        final_res += term

    return final_res


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
    
    breaks = [
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-3.1499998569488525),
        sfix(-2.8874998092651367),
        sfix(-2.625),
        sfix(-2.0999999046325684),
        sfix(-1.5749999284744263),
        sfix(-1.0499999523162842),
        sfix(-0.5249999761581421),
        sfix(-0.26249998807907104),
        sfix(0.0),
        sfix(0.26249998807907104),
        sfix(0.5249999761581421),
        sfix(1.0499999523162842),
        sfix(1.5749999284744263),
        sfix(2.0999999046325684),
        sfix(2.625),
        sfix(3.1499998569488525)
    ]
    coeffA = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(121182499.41411783), sfix(154768680.31863403), sfix(78958971.80524099), sfix(20126938.250358876), sfix(2563921.3374914015), sfix(130587.27941515855), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-312424000.4668817), sfix(-486619978.89352924), sfix(-299831843.6776935), sfix(-91493545.42172913), sfix(-13843521.733605526), sfix(-831568.4156617655), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(353052831.94490385), sfix(665630955.4157635), sfix(498504530.97679746), sfix(185174869.11094064), sfix(34115242.69797631), sfix(2495033.9099588995), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-147524736.4542366), sfix(-345015523.9692003), sfix(-317099603.4464297), sfix(-143709147.4119158), sfix(-32153297.521429192), sfix(-2842970.8417193363), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(100789205.57635385), sfix(283414376.5763035), sfix(316807224.33100015), sfix(175047656.8063266), sfix(47785968.25200257), sfix(5158798.267484555), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-20591689.44392134), sfix(-78587484.00995545), sfix(-113151080.56804264), sfix(-78889639.93193348), sfix(-26686269.848347347), sfix(-3501048.175773445), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1783882.7117872324), sfix(5878763.9705022285), sfix(6573528.987658328), sfix(-3722583.51198859), sfix(-9476243.425387198), sfix(-3825408.5753080645), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(829632.7565937137), sfix(-82914.69395538249), sfix(-6173472.143023419), sfix(-12049541.7598864), sfix(-4503794.342448735), sfix(2315649.394412409), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(870958.9656080279), sfix(531870.9413069759), sfix(-2851184.8751045307), sfix(-4688715.156361278), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(870958.9656080279), sfix(575600.5844500345), sfix(-2872241.5460546864), sfix(3346810.915993927), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(829187.7525727844), sfix(1197401.3410608596), sfix(-6232203.857293085), sfix(10831438.255992472), sfix(-4971279.430980877), sfix(-1368948.0114585548), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(2124341.2681835475), sfix(-7412828.449203742), sfix(14742499.512289453), sfix(-10296327.385494972), sfix(55172.94876990906), sfix(1626327.1685537915), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-31930807.981535386), sfix(126894918.05417985), sfix(-189714756.1240615), sfix(136498797.9217756), sfix(-47201013.76314965), sfix(6290363.146337445), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(151334519.3234314), sfix(-419329912.4012904), sfix(459175386.27353656), sfix(-247201570.05678505), sfix(65604527.74066797), sfix(-6880814.134784606), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-204685871.64139816), sfix(453018869.46155095), sfix(-395416825.6414301), sfix(171238719.48389342), sfix(-36807702.47262729), sfix(3143114.670425081), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(71560933.92286551), sfix(-146902582.45592338), sfix(118564504.23911612), sfix(-46558670.24693849), sfix(8936709.595647411), sfix(-672670.5164636999), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(98290491.93941748), sfix(-125259470.08721842), sfix(64177816.78320344), sfix(-16372870.04234471), sfix(2087370.0039004802), sfix(-106398.52504905027), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    scaler = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    # pre_muls[j] 对应 x^(j+1)
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    col_c0 = [coeffA[i][0] for i in range(m)]
    col_s0 = [scaler[i][0] for i in range(m)]

    # 使用 dot_product 选出当前区间对应的 c 和 s
    # 此时 selected_c0 和 selected_s0 变成了 sfix (Secret)
    selected_c0 = sfix.dot_product(cipher_index, col_c0)
    selected_s0 = sfix.dot_product(cipher_index, col_s0)

    # 计算常数项结果
    final_res = selected_c0 * selected_s0

    # 4. 处理高阶项 (x^1 到 x^degree)
    for j in range(degree):
        # 提取第 j+1 列 (对应 x^(j+1))
        col_c = [coeffA[i][j+1] for i in range(m)]
        col_s = [scaler[i][j+1] for i in range(m)]

        # 选出当前区间的 c 和 s
        selected_c = sfix.dot_product(cipher_index, col_c)
        selected_s = sfix.dot_product(cipher_index, col_s)


        term = selected_c * pre_muls[j] * selected_s
        final_res += term

    return final_res


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
    
    breaks = [
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-3.1499998569488525),
        sfix(-3.018749713897705),
        sfix(-2.8874998092651367),
        sfix(-2.2312498092651367),
        sfix(-2.0999999046325684),
        sfix(-1.5749999284744263),
        sfix(-1.0499999523162842),
        sfix(-0.5249999761581421),
        sfix(-0.26249998807907104),
        sfix(0.0),
        sfix(0.26249998807907104),
        sfix(0.5249999761581421),
        sfix(0.7874999642372131),
        sfix(1.0499999523162842),
        sfix(2.0999999046325684)
    ]
    coeffA = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1137411655.1800995), sfix(-1454494488.1438754), sfix(-742466699.8062814), sfix(-189317108.9426391), sfix(-24122068.448120542), sfix(-1228841.24566673), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(4133923051.977247), sfix(6522111182.345403), sfix(4087015655.734229), sfix(1273160176.0381973), sfix(197388579.49059185), sfix(12196257.458849533), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(2375709248.467303), sfix(3594119226.540768), sfix(2136452375.996313), sfix(623401826.2660527), sfix(89159235.4290643), sfix(4984698.287409605), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-2580255262.404959), sfix(-5072618927.07673), sfix(-3925614633.312003), sfix(-1496545049.3313231), sfix(-281487357.6178075), sfix(-20933655.952113673), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(930988910.8880091), sfix(2407590275.913301), sfix(2452672675.5919523), sfix(1224704378.0578978), sfix(299454428.1175962), sfix(28715563.43891483), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(445008298.8046699), sfix(1124728339.5658944), sfix(1102317541.254974), sfix(516001980.51232064), sfix(113957543.39309451), sfix(9340289.704900637), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-111491177.56875867), sfix(-439552594.4391999), sfix(-631115169.3060774), sfix(-425549803.590112), sfix(-134637776.20958525), sfix(-15820953.67209287), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(11030985.234006627), sfix(40287948.09964287), sfix(92284162.89371662), sfix(85976669.94502376), sfix(25282050.616033632), sfix(-1353086.6223925343), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(4959889.507756999), sfix(-2922082.6251752363), sfix(-26196699.674451035), sfix(-66923121.301875606), sfix(-62738470.1313841), sfix(-16494148.231210444), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5100236.027761586), sfix(-671524.8597815109), sfix(-11604723.443953888), sfix(-20904355.273039754), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5100236.027761586), sfix(-595697.9378941177), sfix(-13872233.714561597), sfix(-7629022.307956251), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5145050.520515334), sfix(-1452172.7395774717), sfix(-6306410.63380503), sfix(-40885829.88420682), sfix(60837043.4350171), sfix(-22975122.671140175), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(4555351.689389538), sfix(3361197.8727278737), sfix(-21799288.609963354), sfix(-16453087.800350292), sfix(42145414.139805034), sfix(-17524372.22082543), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-4924291.617908761), sfix(62432795.56605956), sfix(-169790080.0636931), sfix(169909183.80574727), sfix(-75834505.73573731), sfix(12515839.241432676), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(56120855.924589284), sfix(-176797550.98042345), sfix(201999650.03539678), sfix(-115896495.64176203), sfix(32476460.835324176), sfix(-3584305.782353609), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-4071136.9592117644), sfix(3438772.30775755), sfix(-6436608.390005413), sfix(1875077.536554445), sfix(-266189.80748438725), sfix(15003.30419527711), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    scaler = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    # pre_muls[j] 对应 x^(j+1)
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    col_c0 = [coeffA[i][0] for i in range(m)]
    col_s0 = [scaler[i][0] for i in range(m)]

    # 使用 dot_product 选出当前区间对应的 c 和 s
    # 此时 selected_c0 和 selected_s0 变成了 sfix (Secret)
    selected_c0 = sfix.dot_product(cipher_index, col_c0)
    selected_s0 = sfix.dot_product(cipher_index, col_s0)

    # 计算常数项结果
    final_res = selected_c0 * selected_s0

    # 4. 处理高阶项 (x^1 到 x^degree)
    for j in range(degree):
        # 提取第 j+1 列 (对应 x^(j+1))
        col_c = [coeffA[i][j+1] for i in range(m)]
        col_s = [scaler[i][j+1] for i in range(m)]

        # 选出当前区间的 c 和 s
        selected_c = sfix.dot_product(cipher_index, col_c)
        selected_s = sfix.dot_product(cipher_index, col_s)


        term = selected_c * pre_muls[j] * selected_s
        final_res += term

    return final_res


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
    
    breaks = [
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-3.674999713897705),
        sfix(-3.1499998569488525),
        sfix(-2.625),
        sfix(-2.0999999046325684),
        sfix(-1.5749999284744263),
        sfix(-1.0499999523162842),
        sfix(-0.7874999642372131),
        sfix(-0.5249999761581421),
        sfix(-0.26249998807907104),
        sfix(-0.13124999403953552),
        sfix(0.0),
        sfix(0.13124999403953552),
        sfix(0.26249998807907104),
        sfix(0.39374998211860657),
        sfix(0.5249999761581421),
        sfix(0.7874999642372131),
        sfix(1.0499999523162842),
        sfix(1.3125),
        sfix(2.0999999046325684),
        sfix(3.1499998569488525)
    ]
    coeffA = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(19202270.066372883), sfix(23705853.92092801), sfix(11752400.586454585), sfix(2917120.377156325), sfix(362169.29301925155), sfix(17985.46951566772), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(83225539.61398739), sfix(106791019.29162036), sfix(54770272.14378503), sfix(14020921.776460875), sfix(1790441.1686225196), sfix(91190.27530453105), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-165043545.43032655), sfix(-287245208.3676598), sfix(-195681001.6676656), sfix(-65667353.5305914), sfix(-10902103.033520471), sfix(-718415.2908412615), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(76698686.25948073), sfix(189985161.84112722), sfix(181386133.12392652), sfix(83379935.49270794), sfix(18571499.30336791), sfix(1614099.3258082932), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(12564193.888162421), sfix(13522382.901268367), sfix(-9894118.03429689), sfix(-19086650.92578176), sfix(-8622216.559983812), sfix(-1251442.267459154), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-10892786.984404074), sfix(-33235885.046735417), sfix(-33542253.260837637), sfix(-10922163.897744754), sfix(1533970.1318740437), sfix(1031187.9374994229), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5914808.144623984), sfix(32616436.20147133), sfix(67115503.54494911), sfix(63256826.35670534), sfix(27338269.772861443), sfix(4268458.391982115), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-394891.39309057273), sfix(-5972566.120826471), sfix(-27632995.35754874), sfix(-53521853.12298359), sfix(-44929426.5016852), sfix(-13699394.887558527), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(118958.20895759518), sfix(-803260.304892465), sfix(-6679124.545494209), sfix(-10753797.307287076), sfix(-995311.5028666796), sfix(4461872.254073808), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(163770.95961704952), sfix(-111634.96817066323), sfix(-2417237.5688068788), sfix(2374003.238769155), sfix(19255516.822668087), sfix(17002226.663667504), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(163384.5824502939), sfix(-130041.20866274968), sfix(-2851417.587667436), sfix(-2270840.2449017786), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(163384.5824502939), sfix(-120798.3220209986), sfix(-2834422.5852119164), sfix(3664051.5632533915), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(163628.45751829338), sfix(-134289.21640028417), sfix(-2475739.1977216187), sfix(-426155.6101556251), sfix(17904552.29324715), sfix(-18419720.889848616), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(147191.1355658867), sfix(152221.03348716017), sfix(-4481864.959766745), sfix(6633561.573604803), sfix(5406782.682038072), sfix(-9507515.910998221), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-24328.49718902718), sfix(2279994.6899933396), sfix(-15095533.986790331), sfix(33250410.249841742), sfix(-28157805.51153686), sfix(7521057.1577904355), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-229199.49972543385), sfix(4516308.831952843), sfix(-24638796.350689046), sfix(53281357.68977382), sfix(-48927228.00285967), sfix(16057411.861620856), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(8912427.005488275), sfix(-51991949.792071745), sfix(115688793.56338133), sfix(-121755310.2489277), sfix(60759165.414262004), sfix(-11571552.262445895), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-7325664.730582664), sfix(18103319.66208334), sfix(-4382484.570403776), sfix(-19938528.25979233), sfix(18138764.343409985), sfix(-4554014.092330497), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(90346648.00813289), sfix(-261969458.66129008), sfix(298001695.5130786), sfix(-166300975.63007998), sfix(45516529.99281877), sfix(-4888306.4002197385), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(477882626.6862468), sfix(-909037398.1128521), sfix(682473693.1012367), sfix(-252809588.82028678), sfix(46224310.80719467), sfix(-3341418.615004861), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(242406040.98262593), sfix(-308760214.47198904), sfix(157033258.65672487), sfix(-39959679.59813577), sfix(5082552.111585148), sfix(-258487.35580635097), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    scaler = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    # pre_muls[j] 对应 x^(j+1)
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    col_c0 = [coeffA[i][0] for i in range(m)]
    col_s0 = [scaler[i][0] for i in range(m)]

    # 使用 dot_product 选出当前区间对应的 c 和 s
    # 此时 selected_c0 和 selected_s0 变成了 sfix (Secret)
    selected_c0 = sfix.dot_product(cipher_index, col_c0)
    selected_s0 = sfix.dot_product(cipher_index, col_s0)

    # 计算常数项结果
    final_res = selected_c0 * selected_s0

    # 4. 处理高阶项 (x^1 到 x^degree)
    for j in range(degree):
        # 提取第 j+1 列 (对应 x^(j+1))
        col_c = [coeffA[i][j+1] for i in range(m)]
        col_s = [scaler[i][j+1] for i in range(m)]

        # 选出当前区间的 c 和 s
        selected_c = sfix.dot_product(cipher_index, col_c)
        selected_s = sfix.dot_product(cipher_index, col_s)


        term = selected_c * pre_muls[j] * selected_s
        final_res += term

    return final_res


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
    
    breaks = [
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-3.1499998569488525),
        sfix(-2.0999999046325684),
        sfix(-1.5749999284744263),
        sfix(-1.0499999523162842),
        sfix(-0.5249999761581421),
        sfix(-0.26249998807907104),
        sfix(-0.13124999403953552),
        sfix(0.0),
        sfix(0.26249998807907104),
        sfix(1.0499999523162842),
        sfix(2.0999999046325684),
        sfix(3.1499998569488525)
    ]
    coeffA = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-3390950.2020672415), sfix(1081910.8695225196), sfix(1379505.3590098186), sfix(385514.97743756586), sfix(45562.23674613402), sfix(2018.89849568764), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-478188947.50807923), sfix(-836389098.5235661), sfix(-589862279.229774), sfix(-208371318.11012283), sfix(-36805697.50635331), sfix(-2599130.961040627), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-404706207.61822915), sfix(-145676041.43723252), sfix(564105991.8847361), sfix(581118985.5353272), sfix(209514454.53861725), sfix(26562112.665357098), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(668922511.4760698), sfix(2277453071.097144), sfix(2363061350.4851317), sfix(889297685.6146184), sfix(33656720.77235834), sfix(-31885043.885998797), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-36412184.43271944), sfix(-331884142.1024265), sfix(-1210813819.3331773), sfix(-1196384028.0466084), sfix(-328931679.0187262), sfix(21379715.941590928), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(19896794.22716361), sfix(79651812.48926297), sfix(-35246383.23478378), sfix(427964024.3893341), sfix(735993026.3346868), sfix(275155755.3345289), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(18930394.045202963), sfix(64187952.74674993), sfix(-135015134.18754718), sfix(102294551.81139378), sfix(195893584.86844125), sfix(-90373595.22464354), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(18921847.631925132), sfix(63845763.03423801), sfix(-141886644.54498747), sfix(38756452.89929668), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(18921847.631925136), sfix(64030135.66049439), sfix(-141649756.06326237), sfix(110775446.02683145), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(18155760.35017251), sfix(74393452.84624882), sfix(-196870795.5213259), sfix(251638965.47583583), sfix(-156879685.94821134), sfix(38305895.14785075), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(24368860.456700366), sfix(17995641.791993115), sfix(-27386953.79612967), sfix(19737736.91358806), sfix(-6915166.260896832), sfix(947770.8515198068), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(873952765.635516), sfix(-1704649899.614622), sfix(1361745176.468698), sfix(-538045686.0998933), sfix(104961728.11445248), sfix(-8069188.123627657), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1380037136.8867052), sfix(-1765718498.6877878), sfix(911669299.2655153), sfix(-233744995.8399984), sfix(29943610.919257645), sfix(-1533485.2620441548), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    scaler = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    # pre_muls[j] 对应 x^(j+1)
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    col_c0 = [coeffA[i][0] for i in range(m)]
    col_s0 = [scaler[i][0] for i in range(m)]

    # 使用 dot_product 选出当前区间对应的 c 和 s
    # 此时 selected_c0 和 selected_s0 变成了 sfix (Secret)
    selected_c0 = sfix.dot_product(cipher_index, col_c0)
    selected_s0 = sfix.dot_product(cipher_index, col_s0)

    # 计算常数项结果
    final_res = selected_c0 * selected_s0

    # 4. 处理高阶项 (x^1 到 x^degree)
    for j in range(degree):
        # 提取第 j+1 列 (对应 x^(j+1))
        col_c = [coeffA[i][j+1] for i in range(m)]
        col_s = [scaler[i][j+1] for i in range(m)]

        # 选出当前区间的 c 和 s
        selected_c = sfix.dot_product(cipher_index, col_c)
        selected_s = sfix.dot_product(cipher_index, col_s)


        term = selected_c * pre_muls[j] * selected_s
        final_res += term

    return final_res


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
    
    breaks = [
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-3.1499998569488525),
        sfix(-2.625),
        sfix(-2.0999999046325684),
        sfix(-1.8374998569488525),
        sfix(-1.5749999284744263),
        sfix(-0.5249999761581421),
        sfix(0.26249998807907104),
        sfix(1.0499999523162842),
        sfix(1.181249976158142),
        sfix(1.5749999284744263),
        sfix(2.0999999046325684),
        sfix(2.362499952316284),
        sfix(3.1499998569488525)
    ]
    coeffA = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(16122689.536901832), sfix(20927389.956982046), sfix(10974013.414417543), sfix(2884271.1606330667), sfix(378926.1662466784), sfix(19888.05962644193), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-38587774.812831715), sfix(-87465896.91576527), sfix(-71520091.34059295), sfix(-27652848.499849305), sfix(-5161482.200073711), sfix(-376200.3811625623), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-186219727.0544752), sfix(-347428632.32278526), sfix(-253517024.87782723), sfix(-90891941.62909174), sfix(-16049154.178560255), sfix(-1117514.0748824622), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(115385583.76064609), sfix(354997459.5609789), sfix(401707348.5629425), sfix(215114515.36389977), sfix(55504803.9860144), sfix(5584395.1164305825), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(70055072.78185408), sfix(222655879.23862037), sfix(247693412.57533124), sfix(125767633.040895), sfix(29657733.321556915), sfix(2600537.395111722), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-14850229.691078499), sfix(-20305194.567833662), sfix(-18996746.168470677), sfix(-10738270.98610864), sfix(-876931.6146135246), sfix(705265.6558849295), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-12645902.629605997), sfix(-8829155.73928098), sfix(1026772.4314328528), sfix(1653565.0811411808), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-13178482.387239937), sfix(-4548831.315044666), sfix(-5303468.96082314), sfix(-29084461.367555726), sfix(97335079.63431583), sfix(-48926167.29980229), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-55917154.75339406), sfix(287790457.0074956), sfix(-772460603.4174762), sfix(949350115.2138631), sfix(-513595098.49363357), sfix(101120882.75126185), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(364039956.0210204), sfix(-1398156075.8023474), sfix(1938825834.1269174), sfix(-1234208091.2903697), sfix(367180254.51596445), sfix(-41248682.491963975), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-254927137.3959947), sfix(329584925.45908886), sfix(36028796.6022481), sfix(-205412015.02740905), sfix(96023363.67907377), sfix(-13702120.206721308), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1182637384.4538305), sfix(2700316072.12593), sfix(-2387257495.856315), sfix(1033002773.6889421), sfix(-220381769.4937122), sfix(18627802.607595652), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(657855835.3690015), sfix(-1042026069.8565358), sfix(660362470.7771538), sfix(-209574601.56550968), sfix(33280979.839946803), sfix(-2115296.008609414), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(14135840.32004519), sfix(-18993627.67696847), sfix(9673931.606931012), sfix(-2551898.3236461845), sfix(336457.6307781391), sfix(-17718.48903027782), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    scaler = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    # pre_muls[j] 对应 x^(j+1)
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    col_c0 = [coeffA[i][0] for i in range(m)]
    col_s0 = [scaler[i][0] for i in range(m)]

    # 使用 dot_product 选出当前区间对应的 c 和 s
    # 此时 selected_c0 和 selected_s0 变成了 sfix (Secret)
    selected_c0 = sfix.dot_product(cipher_index, col_c0)
    selected_s0 = sfix.dot_product(cipher_index, col_s0)

    # 计算常数项结果
    final_res = selected_c0 * selected_s0

    # 4. 处理高阶项 (x^1 到 x^degree)
    for j in range(degree):
        # 提取第 j+1 列 (对应 x^(j+1))
        col_c = [coeffA[i][j+1] for i in range(m)]
        col_s = [scaler[i][j+1] for i in range(m)]

        # 选出当前区间的 c 和 s
        selected_c = sfix.dot_product(cipher_index, col_c)
        selected_s = sfix.dot_product(cipher_index, col_s)


        term = selected_c * pre_muls[j] * selected_s
        final_res += term

    return final_res


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
    
    breaks = [
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-3.1499998569488525),
        sfix(-2.625),
        sfix(-2.0999999046325684),
        sfix(-1.5749999284744263),
        sfix(-1.0499999523162842),
        sfix(-0.7874999642372131),
        sfix(-0.26249998807907104),
        sfix(0.0),
        sfix(0.5249999761581421),
        sfix(1.0499999523162842),
        sfix(1.5749999284744263),
        sfix(2.0999999046325684)
    ]
    coeffA = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(15015181.667826448), sfix(17337173.62788389), sfix(5965944.040986921), sfix(613175.6962158197), sfix(-44520.17965903671), sfix(-8576.31994905975), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-2324561830.0124416), sfix(-3483806329.4193587), sfix(-2087149039.1039624), sfix(-624134573.4553343), sfix(-93120069.32360557), sfix(-5543939.413704571), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(4373887721.798773), sfix(9383308034.159002), sfix(7813599985.231926), sfix(3190349021.163388), sfix(642702407.6765509), sfix(51309516.03460741), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1594489212.05905), sfix(-5060174708.590208), sfix(-6190036339.698825), sfix(-3608951080.1669445), sfix(-1010516998.236297), sfix(-109723657.64910315), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(31414935.13989298), sfix(263516215.64658538), sfix(801080840.4128939), sfix(993557582.3379413), sfix(508400458.9072425), sfix(91288346.97053714), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(66623378.066494405), sfix(338656173.85055447), sfix(781512081.4913063), sfix(831283360.9538769), sfix(367394062.7608845), sfix(53048720.53585075), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(8840628.834667843), sfix(-13569640.18230924), sfix(-78271573.2089287), sfix(-218632223.26716176), sfix(-273501753.1523876), sfix(-103254549.35946812), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(9883672.836973866), sfix(717437.48714881), sfix(109105.74701445836), sfix(-5035323.841142184), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(9883672.836973866), sfix(833556.8422039237), sfix(-3284867.3577778814), sfix(3918663.5213366174), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(14136851.094983894), sfix(-27535577.515931368), sfix(66484858.054160506), sfix(-70771401.50235443), sfix(30755426.07818653), sfix(-2964631.4570352226), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-119984980.71149176), sfix(515796559.8963834), sfix(-794292432.7759976), sfix(588217149.9084016), sfix(-207901042.5538695), sfix(28264259.74628859), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(630990957.9518125), sfix(-1730092448.1497402), sfix(1885641978.3307488), sfix(-1005670590.7207468), sfix(264198319.93006614), sfix(-27389407.852393348), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(198383736.70110163), sfix(-305162138.58117884), sfix(194396680.0042191), sfix(-58874936.05876177), sfix(8801750.767058264), sfix(-520611.1292936096), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    scaler = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    # pre_muls[j] 对应 x^(j+1)
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    col_c0 = [coeffA[i][0] for i in range(m)]
    col_s0 = [scaler[i][0] for i in range(m)]

    # 使用 dot_product 选出当前区间对应的 c 和 s
    # 此时 selected_c0 和 selected_s0 变成了 sfix (Secret)
    selected_c0 = sfix.dot_product(cipher_index, col_c0)
    selected_s0 = sfix.dot_product(cipher_index, col_s0)

    # 计算常数项结果
    final_res = selected_c0 * selected_s0

    # 4. 处理高阶项 (x^1 到 x^degree)
    for j in range(degree):
        # 提取第 j+1 列 (对应 x^(j+1))
        col_c = [coeffA[i][j+1] for i in range(m)]
        col_s = [scaler[i][j+1] for i in range(m)]

        # 选出当前区间的 c 和 s
        selected_c = sfix.dot_product(cipher_index, col_c)
        selected_s = sfix.dot_product(cipher_index, col_s)


        term = selected_c * pre_muls[j] * selected_s
        final_res += term

    return final_res


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
    
    breaks = [
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-3.018749713897705),
        sfix(-2.8874998092651367),
        sfix(-2.625),
        sfix(-2.0999999046325684),
        sfix(-1.5749999284744263),
        sfix(-1.3125),
        sfix(-0.5249999761581421),
        sfix(0.0),
        sfix(0.26249998807907104),
        sfix(0.39374998211860657),
        sfix(1.0499999523162842),
        sfix(2.0999999046325684)
    ]
    coeffA = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(3426149678.050811), sfix(4437650843.870342), sfix(2294394958.1108932), sfix(592517239.8378797), sfix(76453334.9418311), sfix(3943533.548734633), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-6931577557.675069), sfix(-12101191365.013716), sfix(-8277757806.326438), sfix(-2789389945.3719106), sfix(-464937636.0981087), sfix(-30755020.243665576), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-8958950318.683134), sfix(-15582453009.130308), sfix(-10668664050.25528), sfix(-3610344383.536517), sfix(-605867780.9660412), sfix(-40431216.77817065), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5350947021.3145895), sfix(12561752404.125698), sfix(11489733550.068218), sfix(5118943226.933921), sfix(1114788381.1364355), sfix(95324343.33192535), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1533679320.9346473), sfix(-4597255704.44393), sfix(-5602432676.001335), sfix(-3388102318.6201262), sfix(-1001137332.9811357), sfix(-115105037.68925174), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(157235992.882146), sfix(745770535.1932365), sfix(1156609284.0202334), sfix(890904298.650888), sfix(354605229.3918347), sfix(56880990.198264815), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-28256008.846686263), sfix(-65043041.27026348), sfix(-245795350.3866216), sfix(-311383849.3142325), sfix(-157080077.67230743), sfix(-29707107.12242091), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-12622548.223563226), sfix(39340801.46163134), sfix(17884127.14162338), sfix(-5536927.023667797), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-12622548.223563226), sfix(39249596.55638448), sfix(19496561.50215132), sfix(-37727799.48134242), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-12607812.806408077), sfix(39147967.353385195), sfix(17708231.31297659), sfix(-18335717.53656251), sfix(-58988287.08959767), sfix(51740796.523873486), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-9889850.510784501), sfix(12545779.614764433), sfix(122242644.94352336), sfix(-225603055.8543631), sfix(149619957.2823559), sfix(-34013922.404646866), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-69536155.56423202), sfix(306692408.46281195), sfix(-446553957.11456376), sfix(315847590.4281385), sfix(-104870476.87083739), sfix(13333394.344619589), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-23608702.809633896), sfix(44609984.99428495), sfix(-14909581.764996072), sfix(4699845.577881447), sfix(-741850.2009504575), sfix(45996.74891452721), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    scaler = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    # pre_muls[j] 对应 x^(j+1)
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    col_c0 = [coeffA[i][0] for i in range(m)]
    col_s0 = [scaler[i][0] for i in range(m)]

    # 使用 dot_product 选出当前区间对应的 c 和 s
    # 此时 selected_c0 和 selected_s0 变成了 sfix (Secret)
    selected_c0 = sfix.dot_product(cipher_index, col_c0)
    selected_s0 = sfix.dot_product(cipher_index, col_s0)

    # 计算常数项结果
    final_res = selected_c0 * selected_s0

    # 4. 处理高阶项 (x^1 到 x^degree)
    for j in range(degree):
        # 提取第 j+1 列 (对应 x^(j+1))
        col_c = [coeffA[i][j+1] for i in range(m)]
        col_s = [scaler[i][j+1] for i in range(m)]

        # 选出当前区间的 c 和 s
        selected_c = sfix.dot_product(cipher_index, col_c)
        selected_s = sfix.dot_product(cipher_index, col_s)


        term = selected_c * pre_muls[j] * selected_s
        final_res += term

    return final_res


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
    
    breaks = [
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-3.674999713897705),
        sfix(-3.4124999046325684),
        sfix(-3.1499998569488525),
        sfix(-2.625),
        sfix(-2.0999999046325684),
        sfix(-1.9687498807907104),
        sfix(-1.8374998569488525),
        sfix(-1.0499999523162842),
        sfix(-0.5249999761581421),
        sfix(0.0),
        sfix(0.5249999761581421),
        sfix(1.0499999523162842),
        sfix(2.0999999046325684),
        sfix(3.1499998569488525)
    ]
    coeffA = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1235159001.674688), sfix(1533300041.984941), sfix(761541027.2276119), sfix(189109007.90636453), sfix(23476740.07079577), sfix(1165577.5307083118), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5094221507.10388), sfix(6610341882.089662), sfix(3432390720.60563), sfix(891368874.0270301), sfix(115764675.00421004), sfix(6014761.220746715), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-8353807952.162528), sfix(-13243280349.837585), sfix(-8294604374.423831), sfix(-2572872776.6517625), sfix(-396038004.38695943), sfix(-24237532.36445369), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-357086067.1678675), sfix(891715393.7763213), sfix(1632285500.2834578), sfix(893035105.582434), sfix(206045775.82182416), sfix(17421009.338123873), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-220512922.346426), sfix(-1497573015.7318609), sfix(-2215360249.443629), sfix(-1349975276.699011), sfix(-370505513.2499094), sfix(-38003749.46689449), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-2792941170.519828), sfix(-6825480930.174867), sfix(-6576450343.19705), sfix(-3107844295.3610535), sfix(-717812365.045939), sfix(-64718621.207026824), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-470649086.8649161), sfix(-932360277.8615118), sfix(-593228706.255457), sfix(-69784645.50119196), sfix(53675426.35806826), sfix(13664654.394582566), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(86480938.66314913), sfix(300155875.7711663), sfix(398467428.44783086), sfix(254540225.42423135), sfix(75789805.37941945), sfix(7969436.154738174), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-2458782.229274967), sfix(3286463.0050475816), sfix(42206809.4918154), sfix(88763852.8203803), sfix(69360566.98385799), sfix(19007693.23040032), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-2681522.3942078818), sfix(-2094407.2051133742), sfix(11173431.118245292), sfix(16460494.723421143), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-2681522.3942078818), sfix(-2322347.04324649), sfix(11684960.661857322), sfix(-10183000.952553578), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-4838760.87424319), sfix(10657791.121742748), sfix(-13662018.973230725), sfix(2382430.4506513104), sfix(9490182.650282478), sfix(-5272592.037543923), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(29601171.140317418), sfix(-135076816.7573053), sfix(216936110.86761415), sfix(-162097923.2534772), sfix(57083400.62114031), sfix(-7698636.900920209), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-100485227.09428447), sfix(159376648.9181539), sfix(-96177982.91200215), sfix(26332761.849906538), sfix(-3149912.526999557), sfix(110528.36226612797), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(44868768.023201294), sfix(-59600778.254376404), sfix(30075677.238412213), sfix(-7856121.97816484), sfix(1026306.5908427848), sfix(-53584.6389230163), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    scaler = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k - 1

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

    # pre_muls[j] 对应 x^(j+1)
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    col_c0 = [coeffA[i][0] for i in range(m)]
    col_s0 = [scaler[i][0] for i in range(m)]

    # 使用 dot_product 选出当前区间对应的 c 和 s
    # 此时 selected_c0 和 selected_s0 变成了 sfix (Secret)
    selected_c0 = sfix.dot_product(cipher_index, col_c0)
    selected_s0 = sfix.dot_product(cipher_index, col_s0)

    # 计算常数项结果
    final_res = selected_c0 * selected_s0

    # 4. 处理高阶项 (x^1 到 x^degree)
    for j in range(degree):
        # 提取第 j+1 列 (对应 x^(j+1))
        col_c = [coeffA[i][j+1] for i in range(m)]
        col_s = [scaler[i][j+1] for i in range(m)]

        # 选出当前区间的 c 和 s
        selected_c = sfix.dot_product(cipher_index, col_c)
        selected_s = sfix.dot_product(cipher_index, col_s)


        term = selected_c * pre_muls[j] * selected_s
        final_res += term

    return final_res


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


def func2_kan_model_evaluate(x):
    # dim_list required
    input_x = x
    dim_list = [(2, 9), (9, 1)]
    for l in range(len(dim_list)):
        in_dim, out_dim = dim_list[l]
        partial_result = [0]*out_dim
        for i in range(in_dim):
            for j in range(out_dim):
                partial_result[j] += neuron_func_dict[f"neuron{l}{i}{j}"](input_x[i])
        input_x = partial_result
    return input_x

def func2_kan_model_evaluate_vectorized(x):
    dim_list = [(2, 9), (9, 1)]
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