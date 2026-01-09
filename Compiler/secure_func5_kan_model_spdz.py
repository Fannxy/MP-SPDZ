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
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-2.0999999046325684),
        sfix(-0.26249998807907104),
        sfix(0.0),
        sfix(0.13124999403953552),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-114768236.40929449), sfix(-342937958.7071008), sfix(-409322361.04160786), sfix(-271574384.76579136), sfix(-110665668.19579825), sfix(-28429846.15389289), sfix(-4502906.5910860775), sfix(-402551.78761086194), sfix(-15570.53320635267)],
        [sfix(1491943.8776342454), sfix(-3179677.926652555), sfix(55817452.05138961), sfix(175322884.79485935), sfix(240941711.1636317), sfix(180766872.31098723), sfix(76526992.2080852), sfix(17197238.740853533), sfix(1598926.7656651048)],
        [sfix(479726.2831288758), sfix(-15871982.038069634), sfix(-8253683.585146025), sfix(7382225.7865664605), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(479726.28312887566), sfix(-15849510.608014707), sfix(-7714447.557028164), sfix(9991888.354052592), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(402452.69487048313), sfix(-14400469.179187346), sfix(-17773249.29094088), sfix(43411889.56057228), sfix(-56398007.29522627), sfix(41792331.50728066), sfix(-17756847.73542218), sfix(4042133.339239906), sfix(-384593.9858050815)],
        [sfix(1771813004.2503383), sfix(-4269658653.804439), sfix(4314103237.079771), sfix(-2406104544.862959), sfix(802531628.7331417), sfix(-162503155.2086548), sfix(19168127.765448797), sfix(-1157597.0584458928), sfix(24465.9355447199)]
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)]
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
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-1.0499999523162842),
        sfix(-0.5249999761581421),
        sfix(-0.26249998807907104),
        sfix(0.0),
        sfix(0.26249998807907104),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(23330773.239141293), sfix(91827477.3182024), sfix(146089568.33853495), sfix(125074376.84432077), sfix(63692853.319187045), sfix(19917765.972029895), sfix(3759331.789295589), sfix(393516.2793943669), sfix(17560.15399147705)],
        [sfix(126599.67101175246), sfix(-662068.780408719), sfix(-7136442.400702938), sfix(-22393455.331135392), sfix(-48500543.313820675), sfix(-64606154.72424744), sfix(-47977366.11222018), sfix(-18323712.882948946), sfix(-2825210.329763183)],
        [sfix(216450.36775285623), sfix(536451.4078732827), sfix(-142732.28310650613), sfix(924994.3953915464), sfix(89342.39209731246), sfix(190331.73891446716), sfix(6025995.190408905), sfix(7394414.1203949815), sfix(2533077.095169125)],
        [sfix(216440.06182997557), sfix(533690.7849057382), sfix(-199373.8833194223), sfix(661327.7508609542), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(216440.06182997557), sfix(533051.0183205925), sfix(-80292.08228719291), sfix(455197.8931336604), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(195169.8226002034), sfix(817969.5919851867), sfix(-1694738.7175100562), sfix(5458012.374209665), sfix(-8589249.655716555), sfix(7263985.321240325), sfix(-3376058.784253984), sfix(806500.2229824819), sfix(-76813.47544905466)],
        [sfix(943407567.8318348), sfix(-2718936800.024069), sfix(3350732805.186712), sfix(-2293439709.6312585), sfix(947857415.6595751), sfix(-240027133.84720522), sfix(35816034.11610676), sfix(-2792445.2251871456), sfix(80646.30395259899)],
        [sfix(4978225601.700524), sfix(-10752284255.825905), sfix(10114845836.781223), sfix(-5415307491.187235), sfix(1805745358.515055), sfix(-384179159.66162616), sfix(50944757.53640572), sfix(-3850850.2950506457), sfix(127064.34231742028)]
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)]
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
        sfix(-0.26249998807907104),
        sfix(0.06562499701976776),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(80274892.12894517), sfix(203822311.66470936), sfix(242102317.3947601), sfix(160604462.4940676), sfix(64864090.4875421), sfix(16436884.729239294), sfix(2564835.1749874107), sfix(226023.5895474075), sfix(8628.86111088924)],
        [sfix(2187310.671942218), sfix(-14689125.119721482), sfix(14317230.751486365), sfix(68266594.33746246), sfix(72182649.26819602), sfix(33514872.628674492), sfix(6099550.522882364), sfix(-223279.0532812406), sfix(-150870.44308433443)],
        [sfix(1797551.9390563031), sfix(-19449973.16761526), sfix(-8876555.513498206), sfix(10703176.618551837), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(1797689.9028713545), sfix(-19472173.092793062), sfix(-8582448.318914967), sfix(10689559.896266287), sfix(4249595.511812867), sfix(-19604212.80944889), sfix(15071990.874515984), sfix(-3777755.9724307903), sfix(729.55356591927)],
        [sfix(54778946.80103814), sfix(-321674739.24837816), sfix(730176452.1887177), sfix(-993679366.6174026), sfix(827843899.5495284), sfix(-433083928.3511289), sfix(139258187.91948828), sfix(-25217420.85534804), sfix(1971159.1507022537)],
        [sfix(1550706129.4602249), sfix(-3760674248.793516), sfix(3819242694.8670654), sfix(-2147813135.242736), sfix(724261862.9850513), sfix(-148975980.85861138), sfix(18014253.913998254), sfix(-1138193.544356227), sfix(26781.15417907335)]
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)]
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
        sfix(-999.0),
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
        sfix(-1.0499999523162842),
        sfix(-0.5249999761581421),
        sfix(0.13124999403953552),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(50943529.61728657), sfix(213752169.40474996), sfix(356287713.87060124), sfix(316287835.3056348), sfix(165653426.19547886), sfix(52951768.29679293), sfix(10169614.699287038), sfix(1079536.6550938548), sfix(48727.0468118781)],
        [sfix(-844825.6009415325), sfix(339224.98645930126), sfix(-9389479.389126271), sfix(-40080584.32163513), sfix(-89964096.61284931), sfix(-120398228.15757518), sfix(-90572202.87693748), sfix(-35160077.7154154), sfix(-5504696.949105631)],
        [sfix(-679422.5630185978), sfix(2555474.74890714), sfix(3104804.7380931675), sfix(1521224.778089799), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-680633.1499092992), sfix(2526019.1961322753), sfix(3345460.0255389684), sfix(2308270.4725846257), sfix(-2286198.4597107978), sfix(-4501711.365202144), sfix(476118.0936183784), sfix(4451348.560981296), sfix(-2031616.4390992925)],
        [sfix(-2364413.865569379), sfix(17724615.85062744), sfix(-54870783.696793556), sfix(124940235.3240142), sfix(-155229896.45982987), sfix(107029072.43694551), sfix(-41334009.80525087), sfix(8427506.448746124), sfix(-710719.4432440223)],
        [sfix(973489022.0131245), sfix(-2338947801.496502), sfix(2391076355.2868543), sfix(-1351930768.726189), sfix(462022500.7067506), sfix(-97325199.41631813), sfix(12247639.520360013), sfix(-829844.83131574), sfix(22496.81116478028)]
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)]
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
        sfix(-0.5249999761581421),
        sfix(-0.13124999403953552),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-62322124.82721938), sfix(-185084949.49872446), sfix(-225493075.9165815), sfix(-151934939.00600094), sfix(-62506445.28891748), sfix(-16151919.362870531), sfix(-2567833.3461419935), sfix(-230144.0830136933), sfix(-8918.2311573588)],
        [sfix(517079.8284261013), sfix(3691855.403913326), sfix(26346727.527492736), sfix(68179903.73388083), sfix(95332450.2784766), sfix(76056744.84144695), sfix(34415763.60502527), sfix(8230540.728646423), sfix(809621.3067511979)],
        [sfix(-80363.84883391633), sfix(-2471697.565824737), sfix(-585855.3372173058), sfix(3309630.9485996775), sfix(1670705.6635385095), sfix(-6107745.017565723), sfix(-7466956.220748122), sfix(-2548754.8528741905), sfix(-92057.4126447294)],
        [sfix(-80356.82465856543), sfix(-2472695.3818654935), sfix(-641334.3742670163), sfix(2639597.6691742996), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-80356.82465856528), sfix(-2576535.556595947), sfix(539029.4525805303), sfix(1112372.684596115), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-3395442.783065941), sfix(26360951.033970386), sfix(-106375134.45967421), sfix(215138469.69738117), sfix(-245745544.2758123), sfix(161050753.2422444), sfix(-60094679.21623269), sfix(11873321.652708825), sfix(-963753.6940534814)],
        [sfix(489914759.4447513), sfix(-1359516383.324308), sfix(1612865534.2483606), sfix(-1077526135.954554), sfix(443091292.3833734), sfix(-115020850.78860751), sfix(18429476.48595109), sfix(-1668083.9726899501), sfix(65354.20277743158)]
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)]
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
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
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
        sfix(-1.0499999523162842),
        sfix(-0.26249998807907104),
        sfix(0.0),
        sfix(0.13124999403953552),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(13895959.62257754), sfix(29114748.435019), sfix(43154700.855129346), sfix(34533978.38684441), sfix(16111608.286041878), sfix(4611011.580443376), sfix(802759.4971141923), sfix(78299.02547857659), sfix(3287.44077368227)],
        [sfix(53316.39284170101), sfix(-15381701.393320888), sfix(-10304538.78580183), sfix(-6332485.317642766), sfix(-35228972.04863628), sfix(-61448929.61282953), sfix(-45750028.168700844), sfix(-15684381.957338078), sfix(-1992463.700805535)],
        [sfix(82331.1059725385), sfix(-14899083.010616418), sfix(-7024553.856012585), sfix(6531729.932351945), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(82331.1059725385), sfix(-14883629.234166691), sfix(-6646868.882039431), sfix(8254943.911038588), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(19878.50039430575), sfix(-13714206.638979275), sfix(-14746244.815149873), sfix(35081768.63968085), sfix(-45138439.7516286), sfix(33392846.1874483), sfix(-14183194.586101143), sfix(3220411.8968747924), sfix(-304692.1444043118)],
        [sfix(1448713467.108723), sfix(-3506477821.401654), sfix(3555695187.2320576), sfix(-1993119599.9845657), sfix(669179398.1749573), sfix(-136797017.67245418), sfix(16383829.01975121), sfix(-1017806.8271221368), sfix(23054.15668866748)]
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)]
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
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-2.0999999046325684),
        sfix(-0.26249998807907104),
        sfix(0.0),
        sfix(0.13124999403953552),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-60785535.53725081), sfix(-171580974.46078947), sfix(-196809042.15143657), sfix(-126699381.87388556), sfix(-50444503.53307399), sfix(-12725458.241983965), sfix(-1986448.0910894617), sfix(-175494.552392329), sfix(-6721.8228954382)],
        [sfix(750057.201053754), sfix(-1950611.4415141954), sfix(27032363.195260223), sfix(85050394.45584714), sfix(112964054.49569546), sfix(80873836.5504561), sfix(32532820.697270554), sfix(6939772.470737391), sfix(612493.1656019624)],
        [sfix(251455.86737290272), sfix(-8173119.191473213), sfix(-4140764.7708647153), sfix(4397497.273244307), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(251455.86737290275), sfix(-8163003.590485404), sfix(-3880470.4086403004), sfix(5335478.704498732), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(217768.888084071), sfix(-7528358.4244391965), sfix(-8330336.081800236), sfix(20435513.997668143), sfix(-26289375.51195953), sfix(19147715.248984117), sfix(-7972721.040681919), sfix(1780417.6572101482), sfix(-166962.05653705593)],
        [sfix(1055182681.3632298), sfix(-2553232630.4680424), sfix(2597327455.5078435), sfix(-1460834158.863238), sfix(493053281.3642759), sfix(-101591342.7526105), sfix(12318865.522501605), sfix(-782109.4333280902), sfix(18592.23234588387)]
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)]
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
        sfix(-1.0499999523162842),
        sfix(-0.26249998807907104),
        sfix(0.0),
        sfix(0.26249998807907104),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-6358640.469661748), sfix(-27470844.04962379), sfix(-48126763.58125228), sfix(-44120778.12488275), sfix(-23593665.441273775), sfix(-7651049.037362871), sfix(-1484973.3712339103), sfix(-158906.90149001597), sfix(-7218.06336866319)],
        [sfix(626635.4990834101), sfix(977288.0589938392), sfix(-248252.07043185), sfix(1335129.850111891), sfix(7930277.777059487), sfix(12913090.519721754), sfix(9840095.582888015), sfix(3591630.052243777), sfix(499658.8339484043)],
        [sfix(620908.7048135843), sfix(879672.5250813775), sfix(-953948.0771120557), sfix(-1606663.80454183), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(620908.7048135842), sfix(884731.7951033252), sfix(-1102847.3829474612), sfix(-816922.8851026968), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(610737.6227284153), sfix(1053641.7970346708), sfix(-2243361.1740685487), sfix(3588042.0357401986), sfix(-11908488.850897858), sfix(21120809.750410512), sfix(-16982314.509730313), sfix(6260230.43013774), sfix(-854398.66236275)],
        [sfix(-6652681.5913529815), sfix(38896501.99808789), sfix(-82011343.57930502), sfix(85868956.2741478), sfix(-45390176.802531704), sfix(9441792.273662988), sfix(1291023.6685806634), sfix(-914008.1479702924), sfix(114796.18412726455)],
        [sfix(-419245748.33619666), sfix(1094901477.2825623), sfix(-1222937669.1404061), sfix(765300475.9335818), sfix(-293941832.89364576), sfix(71101750.16287728), sfix(-10596880.745854057), sfix(891079.612177074), sfix(-32410.88494838068)]
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)]
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
        sfix(-0.5249999761581421),
        sfix(0.0),
        sfix(0.13124999403953552),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(4975319.8853534395), sfix(55058084.845812276), sfix(106853819.95633568), sfix(107185057.34413451), sfix(62528740.1564759), sfix(21914560.124644227), sfix(4552059.90828521), sfix(516967.73934732977), sfix(24749.62820088909)],
        [sfix(-1327206.6360591962), sfix(15552282.426442469), sfix(11957774.354897553), sfix(-1200279.3637219858), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-1327206.6360591957), sfix(15287314.587524906), sfix(8915753.455509529), sfix(-10207131.362671267), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-1254287.5530635307), sfix(13937600.094465056), sfix(18046929.331347764), sfix(-38956228.54517842), sfix(43585718.674368), sfix(-26846818.328020222), sfix(8971061.366402952), sfix(-1463296.7109570384), sfix(83508.31665457584)],
        [sfix(-1381115893.8832798), sfix(3396077504.9900637), sfix(-3512334989.0539594), sfix(2020556344.7225454), sfix(-702287985.1531917), sfix(150666715.3226887), sfix(-19386565.094055627), sfix(1354416.62985193), sfix(-38563.35625608598)]
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)]
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
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-1.0499999523162842),
        sfix(-0.5249999761581421),
        sfix(0.0),
        sfix(0.06562499701976776),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(2078862.466344383), sfix(51365382.0565173), sfix(105460800.96076788), sfix(105232896.1307851), sfix(59704695.82971589), sfix(20186445.9635757), sfix(4035963.5708635673), sfix(441286.32420650806), sfix(20367.93689762692)],
        [sfix(-1827416.4261687913), sfix(17475430.302662935), sfix(19466546.904820587), sfix(25564938.60491436), sfix(73898559.43510473), sfix(109360920.17157368), sfix(79395839.97759624), sfix(28597151.246930417), sfix(4144059.3020991106)],
        [sfix(-1964896.8963311324), sfix(15893671.03749611), sfix(11660016.893324718), sfix(-2651665.7496613464), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-1964896.8963311324), sfix(15626027.253082946), sfix(8609370.82630225), sfix(-10911314.961527755), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-1965328.5129330284), sfix(15642381.154175293), sfix(8375988.26129413), sfix(-9213373.521393755), sfix(-7625960.615502325), sfix(21454771.54790786), sfix(-13450146.382676309), sfix(1731308.8399470134), sfix(588639.1481687032)],
        [sfix(-61476019.20365629), sfix(354869082.4192766), sfix(-820421705.1686858), sfix(1117644243.4500353), sfix(-933857076.9365125), sfix(490917426.0080539), sfix(-158780958.85479167), sfix(28912886.339822877), sfix(-2269841.477241151)],
        [sfix(-944176713.3819116), sfix(2141768096.4476256), sfix(-1976770050.9342628), sfix(971301875.6499509), sfix(-263743291.0289866), sfix(35572677.82202248), sfix(-822081.4542078782), sfix(-331490.42371107877), sfix(27542.01628450062)]
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)]
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
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-3.1499998569488525),
        sfix(-2.0999999046325684),
        sfix(-1.0499999523162842),
        sfix(-0.26249998807907104),
        sfix(0.0),
        sfix(0.26249998807907104),
        sfix(0.5249999761581421),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-61620340.3388536), sfix(-129116636.95007241), sfix(-118070319.3581701), sfix(-61660993.11439004), sfix(-20121629.824648358), sfix(-4201437.103765073), sfix(-548134.1101026086), sfix(-40849.38694230434), sfix(-1331.3416184101)],
        [sfix(167540455.14624843), sfix(445560750.79450154), sfix(491930322.794489), sfix(292882527.1218119), sfix(100997533.73680931), sfix(19700273.96738727), sfix(1818479.0649043235), sfix(9678.5268228708), sfix(-7390.21753335149)],
        [sfix(55564868.39885655), sfix(314404837.0872354), sfix(768967409.6927695), sfix(1039064277.1435941), sfix(842629422.2434934), sfix(421107993.01634777), sfix(127403258.19078068), sfix(21464014.935988184), sfix(1549778.9981054836)],
        [sfix(234181.6685599912), sfix(-382128.725776428), sfix(2835056.831971018), sfix(7085390.356891445), sfix(15189895.83629678), sfix(30038444.169333477), sfix(29517257.73063794), sfix(13118177.688434185), sfix(2156880.3599585146)],
        [sfix(219790.6933407304), sfix(-618026.3472893381), sfix(1303248.6708024587), sfix(1485956.1754119687), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(219790.69334073036), sfix(-635114.9468289536), sfix(1169670.5133836498), sfix(-1359997.9308027367), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(219800.1066209166), sfix(-629936.7246063026), sfix(1032403.8625826619), sfix(-334450.47562934656), sfix(-2602992.2151220012), sfix(196633.79303002977), sfix(6807587.037702972), sfix(-7284446.845388082), sfix(2320531.3779731547)],
        [sfix(143487.094412463), sfix(388924.1564808343), sfix(-4917282.618743365), sfix(19514571.664463658), sfix(-43982476.42192428), sfix(55397614.09476691), sfix(-39211401.41590798), sfix(14635958.257500488), sfix(-2247260.498133819)],
        [sfix(-35994663.64897003), sfix(206970912.81691143), sfix(-510533487.05663043), sfix(704845144.7542609), sfix(-596619160.2750701), sfix(316728744.95786095), sfix(-102954641.79992722), sfix(18743898.58874265), sfix(-1464755.3261213861)],
        [sfix(-207830416.67147234), sfix(433232185.49781895), sfix(-356271846.66582996), sfix(136972031.69714633), sfix(-16994251.074938808), sfix(-5194186.486475225), sfix(2270402.7808644464), sfix(-326391.7812510906), sfix(17165.55887348037)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)]
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
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-1.0499999523162842),
        sfix(-0.5249999761581421),
        sfix(0.0),
        sfix(0.13124999403953552),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-4968865.426692599), sfix(25318986.258335743), sfix(60245503.578963295), sfix(64737711.7057239), sfix(38700899.37475772), sfix(13578548.6323607), sfix(2788345.9661790296), sfix(310998.3784344368), sfix(14575.3795359704)],
        [sfix(-1412986.695293795), sfix(20708442.965706583), sfix(20491493.098391216), sfix(21684486.094893344), sfix(66888994.7933457), sfix(103995573.42745192), sfix(77436215.8903826), sfix(28319439.253622565), sfix(4145012.307846232)],
        [sfix(-1540365.0046984595), sfix(19302188.584378548), sfix(13979791.158491861), sfix(-2169092.563455897), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-1540365.0046984593), sfix(18993824.574305203), sfix(10437596.697344832), sfix(-12465290.144961748), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-1438353.3271718125), sfix(17099312.094569106), sfix(23339470.35474009), sfix(-53686894.3923506), sfix(64799070.00059588), sfix(-44315562.96680678), sfix(17347911.18576454), sfix(-3643501.1288648196), sfix(320848.4551587386)],
        [sfix(-1246930055.0489416), sfix(2862763458.869808), sfix(-2689963322.4258943), sfix(1358315700.8878226), sfix(-387920049.0346544), sfix(59292739.110337), sfix(-3356150.2904802677), sfix(-207757.80718365137), sfix(26488.16538196953)]
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)]
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
        sfix(-999.0),
        sfix(-999.0),
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
        sfix(-0.26249998807907104),
        sfix(-0.06562499701976776),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-25874156.305133317), sfix(-78732103.55005328), sfix(-95712334.46470273), sfix(-64362524.84561171), sfix(-26478596.864949755), sfix(-6849547.390303614), sfix(-1090555.5250011045), sfix(-97892.59018179525), sfix(-3798.91796106688)],
        [sfix(-49794.56506155338), sfix(-846681.1507594339), sfix(6286386.571011292), sfix(21215042.961195003), sfix(33051279.736863628), sfix(28182106.21245841), sfix(13321175.55392998), sfix(3282142.8443004917), sfix(329797.43746063375)],
        [sfix(-157329.4150518701), sfix(-2227512.586880361), sfix(-914418.9691694744), sfix(1316629.4598893905), sfix(1146155.5409489232), sfix(-2287197.0728919725), sfix(-4018160.374965608), sfix(-3269471.4265408507), sfix(-1938332.2815791098)],
        [sfix(-158215.8190039662), sfix(-2228677.019418484), sfix(-737580.6503278987), sfix(1061356.8534434976), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-1059230.466183221), sfix(4805239.826815294), sfix(-23207743.322671846), sfix(37444929.28451324), sfix(-28051813.77575526), sfix(4870825.382924028), sfix(4755602.660244736), sfix(-2563433.448825561), sfix(370390.5327275999)],
        [sfix(1082229678.7227378), sfix(-2643786911.5336885), sfix(2742231698.1947064), sfix(-1582521555.0631096), sfix(554771184.2873541), sfix(-120834787.64949918), sfix(15926496.292012611), sfix(-1155427.2078336622), sfix(34989.99909065851)]
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)]
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
        sfix(-999.0),
        sfix(-999.0),
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
        sfix(-1.0499999523162842),
        sfix(-0.5249999761581421),
        sfix(0.0),
        sfix(0.06562499701976776),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(18838338.604896262), sfix(87765987.54534428), sfix(153583223.4312075), sfix(141240757.68657857), sfix(75968786.38961174), sfix(24780127.079143345), sfix(4834115.421203735), sfix(519511.2975516608), sfix(23681.76018370232)],
        [sfix(-16020.19373426034), sfix(3981158.318796788), sfix(3596581.9622057527), sfix(6973031.048789296), sfix(18831954.367885504), sfix(20424192.636772312), sfix(9675692.57520627), sfix(1822751.423404842), sfix(54325.11184119684)],
        [sfix(-47078.82483322373), sfix(3562353.794246749), sfix(1056116.1540119168), sfix(-2082270.891145922), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-47078.82483322373), sfix(3564259.876987215), sfix(1143776.7033049506), sfix(-867500.183017536), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-48845.62187265972), sfix(3607357.2286185944), sfix(904646.5999447438), sfix(-1407307.3440798698), sfix(7438289.863231571), sfix(-14714136.848224886), sfix(11443730.928278195), sfix(-3919707.203558249), sfix(499488.7511936015)],
        [sfix(-390243037.18070084), sfix(984351502.5962856), sfix(-1049274924.1169101), sfix(620963302.4797708), sfix(-221916778.29630113), sfix(48954780.84137934), sfix(-6486715.587200748), sfix(468662.27982356615), sfix(-13938.27225219742)]
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)]
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
        sfix(-999.0),
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
        sfix(-1.0499999523162842),
        sfix(-0.5249999761581421),
        sfix(0.0),
        sfix(0.13124999403953552),
        sfix(1.0499999523162842)
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(28993308.35221363), sfix(166650404.6918321), sfix(305446384.7376223), sfix(287648650.93550664), sfix(157030193.8371839), sfix(51720916.67675425), sfix(10155829.172549367), sfix(1096370.8766514037), sfix(50139.1779346294)],
        [sfix(-2560388.36377953), sfix(15473749.072933473), sfix(13684023.527823156), sfix(7619979.197875599), sfix(36372318.41808991), sfix(58358266.44762654), sfix(39489070.79432725), sfix(12525273.447294867), sfix(1553950.1228189738)],
        [sfix(-2626809.181437953), sfix(14806764.840026237), sfix(11022057.792424217), sfix(-3324653.8283882686), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-2626809.181437953), sfix(14570316.560496863), sfix(8316334.029624472), sfix(-10390930.042614646), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-2629211.101081258), sfix(14630467.29311066), sfix(7714040.819880932), sfix(-7139447.642068724), sfix(-11512931.986109376), sfix(26673015.92514124), sfix(-18470200.048234154), sfix(4582964.181284852), sfix(-89743.68640917665)],
        [sfix(2568285.5793229905), sfix(3036763.6533192657), sfix(7029935.870733582), sfix(9745539.620204644), sfix(-14881021.37984581), sfix(8254018.594653652), sfix(-2293253.507960879), sfix(319129.5063299645), sfix(-17739.54702305641)]
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)]
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
        sfix(-0.5249999761581421),
        sfix(0.0),
        sfix(0.13124999403953552),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(2489959.652255439), sfix(29215526.11015122), sfix(54675117.18355825), sfix(52822265.262208596), sfix(30022594.63070571), sfix(10356838.559333343), sfix(2132404.4507552246), sfix(241122.23216016783), sfix(11525.68159864746)],
        [sfix(-864211.086957626), sfix(8269783.852570242), sfix(5046684.0592522845), sfix(-2092097.1175774778), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-864211.0869576259), sfix(8146590.002475744), sfix(3645243.393992231), sfix(-4960433.688206569), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-841592.1676139763), sfix(7716954.661487182), sfix(6710005.258717293), sfix(-15730475.805904325), sfix(19718929.69840226), sfix(-14254536.643310994), sfix(6018581.814971511), sfix(-1393527.8317641194), sfix(137925.58643747753)],
        [sfix(-636625024.195447), sfix(1472086325.1541796), sfix(-1403474191.2372458), sfix(723792672.279167), sfix(-214557516.44422174), sfix(35531351.88901158), sfix(-2697968.36813241), sfix(-5471.77317300594), sfix(9181.95808872061)]
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)]
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
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-1.5749999284744263),
        sfix(-1.0499999523162842),
        sfix(-0.26249998807907104),
        sfix(0.0),
        sfix(0.26249998807907104),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(8410886.462129876), sfix(20166812.33914153), sfix(19681000.917176813), sfix(10240480.364389349), sfix(3036023.944507856), sfix(491604.26638801105), sfix(32879.14410873702), sfix(-1018.17395931562), sfix(-189.91284405184)],
        [sfix(-349847.8219200162), sfix(-8389541.733494654), sfix(-33322949.823894173), sfix(-66402927.71136656), sfix(-77944776.0331387), sfix(-55502427.522444695), sfix(-23534907.57407656), sfix(-5476591.054383457), sfix(-539816.9989093188)],
        [sfix(699826.521837444), sfix(616735.3117061228), sfix(-306451.23372499796), sfix(1391197.6759755055), sfix(7440665.580207029), sfix(11990078.581667574), sfix(9064465.134337366), sfix(3268252.528422208), sfix(446947.32013037486)],
        [sfix(694470.3123257408), sfix(525276.9995839966), sfix(-970265.4734382496), sfix(-1382433.1862111932), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(694470.3123257408), sfix(530158.5942826973), sfix(-1105480.790634967), sfix(-616601.1468192182), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(686039.4134522954), sfix(669560.9890059247), sfix(-2036548.571405168), sfix(2949748.1336246035), sfix(-9756420.485123973), sfix(17659287.33388127), sfix(-14121957.664128404), sfix(5074738.841125128), sfix(-661144.5368356251)],
        [sfix(5614669.768669059), sfix(-32390931.459987897), sfix(96224830.87527756), sfix(-165864433.24092734), sfix(173046520.95581242), sfix(-109419940.46634293), sfix(40796994.43408272), sfix(-8239819.768671883), sfix(695419.5000290248)],
        [sfix(-595880769.7654903), sfix(1594172715.9027793), sfix(-1826763839.1271944), sfix(1173623972.6327941), sfix(-463242961.6341065), sfix(115265837.20096202), sfix(-17688350.542015262), sfix(1532941.2727204345), sfix(-57518.11930134553)]
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)]
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
        sfix(-0.26249998807907104),
        sfix(0.0),
        sfix(0.13124999403953552),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-20451807.629945237), sfix(-61069239.388237596), sfix(-61498480.07936142), sfix(-35047776.24432958), sfix(-12762260.9706036), sfix(-3025561.4257247415), sfix(-452009.0823459416), sfix(-38663.22966419409), sfix(-1444.4164794228)],
        [sfix(2860291.3924933206), sfix(-6413577.625030323), sfix(35566567.148989834), sfix(126092022.31677465), sfix(163455949.4178139), sfix(110224300.20882855), sfix(41193457.532901175), sfix(8101139.816167469), sfix(654596.4949915735)],
        [sfix(2136272.369208257), sfix(-15444836.769167962), sfix(-9765829.073920034), sfix(8415744.124025831), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(2136272.369208257), sfix(-15418750.313453993), sfix(-9154365.948252881), sfix(11649635.545199478), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(2050183.3904237319), sfix(-13810683.367798297), sfix(-20234238.350631326), sfix(47921084.84819499), sfix(-59514371.77943135), sfix(41975046.06067161), sfix(-17049288.27273336), sfix(3747853.4064972084), sfix(-348255.6464074874)],
        [sfix(990206863.0504174), sfix(-2209499231.9025416), sfix(1991813905.6682913), sfix(-940921464.6240101), sfix(236067163.89600894), sfix(-24807692.59254059), sfix(-1421835.9819903905), sfix(576980.2917910832), sfix(-38656.102472258)]
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)]
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
def neuron020(x):
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
        sfix(-0.26249998807907104),
        sfix(-0.03281249850988388),
        sfix(0.0),
        sfix(0.13124999403953552),
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
        [sfix(-197263071.51989478), sfix(-548252532.7057832), sfix(-650211631.9261552), sfix(-430001545.72183174), sfix(-174223109.66366205), sfix(-44448607.90537109), sfix(-6991422.683940389), sfix(-621048.516650975), sfix(-23886.8100337944)],
        [sfix(-1136837.2857207756), sfix(1269589.946302699), sfix(-115464428.15450993), sfix(-292198118.4102836), sfix(-282235913.4671057), sfix(-125732803.1018514), sfix(-21167890.694957074), sfix(1514169.370535941), sfix(656072.605723027)],
        [sfix(700120.0266969029), sfix(23581876.51029993), sfix(-8875923.428373318), sfix(-37828888.968558565), sfix(29184989.927397054), sfix(37104814.3529573), sfix(-16099659.938743586), sfix(28893976.645185545), sfix(63062317.367153846)],
        [sfix(700119.2875673283), sfix(23581629.656496122), sfix(-8912610.408903511), sfix(-39655696.31916907), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(700119.2875673281), sfix(23596687.588969942), sfix(-9587578.139543105), sfix(-29144054.321006455), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(699801.9059105265), sfix(23590975.487881504), sfix(-8995503.327161198), sfix(-37002985.730822094), sfix(23970771.892564043), sfix(48059939.66145004), sfix(-72957340.17617998), sfix(37036143.31411595), sfix(-6708168.201864104)],
        [sfix(-249599007.88383996), sfix(1477102052.2033992), sfix(-3649130436.3129616), sfix(5072678113.76908), sfix(-4337343617.470643), sfix(2332512210.6510644), sfix(-769591893.8527042), sfix(142373546.31695017), sfix(-11308260.317795116)],
        [sfix(8445359219.410764), sfix(-23382335537.121887), sfix(27426444247.12848), sfix(-17612204183.30209), sfix(6660922203.489675), sfix(-1470546094.9909012), sfix(170542782.05276477), sfix(-6674264.859844873), sfix(-230921.7291157478)],
        [sfix(45912529014.862434), sfix(-99066267977.0159), sfix(93111117721.10085), sfix(-49813084560.36714), sfix(16599517599.141073), sfix(-3529596735.972892), sfix(467812138.16811186), sfix(-35345443.908482514), sfix(1165805.1240560252)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)]
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
def neuron021(x):
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
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-2.0999999046325684),
        sfix(-0.5249999761581421),
        sfix(-0.26249998807907104),
        sfix(0.0),
        sfix(0.06562499701976776),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(60538295.496804625), sfix(179037388.25986195), sfix(225550646.0243661), sfix(155680984.0796159), sfix(65008900.492384285), sfix(16956697.817253664), sfix(2712686.773606304), sfix(244213.2452225726), sfix(9495.40248096677)],
        [sfix(6106508.621626064), sfix(16353885.181270063), sfix(146836767.73171082), sfix(395124567.24828166), sfix(490205355.84646267), sfix(332465829.9495052), sfix(128342681.44211575), sfix(26646738.91681278), sfix(2321302.1495083943)],
        [sfix(1694385.6025516207), sfix(-24329627.978313204), sfix(-13531771.597202595), sfix(43109131.86983382), sfix(21971797.127046585), sfix(-50148101.65218874), sfix(-55268622.85757193), sfix(-18264624.62740817), sfix(-1273304.2079627714)],
        [sfix(1694443.2816804969), sfix(-24459560.56792596), sfix(-16606777.380055664), sfix(24975099.766439684), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(1694443.2816804969), sfix(-24326319.43184525), sfix(-13590322.751927057), sfix(46214981.14545118), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(1694395.2577711218), sfix(-24324763.8306807), sfix(-13547478.95845516), sfix(44178621.85056985), sfix(19782256.483961638), sfix(-19474020.06552548), sfix(-84661746.07021628), sfix(98962468.46297053), sfix(-30787548.47742655)],
        [sfix(-16323794.996278824), sfix(131434139.3074092), sfix(-580035169.5506794), sfix(1162165591.180054), sfix(-1253360306.040371), sfix(774028985.9665449), sfix(-273365591.40867954), sfix(51163267.17273992), sfix(-3916042.541148821)],
        [sfix(6225361818.484506), sfix(-16626369792.850426), sfix(19027923072.363026), sfix(-12213041920.36047), sfix(4815207342.055492), sfix(-1196473601.1040328), sfix(183300314.13987458), sfix(-15854687.198526097), sfix(593591.6618716322)]
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)]
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
def neuron022(x):
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
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-3.1499998569488525),
        sfix(-2.0999999046325684),
        sfix(-1.0499999523162842),
        sfix(-0.13124999403953552),
        sfix(-0.06562499701976776),
        sfix(0.26249998807907104),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(64711114.87264885), sfix(134844665.91403052), sfix(123513825.00285403), sfix(64658294.56109546), sfix(21139008.23725057), sfix(4419466.546513164), sfix(577056.4413483858), sfix(43027.69198857614), sfix(1402.81101654519)],
        [sfix(-100438398.12658188), sfix(-239692031.21082303), sfix(-215003925.532363), sfix(-81022509.69031821), sfix(-222144.74308912817), sfix(10828109.876889003), sfix(3934922.9462227384), sfix(607215.6930272782), sfix(36209.3440146553)],
        [sfix(-116288676.64768885), sfix(-640079852.1926147), sfix(-1443687704.0856314), sfix(-1787293699.6168146), sfix(-1339275134.6620262), sfix(-625275590.6497175), sfix(-178406424.65483996), sfix(-28549592.488484487), sfix(-1967913.4403749553)],
        [sfix(-625946.8456969338), sfix(-8573772.227598673), sfix(4555715.233474532), sfix(1061521.804721755), sfix(-76544886.59674667), sfix(-124031454.19011821), sfix(-67513436.27218689), sfix(-7161576.9495529225), sfix(2996712.785980736)],
        [sfix(-611749.0528891265), sfix(-8216949.534337753), sfix(8169419.737454101), sfix(20241687.610109735), sfix(-18533547.81762298), sfix(-23838509.82607315), sfix(20821104.94475619), sfix(12586063.364348046), sfix(-13533120.037359659)],
        [sfix(-613017.0534063778), sfix(-8147867.76546871), sfix(8820360.911032999), sfix(10741464.505925417), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-2547287.761361884), sfix(16571662.74773771), sfix(-120480204.90828964), sfix(372546863.45571834), sfix(-573245616.4436505), sfix(483444135.0849205), sfix(-228599100.36590448), sfix(57046139.94165336), sfix(-5860468.811939488)],
        [sfix(1482306770.7234044), sfix(-2914093261.712362), sfix(2122082173.7055717), sfix(-569927982.7194118), sfix(-93218669.14316015), sfix(103522527.08569196), sfix(-28362727.21438883), sfix(3549190.6383997733), sfix(-174359.60122426468)]
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)]
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
def neuron023(x):
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
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-2.0999999046325684),
        sfix(-0.5249999761581421),
        sfix(-0.26249998807907104),
        sfix(0.13124999403953552),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-4198132.459478944), sfix(-13715689.470766682), sfix(-16084114.03481897), sfix(-10502584.062078707), sfix(-4251600.415247585), sfix(-1091216.418373602), sfix(-173113.87154757328), sfix(-15514.62771311452), sfix(-601.65624630956)],
        [sfix(1713487.7824727057), sfix(7492684.802377684), sfix(40609043.881856225), sfix(93629930.1646637), sfix(111364923.90453404), sfix(75524508.40088886), sfix(29672860.21898754), sfix(6315253.904809636), sfix(565130.9584176382)],
        [sfix(564190.5636743825), sfix(-3040464.3039218076), sfix(-396906.91519049706), sfix(5729509.302837562), sfix(-442630.73898065125), sfix(-8112810.868741383), sfix(-3178249.0478997463), sfix(2326894.963408245), sfix(1322088.7415420797)],
        [sfix(563929.6098662133), sfix(-3031646.145214634), sfix(-397540.52492767095), sfix(5208750.775339626), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(564171.8935692557), sfix(-3039439.3746866616), sfix(-411166.72331317613), sfix(5918259.090797209), sfix(-1378549.5236860914), sfix(-3266808.2883469807), sfix(-12757215.225830996), sfix(19838650.091821745), sfix(-7311780.439490432)],
        [sfix(-4018087.9145124936), sfix(39874272.88098266), sfix(-170984111.18718258), sfix(378575387.0483435), sfix(-483018213.1098309), sfix(360883372.4719148), sfix(-155559696.30993068), sfix(35831159.94107271), sfix(-3418099.8404598203)],
        [sfix(-187035149.6432783), sfix(149475638.89867485), sfix(217569621.4991371), sfix(-387673904.1401366), sfix(250071116.73060519), sfix(-86273137.08040011), sfix(16921261.084328383), sfix(-1784913.6116958065), sfix(78888.65743014206)]
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)]
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
def neuron024(x):
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
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-1.0499999523162842),
        sfix(-0.13124999403953552),
        sfix(0.0),
        sfix(0.13124999403953552),
        sfix(0.5249999761581421),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(27248048.12119161), sfix(106520891.21954714), sfix(170375352.36637402), sfix(148255310.42615885), sfix(76916633.18100744), sfix(24477345.265290167), sfix(4691510.609698935), sfix(497629.5775012779), sfix(22458.325656323)],
        [sfix(269370.3954338751), sfix(-1558477.0210061583), sfix(-2568247.940332935), sfix(6195169.1038223095), sfix(5500241.583402844), sfix(-11683227.922038704), sfix(-18276217.31470449), sfix(-9096121.949522141), sfix(-1568881.0075140372)],
        [sfix(269685.7988960005), sfix(-1553994.8334184275), sfix(-2657434.560432046), sfix(4510475.204841664), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(269685.7988960005), sfix(-1547957.738556076), sfix(-2595286.3636168297), sfix(8329884.530060824), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(269653.3462758512), sfix(-1549001.7557928765), sfix(-2501715.495293631), sfix(6940737.286820133), sfix(6190354.597850435), sfix(-1102077.746697689), sfix(-21415974.85078692), sfix(21402208.68024286), sfix(-6271614.813173718)],
        [sfix(420508.3199968094), sfix(-3567323.392278973), sfix(9304835.589451902), sfix(-32505140.629009053), sfix(88530212.59736744), sfix(-111085195.16345543), sfix(70406254.65663655), sfix(-22419657.40148213), sfix(2885530.042263262)],
        [sfix(-37507500.06466515), sfix(226198503.25526235), sfix(-600677277.4276396), sfix(896147985.3237898), sfix(-800302519.1121114), sfix(438102893.5684349), sfix(-144195351.9085836), sfix(26233889.383482523), sfix(-2030723.2138921632)],
        [sfix(402839410.2970585), sfix(-1025134183.7178944), sfix(1124437675.5622363), sfix(-690926076.9123889), sfix(261414326.17337373), sfix(-62456739.35977276), sfix(9214136.30263726), sfix(-768326.3642829291), sfix(27753.31685861881)]
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)]
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
def neuron025(x):
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
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-2.0999999046325684),
        sfix(-0.5249999761581421),
        sfix(-0.06562499701976776),
        sfix(0.26249998807907104),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-8071709.873283379), sfix(-49980995.1987235), sfix(-76796695.34928635), sfix(-58998092.38000241), sfix(-26491212.576887593), sfix(-7285974.87281173), sfix(-1213061.6480034867), sfix(-112607.4140170608), sfix(-4484.31960501008)],
        [sfix(21769173.15605841), sfix(195682901.34351847), sfix(909479727.4171957), sfix(1842575269.9950087), sfix(1984814097.257664), sfix(1241955450.9584382), sfix(456191894.8252273), sfix(91694066.64633644), sfix(7812497.325016007)],
        [sfix(-4756577.007989211), sfix(-39693508.02197681), sfix(30954202.565822177), sfix(68722764.6898179), sfix(-62572944.44178552), sfix(-13807763.837196695), sfix(216053598.3783477), sfix(222869111.00902647), sfix(66484946.500330955)],
        [sfix(-4761114.843749462), sfix(-39457313.70714402), sfix(33027363.930888146), sfix(33403338.294336442), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-7608890.455239464), sfix(-2467067.495851505), sfix(-167805798.26776943), sfix(633273795.831816), sfix(-1018118221.4713731), sfix(872884598.5492629), sfix(-417265003.1462896), sfix(105140847.08660947), sfix(-10901636.347572058)],
        [sfix(-9974158064.894707), sfix(26561607006.116123), sfix(-29535933871.5921), sfix(17505403346.384617), sfix(-5776494719.404054), sfix(950031600.7648559), sfix(-25616596.60871533), sfix(-13735614.182342993), sfix(1402578.1109548076)],
        [sfix(-51852558579.65594), sfix(111458195910.55789), sfix(-104416776888.14415), sfix(55703140143.01354), sfix(-18516371020.846794), sfix(3928626654.668255), sfix(-519700353.4057625), sfix(39198985.83424021), sfix(-1290944.8197846056)]
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)]
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
def neuron026(x):
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
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-2.0999999046325684),
        sfix(-0.26249998807907104),
        sfix(0.0),
        sfix(0.26249998807907104),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(65437231.56069282), sfix(178114090.8573173), sfix(209023251.91539437), sfix(137157194.01515055), sfix(55212434.90644739), sfix(14008714.358493656), sfix(2193151.9622303164), sfix(194038.53398751697), sfix(7437.48717915853)],
        [sfix(223025.2596122473), sfix(-5437244.570538084), sfix(-8072647.495719872), sfix(-14642568.67274176), sfix(-28977910.185705557), sfix(-30355394.48501147), sfix(-16210755.348453678), sfix(-4299971.711073842), sfix(-453078.57028858445)],
        [sfix(300857.2375347708), sfix(-4405398.6421925295), sfix(-2452757.738474652), sfix(1883279.9690061372), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(300857.2375347708), sfix(-4402978.2385621965), sfix(-2468812.9859274365), sfix(2124049.4199531935), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(779875.2528381833), sfix(-10454799.821836768), sfix(28330877.95789365), sfix(-79747987.84195353), sfix(122832999.19547871), sfix(-104566846.65383029), sfix(49957256.79402089), sfix(-12555473.306873899), sfix(1291029.3486086153)],
        [sfix(2203507129.814644), sfix(-5463164611.9549055), sfix(5758542167.657406), sfix(-3376203509.196427), sfix(1204121469.1900535), sfix(-267467008.51569542), sfix(36092793.77921627), sfix(-2697960.339889001), sfix(85099.47698873324)]
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)]
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
def neuron027(x):
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
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-1.0499999523162842),
        sfix(-0.26249998807907104),
        sfix(-0.13124999403953552),
        sfix(0.26249998807907104),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(51798648.238671705), sfix(253290953.70714688), sfix(443405116.32568777), sfix(401912491.1283938), sfix(212568635.7780433), sfix(68272047.56523554), sfix(13141937.012446092), sfix(1396491.8670462163), sfix(63056.98906036643)],
        [sfix(6973693.839879429), sfix(33544263.058107194), sfix(-822652.7576133392), sfix(-63402101.6164306), sfix(-33444417.204239283), sfix(38125408.737989254), sfix(49299098.39625144), sfix(20916660.092697386), sfix(3284694.5784829874)],
        [sfix(6988478.8890102105), sfix(33837036.10888163), sfix(2068014.7889233835), sfix(-43422290.90518455), sfix(71770063.36051515), sfix(439650436.2927932), sfix(1060419619.359551), sfix(1499217354.185573), sfix(948451660.1663411)],
        [sfix(6987905.121590487), sfix(33786477.91161446), sfix(386311.0422009238), sfix(-57389934.4003557), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(6750556.696263054), sfix(37831215.35145286), sfix(-28819252.150892194), sfix(62388351.83955983), sfix(-311335259.1181604), sfix(478735514.11467147), sfix(-321075855.2676601), sfix(97246067.55709203), sfix(-10184357.523653068)],
        [sfix(57121753.12131484), sfix(-333482475.561572), sfix(1173678461.9929101), sfix(-2161534487.724222), sfix(2240981309.768116), sfix(-1365553590.9338717), sfix(486879720.59602726), sfix(-94209536.0284071), sfix(7655829.383914542)],
        [sfix(-4415653825.002539), sfix(11633107217.537113), sfix(-13127235243.756945), sfix(8309015038.1470585), sfix(-3230261138.6147), sfix(791347773.6597952), sfix(-119510362.21480979), sfix(10188458.004414367), sfix(-375901.5466961688)]
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)]
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
def neuron028(x):
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
        sfix(-0.26249998807907104),
        sfix(0.0),
        sfix(0.03281249850988388),
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
        [sfix(-142181146.24767694), sfix(-438879792.31199837), sfix(-546246282.7870945), sfix(-373238823.412467), sfix(-155054498.74868542), sfix(-40348647.62385198), sfix(-6447827.787942149), sfix(-580129.1627148695), sfix(-22546.37091999992)],
        [sfix(-382671816.02338725), sfix(-2102074695.6663613), sfix(-4439609160.750171), sfix(-5041679193.211856), sfix(-3444949896.094855), sfix(-1465347728.6408775), sfix(-380874222.70720077), sfix(-55441727.723789394), sfix(-3462428.5519968634)],
        [sfix(981349.4726548702), sfix(-76132330.04106021), sfix(-57793957.267184354), sfix(-234884690.00886154), sfix(-955494409.0757542), sfix(-1383051280.7155316), sfix(-925480598.0433903), sfix(-289276760.54612535), sfix(-32579695.901026886)],
        [sfix(1680474.754918608), sfix(-64068054.80214913), sfix(31694766.190315936), sfix(140517341.94808492), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(1680474.754918608), sfix(-64125351.39172708), sfix(29905193.10013971), sfix(112051350.68309368), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(1680734.302638296), sfix(-64140474.35142513), sfix(30104379.42484877), sfix(115404345.32305832), sfix(-77507395.23044112), sfix(-176562534.85574266), sfix(265661342.4805776), sfix(-132506625.05839749), sfix(23150396.23337685)],
        [sfix(968362343.3959775), sfix(-5661413443.396121), sfix(13993810477.00984), sfix(-19385502651.86546), sfix(16455795621.844732), sfix(-8763465804.936712), sfix(2859646101.9685903), sfix(-523026708.5103258), sfix(41081885.9220625)],
        [sfix(-23001408446.256428), sfix(62850824229.760284), sfix(-72413047126.07266), sfix(45328608170.75935), sfix(-16469526380.456911), sfix(3376963539.847438), sfix(-324288360.3757995), sfix(944431.3297347988), sfix(1530034.101037455)],
        [sfix(-126111332231.69455), sfix(271999501513.58688), sfix(-255553683555.52563), sfix(136674957911.29753), sfix(-45532637530.51687), sfix(9679396927.899546), sfix(-1282633030.8815799), sfix(96890722.80155267), sfix(-3195223.163938846)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)]
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
        sfix(-2.0999999046325684),
        sfix(-1.0499999523162842),
        sfix(-0.26249998807907104),
        sfix(0.0),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-38961136613.99664), sfix(-73945156483.54793), sfix(-61385583260.54895), sfix(-29113042862.725876), sfix(-8627556460.937305), sfix(-1635918097.0312688), sfix(-193821863.27984768), sfix(-13118579.821656551), sfix(-388349.64253032114)],
        [sfix(-2231679737.2595696), sfix(-20648771450.37954), sfix(-36563779050.08971), sfix(-30047363090.21477), sfix(-13979736771.290817), sfix(-3925814228.08642), sfix(-662663623.4247319), sfix(-62154980.330212526), sfix(-2497439.609298734)],
        [sfix(15362538665.704348), sfix(43982265470.51771), sfix(53805645444.81956), sfix(36564791486.24278), sfix(14989935352.609768), sfix(3755172465.839947), sfix(550920158.1483166), sfix(41617177.40406114), sfix(1112635.2937982962)],
        [sfix(-250132041.95556077), sfix(-1680757194.5287638), sfix(-4376092154.967242), sfix(-6152379989.400944), sfix(-5244970354.051183), sfix(-2800635305.525077), sfix(-917689034.1197654), sfix(-168940721.58497787), sfix(-13385761.97173454)],
        [sfix(24393785.835668296), sfix(-30179956.247519996), sfix(-55285253.14062918), sfix(256377309.02879375), sfix(598583544.3484496), sfix(494820891.73930526), sfix(159215077.54233912), sfix(-4111474.35545219), sfix(-9555644.677799474)],
        [sfix(24043926.276740663), sfix(-36804225.8028186), sfix(-114051661.51506536), sfix(-16621801.130241439), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(24043926.276740663), sfix(-35829675.94847893), sfix(-107982303.67984135), sfix(150066848.56403515), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(24043129.89099116), sfix(-36148983.66664244), sfix(-99463527.2472847), sfix(87280565.26938912), sfix(148077674.64239758), sfix(58376306.99486378), sfix(-565463790.7699028), sfix(535970005.73075545), sfix(-158768395.7145148)],
        [sfix(-29560292.962437477), sfix(442995530.75370526), sfix(-1900340076.7144682), sfix(3744389787.9090157), sfix(-4082735551.222488), sfix(2628194730.3104005), sfix(-998081941.9717542), sfix(207467605.43410617), sfix(-18254485.833369125)],
        [sfix(2029727646.799883), sfix(-4555478698.182427), sfix(4203072233.9676194), sfix(-2048726768.54762), sfix(553115828.9225976), sfix(-74563030.33772494), sfix(1849964.1232762635), sfix(663241.726623351), sfix(-55481.78962293138)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)]
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
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-2.0999999046325684),
        sfix(-0.5249999761581421),
        sfix(0.06562499701976776),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-98397935.7956982), sfix(-217336076.41139686), sfix(-212187186.715859), sfix(-116321510.81760903), sfix(-38976575.22836111), sfix(-8164993.689457351), sfix(-1042338.3087854758), sfix(-73853.26336050373), sfix(-2207.91662005269)],
        [sfix(3734488.6770674353), sfix(40247158.692388624), sfix(139606424.47227463), sfix(247403755.27767512), sfix(235709028.71277303), sfix(126021668.91859049), sfix(37441553.22235597), sfix(5619600.149339084), sfix(312086.77996889147)],
        [sfix(-469009.7497820385), sfix(4359266.174777249), sfix(12830357.466726402), sfix(13065959.94228807), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-464009.61718585313), sfix(4385694.154274659), sfix(11901025.281712282), sfix(4629325.122930255), sfix(-17986182.489396513), sfix(-14245315.92753253), sfix(41257855.21213204), sfix(-27315865.838812903), sfix(6195035.235322691)],
        [sfix(-952638.9593904272), sfix(9116436.673529433), sfix(-8760913.187569782), sfix(58636266.231873676), sfix(-111191322.03084983), sfix(94226624.76338261), sfix(-40806179.03375139), sfix(8886430.139436057), sfix(-775309.732292037)],
        [sfix(516512291.68259954), sfix(-1304906765.4310577), sfix(1428710773.151961), sfix(-875782859.7963091), sfix(331945700.3679113), sfix(-79792516.92263232), sfix(11892563.401843641), sfix(-1005705.46348154), sfix(36971.6673644532)]
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)]
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
        sfix(-999.0),
        sfix(-999.0),
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
        sfix(-1.5749999284744263),
        sfix(-1.0499999523162842),
        sfix(-0.26249998807907104),
        sfix(0.0),
        sfix(0.26249998807907104),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-11990071825.802076), sfix(-26226691012.446854), sfix(-24933706162.237034), sfix(-13470737122.790068), sfix(-4527092823.814018), sfix(-969713413.4832443), sfix(-129355275.18820444), sfix(-9828900.390693272), sfix(-325816.08200730686)],
        [sfix(639243252.3422064), sfix(2507987470.0202503), sfix(4103159465.197403), sfix(3708657826.264532), sfix(2048679788.6344655), sfix(712712405.436995), sfix(152931844.29923108), sfix(18527384.73952752), sfix(970689.2895838261)],
        [sfix(6796172.991383772), sfix(-55183050.24671126), sfix(-268753383.6057739), sfix(-285951291.78231186), sfix(34932099.974854276), sfix(246289876.57267633), sfix(174369305.45091614), sfix(52333101.04582993), sfix(5996541.822544627)],
        [sfix(18191731.145092506), sfix(21523641.15221135), sfix(-48966385.14964614), sfix(53065600.77522348), sfix(319368458.490392), sfix(342787072.3496114), sfix(142381937.2572425), sfix(14467707.839148654), sfix(-3279626.610836609)],
        [sfix(18010487.34135113), sfix(18177791.809559774), sfix(-77526218.03045478), sfix(-79914048.53005692), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(18010487.34135113), sfix(18752560.72859093), sfix(-79851347.19711229), sfix(15496737.261477629), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(18051920.16177733), sfix(17704901.766608473), sfix(-66508876.78640221), sfix(-57910585.23684887), sfix(145201250.70068413), sfix(-18358149.4833631), sfix(-90187303.21192667), sfix(60756351.313948914), sfix(-12169829.910640286)],
        [sfix(-214166754.83873764), sfix(1350161536.5199742), sfix(-3345465498.1924047), sfix(4420954280.905122), sfix(-3506166478.5656934), sfix(1735541487.396616), sfix(-528436104.89063334), sfix(90945917.05829665), sfix(-6789614.999982405)],
        [sfix(-3873492508.167231), sfix(9414787493.320505), sfix(-9738847510.346382), sfix(5581516135.122819), sfix(-1934141916.451742), sfix(413442486.0057263), sfix(-52896200.71501998), sfix(3659103.242408108), sfix(-102269.48618758399)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)]
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
        sfix(-999.0),
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
        sfix(-0.5249999761581421),
        sfix(0.0),
        sfix(1.0499999523162842)
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-597288637.9797859), sfix(-1594305050.7337406), sfix(-1810225963.434137), sfix(-1151322042.5054293), sfix(-450607120.0477101), sfix(-111446618.52220356), sfix(-17043561.166984737), sfix(-1475652.5424046016), sfix(-55439.90079578426)],
        [sfix(-65918445.11488931), sfix(-369051803.53579915), sfix(-889681473.2057431), sfix(-1171330450.2842922), sfix(-908984045.3693517), sfix(-427680174.4217424), sfix(-120231933.41789456), sfix(-18624428.3867196), sfix(-1225512.5270510935)],
        [sfix(-260170.50342063265), sfix(-776193.9643060898), sfix(-13288696.899095485), sfix(-35351474.568943), sfix(-62875841.59849312), sfix(-91099222.63470635), sfix(-77581415.14523652), sfix(-32849604.252886973), sfix(-5424644.277264672)],
        [sfix(-132156.98955029433), sfix(837738.6669376828), sfix(-4533447.229561677), sfix(-6798017.299334326), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-132156.9895502944), sfix(1040598.9949270564), sfix(-4618127.620156279), sfix(1814406.1749078687), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(1939961.1820241492), sfix(-6891814.414385842), sfix(6752850.820599686), sfix(-5956027.4579124395), sfix(3069204.169115188), sfix(-969067.6357162659), sfix(185221.63261950863), sfix(-19692.14061169578), sfix(893.98685601077)]
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)]
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
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-1.0499999523162842),
        sfix(-0.26249998807907104),
        sfix(0.0),
        sfix(0.26249998807907104),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(17054676.62796086), sfix(67610088.31459692), sfix(107898413.17685625), sfix(93466213.88218431), sfix(48322388.006449275), sfix(15346484.236971151), sfix(2938936.462592119), sfix(311731.7777763526), sfix(14076.32106114979)],
        [sfix(775951.7143043082), sfix(-123195.75497543249), sfix(-3584593.99915448), sfix(3551933.876407122), sfix(12017891.497615628), sfix(5072343.505824802), sfix(-4356336.554806535), sfix(-4047871.960938789), sfix(-906842.8291755603)],
        [sfix(771500.4436924359), sfix(-221132.5960202535), sfix(-4667280.508773078), sfix(-2141844.446224071), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(771500.4436924359), sfix(-181332.2952045157), sfix(-4585227.331685499), sfix(4481290.927420719), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(789383.0438870777), sfix(-506433.154364302), sfix(-1898394.7214756978), sfix(-7642007.50470691), sfix(28819695.221760396), sfix(-32819695.49085674), sfix(18706786.526141163), sfix(-5408936.900619042), sfix(593809.8783357155)],
        [sfix(36405719.34498115), sfix(-204834339.46770608), sfix(501828864.11555195), sfix(-700725660.6032557), sfix(606194955.2683529), sfix(-327504075.1488796), sfix(107216011.06918736), sfix(-19448422.418331888), sfix(1501295.62134053)],
        [sfix(-193227371.89019495), sfix(416521866.2332466), sfix(-365198968.6170637), sfix(169133162.90610793), sfix(-42909688.09639266), sfix(5196938.589931511), sfix(-17639.79017115147), sfix(-61492.88603055342), sfix(4524.68791651162)]
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)]
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
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-2.0999999046325684),
        sfix(-1.0499999523162842),
        sfix(-0.5249999761581421),
        sfix(-0.13124999403953552),
        sfix(0.0),
        sfix(0.26249998807907104),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-386354372.4332908), sfix(-944798927.360838), sfix(-1003790923.0629815), sfix(-582548491.0002393), sfix(-197571919.22266316), sfix(-39043092.50381911), sfix(-4141716.83885238), sfix(-175871.75760686523), sfix(999.01816382311)],
        [sfix(-1138423650.9349837), sfix(-6447963377.25876), sfix(-15596524050.548668), sfix(-20794555712.25993), sfix(-16765443468.835957), sfix(-8408091803.841933), sfix(-2572422790.531145), sfix(-440593709.54876786), sfix(-32446172.468009554)],
        [sfix(1011312.0621538338), sfix(-33765280.40043609), sfix(-253305306.7832226), sfix(-744077325.109317), sfix(-1608842982.930025), sfix(-2163967463.2482595), sfix(-1624034507.6373258), sfix(-627026711.4288642), sfix(-97716088.0930837)],
        [sfix(4020234.660164991), sfix(6345743.833779093), sfix(-19363261.74652073), sfix(35627462.399955146), sfix(15396772.181342637), sfix(1605408.7752264554), sfix(180673625.58077195), sfix(232480950.97356674), sfix(81403191.14728636)],
        [sfix(4019912.7242940967), sfix(6325474.0225165365), sfix(-19916771.051669642), sfix(30108669.474470243), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(4019912.724294096), sfix(6269307.068145068), sfix(-18162170.9766362), sfix(26205143.544235498), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(4864798.143425638), sfix(-4176991.87178697), sfix(32446942.72357916), sfix(-98355113.95057379), sfix(182677177.68880358), sfix(-190034364.95348385), sfix(107140983.35892), sfix(-30588277.853847917), sfix(3470857.552434264)],
        [sfix(1707616587.7526743), sfix(-4430313672.189999), sfix(4953021582.0166025), sfix(-3115790614.602198), sfix(1211065592.2481837), sfix(-298290221.0652917), sfix(45516737.5406709), sfix(-3937489.6486718347), sfix(147942.80134855217)]
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)]
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
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-2.0999999046325684),
        sfix(-0.5249999761581421),
        sfix(-0.26249998807907104),
        sfix(0.0),
        sfix(0.26249998807907104),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-799224095.1491518), sfix(-2385849652.695604), sfix(-3029831438.6743283), sfix(-2134132375.0676043), sfix(-914483512.0254987), sfix(-244952341.9499509), sfix(-40180486.69053631), sfix(-3700217.82939404), sfix(-146791.80503227646)],
        [sfix(-4145731.7706108787), sfix(-87028821.00875822), sfix(-397106867.5455904), sfix(-742057014.4348395), sfix(-739417292.4063773), sfix(-429246167.9733216), sfix(-146633629.6914896), sfix(-27526211.576929484), sfix(-2205099.1339623607)],
        [sfix(7328011.547050062), sfix(13550471.008765638), sfix(-28475463.202671733), sfix(-20031861.916930042), sfix(44844642.2291557), sfix(-25102081.628801294), sfix(-160716781.3597471), sfix(-142157650.27346388), sfix(-40412516.26332619)],
        [sfix(7328231.106822134), sfix(13436904.96647258), sfix(-31421126.220222894), sfix(-40812159.9001011), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(7328231.106822135), sfix(13726973.254186232), sfix(-32431983.05193048), sfix(8804496.092040405), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(7487690.562475349), sfix(10822357.767454479), sfix(-8394743.86520576), sfix(-98619614.04349075), sfix(247260079.91895962), sfix(-262777622.0683003), sfix(141241096.32421458), sfix(-34853161.12543019), sfix(2402017.3073382145)],
        [sfix(55605515.38777194), sfix(-234568746.00907862), sfix(491400525.548393), sfix(-582929495.4498365), sfix(410532466.7517973), sfix(-171860042.12534475), sfix(41210671.02354182), sfix(-5047555.448737715), sfix(225027.77786535112)],
        [sfix(526361970.62965554), sfix(-1413459560.4236052), sfix(1628992935.932037), sfix(-1050859020.083466), sfix(417589843.1470223), sfix(-104893187.63475554), sfix(16289057.964860203), sfix(-1431470.4315542304), sfix(54553.27731705801)]
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)]
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
        sfix(-999.0),
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
        sfix(-1.0499999523162842),
        sfix(-0.26249998807907104),
        sfix(0.0),
        sfix(0.26249998807907104),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-23287379.288030587), sfix(-90068378.15187152), sfix(-149546284.61420193), sfix(-133045843.69162096), sfix(-69826104.68249063), sfix(-22359152.166261714), sfix(-4300586.6162868105), sfix(-457100.8158708842), sfix(-20654.10562882503)],
        [sfix(1020581.4184362832), sfix(3823533.2157729), sfix(1567660.0491114361), sfix(13730995.177887803), sfix(51665126.37180015), sfix(74129494.02201764), sfix(51241156.70268714), sfix(16936522.700690255), sfix(2080672.6806311929)],
        [sfix(983281.7245928934), sfix(3177210.2090883213), sfix(-3269683.6902953777), sfix(-6682504.978984705), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(983281.7245928933), sfix(3208288.9143632487), sfix(-3711383.439660001), sfix(-1430848.1080292428), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(973386.2773933763), sfix(3353208.35817579), sfix(-4355369.912300168), sfix(-29264.06669269055), sfix(-7248289.351113833), sfix(26952460.43110334), sfix(-28581273.69059489), sfix(12790037.121015087), sfix(-2114802.6239055404)],
        [sfix(-53474250.990346834), sfix(314647528.52122855), sfix(-767229029.790133), sfix(1037909597.1143538), sfix(-852388266.122671), sfix(436928946.49934083), sfix(-136836380.05780572), sfix(23987641.85868918), sfix(-1805911.8473142225)],
        [sfix(229030848.87879553), sfix(-608894497.5995998), sfix(697714512.2540075), sfix(-447718060.3870876), sfix(177194569.29917082), sfix(-44366359.90665442), sfix(6871635.922595396), sfix(-602535.8293049791), sfix(22918.65610295949)]
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)]
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
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
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
        sfix(-1.0499999523162842),
        sfix(-0.26249998807907104),
        sfix(0.13124999403953552),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-164758622.90707013), sfix(-580986552.2442112), sfix(-898847248.8496387), sfix(-770851907.831874), sfix(-396483734.2212288), sfix(-125144880.49031273), sfix(-23749873.206811685), sfix(-2488722.341801777), sfix(-110731.28808000534)],
        [sfix(-4351531.089876922), sfix(26023810.225344606), sfix(42745062.28135768), sfix(123327341.12785302), sfix(409212716.2381049), sfix(610043747.7421154), sfix(437799331.0781254), sfix(149521532.91660708), sfix(19060578.974862657)],
        [sfix(-4667386.6678992305), sfix(20667626.55276104), sfix(3834748.054184354), sfix(-37248425.840982065), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-4665814.2418803), sfix(20633248.51059444), sfix(3289798.957106639), sfix(-34714842.21794068), sfix(16024297.838484352), sfix(59657265.537195735), sfix(-102338715.22251469), sfix(66514398.34230239), sfix(-16419821.209379192)],
        [sfix(-4754983.695678821), sfix(22529369.130695358), sfix(-5907931.637074444), sfix(-20844051.304997947), sfix(30268819.52424277), sfix(-15982816.385441469), sfix(1910192.5875354428), sfix(1038751.3863272168), sfix(-260885.2989146298)],
        [sfix(-2096926292.8092873), sfix(5835074487.585524), sfix(-6922187023.792589), sfix(4597111703.307596), sfix(-1872434108.5007763), sfix(480148325.032121), sfix(-75854576.7514925), sfix(6761442.62394558), sfix(-260715.36102862493)]
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)]
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
    "neuron020": neuron020,
    "neuron021": neuron021,
    "neuron022": neuron022,
    "neuron023": neuron023,
    "neuron024": neuron024,
    "neuron025": neuron025,
    "neuron026": neuron026,
    "neuron027": neuron027,
    "neuron028": neuron028,
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

def func5_kan_model_evaluate(x):
    # dim_list required
    input_x = x
    dim_list = [(3, 9), (9, 1)]
    for l in range(len(dim_list)):
        in_dim, out_dim = dim_list[l]
        partial_result = [0]*out_dim
        for i in range(in_dim):
            for j in range(out_dim):
                partial_result[j] += neuron_func_dict[f"neuron{l}{i}{j}"](input_x[i])
        input_x = partial_result
    return input_x

def func5_kan_model_evaluate_vectorized(x):
    dim_list = [(3, 9), (9, 1)]
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