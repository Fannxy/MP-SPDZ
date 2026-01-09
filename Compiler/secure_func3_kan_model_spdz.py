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
        sfix(-0.06562499701976776),
        sfix(0.0),
        sfix(0.5249999761581421),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(47804469.74520896), sfix(57531938.104668), sfix(28277217.91597982), sfix(7004146.71324293), sfix(869877.505577216), sfix(43248.31190281254), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(37639227.62659407), sfix(24550292.60554006), sfix(-333098.5028463278), sfix(-3750632.0401779157), sfix(-1007252.2095786065), sfix(-81998.25497975554), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-113057261.05520345), sfix(-157788444.68516874), sfix(-79631812.41542302), sfix(-17210816.633148868), sfix(-1259940.4440420389), sfix(23310.94328472126), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(49688620.31954588), sfix(88679487.0096788), sfix(59924051.53778177), sfix(17605715.908477314), sfix(1874326.1343226065), sfix(-5137.58288660762), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-7528224.801703742), sfix(-20135150.713253334), sfix(-18166989.799633328), sfix(-7648048.2088554595), sfix(-1342735.9493570616), sfix(-48677.98064079318), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(686956.817002582), sfix(829588.9846410704), sfix(2209088.733907148), sfix(1458087.7773157915), sfix(367078.5984226009), sfix(21994.3905056412), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-27940.69415381726), sfix(-1450942.5025908807), sfix(41926.7646572725), sfix(1547731.3577542852), sfix(1496908.569057804), sfix(460695.5648923988), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-33954.61097926757), sfix(-1534905.603672904), sfix(-426664.68826893566), sfix(231057.413828073), sfix(-384878.59867979586), sfix(-647714.7403637881), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-33955.28290307685), sfix(-1534916.8958083251), sfix(-425469.95181500626), sfix(271975.6799368633), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-33955.28290307682), sfix(-1550895.4019922642), sfix(-235892.3772764426), sfix(-357784.60382485617), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(199954.72430763024), sfix(-3075489.922164587), sfix(3510525.400990232), sfix(-4498548.572365881), sfix(1892936.3463635424), sfix(-268970.00660457165), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(22110419.40749891), sfix(-37495314.99646912), sfix(21351013.328030806), sfix(-6612639.71754974), sfix(1005714.583793017), sfix(-60160.482349171), sfix(1.0), sfix(1.0), sfix(1.0)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1

    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res0 += pre_muls[j] * coeffA[i][j+1] * scaler[i][j+1]
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
        sfix(-4.199999809265137),
        sfix(-3.1499998569488525),
        sfix(-2.0999999046325684),
        sfix(-1.5749999284744263),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-309091924.113848), sfix(-389862852.2091762), sfix(-198626323.29828972), sfix(-50764419.044728614), sfix(-6492691.290263437), sfix(-332139.413785661), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-298210300.2254519), sfix(-611200498.3607342), sfix(-497174253.6974861), sfix(-198012684.7248041), sfix(-38599385.41485541), sfix(-2953470.124552911), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(43252093.64003185), sfix(124309185.73532623), sfix(134188188.5983675), sfix(71764346.80326325), sfix(18726928.664603557), sfix(1886841.798565035), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(660562.0556538395), sfix(3793815.094173837), sfix(852561.0855149839), sfix(536762.9314437538), sfix(761171.3485696118), sfix(256307.59752229316), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(800419.4980460069), sfix(4516965.286963573), sfix(2134609.65448467), sfix(1345194.1953273201), sfix(744280.213539631), sfix(138527.76882761598), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(801047.5608268151), sfix(4526106.179689485), sfix(2186611.783849945), sfix(1488565.3147668017), sfix(933068.8518794329), sfix(230756.45836928123), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(801004.3563866725), sfix(4524461.907605785), sfix(2156172.656108466), sfix(1214499.144186), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(801004.356386672), sfix(4523908.999760777), sfix(2182955.205444552), sfix(1339913.415655611), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(780135.4307743907), sfix(4797105.772574765), sfix(754614.0081410386), sfix(5026912.013022285), sfix(-4335749.390192434), sfix(1181695.3781973906), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-3907358.8775019064), sfix(20847330.72337181), sfix(-19378253.804049302), sfix(15379339.237394864), sfix(-5457242.649971482), sfix(719570.3715451435), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-98545464.024384), sfix(192140658.1049669), sfix(-134837341.27766553), sfix(49283191.41414354), sfix(-8859020.108906431), sfix(628270.6361567223), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(2878146.11805313), sfix(485623.76236052334), sfix(6344931.39043694), sfix(-1743525.3155527671), sfix(229867.27182309277), sfix(-11970.92499578759), sfix(1.0), sfix(1.0), sfix(1.0)]
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
    degree = k-1

    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res0 += pre_muls[j] * coeffA[i][j+1] * scaler[i][j+1]
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
        [sfix(26950853.91761191), sfix(32267907.437702738), sfix(15831574.152592251), sfix(3919705.211271207), sfix(486840.4971439828), sfix(24210.41048608884), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(13563893.425644912), sfix(2867424.7774598254), sfix(-6400697.635671133), sfix(-3867021.881460731), sfix(-814849.3284891563), sfix(-60153.86801737607), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-48486486.29632274), sfix(-61005208.00040312), sfix(-24714197.368831154), sfix(-2526642.381625428), sfix(550173.9820511614), sfix(100848.5772003523), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(13778617.087383699), sfix(16922689.00539771), sfix(3686400.0595111614), sfix(-3526127.4317293274), sfix(-1899957.3742823324), sfix(-259022.19239662515), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(2146632.3705204735), sfix(7319585.571643556), sfix(11487383.758073162), sfix(8150221.5733637335), sfix(2756309.884090957), sfix(361867.29432508105), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-431439.0808824483), sfix(-3094604.040686137), sfix(-4443797.526917632), sfix(-3614895.297433817), sfix(-1484040.836273157), sfix(-238836.76206640256), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(127251.70948008019), sfix(-709612.178407572), sfix(-444818.15853023145), sfix(-355272.67147714226), sfix(-214509.05293360315), sfix(-56253.80364885611), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(126753.85211048718), sfix(-712262.4468999804), sfix(-432855.8643405275), sfix(-246332.0393760574), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(126753.85211048716), sfix(-712610.3436213303), sfix(-438843.50279483135), sfix(-311423.69107341056), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(126751.0628766031), sfix(-712485.1053539709), sfix(-441612.8669474786), sfix(-283631.37556360953), sfix(-101997.88488368888), sfix(38219.62872232668), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(134234.1489419972), sfix(-790946.3030570212), sfix(-144259.81978413367), sfix(-759408.1066604097), sfix(140829.66749856077), sfix(99461.45798592892), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1205652.2607624214), sfix(5015047.455915356), sfix(-9682317.736193998), sfix(6470035.688022534), sfix(-2220509.498507443), sfix(303600.9401408372), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-37950062.90930013), sfix(77500156.86755528), sfix(-63947344.42992553), sfix(24961164.35469461), sfix(-4776134.142784707), sfix(359675.695999153), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-24209635.101272944), sfix(29875441.206154298), sfix(-16601053.2421033), sfix(4245139.766154786), sfix(-540782.4391573869), sfix(27517.07155743652), sfix(1.0), sfix(1.0), sfix(1.0)]
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
    degree = k-1

    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res0 += pre_muls[j] * coeffA[i][j+1] * scaler[i][j+1]
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
        sfix(-0.5249999761581421),
        sfix(-0.26249998807907104),
        sfix(-0.13124999403953552),
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
        [sfix(203776666.84850872), sfix(248742542.91370985), sfix(122850296.45201209), sfix(30465312.244895916), sfix(3782915.3684623186), sfix(187955.9891893503), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(523206194.54911447), sfix(621195668.7657758), sfix(291164796.90101665), sfix(66745190.7426498), sfix(7399674.004359347), sfix(311589.73873334564), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1020419389.1739601), sfix(-1702364510.540634), sfix(-1104316571.3790095), sfix(-351087782.2400659), sfix(-54945009.9206826), sfix(-3394999.486022442), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(517325048.0407157), sfix(1160222489.3982713), sfix(1029508661.8004663), sfix(445093800.1453153), sfix(93763225.09715648), sfix(7728279.495537514), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-97963712.91063178), sfix(-313638487.6471741), sfix(-385587767.574769), sfix(-235633627.15521008), sfix(-70299324.60323858), sfix(-8119617.784656424), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(521464.85745175387), sfix(6140738.004796537), sfix(30470613.759089716), sfix(35522544.9391823), sfix(18225458.08382653), sfix(3462596.464192143), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-421621.63370049745), sfix(-78990.51911814221), sfix(15408364.000080626), sfix(18136302.428912856), sfix(8482498.102912055), sfix(1320136.8807444642), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-844578.811305234), sfix(-3613219.703565433), sfix(3436568.2264544456), sfix(-2477659.92272514), sfix(-9609392.89252802), sfix(-5167051.245761497), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-848085.576660128), sfix(-3660022.2193817156), sfix(3207772.410788459), sfix(-2938778.4534925246), sfix(-9821505.937058855), sfix(-4888668.884087292), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-846981.0245710438), sfix(-3628456.314171746), sfix(3202272.538420727), sfix(-3119695.264468712), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-792843.4613822993), sfix(-4500722.796573667), sfix(8481945.039333422), sfix(-17292648.632753566), sfix(15660717.353352418), sfix(-5591778.12648755), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(13344163.793119682), sfix(-51253993.420032665), sfix(57490160.96200278), sfix(-24112057.474696472), sfix(-1336732.6426941617), sfix(1833851.1308147004), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(45180396.29002177), sfix(-188841315.18045127), sfix(279233143.3746366), sfix(-195379049.73380637), sfix(62970593.42158756), sfix(-7635538.362821148), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-410124590.79645157), sfix(957077513.2696326), sfix(-873166056.7246277), sfix(383577829.72930294), sfix(-82359750.55746216), sfix(6948707.271918205), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(599496072.2080367), sfix(-1015546968.6096416), sfix(670137398.3043424), sfix(-220749409.97535387), sfix(36077741.541647755), sfix(-2344676.778919972), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-236450174.80357394), sfix(300542137.1117133), sfix(-159542648.8091805), sfix(41052039.15614525), sfix(-5272299.654013613), sfix(270599.35606459295), sfix(1.0), sfix(1.0), sfix(1.0)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1

    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res0 += pre_muls[j] * coeffA[i][j+1] * scaler[i][j+1]
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
        sfix(-2.8874998092651367),
        sfix(-2.625),
        sfix(-2.0999999046325684),
        sfix(-1.5749999284744263),
        sfix(-1.0499999523162842),
        sfix(-0.5249999761581421),
        sfix(-0.26249998807907104),
        sfix(-0.13124999403953552),
        sfix(0.26249998807907104),
        sfix(1.0499999523162842),
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
        [sfix(120464895.22451515), sfix(147203644.3690328), sfix(72727804.2203663), sfix(18037127.99525177), sfix(2239658.9969437057), sfix(111273.09252626826), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(43170367.6304314), sfix(-9605963.933855202), sfix(-41391270.437360235), sfix(-21040454.740816195), sfix(-4196524.633156727), sfix(-301505.1890081268), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1017197161.2700768), sfix(-1613287830.2569375), sfix(-1010680690.8734461), sfix(-313684935.4573309), sfix(-48327447.11530267), sfix(-2960460.870820475), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(610093078.5670223), sfix(1209578045.0324547), sfix(948806535.4901912), sfix(366663123.9743246), sfix(69828548.47062005), sfix(5250717.492719582), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-5683257.374257776), sfix(-77236619.50818442), sfix(-122165528.85046549), sfix(-77321528.9396176), sfix(-21896669.3778213), sfix(-2307139.220657091), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(35713400.29982685), sfix(113328155.8574213), sfix(145882191.53685993), sfix(91169445.45644759), sfix(27891077.46501858), sfix(3353427.0044882884), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-7921480.974005786), sfix(-33686797.44781403), sfix(-51187682.47414082), sfix(-40337623.428545), sfix(-15830472.380194627), sfix(-2444000.7786596464), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-588172.9959771066), sfix(-1717865.4462299002), sfix(4439901.012523166), sfix(7912132.063882712), sfix(5004718.365723695), sfix(1133204.811546435), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-784805.0489182088), sfix(-3217550.100900795), sfix(-105841.321303371), sfix(1068118.3391041113), sfix(-110782.7648499544), sfix(-383398.24627350754), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-783989.4919753649), sfix(-3205112.519680203), sfix(-30813.32384705824), sfix(1290950.0749602187), sfix(212508.11244142696), sfix(-202840.20885415527), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-783935.5777669931), sfix(-3203511.9745877003), sfix(-39987.60818248526), sfix(1120598.806098906), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-822247.1785894177), sfix(-2743228.881378873), sfix(-2227784.814524667), sfix(6368682.221415293), sfix(-6062334.317565657), sfix(1683150.904675464), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(13775323.467895271), sfix(-61509894.217827514), sfix(92530344.330797), sfix(-70167707.46310502), sfix(24905832.318681505), sfix(-3335311.795108952), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-6126560.320542454), sfix(86307302.71513991), sfix(-145506970.45206076), sfix(90527493.67590207), sfix(-24937559.35257654), sfix(2550716.3965772297), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(64029286.85281149), sfix(-205316664.98652542), sfix(197813373.4005719), sfix(-86794480.53572352), sfix(17794806.904873602), sfix(-1396088.505482035), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(154204601.69211364), sfix(-197644957.6535884), sfix(97520996.28812136), sfix(-24697637.924225125), sfix(3129809.628507239), sfix(-158646.50404140563), sfix(1.0), sfix(1.0), sfix(1.0)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1

    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res0 += pre_muls[j] * coeffA[i][j+1] * scaler[i][j+1]
        poss_res[i] += poss_res0

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

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
        sfix(-3.674999713897705),
        sfix(-3.1499998569488525),
        sfix(-2.625),
        sfix(-2.362499952316284),
        sfix(-2.0999999046325684),
        sfix(-1.8374998569488525),
        sfix(-1.5749999284744263),
        sfix(-1.3125),
        sfix(-1.0499999523162842),
        sfix(-0.7874999642372131),
        sfix(-0.5249999761581421),
        sfix(-0.13124999403953552),
        sfix(0.0),
        sfix(0.13124999403953552),
        sfix(0.5249999761581421),
        sfix(0.65625),
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
        [sfix(6852867.155486805), sfix(5977514.049838478), sfix(2554017.102200307), sfix(609401.2850980858), sfix(76147.66448699596), sfix(3864.95490849801), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-122232949.80215345), sfix(-179013509.75404346), sfix(-103409285.30520698), sfix(-29717123.10906459), sfix(-4260654.878968743), sfix(-244049.69550265055), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(213154239.42014214), sfix(403324154.3246503), sfix(298934228.56394243), sfix(108656208.47979741), sfix(19442528.83235326), sfix(1374651.8823354272), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(100632771.45255098), sfix(144548525.97117254), sfix(68709223.21566212), sfix(8642253.313427752), sfix(-1901588.576501321), sfix(-422746.00789942744), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-315789397.1264643), sfix(-722794099.864707), sfix(-654118735.2668049), sfix(-292644331.1911708), sfix(-64711525.26654656), sfix(-5662050.537683784), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(17929414.44771913), sfix(79131303.86019795), sfix(117175679.20995481), sfix(78502233.46160278), sfix(24640717.54134373), sfix(2947600.6363987103), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(82458418.68877064), sfix(240247522.37210265), sfix(276926660.98776263), sfix(157010352.28868872), sfix(43724583.576627046), sfix(4778093.188941251), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-23460791.2537128), sfix(-92663268.07657187), sfix(-142112238.105721), sfix(-107032172.11686039), sfix(-39565777.8386527), sfix(-5744278.969071204), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-6397146.322930702), sfix(-24028805.48095149), sfix(-31820511.806685224), sfix(-18509381.97717164), sfix(-4073029.335954738), sfix(-56552.43486736625), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(3050011.2420022204), sfix(18474539.394496165), sfix(44631878.36578405), sfix(50209537.91483778), sfix(26789503.306755394), sfix(5483186.989928411), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(517148.71723198914), sfix(2522233.208947795), sfix(4238557.847164683), sfix(-1197692.3459469432), sfix(-6094348.56766932), sfix(-2974669.313387593), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(339270.92753334576), sfix(1110621.7201144868), sfix(-76119.37129497668), sfix(-7365891.470828565), sfix(-9940529.47759401), sfix(-3617738.3431658503), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(341455.6982418055), sfix(1165095.0139711497), sfix(516720.59310305474), sfix(-3802519.80796042), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(341455.6982418055), sfix(1161850.1514350318), sfix(478807.05443294474), sfix(-5841160.116290659), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(342714.3968006154), sfix(1134651.5853979175), sfix(661587.3947194353), sfix(-5968690.36877523), sfix(-2366246.5557479905), sfix(3927560.515857642), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(482322.9553213024), sfix(-276450.3218354631), sfix(6453322.381012644), sfix(-18034192.46289351), sfix(10380660.890621763), sfix(-1527856.616731387), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(833906.4621978364), sfix(-2848633.6800819454), sfix(14018947.93751711), sfix(-29219290.88263984), sfix(18693097.867451947), sfix(-4012189.7512852596), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-9821052.931330081), sfix(43091295.040953204), sfix(-65478249.04031951), sfix(39843905.31711915), sfix(-11449618.317531204), sfix(1279018.331000639), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(18374100.456088047), sfix(-28847669.888065435), sfix(9928789.921137435), sfix(-514635.30093404953), sfix(-485261.1041316923), sfix(75721.94543366774), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-77418886.09449942), sfix(97428564.19319664), sfix(-52947157.13051562), sfix(13625944.1065332), sfix(-1748658.7306545125), sfix(89658.83180354649), sfix(1.0), sfix(1.0), sfix(1.0)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1

    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res0 += pre_muls[j] * coeffA[i][j+1] * scaler[i][j+1]
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
        sfix(-1.5749999284744263),
        sfix(-1.3125),
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
        [sfix(54526176.32608088), sfix(65247219.44579068), sfix(32006046.074713714), sfix(7923943.678723245), sfix(984189.0328594622), sfix(48944.71820137584), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(192865103.0120833), sfix(240070426.9926721), sfix(119779924.23629904), sfix(29778957.93196547), sfix(3677966.3198565748), sfix(180106.30910166647), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-510381324.4867871), sfix(-868798866.1315242), sfix(-580333366.3549612), sfix(-191472700.69404915), sfix(-31319686.958601706), sfix(-2036651.2877780977), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(327537216.71260244), sfix(768226844.7907487), sfix(700314937.057616), sfix(309966467.1717116), sfix(66946247.44508929), sfix(5673371.038033731), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-43131815.99477697), sfix(-164091091.6451148), sfix(-236676247.98792535), sfix(-160466733.3143964), sfix(-51065383.341082044), sfix(-6161610.986997855), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-36747727.33764432), sfix(-128168308.95155783), sfix(-172285049.5826247), sfix(-108302203.6539769), sfix(-31107663.317879282), sfix(-3216846.678838704), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(2087101.4640634162), sfix(15709661.267336318), sfix(39769777.6102954), sfix(46796084.969950385), sfix(25039696.23234657), sfix(4803187.075747636), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-144121.14019126658), sfix(180561.3301170572), sfix(-2675741.2576385993), sfix(-9947268.186896928), sfix(-11789573.977027576), sfix(-4334326.641569477), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-127494.46511807812), sfix(424258.29907105945), sfix(-1116094.7935159022), sfix(-3827086.455298721), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-89043.95442817024), sfix(-117066.5850873526), sfix(2003880.8647779396), sfix(-12744346.554736916), sfix(11378039.94588343), sfix(-3263777.9112367253), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5220802.147091071), sfix(-15788788.471245699), sfix(15049871.786988106), sfix(-10100232.731534092), sfix(3158240.305135517), sfix(-370542.9327261183), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5449132.151208658), sfix(-4405031.513022467), sfix(-5804964.141218048), sfix(3979877.113788194), sfix(-1038856.535259777), sfix(96273.84312873778), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-23581731.492810823), sfix(28198627.151635606), sfix(-17274081.46651577), sfix(4453823.082763254), sfix(-570199.6391364447), sfix(29129.11124814617), sfix(1.0), sfix(1.0), sfix(1.0)]
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
    degree = k-1

    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res0 += pre_muls[j] * coeffA[i][j+1] * scaler[i][j+1]
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
        sfix(-0.5249999761581421),
        sfix(-0.13124999403953552),
        sfix(-0.06562499701976776),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-18046441.615273327), sfix(-24437477.254202634), sfix(-12471036.142347768), sfix(-3116827.064297064), sfix(-386537.3510751122), sfix(-19122.99207946493), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-44255873.77911193), sfix(-53934696.35511377), sfix(-25111880.03775374), sfix(-5610904.268657946), sfix(-594715.4991424488), sfix(-23169.93909154162), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(65618065.303628914), sfix(105625303.8395786), sfix(66758465.990465984), sfix(20549265.153290097), sfix(3078533.5832871627), sfix(179443.78871244547), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-29063979.99145554), sfix(-61708959.94930902), sfix(-50996485.15356649), sfix(-20659557.985540777), sfix(-4085335.263809073), sfix(-314789.7924890433), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(7681608.363127594), sfix(21148433.846773475), sfix(23694019.184172083), sfix(12981220.614201235), sfix(3484233.452872917), sfix(365816.888367834), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1249289.820570416), sfix(-5015094.286478099), sfix(-6811885.258612178), sfix(-4690756.68885409), sfix(-1593010.7855440096), sfix(-211553.37148156425), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-38459.44491023565), sfix(-539961.8331732235), sfix(-696481.6990041018), sfix(-1142992.8611419275), sfix(-993673.2940718794), sfix(-308951.8718113731), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-72835.42354443808), sfix(-688487.4114524967), sfix(-663199.3568377091), sfix(-48554.22947821363), sfix(968224.1699859845), sfix(780422.0345253259), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-72556.85509701366), sfix(-682612.3656138355), sfix(-618717.7805673504), sfix(88979.67097582393), sfix(1070239.8766488426), sfix(601847.094179962), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-72590.71542181102), sfix(-683822.6705810205), sfix(-613023.1524986076), sfix(269337.3336582422), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(100892.35899275224), sfix(-1877558.737223354), sfix(2411617.6151842508), sfix(-3108838.10493587), sfix(1690772.3977967284), sfix(-502766.42296554), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-10115810.962797076), sfix(42062890.74621107), sfix(-72941349.14111911), sfix(61221777.22353174), sfix(-25605491.379667938), sfix(4091774.4987062328), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(103488909.94557738), sfix(-303023088.5233825), sfix(346970775.64426297), sfix(-194648785.48829237), sfix(52472371.50397071), sfix(-5453308.910882885), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-331808654.7577531), sfix(678211210.8275896), sfix(-537405980.4427567), sfix(203689712.72892973), sfix(-37182009.688243), sfix(2612151.989443728), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(385531615.4832191), sfix(-547621254.264422), sfix(290629052.8507672), sfix(-71743881.38022678), sfix(7710518.502911127), sfix(-233919.67568032537), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-360806609.62491536), sfix(459403261.14694023), sfix(-237031076.21872342), sfix(60559570.5770706), sfix(-7730188.2422850095), sfix(394477.32398728386), sfix(1.0), sfix(1.0), sfix(1.0)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1

    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res0 += pre_muls[j] * coeffA[i][j+1] * scaler[i][j+1]
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
        sfix(-3.674999713897705),
        sfix(-3.1499998569488525),
        sfix(-2.625),
        sfix(-2.0999999046325684),
        sfix(-1.5749999284744263),
        sfix(-1.0499999523162842),
        sfix(-0.26249998807907104),
        sfix(0.0),
        sfix(0.26249998807907104),
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
        [sfix(48102821.09825494), sfix(58109661.19600175), sfix(28598157.709643286), sfix(7085877.97313753), sfix(879983.343805204), sfix(43743.12816808136), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(34923577.1260854), sfix(20694455.65671203), sfix(-2611960.0087911324), sfix(-4428858.793163454), sfix(-1107922.4977746464), sfix(-87946.95074285108), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-99692100.17519645), sfix(-134145910.3617294), sfix(-63160698.87506723), sfix(-11514253.030016579), sfix(-279569.5983717609), sfix(90532.98768525076), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(34905321.04817438), sfix(54875106.05297552), sfix(29635988.70639393), sfix(4320509.598963615), sfix(-989623.7151779556), sfix(-248747.84637155753), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(533253.9120933722), sfix(2181204.1896791863), sfix(6674671.634173146), sfix(6139033.907846577), sfix(2439567.979910172), sfix(360336.6955884755), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-285383.58319005644), sfix(-3775371.7315484243), sfix(-4904833.694379509), sfix(-3620290.4874179633), sfix(-1382356.072554816), sfix(-212327.32703015456), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(453703.0480417191), sfix(-937615.4308475124), sfix(-856083.4330770808), sfix(-1141090.9597053893), sfix(-912949.8347379259), sfix(-272053.5356485099), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(459008.36494349845), sfix(-867070.899654125), sfix(-494241.498791014), sfix(-272210.20110377297), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(459008.36494349845), sfix(-866065.5221765744), sfix(-492099.95972524525), sfix(-75684.77614769808), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(457246.2432246266), sfix(-838900.2761367477), sfix(-652861.9542222458), sfix(364466.14805378), sfix(-513801.16612771805), sfix(149966.5436888816), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(588153.3878858655), sfix(-1802795.3078970294), sfix(2129065.887200043), sfix(-3538276.5451009753), sfix(2108296.9860409866), sfix(-504198.66994065006), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-2837757.6477541355), sfix(14381654.515886381), sfix(-27599339.668685466), sfix(23060900.189611346), sfix(-9484306.328837244), sfix(1459956.994967448), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-391184698.98537344), sfix(782629405.7250316), sfix(-615172022.8852829), sfix(235899016.07169503), sfix(-44456561.814240664), sfix(3303014.438954218), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-194933200.3434711), sfix(246979527.17133594), sfix(-127669638.01508275), sfix(32526329.07714337), sfix(-4139414.7523131147), sfix(210598.5400625078), sfix(1.0), sfix(1.0), sfix(1.0)]
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
    degree = k-1

    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res0 += pre_muls[j] * coeffA[i][j+1] * scaler[i][j+1]
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
        sfix(-2.362499952316284),
        sfix(-2.0999999046325684),
        sfix(-1.5749999284744263),
        sfix(-1.0499999523162842),
        sfix(-0.5249999761581421),
        sfix(0.0),
        sfix(0.26249998807907104),
        sfix(1.0499999523162842),
        sfix(1.5749999284744263),
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
        [sfix(356182309.5969058), sfix(466491705.82749283), sfix(241751639.4558694), sfix(62381429.43887193), sfix(8033753.942203245), sfix(413438.69042629446), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-509875956.7982806), sfix(-926043295.4753422), sfix(-653841561.4167823), sfix(-225616649.9290821), sfix(-38274583.94352039), sfix(-2565245.929133491), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(462403425.7689107), sfix(1030614103.1401607), sfix(922281093.4149601), sfix(409640022.66231614), sfix(89844587.42461212), sfix(7778915.001781806), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-94766126.3741731), sfix(-330516664.9111628), sfix(-409554633.50303537), sfix(-242791520.73265165), sfix(-70161251.19755074), sfix(-7936453.488644466), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(25424851.23680966), sfix(56526123.909503825), sfix(89671933.94905992), sfix(79633530.12530218), sfix(34113326.907516025), sfix(5573628.096983336), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(13682007.813530205), sfix(1662751.6674195651), sfix(-13552311.026028894), sfix(-18169209.650247425), sfix(-12564833.897679819), sfix(-3405371.9571150765), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(13889287.814870058), sfix(3712833.276239312), sfix(-5580184.843928815), sfix(-3331762.9942797096), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(13889287.814870058), sfix(3770176.455452973), sfix(-5535118.605761181), sfix(3010725.1882025544), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(13852453.76429312), sfix(4142818.053914939), sfix(-6511452.935059812), sfix(1739829.6328588042), sfix(7033638.7598649105), sfix(-3303380.400839208), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(3680448.292090265), sfix(52423000.01296879), sfix(-99451127.76671489), sfix(92552135.8478344), sfix(-38036760.526608), sfix(5785963.438884147), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(91414561.04410873), sfix(-226830971.46127203), sfix(256775337.05918363), sfix(-135103229.5740545), sfix(34853436.71498048), sfix(-3568091.3931980818), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(341397442.2017037), sfix(-692369322.3587308), sfix(584408853.2518104), sfix(-239352273.18487412), sfix(48067182.76637761), sfix(-3782288.162173466), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(753027220.44409), sfix(-960755899.1585733), sfix(500382412.5184123), sfix(-128372085.29487407), sfix(16449388.435770553), sfix(-842552.2426331718), sfix(1.0), sfix(1.0), sfix(1.0)]
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
    degree = k-1

    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res0 += pre_muls[j] * coeffA[i][j+1] * scaler[i][j+1]
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
        sfix(-1.0499999523162842),
        sfix(-0.26249998807907104),
        sfix(0.0),
        sfix(0.26249998807907104),
        sfix(0.39374998211860657),
        sfix(0.5249999761581421),
        sfix(1.0499999523162842),
        sfix(1.5749999284744263),
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
        [sfix(864785488.2103035), sfix(1126795748.870778), sfix(579913282.6964318), sfix(148526465.82917666), sfix(18983818.669269845), sfix(969691.0730620925), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1032461492.6598483), sfix(-1545522118.643551), sfix(-903861416.515569), sfix(-255536041.76738563), sfix(-34597365.29389568), sfix(-1765435.312685438), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(522169432.50585365), sfix(1170839029.5539253), sfix(982198353.6943362), sfix(394034764.99391526), sfix(76163024.59413126), sfix(5695680.096457085), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-49449175.152889475), sfix(-151413188.23471132), sfix(-248602691.29754117), sfix(-182691002.6782951), sfix(-59970504.068783216), sfix(-7261950.067391296), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-9099372.848175466), sfix(16192573.024083814), sfix(27604601.742477454), sfix(41887765.390933715), sfix(29370677.200417135), sfix(6449022.419757678), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-9322807.004992682), sfix(13526289.313198494), sfix(15142146.545205982), sfix(13487994.770009141), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-9322807.004992682), sfix(13489180.602265108), sfix(16068040.560241539), sfix(7658911.414656966), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-9339157.133952206), sfix(13828694.402211193), sfix(12896309.870807659), sfix(21682223.6509468), sfix(-23997516.53513946), sfix(4869831.054851827), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-9439080.822245128), sfix(15080375.583675148), sfix(6589387.068183922), sfix(37663916.580343895), sfix(-44365435.35032054), sfix(15314108.318906361), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-7288781.47948388), sfix(-817321.6136405398), sfix(52948459.26143522), sfix(-28815205.764289264), sfix(2320020.717401444), sfix(2560939.631152268), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-31276974.237300538), sfix(84592044.03360073), sfix(-55972885.2164486), sfix(24098528.399745207), sfix(1476114.62444014), sfix(-2010424.1167338137), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-47534349.157339245), sfix(182565471.06895933), sfix(-240461159.7047618), sfix(180402756.00877655), sfix(-60987780.37485215), sfix(7615159.9380435115), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(87440390.4597838), sfix(-315349568.15379727), sfix(388913530.3335601), sfix(-187806615.48041075), sfix(41890611.26566573), sfix(-3542688.4947890257), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(722915893.4463743), sfix(-911881209.4050542), sfix(489619079.5774946), sfix(-125760571.47420584), sfix(16114995.539744528), sfix(-825145.2190310721), sfix(1.0), sfix(1.0), sfix(1.0)]
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
    degree = k-1

    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res0 += pre_muls[j] * coeffA[i][j+1] * scaler[i][j+1]
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
        sfix(-3.674999713897705),
        sfix(-3.1499998569488525),
        sfix(-2.362499952316284),
        sfix(-2.0999999046325684),
        sfix(-1.5749999284744263),
        sfix(-1.0499999523162842),
        sfix(-0.26249998807907104),
        sfix(0.0),
        sfix(0.5249999761581421),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-62147949.27832186), sfix(-84265994.60721476), sfix(-43019343.602841765), sfix(-10752579.780024122), sfix(-1333477.2094725675), sfix(-65967.35873157898), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-279118386.077211), sfix(-365338529.7498629), sfix(-188258323.54687852), sfix(-48158062.05978899), sfix(-6132711.859890568), sfix(-311234.05178750417), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(9248765.3260883), sfix(53009242.023601264), sfix(51824046.04954026), sfix(19760180.831340313), sfix(3296624.0300993314), sfix(199249.77365260443), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(109743268.9940546), sfix(255856248.64421007), sfix(215282190.62602714), sfix(85479571.10725324), sfix(16477535.196495108), sfix(1254011.7971567109), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-105953039.19755754), sfix(-259555568.78579557), sfix(-277673308.66776145), sfix(-150409271.1146375), sfix(-39996339.1202354), sfix(-4157417.3216746696), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(13739477.407726955), sfix(96386053.68101567), sfix(144313719.09592202), sfix(98683332.02580832), sfix(33131945.16828301), sfix(4372511.497364877), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-10617566.589605043), sfix(-1235100.349663957), sfix(-6240322.305632802), sfix(-9779049.826837244), sfix(-887700.6619085653), sfix(1525968.5764576057), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-10508187.27469053), sfix(-80601.33146810993), sfix(-1965126.639043962), sfix(-3861952.500911461), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-10508187.27469053), sfix(-42419.94994585026), sfix(-2116631.6994666425), sfix(-761210.0099099436), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-10721254.150684247), sfix(1454547.656544058), sfix(-6272595.191062654), sfix(4868533.484967864), sfix(-3671777.5948571186), sfix(926356.8965023238), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-5121996.9674574295), sfix(-40203225.4221363), sfix(75950920.74992797), sfix(-65429768.475624636), sfix(24256359.33375883), sfix(-3320074.5810639528), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(6182797.605614412), sfix(71142608.41768076), sfix(-160187463.1946193), sfix(108421637.79093562), sfix(-31676669.49010188), sfix(3388684.3843415654), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-137102197.09320238), sfix(57800844.41820208), sfix(68714097.0034284), sfix(-62527246.87155703), sfix(16951608.115128323), sfix(-1551813.884993074), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(448284299.88989234), sfix(-577560567.4504867), sfix(286564671.96677583), sfix(-72965127.41681165), sfix(9296082.346429773), sfix(-473716.6941443499), sfix(1.0), sfix(1.0), sfix(1.0)]
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
    degree = k-1

    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res0 += pre_muls[j] * coeffA[i][j+1] * scaler[i][j+1]
        poss_res[i] += poss_res0

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

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
        sfix(-2.0999999046325684),
        sfix(-1.5749999284744263),
        sfix(-1.4437499046325684),
        sfix(-1.3125),
        sfix(-1.0499999523162842),
        sfix(-0.5249999761581421),
        sfix(0.0),
        sfix(0.26249998807907104),
        sfix(0.65625),
        sfix(0.7874999642372131),
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
        [sfix(-97022934.44753556), sfix(-124554154.19100517), sfix(-63976800.99133585), sfix(-16427316.038697528), sfix(-2108160.715139953), sfix(-108163.9722337153), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(579394.5153369043), sfix(-26261853.547564976), sfix(-40418601.4031407), sfix(-22294031.603096154), sfix(-5333926.1296562), sfix(-470871.56470225495), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(20013768.07789981), sfix(76031194.63515432), sfix(106448577.2814387), sfix(69554427.21116315), sfix(21414509.311857488), sfix(2513895.4772955715), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(21063985.33783976), sfix(75316740.28210464), sfix(100825143.00595202), sfix(63240465.64979543), sfix(18613019.86291206), sfix(2065621.4134676391), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(9667555.05635242), sfix(35833363.620684996), sfix(46084201.92989421), sfix(25276404.208442777), sfix(5442734.238665707), sfix(237229.50930060045), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-817511.2106334096), sfix(-4681804.5967602795), sfix(-16612347.691187756), sfix(-23292035.072605234), sfix(-13391260.048025584), sfix(-2687529.671589468), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-826730.1330703349), sfix(-2815286.416545621), sfix(-9032184.88876175), sfix(-11813030.934337137), sfix(-5663616.428223072), sfix(-734446.9793131944), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-411326.34893615346), sfix(255940.4699886474), sfix(-450886.71784628293), sfix(-968776.4301519963), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-411326.34893615346), sfix(299372.03526996885), sfix(61315.30857099414), sfix(942550.6237364925), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-426806.4997400393), sfix(523771.52252458787), sfix(-1230980.0242898634), sfix(4545384.207644695), sfix(-4436240.3984763725), sfix(1218288.383630199), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-394546.49720154674), sfix(407490.5139545236), sfix(-1340993.2130257818), sfix(5546626.518884817), sfix(-5946480.900628869), sfix(1945888.5752538352), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(502408.5196799463), sfix(-5020878.850022585), sfix(11829029.875231884), sfix(-10467627.933193114), sfix(3814653.113452294), sfix(-440393.12917827745), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-836957.9099676689), sfix(-224027.95257004592), sfix(5480978.951319333), sfix(-6890245.430181761), sfix(3208374.953618134), sfix(-521044.13882294006), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-2189289.1091921045), sfix(5336652.6535890885), sfix(-3397393.420998688), sfix(41246.81262098342), sfix(549348.6054510233), sfix(-118716.9824198615), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-11526883.515496846), sfix(32544713.726291537), sfix(-34012910.09431243), sfix(16850149.67247842), sfix(-3983273.032556258), sfix(363610.0750143921), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(34510628.07661322), sfix(-63618425.70165188), sfix(45852277.551370345), sfix(-16148216.455922734), sfix(2804841.002168866), sfix(-192918.54037512533), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-12013942.543888297), sfix(15696332.775474953), sfix(-8008750.710941431), sfix(2075436.3389893568), sfix(-268886.16580861976), sfix(13925.34424491773), sfix(1.0), sfix(1.0), sfix(1.0)]
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
    degree = k-1

    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res0 += pre_muls[j] * coeffA[i][j+1] * scaler[i][j+1]
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
        sfix(-2.625),
        sfix(-1.9687498807907104),
        sfix(-1.8374998569488525),
        sfix(-1.5749999284744263),
        sfix(-1.0499999523162842),
        sfix(-0.5249999761581421),
        sfix(-0.26249998807907104),
        sfix(0.0),
        sfix(0.26249998807907104),
        sfix(1.0499999523162842),
        sfix(1.5749999284744263),
        sfix(2.0999999046325684),
        sfix(2.362499952316284),
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
        [sfix(-1396313493.5425096), sfix(-1780128369.0758836), sfix(-907909872.3144611), sfix(-231485781.09563428), sfix(-29500997.778111286), sfix(-1503284.831955572), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(617625237.945898), sfix(552943635.8909942), sfix(28321871.78470393), sfix(-106663149.39693333), sfix(-37010093.29303013), sfix(-3715971.534515095), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(720423594.909181), sfix(1709993330.1600685), sfix(1653980934.346299), sfix(801367180.0290965), sfix(192102486.17997608), sfix(18118860.97531643), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-107948707.84085648), sfix(-446759677.6645519), sfix(-582992423.5593272), sfix(-354598486.41707796), sfix(-105643840.7715499), sfix(-12474117.41512266), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-279520853.234617), sfix(-894868878.0766599), sfix(-1049976108.3210224), sfix(-597247229.6540068), sfix(-168486884.14446622), sfix(-18961122.4007055), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(73390809.45799702), sfix(217680013.0037189), sfix(354138927.35843134), sfix(289530041.3224683), sfix(111759961.84380674), sfix(16492091.837813482), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(17712522.49857151), sfix(-20024300.3469233), sfix(-49406093.96006954), sfix(-50257171.94337029), sfix(-29692531.156778697), sfix(-6690379.31682692), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(19567026.74105523), sfix(-5914929.311658333), sfix(-6784237.773530299), sfix(13602461.173199575), sfix(17700195.243915107), sfix(7210748.462071679), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(19550232.51304539), sfix(-6215932.322467397), sfix(-9212835.560104035), sfix(3641043.066728629), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(19550232.513045393), sfix(-6189004.216171346), sfix(-8812102.38579706), sfix(8016007.574363627), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(19528148.959803414), sfix(-5823189.061874759), sfix(-11092115.002344336), sfix(14503907.505123027), sfix(-7648134.565530669), sfix(1705481.21991327), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-929111.0584164704), sfix(77868390.2136116), sfix(-144976029.49401766), sfix(117808239.98700473), sfix(-45129965.60981653), sfix(6531876.658882516), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(193404836.1513229), sfix(-483220647.2621064), sfix(500131715.09050244), sfix(-250990566.57571784), sfix(59553522.4617627), sfix(-5248004.949892581), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(341203430.46993977), sfix(-922361282.8223388), sfix(1005257575.2964933), sfix(-534852872.35734296), sfix(137951324.26284924), sfix(-13794507.06910803), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1798874330.085901), sfix(3591139675.370711), sfix(-2804625596.739501), sfix(1074071594.405717), sfix(-201976637.26922378), sfix(14950096.671652459), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(705659857.026977), sfix(-838945590.0582633), sfix(321109532.5968853), sfix(-25189809.091230676), sfix(-9370225.123599602), sfix(1506252.2121161234), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-981020883.7601155), sfix(1252738687.8792994), sfix(-637833028.252763), sfix(162647341.20098242), sfix(-20731370.61560899), sfix(1056583.4723297188), sfix(1.0), sfix(1.0), sfix(1.0)]
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
    degree = k-1

    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res0 += pre_muls[j] * coeffA[i][j+1] * scaler[i][j+1]
        poss_res[i] += poss_res0

    comp = [x >= breaks[i] for i in range(m)]
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

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
        sfix(-2.8874998092651367),
        sfix(-2.7562499046325684),
        sfix(-2.362499952316284),
        sfix(-2.0999999046325684),
        sfix(-1.8374998569488525),
        sfix(-1.0499999523162842),
        sfix(-0.5249999761581421),
        sfix(0.0),
        sfix(0.26249998807907104),
        sfix(0.5249999761581421),
        sfix(1.0499999523162842),
        sfix(1.5749999284744263),
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
        [sfix(553346431.1027216), sfix(710536141.2521645), sfix(363797187.83575165), sfix(93003787.65331863), sfix(11879090.96188694), sfix(606584.2046077522), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1520456354.3938577), sfix(-2422006229.3022513), sfix(-1528765707.6140554), sfix(-478652081.6086172), sfix(-74447761.47280024), sfix(-4607387.054130868), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-121333098.02710858), sfix(-13695149.034569226), sfix(129750734.16120681), sfix(92547623.75439091), sfix(23934659.898427878), sfix(2172128.429977085), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(901354974.318376), sfix(1847736147.99045), sfix(1485244756.9089797), sfix(586181313.9404501), sfix(113836447.37080978), sfix(8722680.620966349), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(82817691.74138714), sfix(124174561.04674235), sfix(32414390.3120583), sfix(-26611742.682619665), sfix(-15500906.316865552), sfix(-2205176.7128308257), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-130024587.74663493), sfix(-371244545.9525555), sfix(-429004124.7724088), sfix(-241563741.09023565), sfix(-65587206.3313241), sfix(-6875255.155315163), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-594736.4415452703), sfix(6482490.027690292), sfix(13316681.021732641), sfix(18156592.20335547), sfix(10859105.460022572), sfix(2145546.948054088), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-750485.1211639144), sfix(2490326.782438913), sfix(631903.0685694225), sfix(2131292.563829088), sfix(1703420.5739531815), sfix(166007.52179184242), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-749196.3050317192), sfix(2446696.695247605), sfix(99096.64186222172), sfix(435084.9310341921), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-749196.305031719), sfix(2477011.428957783), sfix(483506.6107462555), sfix(1363580.4920312758), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-753110.083440022), sfix(2540785.060905718), sfix(54677.86236589264), sfix(2778466.785119037), sfix(-1974282.6425236494), sfix(404300.22803470073), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-616623.3648145363), sfix(1588850.5191678351), sfix(2580727.21505017), sfix(-292101.3194615953), sfix(-433907.57771409315), sfix(262297.5379597422), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-2129317.841667293), sfix(6608181.345785239), sfix(-2891846.5638049385), sfix(1041398.6925170108), sfix(796653.856523937), sfix(-335954.7506362684), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-14274289.939151475), sfix(47235801.049154624), sfix(-57406900.32309579), sfix(37711848.65735933), sfix(-11566693.246669808), sfix(1335037.6473253712), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(114253435.37495933), sfix(-250120463.08107793), sfix(217874602.32978335), sfix(-89780987.11690551), sfix(17978436.003998358), sfix(-1406238.1784773297), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(175096670.39585415), sfix(-221957425.54313686), sfix(116876845.98524965), sfix(-29949592.50103254), sfix(3831436.6619099835), sfix(-195906.6124670976), sfix(1.0), sfix(1.0), sfix(1.0)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1

    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res0 += pre_muls[j] * coeffA[i][j+1] * scaler[i][j+1]
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
        sfix(-3.674999713897705),
        sfix(-3.1499998569488525),
        sfix(-2.625),
        sfix(-2.0999999046325684),
        sfix(-1.5749999284744263),
        sfix(-1.0499999523162842),
        sfix(-0.5249999761581421),
        sfix(-0.39374998211860657),
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
        [sfix(-91149967.72323589), sfix(-122696057.88786905), sfix(-62504434.90092328), sfix(-15615020.679730045), sfix(-1936645.585554959), sfix(-95832.611249249), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-375523280.6114793), sfix(-487119118.0894345), sfix(-248496220.07446164), sfix(-62837443.76010731), sfix(-7895700.81149711), sfix(-394490.2247813296), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(757755357.2421823), sfix(1297326718.6523848), sfix(876539647.139085), sfix(292173330.05227184), sfix(48174696.21254904), sfix(3151490.0749785784), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-461322959.32951623), sfix(-1080739347.5156765), sfix(-981077474.237981), sfix(-434136765.37836814), sfix(-93961305.85292596), sfix(-7985655.73491298), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(80949160.13721938), sfix(271400435.4821118), sfix(366785997.8303902), sfix(237384394.85526502), sfix(73268473.94589113), sfix(8669184.646732887), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-3021163.514467666), sfix(-8035548.041275144), sfix(-4570300.674257605), sfix(-9075691.258924037), sfix(-8447521.955530012), sfix(-2162495.1541925324), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-2004298.0562553783), sfix(-4392102.068889152), sfix(-260233.28176403887), sfix(-7839445.604452304), sfix(-9415871.546917366), sfix(-2683577.1696763146), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-2207087.5256407578), sfix(-5813710.836671824), sfix(-4095670.075835852), sfix(-12715139.50685393), sfix(-12204087.37465435), sfix(-3181958.7023584717), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-2182515.997071598), sfix(-5506018.460147957), sfix(-2545689.629546028), sfix(-8788275.59281986), sfix(-7200123.117145215), sfix(-616169.2610891346), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-2176518.9920518673), sfix(-5429984.973892921), sfix(-2025252.2114572024), sfix(-5729968.254727925), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-2134277.376937348), sfix(-6054797.477108398), sfix(1735318.803149638), sfix(-16848190.916739974), sfix(14532686.658460278), sfix(-4214014.833614706), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(8971513.625423633), sfix(-43970842.46717808), sfix(47221780.28398464), sfix(-35688995.129215345), sfix(11980101.266287634), sfix(-1494785.7620749776), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(764769.7424304045), sfix(7759527.300486058), sfix(-31985908.300230186), sfix(16106170.420088066), sfix(-3699042.802275787), sfix(320385.00956221635), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-80471434.7142369), sfix(95376589.93993849), sfix(-59622327.183465935), sfix(15378254.007496566), sfix(-1968199.5698714165), sfix(100496.53512075036), sfix(1.0), sfix(1.0), sfix(1.0)]
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
    degree = k-1

    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res0 += pre_muls[j] * coeffA[i][j+1] * scaler[i][j+1]
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
        sfix(-3.1499998569488525),
        sfix(-2.7562499046325684),
        sfix(-2.625),
        sfix(-2.362499952316284),
        sfix(-2.0999999046325684),
        sfix(-1.5749999284744263),
        sfix(-1.0499999523162842),
        sfix(-0.26249998807907104),
        sfix(0.0),
        sfix(0.26249998807907104),
        sfix(1.0499999523162842),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(798010752.2755041), sfix(1029134778.5294992), sfix(528388858.34956163), sfix(135381571.82442537), sfix(17326606.129762705), sfix(886449.6395752385), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1024364315.72292), sfix(-1643142665.5257967), sfix(-1032246186.340232), sfix(-318014813.99862397), sfix(-48136632.97613936), sfix(-2866900.8026377843), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1075453980.1419542), sfix(2078330795.1975274), sfix(1606737839.397078), sfix(617955235.7196407), sfix(117896645.36867425), sfix(8918134.298705788), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(747179793.523994), sfix(1423481244.4572108), sfix(1084760499.446553), sfix(410125626.44272494), sfix(76559902.51411682), sfix(5632244.676328959), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-360357796.1224511), sfix(-905144715.4998715), sfix(-874692901.9706578), sfix(-414728143.55924827), sfix(-97151515.37024227), sfix(-9009113.869403334), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(25260864.648304723), sfix(68461319.55171108), sfix(108441484.98290111), sfix(81591981.01780859), sfix(28114332.696256727), sfix(3635791.3301120577), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(11824510.877934791), sfix(-3505359.2845525313), sfix(-19826087.917963397), sfix(-23201027.868995313), sfix(-12595292.92140309), sfix(-2488443.314791303), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(10694544.802939603), sfix(2140360.7127545034), sfix(12820173.358117579), sfix(30055833.79464255), sfix(24183689.82743999), sfix(6904577.985396235), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(10560786.986889845), sfix(405566.28249948827), sfix(3976607.325129473), sfix(8274881.481519443), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(10560786.986889843), sfix(381365.9888381982), sfix(4335172.612780963), sfix(3976724.579496471), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(10576093.317469608), sfix(155863.96202987153), sfix(5317367.713016956), sfix(3141344.047920446), sfix(-1674120.6286631713), sfix(-587558.1952830087), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(27254443.361930203), sfix(-62988907.38510638), sfix(96374932.91977836), sfix(-56740160.33815958), sfix(14191454.043556472), sfix(-1160852.0917680874), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-302763401.33043826), sfix(591420612.7881175), sfix(-403733407.8939374), sfix(123442106.01820485), sfix(-15006004.09863235), sfix(318120.9376713732), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(358409268.79957366), sfix(-374494899.13356537), sfix(109174929.10337716), sfix(12980199.747213483), sfix(-10172147.26211017), sfix(1189487.8784896994), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-449536353.3457834), sfix(577348060.503716), sfix(-286823655.8944141), sfix(72896060.7384091), sfix(-9269004.847623717), sfix(471396.79406646267), sfix(1.0), sfix(1.0), sfix(1.0)]
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
    degree = k-1

    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res0 += pre_muls[j] * coeffA[i][j+1] * scaler[i][j+1]
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
        sfix(-3.674999713897705),
        sfix(-3.1499998569488525),
        sfix(-2.625),
        sfix(-2.0999999046325684),
        sfix(-1.8374998569488525),
        sfix(-1.0499999523162842),
        sfix(-0.26249998807907104),
        sfix(0.0),
        sfix(0.5249999761581421),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-28718111.610226206), sfix(-39314233.0411543), sfix(-20127019.781984426), sfix(-5033980.106322212), sfix(-624222.020630392), sfix(-30869.26939627716), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-114636568.97348836), sfix(-148788541.15356845), sfix(-75628501.29357564), sfix(-19015610.96762993), sfix(-2372222.206295618), sfix(-117496.31818505136), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(89577952.94127622), sfix(161691780.03328413), sfix(112932002.61388458), sfix(38154867.21256793), sfix(6279676.208616049), sfix(405212.86599806376), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-14384714.15947623), sfix(-28581100.555936), sfix(-26399967.91230128), sfix(-12874446.914203756), sfix(-3067801.5054599578), sfix(-279921.2122581907), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-49505076.21210054), sfix(-111109102.46602586), sfix(-104045917.4161544), sfix(-49436056.8262081), sfix(-11684159.57679985), sfix(-1092950.0615836214), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(2865646.692833509), sfix(41907381.120905645), sfix(75057723.0139557), sfix(55526721.98147484), sfix(19109800.343222234), sfix(2524624.859399964), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-7962204.879152727), sfix(-2938654.9397723065), sfix(1629842.0634649831), sfix(-3498429.5523328492), sfix(-3932019.5459163547), sfix(-901137.6267710538), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-7945633.254989872), sfix(-2751887.939142397), sfix(2553447.1825160985), sfix(-804151.2668425819), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-7945633.254989872), sfix(-2748659.388087047), sfix(2295058.7274090345), sfix(-2327839.2100173165), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-8752400.39963123), sfix(2076203.3449458317), sfix(-8194589.419388064), sfix(7296780.527398203), sfix(-3264005.0429495093), sfix(505834.1416022236), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(34632364.09167229), sfix(-126888675.80714603), sfix(143833571.49490598), sfix(-81184296.3145646), sfix(22011814.730446838), sfix(-2303821.677857021), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-197232377.45811498), sfix(389276843.9832998), sfix(-315051121.294161), sfix(122416414.35361348), sfix(-23057797.03037944), sfix(1676755.20252611), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(368191155.2975739), sfix(-586656012.8344365), sfix(352498144.41645247), sfix(-103241730.92950083), sfix(14516266.837698199), sfix(-776731.6950269614), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-427150106.7782404), sfix(544787406.0181179), sfix(-283476832.85086155), sfix(72688467.57692693), sfix(-9309688.760694422), sfix(476627.5366396182), sfix(1.0), sfix(1.0), sfix(1.0)]
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
    degree = k-1

    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res0 += pre_muls[j] * coeffA[i][j+1] * scaler[i][j+1]
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
        sfix(-2.0999999046325684),
        sfix(-1.5749999284744263),
        sfix(-1.0499999523162842),
        sfix(-0.5249999761581421),
        sfix(-0.39374998211860657),
        sfix(-0.13124999403953552),
        sfix(0.0),
        sfix(0.13124999403953552),
        sfix(0.7874999642372131),
        sfix(0.9187499284744263),
        sfix(1.0499999523162842),
        sfix(1.5749999284744263),
        sfix(1.8374998569488525),
        sfix(1.9687498807907104),
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
        [sfix(-3431862.255687774), sfix(3114803.0479791253), sfix(2756301.329754767), sfix(756713.4923613857), sfix(92476.541673612), sfix(4343.64770926633), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-416666711.2050295), sfix(-716173770.6386975), sfix(-498585356.21699566), sfix(-174092565.26779407), sfix(-30412385.221125502), sfix(-2124906.76124273), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(281806115.2734494), sfix(1021689055.2030873), sfix(1229142145.1133084), sfix(684131711.1202096), sfix(182659991.94858935), sfix(19032186.265695177), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(144909398.73636055), sfix(467462699.93053526), sfix(366139732.20305747), sfix(29737777.194891624), sfix(-60817335.39049073), sfix(-16699859.321736332), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(21318724.934210755), sfix(-28659056.699851047), sfix(-410463010.2953295), sfix(-554662360.6893966), sfix(-266639138.648063), sfix(-42187050.0216529), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(31894082.19689426), sfix(55228347.594485834), sfix(-143368690.55816683), sfix(-126955533.15604001), sfix(78719336.9276774), sfix(70600951.32325771), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(32212611.33762429), sfix(59163711.50179005), sfix(-123776296.72053607), sfix(-77783816.60481076), sfix(140973822.80281228), sfix(102426483.49567586), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(32210774.275093697), sfix(59061547.53979456), sfix(-126678748.8074011), sfix(-111517993.70218717), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(32210774.275093697), sfix(59158812.89494851), sfix(-127148763.13977708), sfix(-50675708.79779295), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(32272384.398789585), sfix(57789788.63271476), sfix(-113659294.8899593), sfix(-128975483.63649075), sfix(221640186.67803493), sfix(-78072584.5876782), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(14248981.72585133), sfix(177102154.55927622), sfix(-431713475.5744256), sfix(297792320.54481065), sfix(-66561635.99085438), sfix(268369.15216967685), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-5406288.751760868), sfix(284558214.1850675), sfix(-666946409.0966898), sfix(555535472.7366676), sfix(-207910793.529), sfix(31306854.65054701), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(72284158.75644936), sfix(-39610894.696007006), sfix(-127619522.75211272), sfix(108428273.14940609), sfix(-23277860.97085274), sfix(936763.8534647849), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(16605111.701052047), sfix(68316533.00683045), sfix(-171788043.68893346), sfix(73645728.38723852), sfix(9056229.12002593), sfix(-6060321.260748708), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-805049883.8761802), sfix(2325802447.539916), sfix(-2654226543.367137), sfix(1439355128.808739), sfix(-366835240.57359177), sfix(35347140.187471524), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1571998393.3895104), sfix(4277096045.061417), sfix(-4640500359.485867), sfix(2450527962.0751104), sfix(-624278228.1559759), sfix(61570944.11688896), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1998526845.4687605), sfix(-3616076570.053336), sfix(2332091882.757724), sfix(-625954312.3672857), sfix(53697342.28957476), sfix(1875337.0937690418), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-988382800.0012197), sfix(292568972.65035385), sfix(710395109.3618696), sfix(-525823946.0575416), sfix(133624929.56882852), sfix(-11803973.806277025), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1973280845.014175), sfix(-2494837164.9958277), sfix(1272661701.6763523), sfix(-322463259.27052337), sfix(40826813.171695836), sfix(-2066674.4874375209), sfix(1.0), sfix(1.0), sfix(1.0)]
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
    degree = k-1

    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res0 += pre_muls[j] * coeffA[i][j+1] * scaler[i][j+1]
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
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-2.0999999046325684),
        sfix(-1.0499999523162842),
        sfix(-0.06562499701976776),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(549047.0053521192), sfix(-13298612.499761902), sfix(-9236298.950179094), sfix(-2554423.417454561), sfix(-332600.1665507211), sfix(-17056.13112514575), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1018383.4639071621), sfix(-15485029.92328147), sfix(-9747542.623709377), sfix(-1984728.9731456528), sfix(16459.89474361276), sfix(38820.94559878564), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-85571.34225002046), sfix(-12278893.386375366), sfix(-5725932.075149887), sfix(41574.99965444787), sfix(175053.94462276791), sfix(-80849.89699843191), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-85540.72422641556), sfix(-12278000.644220496), sfix(-5718389.0548995305), sfix(45720.94404897396), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-85540.72422641581), sfix(-12275765.835416583), sfix(-5746805.790787858), sfix(197636.4898034938), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-19265.6343664993), sfix(-12753475.749546366), sfix(-4418235.378502045), sfix(-1515559.356127183), sfix(895195.717766535), sfix(-44305.24570716804), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-2454575.2983307457), sfix(-3827848.4883851158), sfix(-17007742.310673244), sfix(6800919.544441841), sfix(-1516299.7083508412), sfix(149348.18859858837), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-13625712.821898295), sfix(15614072.716845507), sfix(-29286969.88785568), sfix(9936426.225193277), sfix(-1674964.2851646384), sfix(113655.97123892311), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-410330.135528518), sfix(-10631131.908330906), sfix(-9208146.578361144), sfix(2453276.555681431), sfix(-306826.4145967394), sfix(15040.94081052339), sfix(1.0), sfix(1.0), sfix(1.0)]
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
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
    degree = k-1

    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res0 += pre_muls[j] * coeffA[i][j+1] * scaler[i][j+1]
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
        sfix(-3.674999713897705),
        sfix(-3.28125),
        sfix(-3.1499998569488525),
        sfix(-2.8874998092651367),
        sfix(-2.362499952316284),
        sfix(-1.9031248092651367),
        sfix(-1.8374998569488525),
        sfix(-1.5749999284744263),
        sfix(-1.0499999523162842),
        sfix(-0.5249999761581421),
        sfix(-0.39374998211860657),
        sfix(-0.13124999403953552),
        sfix(0.0),
        sfix(0.13124999403953552),
        sfix(0.5249999761581421),
        sfix(1.0499999523162842),
        sfix(1.5749999284744263),
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
        [sfix(-2080971470.183222), sfix(-2592032151.3640127), sfix(-1288815908.835255), sfix(-320130096.3784258), sfix(-39740513.726529874), sfix(-1972752.7028144745), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-5920388769.677339), sfix(-7348730196.514973), sfix(-3623584034.4307337), sfix(-886357021.958105), sfix(-107372184.74333173), sfix(-5140702.305239287), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(17449223421.408405), sfix(27761509379.906662), sfix(17481306574.430576), sfix(5458343530.820032), sfix(846564309.5508476), sfix(52244459.79465266), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(18842342220.85559), sfix(29751403914.370995), sfix(18601902161.028305), sfix(5768012013.996495), sfix(888285118.4853653), sfix(54413716.62745856), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-13863259148.526043), sfix(-27368262398.633343), sfix(-21324723626.443264), sfix(-8194436288.889544), sfix(-1554474769.8359678), sfix(-116630364.22987612), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(4088488311.9153714), sfix(9875684725.857664), sfix(9604435845.85386), sfix(4657191914.138954), sfix(1117480757.1988575), sfix(105738498.14245503), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-243848712.19267535), sfix(-1072322879.7518734), sfix(-1467383630.531886), sfix(-944211596.0677414), sfix(-300209236.9988871), sfix(-37868114.39851173), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1073688889.1689373), sfix(-3339982613.300538), sfix(-3946439517.278398), sfix(-2299493248.6362286), sfix(-670725597.1163516), sfix(-78391856.66817227), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-29377998.614553962), sfix(106439314.14974743), sfix(615569019.0316405), sfix(727798968.4955927), sfix(336220669.74685943), sfix(55896365.22893894), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-14874069.203706209), sfix(76856707.04756062), sfix(370229956.7253377), sfix(310404407.3830091), sfix(46867149.077843755), sfix(-17320459.410861716), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-26927649.624021135), sfix(-15552337.199756682), sfix(87735115.42265326), sfix(-120662876.16229601), sfix(-282059720.3915874), sfix(-117937289.59421168), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-26737886.441440333), sfix(-12845023.150839116), sfix(103409513.57646322), sfix(-74730829.34373027), sfix(-214109204.36710826), sfix(-77445440.94013003), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-26722719.539747357), sfix(-12367357.009093866), sfix(110931658.19343208), sfix(-11671911.64619457), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-26722719.539747357), sfix(-12472482.318102963), sfix(110294678.0608728), sfix(-77659718.40555514), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-26692719.88956398), sfix(-13094638.700783122), sfix(113625045.81821878), sfix(-68632938.74497591), sfix(-99650570.71823595), sfix(88575061.53850645), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-22994009.8690607), sfix(-50550243.98144569), sfix(266751197.73921236), sfix(-385200547.9553873), sfix(231653281.0764541), sfix(-51844347.24446641), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-86499358.47677799), sfix(258349708.9736835), sfix(-340050714.5659299), sfix(216391691.9996757), sfix(-69220822.52231579), sfix(8844175.733029425), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(25179138.45337617), sfix(-83604424.0229099), sfix(79622946.44498004), sfix(-41680221.950233124), sfix(10299514.973399071), sfix(-978516.3909879982), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-39187805.931759804), sfix(63355563.20434317), sfix(-53867155.567137174), sfix(18575849.540740587), sfix(-3203744.1990888612), sfix(221835.3563314221), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(2101911.215026808), sfix(-8703806.205463879), sfix(-3491264.5026212884), sfix(949527.4415587471), sfix(-118142.13015455718), sfix(5712.98346270312), sfix(1.0), sfix(1.0), sfix(1.0)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1

    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res0 += pre_muls[j] * coeffA[i][j+1] * scaler[i][j+1]
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
        sfix(-2.0999999046325684),
        sfix(-1.5749999284744263),
        sfix(-0.7874999642372131),
        sfix(-0.5249999761581421),
        sfix(-0.13124999403953552),
        sfix(0.0),
        sfix(0.06562499701976776),
        sfix(0.13124999403953552),
        sfix(0.65625),
        sfix(0.7874999642372131),
        sfix(1.0499999523162842),
        sfix(1.5749999284744263),
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
        [sfix(13238992.35723845), sfix(17604453.817576777), sfix(9193814.77769266), sfix(2384468.340859213), sfix(308349.70042560715), sfix(15927.93221869452), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-101985682.11199524), sfix(-177410699.71902013), sfix(-122649673.58910863), sfix(-42130762.40423667), sfix(-7199002.374465622), sfix(-490060.2691933722), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(118256751.01896834), sfix(313339093.5315521), sfix(314675838.4032122), sfix(152654662.3376638), sfix(36152353.8206955), sfix(3365551.2123763617), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-18265910.39315484), sfix(-100162677.05369608), sfix(-185115488.8996439), sfix(-148362486.22417015), sfix(-54069310.4854677), sfix(-7381924.072029597), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1338698.5298766966), sfix(4940299.234477262), sfix(40920739.894810915), sfix(95789182.2104183), sfix(78605982.10212041), sfix(21682896.732141096), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(430383.0432701723), sfix(-4085126.2888993644), sfix(4340539.637962659), sfix(20206487.389870495), sfix(-910523.6336135543), sfix(-12319211.700369334), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(421548.791038988), sfix(-4281133.529503041), sfix(2809536.8793247407), sfix(15919935.196915623), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(421548.791038988), sfix(-4285349.94549155), sfix(2705139.6413756916), sfix(11643220.276487585), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(421535.0711090453), sfix(-4283713.677757217), sfix(2610274.8247242314), sfix(13758408.36436036), sfix(-15108622.290217452), sfix(-2210849.87213498), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(419603.1591455959), sfix(-4228460.010315193), sfix(1979187.0534171036), sfix(17389629.93148599), sfix(-25774574.52513073), sfix(10789927.714977035), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1246340.2994919482), sfix(-10941575.902926723), sfix(24073201.821509216), sfix(-19449803.472424652), sfix(5325054.549652897), sfix(168725.39124341417), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(2716636.4532064875), sfix(-20021828.196549524), sfix(46564537.065463446), sfix(-47381727.52665604), sfix(22718288.649868283), sfix(-4175979.3668941073), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-7354552.926270254), sfix(22771646.536354184), sfix(-26069908.243593965), sfix(14172049.931142835), sfix(-3322726.2868612427), sfix(223004.21983867467), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(12286833.382312799), sfix(-30418367.95694965), sfix(29722439.849682502), sfix(-13669674.865576494), sfix(3054669.4587995806), sfix(-265362.073536103), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-8117422.787894197), sfix(14704659.813985273), sfix(-9855641.826650223), sfix(3505585.5792323356), sfix(-622468.2041591632), sfix(44093.83970961581), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-83267.33153820406), sfix(459776.1723374192), sfix(234566.84361610204), sfix(-63557.29883202761), sfix(7961.65913125062), sfix(-389.13470591267), sfix(1.0), sfix(1.0), sfix(1.0)]
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
    degree = k-1

    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res0 += pre_muls[j] * coeffA[i][j+1] * scaler[i][j+1]
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
        sfix(-2.0999999046325684),
        sfix(-1.0499999523162842),
        sfix(-0.26249998807907104),
        sfix(0.06562499701976776),
        sfix(0.13124999403953552),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-15122386.066030962), sfix(-13361881.23406647), sfix(-7074606.14658212), sfix(-2200712.14337614), sfix(-349543.72813728283), sfix(-21820.2458901031), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-7996447.085534057), sfix(1325461.749369451), sfix(4611647.317692195), sfix(2259414.813334304), sfix(459491.75135702506), sfix(33219.12886786614), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1745363.6635118115), sfix(11786864.283346225), sfix(-10276630.829412306), sfix(-44146672.611306086), sfix(-36979784.37903579), sfix(-10101333.81925059), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1546232.794468482), sfix(14351444.199237188), sfix(2802858.45826686), sfix(-11518220.919088155), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1546296.5868772645), sfix(14346422.528235752), sfix(2816259.9171733884), sfix(-10836039.411994427), sfix(7446260.730431074), sfix(3875353.690060566), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1543299.2755617937), sfix(14272628.008823145), sfix(3536321.4030601284), sfix(-14379088.565369977), sfix(16453464.99309613), sfix(-5832390.044830013), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-2409061.723567582), sfix(20910755.06629808), sfix(-16651111.803417662), sfix(15962361.022764908), sfix(-5945999.346720215), sfix(588074.2014831987), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(9778365.394368839), sfix(-28061436.546504613), sfix(59984543.02408454), sfix(-41555818.69532858), sfix(14162638.929103822), sfix(-1852710.1600802962), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-47069379.576380245), sfix(138617269.47411084), sfix(-134388654.8057255), sfix(70960887.42051242), sfix(-18101437.04269983), sfix(1803155.9406810566), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(3458005.800806082), sfix(-329.2204255768), sfix(11355997.153725633), sfix(-3463973.3836394455), sfix(508792.4518108481), sfix(-29543.87696882558), sfix(1.0), sfix(1.0), sfix(1.0)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1

    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res0 += pre_muls[j] * coeffA[i][j+1] * scaler[i][j+1]
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
        sfix(0.0),
        sfix(0.13124999403953552),
        sfix(0.26249998807907104),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-13665584.839005588), sfix(-17664254.914336976), sfix(-10132220.49669322), sfix(-2986252.2265601126), sfix(-440272.7845056604), sfix(-25775.75583416605), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-18675088.738474432), sfix(-58465618.82548632), sfix(-77548284.5639485), sfix(-49371158.3255274), sfix(-15091131.914494097), sfix(-1788519.6323197018), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1092547.5303011863), sfix(5236382.3747326), sfix(7226252.233662839), sfix(-2970302.0849439483), sfix(-9607361.434055774), sfix(-4052806.1581203328), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1175056.4755424466), sfix(4423683.419593051), sfix(4960147.977267396), sfix(-2127698.015320824), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1175056.4755424466), sfix(4394648.469620337), sfix(4387839.761631556), sfix(-7214575.230084866), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1175003.9055320534), sfix(4394827.147494763), sfix(4321057.59928529), sfix(-6096987.6968706595), sfix(-6125346.919272776), sfix(9378398.771282617), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1149555.70911753), sfix(3993836.4030141938), sfix(6860136.166536147), sfix(-14201051.863443134), sfix(6965178.872540531), sfix(780756.830670811), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1374287.299924794), sfix(4973873.118499872), sfix(6868308.788308938), sfix(-20313812.372539278), sfix(17842214.562246345), sfix(-5081868.50465773), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-3817529.6510303714), sfix(22199242.400190752), sfix(-37080812.56898234), sfix(32778788.817696318), sfix(-13169142.83990795), sfix(2004097.0519608182), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(12757853.579233887), sfix(-34404323.184617765), sfix(40363463.96214614), sfix(-20276483.75237171), sfix(5026893.27335064), sfix(-494743.4587308528), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-4743304.530897396), sfix(9145590.296771716), sfix(-2636702.591547119), sfix(828582.0653972742), sfix(-131252.6617049771), sfix(8162.75543000057), sfix(1.0), sfix(1.0), sfix(1.0)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1

    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res0 += pre_muls[j] * coeffA[i][j+1] * scaler[i][j+1]
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
        sfix(-3.674999713897705),
        sfix(-3.1499998569488525),
        sfix(-2.625),
        sfix(-2.0999999046325684),
        sfix(-1.5749999284744263),
        sfix(-1.3125),
        sfix(-1.0499999523162842),
        sfix(-0.7874999642372131),
        sfix(-0.5249999761581421),
        sfix(-0.26249998807907104),
        sfix(0.26249998807907104),
        sfix(0.5249999761581421),
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
        [sfix(3992269.996041193), sfix(4846422.365099799), sfix(2389108.6232957686), sfix(592199.6773424951), sfix(73539.52291897009), sfix(3654.76176075388), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(8696638.829280926), sfix(9948553.090424195), sfix(4446271.380368702), sfix(952422.8170334708), sfix(94853.11511650759), sfix(3275.73783636711), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-18338935.225661036), sfix(-30041812.312185686), sfix(-19092640.92814005), sfix(-5932803.616840493), sfix(-904716.9281183695), sfix(-54249.52184144948), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5305427.114300643), sfix(12927591.544222672), sfix(12125131.203408426), sfix(5399903.981203002), sfix(1150785.8365115013), sfix(94756.13921419095), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(2369323.121526834), sfix(5901077.942820107), sfix(5358766.09585784), sfix(2122780.1095905174), sfix(352649.79968584096), sfix(16577.83664717107), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1131404.851813502), sfix(-4639752.018650753), sfix(-7354184.404495802), sfix(-5555016.207667227), sfix(-1969540.6079446718), sfix(-264852.1695391191), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-266849.574072884), sfix(-1278948.217777188), sfix(-2120723.394606836), sfix(-1474440.7376254436), sfix(-376526.66364555195), sfix(-15765.27116585591), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(82230.59103506972), sfix(313754.3470117374), sfix(789427.6164797699), sfix(1187633.347729727), sfix(842717.4474688976), sfix(207930.88998501765), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(39184.72176751915), sfix(37425.33582717083), sfix(76428.10772033663), sfix(263346.88916619564), sfix(240809.52987872795), sfix(50431.9732873966), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(33042.21012690402), sfix(-15764.83913475003), sfix(-108506.96782685474), sfix(-59681.89239180594), sfix(-42948.31225159522), sfix(-49958.7958167891), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(33063.84343710296), sfix(-15344.39397721008), sfix(-105025.77499895835), sfix(-43494.43448557556), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(33082.0719344175), sfix(-15592.73269965888), sfix(-103773.9636250666), sfix(-45204.19130768427), sfix(-9307.82554853216), sfix(28741.819232631), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(4240.2050164639), sfix(128852.73943443251), sfix(-351521.20854875015), sfix(101385.18587803196), sfix(10127.58980027038), sfix(-6237.40813047814), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(144674.6208367344), sfix(-311727.2462932902), sfix(51340.31654407971), sfix(-17365.42551986554), sfix(2994.8975922093), sfix(-198.60173993116), sfix(1.0), sfix(1.0), sfix(1.0)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1

    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res0 += pre_muls[j] * coeffA[i][j+1] * scaler[i][j+1]
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
        sfix(-2.625),
        sfix(-2.0999999046325684),
        sfix(-1.5749999284744263),
        sfix(-1.3125),
        sfix(-0.7874999642372131),
        sfix(-0.5249999761581421),
        sfix(-0.39374998211860657),
        sfix(-0.13124999403953552),
        sfix(0.0),
        sfix(0.13124999403953552),
        sfix(0.5249999761581421),
        sfix(1.0499999523162842),
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
        [sfix(-7255992.436937132), sfix(8824536.791399373), sfix(7334934.615634983), sfix(2005989.613671333), sfix(246868.24892322085), sfix(11730.24754661612), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-487713006.22075844), sfix(-780807224.7174127), sfix(-512154040.4828777), sfix(-168993486.83742166), sfix(-27914619.512911346), sfix(-1844471.2108120297), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1422142519.6448247), sfix(-2512331389.3087416), sfix(-1795278508.0449076), sfix(-644264776.781811), sfix(-115899334.44595827), sfix(-8356428.593383093), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1372512367.6413224), sfix(4153871401.692729), sfix(4579114372.508934), sfix(2410083073.07779), sfix(617451663.614916), sfix(62226295.420202106), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(516464657.2851199), sfix(1405284246.0905552), sfix(1044696379.6337086), sfix(134835502.149885), sfix(-115769949.73252618), sfix(-32401620.907389566), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-145995211.06471878), sfix(-1078614961.8793623), sfix(-2683146590.053891), sfix(-2664077539.032729), sfix(-1166936958.3414884), sfix(-190355511.96450967), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(39966600.77992126), sfix(11319153.503720472), sfix(-111034117.45723106), sfix(393405146.06845886), sfix(665126748.5727913), sfix(252605319.96913058), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(42394120.93449146), sfix(28915213.687054414), sfix(-63083254.97985142), sfix(451727743.12763524), sfix(692046933.9344084), sfix(252898329.25560352), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(40901934.56687197), sfix(9372360.49115331), sfix(-167023310.35552162), sfix(171058532.1626042), sfix(307455074.78324133), sfix(39205044.319723636), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(40867337.07770763), sfix(8367476.933289697), sfix(-180771711.55698803), sfix(69662129.81222676), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(40867337.07770763), sfix(8502361.176824316), sfix(-179312544.3719231), sfix(153608165.8706184), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(40829145.19776185), sfix(9337730.651245933), sfix(-184727596.1795159), sfix(153373885.53498963), sfix(87872101.55462988), sfix(-95364859.83671132), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(34147848.47564991), sfix(68438952.22622634), sfix(-399172292.35992324), sfix(553820750.7890009), sfix(-297727263.94530195), sfix(57760333.44315739), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(154910201.48864117), sfix(-453254827.90975136), sfix(506115054.5617243), sfix(-235369160.4033213), sfix(48050013.47363158), sfix(-3175793.0400329623), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-456990908.27065945), sfix(650367208.1610111), sfix(-217334102.7187705), sfix(-43093440.75265616), sfix(37711541.58462614), sfix(-5499344.463479454), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(472533044.54508513), sfix(-320117829.83996844), sfix(-88103198.41850999), sfix(140872555.4735696), sfix(-41986109.81961999), sfix(4000750.0527230417), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1362399244.4372709), sfix(1753364904.8096797), sfix(-874716042.2283856), sfix(222911558.2200859), sfix(-28418518.828543287), sfix(1449021.295303113), sfix(1.0), sfix(1.0), sfix(1.0)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1

    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res0 += pre_muls[j] * coeffA[i][j+1] * scaler[i][j+1]
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
    
    breaks = [
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
        sfix(-3.28125),
        sfix(-3.1499998569488525),
        sfix(-2.625),
        sfix(-2.0999999046325684),
        sfix(-1.8374998569488525),
        sfix(-1.7062499523162842),
        sfix(-1.0499999523162842),
        sfix(-0.65625),
        sfix(-0.5249999761581421),
        sfix(-0.13124999403953552),
        sfix(0.0),
        sfix(0.13124999403953552),
        sfix(0.5249999761581421),
        sfix(0.7874999642372131),
        sfix(0.9187499284744263),
        sfix(1.0499999523162842),
        sfix(1.181249976158142),
        sfix(1.5749999284744263),
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
        [sfix(-277886251.84099996), sfix(-340430181.625271), sfix(-165961925.2366806), sfix(-40372894.42064087), sfix(-4906768.494955614), sfix(-238463.65448450047), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-4808777388.157497), sfix(-6145066759.117026), sfix(-3141078995.97422), sfix(-802942337.5545294), sfix(-102652929.95512451), sfix(-5250954.903676543), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-9961887398.035515), sfix(-13073561538.514324), sfix(-6867487510.362565), sfix(-1805095600.8415406), sfix(-237415699.15815917), sfix(-12500116.167755732), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-817217382.8107865), sfix(314416070.5834872), sfix(973656282.068083), sfix(491429253.1101974), sfix(98933137.87845403), sfix(7207109.345564062), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(9877111618.810587), sfix(16609691367.052368), sfix(10906337864.157537), sfix(3518886319.133465), sfix(560352844.0219074), sfix(35339777.66023175), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(11838192519.039518), sfix(19185684045.988934), sfix(12183868057.673712), sfix(3805112844.886252), sfix(585904037.4494675), sfix(35637728.01387041), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-5124918906.181871), sfix(-12376323720.692242), sfix(-11333609986.17655), sfix(-4967233477.37522), sfix(-1052271787.4862058), sfix(-86890045.8792924), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-2657357390.198897), sfix(-6490200131.142101), sfix(-5711863817.025393), sfix(-2280033118.902452), sfix(-409419270.6744741), sfix(-25317129.433922976), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1019301297.7501576), sfix(-2102804951.7391555), sfix(-1008827771.1976815), sfix(242042639.0819523), sfix(267209679.85357887), sfix(47335218.59501675), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(354705963.7228124), sfix(2084864959.0614836), sfix(4108277919.198304), sfix(3375557127.224596), sfix(1228740338.9812074), sfix(165603964.7439754), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-21748563.498821124), sfix(257551234.3626027), sfix(536975276.3777102), sfix(-136714239.61894763), sfix(-508971717.309894), sfix(-180278179.95699584), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-66922435.21591382), sfix(-38507394.93119965), sfix(-236631475.2816957), sfix(-1144054056.14388), sfix(-1162500589.7096148), sfix(-349223783.75021136), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-58548578.76107325), sfix(48901521.91306051), sfix(134515932.63503292), sfix(-343712537.2432649), sfix(-287819695.77711916), sfix(37362169.77361334), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-58409808.395946965), sfix(52144251.19544609), sfix(164830463.65376607), sfix(-201188762.3715837), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-58409808.395946965), sfix(52108440.17209695), sfix(162730234.42156532), sfix(-222347842.40438172), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-58365922.42918776), sfix(51021977.248246066), sfix(173537956.43997326), sfix(-275599703.015015), sfix(110764626.58767831), sfix(1648967.9907706298), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-57614167.075632796), sfix(43179336.37148945), sfix(207363428.5224842), sfix(-350645776.2316575), sfix(195859808.22079057), sfix(-37532885.00615415), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-56238818.742535144), sfix(34000372.60765441), sfix(231939498.95100304), sfix(-383636682.4717723), sfix(218059472.58077335), sfix(-43521975.18585039), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-58852636.058077484), sfix(47793696.11956715), sfix(202818574.6192138), sfix(-352889909.93475866), sfix(201824272.6682171), sfix(-40092126.10782903), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-76815825.16457292), sfix(132506864.66368732), sfix(42900685.949142575), sfix(-201833932.07597122), sfix(130427416.47303768), sfix(-26583364.82245397), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-175071976.82831433), sfix(528512094.5861255), sfix(-596566669.8644003), sfix(315385198.8589276), sfix(-79137764.80939138), sfix(7448670.123960962), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-98782406.13090448), sfix(330276964.9119338), sfix(-399367543.72149193), sfix(224146621.26008716), sfix(-60799982.535181694), sfix(6456056.40171646), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(88028391.10085796), sfix(-160022646.43140388), sfix(111122124.1653983), sfix(-39912862.09890049), sfix(7154272.453798411), sfix(-511629.261699351), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(807012.9192878645), sfix(-3316404.312439679), sfix(-1319127.9730486285), sfix(358813.66944430163), sfix(-44631.6113645175), sfix(2157.28355141309), sfix(1.0), sfix(1.0), sfix(1.0)]
    ]
    scaler = [
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
    degree = k-1

    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res0 += pre_muls[j] * coeffA[i][j+1] * scaler[i][j+1]
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

def func3_kan_model_evaluate(x):
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

def func3_kan_model_evaluate_vectorized(x):
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