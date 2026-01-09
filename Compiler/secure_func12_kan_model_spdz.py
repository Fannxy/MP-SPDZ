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
        sfix(-2.5999999046325684),
        sfix(-2.125),
        sfix(-1.8874999284744263),
        sfix(-1.6499998569488525),
        sfix(-1.4124999046325684),
        sfix(-1.1749999523162842),
        sfix(-0.9374999403953552),
        sfix(-0.8187499046325684),
        sfix(-0.6999999284744263),
        sfix(-0.4624999165534973),
        sfix(-0.22499993443489075),
        sfix(-0.046874936670064926),
        sfix(0.012500062584877014),
        sfix(0.2500000596046448),
        sfix(0.48750004172325134),
        sfix(0.7250000238418579),
        sfix(0.9625000357627869),
        sfix(1.2000000476837158),
        sfix(1.318750023841858),
        sfix(1.4375),
        sfix(1.5562500953674316),
        sfix(1.9125001430511475),
        sfix(2.1500000953674316),
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
        [sfix(9287678.442799352), sfix(22685762.846196316), sfix(23732009.638629265), sfix(13225042.412893955), sfix(4129365.067462305), sfix(685640.6652617737), sfix(47342.14147921585), sfix(1.0), sfix(1.0)],
        [sfix(339853900.34919447), sfix(963136759.5090058), sfix(1139561328.7630842), sfix(719935898.7848309), sfix(256117519.91184714), sfix(48645395.609452434), sfix(3853703.0781453173), sfix(1.0), sfix(1.0)],
        [sfix(-538289332.1006515), sfix(-1894423042.7963462), sfix(-2735962519.4679255), sfix(-2084069964.6431293), sfix(-885347958.7916389), sfix(-199242987.28545752), sfix(-18582374.225578513), sfix(1.0), sfix(1.0)],
        [sfix(-305411328.80264217), sfix(-934461374.3047999), sfix(-1106804403.0272455), sfix(-623556350.4425952), sfix(-154595602.21078354), sfix(-5505788.028315315), sfix(2702609.147222214), sfix(1.0), sfix(1.0)],
        [sfix(774034729.1646978), sfix(3454500557.462999), sfix(6315571367.921524), sfix(6057408195.47183), sfix(3220139764.905263), sfix(901191356.5727441), sfix(103885778.70168278), sfix(1.0), sfix(1.0)],
        [sfix(-271926633.2229011), sfix(-1609363527.8340893), sfix(-3877414188.038362), sfix(-4857561467.030758), sfix(-3334912584.999724), sfix(-1191017752.4443731), sfix(-173199793.6617053), sfix(1.0), sfix(1.0)],
        [sfix(174043689.63476586), sfix(1083532944.0871985), sfix(2898158740.6022673), sfix(4235265479.626633), sfix(3529526273.1336713), sfix(1573009170.3012035), sfix(290568416.7679617), sfix(1.0), sfix(1.0)],
        [sfix(30054285.422466103), sfix(22780270.210064054), sfix(-361208493.7562666), sfix(-1111546523.560361), sfix(-1409243331.38773), sfix(-862423370.951102), sfix(-210331686.8231622), sfix(1.0), sfix(1.0)],
        [sfix(-4386611.478285003), sfix(-256318901.0364125), sfix(-1299271997.226012), sfix(-2783420869.0734453), sfix(-3073216691.0467095), sfix(-1737557742.3894656), sfix(-399828724.07895327), sfix(1.0), sfix(1.0)],
        [sfix(16298911.595124396), sfix(3757059.430697718), sfix(76080409.2239518), sfix(1134284048.5159285), sfix(3268558252.2627826), sfix(3794292042.302456), sfix(1631352897.8319738), sfix(1.0), sfix(1.0)],
        [sfix(15647986.609398872), sfix(-12077609.185893448), sfix(-87462796.26688512), sfix(213188532.4383358), sfix(276074397.72499156), sfix(-1533544371.45552), sfix(-2432302611.476242), sfix(1.0), sfix(1.0)],
        [sfix(15647759.59094073), sfix(-12086492.84577352), sfix(-88073896.08432043), sfix(185930595.7166629), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(15647760.860375544), sfix(-12095628.246908698), sfix(-87649008.12910455), sfix(205775398.90509364), sfix(340696118.26324713), sfix(-1805051098.5870183), sfix(1888860699.2293456), sfix(1.0), sfix(1.0)],
        [sfix(15179203.156003756), sfix(-820556.0102914656), sfix(-202484084.48714793), sfix(841167458.227886), sfix(-1678002263.1000736), sfix(1690523599.4924154), sfix(-688037853.2159197), sfix(1.0), sfix(1.0)],
        [sfix(22763029.073239792), sfix(-99464619.46580136), sfix(335059457.8736594), sfix(-729728839.2476832), sfix(918352718.564501), sfix(-610160207.0688639), sfix(165630342.17351502), sfix(1.0), sfix(1.0)],
        [sfix(-28970855.842156965), sfix(317977652.13185155), sfix(-1074564306.1949522), sfix(1820671751.2637887), sfix(-1689742290.1434238), sfix(819370355.7394476), sfix(-162507396.9771302), sfix(1.0), sfix(1.0)],
        [sfix(350847563.0887371), sfix(-1996609098.9243324), sfix(4808461681.239117), sfix(-6162543416.161602), sfix(4410363490.80998), sfix(-1669276979.78459), sfix(260991674.91322556), sfix(1.0), sfix(1.0)],
        [sfix(-1410398845.7982292), sfix(6862495148.182751), sfix(-13772309010.913923), sfix(14636985657.86987), sfix(-8696058937.439548), sfix(2738632247.5920706), sfix(-357151715.11002874), sfix(1.0), sfix(1.0)],
        [sfix(249504695.40754083), sfix(-491962040.11389315), sfix(-198307429.43290704), sfix(1278480037.4324484), sfix(-1303120597.4291468), sfix(557139074.1077976), sfix(-89019034.1264809), sfix(1.0), sfix(1.0)],
        [sfix(4834206993.244222), sfix(-19817663051.191505), sfix(33753311598.32379), sfix(-30541160346.30285), sfix(15475714287.035883), sfix(-4162781127.0098715), sfix(464333864.6280381), sfix(1.0), sfix(1.0)],
        [sfix(-8306889436.307882), sfix(29647191036.172203), sfix(-43845178206.84488), sfix(34399335432.502846), sfix(-15102487886.111704), sfix(3518310333.3777423), sfix(-339827132.756172), sfix(1.0), sfix(1.0)],
        [sfix(2273116803.0764894), sfix(-8181341923.322724), sfix(11803961010.991302), sfix(-8824896559.355228), sfix(3628704488.527724), sfix(-781641730.3040606), sfix(69137871.1925973), sfix(1.0), sfix(1.0)],
        [sfix(2600057078.1366014), sfix(-6210078133.3777275), sfix(6178567484.697367), sfix(-3278668406.1278143), sfix(978550577.609504), sfix(-155747268.67396852), sfix(10327577.425288592), sfix(1.0), sfix(1.0)],
        [sfix(-51221.43496294611), sfix(-254266.04475326912), sfix(-429229.54415179224), sfix(135020.74104830853), sfix(-22600.3715819244), sfix(1987.39174496316), sfix(-72.75357243982), sfix(1.0), sfix(1.0)]
    ]
    scaler = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)]
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
        sfix(-2.5999999046325684),
        sfix(-1.6499998569488525),
        sfix(-1.1749999523162842),
        sfix(-0.9374999403953552),
        sfix(-0.6999999284744263),
        sfix(-0.40312492847442627),
        sfix(-0.3437499403953552),
        sfix(-0.10624993592500687),
        sfix(-0.046874936670064926),
        sfix(0.012500062584877014),
        sfix(0.2500000596046448),
        sfix(0.48750004172325134),
        sfix(0.7250000238418579),
        sfix(0.9625000357627869),
        sfix(1.2000000476837158),
        sfix(1.4375),
        sfix(1.6750000715255737),
        sfix(1.9125001430511475),
        sfix(2.1500000953674316),
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
        [sfix(44628065.71471219), sfix(121956763.97690563), sfix(133412787.19624126), sfix(77845072.80620018), sfix(25624097.75396617), sfix(4503519.884243053), sfix(329674.1614874337), sfix(1.0), sfix(1.0)],
        [sfix(317219550.1749261), sfix(1368644618.5205243), sfix(2415011056.2040095), sfix(2245623641.9002056), sfix(1162347688.8868196), sfix(317999317.79705596), sfix(35976118.81449823), sfix(1.0), sfix(1.0)],
        [sfix(-173608852.4180975), sfix(-957140725.2592288), sfix(-2155248653.6425934), sfix(-2516811349.048052), sfix(-1609778971.3731732), sfix(-535207491.6042399), sfix(-72262031.5179568), sfix(1.0), sfix(1.0)],
        [sfix(46643383.48787672), sfix(328319353.7784897), sfix(949181880.2414122), sfix(1447213297.2475338), sfix(1206042432.5818315), sfix(516268718.7069314), sfix(88194121.7880943), sfix(1.0), sfix(1.0)],
        [sfix(-595586.9277902872), sfix(-32619262.866058055), sfix(-188575656.39979157), sfix(-439935975.7831249), sfix(-521761456.70455724), sfix(-304623679.6707362), sfix(-67614601.68948495), sfix(1.0), sfix(1.0)],
        [sfix(2512533.2254516766), sfix(7295154.132135813), sfix(25662611.130494505), sfix(175854108.89775357), sfix(478924701.0152495), sfix(567953071.0247128), sfix(251651359.92388695), sfix(1.0), sfix(1.0)],
        [sfix(2401158.3299094154), sfix(4792094.90813476), sfix(2278950.393162285), sfix(59619848.894615084), sfix(154839597.92863834), sfix(87699286.77933943), sfix(-43642622.54173899), sfix(1.0), sfix(1.0)],
        [sfix(2392064.8513903413), sfix(4460976.036766551), sfix(-2632560.4952311404), sfix(21624456.00540291), sfix(-6736356.528052676), sfix(-268914732.41087896), sfix(-358328247.11248106), sfix(1.0), sfix(1.0)],
        [sfix(2392070.526625975), sfix(4461744.1667258125), sfix(-2623145.610875513), sfix(21292620.322708957), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(2392065.1811004835), sfix(4462150.575777566), sfix(-2636787.5402225344), sfix(22539291.358067438), sfix(1322002.1534024326), sfix(-234613935.11871254), sfix(352332551.45722383), sfix(1.0), sfix(1.0)],
        [sfix(2471278.4097344317), sfix(3584248.9146729093), sfix(-2738850.2747615245), sfix(65891230.41485297), sfix(-251309292.3355766), sfix(368922539.115249), sfix(-193594756.58670968), sfix(1.0), sfix(1.0)],
        [sfix(-2256866.1940797), sfix(45884410.00027337), sfix(-141863092.12950194), sfix(240363284.7029448), sfix(-207947736.6558687), sfix(77534411.16736656), sfix(-5055764.093894248), sfix(1.0), sfix(1.0)],
        [sfix(72683047.58837408), sfix(-505113371.9459516), sfix(1527177184.5226703), sfix(-2415522457.599948), sfix(2120119523.227915), sfix(-978527439.3651599), sfix(185519983.97795016), sfix(1.0), sfix(1.0)],
        [sfix(-450619692.5721815), sfix(2631634793.914441), sfix(-6304593389.441929), sfix(8008922204.898743), sfix(-5680394722.898481), sfix(2132319007.380842), sfix(-330931638.07561415), sfix(1.0), sfix(1.0)],
        [sfix(1634505291.2964516), sfix(-7892391017.895658), sfix(15832358518.356108), sfix(-16831622240.859554), sfix(10003221042.353117), sfix(-3150420852.262171), sfix(410719235.49431175), sfix(1.0), sfix(1.0)],
        [sfix(-3584604285.2198954), sfix(15042536863.916006), sfix(-26063506080.909748), sfix(23902310383.65146), sfix(-12234329914.411783), sfix(3314069778.8093643), sfix(-371216342.4465793), sfix(1.0), sfix(1.0)],
        [sfix(4759956567.409276), sfix(-17649375411.119236), sfix(26935943046.567196), sfix(-21658669363.563866), sfix(9689295684.725992), sfix(-2288826284.4417787), sfix(223258365.0201996), sfix(1.0), sfix(1.0)],
        [sfix(-4094497940.607975), sfix(13289144124.018011), sfix(-17678041522.64275), sfix(12384786564.98373), sfix(-4827786536.747741), sfix(994591437.3373647), sfix(-84715858.49972403), sfix(1.0), sfix(1.0)],
        [sfix(-1017442692.3617265), sfix(2409104568.9588294), sfix(-2368612019.23514), sfix(1244735089.4173474), sfix(-367752401.87760556), sfix(57919278.84012228), sfix(-3799209.9399881535), sfix(1.0), sfix(1.0)],
        [sfix(359190.52246747457), sfix(1783041.680340381), sfix(3009973.9364881422), sfix(-946833.4996453767), sfix(158485.19828904618), sfix(-13936.59275186331), sfix(510.18472473037), sfix(1.0), sfix(1.0)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)]
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
        sfix(-2.5999999046325684),
        sfix(-2.125),
        sfix(-1.8874999284744263),
        sfix(-1.6499998569488525),
        sfix(-1.4124999046325684),
        sfix(-1.1749999523162842),
        sfix(-0.9374999403953552),
        sfix(-0.8187499046325684),
        sfix(-0.6999999284744263),
        sfix(-0.5812499523162842),
        sfix(-0.5218749046325684),
        sfix(-0.10624993592500687),
        sfix(0.012500062584877014),
        sfix(0.2500000596046448),
        sfix(0.7250000238418579),
        sfix(1.2000000476837158),
        sfix(1.6750000715255737),
        sfix(2.1500000953674316),
        sfix(3.0999999046325684)
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
        [sfix(-587450.7697691192), sfix(-1652523.8613299804), sfix(-1625826.3938243664), sfix(-852617.1400031873), sfix(-256217.32296206747), sfix(-41643.86844122784), sfix(-2843.25784686898), sfix(1.0), sfix(1.0)],
        [sfix(-17759373.842132673), sfix(-50376030.19509324), sfix(-59284485.86410796), sfix(-37277338.52447707), sfix(-13211480.514068147), sfix(-2501326.88470058), sfix(-197591.26754191416), sfix(1.0), sfix(1.0)],
        [sfix(50599458.57694902), sfix(171011854.7001167), sfix(239581274.54247278), sfix(177985057.66127998), sfix(74035449.57689601), sfix(16365317.507560613), sfix(1502953.0330462628), sfix(1.0), sfix(1.0)],
        [sfix(-18525729.210009445), sfix(-88787659.68788274), sfix(-167286756.45580134), sfix(-161872954.38694307), sfix(-85662232.72866517), sfix(-23660194.771001287), sfix(-2677327.983000876), sfix(1.0), sfix(1.0)],
        [sfix(-41843652.64843097), sfix(-168352344.75075316), sfix(-273058279.03816134), sfix(-228021909.32319582), sfix(-102531345.08988921), sfix(-23153339.810860876), sfix(-1979119.5308573644), sfix(1.0), sfix(1.0)],
        [sfix(37445231.07654593), sfix(199841251.01548994), sfix(432269504.6823492), sfix(483501764.86836636), sfix(294585059.77581537), sfix(92443236.54827167), sfix(11606023.19760482), sfix(1.0), sfix(1.0)],
        [sfix(-26294373.042741273), sfix(-183373434.8841064), sfix(-527456840.9948585), sfix(-798020329.6584752), sfix(-667670573.3775407), sfix(-292771006.347132), sfix(-52623411.850682385), sfix(1.0), sfix(1.0)],
        [sfix(-2100363.484454022), sfix(-5438694.914054992), sfix(18369807.04701885), sfix(95897798.88369252), sfix(156677358.78065562), sfix(113078822.07487535), sfix(30715396.036011826), sfix(1.0), sfix(1.0)],
        [sfix(2778505.4623705847), sfix(34649121.84582155), sfix(155602101.4113223), sfix(346423233.842649), sfix(413901615.2626079), sfix(253910416.72463584), sfix(62836577.422770105), sfix(1.0), sfix(1.0)],
        [sfix(1208551.2376643105), sfix(18702935.785164334), sfix(88040740.41829485), sfix(193586778.5348619), sfix(219199617.8238373), sfix(121473894.84574518), sfix(25258840.439186715), sfix(1.0), sfix(1.0)],
        [sfix(-291109.4900334024), sfix(336726.54891000007), sfix(-5926275.969773143), sfix(-63176623.01100568), sfix(-175477459.61093515), sfix(-201661900.46029627), sfix(-84679981.94407198), sfix(1.0), sfix(1.0)],
        [sfix(-273356.67680218566), sfix(903019.5508487867), sfix(1502924.8705500483), sfix(-12147599.237645544), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(-273319.04240292066), sfix(902760.9437917189), sfix(1322361.339083867), sfix(-15272294.670291197), sfix(-5091761.681683325), sfix(129532051.63637035), sfix(-174672939.20504668), sfix(1.0), sfix(1.0)],
        [sfix(-672998.1166730204), sfix(7015604.439753667), sfix(-35126310.13219083), sfix(86411153.91589753), sfix(-113022677.66509166), sfix(72023050.07984152), sfix(-17089343.860691227), sfix(1.0), sfix(1.0)],
        [sfix(-362685.7747364172), sfix(-8020876.12499666), sfix(50114842.73362912), sfix(-114578299.84184311), sfix(122823528.89417009), sfix(-63344559.02948317), sfix(12752589.599141207), sfix(1.0), sfix(1.0)],
        [sfix(204737729.8647508), sfix(-906908703.3533901), sfix(1659965255.8429983), sfix(-1609371970.8526704), sfix(870284057.1660657), sfix(-248556599.1986637), sfix(29268591.70535102), sfix(1.0), sfix(1.0)],
        [sfix(1305767246.3366022), sfix(-4071549442.413355), sfix(5252782968.695124), sfix(-3592233849.0865855), sfix(1374231657.8990352), sfix(-279005844.462576), sfix(23498825.061388366), sfix(1.0), sfix(1.0)],
        [sfix(62975242.38102436), sfix(-140742673.19054234), sfix(130297681.30540438), sfix(-64344214.874985464), sfix(17825652.44120401), sfix(-2626880.5286092465), sfix(160886.07945017752), sfix(1.0), sfix(1.0)],
        [sfix(3774.32364920869), sfix(-147760.85514753283), sfix(-157548.57689351222), sfix(48971.91426780642), sfix(-8016.17752314851), sfix(685.74340480148), sfix(-24.34797214178), sfix(1.0), sfix(1.0)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)]
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
        sfix(-2.5999999046325684),
        sfix(-1.6499998569488525),
        sfix(-1.1749999523162842),
        sfix(-0.9374999403953552),
        sfix(-0.6999999284744263),
        sfix(-0.3437499403953552),
        sfix(-0.2843749523162842),
        sfix(-0.22499993443489075),
        sfix(-0.046874936670064926),
        sfix(0.012500062584877014),
        sfix(0.2500000596046448),
        sfix(0.48750004172325134),
        sfix(0.7250000238418579),
        sfix(0.9625000357627869),
        sfix(1.2000000476837158),
        sfix(1.6750000715255737),
        sfix(2.1500000953674316),
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
        [sfix(123562564.4184822), sfix(332061929.59643847), sfix(368347599.46686417), sfix(217578595.1801744), sfix(72213269.020079), sfix(12763160.10023693), sfix(938181.6728024373), sfix(1.0), sfix(1.0)],
        [sfix(619418762.5149761), sfix(2717293754.956714), sfix(4884878670.4809265), sfix(4618195711.706842), sfix(2425905670.4042764), sfix(672529066.5250233), sfix(77000301.16723286), sfix(1.0), sfix(1.0)],
        [sfix(-353250963.6423666), sfix(-1967583891.6546445), sfix(-4486470063.276183), sfix(-5341823340.947017), sfix(-3502207526.6027927), sfix(-1199435673.2909403), sfix(-167765217.94071132), sfix(1.0), sfix(1.0)],
        [sfix(80347255.29586667), sfix(610659287.1395876), sfix(1880950513.5557542), sfix(3012727756.349706), sfix(2634802877.246999), sfix(1190953691.688776), sfix(217388474.4400252), sfix(1.0), sfix(1.0)],
        [sfix(-2088849.4306648904), sfix(-40622379.560394585), sfix(-256360949.7816565), sfix(-711581826.6268617), sfix(-992871466.9111483), sfix(-677040361.9800922), sfix(-178414145.69724843), sfix(1.0), sfix(1.0)],
        [sfix(1260101.3241354937), sfix(6793972.074955263), sfix(23410050.415332373), sfix(169987948.87201226), sfix(573772430.0732211), sfix(813677174.1319817), sfix(415727442.0720414), sfix(1.0), sfix(1.0)],
        [sfix(1200915.757201505), sfix(5521944.91586477), sfix(11994250.012185259), sfix(115231880.84520642), sfix(425735355.051747), sfix(599798992.7060255), sfix(286731385.63815314), sfix(1.0), sfix(1.0)],
        [sfix(1149338.9004666733), sfix(4095295.8679784373), sfix(-4680891.316733604), sfix(9696260.248528989), sfix(44068055.98149993), sfix(-147989233.9916092), sfix(-332921232.7665208), sfix(1.0), sfix(1.0)],
        [sfix(1149266.5736411547), sfix(4091153.286379361), sfix(-4839718.889172425), sfix(5134479.042291564), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(1149266.4366540387), sfix(4090047.5169648216), sfix(-4787964.346685586), sfix(7618869.736872439), sfix(44494676.62742185), sfix(-220315086.58606735), sfix(253209326.654322), sfix(1.0), sfix(1.0)],
        [sfix(1130710.6567180122), sfix(4819044.604452485), sfix(-14679757.195205342), sfix(73890061.19796261), sfix(-196500573.1488887), sfix(239899435.35124168), sfix(-111270591.86866295), sfix(1.0), sfix(1.0)],
        [sfix(386685.31042589067), sfix(8997330.598319655), sfix(-11281095.940472748), sfix(-2481471.9876918346), sfix(24647217.007089686), sfix(-28417524.36654819), sfix(11278859.42459892), sfix(1.0), sfix(1.0)],
        [sfix(16782917.2074079), sfix(-107656486.11248988), sfix(326957200.59001756), sfix(-508960029.3331189), sfix(430396449.0550818), sfix(-187333567.1130424), sfix(32829979.31671414), sfix(1.0), sfix(1.0)],
        [sfix(-60008759.460138865), sfix(336162292.9641742), sfix(-737030170.7155819), sfix(843979975.4102929), sfix(-530752070.8025462), sfix(173746701.2613674), sfix(-23081469.11293147), sfix(1.0), sfix(1.0)],
        [sfix(174562232.06837213), sfix(-717122573.3224324), sfix(1225640879.701476), sfix(-1096841039.4810429), sfix(542130684.7839823), sfix(-140096773.88883603), sfix(14787643.128993655), sfix(1.0), sfix(1.0)],
        [sfix(-756144528.0582961), sfix(2496057192.6836524), sfix(-3388939465.155991), sfix(2430663427.8144484), sfix(-971048490.105541), sfix(205100831.9044714), sfix(-17911573.901996072), sfix(1.0), sfix(1.0)],
        [sfix(-392364767.7857377), sfix(941017258.4503068), sfix(-936286378.5877898), sfix(498519007.7600835), sfix(-149254896.19120064), sfix(23826021.23620037), sfix(-1584430.4098640566), sfix(1.0), sfix(1.0)],
        [sfix(193141.7345027316), sfix(958766.2849203527), sfix(1618504.805972391), sfix(-509125.52798476827), sfix(85219.69310037745), sfix(-7493.89955658479), sfix(274.33341495472), sfix(1.0), sfix(1.0)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)]
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
        sfix(-2.5999999046325684),
        sfix(-1.6499998569488525),
        sfix(-1.1749999523162842),
        sfix(-0.6999999284744263),
        sfix(-0.22499993443489075),
        sfix(-0.10624993592500687),
        sfix(-0.046874936670064926),
        sfix(0.012500062584877014),
        sfix(0.2500000596046448),
        sfix(0.48750004172325134),
        sfix(0.5468750596046448),
        sfix(0.6062500476837158),
        sfix(0.7250000238418579),
        sfix(0.9625000357627869),
        sfix(1.2000000476837158),
        sfix(1.4375),
        sfix(1.6750000715255737),
        sfix(1.9125001430511475),
        sfix(2.1500000953674316),
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
        [sfix(68340211.05091757), sfix(184052196.74959552), sfix(204840535.1050845), sfix(121373757.00771812), sfix(40396827.10552218), sfix(7158246.324030065), sfix(527439.0515816789), sfix(1.0), sfix(1.0)],
        [sfix(242161339.94461828), sfix(1099551568.3954408), sfix(2037378822.7694767), sfix(1977508966.9142413), sfix(1062811813.2580847), sfix(300598928.6984621), sfix(35030134.39662827), sfix(1.0), sfix(1.0)],
        [sfix(-13787610.492576485), sfix(-67831724.8614566), sfix(-109644495.12278365), sfix(-27351519.001671974), sfix(93039589.44806497), sfix(88874536.49770102), sfix(23806335.92438716), sfix(1.0), sfix(1.0)],
        [sfix(254073.466264372), sfix(-1292654.060931519), sfix(-43434248.76104042), sfix(-196516810.96975392), sfix(-379406244.51717186), sfix(-337542747.7825638), sfix(-113591844.21610093), sfix(1.0), sfix(1.0)],
        [sfix(495088.6221864212), sfix(3346263.7550669326), sfix(-5996201.265466722), sfix(-33012619.599933464), sfix(32092870.522855863), sfix(233926208.5004659), sfix(231432926.0423042), sfix(1.0), sfix(1.0)],
        [sfix(495172.5904663366), sfix(3348833.5096458565), sfix(-5976588.8590250965), sfix(-33181641.654913556), sfix(28468271.456928633), sfix(212393702.39356393), sfix(186454271.55054957), sfix(1.0), sfix(1.0)],
        [sfix(495169.5014185458), sfix(3348676.645489963), sfix(-5997368.7920621), sfix(-34470516.901537545), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(495169.74549773696), sfix(3348378.906218953), sfix(-5990946.380539269), sfix(-33486960.16564326), sfix(20189465.150530096), sfix(200678267.40401247), sfix(-270069870.3495805), sfix(1.0), sfix(1.0)],
        [sfix(590851.2537355849), sfix(1191234.059350099), sfix(14748794.175521845), sfix(-142781797.4607568), sfix(354234405.80992717), sfix(-361665801.53124946), sfix(137088224.79242676), sfix(1.0), sfix(1.0)],
        [sfix(-244942.42004146244), sfix(11894369.973712502), sfix(-42608289.650702596), sfix(21859365.15647409), sfix(87260359.9241976), sfix(-129812171.15076162), sfix(52851544.30021867), sfix(1.0), sfix(1.0)],
        [sfix(-1316154.7535610765), sfix(23617213.585538764), sfix(-96098469.30090271), sfix(152119156.58717594), sfix(-91292528.84203935), sfix(811071.0397318372), sfix(13007686.413935734), sfix(1.0), sfix(1.0)],
        [sfix(-3947047.968393074), sfix(49187815.84466991), sfix(-199769302.8650131), sfix(376542518.114407), sfix(-364886137.7374813), sfix(178906172.72276184), sfix(-35353886.73426628), sfix(1.0), sfix(1.0)],
        [sfix(1939776.4024044021), sfix(5638862.652482417), sfix(-66222672.590316966), sfix(159469096.83287096), sfix(-167901544.17421472), sfix(84457805.6776309), sfix(-16707567.882337889), sfix(1.0), sfix(1.0)],
        [sfix(5658017.563071811), sfix(-23008061.205758043), sfix(23252294.27350942), sfix(13354862.892619424), sfix(-35686641.533749856), sfix(21394954.460306983), sfix(-4291653.796528684), sfix(1.0), sfix(1.0)],
        [sfix(35235632.797946356), sfix(-183758618.4977906), sfix(384365558.62233746), sfix(-416451308.4553691), sfix(250500280.20431486), sfix(-79771291.42466195), sfix(10551630.356035352), sfix(1.0), sfix(1.0)],
        [sfix(11084896.7472012), sfix(16490252.17161164), sfix(-134521128.73201203), sfix(221242809.557702), sfix(-162999660.5347043), sfix(57586175.543010935), sfix(-7942532.001992094), sfix(1.0), sfix(1.0)],
        [sfix(-195252793.03541446), sfix(421848104.9148762), sfix(-244611472.50606528), sfix(-83072010.85702287), sfix(148103758.24042612), sfix(-58362882.51358891), sfix(7735646.370412247), sfix(1.0), sfix(1.0)],
        [sfix(138960508.87981156), sfix(-87948230.2224038), sfix(-283135098.0402962), sfix(436277436.114272), sfix(-249317631.9514467), sfix(65456247.93989874), sfix(-6620483.6115451595), sfix(1.0), sfix(1.0)],
        [sfix(-681818680.996789), sfix(1632444697.8298655), sfix(-1626592541.9895453), sfix(865131171.2040104), sfix(-258788090.161123), sfix(41280675.0770664), sfix(-2743381.2750905156), sfix(1.0), sfix(1.0)],
        [sfix(88553.63690919506), sfix(439585.16632669023), sfix(742068.9645558), sfix(-233429.18228322957), sfix(39072.41373951856), sfix(-3435.88123053859), sfix(125.7792454022), sfix(1.0), sfix(1.0)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)]
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
        sfix(-2.5999999046325684),
        sfix(-2.125),
        sfix(-1.6499998569488525),
        sfix(-1.1749999523162842),
        sfix(-0.9374999403953552),
        sfix(-0.6999999284744263),
        sfix(-0.40312492847442627),
        sfix(-0.3437499403953552),
        sfix(-0.10624993592500687),
        sfix(0.012500062584877014),
        sfix(0.2500000596046448),
        sfix(0.7250000238418579),
        sfix(1.2000000476837158),
        sfix(1.6750000715255737),
        sfix(2.1500000953674316),
        sfix(3.0999999046325684)
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
        [sfix(607439.7778342287), sfix(-661828.8576813393), sfix(321989.9073734743), sfix(705780.2864829089), sfix(318954.02131058904), sfix(61813.47426355968), sfix(4585.01865426441), sfix(1.0), sfix(1.0)],
        [sfix(-2630912.5463090762), sfix(-18080960.41774766), sfix(-30709267.805934194), sfix(-25920045.22325012), sfix(-11810117.258911632), sfix(-2777245.8349712486), sfix(-265199.89619125763), sfix(1.0), sfix(1.0)],
        [sfix(77994364.38434593), sfix(338617440.20493615), sfix(610080396.4947394), sfix(576791256.8088667), sfix(302716591.31886476), sfix(83845100.22017741), sfix(9593109.15427128), sfix(1.0), sfix(1.0)],
        [sfix(-53022020.03951617), sfix(-299188780.4723306), sfix(-681284461.9300808), sfix(-814807423.470228), sfix(-538844635.3585995), sfix(-186858478.99179652), sfix(-26577201.874910183), sfix(1.0), sfix(1.0)],
        [sfix(2711786.864930708), sfix(41026726.10905657), sfix(184555935.02883816), sfix(361130973.65864456), sfix(360073364.7479449), sfix(179848807.56762436), sfix(35791772.90270508), sfix(1.0), sfix(1.0)],
        [sfix(-430797.9260884802), sfix(15450907.919306379), sfix(97039681.7806583), sfix(199682897.767482), sfix(190438276.9099033), sfix(83455838.00106972), sfix(12624591.830110185), sfix(1.0), sfix(1.0)],
        [sfix(-1840573.2106867225), sfix(-3252934.6509460676), sfix(-6836999.78551467), sfix(-109636615.21703371), sfix(-330738090.3001238), sfix(-387905633.4258793), sfix(-166225289.33336478), sfix(1.0), sfix(1.0)],
        [sfix(-1789949.412158065), sfix(-1993454.6410827024), sfix(5793511.490024559), sfix(-43570508.625925705), sfix(-139512111.88369963), sfix(-96527901.02445967), sfix(16735761.025364898), sfix(1.0), sfix(1.0)],
        [sfix(-1783712.4163791547), sfix(-1762442.9917249968), sfix(9655989.662302092), sfix(-8767887.142699685), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(-1783627.17307666), sfix(-1762595.2990854986), sfix(9227950.97502642), sfix(-16826138.03374822), sfix(-31472276.22189848), sfix(165089475.19598356), sfix(-191328251.6998071), sfix(1.0), sfix(1.0)],
        [sfix(-2276096.9280876378), sfix(5990038.940028745), sfix(-39077279.58366203), sfix(129437107.958264), sfix(-230034422.83409256), sfix(199103665.98779207), sfix(-66640736.098263405), sfix(1.0), sfix(1.0)],
        [sfix(-26911419.083918575), sfix(169152008.29360226), sfix(-464521419.4812481), sfix(662629256.2256751), sfix(-523979789.2546252), sfix(217598396.58174932), sfix(-37125335.399681605), sfix(1.0), sfix(1.0)],
        [sfix(-16021817.619782194), sfix(35874562.064194866), sfix(-12911365.594583903), sfix(-45431060.16803016), sfix(57046554.66490405), sfix(-25938828.48244759), sfix(4212931.738640829), sfix(1.0), sfix(1.0)],
        [sfix(1549456474.8838916), sfix(-4990611754.481042), sfix(6643643264.461801), sfix(-4686032089.972154), sfix(1845922263.3551457), sfix(-385229748.8204658), sfix(33293193.050184827), sfix(1.0), sfix(1.0)],
        [sfix(204579068.4739587), sfix(-458771349.81628734), sfix(422622986.50231344), sfix(-209071911.35663134), sfix(57997621.608826965), sfix(-8554939.55609413), sfix(524318.4105421808), sfix(1.0), sfix(1.0)],
        [sfix(43313.11309241878), sfix(-1695663.4382243012), sfix(-1807984.6741698137), sfix(561988.3861012871), sfix(-91991.47585466193), sfix(7869.40504784418), sfix(-279.41071475877), sfix(1.0), sfix(1.0)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)]
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
        sfix(-2.5999999046325684),
        sfix(-2.125),
        sfix(-1.8874999284744263),
        sfix(-1.6499998569488525),
        sfix(-1.4124999046325684),
        sfix(-1.1749999523162842),
        sfix(-1.056249976158142),
        sfix(-0.8187499046325684),
        sfix(-0.6999999284744263),
        sfix(-0.4624999165534973),
        sfix(-0.22499993443489075),
        sfix(-0.10624993592500687),
        sfix(0.012500062584877014),
        sfix(0.2500000596046448),
        sfix(0.48750004172325134),
        sfix(0.7250000238418579),
        sfix(0.9625000357627869),
        sfix(1.140625),
        sfix(1.4375),
        sfix(1.6750000715255737),
        sfix(2.1500000953674316),
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
        [sfix(1936553.6361436232), sfix(4275547.080138519), sfix(4687605.452904153), sfix(2723742.1901164567), sfix(871338.0002930848), sfix(146552.25875085947), sfix(10186.23557063923), sfix(1.0), sfix(1.0)],
        [sfix(63762134.15643626), sfix(179766700.20768508), sfix(212439928.09458122), sfix(134016061.48164444), sfix(47585440.83334779), sfix(9018857.08822683), sfix(712906.7693334888), sfix(1.0), sfix(1.0)],
        [sfix(-172220930.6725746), sfix(-584976756.3087928), sfix(-820582149.4049072), sfix(-610491260.395056), sfix(-254350072.1847679), sfix(-56311925.09274664), sfix(-5179140.80028944), sfix(1.0), sfix(1.0)],
        [sfix(34316568.1499256), sfix(196168828.46982554), sfix(410060725.2797698), sfix(423281558.73657316), sfix(234020129.86308303), sfix(66712932.04468892), sfix(7731780.303417135), sfix(1.0), sfix(1.0)],
        [sfix(176157204.6692164), sfix(732423472.5416777), sfix(1240550945.0560827), sfix(1093696397.9080665), sfix(528755561.230976), sfix(132526431.95456542), sfix(13373365.47885494), sfix(1.0), sfix(1.0)],
        [sfix(-223396278.32007116), sfix(-1233842758.2290483), sfix(-2792841760.486753), sfix(-3320748759.6061506), sfix(-2190120230.056567), sfix(-760969387.9492455), sfix(-109026623.35336584), sfix(1.0), sfix(1.0)],
        [sfix(52605912.96043818), sfix(380954913.9241575), sfix(1148328982.4226382), sfix(1815316721.877265), sfix(1579027870.0165596), sfix(715837252.0701792), sfix(132322147.82411902), sfix(1.0), sfix(1.0)],
        [sfix(11228336.356202958), sfix(66482825.30752935), sfix(154837521.10217357), sfix(144677916.41018328), sfix(1418862.0685973505), sfix(-77595084.82013226), sfix(-33754054.14908588), sfix(1.0), sfix(1.0)],
        [sfix(-1240196.3919873545), sfix(-34573333.59855975), sfix(-185046801.44978398), sfix(-461926508.01461905), sfix(-603735380.5740666), sfix(-397027241.4638386), sfix(-103301665.44982086), sfix(1.0), sfix(1.0)],
        [sfix(2007706.781085443), sfix(5427183.139610384), sfix(22073003.80699403), sfix(115671172.22128779), sfix(311804973.71111524), sfix(385397273.499844), sfix(178404033.69905636), sfix(1.0), sfix(1.0)],
        [sfix(1928154.822976621), sfix(3511188.527124392), sfix(2559189.4120479175), sfix(7870174.76772308), sfix(-29465241.58934746), sfix(-202250237.53380328), sfix(-251740237.6742973), sfix(1.0), sfix(1.0)],
        [sfix(1927619.2495614684), sfix(3489602.3129164423), sfix(2266901.9658202827), sfix(7734277.880342778), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(1927619.7979481705), sfix(3491164.206104967), sfix(2162230.6966951047), sfix(6370516.281906381), sfix(-41214676.45722265), sfix(-159124751.21977693), sfix(351057583.17613614), sfix(1.0), sfix(1.0)],
        [sfix(2013935.422177223), sfix(2575516.652548098), sfix(1235983.330554296), sfix(60291577.41274857), sfix(-344746317.28055805), sfix(560011761.7355043), sfix(-298736503.9023695), sfix(1.0), sfix(1.0)],
        [sfix(2329993.023061349), sfix(-12505756.761099968), sfix(135899697.17792258), sfix(-467373667.58175874), sfix(720523727.0807196), sfix(-532557801.7072929), sfix(154399650.9214586), sfix(1.0), sfix(1.0)],
        [sfix(-13970160.6569741), sfix(141646864.79932576), sfix(-465511861.614466), sfix(774609804.3180953), sfix(-713863302.5036722), sfix(346990388.4011797), sfix(-69526421.69924845), sfix(1.0), sfix(1.0)],
        [sfix(106966075.1990892), sfix(-614143090.7424691), sfix(1506739666.4153166), sfix(-1976221835.3383067), sfix(1449053497.3827546), sfix(-562024880.2008144), sfix(90005919.53854232), sfix(1.0), sfix(1.0)],
        [sfix(-498645268.3538617), sfix(2465484475.7604346), sfix(-5022441768.180356), sfix(5411250108.557283), sfix(-3255769447.197343), sfix(1037116576.4554603), sfix(-136628519.96506006), sfix(1.0), sfix(1.0)],
        [sfix(1143330457.1132822), sfix(-4839605982.182039), sfix(8471810571.753752), sfix(-7843197622.641039), sfix(4048339281.365427), sfix(-1104751939.601904), sfix(124561499.74819103), sfix(1.0), sfix(1.0)],
        [sfix(3632314954.0500994), sfix(-11258421358.527323), sfix(14470891755.951464), sfix(-9874419182.496475), sfix(3772827140.3590093), sfix(-765490137.9701028), sfix(64452752.99679944), sfix(1.0), sfix(1.0)],
        [sfix(878079491.8020085), sfix(-2096156192.5367188), sfix(2083472957.6875563), sfix(-1104905772.1451185), sfix(329550713.94823086), sfix(-52415216.973076984), sfix(3473154.0826020786), sfix(1.0), sfix(1.0)],
        [sfix(-62997.23737701226), sfix(-312721.7812106897), sfix(-527909.3703888118), sfix(166061.99495697403), sfix(-27796.19458855168), sfix(2444.29289432455), sfix(-89.47961095367), sfix(1.0), sfix(1.0)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)]
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
        sfix(-2.5999999046325684),
        sfix(-2.125),
        sfix(-1.6499998569488525),
        sfix(-1.4124999046325684),
        sfix(-1.1749999523162842),
        sfix(-0.9374999403953552),
        sfix(-0.6999999284744263),
        sfix(-0.4624999165534973),
        sfix(-0.3437499403953552),
        sfix(-0.22499993443489075),
        sfix(-0.10624993592500687),
        sfix(0.012500062584877014),
        sfix(0.2500000596046448),
        sfix(0.48750004172325134),
        sfix(0.7250000238418579),
        sfix(0.9625000357627869),
        sfix(1.2000000476837158),
        sfix(1.4375),
        sfix(1.6750000715255737),
        sfix(1.9125001430511475),
        sfix(2.1500000953674316),
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
        [sfix(-5549922.742174471), sfix(-19387541.686563212), sfix(-17524691.75071473), sfix(-8335303.35030662), sfix(-2334652.0211850205), sfix(-363579.6644497706), sfix(-24243.03268381214), sfix(1.0), sfix(1.0)],
        [sfix(-1760238.0965370606), sfix(37131266.25215745), sfix(107348303.93210799), sfix(109679215.79306526), sfix(54468978.19659656), sfix(13414189.643197058), sfix(1317985.02897604), sfix(1.0), sfix(1.0)],
        [sfix(112676504.88586244), sfix(296120576.54422235), sfix(270405954.8179392), sfix(62474756.899361156), sfix(-45750986.01037561), sfix(-29420628.675337218), sfix(-4832305.717537721), sfix(1.0), sfix(1.0)],
        [sfix(-408496305.85486645), sfix(-1801437014.6047375), sfix(-3236256010.9126086), sfix(-3052892529.490161), sfix(-1596041826.6974454), sfix(-438821153.4938456), sfix(-49612646.08876202), sfix(1.0), sfix(1.0)],
        [sfix(211781359.84290648), sfix(1198111045.5018847), sfix(2793899256.349582), sfix(3395377811.160351), sfix(2270462153.1400323), sfix(793094662.2249012), sfix(113209944.79789193), sfix(1.0), sfix(1.0)],
        [sfix(-46492172.475829065), sfix(-339286511.7049518), sfix(-1007679637.9208767), sfix(-1599747328.761628), sfix(-1404978291.228421), sfix(-641360163.4716127), sfix(-118474272.66298103), sfix(1.0), sfix(1.0)],
        [sfix(-1125531.672019852), sfix(19855886.219323512), sfix(176651065.39394495), sfix(482405189.1937671), sfix(652972208.6642232), sfix(442606359.6571113), sfix(119161791.35462591), sfix(1.0), sfix(1.0)],
        [sfix(-3394847.3947146866), sfix(-7632864.533427778), sfix(37078112.035668895), sfix(101975171.16347018), sfix(65620948.270025074), sfix(-44589104.871142745), sfix(-50501222.17409708), sfix(1.0), sfix(1.0)],
        [sfix(-3602389.1855870495), sfix(-11051429.047382412), sfix(13531572.08278134), sfix(15129482.94436433), sfix(-115351980.64626049), sfix(-246693963.4219289), sfix(-145036600.29911682), sfix(1.0), sfix(1.0)],
        [sfix(-3601278.425785814), sfix(-11008927.501257798), sfix(14152955.501359122), sfix(19752840.3066573), sfix(-96536456.19235542), sfix(-206571848.5679532), sfix(-109800272.88890298), sfix(1.0), sfix(1.0)],
        [sfix(-3600971.545534492), sfix(-10990859.990344923), sfix(14943644.973287316), sfix(33906724.479845874), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(-3600891.4053058885), sfix(-10989941.705780407), sfix(14488410.707065), sfix(24354339.31440776), sfix(-73931009.07873008), sfix(-86254615.37039895), sfix(215645841.28473493), sfix(1.0), sfix(1.0)],
        [sfix(-3723116.0864730114), sfix(-8334525.901883156), sfix(-10141293.953697983), sfix(149956464.09991223), sfix(-447366925.5450364), sfix(529592789.96766144), sfix(-224614198.8163207), sfix(1.0), sfix(1.0)],
        [sfix(6238477.443167894), sfix(-118973060.50249247), sfix(503030329.53720653), sfix(-1122983460.9431329), sfix(1334481007.727458), sfix(-805557445.8964586), sfix(193959005.78521937), sfix(1.0), sfix(1.0)],
        [sfix(-115879808.42748295), sfix(808749587.1052276), sfix(-2424608848.4009023), sfix(3785427308.739406), sfix(-3271886721.161709), sfix(1485565363.1526933), sfix(-277013823.3523972), sfix(1.0), sfix(1.0)],
        [sfix(577588137.0553219), sfix(-3341648363.9894195), sfix(7921562599.150977), sfix(-9962930765.561089), sfix(6997929231.179037), sfix(-2602487815.5434303), sfix(400339908.1805141), sfix(1.0), sfix(1.0)],
        [sfix(-1836451957.7032402), sfix(8872020042.279596), sfix(-17825692788.853077), sfix(18985509802.948017), sfix(-11311207418.234833), sfix(3574112142.398993), sfix(-467967151.5843158), sfix(1.0), sfix(1.0)],
        [sfix(3547618113.8550124), sfix(-15388870317.549568), sfix(27468754709.24638), sfix(-25901158633.91075), sfix(13609164332.365053), sfix(-3779193542.1850004), sfix(433392479.8921267), sfix(1.0), sfix(1.0)],
        [sfix(-4110896317.810394), sfix(16957998105.841072), sfix(-28151611776.979965), sfix(24232366121.426334), sfix(-11472204101.436956), sfix(2842624773.0431933), sfix(-288824561.6902899), sfix(1.0), sfix(1.0)],
        [sfix(3972979725.5789585), sfix(-14844395916.830576), sfix(21889743824.79156), sfix(-16600784285.391806), sfix(6891272175.527457), sfix(-1494167796.3479083), sfix(132776125.11785649), sfix(1.0), sfix(1.0)],
        [sfix(4633310286.016664), sfix(-11058124244.518967), sfix(10982218014.625082), sfix(-5821989655.682269), sfix(1735776193.575536), sfix(-275955680.4588218), sfix(18277069.414677538), sfix(1.0), sfix(1.0)],
        [sfix(-640542.0808926828), sfix(-3179686.424707843), sfix(-5367666.594848809), sfix(1688481.9118618502), sfix(-282625.6049343136), sfix(24853.03359398486), sfix(-909.80904218492), sfix(1.0), sfix(1.0)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)]
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
        sfix(-2.5999999046325684),
        sfix(-2.125),
        sfix(-1.6499998569488525),
        sfix(-1.4124999046325684),
        sfix(-1.1749999523162842),
        sfix(-0.9374999403953552),
        sfix(-0.6999999284744263),
        sfix(-0.4624999165534973),
        sfix(-0.40312492847442627),
        sfix(-0.10624993592500687),
        sfix(-0.046874936670064926),
        sfix(0.012500062584877014),
        sfix(0.2500000596046448),
        sfix(0.7250000238418579),
        sfix(0.9625000357627869),
        sfix(1.2000000476837158),
        sfix(1.4375),
        sfix(1.6750000715255737),
        sfix(2.1500000953674316),
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
        [sfix(244742.05516105008), sfix(-806205.3922665514), sfix(-179577.207210575), sfix(244381.44396927004), sfix(140821.54586903212), sfix(29176.93873416886), sfix(2222.0469532582), sfix(1.0), sfix(1.0)],
        [sfix(23629008.519010477), sfix(66452199.480490305), sfix(80488082.37013291), sfix(51883061.278963365), sfix(18747986.906914793), sfix(3607453.75189003), sfix(289121.4099460134), sfix(1.0), sfix(1.0)],
        [sfix(-95320577.18249717), sfix(-359899476.3133746), sfix(-556827261.0372576), sfix(-456660458.9469708), sfix(-209710985.58166987), sfix(-51178001.28592963), sfix(-5189647.813196077), sfix(1.0), sfix(1.0)],
        [sfix(66907461.41801477), sfix(333862208.40874285), sfix(680898265.943484), sfix(722504760.6268845), sfix(422963500.7994436), sfix(130085953.20265767), sfix(16474953.231253885), sfix(1.0), sfix(1.0)],
        [sfix(-547106.0598381177), sfix(-47920115.81032447), sfix(-213991368.032883), sfix(-390571649.4771163), sfix(-352486793.2120431), sfix(-156998788.95664343), sfix(-27672696.633567594), sfix(1.0), sfix(1.0)],
        [sfix(-30371418.63566566), sfix(-179221319.31568453), sfix(-404642984.4796425), sfix(-432963832.458491), sfix(-200994147.05595827), sfix(-11860756.765777567), sfix(12755717.743434157), sfix(1.0), sfix(1.0)],
        [sfix(4492560.783352269), sfix(91366493.81339528), sfix(466587282.77548826), sfix(1054812421.4058051), sfix(1217864798.6194232), sfix(703030971.0616897), sfix(160957009.136017), sfix(1.0), sfix(1.0)],
        [sfix(-1672283.6840296704), sfix(17251024.483505156), sfix(94002034.34236242), sfix(52029362.53933035), sfix(-306493622.2529263), sfix(-538150395.4521765), sfix(-262017773.48270264), sfix(1.0), sfix(1.0)],
        [sfix(-2793742.444949089), sfix(1806170.4943473614), sfix(8840520.301625654), sfix(-181686590.5412869), sfix(-620873454.6839606), sfix(-690931748.3434166), sfix(-238781994.83947757), sfix(1.0), sfix(1.0)],
        [sfix(-2758365.924365226), sfix(3032416.31369456), sfix(26121592.508881673), sfix(-54437668.22724349), sfix(-101399285.05449468), sfix(431622363.51651204), sfix(770687920.6565449), sfix(1.0), sfix(1.0)],
        [sfix(-2758377.378165552), sfix(3029506.8292038133), sfix(26190458.148816414), sfix(-46133502.718491584), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(-2758381.2193531995), sfix(3033343.3322616853), sfix(26016507.406793058), sfix(-53193587.17620715), sfix(-135210693.36435276), sfix(514606517.299832), sfix(-463863460.0375065), sfix(1.0), sfix(1.0)],
        [sfix(-2755937.753332348), sfix(1894405.827631878), sfix(44513093.19786454), sfix(-176785054.44768345), sfix(287315153.97695744), sfix(-226612373.61720493), sfix(71590055.89973831), sfix(1.0), sfix(1.0)],
        [sfix(24402644.66599575), sfix(-194974124.41782588), sfix(623000091.4005271), sfix(-1044240751.4718108), sfix(964392010.252484), sfix(-466195046.56405133), sfix(92232952.60213405), sfix(1.0), sfix(1.0)],
        [sfix(-229737702.25818706), sfix(1340940514.4676561), sfix(-3246735954.198134), sfix(4158335014.919503), sfix(-2971940427.8793564), sfix(1122954557.1619408), sfix(-175198208.29424953), sfix(1.0), sfix(1.0)],
        [sfix(914202479.7666174), sfix(-4381582516.990982), sfix(8689606898.09315), sfix(-9129921034.122665), sfix(5355364929.829578), sfix(-1662265680.135926), sfix(213242932.8166067), sfix(1.0), sfix(1.0)],
        [sfix(-2135382674.949039), sfix(8527333856.571119), sfix(-14090882699.265837), sfix(12322217929.730858), sfix(-6013991526.710971), sfix(1553129372.4805784), sfix(-165857983.52628762), sfix(1.0), sfix(1.0)],
        [sfix(2364207932.592236), sfix(-7871522221.283553), sfix(10802053668.762405), sfix(-7824977133.068334), sfix(3156495785.173874), sfix(-672852505.4279503), sfix(59267439.32663122), sfix(1.0), sfix(1.0)],
        [sfix(1642681907.0206518), sfix(-3940462450.0546813), sfix(3934917010.19366), sfix(-2097003272.514313), sfix(628542167.6879351), sfix(-100466222.97517261), sfix(6690365.287574121), sfix(1.0), sfix(1.0)],
        [sfix(-162939.8607343853), sfix(-808842.5080840043), sfix(-1365416.689312895), sfix(429512.77642155613), sfix(-71893.75699575274), sfix(6322.06681425021), sfix(-231.435471696), sfix(1.0), sfix(1.0)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)]
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
        sfix(-2.5999999046325684),
        sfix(-1.6499998569488525),
        sfix(-1.1749999523162842),
        sfix(-0.6999999284744263),
        sfix(-0.4624999165534973),
        sfix(-0.046874936670064926),
        sfix(0.012500062584877014),
        sfix(0.36875003576278687),
        sfix(0.48750004172325134),
        sfix(0.7250000238418579),
        sfix(0.9625000357627869),
        sfix(1.2000000476837158),
        sfix(1.6750000715255737),
        sfix(2.1500000953674316),
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
        [sfix(38568658.75048948), sfix(108987997.70911913), sfix(117766215.465507), sfix(68007265.76842846), sfix(22279614.913955353), sfix(3911357.207906546), sfix(286550.7628056909), sfix(1.0), sfix(1.0)],
        [sfix(204644583.7664059), sfix(898791935.675547), sfix(1601930604.02802), sfix(1505950696.0350292), sfix(787947548.1618708), sfix(217744125.23268685), sfix(24860550.743658822), sfix(1.0), sfix(1.0)],
        [sfix(6854402.378684406), sfix(100695210.63699718), sfix(388281441.5977569), sfix(722165491.8498726), sfix(698190035.2783062), sfix(339180895.4235554), sfix(65598687.54520197), sfix(1.0), sfix(1.0)],
        [sfix(-3483341.9458621084), sfix(23826737.815537404), sfix(160169197.6735854), sfix(383499751.5259192), sfix(445021263.12518156), sfix(260803531.623284), sfix(63519643.95920128), sfix(1.0), sfix(1.0)],
        [sfix(-4818403.488251135), sfix(3487737.5988373016), sfix(34056307.22797014), sfix(-26065004.59534872), sfix(-291836822.7212963), sfix(-436437166.2965223), sfix(-207621498.49146584), sfix(1.0), sfix(1.0)],
        [sfix(-4815579.150564715), sfix(3635899.947419185), sfix(37143127.49403142), sfix(12520697.857689131), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(-4815803.7884556865), sfix(3668593.9801881425), sfix(35911293.92876843), sfix(20056804.8992882), sfix(-262236158.36112672), sfix(394135291.26366025), sfix(-156157617.51434523), sfix(1.0), sfix(1.0)],
        [sfix(-2539465.318981994), sfix(-31042813.376833383), sfix(254078657.42588612), sfix(-696485254.839177), sfix(1013399762.1839206), sfix(-736003774.5374544), sfix(204022886.66571563), sfix(1.0), sfix(1.0)],
        [sfix(-13572112.875944156), sfix(81375218.24501288), sfix(-214663898.18826956), sfix(320072394.2299205), sfix(-181743346.74672228), sfix(-29532278.034083486), sfix(47784627.45910061), sfix(1.0), sfix(1.0)],
        [sfix(70684851.55263731), sfix(-509544178.0069425), sfix(1464014300.4406512), sfix(-2116602902.532674), sfix(1670950603.5026886), sfix(-683130191.0026073), sfix(112659053.83214206), sfix(1.0), sfix(1.0)],
        [sfix(-287722933.11092204), sfix(1555214648.6955884), sfix(-3464692955.0325828), sfix(4115119242.6712995), sfix(-2723112657.243501), sfix(951298148.1016718), sfix(-137071756.5514497), sfix(1.0), sfix(1.0)],
        [sfix(290473029.7848168), sfix(-1356922351.6126642), sfix(2615217316.4789877), sfix(-2623027742.45699), sfix(1459224204.2591753), sfix(-427574035.76916003), sfix(51608810.17521975), sfix(1.0), sfix(1.0)],
        [sfix(2671062377.31834), sfix(-8534567833.166707), sfix(11317180361.446743), sfix(-7945018216.816478), sfix(3118425492.0330954), sfix(-648934386.8377298), sfix(55953028.32738149), sfix(1.0), sfix(1.0)],
        [sfix(1247693578.7203555), sfix(-2983076012.751223), sfix(2986010817.9931746), sfix(-1587836158.4555414), sfix(475057358.78242576), sfix(-75814656.31651308), sfix(5041666.290175613), sfix(1.0), sfix(1.0)],
        [sfix(694448.9512124407), sfix(3447283.1197261265), sfix(5819399.768674985), sfix(-1830581.5150147274), sfix(306410.8679088112), sfix(-26944.62023515852), sfix(986.37693605628), sfix(1.0), sfix(1.0)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)]
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
        sfix(-2.5999999046325684),
        sfix(-2.125),
        sfix(-1.8874999284744263),
        sfix(-1.7687499523162842),
        sfix(-1.6499998569488525),
        sfix(-1.1749999523162842),
        sfix(-0.9968749284744263),
        sfix(-0.9374999403953552),
        sfix(-0.8187499046325684),
        sfix(-0.6999999284744263),
        sfix(-0.6406249403953552),
        sfix(-0.5218749046325684),
        sfix(-0.4624999165534973),
        sfix(-0.3437499403953552),
        sfix(-0.10624993592500687),
        sfix(-0.046874936670064926),
        sfix(0.012500062584877014),
        sfix(0.2500000596046448),
        sfix(0.48750004172325134),
        sfix(0.6062500476837158),
        sfix(0.7250000238418579),
        sfix(0.9625000357627869),
        sfix(1.2000000476837158),
        sfix(1.6750000715255737),
        sfix(2.1500000953674316),
        sfix(3.0999999046325684)
    ]
    coeffA = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-6616351.856439031), sfix(-16540703.31214277), sfix(-17123936.4795646), sfix(-9449387.869114744), sfix(-2933003.6497098343), sfix(-485428.3392393229), sfix(-33461.72406592237), sfix(1.0), sfix(1.0)],
        [sfix(-234768917.5174205), sfix(-665362956.0172592), sfix(-786633132.745065), sfix(-496627966.41564584), sfix(-176577447.73737133), sfix(-33522084.891612988), sfix(-2654488.897310078), sfix(1.0), sfix(1.0)],
        [sfix(156886105.520424), sfix(589396870.8526855), sfix(888506192.602802), sfix(696221018.484748), sfix(301269413.59013706), sfix(68580708.60684967), sfix(6436743.515719683), sfix(1.0), sfix(1.0)],
        [sfix(544173853.8716123), sfix(1893399297.5403183), sfix(2718262616.9913063), sfix(2065807283.6191008), sfix(878024626.9013803), sfix(198142475.65757993), sfix(18566061.087201856), sfix(1.0), sfix(1.0)],
        [sfix(-551489170.5340673), sfix(-2440001468.216801), sfix(-4425298511.342687), sfix(-4216298464.952954), sfix(-2230009828.172365), sfix(-622012486.4942746), sfix(-71609829.51488678), sfix(1.0), sfix(1.0)],
        [sfix(407194013.3812524), sfix(2299813635.251806), sfix(5334421713.882002), sfix(6497007162.58562), sfix(4382294906.758823), sfix(1553740401.946118), sfix(226578061.34967762), sfix(1.0), sfix(1.0)],
        [sfix(15716638.654041125), sfix(-8089631.088703511), sfix(-338036642.34181833), sfix(-943139721.9000244), sfix(-1110271744.8010993), sfix(-610133578.1380965), sfix(-128843686.96790041), sfix(1.0), sfix(1.0)],
        [sfix(-81265153.11915365), sfix(-627011166.6877546), sfix(-1984327207.971137), sfix(-3279364411.0269227), sfix(-2975729558.121585), sfix(-1404821774.3351934), sfix(-269947955.97390634), sfix(1.0), sfix(1.0)],
        [sfix(-23780082.167108096), sfix(-199806344.6002368), sfix(-660417686.7880223), sfix(-1089457089.379747), sfix(-936547931.469462), sfix(-391334745.6898264), sfix(-59911192.532924645), sfix(1.0), sfix(1.0)],
        [sfix(-732734.1125387625), sfix(-7750652.915250622), sfix(6898851.240725554), sfix(148076057.62573445), sfix(355376990.23399013), sfix(328545764.6844361), sfix(107362184.98254779), sfix(1.0), sfix(1.0)],
        [sfix(4214373.113603611), sfix(38641973.36809385), sfix(188334178.6115856), sfix(526854920.8340475), sfix(800591663.3216528), sfix(607898911.4590088), sfix(180464577.8900634), sfix(1.0), sfix(1.0)],
        [sfix(3226373.0223362227), sfix(27163960.686944272), sfix(132749609.53153941), sfix(383228619.0205531), sfix(591742179.9621607), sfix(445855364.1756717), sfix(128053708.9977447), sfix(1.0), sfix(1.0)],
        [sfix(1636735.2173896874), sfix(5928404.332552883), sfix(14276305.087795721), sfix(29918703.440445717), sfix(-2228770.0423239055), sfix(-87837966.14785378), sfix(-72157406.5990485), sfix(1.0), sfix(1.0)],
        [sfix(1327932.002458024), sfix(1373313.3380492644), sfix(-12350979.816741975), sfix(-45612498.53966976), sfix(-98736067.2859723), sfix(-108712382.5770181), sfix(-30517897.528356194), sfix(1.0), sfix(1.0)],
        [sfix(1334969.2148980328), sfix(1630440.1737610581), sfix(-8518745.528159695), sfix(-15762020.544872975), sfix(29523981.0541187), sfix(179106365.1532036), sfix(230955579.0980043), sfix(1.0), sfix(1.0)],
        [sfix(1334966.4451537034), sfix(1630356.038461711), sfix(-8542208.111321902), sfix(-17265336.116212178), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(1334970.2977297427), sfix(1629443.8322905004), sfix(-8506869.221413093), sfix(-16568955.688106077), sfix(25558332.13951429), sfix(147980513.19129452), sfix(-260710176.5952617), sfix(1.0), sfix(1.0)],
        [sfix(1271650.6541684142), sfix(2345969.364547884), sfix(-8697564.368553812), sfix(-49201317.45098367), sfix(219947764.37331486), sfix(-320258014.0884413), sfix(164937242.13201138), sfix(1.0), sfix(1.0)],
        [sfix(-443077.1776006552), sfix(27263230.96539259), sfix(-158514334.97421604), sfix(428721792.35105556), sfix(-634230755.9017714), sfix(491399380.0860362), sfix(-155590877.02623156), sfix(1.0), sfix(1.0)],
        [sfix(13342194.007170958), sfix(-108119094.39678401), sfix(396411795.5942352), sfix(-786498976.5796876), sfix(865293494.9774842), sfix(-497179492.35663927), sfix(116441731.60359113), sfix(1.0), sfix(1.0)],
        [sfix(-33884655.20708097), sfix(249251357.1952551), sfix(-728656980.42412), sfix(1099292116.1160252), sfix(-909219224.5947673), sfix(391366399.69563067), sfix(-68451991.12261634), sfix(1.0), sfix(1.0)],
        [sfix(154163855.63514602), sfix(-845776124.8931428), sfix(1918942884.4987562), sfix(-2300385053.286788), sfix(1533629114.5375457), sfix(-538846573.7774227), sfix(77968839.29236145), sfix(1.0), sfix(1.0)],
        [sfix(-281858729.11516815), sfix(1273682820.358298), sfix(-2368557138.851014), sfix(2319560766.619401), sfix(-1262909486.7308424), sfix(362720984.28696394), sfix(-42956334.860714905), sfix(1.0), sfix(1.0)],
        [sfix(-1928776053.9902802), sfix(6099708079.213812), sfix(-7993107773.460916), sfix(5554073684.289555), sfix(-2158655694.3331556), sfix(445074728.96194845), sfix(-38046126.68869718), sfix(1.0), sfix(1.0)],
        [sfix(-197407178.30893663), sfix(440776359.3761836), sfix(-409169065.11922365), sfix(202002970.61007446), sfix(-55955833.84831042), sfix(8246164.247908762), sfix(-505101.75603631686), sfix(1.0), sfix(1.0)],
        [sfix(1250.96498111068), sfix(-48973.98120934036), sfix(-52218.0318793195), sfix(16231.29215668422), sfix(-2656.88857181849), sfix(227.28336668669), sfix(-8.06991221736), sfix(1.0), sfix(1.0)]
    ]
    scaler = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)]
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
        sfix(-2.5999999046325684),
        sfix(-1.6499998569488525),
        sfix(-1.1749999523162842),
        sfix(-0.6999999284744263),
        sfix(-0.4624999165534973),
        sfix(-0.10624993592500687),
        sfix(-0.046874936670064926),
        sfix(0.012500062584877014),
        sfix(0.2500000596046448),
        sfix(0.36875003576278687),
        sfix(0.7250000238418579),
        sfix(1.2000000476837158),
        sfix(1.6750000715255737),
        sfix(2.1500000953674316),
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
        [sfix(22390874.54935408), sfix(66968977.81135491), sfix(70981152.24009156), sfix(40315808.40806905), sfix(13110535.672519427), sfix(2298840.2137011006), sfix(168752.8662890713), sfix(1.0), sfix(1.0)],
        [sfix(48817651.11038366), sfix(242768662.71849647), sfix(464312725.6671542), sfix(466468089.4303326), sfix(258971348.01478222), sfix(75337712.78064096), sfix(8992522.097011011), sfix(1.0), sfix(1.0)],
        [sfix(-40913358.12652528), sfix(-232955801.06957054), sfix(-579486805.634027), sfix(-747599662.5414654), sfix(-530914514.4867004), sfix(-197298718.56613725), sfix(-30014852.96247031), sfix(1.0), sfix(1.0)],
        [sfix(2187214.6553510195), sfix(98776701.6635289), sfix(489344305.64523625), sfix(1098974179.9826581), sfix(1274522812.611455), sfix(750477061.9983444), sfix(178800655.8236502), sfix(1.0), sfix(1.0)],
        [sfix(-4785376.15462119), sfix(9940552.72226873), sfix(16189432.239191221), sfix(-246894782.95363012), sfix(-876358065.1408685), sfix(-1074809671.4906745), sfix(-461181522.426245), sfix(1.0), sfix(1.0)],
        [sfix(-4725222.948050174), sfix(11939301.31905744), sfix(43094524.69857893), sfix(-57947021.62932063), sfix(-139498162.98938248), sfix(454750246.42190784), sfix(873544103.0916734), sfix(1.0), sfix(1.0)],
        [sfix(-4725235.913695957), sfix(11935723.042561525), sfix(43190635.28931837), sfix(-46945826.208448626), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(-4725242.070823379), sfix(11940853.83306939), sfix(42960645.5554053), sfix(-56072908.140930526), sfix(-179728653.51860955), sfix(572032257.6602), sfix(-471102234.95792973), sfix(1.0), sfix(1.0)],
        [sfix(-4615682.760611031), sfix(9411085.335114824), sfix(67602743.4029038), sfix(-185814458.48056614), sfix(209898645.84116557), sfix(-60792219.663195245), sfix(-37030935.36339929), sfix(1.0), sfix(1.0)],
        [sfix(-5139435.568710233), sfix(14157733.877055878), sfix(55851273.949880235), sfix(-202155897.49151725), sfix(338592270.38354135), sfix(-283572544.8657651), sfix(94290624.72029506), sfix(1.0), sfix(1.0)],
        [sfix(32421401.567690287), sfix(-238772754.6463246), sfix(732017267.7600825), sfix(-1086921376.9373827), sfix(879090485.4119096), sfix(-369906957.7036196), sfix(63524986.60595811), sfix(1.0), sfix(1.0)],
        [sfix(361922889.4253721), sfix(-1527469016.2216618), sfix(2700634923.113743), sfix(-2505991776.302343), sfix(1298446128.972665), sfix(-356544147.8237896), sfix(40568213.51489872), sfix(1.0), sfix(1.0)],
        [sfix(2936245912.2944703), sfix(-9363831203.64266), sfix(12410589681.343956), sfix(-8714708805.043716), sfix(3422827816.6660123), sfix(-712901067.2875135), sfix(61525610.05362452), sfix(1.0), sfix(1.0)],
        [sfix(1598719744.0159717), sfix(-3825479189.2706285), sfix(3830385285.8786983), sfix(-2038318604.970753), sfix(610260191.4763725), sfix(-97457486.36373103), sfix(6485204.314144731), sfix(1.0), sfix(1.0)],
        [sfix(793426.3515928419), sfix(3938612.425737028), sfix(6648818.633139765), sfix(-2091487.9489889494), sfix(350082.5461285992), sfix(-30784.94350021702), sfix(1126.96181952157), sfix(1.0), sfix(1.0)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)]
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
        sfix(-2.5999999046325684),
        sfix(-1.6499998569488525),
        sfix(-1.1749999523162842),
        sfix(-0.6999999284744263),
        sfix(-0.22499993443489075),
        sfix(-0.10624993592500687),
        sfix(-0.046874936670064926),
        sfix(0.012500062584877014),
        sfix(0.2500000596046448),
        sfix(0.48750004172325134),
        sfix(0.7250000238418579),
        sfix(1.2000000476837158),
        sfix(1.6750000715255737),
        sfix(2.1500000953674316),
        sfix(3.0999999046325684)
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
        [sfix(32588696.63309846), sfix(89079908.77210154), sfix(98491297.05781311), sfix(58042375.94257706), sfix(19264919.1530937), sfix(3410012.366915215), sfix(251205.5377729767), sfix(1.0), sfix(1.0)],
        [sfix(109992852.47023037), sfix(509435049.4240267), sfix(955035717.1516297), sfix(936348807.5869637), sfix(507619277.7183659), sfix(144642884.9076904), sfix(16964842.44917983), sfix(1.0), sfix(1.0)],
        [sfix(-19924187.003457908), sfix(-127287241.27287644), sfix(-326936623.28943), sfix(-416603314.50662297), sfix(-277919872.21329266), sfix(-91417688.56054316), sfix(-11337670.126499955), sfix(1.0), sfix(1.0)],
        [sfix(611065.3560881923), sfix(2438379.4161035684), sfix(-14590114.695856871), sfix(-88271755.72344682), sfix(-195989045.81364235), sfix(-193421794.51604876), sfix(-70622525.35273536), sfix(1.0), sfix(1.0)],
        [sfix(716499.6352616985), sfix(4466203.8199676275), sfix(1712752.4437954193), sfix(-17640365.13267479), sfix(-20527303.19578075), sfix(45894967.045493804), sfix(70746357.87831897), sfix(1.0), sfix(1.0)],
        [sfix(716608.2738872548), sfix(4470906.183583164), sfix(1796965.710915408), sfix(-16841813.646563135), sfix(-16301942.013320327), sfix(57699990.82471678), sfix(84292321.78578173), sfix(1.0), sfix(1.0)],
        [sfix(716607.0881832755), sfix(4470522.450101554), sfix(1809990.9901031188), sfix(-15518558.339030288), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(716603.1945557822), sfix(4471591.978750732), sfix(1760875.899639452), sfix(-16151271.971805826), sfix(-24312074.641889624), sfix(92703861.59146291), sfix(-45278088.42193034), sfix(1.0), sfix(1.0)],
        [sfix(843832.0108073357), sfix(2127762.1617013956), sfix(19332370.271037463), sfix(-83661430.19620521), sfix(110756872.46680103), sfix(-27149539.32773258), sfix(-25667569.828942537), sfix(1.0), sfix(1.0)],
        [sfix(-2224840.0828397386), sfix(31225676.02869684), sfix(-87711318.43490864), sfix(98176974.70131162), sfix(-2335171.4505718905), sfix(-70114942.96816732), sfix(35885709.06647669), sfix(1.0), sfix(1.0)],
        [sfix(28531743.450325754), sfix(-173302247.76110438), sfix(456687374.59094685), sfix(-624715601.5674472), sfix(472104499.7142838), sfix(-187159038.32906872), sfix(30518683.465513397), sfix(1.0), sfix(1.0)],
        [sfix(159933214.2276554), sfix(-683646622.8789874), sfix(1227758129.2105846), sfix(-1168910933.4040718), sfix(622686158.0178715), sfix(-175540701.7364811), sfix(20432614.73814745), sfix(1.0), sfix(1.0)],
        [sfix(1136590410.1781871), sfix(-3553186579.953564), sfix(4607954103.478626), sfix(-3167557986.470612), sfix(1218675187.8241842), sfix(-248884789.13782203), sfix(21085891.697686), sfix(1.0), sfix(1.0)],
        [sfix(87918253.80617258), sfix(-194875588.32860452), sfix(183245885.2025301), sfix(-90158332.31262226), sfix(24913828.309337307), sfix(-3665828.5106471605), sfix(224322.98264969513), sfix(1.0), sfix(1.0)],
        [sfix(-32744.47305229586), sfix(1281912.1507639766), sfix(1366826.3822284504), sfix(-424860.1017515721), sfix(69545.04534063337), sfix(-5949.22655364827), sfix(211.23295008157), sfix(1.0), sfix(1.0)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)]
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
        sfix(-2.5999999046325684),
        sfix(-1.6499998569488525),
        sfix(-1.1749999523162842),
        sfix(-0.6999999284744263),
        sfix(-0.22499993443489075),
        sfix(-0.10624993592500687),
        sfix(-0.017187437042593956),
        sfix(0.012500062584877014),
        sfix(0.2500000596046448),
        sfix(0.48750004172325134),
        sfix(0.7250000238418579),
        sfix(0.9625000357627869),
        sfix(1.4375),
        sfix(1.6750000715255737),
        sfix(1.9125001430511475),
        sfix(2.1500000953674316),
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
        [sfix(60117121.088743605), sfix(164074768.46188074), sfix(181175547.10911402), sfix(106635864.93296091), sfix(35350787.19848083), sfix(6250070.783137151), sfix(459918.93115838256), sfix(1.0), sfix(1.0)],
        [sfix(232788524.17305493), sfix(1045029442.1131159), sfix(1911840911.7657714), sfix(1837296239.5964541), sfix(979560330.3393418), sfix(275187197.5762213), sfix(31882052.0332305), sfix(1.0), sfix(1.0)],
        [sfix(1378872.9292397276), sfix(41792103.10611602), sfix(196575021.44292295), sfix(416687544.81463295), sfix(443879365.1972603), sfix(232568033.0098488), sfix(47767765.86001874), sfix(1.0), sfix(1.0)],
        [sfix(847537.8915321254), sfix(9908768.704850549), sfix(-3841870.835324377), sfix(-115562987.64084779), sfix(-279269979.289067), sfix(-267166414.72504812), sfix(-92538275.66537042), sfix(1.0), sfix(1.0)],
        [sfix(847459.7306453068), sfix(10409734.625836547), sfix(5039331.169049608), sfix(-52130538.48462445), sfix(-49704332.190753035), sfix(156176146.7756375), sfix(227230994.09770238), sfix(1.0), sfix(1.0)],
        [sfix(847960.3171547803), sfix(10431069.133856976), sfix(5411882.014148966), sfix(-48748476.90105554), sfix(-33186267.4877289), sfix(195487209.05820933), sfix(258026362.91547087), sfix(1.0), sfix(1.0)],
        [sfix(847960.4910898906), sfix(10430983.349940794), sfix(5400497.2121363), sfix(-48459393.84131628), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(847952.7007618548), sfix(10432155.23720888), sfix(5353169.253778072), sfix(-47610335.73222779), sfix(-49147915.10752754), sfix(259033430.91989943), sfix(-193202665.9790494), sfix(1.0), sfix(1.0)],
        [sfix(1018300.1065777461), sfix(7140200.316547526), sfix(31786007.977389082), sfix(-160322331.02589568), sfix(218976035.3798461), sfix(-75396687.27975133), sfix(-25485550.814353522), sfix(1.0), sfix(1.0)],
        [sfix(-223538.5983712997), sfix(16208242.639622282), sfix(16280790.791931212), sfix(-201732884.89183816), sfix(412410826.139209), sfix(-343076033.61829764), sfix(104802945.30467674), sfix(1.0), sfix(1.0)],
        [sfix(-16332480.822441716), sfix(157155634.01462722), sfix(-499155425.2869257), sfix(806498897.9194057), sfix(-699980125.999308), sfix(313152485.77028286), sfix(-56874993.86469683), sfix(1.0), sfix(1.0)],
        [sfix(86900554.08747791), sfix(-438159723.5459756), sfix(935692723.9529849), sfix(-1044273070.2958609), sfix(647912111.4846392), sfix(-212531327.9957666), sfix(28922735.19993282), sfix(1.0), sfix(1.0)],
        [sfix(232385095.75046006), sfix(-688170921.0798937), sfix(752545753.9711097), sfix(-302939220.0424268), sfix(-36849599.984951705), sfix(61081079.47541365), sfix(-12473362.622506151), sfix(1.0), sfix(1.0)],
        [sfix(-873817508.3403966), sfix(2173185702.3570747), sfix(-1887347680.6335423), sfix(508640500.2069335), sfix(174384099.27658924), sfix(-126086879.01401661), sfix(19724147.64275501), sfix(1.0), sfix(1.0)],
        [sfix(610071212.8090855), sfix(-656825686.270726), sfix(-575285381.8386091), sfix(1260959947.8518069), sfix(-776163765.2921212), sfix(210345188.15601557), sfix(-21646685.397278193), sfix(1.0), sfix(1.0)],
        [sfix(-2313199926.3204007), sfix(5537751188.064516), sfix(-5516306380.459762), sfix(2933497918.573093), sfix(-877358172.7845855), sfix(139927816.4473794), sfix(-9297482.348780915), sfix(1.0), sfix(1.0)],
        [sfix(346372.63188307884), sfix(1719412.960200448), sfix(2902561.53488992), sfix(-913045.2801289661), sfix(152829.57597379733), sfix(-13439.25857928438), sfix(491.97853169455), sfix(1.0), sfix(1.0)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)]
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
        sfix(-2.5999999046325684),
        sfix(-2.125),
        sfix(-1.8874999284744263),
        sfix(-1.6499998569488525),
        sfix(-1.4124999046325684),
        sfix(-1.1749999523162842),
        sfix(-0.9374999403953552),
        sfix(-0.6999999284744263),
        sfix(-0.4624999165534973),
        sfix(-0.3437499403953552),
        sfix(-0.22499993443489075),
        sfix(-0.10624993592500687),
        sfix(0.012500062584877014),
        sfix(0.2500000596046448),
        sfix(0.48750004172325134),
        sfix(0.7250000238418579),
        sfix(1.2000000476837158),
        sfix(1.6750000715255737),
        sfix(2.1500000953674316)
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
        [sfix(5175283.676528981), sfix(10857374.894815048), sfix(12201319.032591129), sfix(7236926.64764114), sfix(2341595.83240949), sfix(396159.40516453265), sfix(27617.46915783779), sfix(1.0), sfix(1.0)],
        [sfix(192645625.0195094), sfix(544039459.307241), sfix(644621207.7079005), sfix(407661795.9458222), sfix(145077797.26042852), sfix(27554855.865595747), sfix(2182497.678278684), sfix(1.0), sfix(1.0)],
        [sfix(-334303780.18864554), sfix(-1169487960.9188726), sfix(-1677735884.9778588), sfix(-1271492637.2043974), sfix(-538043048.3548019), sfix(-120704970.47243534), sfix(-11228341.654214617), sfix(1.0), sfix(1.0)],
        [sfix(-141714554.62247387), sfix(-400794147.2445127), sfix(-407245385.6609346), sfix(-157401882.69381112), sfix(9050385.515782144), sfix(22033803.167785414), sfix(4237508.761189183), sfix(1.0), sfix(1.0)],
        [sfix(463031754.87139374), sfix(2042657413.9120076), sfix(3695864623.2457542), sfix(3506428861.411416), sfix(1842982995.922171), sfix(509649707.2484952), sfix(58001999.23451006), sfix(1.0), sfix(1.0)],
        [sfix(-245741465.13031286), sfix(-1407963519.1020677), sfix(-3294179092.570673), sfix(-4033434627.180083), sfix(-2723192451.909587), sfix(-961926831.9772822), sfix(-139093818.1402592), sfix(1.0), sfix(1.0)],
        [sfix(39442254.34095934), sfix(320826673.2462066), sfix(1071238105.8915473), sfix(1843346680.4022667), sfix(1724676553.5783007), sfix(832279536.5793811), sfix(162213944.24660036), sfix(1.0), sfix(1.0)],
        [sfix(-2186372.4739040523), sfix(-23345447.95270896), sfix(-120127418.44282134), sfix(-367514076.72203815), sfix(-595828628.0662994), sfix(-474179667.1592643), sfix(-146086976.74419194), sfix(1.0), sfix(1.0)],
        [sfix(-1299489.093312056), sfix(-10416331.037819346), sfix(-42984131.62332767), sfix(-125150264.01094252), sfix(-171485747.47672564), sfix(-80622378.93429361), sfix(5245836.779683866), sfix(1.0), sfix(1.0)],
        [sfix(-915909.6078162288), sfix(-4143915.2809489407), sfix(-134433.3079185007), sfix(31434935.858191498), sfix(151451035.8796372), sfix(275890488.04537565), sfix(169896011.1823462), sfix(1.0), sfix(1.0)],
        [sfix(-927658.7222231108), sfix(-4465599.063313364), sfix(-3845651.568231729), sfix(8340677.974563392), sfix(69714790.87268077), sfix(119971095.94828284), sfix(44749776.04025448), sfix(1.0), sfix(1.0)],
        [sfix(-928156.4347076814), sfix(-4490689.5968396915), sfix(-4619202.295325725), sfix(-3238703.6918039904), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(-928206.1896262326), sfix(-4492049.911229224), sfix(-4266934.584000276), sfix(2131440.1629149267), sfix(50814955.35466068), sfix(-41097429.25969596), sfix(-65838511.11887879), sfix(1.0), sfix(1.0)],
        [sfix(-1070284.527877125), sfix(-2066099.098056139), sfix(-20226956.21703603), sfix(48932872.350382246), sfix(14061135.719273603), sfix(-140237330.69174388), sfix(107035327.4826505), sfix(1.0), sfix(1.0)],
        [sfix(2001163.3868157251), sfix(-28321488.59724225), sfix(57568482.514736935), sfix(-12309142.774724983), sfix(-122672746.08269888), sfix(162897020.85295165), sfix(-63490090.1336738), sfix(1.0), sfix(1.0)],
        [sfix(-33788760.18155722), sfix(205046117.9733138), sfix(-544718510.8461748), sfix(744440716.631057), sfix(-559995945.1308733), sfix(220780086.22860688), sfix(-35774708.61661947), sfix(1.0), sfix(1.0)],
        [sfix(45483288.28220929), sfix(-226323898.74270496), sfix(434881650.55673623), sfix(-443672636.1354425), sfix(251575836.44726726), sfix(-75195313.16084391), sfix(9240225.24908272), sfix(1.0), sfix(1.0)],
        [sfix(617432303.2236999), sfix(-1942833856.6610754), sfix(2513441550.0198674), sfix(-1721959556.1656592), sfix(658617759.0286232), sfix(-133521282.83477212), sfix(11220288.496566093), sfix(1.0), sfix(1.0)],
        [sfix(-219278.28550079756), sfix(-1188013.7046399016), sfix(-1939024.4187092115), sfix(608616.2333815773), sfix(-101567.0070853944), sfix(8900.20585739643), sfix(-324.58387602878), sfix(1.0), sfix(1.0)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)]
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
        sfix(-2.5999999046325684),
        sfix(-2.125),
        sfix(-1.6499998569488525),
        sfix(-1.4124999046325684),
        sfix(-1.1749999523162842),
        sfix(-0.9374999403953552),
        sfix(-0.6999999284744263),
        sfix(-0.4624999165534973),
        sfix(-0.22499993443489075),
        sfix(-0.046874936670064926),
        sfix(0.012500062584877014),
        sfix(0.2500000596046448),
        sfix(0.48750004172325134),
        sfix(0.7250000238418579),
        sfix(0.9031250476837158),
        sfix(0.9625000357627869),
        sfix(1.4375),
        sfix(1.6750000715255737),
        sfix(1.9125001430511475),
        sfix(2.1500000953674316),
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
        [sfix(-773826.2291573149), sfix(-2543010.8921947856), sfix(-2351636.2453519995), sfix(-1150324.048114825), sfix(-329177.7772314106), sfix(-51962.55791780959), sfix(-3491.48432790865), sfix(1.0), sfix(1.0)],
        [sfix(-9698908.156752743), sfix(-23168135.345709972), sfix(-20775059.99083363), sfix(-8732458.912771353), sfix(-1482016.0179749674), sfix(41999.95011538242), sfix(30315.6318978045), sfix(1.0), sfix(1.0)],
        [sfix(48408737.20690968), sfix(168901489.66008976), sfix(242369288.48103908), sfix(182326310.85152304), sfix(75941287.45424901), sfix(16612794.129255792), sfix(1489853.3026891341), sfix(1.0), sfix(1.0)],
        [sfix(-58490538.06843334), sfix(-275497131.05557853), sfix(-527587700.1529374), sfix(-529309035.6080662), sfix(-294108462.43099153), sfix(-86032702.1962048), sfix(-10375350.865794811), sfix(1.0), sfix(1.0)],
        [sfix(19602680.08376307), sfix(118531526.37944378), sfix(302071062.3764139), sfix(403845678.5283648), sfix(297218161.65085983), sfix(114141613.73119868), sfix(17905700.36708572), sfix(1.0), sfix(1.0)],
        [sfix(9016044.04533231), sfix(45925026.18479606), sfix(94770433.43412802), sfix(88392213.2344658), sfix(27334127.186765034), sfix(-8959248.397885283), sfix(-5483899.588724669), sfix(1.0), sfix(1.0)],
        [sfix(-650663.8007325354), sfix(-34560222.53177581), sfix(-185817420.69337818), sfix(-435991990.18145686), sfix(-526862758.45447165), sfix(-323043020.7401466), sfix(-80062407.52180326), sfix(1.0), sfix(1.0)],
        [sfix(2171980.5588327153), sfix(2235908.164238965), sfix(15803599.704618018), sfix(158466432.94375026), sfix(467782988.1991957), sfix(572256406.7129023), sfix(258516857.8995398), sfix(1.0), sfix(1.0)],
        [sfix(2085076.2595973595), sfix(64653.6558340991), sfix(-7196076.750617646), sfix(25862099.746761374), sfix(27813334.51157794), sfix(-225556301.8064346), sfix(-359461946.2130175), sfix(1.0), sfix(1.0)],
        [sfix(2085035.4682639088), sfix(62637.38439869435), sfix(-7289491.4364845315), sfix(22628503.490559313), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(2085037.9461506903), sfix(61283.07791794193), sfix(-7223928.358896267), sfix(24342028.99670856), sfix(38719642.852624215), sfix(-283758881.2295195), sfix(312139109.24914765), sfix(1.0), sfix(1.0)],
        [sfix(1894601.1178079261), sfix(4025180.1969302017), sfix(-42194297.45095798), sfix(192586070.0466936), sfix(-429245493.42704695), sfix(432891651.9105578), sfix(-161226383.46000823), sfix(1.0), sfix(1.0)],
        [sfix(9640715.804038288), sfix(-80097949.95306444), sfix(337243882.1892594), sfix(-716233689.6912539), sfix(787853786.0401102), sfix(-429085492.49091303), sfix(90066443.20536591), sfix(1.0), sfix(1.0)],
        [sfix(-29990787.440387614), sfix(211372136.15650797), sfix(-542333231.1134859), sfix(669925077.2744703), sfix(-404448998.70936066), sfix(93314398.86848682), sfix(1794560.8442292213), sfix(1.0), sfix(1.0)],
        [sfix(-112022798.51482439), sfix(784227472.0237722), sfix(-2209974171.959103), sfix(3260220570.064007), sfix(-2668532144.4572015), sfix(1149138184.2328756), sfix(-203425733.22761625), sfix(1.0), sfix(1.0)],
        [sfix(365662066.38047373), sfix(-1925337184.4139314), sfix(4200969720.7503786), sfix(-4839980612.313106), sfix(3096751886.268951), sfix(-1042891803.2167084), sfix(144457328.2598605), sfix(1.0), sfix(1.0)],
        [sfix(-988660595.2921939), sfix(4641477440.175148), sfix(-8813394153.913513), sfix(8716680291.819061), sfix(-4756550587.607288), sfix(1361412854.6667516), sfix(-159973469.7607813), sfix(1.0), sfix(1.0)],
        [sfix(1685764637.8591678), sfix(-7071403308.924452), sfix(11853254813.544247), sfix(-10274190587.23857), sfix(4887764738.603411), sfix(-1215443041.0332751), sfix(123832576.76097691), sfix(1.0), sfix(1.0)],
        [sfix(-1700517530.8267868), sfix(6370218631.128392), sfix(-9422476533.081741), sfix(7159295045.707689), sfix(-2976876196.8387837), sfix(646380283.6972735), sfix(-57511436.96508524), sfix(1.0), sfix(1.0)],
        [sfix(-2099398532.3323581), sfix(5009471273.571394), sfix(-4981536103.145925), sfix(2641107820.370985), sfix(-787577216.8642609), sfix(125243963.18405378), sfix(-8297800.655183477), sfix(1.0), sfix(1.0)],
        [sfix(-70872.68810383425), sfix(-351815.95552405383), sfix(-593904.7125331355), sfix(186821.84274339565), sfix(-31271.07015442228), sfix(2749.86039304008), sfix(-100.66569301785), sfix(1.0), sfix(1.0)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)]
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
        sfix(-2.5999999046325684),
        sfix(-2.125),
        sfix(-1.8874999284744263),
        sfix(-1.6499998569488525),
        sfix(-1.4124999046325684),
        sfix(-1.1749999523162842),
        sfix(-0.9374999403953552),
        sfix(-0.8187499046325684),
        sfix(-0.6999999284744263),
        sfix(-0.4624999165534973),
        sfix(-0.22499993443489075),
        sfix(-0.046874936670064926),
        sfix(0.012500062584877014),
        sfix(0.2500000596046448),
        sfix(0.48750004172325134),
        sfix(0.5468750596046448),
        sfix(0.6062500476837158),
        sfix(0.7250000238418579),
        sfix(1.2000000476837158),
        sfix(1.4375),
        sfix(1.6750000715255737),
        sfix(1.9125001430511475),
        sfix(2.1500000953674316),
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
        [sfix(-2154630.9299688814), sfix(-5766833.310406158), sfix(-5794436.337886615), sfix(-3105357.307083355), sfix(-946442.8115618785), sfix(-155066.07267979687), sfix(-10632.46552394458), sfix(1.0), sfix(1.0)],
        [sfix(-64097078.32351864), sfix(-181414049.18826982), sfix(-213527121.08884457), sfix(-134258458.21613085), sfix(-47566764.6883145), sfix(-9001326.23683861), sfix(-710651.9041925004), sfix(1.0), sfix(1.0)],
        [sfix(203378133.88017455), sfix(684337194.9605302), sfix(954555013.9405302), sfix(706615172.0755603), sfix(293065106.18128264), sfix(64620974.91950017), sfix(5922029.349236999), sfix(1.0), sfix(1.0)],
        [sfix(-82469035.53895001), sfix(-388432611.57343316), sfix(-723204454.1182846), sfix(-693025154.7786617), sfix(-363825415.05136585), sfix(-99830320.61510034), sfix(-11234938.55361433), sfix(1.0), sfix(1.0)],
        [sfix(-169522584.9383219), sfix(-679670287.6198044), sfix(-1097310978.7224207), sfix(-910219271.2170106), sfix(-405470452.43633), sfix(-90287748.17110388), sfix(-7530227.525271175), sfix(1.0), sfix(1.0)],
        [sfix(185253950.03976965), sfix(993937112.2325395), sfix(2171240561.4193068), sfix(2467637729.656184), sfix(1538994239.9134784), sfix(499323639.1068692), sfix(65770505.5410667), sfix(1.0), sfix(1.0)],
        [sfix(-63923074.81746815), sfix(-514403022.60229766), sfix(-1634296651.6240692), sfix(-2654861496.5077376), sfix(-2341030595.623439), sfix(-1068738500.0106082), sfix(-198391918.00090474), sfix(1.0), sfix(1.0)],
        [sfix(-3184292.771415141), sfix(-66681521.37029417), sfix(-257845432.4154335), sfix(-395782047.56885064), sfix(-253466646.7864545), sfix(-38928596.68498292), sfix(13477255.457991919), sfix(1.0), sfix(1.0)],
        [sfix(1703324.6125700776), sfix(-34647533.53169903), sfix(-180352866.3631179), sfix(-322221657.62208956), sfix(-258542842.60679984), sfix(-92710841.95517452), sfix(-12229353.66718664), sfix(1.0), sfix(1.0)],
        [sfix(3968685.2951892437), sfix(-2138253.6591658243), sfix(12931375.928993186), sfix(288561764.16846496), sfix(825178484.4400053), sfix(932200662.476735), sfix(391749283.51937836), sfix(1.0), sfix(1.0)],
        [sfix(3818497.3813629183), sfix(-5850726.390446031), sfix(-26009961.40277598), sfix(65999573.81064893), sfix(92246086.91163947), sfix(-388723032.6059613), sfix(-626555312.6540927), sfix(1.0), sfix(1.0)],
        [sfix(3818428.6191190854), sfix(-5853507.9695339), sfix(-26204092.31714385), sfix(57342799.81875457), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(3818433.910527323), sfix(-5857036.8859561), sfix(-26041686.715968598), sfix(62892587.62070752), sfix(113013202.80672719), sfix(-512509598.47890264), sfix(468504139.4711362), sfix(1.0), sfix(1.0)],
        [sfix(3539610.0844092625), sfix(-133822.4309849817), sfix(-75676564.52612719), sfix(296717581.5085945), sfix(-520858840.8197015), sfix(428698390.53526366), sfix(-131155218.15108985), sfix(1.0), sfix(1.0)],
        [sfix(3611606.1772532635), sfix(520505.209070561), sfix(-88219842.79986006), sfix(360268989.3111616), sfix(-670973037.7326872), sfix(601774866.3541287), sfix(-210117044.2409161), sfix(1.0), sfix(1.0)],
        [sfix(7468961.256688569), sfix(-41412209.167179726), sfix(101832516.25781372), sfix(-99420923.44188587), sfix(-45143441.27758024), sfix(147073050.5655366), sfix(-72373814.03844775), sfix(1.0), sfix(1.0)],
        [sfix(21203306.714361887), sfix(-174847241.78983197), sfix(642547625.1887591), sfix(-1269244741.0918093), sfix(1379988498.4512882), sfix(-779869881.4045943), sfix(179108580.30135772), sfix(1.0), sfix(1.0)],
        [sfix(-70682663.19909249), sfix(499321477.86866754), sfix(-1416672250.4869547), sfix(2082113166.5120401), sfix(-1684676086.8272848), sfix(712830604.5203365), sfix(-123339644.06431955), sfix(1.0), sfix(1.0)],
        [sfix(365238065.29847676), sfix(-1964272792.767178), sfix(4327165355.392461), sfix(-5005220621.012612), sfix(3204690343.28505), sfix(-1077498275.1610851), sfix(148764947.6044228), sfix(1.0), sfix(1.0)],
        [sfix(-1390412264.5847347), sfix(6220897088.252306), sfix(-11393427410.635118), sfix(10951752199.221664), sfix(-5838528772.657834), sfix(1639048566.1827831), sfix(-189498823.8136878), sfix(1.0), sfix(1.0)],
        [sfix(1937750275.733918), sfix(-7930341647.6030245), sfix(13059162793.709583), sfix(-11171574688.501951), sfix(5262561613.15614), sfix(-1298889849.533079), sfix(131576176.06062078), sfix(1.0), sfix(1.0)],
        [sfix(-1625383961.5661962), sfix(6167389077.179647), sfix(-9207516513.745377), sfix(7046421568.766399), sfix(-2946783415.5723033), sfix(642854711.3401155), sfix(-57422101.17779524), sfix(1.0), sfix(1.0)],
        [sfix(-2335038998.9052024), sfix(5576071370.8672285), sfix(-5548663935.347307), sfix(2944063835.950571), sfix(-878600019.1947305), sfix(139827770.0776895), sfix(-9271298.46598715), sfix(1.0), sfix(1.0)],
        [sfix(-46129.66963968238), sfix(-228990.23921935), sfix(-386561.15522644954), sfix(121598.74442547874), sfix(-20353.73814848886), sfix(1789.83124365186), sfix(-65.5213635511), sfix(1.0), sfix(1.0)]
    ]
    scaler = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)]
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
        sfix(-2.5999999046325684),
        sfix(-2.125),
        sfix(-1.6499998569488525),
        sfix(-1.1749999523162842),
        sfix(-0.9374999403953552),
        sfix(-0.6999999284744263),
        sfix(-0.4624999165534973),
        sfix(-0.22499993443489075),
        sfix(-0.017187437042593956),
        sfix(0.012500062584877014),
        sfix(0.1312500536441803),
        sfix(0.48750004172325134),
        sfix(0.7250000238418579),
        sfix(1.2000000476837158),
        sfix(1.6750000715255737),
        sfix(2.1500000953674316),
        sfix(3.0999999046325684)
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
        [sfix(30485.10482203985), sfix(-2378028.091196005), sfix(-1328271.91841236), sfix(-138568.33540775752), sfix(69415.70473053456), sfix(21646.25151049138), sfix(1856.85645755914), sfix(1.0), sfix(1.0)],
        [sfix(-23664177.135531355), sfix(-76850513.27166453), sfix(-98555700.81964053), sfix(-67650615.1211382), sfix(-26234134.400892857), sfix(-5431686.9643247), sfix(-468249.7939446534), sfix(1.0), sfix(1.0)],
        [sfix(72908912.66765226), sfix(291412726.4767614), sfix(484513885.7340352), sfix(423190297.6189891), sfix(205557694.83253163), sfix(52804977.70837386), sfix(5614944.570611696), sfix(1.0), sfix(1.0)],
        [sfix(-50062659.46372674), sfix(-255704105.49585816), sfix(-513064240.1166533), sfix(-525115679.5936516), sfix(-285242198.8522695), sfix(-76038761.48223409), sfix(-7315677.8966119895), sfix(1.0), sfix(1.0)],
        [sfix(22382725.134498343), sfix(158991557.261828), sfix(464520729.80458784), sfix(685240349.1270763), sfix(540369471.5035521), sfix(215637787.17561173), sfix(33770263.42928959), sfix(1.0), sfix(1.0)],
        [sfix(-2215428.9918291247), sfix(-35509468.575794876), sfix(-175990545.1810225), sfix(-438979100.9809993), sfix(-568589299.4664537), sfix(-367080538.23992527), sfix(-93606753.3477409), sfix(1.0), sfix(1.0)],
        [sfix(222739.94027171447), sfix(-4823537.518235577), sfix(-13268455.082460392), sfix(26722867.985584676), sfix(190417614.46206403), sfix(300953625.57481587), sfix(154407613.45472398), sfix(1.0), sfix(1.0)],
        [sfix(223472.43332239857), sfix(-4927206.046268617), sfix(-15630640.469608136), sfix(5922917.095731852), sfix(97707465.64980638), sfix(89732177.12298767), sfix(-42836310.26981438), sfix(1.0), sfix(1.0)],
        [sfix(223462.78998509195), sfix(-4928216.752571298), sfix(-15660419.539215546), sfix(4059783.712730178), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(223463.79659706785), sfix(-4928339.814926288), sfix(-15680161.77576859), sfix(4826804.212791509), sfix(86538921.60146186), sfix(21354712.827588752), sfix(-263436336.22523797), sfix(1.0), sfix(1.0)],
        [sfix(247603.97509026833), sfix(-5684004.401523447), sfix(-5845766.917300513), sfix(-63803859.51363481), sfix(360217049.3810229), sfix(-577763264.4292095), sfix(307924206.2324666), sfix(1.0), sfix(1.0)],
        [sfix(-1388144.5271925516), sfix(22061142.043143213), sfix(-189561028.98772198), sfix(561608747.4772813), sfix(-811172092.3388), sfix(576306554.8584619), sfix(-161676403.52500013), sfix(1.0), sfix(1.0)],
        [sfix(19113002.839661006), sfix(-166578464.13075814), sfix(521268338.90976745), sfix(-850305627.8440276), sfix(753980159.4000889), sfix(-344322267.041501), sfix(63261074.54003176), sfix(1.0), sfix(1.0)],
        [sfix(212922409.4616096), sfix(-807511141.3935208), sfix(1193637024.1130579), sfix(-876032800.2028351), sfix(323894710.61024123), sfix(-52186094.40728225), sfix(1791340.8637272757), sfix(1.0), sfix(1.0)],
        [sfix(-1606383768.0539472), sfix(5061847712.717423), sfix(-6598928632.303438), sfix(4551816054.017948), sfix(-1755369237.7252235), sfix(359101001.38365257), sfix(-30464535.9585051), sfix(1.0), sfix(1.0)],
        [sfix(-71836339.22493076), sfix(158207260.98301336), sfix(-150355747.57023177), sfix(73749615.82002187), sfix(-20333975.020952858), sfix(2987463.365773441), sfix(-182628.07536748567), sfix(1.0), sfix(1.0)],
        [sfix(48875.66915948499), sfix(-1913431.7427135217), sfix(-2040178.0144386897), sfix(634162.6486538826), sfix(-103805.62912826252), sfix(8880.04605073558), sfix(-315.29448529694), sfix(1.0), sfix(1.0)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)]
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
        sfix(-2.5999999046325684),
        sfix(-2.125),
        sfix(-1.8874999284744263),
        sfix(-1.6499998569488525),
        sfix(-1.4124999046325684),
        sfix(-1.1749999523162842),
        sfix(-1.056249976158142),
        sfix(-0.9374999403953552),
        sfix(-0.8187499046325684),
        sfix(-0.6999999284744263),
        sfix(-0.4624999165534973),
        sfix(-0.22499993443489075),
        sfix(-0.046874936670064926),
        sfix(0.012500062584877014),
        sfix(0.2500000596046448),
        sfix(0.48750004172325134),
        sfix(0.7250000238418579),
        sfix(0.9625000357627869),
        sfix(1.0812500715255737),
        sfix(1.140625),
        sfix(1.4375),
        sfix(1.6750000715255737),
        sfix(2.1500000953674316),
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
        [sfix(5866951.812003098), sfix(14229532.736834707), sfix(14933427.037117004), sfix(8346612.498109923), sfix(2610760.4652950685), sfix(433906.543917224), sfix(29975.23422281467), sfix(1.0), sfix(1.0)],
        [sfix(206492774.73674262), sfix(584619833.8974282), sfix(691246416.7406805), sfix(436414131.2803677), sfix(155148696.12652993), sfix(29447978.05939608), sfix(2331324.2176137706), sfix(1.0), sfix(1.0)],
        [sfix(-390532110.7993208), sfix(-1355030726.5392168), sfix(-1935272896.2583303), sfix(-1461040176.3468451), sfix(-616139939.2315462), sfix(-137811569.7082161), sfix(-12786193.100920467), sfix(1.0), sfix(1.0)],
        [sfix(-70875272.9274666), sfix(-116699193.62693244), sfix(58898959.51258532), sfix(248156202.86401278), sfix(206390574.52751717), sfix(72957745.85454696), sfix(9684907.391816273), sfix(1.0), sfix(1.0)],
        [sfix(466340493.0613955), sfix(2016445489.897165), sfix(3569758964.0316625), sfix(3310771545.16182), sfix(1697840223.5561545), sfix(456741343.1308294), sfix(50357401.191194735), sfix(1.0), sfix(1.0)],
        [sfix(-446655027.08683753), sfix(-2484979005.0999293), sfix(-5682026633.006855), sfix(-6835657050.693167), sfix(-4564609539.468711), sfix(-1605797684.514363), sfix(-232836518.58937824), sfix(1.0), sfix(1.0)],
        [sfix(-40764407.96615105), sfix(-151321355.49683905), sfix(-88284439.81676532), sfix(319356418.2359384), sfix(586256944.8480611), sfix(372917353.35338), sfix(84050362.28512059), sfix(1.0), sfix(1.0)],
        [sfix(142239641.47808057), sfix(985897777.2343743), sfix(2856440578.968957), sfix(4386332692.733364), sfix(3745969133.3584414), sfix(1682241447.2650177), sfix(310128600.5748053), sfix(1.0), sfix(1.0)],
        [sfix(34056880.69546368), sfix(187306646.347574), sfix(397674211.77059716), sfix(344836780.56694245), sfix(5571308.193296052), sfix(-165811611.3862178), sfix(-70687491.99725708), sfix(1.0), sfix(1.0)],
        [sfix(-5587363.574727499), sfix(-145940194.04715276), sfix(-770944662.5637527), sfix(-1843516602.4979596), sfix(-2302384025.9249296), sfix(-1465621274.1747804), sfix(-376082695.32778513), sfix(1.0), sfix(1.0)],
        [sfix(6056700.806153198), sfix(3184411.808794339), sfix(32691413.786936924), sfix(489858160.01761883), sfix(1547963266.3937469), sfix(1957637858.273476), sfix(904654455.4615792), sfix(1.0), sfix(1.0)],
        [sfix(5797980.831812216), sfix(-3378518.589869507), sfix(-37819865.03219555), sfix(77988520.86377877), sfix(165109266.62338307), sfix(-576755521.8136646), sfix(-1077011221.51724), sfix(1.0), sfix(1.0)],
        [sfix(5797816.885026461), sfix(-3386542.5687956344), sfix(-38233550.054456174), sfix(62327428.6495858), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(5797820.43312033), sfix(-3391638.881805247), sfix(-38000214.837570384), sfix(72268882.25042085), sfix(185050664.02180457), sfix(-789539210.013827), sfix(779823882.0966629), sfix(1.0), sfix(1.0)],
        [sfix(5561739.199415552), sfix(2028431.3048202822), sfix(-90882069.27697916), sfix(353682385.50320196), sfix(-678152166.8843608), sfix(658854733.9854623), sfix(-258379208.8796632), sfix(1.0), sfix(1.0)],
        [sfix(9363960.311750969), sfix(-44282664.26733554), sfix(146489007.86528936), sfix(-301837441.4876959), sfix(350578041.2574036), sfix(-210856222.75604042), sfix(50956560.81779333), sfix(1.0), sfix(1.0)],
        [sfix(-5431804.828584902), sfix(68767547.53559326), sfix(-212981965.81484553), sfix(306817043.44027567), sfix(-227940222.6671356), sfix(81641061.50514704), sfix(-10453996.397188554), sfix(1.0), sfix(1.0)],
        [sfix(-32087707.48468771), sfix(244681398.9574811), sfix(-697175464.5333096), sfix(1018244920.8873754), sfix(-816417175.6864016), sfix(341453623.9104794), sfix(-58281964.91545164), sfix(1.0), sfix(1.0)],
        [sfix(23261553.836636104), sfix(-62537672.165390216), sfix(13551811.482765146), sfix(141067555.64988703), sfix(-207264185.74150532), sfix(115771528.54195108), sfix(-23432944.769710742), sfix(1.0), sfix(1.0)],
        [sfix(335467566.6928051), sfix(-1661507026.7491508), sfix(3426768040.2990117), sfix(-3746065936.0859637), sfix(2283703806.591628), sfix(-735882708.2950748), sfix(97937284.29832077), sfix(1.0), sfix(1.0)],
        [sfix(-764682962.1100671), sfix(3315224614.4824615), sfix(-5901350318.68275), sfix(5535081793.113583), sfix(-2890024554.014799), sfix(797075841.5108049), sfix(-90766933.78890012), sfix(1.0), sfix(1.0)],
        [sfix(-3280255733.379937), sfix(10222290975.50381), sfix(-13194612343.729284), sfix(9031268552.675892), sfix(-3458914269.2338047), sfix(703124858.5604131), sfix(-59292549.40101166), sfix(1.0), sfix(1.0)],
        [sfix(-677069549.1573175), sfix(1612531209.3519201), sfix(-1600894097.2852817), sfix(847149110.3149937), sfix(-252136542.14622825), sfix(40018573.98181218), sfix(-2646192.5964284497), sfix(1.0), sfix(1.0)],
        [sfix(-43962.44396543346), sfix(-218232.01075751105), sfix(-368400.06137840834), sfix(115885.89361378623), sfix(-19397.49579533731), sfix(1705.74288465737), sfix(-62.44309348504), sfix(1.0), sfix(1.0)]
    ]
    scaler = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)]
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
        sfix(-2.5999999046325684),
        sfix(-1.6499998569488525),
        sfix(-1.1749999523162842),
        sfix(-0.6999999284744263),
        sfix(-0.22499993443489075),
        sfix(-0.017187437042593956),
        sfix(-0.002343687228858471),
        sfix(0.012500062584877014),
        sfix(0.2500000596046448),
        sfix(0.48750004172325134),
        sfix(0.7250000238418579),
        sfix(0.9625000357627869),
        sfix(1.2000000476837158),
        sfix(1.6750000715255737),
        sfix(2.1500000953674316),
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
        [sfix(-25678884.756882746), sfix(-67133604.46162602), sfix(-76084418.84179552), sfix(-45767717.18317268), sfix(-15369120.444184687), sfix(-2737196.6286761407), sfix(-202294.3869369328), sfix(1.0), sfix(1.0)],
        [sfix(-69050327.84463815), sfix(-320818618.7000963), sfix(-612790227.0231639), sfix(-608990880.8693182), sfix(-333565118.19731927), sfix(-95853151.1997533), sfix(-11323449.021778576), sfix(1.0), sfix(1.0)],
        [sfix(13553925.20632436), sfix(88768011.93482232), sfix(221421273.7991833), sfix(281994399.67085284), sfix(190614902.19143173), sfix(64159647.80150934), sfix(8261692.5636357935), sfix(1.0), sfix(1.0)],
        [sfix(249742.7489664592), sfix(6923278.734091873), sfix(31033592.895090718), sfix(91551394.98243754), sfix(150184109.38141063), sfix(123796943.70397697), sfix(39809397.41256429), sfix(1.0), sfix(1.0)],
        [sfix(8739.33481200998), sfix(2809608.689718126), sfix(2948002.8687843443), sfix(-4567593.635653338), sfix(-14132952.753599655), sfix(17121065.204827435), sfix(55357167.09595865), sfix(1.0), sfix(1.0)],
        [sfix(8741.30571301081), sfix(2809853.6979717347), sfix(2958513.2906809333), sfix(-4369635.2307414), sfix(-12459312.37916321), sfix(19940659.785241302), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(8741.30152821919), sfix(2809855.808974366), sfix(2959536.7856058446), sfix(-4613007.48209617), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(8739.14932384823), sfix(2810180.0010630516), sfix(2942406.820194554), sfix(-4019528.3609332773), sfix(-16245667.90644022), sfix(45722333.18799169), sfix(-29360797.12114256), sfix(1.0), sfix(1.0)],
        [sfix(60461.1830273307), sfix(1827043.3103794577), sfix(10657870.902440293), sfix(-35854324.04899841), sfix(55808774.45162875), sfix(-37131399.12240215), sfix(6329694.609966114), sfix(1.0), sfix(1.0)],
        [sfix(-2104237.976684375), sfix(24227717.693206098), sfix(-84046024.92807402), sfix(171496373.86947572), sfix(-187852069.8483984), sfix(103389420.59716862), sfix(-21892398.61760757), sfix(1.0), sfix(1.0)],
        [sfix(22124519.37399732), sfix(-155072205.64841893), sfix(463840048.12716734), sfix(-710838892.7417668), sfix(598720536.3429139), sfix(-262332897.0155853), sfix(46692124.002663806), sfix(1.0), sfix(1.0)],
        [sfix(-88344689.83034813), sfix(489064848.31153417), sfix(-1096494685.295952), sfix(1297789224.4843745), sfix(-849419840.8542595), sfix(291529678.41076624), sfix(-40991261.690073766), sfix(1.0), sfix(1.0)],
        [sfix(423594395.43584156), sfix(-1848123636.7343829), sfix(3343100854.946223), sfix(-3192305726.149729), sfix(1699753806.881074), sfix(-478407806.9700939), sfix(55606027.91857466), sfix(1.0), sfix(1.0)],
        [sfix(2717916047.626015), sfix(-8554498779.619187), sfix(11164611662.805164), sfix(-7725760168.480406), sfix(2991239704.739579), sfix(-614551774.0936731), sfix(52359706.78181002), sfix(1.0), sfix(1.0)],
        [sfix(879748446.2100458), sfix(-2101736481.8767068), sfix(2096533260.3396423), sfix(-1113352452.1333692), sfix(332590325.4517633), sfix(-52989762.08906967), sfix(3517624.914283771), sfix(1.0), sfix(1.0)],
        [sfix(219624.03300513976), sfix(1090225.8838427095), sfix(1840423.323538319), sfix(-578933.4037527273), sfix(96904.44552768015), sfix(-8521.41277386914), sfix(311.94817182191), sfix(1.0), sfix(1.0)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)]
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
        sfix(-2.5999999046325684),
        sfix(-1.6499998569488525),
        sfix(-1.1749999523162842),
        sfix(-0.9374999403953552),
        sfix(-0.6999999284744263),
        sfix(-0.22499993443489075),
        sfix(-0.10624993592500687),
        sfix(0.012500062584877014),
        sfix(0.1312500536441803),
        sfix(0.19062505662441254),
        sfix(0.48750004172325134),
        sfix(0.7250000238418579),
        sfix(1.2000000476837158),
        sfix(1.6750000715255737),
        sfix(2.1500000953674316),
        sfix(3.0999999046325684)
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
        [sfix(112448223.49840319), sfix(306692475.5179608), sfix(337852810.91123736), sfix(198409375.61600128), sfix(65647829.64977827), sfix(11586932.404337734), sfix(851329.1959287098), sfix(1.0), sfix(1.0)],
        [sfix(544371947.871781), sfix(2394358835.138248), sfix(4303530905.544254), sfix(4071408239.169908), sfix(2141001252.359809), sfix(594230666.3565125), sfix(68111322.43399937), sfix(1.0), sfix(1.0)],
        [sfix(-324720147.9153338), sfix(-1805738540.1788504), sfix(-4129570481.622118), sfix(-4929205308.835173), sfix(-3241798833.979704), sfix(-1114952644.625153), sfix(-156819449.44770154), sfix(1.0), sfix(1.0)],
        [sfix(60060544.49297392), sfix(497221552.5788835), sfix(1601565500.5979462), sfix(2658325141.554688), sfix(2391475671.3297515), sfix(1107409249.1584702), sfix(206841286.60623148), sfix(1.0), sfix(1.0)],
        [sfix(-2053760.5672542509), sfix(3768578.2040093835), sfix(-28547333.03365259), sfix(-204324887.79487053), sfix(-421977249.1404079), sfix(-356094560.91020954), sfix(-106782184.41769339), sfix(1.0), sfix(1.0)],
        [sfix(-1760332.380783632), sfix(9202396.579419162), sfix(13416158.306996483), sfix(-29744003.309458725), sfix(-4444115.276183554), sfix(195357158.1545783), sfix(211282133.4802398), sfix(1.0), sfix(1.0)],
        [sfix(-1760328.76906762), sfix(9204484.685545288), sfix(13745474.8386668), sfix(-24402349.171752695), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(-1760264.4510107178), sfix(9204352.248413168), sfix(13416859.66004458), sfix(-30041120.33412792), sfix(-14454767.742039239), sfix(167380722.68768433), sfix(-192262055.9229613), sfix(1.0), sfix(1.0)],
        [sfix(-1759897.0367457937), sfix(9189520.732670117), sfix(13662434.16865346), sfix(-32148327.63997149), sfix(-4818513.022633422), sfix(146360792.09182927), sfix(-178121240.1590115), sfix(1.0), sfix(1.0)],
        [sfix(-1724124.5275632627), sfix(8270555.206171804), sfix(23581332.08705494), sfix(-89884441.17231973), sfix(186847569.92933634), sfix(-198530038.91347957), sfix(85197511.56971726), sfix(1.0), sfix(1.0)],
        [sfix(-1404032.3204871195), sfix(7323775.473644593), sfix(13320569.79424622), sfix(-20354289.182504307), sfix(14686139.09007027), sfix(-1600540.2375711312), sfix(-2274264.5372820897), sfix(1.0), sfix(1.0)],
        [sfix(-11518100.10247856), sfix(80942059.66959122), sfix(-205423356.6785443), sfix(316698534.08912027), sfix(-265722786.88359293), sfix(114926374.69591518), sfix(-20139237.389709618), sfix(1.0), sfix(1.0)],
        [sfix(52121983.91621868), sfix(-225578496.46045116), sfix(429858653.54492426), sfix(-409251382.48739743), sfix(215750610.08281353), sfix(-60045149.816901445), sfix(6927837.445870934), sfix(1.0), sfix(1.0)],
        [sfix(1059599733.3397198), sfix(-3426385698.058822), sfix(4621187798.974952), sfix(-3296360220.8878355), sfix(1314517240.8591878), sfix(-277721418.367851), sfix(24286750.01530074), sfix(1.0), sfix(1.0)],
        [sfix(234523396.69495812), sfix(-518576649.9155799), sfix(490120677.04106915), sfix(-240905444.49881142), sfix(66527952.62609379), sfix(-9785698.796506599), sfix(598736.4110107746), sfix(1.0), sfix(1.0)],
        [sfix(-119359.12173859), sfix(4672785.7964447), sfix(4982312.478760421), sfix(-1548686.661458598), sfix(253503.40887702335), sfix(-21685.93325591702), sfix(769.97969662592), sfix(1.0), sfix(1.0)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)]
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
        sfix(-2.5999999046325684),
        sfix(-1.6499998569488525),
        sfix(-1.1749999523162842),
        sfix(-0.6999999284744263),
        sfix(-0.22499993443489075),
        sfix(-0.10624993592500687),
        sfix(-0.017187437042593956),
        sfix(0.012500062584877014),
        sfix(0.2500000596046448),
        sfix(0.48750004172325134),
        sfix(0.7250000238418579),
        sfix(0.9625000357627869),
        sfix(1.2000000476837158),
        sfix(1.4375),
        sfix(1.6750000715255737),
        sfix(1.9125001430511475),
        sfix(2.1500000953674316),
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
        [sfix(4959935.245255388), sfix(14215789.213703407), sfix(15294797.778170245), sfix(8800830.17778362), sfix(2879322.7102122195), sfix(505542.9171422335), sfix(37068.5260913477), sfix(1.0), sfix(1.0)],
        [sfix(18542316.278505538), sfix(75320874.82934888), sfix(125205262.90629882), sfix(111352279.22469914), sfix(55648365.60124196), sfix(14776384.540861566), sfix(1627266.7481136604), sfix(1.0), sfix(1.0)],
        [sfix(14055334.30514666), sfix(100169608.13769877), sfix(285164416.5928758), sfix(421755110.4014443), sfix(341536841.4385204), sfix(144127918.07634628), sfix(24865886.208629083), sfix(1.0), sfix(1.0)],
        [sfix(-40846.23876119664), sfix(-338966.8845489274), sfix(-2674621.3326149504), sfix(9562909.010922119), sfix(50211803.80898452), sfix(68526084.4045206), sfix(30306840.95492677), sfix(1.0), sfix(1.0)],
        [sfix(34984.96779004894), sfix(716497.2453782451), sfix(2012016.3227506278), sfix(10853558.775417428), sfix(108648.83178716978), sfix(-79117137.19865258), sfix(-105659360.28472833), sfix(1.0), sfix(1.0)],
        [sfix(34759.2628006061), sfix(707165.2899755813), sfix(1856800.3157524245), sfix(9560633.889465187), sfix(-5175090.874862885), sfix(-86475224.20264058), sfix(-99158179.04334491), sfix(1.0), sfix(1.0)],
        [sfix(34759.46488968246), sfix(707192.241192001), sfix(1858071.4559518083), sfix(9647064.483793003), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(34757.7937033244), sfix(707424.9387632529), sfix(1849393.977760628), sfix(9767125.513202697), sfix(-3763692.96366477), sfix(-81115611.18102396), sfix(122779460.75771718), sfix(1.0), sfix(1.0)],
        [sfix(53850.10795392495), sfix(558611.391143712), sfix(629205.6973611884), sfix(29493612.373036396), sfix(-101405317.8155424), sfix(138764508.24227986), sfix(-70419024.90410627), sfix(1.0), sfix(1.0)],
        [sfix(-616867.0817446945), sfix(4763754.809681978), sfix(-757438.4958425893), sfix(-21201465.287034906), sfix(60756597.17956347), sfix(-64817499.25837945), sfix(24206014.839394234), sfix(1.0), sfix(1.0)],
        [sfix(553339.8679034216), sfix(5858152.733450412), sfix(-41898469.31976629), sfix(124096799.73581803), sfix(-163116576.91281343), sfix(100455378.75939831), sfix(-23732683.67287852), sfix(1.0), sfix(1.0)],
        [sfix(45490675.24757618), sfix(-287097884.46195537), sfix(753387557.6731082), sfix(-1026915562.7421517), sfix(773758510.9883147), sfix(-306247684.07499844), sfix(49840358.09710943), sfix(1.0), sfix(1.0)],
        [sfix(-224002726.4440213), sfix(1156426927.6570456), sfix(-2451610001.1034374), sfix(2751722498.4037476), sfix(-1722947320.7878485), sfix(570840653.6362624), sfix(-78202423.64442442), sfix(1.0), sfix(1.0)],
        [sfix(435300016.703652), sfix(-2210042447.9006677), sfix(4461964296.85156), sfix(-4635546535.23657), sfix(2636888372.179378), sfix(-782475665.5250771), sfix(94919798.4459804), sfix(1.0), sfix(1.0)],
        [sfix(-332512048.9373145), sfix(2368527234.248248), sfix(-5092991988.140045), sfix(5133754180.853266), sfix(-2706202341.414584), sfix(725188106.4827042), sfix(-78218966.28279915), sfix(1.0), sfix(1.0)],
        [sfix(492458386.4822189), sfix(-2874894958.9270782), sfix(5244117956.59117), sfix(-4512206943.919869), sfix(2038490207.251419), sfix(-469709836.4452605), sfix(43699473.82622478), sfix(1.0), sfix(1.0)],
        [sfix(2658304710.9975843), sfix(-6354299015.431513), sfix(6330588310.783925), sfix(-3362479356.919508), sfix(1004548516.2487469), sfix(-160047682.79580727), sfix(10623798.365291823), sfix(1.0), sfix(1.0)],
        [sfix(109790.19150821267), sfix(545004.6015425526), sfix(920028.771017046), sfix(-289409.17078185774), sfix(48442.59295326132), sfix(-4259.85957754132), sfix(155.9430862793), sfix(1.0), sfix(1.0)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)]
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
        sfix(-2.5999999046325684),
        sfix(-1.6499998569488525),
        sfix(-1.1749999523162842),
        sfix(-0.9374999403953552),
        sfix(-0.6999999284744263),
        sfix(-0.22499993443489075),
        sfix(-0.046874936670064926),
        sfix(-0.017187437042593956),
        sfix(0.012500062584877014),
        sfix(0.2500000596046448),
        sfix(0.48750004172325134),
        sfix(0.7250000238418579),
        sfix(0.9625000357627869),
        sfix(1.4375),
        sfix(1.6750000715255737),
        sfix(1.9125001430511475),
        sfix(2.1500000953674316),
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
        [sfix(72678218.5742313), sfix(196426685.34145543), sfix(217863922.16748455), sfix(128704326.80692707), sfix(42748556.95932357), sfix(7564006.0475682765), sfix(556721.8401017638), sfix(1.0), sfix(1.0)],
        [sfix(301339335.4373574), sfix(1346265435.9276466), sfix(2457816019.120059), sfix(2356211718.252081), sfix(1253185719.7043104), sfix(351289184.4873962), sfix(40621308.89566217), sfix(1.0), sfix(1.0)],
        [sfix(-170379397.2494441), sfix(-976680505.3054031), sfix(-2299046651.643848), sfix(-2827996606.231184), sfix(-1917689171.8815002), sfix(-680523329.4732337), sfix(-98897075.29894476), sfix(1.0), sfix(1.0)],
        [sfix(26430140.450438168), sfix(223217196.71307313), sfix(750320736.7730321), sfix(1306735068.890506), sfix(1237109044.6387904), sfix(603713935.8787682), sfix(118994363.4228806), sfix(1.0), sfix(1.0)],
        [sfix(-112079.86998243532), sfix(-176411.25666160465), sfix(-36943911.35548621), sfix(-179866539.2335783), sfix(-348689006.9937246), sfix(-301862699.021156), sfix(-97141193.1265257), sfix(1.0), sfix(1.0)],
        [sfix(179881.24113271697), sfix(5127703.870339327), sfix(2863209.303250167), sfix(-21111319.923680905), sfix(8462091.261519417), sfix(131117755.5707282), sfix(125521163.29804133), sfix(1.0), sfix(1.0)],
        [sfix(179858.47704300677), sfix(5126014.095820321), sfix(2811925.8557355003), sfix(-21940009.525679313), sfix(737619.4461055293), sfix(90349049.19489707), sfix(26920610.203815315), sfix(1.0), sfix(1.0)],
        [sfix(179858.47541555908), sfix(5126011.454279853), sfix(2811811.140890101), sfix(-21924187.035402298), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(179859.77373903443), sfix(5125830.497508698), sfix(2819302.902738084), sfix(-22051316.255317293), sfix(524767.6283097315), sfix(95002723.08412342), sfix(-119157743.2812763), sfix(1.0), sfix(1.0)],
        [sfix(170234.26993125948), sfix(5135553.3855205495), sfix(4677952.9501967905), sfix(-41643764.698606476), sfix(87952788.44347425), sfix(-93159777.10901949), sfix(42216038.89880348), sfix(1.0), sfix(1.0)],
        [sfix(1747181.9833195554), sfix(-9945912.702197924), sfix(61058344.538215294), sfix(-140998351.40925217), sfix(158893455.74148542), sfix(-85086626.11082877), sfix(16739424.6135692), sfix(1.0), sfix(1.0)],
        [sfix(-19382634.784059454), sfix(144885018.7116166), sfix(-406131380.78211135), sfix(599032836.615421), sfix(-486129468.84526247), sfix(205320969.33468288), sfix(-35096032.123286635), sfix(1.0), sfix(1.0)],
        [sfix(99615212.52673471), sfix(-530168757.236556), sfix(1183384527.6582828), sfix(-1387528604.0545049), sfix(901956667.6097171), sfix(-307946419.89525455), sfix(43186641.92025875), sfix(1.0), sfix(1.0)],
        [sfix(-99859417.50103265), sfix(610835158.9818244), sfix(-1346198898.0156279), sfix(1474507126.1121442), sfix(-866592096.2362491), sfix(262797020.3583241), sfix(-32370682.972437333), sfix(1.0), sfix(1.0)],
        [sfix(89284946.55568747), sfix(-745312563.001399), sfix(1687735379.3336432), sfix(-1743140715.027508), sfix(933447622.5775688), sfix(-252973740.5602578), sfix(27520853.38337009), sfix(1.0), sfix(1.0)],
        [sfix(-82512763.24775812), sfix(789206159.456937), sfix(-1623576946.378109), sfix(1479305216.8380332), sfix(-690544051.428398), sfix(162517862.68115526), sfix(-15345142.618038155), sfix(1.0), sfix(1.0)],
        [sfix(-1053302940.7444817), sfix(2520454219.3669286), sfix(-2508655735.1152806), sfix(1333360553.8071122), sfix(-398561895.5099988), sfix(63528761.2532551), sfix(-4218642.832615981), sfix(1.0), sfix(1.0)],
        [sfix(200765.7465673318), sfix(996612.303827372), sfix(1682393.1220414876), sfix(-529222.5783790547), sfix(88583.62669346842), sfix(-7789.71123510545), sfix(285.16236019598), sfix(1.0), sfix(1.0)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)]
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
        sfix(-2.5999999046325684),
        sfix(-2.125),
        sfix(-1.6499998569488525),
        sfix(-1.4124999046325684),
        sfix(-1.1749999523162842),
        sfix(-0.9374999403953552),
        sfix(-0.6999999284744263),
        sfix(-0.4624999165534973),
        sfix(-0.22499993443489075),
        sfix(-0.10624993592500687),
        sfix(0.012500062584877014),
        sfix(0.2500000596046448),
        sfix(0.7250000238418579),
        sfix(0.9625000357627869),
        sfix(1.2000000476837158),
        sfix(1.4375),
        sfix(1.6750000715255737),
        sfix(2.1500000953674316),
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
        [sfix(1107768.1187989374), sfix(-567085.1308569434), sfix(954090.4431748673), sfix(1334597.8518635535), sfix(567095.8668227311), sfix(107667.67426270188), sfix(7917.7019144688), sfix(1.0), sfix(1.0)],
        [sfix(7774759.594694442), sfix(6412048.256664714), sfix(-5933006.342147483), sfix(-13248510.102194205), sfix(-8502008.288322467), sfix(-2398599.4637974114), sfix(-256458.40934396297), sfix(1.0), sfix(1.0)],
        [sfix(-53498957.61861061), sfix(-172763820.87672442), sfix(-213819008.44974506), sfix(-131695248.11181869), sfix(-40576372.9285554), sfix(-5060762.613642036), sfix(-23383.5222978638), sfix(1.0), sfix(1.0)],
        [sfix(124621111.98407505), sfix(553396405.1222492), sfix(1017857066.4685273), sfix(980599024.5632144), sfix(523341076.6880283), sfix(147075113.81009787), sfix(17033790.561495222), sfix(1.0), sfix(1.0)],
        [sfix(-64402322.458566606), sfix(-375951143.16787136), sfix(-885462118.9067699), sfix(-1097620244.5893536), sfix(-752514488.9681832), sfix(-270440694.77131873), sfix(-39857246.25852561), sfix(1.0), sfix(1.0)],
        [sfix(3254257.6232185103), sfix(43503936.72359609), sfix(200257266.2433172), sfix(404365974.4119112), sfix(418876618.3342316), sfix(217926721.61715552), sfix(45184441.46411919), sfix(1.0), sfix(1.0)],
        [sfix(-432463.7560397103), sfix(9896711.86499434), sfix(72323937.01286049), sfix(144047808.73140454), sfix(120268750.31582853), sfix(34857056.253484845), sfix(-1674478.4902333657), sfix(1.0), sfix(1.0)],
        [sfix(-1764187.2524110398), sfix(-6104262.143812956), sfix(-8265901.928996798), sfix(-73870620.11097391), sfix(-213574137.210759), sfix(-239983669.14384317), sfix(-96695357.19904952), sfix(1.0), sfix(1.0)],
        [sfix(-1711345.6393187556), sfix(-4871994.816652811), sfix(3889031.43968596), sfix(-8762606.54910397), sfix(-13306724.754226299), sfix(96047143.78810593), sfix(143811056.10576442), sfix(1.0), sfix(1.0)],
        [sfix(-1711082.9881009331), sfix(-4859386.843528822), sfix(4294894.720454404), sfix(-3514948.4656647877), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(-1711041.4101086934), sfix(-4859772.344881704), sfix(4107369.284820546), sfix(-7249927.565298803), sfix(-7921277.184027283), sfix(101239263.68516617), sfix(-149533294.65943402), sfix(1.0), sfix(1.0)],
        [sfix(-2262537.2932294365), sfix(3823777.8300728104), sfix(-50306236.801058225), sfix(160794050.0219957), sfix(-252345742.3238215), sfix(191087841.1778004), sfix(-56095814.51749932), sfix(1.0), sfix(1.0)],
        [sfix(17628454.525874685), sfix(-161500610.9985678), sfix(523261345.96117425), sfix(-901240751.3224899), sfix(853167964.1644657), sfix(-421380531.4052466), sfix(84743772.77566062), sfix(1.0), sfix(1.0)],
        [sfix(-152085865.7344553), sfix(873088339.6258548), sfix(-2108545120.5830314), sfix(2674854771.1644297), sfix(-1884482416.9287233), sfix(698201652.9174232), sfix(-106351729.88473307), sfix(1.0), sfix(1.0)],
        [sfix(405494198.5740324), sfix(-1921278016.3717191), sfix(3729525102.132815), sfix(-3833624178.2517414), sfix(2199103849.2467403), sfix(-669010305.91526), sfix(84481994.1506353), sfix(1.0), sfix(1.0)],
        [sfix(-359696687.5926325), sfix(1560333998.0220225), sfix(-2822629654.05555), sfix(2702678742.7437463), sfix(-1449877000.7063432), sfix(412712624.502128), sfix(-48633573.893443994), sfix(1.0), sfix(1.0)],
        [sfix(-4525494783.589723), sfix(14350421855.54416), sfix(-18859451095.303856), sfix(13133721371.167828), sfix(-5114699075.324695), sfix(1056402772.6320907), sfix(-90442624.67642398), sfix(1.0), sfix(1.0)],
        [sfix(-1683148579.224682), sfix(4023639649.428804), sfix(-4015479194.153518), sfix(2133701615.2715976), sfix(-637783312.1094584), sfix(101675469.74232285), sfix(-6753578.584433013), sfix(1.0), sfix(1.0)],
        [sfix(-382786.4769259446), sfix(-1900173.3072185), sfix(-3207705.233532847), sfix(1009032.9139671648), sfix(-168896.41263263914), sfix(14852.11581603668), sfix(-543.69979479189), sfix(1.0), sfix(1.0)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)]
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
        sfix(-2.5999999046325684),
        sfix(-1.6499998569488525),
        sfix(-1.1749999523162842),
        sfix(-0.6999999284744263),
        sfix(-0.4624999165534973),
        sfix(-0.10624993592500687),
        sfix(-0.046874936670064926),
        sfix(0.012500062584877014),
        sfix(0.1312500536441803),
        sfix(0.19062505662441254),
        sfix(0.48750004172325134),
        sfix(0.7250000238418579),
        sfix(0.9625000357627869),
        sfix(1.2000000476837158),
        sfix(1.6750000715255737),
        sfix(2.1500000953674316),
        sfix(3.0999999046325684)
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
        [sfix(-33384992.426640674), sfix(-83383915.55170986), sfix(-95721346.35933247), sfix(-58122246.42055847), sfix(-19563731.437576357), sfix(-3478090.4210333535), sfix(-256088.23628099103), sfix(1.0), sfix(1.0)],
        [sfix(-203684067.63886386), sfix(-864414223.2097478), sfix(-1526367246.402333), sfix(-1417107005.804921), sfix(-731530844.7085534), sfix(-199560747.80310515), sfix(-22513966.784762077), sfix(1.0), sfix(1.0)],
        [sfix(-56526692.44922252), sfix(-403995220.1224523), sfix(-1206154663.7421813), sfix(-1855139729.9055705), sfix(-1561720416.8632953), sfix(-684792483.8762519), sfix(-122518774.53808603), sfix(1.0), sfix(1.0)],
        [sfix(3387394.1424265523), sfix(66188120.36828248), sfix(329743796.52383065), sfix(817725356.998897), sfix(1051429232.7351848), sfix(675712415.2946154), sfix(172082612.33985516), sfix(1.0), sfix(1.0)],
        [sfix(-1422396.2942983927), sfix(5997675.47918465), sfix(13214153.027278682), sfix(-77536367.98441947), sfix(-384301877.5318575), sfix(-561204109.2592337), sfix(-274706337.4730604), sfix(1.0), sfix(1.0)],
        [sfix(-1401743.8698121682), sfix(6692557.692114037), sfix(22735300.88336935), sfix(-8936529.184222413), sfix(-106476740.0392952), sfix(49192973.76710388), sfix(305924301.5429095), sfix(1.0), sfix(1.0)],
        [sfix(-1401747.442795923), sfix(6690775.057380793), sfix(22812678.110481042), sfix(-1441533.0015671242), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(-1401743.0691643602), sfix(6692741.354802964), sfix(22734633.957096033), sfix(-8678627.345476557), sfix(-108470308.70499723), sfix(81350305.9621479), sfix(167255243.46763602), sfix(1.0), sfix(1.0)],
        [sfix(-1402841.1166109657), sfix(6740872.054927058), sfix(21839661.965451404), sfix(398079.6567936586), sfix(-161645995.89316365), sfix(252488537.49267295), sfix(-69375649.02921492), sfix(1.0), sfix(1.0)],
        [sfix(-1363599.7420535248), sfix(6032001.178308041), sfix(26311217.45108224), sfix(-7900101.141848522), sfix(-188816526.29748502), sfix(390107039.46402436), sfix(-233639946.65319973), sfix(1.0), sfix(1.0)],
        [sfix(-4957959.6901971325), sfix(34949289.99001173), sfix(-44668641.926185824), sfix(-26174985.505958993), sfix(174642795.50515252), sfix(-196454482.295822), sfix(72212079.07963975), sfix(1.0), sfix(1.0)],
        [sfix(21752717.9507164), sfix(-139708625.45975012), sfix(399388005.07725793), sfix(-552953040.8939972), sfix(418560389.2799145), sfix(-163039321.39767984), sfix(25176582.505907442), sfix(1.0), sfix(1.0)],
        [sfix(-100951067.4464245), sfix(560580003.1870117), sfix(-1253097120.3045743), sfix(1506610588.4800904), sfix(-1007410133.8673822), sfix(354925313.9453374), sfix(-51480793.249395415), sfix(1.0), sfix(1.0)],
        [sfix(5298188.857394807), sfix(-44233011.81165608), sfix(136800374.39322984), sfix(-158213055.99989048), sfix(94794633.79659659), sfix(-28887066.108241245), sfix(3578256.731475457), sfix(1.0), sfix(1.0)],
        [sfix(-169700154.50726256), sfix(486719814.7590943), sfix(-541668275.6912367), sfix(314736623.9031278), sfix(-97732624.2935326), sfix(15146567.255156554), sfix(-881873.2211055582), sfix(1.0), sfix(1.0)],
        [sfix(76798459.30474697), sfix(-166526941.30230325), sfix(163060419.5993465), sfix(-79461305.38610859), sfix(21810970.78956415), sfix(-3196058.7367935744), sfix(195105.90210117612), sfix(1.0), sfix(1.0)],
        [sfix(-115109.75004340732), sfix(4506427.304471631), sfix(4804934.352232647), sfix(-1493550.9910677304), sfix(244478.29053370733), sfix(-20913.88007164044), sfix(742.56721362586), sfix(1.0), sfix(1.0)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)]
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
        sfix(-2.5999999046325684),
        sfix(-2.125),
        sfix(-1.8874999284744263),
        sfix(-1.6499998569488525),
        sfix(-1.4124999046325684),
        sfix(-1.1749999523162842),
        sfix(-1.056249976158142),
        sfix(-0.9968749284744263),
        sfix(-0.8781249523162842),
        sfix(-0.8187499046325684),
        sfix(-0.6999999284744263),
        sfix(-0.4624999165534973),
        sfix(-0.22499993443489075),
        sfix(-0.017187437042593956),
        sfix(0.012500062584877014),
        sfix(0.2500000596046448),
        sfix(0.4281250238418579),
        sfix(0.48750004172325134),
        sfix(0.9625000357627869),
        sfix(1.2000000476837158),
        sfix(1.4375),
        sfix(1.6750000715255737),
        sfix(2.1500000953674316),
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
        [sfix(2838621.79080636), sfix(6879539.017415855), sfix(7222269.07095228), sfix(4037932.14094469), sfix(1263268.1829396994), sfix(209974.77404256837), sfix(14506.23848983376), sfix(1.0), sfix(1.0)],
        [sfix(92841674.56121041), sfix(262428942.88274333), sfix(309839605.67326987), sfix(195337098.43441108), sfix(69347273.45529735), sfix(13144613.036934715), sfix(1039257.8182698757), sfix(1.0), sfix(1.0)],
        [sfix(-235465956.71422705), sfix(-801864661.3271568), sfix(-1128282672.048071), sfix(-841452994.4903054), sfix(-351250514.6451394), sfix(-77887992.87060137), sfix(-7173088.16911074), sfix(1.0), sfix(1.0)],
        [sfix(40619133.241366565), sfix(243254776.11996385), sfix(519586809.6732339), sfix(543842865.9106768), sfix(303635452.9271324), sfix(87187761.04085022), sfix(10160898.444216823), sfix(1.0), sfix(1.0)],
        [sfix(228026361.61081982), sfix(949788155.1937366), sfix(1609735550.0932937), sfix(1419402781.0627413), sfix(685724318.0123538), sfix(171514900.07534024), sfix(17237481.61014598), sfix(1.0), sfix(1.0)],
        [sfix(-307806084.38116705), sfix(-1685763772.939965), sfix(-3793602189.5747766), sfix(-4490994272.480657), sfix(-2952293187.045047), sfix(-1023265675.4712945), sfix(-146324324.095678), sfix(1.0), sfix(1.0)],
        [sfix(-118845697.29752025), sfix(-616940153.1045022), sfix(-1273739032.8984797), sfix(-1321476675.7271285), sfix(-709041256.0586942), sfix(-176219127.29519233), sfix(-13012017.39352756), sfix(1.0), sfix(1.0)],
        [sfix(84613844.5840785), sfix(615130577.351527), sfix(1836234935.0202148), sfix(2866957338.2471366), sfix(2465232334.226196), sfix(1107325491.4251168), sfix(203330245.69127342), sfix(1.0), sfix(1.0)],
        [sfix(81499856.28172375), sfix(587308358.9319103), sfix(1738840233.3482883), sfix(2692111275.848999), sfix(2293397060.301454), sfix(1019031527.2511827), sfix(184711698.79581025), sfix(1.0), sfix(1.0)],
        [sfix(16929833.831337426), sfix(106387146.40654483), sfix(245422666.1953103), sfix(217201910.7526194), sfix(-15092378.447659802), sfix(-130071282.68077165), sfix(-53760416.759558305), sfix(1.0), sfix(1.0)],
        [sfix(-4329974.715545542), sfix(-68717005.33204772), sfix(-354718505.8445243), sfix(-877993945.8900552), sfix(-1136999657.9704635), sfix(-741449214.5952473), sfix(-192141987.38478005), sfix(1.0), sfix(1.0)],
        [sfix(1249425.6920337803), sfix(1317664.1133460181), sfix(15311045.181002216), sfix(176006717.83826926), sfix(570775652.5153778), sfix(751185996.6782589), sfix(357595286.5319657), sfix(1.0), sfix(1.0)],
        [sfix(1153916.6764628731), sfix(-1117240.6044915125), sfix(-10995634.294222614), sfix(21301291.47822109), sfix(46851301.12124611), sfix(-219724236.21877035), sfix(-412178665.7945259), sfix(1.0), sfix(1.0)],
        [sfix(1153912.9447227104), sfix(-1117538.94836627), sfix(-10996261.353468698), sfix(20671692.659125857), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(1153916.05911093), sfix(-1118028.6177253707), sfix(-10983600.283652324), sfix(20509277.959863923), sfix(58389804.2323609), sfix(-266148492.02171126), sfix(283423129.72571063), sfix(1.0), sfix(1.0)],
        [sfix(1085096.7016469445), sfix(551725.4599135347), sfix(-28192766.327906284), sfix(117127225.6164527), sfix(-253596964.7235627), sfix(283219623.55944216), sfix(-128207259.28655052), sfix(1.0), sfix(1.0)],
        [sfix(1893733.98730685), sfix(-11144799.951774739), sfix(42531420.5138096), sfix(-111693972.53435062), sfix(164188697.38263142), sfix(-124904821.95876314), sfix(38428806.8981201), sfix(1.0), sfix(1.0)],
        [sfix(-940915.1651302748), sfix(19231988.78690097), sfix(-91717495.52736646), sfix(201176681.0670753), sfix(-240758768.04510576), sfix(150513134.0576053), sfix(-38239956.11107241), sfix(1.0), sfix(1.0)],
        [sfix(-206352244.03658816), sfix(1198009566.1384284), sfix(-2872343838.7775264), sfix(3634673961.1097207), sfix(-2562819385.392292), sfix(955154169.9981767), sfix(-147056134.4221768), sfix(1.0), sfix(1.0)],
        [sfix(679726586.2814254), sfix(-3263259735.0776467), sfix(6489409473.186743), sfix(-6845952654.091575), sfix(4039257172.9436626), sfix(-1263660086.877178), sfix(163761436.3629332), sfix(1.0), sfix(1.0)],
        [sfix(-1257489478.9308505), sfix(5311563898.939153), sfix(-9274451069.579153), sfix(8567073587.579936), sfix(-4417088529.43956), sfix(1205543845.8770475), sfix(-136096081.6492558), sfix(1.0), sfix(1.0)],
        [sfix(-4913273212.321158), sfix(15363459344.342756), sfix(-19913641703.524), sfix(13693716592.524963), sfix(-5269943988.000153), sfix(1076468075.3954442), sfix(-91209587.17240247), sfix(1.0), sfix(1.0)],
        [sfix(-1391431304.444974), sfix(3323572746.3833585), sfix(-3307962786.936384), sfix(1755611576.1382966), sfix(-524060934.4309597), sfix(83424550.52425347), sfix(-5532884.240255594), sfix(1.0), sfix(1.0)],
        [sfix(-21862.16450481571), sfix(-108524.99744403693), sfix(-183202.343148535), sfix(57629.10887831759), sfix(-9646.21631072283), sfix(848.25201198953), sfix(-31.05244064639), sfix(1.0), sfix(1.0)]
    ]
    scaler = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)]
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
        sfix(-2.5999999046325684),
        sfix(-2.125),
        sfix(-1.8874999284744263),
        sfix(-1.6499998569488525),
        sfix(-1.4124999046325684),
        sfix(-1.1749999523162842),
        sfix(-0.9374999403953552),
        sfix(-0.8187499046325684),
        sfix(-0.5812499523162842),
        sfix(-0.5218749046325684),
        sfix(-0.10624993592500687),
        sfix(0.012500062584877014),
        sfix(0.2500000596046448),
        sfix(0.7250000238418579),
        sfix(1.2000000476837158),
        sfix(1.6750000715255737),
        sfix(2.1500000953674316),
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
        [sfix(2595485.244152186), sfix(6152505.165226426), sfix(6524719.143109237), sfix(3681909.618859062), sfix(1158230.9180400413), sfix(193085.07038323308), sfix(13359.77947296936), sfix(1.0), sfix(1.0)],
        [sfix(94531183.75439033), sfix(267656280.84673887), sfix(316736088.45856327), sfix(200118303.9662577), sfix(71187999.45467137), sfix(13519214.663104171), sfix(1070819.1760151244), sfix(1.0), sfix(1.0)],
        [sfix(-155710992.98901615), sfix(-546225270.5960413), sfix(-786510134.0234442), sfix(-597697025.0194393), sfix(-253430128.05943996), sfix(-56943219.12979982), sfix(-5303659.570517223), sfix(1.0), sfix(1.0)],
        [sfix(-59800737.599800184), sfix(-165754123.29972863), sfix(-160978665.66601035), sfix(-51681132.86906604), sfix(13620657.085716138), sfix(12482351.218355859), sfix(2194601.9841821394), sfix(1.0), sfix(1.0)],
        [sfix(196320341.78063098), sfix(863343373.3087802), sfix(1556172628.5710068), sfix(1470499334.3820882), sfix(769152533.1340845), sfix(211399260.70901227), sfix(23873720.934097458), sfix(1.0), sfix(1.0)],
        [sfix(-112665606.02020757), sfix(-627301168.5880708), sfix(-1432396388.2444444), sfix(-1715280850.667942), sfix(-1134169344.3090987), sfix(-392452465.65804833), sfix(-55538742.465269126), sfix(1.0), sfix(1.0)],
        [sfix(38849702.02102882), sfix(292203494.9540224), sfix(893792947.6604437), sfix(1424923877.4263663), sfix(1251633277.2997606), sfix(574864555.7621558), sfix(107980406.3717369), sfix(1.0), sfix(1.0)],
        [sfix(-545032.4419464754), sfix(-4279715.265890571), sfix(-37802520.76260102), sfix(-139380710.79346222), sfix(-228814034.67697716), sfix(-173824686.2489765), sfix(-50077589.441320896), sfix(1.0), sfix(1.0)],
        [sfix(-1030667.608933296), sfix(-7443612.25108511), sfix(-44358890.68197398), sfix(-140110420.2098002), sfix(-213457538.617618), sfix(-153377855.7515897), sfix(-41724612.611523144), sfix(1.0), sfix(1.0)],
        [sfix(-411491.1875677856), sfix(242875.83983333397), sfix(-3913446.265255104), sfix(-24500337.982585937), sfix(-24089426.311829887), sfix(14982959.723636571), sfix(21618220.55707326), sfix(1.0), sfix(1.0)],
        [sfix(-406034.40597344), sfix(410580.4790750359), sfix(-1901580.6189341221), sfix(-13168560.206162592), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(-406038.08740513254), sfix(410213.57287500304), sfix(-1863088.330723828), sfix(-12222181.588574966), sfix(15810156.1482442), sfix(63212403.2337714), sfix(-107804797.15679526), sfix(1.0), sfix(1.0)],
        [sfix(-647678.2174946119), sfix(4076767.4294067323), sfix(-23429704.085050464), sfix(46142952.33499954), sfix(-38671077.68855189), sfix(8659357.806943303), sfix(2999010.385871713), sfix(1.0), sfix(1.0)],
        [sfix(3879064.679353966), sfix(-28961826.68014202), sfix(74004841.09394902), sfix(-98891185.09379435), sfix(70235271.89601958), sfix(-24385073.64581556), sfix(3079269.665238354), sfix(1.0), sfix(1.0)],
        [sfix(-852464122.4963099), sfix(3739727660.9770503), sfix(-6800693565.125061), sfix(6547707144.984722), sfix(-3516955866.3096585), sfix(998396213.6249077), sfix(-116964238.9374085), sfix(1.0), sfix(1.0)],
        [sfix(-6827756530.566607), sfix(21465260042.396027), sfix(-27957731400.85959), sfix(19310094636.56071), sfix(-7461565830.9666), sfix(1529914689.6364925), sfix(-130093494.08750774), sfix(1.0), sfix(1.0)],
        [sfix(-1945735516.2142115), sfix(4647945117.74942), sfix(-4626589692.526499), sfix(2455645235.49126), sfix(-733089340.4131223), sfix(116709940.46861042), sfix(-7741143.411535742), sfix(1.0), sfix(1.0)],
        [sfix(-35851.20296720662), sfix(-177967.36045833473), sfix(-300428.824753691), sfix(94504.49789185399), sfix(-15818.5827742325), sfix(1391.02672309669), sfix(-50.92210115114), sfix(1.0), sfix(1.0)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)]
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
        sfix(-50.0),
        sfix(-14.0625),
        sfix(-12.5),
        sfix(-10.9375),
        sfix(-9.375),
        sfix(-7.8125),
        sfix(-6.25),
        sfix(-4.6875),
        sfix(-3.125),
        sfix(-2.34375),
        sfix(-1.953125),
        sfix(-1.5625),
        sfix(-1.171875),
        sfix(-0.78125),
        sfix(-0.390625),
        sfix(-0.0244140625),
        sfix(-0.01220703125),
        sfix(0.1953125),
        sfix(0.78125),
        sfix(1.171875),
        sfix(1.5625),
        sfix(2.34375),
        sfix(3.125),
        sfix(6.25),
        sfix(12.5)
    ]
    coeffA = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(10622.627468929), sfix(2108.00539808004), sfix(168.21894605276), sfix(6.92699098082), sfix(0.1556931013), sfix(0.00181636631), sfix(8.61675e-06), sfix(1.0), sfix(1.0)],
        [sfix(2198413.4563089525), sfix(880186.6023599504), sfix(148281.58934945613), sfix(13437.21553220936), sfix(690.0738741802), sfix(19.02482642903), sfix(0.21980148363), sfix(1.0), sfix(1.0)],
        [sfix(4356546.650910456), sfix(1924513.0363700062), sfix(359035.9011288804), sfix(36141.28429312758), sfix(2067.08010505618), sfix(63.60510532074), sfix(0.82167770327), sfix(1.0), sfix(1.0)],
        [sfix(7594449.24133275), sfix(3713350.4725108645), sfix(771311.4585702157), sfix(86877.5152636507), sfix(5583.32823746908), sfix(193.72373201119), sfix(2.8302092877), sfix(1.0), sfix(1.0)],
        [sfix(11086947.07723572), sfix(5954250.34831194), sfix(1371384.5684899807), sfix(172717.44741951965), sfix(12501.59686637276), sfix(491.57373928421), sfix(8.18164920807), sfix(1.0), sfix(1.0)],
        [sfix(12261951.825406777), sfix(6810568.429411081), sfix(1631017.7573153381), sfix(214626.37816434685), sfix(16298.7465766431), sfix(674.60377815127), sfix(11.84677751742), sfix(1.0), sfix(1.0)],
        [sfix(7661372.120953718), sfix(2207814.206615012), sfix(-293078.0274852153), sfix(-215475.12862989568), sfix(-37912.92929909574), sfix(-2977.85278563852), sfix(-90.89657033779), sfix(1.0), sfix(1.0)],
        [sfix(-299599.1567742126), sfix(-8110938.233520526), sfix(-5901721.0953968195), sfix(-1851646.663836459), sfix(-308051.8189613732), sfix(-26905.35288307934), sfix(-978.88730332656), sfix(1.0), sfix(1.0)],
        [sfix(-3180732.225207785), sfix(-13772593.511037827), sfix(-10597348.02452914), sfix(-3952865.9990937426), sfix(-842317.6870917304), sfix(-99977.1548142894), sfix(-5172.34679966028), sfix(1.0), sfix(1.0)],
        [sfix(253220924.07969743), sfix(692051604.4087394), sfix(795742437.7148292), sfix(485649210.3408187), sfix(165882156.46899486), sfix(30101734.061107777), sfix(2269251.4999527223), sfix(1.0), sfix(1.0)],
        [sfix(2781387.879413496), sfix(28314001.528992485), sfix(83933709.18331608), sfix(95779479.05813995), sfix(53920415.19970317), sfix(15098714.007566309), sfix(1683824.5664794052), sfix(1.0), sfix(1.0)],
        [sfix(-43979035.935946696), sfix(-205488614.97039214), sfix(-376393586.4898138), sfix(-370485156.92470723), sfix(-205230198.57799894), sfix(-60353613.16979712), sfix(-7346958.389791285), sfix(1.0), sfix(1.0)],
        [sfix(-5177238.533986021), sfix(-44790184.85880444), sfix(-118901626.81216554), sfix(-180261524.00205082), sfix(-153356257.3384759), sfix(-68077792.06465694), sfix(-12314090.311473973), sfix(1.0), sfix(1.0)],
        [sfix(266516.32293553604), sfix(-2661829.399647066), sfix(12244055.724241361), sfix(29112865.918497644), sfix(25599443.250703786), sfix(7850551.08339258), sfix(-468381.20825498464), sfix(1.0), sfix(1.0)],
        [sfix(-82856.6135864454), sfix(-6345312.920773527), sfix(-2826263.5090009547), sfix(399348.6449866812), sfix(4335238.151739232), sfix(12727748.37817865), sfix(10243182.406977795), sfix(1.0), sfix(1.0)],
        [sfix(-82872.80124469912), sfix(-6346667.844699024), sfix(-2864986.9994921377), sfix(-99050.07250257218), sfix(1084677.2694977089), sfix(1757749.8347537385), sfix(-6353291.488500454), sfix(1.0), sfix(1.0)],
        [sfix(-82859.86961208272), sfix(-6346106.134887822), sfix(-2900884.212809753), sfix(286952.4860168922), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(-112569.20119297282), sfix(-5787775.641097328), sfix(-7087438.193041297), sfix(16097948.365433434), sfix(-31115882.51238829), sfix(29728360.695529032), sfix(-10918017.753818894), sfix(1.0), sfix(1.0)],
        [sfix(-4927675.973013808), sfix(31535874.795652747), sfix(-121236070.99216674), sfix(190031051.2292681), sfix(-165431572.11218554), sfix(74516049.75895137), sfix(-13598208.335832534), sfix(1.0), sfix(1.0)],
        [sfix(-44097674.438769825), sfix(189371857.99673054), sfix(-362604916.32990104), sfix(350546160.0152791), sfix(-190979125.42674744), sfix(55275067.24582638), sfix(-6625277.766630632), sfix(1.0), sfix(1.0)],
        [sfix(-80624288.17517626), sfix(247376535.0364136), sfix(-331828719.9730615), sfix(224826921.44075993), sfix(-85389948.06434724), sfix(17207488.2165664), sfix(-1436314.0876438988), sfix(1.0), sfix(1.0)],
        [sfix(-1819517.2495114605), sfix(-1708325.2355468706), sfix(-7957435.925109995), sfix(2690677.271790425), sfix(-503473.44644883665), sfix(51548.43765263974), sfix(-2293.40033123682), sfix(1.0), sfix(1.0)],
        [sfix(2409075.9164439663), sfix(-8472556.023628585), sfix(-3405888.2356256), sfix(1035218.972036214), sfix(-158786.81754519758), sfix(12438.4911948775), sfix(-397.93253649493), sfix(1.0), sfix(1.0)],
        [sfix(10335496.967700113), sfix(-17916020.448649053), sfix(1188215.3790491654), sfix(-142324.25528955794), sfix(9704.18640238846), sfix(-355.98179672688), sfix(5.47449252583), sfix(1.0), sfix(1.0)],
        [sfix(29740.33672938146), sfix(-12547658.949903045), sfix(510.92484827481), sfix(-21.70613448163), sfix(0.50084116297), sfix(-0.00597395859), sfix(2.888006e-05), sfix(1.0), sfix(1.0)]
    ]
    scaler = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)]
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
        sfix(-50.0),
        sfix(-15.625),
        sfix(-12.5),
        sfix(-10.9375),
        sfix(-9.375),
        sfix(-7.8125),
        sfix(-6.25),
        sfix(-4.6875),
        sfix(-3.125),
        sfix(-2.34375),
        sfix(-1.953125),
        sfix(-1.5625),
        sfix(-1.171875),
        sfix(-0.9765625),
        sfix(-0.78125),
        sfix(-0.5859375),
        sfix(-0.390625),
        sfix(-0.1953125),
        sfix(-0.048828125),
        sfix(0.0),
        sfix(0.048828125),
        sfix(0.1953125),
        sfix(0.390625),
        sfix(0.439453125),
        sfix(0.78125),
        sfix(1.171875),
        sfix(1.5625),
        sfix(1.953125),
        sfix(2.34375),
        sfix(6.25),
        sfix(12.5)
    ]
    coeffA = [
        [sfix(1104.69585248726), sfix(210.57632178913), sfix(16.23456273637), sfix(0.64913408203), sfix(0.01422820234), sfix(0.00016245563), sfix(7.5652e-07), sfix(1.0), sfix(1.0)],
        [sfix(465298.35874293186), sfix(178099.9587331809), sfix(28628.92218600482), sfix(2471.08282539929), sfix(120.6772607941), sfix(3.15896909359), sfix(0.03460485315), sfix(1.0), sfix(1.0)],
        [sfix(1287737.7329066899), sfix(568860.6717625973), sfix(106126.27716364287), sfix(10682.88698115828), sfix(611.00161699259), sfix(18.80083026529), sfix(0.24287709224), sfix(1.0), sfix(1.0)],
        [sfix(2244819.034983952), sfix(1097617.4254863118), sfix(227989.494573987), sfix(25679.8477122556), sfix(1650.35819027056), sfix(57.26218022233), sfix(0.83657253872), sfix(1.0), sfix(1.0)],
        [sfix(3277155.3338213363), sfix(1759997.8742479288), sfix(405363.191689921), sfix(51052.999541479), sfix(3695.30715408505), sfix(145.30271412104), sfix(2.4183876007), sfix(1.0), sfix(1.0)],
        [sfix(3624471.240667814), sfix(2013114.205353743), sfix(482107.33810014906), sfix(63440.72674838111), sfix(4817.69452926977), sfix(199.40397969744), sfix(3.50175119101), sfix(1.0), sfix(1.0)],
        [sfix(2264600.5555811697), sfix(652600.7613275097), sfix(-86629.99961044418), sfix(-63691.60619019101), sfix(-11206.56187929257), sfix(-880.21400948569), sfix(-26.86782738603), sfix(1.0), sfix(1.0)],
        [sfix(-88557.55942928304), sfix(-2397486.3692742465), sfix(-1744470.9198982972), sfix(-547322.3330579654), sfix(-91056.05488868747), sfix(-7952.86746620201), sfix(-289.34617663401), sfix(1.0), sfix(1.0)],
        [sfix(-355358.1822062396), sfix(-2808118.436410581), sfix(-1998240.1682397127), sfix(-626135.7950858192), sfix(-103398.97441054712), sfix(-8745.30234611152), sfix(-291.98405943656), sfix(1.0), sfix(1.0)],
        [sfix(34762787.66799142), sfix(91618270.28128254), sfix(103823303.43264283), sfix(62639379.8930815), sfix(21177020.270858627), sfix(3809594.2093115323), sfix(285220.94118272985), sfix(1.0), sfix(1.0)],
        [sfix(-228244538.279699), sfix(-775823105.4922559), sfix(-1085543000.7767317), sfix(-805378388.660103), sfix(-334542612.29208106), sfix(-73818439.27348067), sfix(-6763768.8794970615), sfix(1.0), sfix(1.0)],
        [sfix(346386936.85724556), sfix(1447805938.4565504), sfix(2503940270.674938), sfix(2288467439.620431), sfix(1167130602.412381), sfix(315339798.6845225), sfix(35301890.01158672), sfix(1.0), sfix(1.0)],
        [sfix(-182027342.34942406), sfix(-1020920839.7525654), sfix(-2276233080.586691), sfix(-2615959438.428587), sfix(-1640670545.3268971), sfix(-533379652.3585731), sfix(-70220100.67003399), sfix(1.0), sfix(1.0)],
        [sfix(217836774.08863178), sfix(1321836391.0068579), sfix(3436438410.4566803), sfix(4803539117.401942), sfix(3771348257.3993015), sfix(1568245225.0452914), sfix(269106137.2451568), sfix(1.0), sfix(1.0)],
        [sfix(-22891930.76070145), sfix(-490226314.31632084), sfix(-2260126106.694437), sfix(-4770474236.990528), sfix(-5302108045.853448), sfix(-3029590260.6825233), sfix(-704198799.1254967), sfix(1.0), sfix(1.0)],
        [sfix(1521498.1301074426), sfix(-215055963.73128426), sfix(-969527864.2466899), sfix(-1545075911.5067134), sfix(-770727537.8933426), sfix(364308991.8881644), sfix(354661365.1138413), sfix(1.0), sfix(1.0)],
        [sfix(15452640.846230876), sfix(-23427852.970863942), sfix(124142702.3749316), sfix(1762951157.2163417), sfix(4804971258.868243), sfix(5306997120.854788), sfix(2142200371.657942), sfix(1.0), sfix(1.0)],
        [sfix(14668446.499187192), sfix(-43901644.31330728), sfix(-101086862.4469943), sfix(421705489.1908151), sfix(227094324.3234734), sfix(-3216406043.8832865), sfix(-4642654360.337143), sfix(1.0), sfix(1.0)],
        [sfix(14668479.71851304), sfix(-43908896.188341364), sfix(-102345125.74472956), sfix(381046641.9943723), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(14668479.718513036), sfix(-43895181.576806836), sfix(-101132083.76925202), sfix(442702085.5217288), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(14668676.938266637), sfix(-43913627.815554455), sfix(-100254038.99545482), sfix(416209431.02086437), sfix(456659035.88707125), sfix(-3441182343.316482), sfix(3948961353.0410047), sfix(1.0), sfix(1.0)],
        [sfix(14045480.274409022), sfix(-27663591.895870097), sfix(-278613348.9810228), sfix(1474392744.650789), sfix(-3134588348.508574), sfix(3190886170.2695265), sfix(-1272427606.9107752), sfix(1.0), sfix(1.0)],
        [sfix(16887690.477230858), sfix(-69088545.47402911), sfix(-30365529.445959512), sfix(695314819.2326471), sfix(-1794341122.7126644), sfix(2007428545.3509269), sfix(-862913569.3066193), sfix(1.0), sfix(1.0)],
        [sfix(22478631.666114904), sfix(-155608018.35784593), sfix(505332608.5073781), sfix(-1026157993.2212228), sfix(1258353189.5473838), sfix(-840027781.9708298), sfix(232638658.59669816), sfix(1.0), sfix(1.0)],
        [sfix(53973118.43858155), sfix(-331961500.1637101), sfix(832405753.2345986), sfix(-1126655685.1645248), sfix(858557747.5789981), sfix(-348568886.99113226), sfix(58806505.14079023), sfix(1.0), sfix(1.0)],
        [sfix(98749415.23276353), sfix(-471225873.1256597), sfix(911621440.2294841), sfix(-937638690.0188658), sfix(537664537.1979814), sfix(-163056593.49553576), sfix(20440232.679764993), sfix(1.0), sfix(1.0)],
        [sfix(360702492.2977495), sfix(-1311614395.1294212), sfix(1967582243.2365816), sfix(-1571207339.3617566), sfix(702749727.3113145), sfix(-166884485.5347417), sfix(16431336.995150436), sfix(1.0), sfix(1.0)],
        [sfix(1151781888.8427854), sfix(-3205629038.0746384), sfix(3691216601.371247), sfix(-2258556574.9225326), sfix(774129514.101123), sfix(-141016346.7098198), sfix(10671165.089939613), sfix(1.0), sfix(1.0)],
        [sfix(19311.91192901879), sfix(-1538218.7517792466), sfix(-1558650.1112470885), sfix(471342.600102285), sfix(-74349.20361819693), sfix(6063.39374582043), sfix(-202.94437566007), sfix(1.0), sfix(1.0)],
        [sfix(3055036.592091886), sfix(-5295739.355972669), sfix(351220.79505410255), sfix(-42069.1727944415), sfix(2868.42951512777), sfix(-105.22352418203), sfix(1.6181877893), sfix(1.0), sfix(1.0)],
        [sfix(8790.85130032175), sfix(-3708922.498545438), sfix(151.02264670273), sfix(-6.41604707647), sfix(0.14804204231), sfix(-0.00176582337), sfix(8.53657e-06), sfix(1.0), sfix(1.0)]
    ]
    scaler = [
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)]
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
        sfix(-50.0),
        sfix(-25.0),
        sfix(-12.5),
        sfix(-6.25),
        sfix(-3.125),
        sfix(-2.34375),
        sfix(-1.5625),
        sfix(-1.171875),
        sfix(-0.78125),
        sfix(-0.390625),
        sfix(-0.09765625),
        sfix(0.0),
        sfix(0.09765625),
        sfix(0.1953125),
        sfix(0.390625),
        sfix(0.78125),
        sfix(1.171875),
        sfix(1.5625),
        sfix(1.953125),
        sfix(3.125),
        sfix(6.25),
        sfix(12.5)
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
        [sfix(-5.27431101282), sfix(-0.83470573362), sfix(-0.05448780507), sfix(-0.00187834205), sfix(-3.607593e-05), sfix(-3.6615e-07), sfix(-1.53e-09), sfix(1.0), sfix(1.0)],
        [sfix(-245714.43908078567), sfix(-75064.74166477137), sfix(-9506.49396294439), sfix(-638.50093979049), sfix(-23.97907843507), sfix(-0.47733700524), sfix(-0.00393457353), sfix(1.0), sfix(1.0)],
        [sfix(-8614415.362626703), sfix(-4479555.759162216), sfix(-990352.069883812), sfix(-118624.21855905141), sfix(-8088.23152724915), sfix(-296.70320333921), sfix(-4.56287227042), sfix(1.0), sfix(1.0)],
        [sfix(-2007913.180281271), sfix(3391369.5840843455), sfix(2838734.8989453753), sfix(862832.8414411121), sfix(132345.41161500826), sfix(10367.21601013329), sfix(331.6682464665), sfix(1.0), sfix(1.0)],
        [sfix(916235.0074272883), sfix(7732927.957929732), sfix(5468155.6584200505), sfix(1685998.8573821278), sfix(270204.6337973064), sfix(21607.54384852893), sfix(641.89010497787), sfix(1.0), sfix(1.0)],
        [sfix(-94284270.1836299), sfix(-313426256.3606669), sfix(-432054135.3935203), sfix(-309036839.81160283), sfix(-121710682.40299168), sfix(-25166555.65898583), sfix(-2142140.526271814), sfix(1.0), sfix(1.0)],
        [sfix(200381797.25078207), sfix(873790318.7850125), sfix(1540898916.1864314), sfix(1425256074.9622602), sfix(730000090.6977997), sfix(196643810.99546406), sfix(21810759.400859464), sfix(1.0), sfix(1.0)],
        [sfix(3135174.5623634667), sfix(70405257.39554131), sfix(279611884.8598483), sfix(522792539.09252685), sfix(507212126.71689), sfix(247389169.7487614), sfix(48008169.473201185), sfix(1.0), sfix(1.0)],
        [sfix(-2802417.488205752), sfix(-15043325.372914268), sfix(-107560848.39443265), sfix(-311925724.9252516), sfix(-444710041.7825303), sfix(-310108208.9492179), sfix(-84666667.97506946), sfix(1.0), sfix(1.0)],
        [sfix(-1214141.1410272962), sfix(5767768.883158716), sfix(6058919.384252044), sfix(18071209.04722034), sfix(90531467.87366961), sfix(145803402.4900123), sfix(72350236.63205007), sfix(1.0), sfix(1.0)],
        [sfix(-1218536.6164852702), sfix(5603358.71037684), sfix(3482592.4182481365), sfix(-3308184.2529576556), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(-1218536.6164852702), sfix(5606635.372345885), sfix(3589341.2252513077), sfix(519434.79627901054), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(-1218531.8207421373), sfix(5605397.190155915), sfix(3661289.012597918), sfix(-1012190.3985023553), sfix(14096575.311393308), sfix(-53571465.53832897), sfix(57812300.11147311), sfix(1.0), sfix(1.0)],
        [sfix(-1228629.1068106329), sfix(5866592.646932477), sfix(822919.735016496), sfix(15617549.086488351), sfix(-41460755.26153144), sfix(47044508.79277763), sfix(-19536016.222701445), sfix(1.0), sfix(1.0)],
        [sfix(-668745.0996458482), sfix(-1059899.9903150839), sfix(36370774.632435575), sfix(-81124559.11755244), sfix(105390662.46885867), sfix(-70262737.24348824), sfix(18642167.31161442), sfix(1.0), sfix(1.0)],
        [sfix(6892764.2141741915), sfix(-35063036.201808825), sfix(78859145.94993073), sfix(-56953065.2802908), sfix(3716207.0391341583), sfix(15296305.916136792), sfix(-5457113.358024648), sfix(1.0), sfix(1.0)],
        [sfix(-143707238.24271843), sfix(684473246.3351624), sfix(-1328579756.824247), sfix(1378197811.3869417), sfix(-794199273.3481255), sfix(241355349.69377095), sfix(-30246844.17568613), sfix(1.0), sfix(1.0)],
        [sfix(-290730755.66428906), sfix(971886431.9849222), sfix(-1331670049.3705382), sfix(978112151.1078781), sfix(-401854380.7410629), sfix(87638826.96008985), sfix(-7931593.889290913), sfix(1.0), sfix(1.0)],
        [sfix(-31362914.263647694), sfix(75762035.7738174), sfix(-63195498.67721684), sfix(32636928.814559553), sfix(-9351712.841921456), sfix(1412673.2393980753), sfix(-88175.17948669124), sfix(1.0), sfix(1.0)],
        [sfix(-2007913.1801507906), sfix(7061693.985358739), sfix(2838734.8990360154), sfix(-862832.8414664973), sfix(132345.4116189463), sfix(-10367.2160104544), sfix(331.66824647726), sfix(1.0), sfix(1.0)],
        [sfix(-8614415.362861509), sfix(14932619.3289308), sfix(-990352.0699262192), sfix(118624.21856513411), sfix(-8088.23152773379), sfix(296.70320335956), sfix(-4.56287227077), sfix(1.0), sfix(1.0)],
        [sfix(-24787.93369075896), sfix(10458204.99619346), sfix(-425.84491806356), sfix(18.09159818721), sfix(-0.41744038224), sfix(0.00497916653), sfix(-2.407091e-05), sfix(1.0), sfix(1.0)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)]
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
        sfix(-50.0),
        sfix(-12.5),
        sfix(-6.25),
        sfix(-1.953125),
        sfix(-1.3671875),
        sfix(-1.26953125),
        sfix(-1.171875),
        sfix(-1.07421875),
        sfix(-0.78125),
        sfix(-0.390625),
        sfix(-0.09765625),
        sfix(0.0),
        sfix(0.0244140625),
        sfix(0.09765625),
        sfix(0.1953125),
        sfix(0.390625),
        sfix(0.5859375),
        sfix(0.9765625),
        sfix(1.171875),
        sfix(1.3671875),
        sfix(1.5625),
        sfix(1.7578125),
        sfix(1.953125),
        sfix(2.34375),
        sfix(6.25),
        sfix(12.5)
    ]
    coeffA = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-1736.85458575838), sfix(-360.25230847948), sfix(-29.8383361894), sfix(-1.26765206316), sfix(-0.02924944255), sfix(-0.00034888298), sfix(-1.68661e-06), sfix(1.0), sfix(1.0)],
        [sfix(-603599.598362744), sfix(-313875.97918767633), sfix(-69392.53407874938), sfix(-8311.82705549319), sfix(-566.73065969085), sfix(-20.78956340386), sfix(-0.31971384637), sfix(1.0), sfix(1.0)],
        [sfix(78805.85804413122), sfix(557013.2197248047), sfix(388627.391457412), sfix(119350.41429201372), sfix(19355.04241683168), sfix(1629.7076455801), sfix(56.36953851427), sfix(1.0), sfix(1.0)],
        [sfix(-292922734.97421074), sfix(-1006550063.411701), sfix(-1424191944.8314612), sfix(-1064204890.7840371), sfix(-443786675.80774367), sfix(-98068324.91143472), sfix(-8981605.858830871), sfix(1.0), sfix(1.0)],
        [sfix(529556387.40229464), sfix(2332821991.5192246), sfix(4225571552.078196), sfix(4034151077.179993), sfix(2144326248.3048413), sfix(602670442.8169098), sfix(70072498.6720788), sfix(1.0), sfix(1.0)],
        [sfix(22751125.382360168), sfix(-75440462.22139111), sfix(-544163225.8578407), sfix(-1005739776.4224069), sfix(-852123681.0612587), sfix(-347774002.8861495), sfix(-55579337.38086816), sfix(1.0), sfix(1.0)],
        [sfix(-350842103.45775795), sfix(-1965799034.1566193), sfix(-4530562434.968985), sfix(-5490308659.298339), sfix(-3690628500.5669127), sfix(-1306215656.0645707), sfix(-190457209.13504997), sfix(1.0), sfix(1.0)],
        [sfix(39926302.22452452), sfix(332528443.2872508), sfix(1107863188.283202), sfix(1894571773.588022), sfix(1755245095.4569125), sfix(837565062.6961559), sfix(161463808.8935262), sfix(1.0), sfix(1.0)],
        [sfix(-991138.9862537979), sfix(-5819820.252087557), sfix(-51332620.29243167), sfix(-215034174.26491645), sfix(-398428802.44046634), sfix(-333061674.18854177), sfix(-103429849.76012902), sfix(1.0), sfix(1.0)],
        [sfix(-155818.42710491002), sfix(5566626.4411518825), sfix(13634952.848105205), sfix(-16480748.412875256), sfix(-55903141.662532635), sfix(-17320761.471532486), sfix(17759628.884359237), sfix(1.0), sfix(1.0)],
        [sfix(-157151.5494578644), sfix(5530714.531403431), sfix(13706770.483489944), sfix(-8133560.8046478005), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(-157151.5494578644), sfix(5519551.8302029595), sfix(13037258.812830482), sfix(-24059093.211198818), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(-157151.46825752876), sfix(5519723.57489914), sfix(12990189.73443518), sfix(-20782918.251289472), sfix(-67007291.28214548), sfix(-16424730.353038894), sfix(258712310.7804744), sfix(1.0), sfix(1.0)],
        [sfix(-157599.61974855894), sfix(5541778.962115224), sfix(12537402.555083638), sfix(-15807292.155429542), sfix(-97969589.7726862), sfix(87403309.6953945), sfix(111522987.35835347), sfix(1.0), sfix(1.0)],
        [sfix(-203447.36184502603), sfix(6791514.536111988), sfix(-1833393.5233826546), sfix(73619609.01541495), sfix(-416212704.77986646), sfix(702443787.4223748), sfix(-393268221.8007075), sfix(1.0), sfix(1.0)],
        [sfix(2807971.0471293572), sfix(-36586570.705105744), sfix(259936460.6475365), sfix(-773922433.5389448), sfix(1137370676.7099955), sfix(-826902788.2295893), sfix(238593237.32981104), sfix(1.0), sfix(1.0)],
        [sfix(-21491572.102932453), sfix(188119880.41844833), sfix(-606382362.5288476), sfix(1007963965.5418423), sfix(-924074445.1383086), sfix(444202310.4078222), sfix(-87513764.37551834), sfix(1.0), sfix(1.0)],
        [sfix(99123072.31948522), sfix(-558879734.9865094), sfix(1326719883.84207), sfix(-1667694530.6208067), sfix(1165133826.823642), sfix(-428339923.4301686), sfix(64761446.67066365), sfix(1.0), sfix(1.0)],
        [sfix(-186781481.8039921), sfix(867180060.7754042), sfix(-1638286120.2867966), sfix(1621555620.146305), sfix(-888284204.2268192), sfix(255641856.06916347), sfix(-30209165.050039794), sfix(1.0), sfix(1.0)],
        [sfix(13705483.390514204), sfix(48981697.325799055), sfix(-254143857.6888685), sfix(380337388.9245347), sfix(-266764314.2044357), sfix(91134348.17681937), sfix(-12265857.845127974), sfix(1.0), sfix(1.0)],
        [sfix(554982678.2771903), sfix(-2056152003.2041683), sfix(3159512415.905569), sfix(-2573900579.5822244), sfix(1172284814.1170912), sfix(-282960000.8178083), sfix(28279998.3840319), sfix(1.0), sfix(1.0)],
        [sfix(-881043391.7412606), sfix(2778784925.1082516), sfix(-3625802933.070586), sfix(2506678697.466405), sfix(-968373642.2374661), sfix(198268972.65519416), sfix(-16814068.218963094), sfix(1.0), sfix(1.0)],
        [sfix(957252251.8073453), sfix(-2628806318.8801146), sfix(2997171677.3551235), sfix(-1815863481.3984096), sfix(617060713.6917527), sfix(-111554189.42187019), sfix(8384639.862588842), sfix(1.0), sfix(1.0)],
        [sfix(-17055.09081029763), sfix(322903.9420220576), sfix(296857.91205682664), sfix(-89743.30227056135), sfix(14120.93959057988), sfix(-1147.92670851003), sfix(38.2921723915), sfix(1.0), sfix(1.0)],
        [sfix(-603599.5983824335), sfix(1046306.9924127086), sfix(-69392.5340822342), sfix(8311.82705598746), sfix(-566.73065972976), sfix(20.78956340547), sfix(-0.3197138464), sfix(1.0), sfix(1.0)],
        [sfix(-1736.85458546149), sfix(732791.2655205098), sfix(-29.83833618155), sfix(1.26765206277), sfix(-0.02924944254), sfix(0.00034888298), sfix(-1.68661e-06), sfix(1.0), sfix(1.0)]
    ]
    scaler = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)]
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
        sfix(-50.0),
        sfix(-12.5),
        sfix(-9.375),
        sfix(-6.25),
        sfix(-3.125),
        sfix(-1.5625),
        sfix(-1.171875),
        sfix(-0.78125),
        sfix(-0.390625),
        sfix(-0.09765625),
        sfix(0.048828125),
        sfix(0.09765625),
        sfix(0.1953125),
        sfix(0.390625),
        sfix(0.5859375),
        sfix(0.78125),
        sfix(1.171875),
        sfix(1.5625),
        sfix(1.953125),
        sfix(2.34375),
        sfix(6.25),
        sfix(12.5)
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
        [sfix(-5334.65032493903), sfix(-1106.4945276642), sfix(-91.64675681754), sfix(-3.89352139559), sfix(-0.08983800342), sfix(-0.00107157429), sfix(-5.18034e-06), sfix(1.0), sfix(1.0)],
        [sfix(-1087071.5027819513), sfix(-506674.2398533395), sfix(-99916.1952306748), sfix(-10645.27952313299), sfix(-644.96058910867), sfix(-21.03250329405), sfix(-0.28799660068), sfix(1.0), sfix(1.0)],
        [sfix(-2183070.379936722), sfix(-1208792.4791226506), sfix(-288409.43292088155), sfix(-37789.9431941776), sfix(-2856.40863316372), sfix(-117.65872293959), sfix(-2.05666800467), sfix(1.0), sfix(1.0)],
        [sfix(-432126.1638348533), sfix(729861.999467482), sfix(610928.6168707708), sfix(185691.61727927675), sfix(28482.2648628399), sfix(2231.14491607661), sfix(71.37884666476), sfix(1.0), sfix(1.0)],
        [sfix(-6951926.406696198), sfix(-16045552.60904415), sfix(-16963896.73974724), sfix(-9472180.464813674), sfix(-2918487.588514), sfix(-472260.90415601246), sfix(-31468.48419565166), sfix(1.0), sfix(1.0)],
        [sfix(-83761591.17652866), sfix(-365662225.64405185), sfix(-659706568.9616992), sfix(-626256239.1840396), sfix(-330720113.213133), sfix(-92323515.73010805), sfix(-10662124.012296483), sfix(1.0), sfix(1.0)],
        [sfix(318820.84142931143), sfix(-8487491.946790084), sfix(-59961383.740335695), sfix(-136482090.8225888), sfix(-146608913.05803922), sfix(-76042659.26356342), sfix(-15362487.25730805), sfix(1.0), sfix(1.0)],
        [sfix(688954.3158958674), sfix(12049289.684553761), sfix(57046990.880290285), sfix(143141716.83875975), sfix(192606837.18347242), sfix(131473765.99057434), sfix(35745095.52719425), sfix(1.0), sfix(1.0)],
        [sfix(-108616.17085763285), sfix(1547425.4384383538), sfix(-237330.96578183357), sfix(-21531322.946891386), sfix(-67677643.60949846), sfix(-78735107.27281187), sfix(-29197566.547386855), sfix(1.0), sfix(1.0)],
        [sfix(-105127.79715991674), sfix(1670741.0181279443), sfix(1614552.7793814929), sfix(-5867535.647765028), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(-105168.77963059524), sfix(1674028.8011064525), sfix(1633262.8234696048), sfix(-6985180.462534136), sfix(-9001993.468351565), sfix(64180796.72984686), sfix(-51236869.866558164), sfix(1.0), sfix(1.0)],
        [sfix(-105211.9123379029), sfix(1676368.9905002906), sfix(1579471.5391130317), sfix(-6312579.875956686), sfix(-13839617.234903943), sfix(83188744.15782575), sfix(-83127864.33476251), sfix(1.0), sfix(1.0)],
        [sfix(-93197.3173636968), sfix(1380251.7641613265), sfix(4621059.005928077), sfix(-23007512.898345117), sfix(37910748.34908425), sfix(-2895313.994589649), sfix(-22955116.898273762), sfix(1.0), sfix(1.0)],
        [sfix(250106.8821696942), sfix(-4004428.3027000115), sfix(40049501.32859414), sfix(-148217623.02018988), sfix(288672115.6826002), sfix(-272755615.6154187), sfix(98954902.91980164), sfix(1.0), sfix(1.0)],
        [sfix(-8746215.459094344), sfix(85549038.71991266), sfix(-332666136.30323464), sfix(682081978.7762053), sfix(-755672556.330403), sfix(430538491.6285779), sfix(-99174463.03801185), sfix(1.0), sfix(1.0)],
        [sfix(32116674.705889862), sfix(-217611189.43701988), sfix(604374541.2931856), sfix(-862560411.6262128), sfix(676621889.9185939), sfix(-277851737.2716443), sfix(46827992.507492155), sfix(1.0), sfix(1.0)],
        [sfix(43828649.09935811), sfix(-167699284.519478), sfix(264502178.5182171), sfix(-209394236.92515206), sfix(86134311.78808104), sfix(-16314543.262049356), sfix(875126.9221942176), sfix(1.0), sfix(1.0)],
        [sfix(-420530895.5774324), sfix(1511662944.7455707), sfix(-2242705857.3520646), sfix(1764444583.1328137), sfix(-775644723.9296376), sfix(180717775.17076015), sfix(-17440761.13600684), sfix(1.0), sfix(1.0)],
        [sfix(-544923157.475038), sfix(1494871722.6597216), sfix(-1698872480.0624888), sfix(1027725595.5499415), sfix(-348652533.02160543), sfix(62918184.0331921), sfix(-4720367.415031108), sfix(1.0), sfix(1.0)],
        [sfix(-15256.63047039452), sfix(938528.2269985613), sfix(942889.2396684088), sfix(-285126.3887806762), sfix(44966.23056157152), sfix(-3666.14443168652), sfix(122.67283844596), sfix(1.0), sfix(1.0)],
        [sfix(-1853921.922999588), sfix(3213672.5681004194), sfix(-213135.23165238363), sfix(25529.30525530794), sfix(-1740.68106954852), sfix(63.85396456436), sfix(-0.98198294117), sfix(1.0), sfix(1.0)],
        [sfix(-5334.65032368306), sfix(2250726.7993390765), sfix(-91.64675678757), sfix(3.89352139412), sfix(-0.08983800338), sfix(0.00107157429), sfix(-5.18034e-06), sfix(1.0), sfix(1.0)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)]
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
        sfix(-50.0),
        sfix(-14.0625),
        sfix(-12.5),
        sfix(-10.9375),
        sfix(-9.375),
        sfix(-7.8125),
        sfix(-6.25),
        sfix(-4.6875),
        sfix(-3.125),
        sfix(-2.34375),
        sfix(-1.953125),
        sfix(-1.5625),
        sfix(-1.3671875),
        sfix(-1.171875),
        sfix(-0.9765625),
        sfix(-0.78125),
        sfix(-0.5859375),
        sfix(-0.1953125),
        sfix(-0.09765625),
        sfix(-0.048828125),
        sfix(0.0),
        sfix(0.09765625),
        sfix(0.390625),
        sfix(0.78125),
        sfix(3.125),
        sfix(6.25),
        sfix(12.5)
    ]
    coeffA = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(9271.09318496078), sfix(1839.80042010932), sfix(146.81617414267), sfix(6.04565857763), sfix(0.13588401312), sfix(0.00158526705), sfix(7.52043e-06), sfix(1.0), sfix(1.0)],
        [sfix(1918705.713082564), sfix(768199.0199255031), sfix(129415.47997423628), sfix(11727.57660103556), sfix(602.2746454001), sfix(16.6042666156), sfix(0.19183578102), sfix(1.0), sfix(1.0)],
        [sfix(3802256.0880712275), sfix(1679654.0919803204), sfix(313355.17562196875), sfix(31542.96952271028), sfix(1804.08211910526), sfix(55.51252363765), sfix(0.71713430384), sfix(1.0), sfix(1.0)],
        [sfix(6628195.030900651), sfix(3240894.8124799426), sfix(673176.2389223388), sfix(75823.94676268182), sfix(4872.95224491029), sfix(169.07594442698), sfix(2.47011712647), sfix(1.0), sfix(1.0)],
        [sfix(9676336.649287058), sfix(5196681.328318756), sfix(1196901.0646364503), sfix(150742.32381441328), sfix(10910.99822965594), sfix(429.03000763797), sfix(7.14068458445), sfix(1.0), sfix(1.0)],
        [sfix(10701843.619674383), sfix(5944048.658022274), sfix(1423500.6977823826), sfix(187319.11268797217), sfix(14225.03036562631), sfix(588.77283500296), sfix(10.33949261841), sfix(1.0), sfix(1.0)],
        [sfix(6686603.202994921), sfix(1926910.3905224444), sfix(-255789.2302323882), sfix(-188059.8752450299), sfix(-33089.20523446128), sfix(-2598.97570047104), sfix(-79.33165088064), sfix(1.0), sfix(1.0)],
        [sfix(-261480.66555351036), sfix(-7078970.283033579), sfix(-5150835.458271888), sfix(-1616058.6273241322), sfix(-268857.8816995897), sfix(-23482.14078692812), sfix(-854.34186911148), sfix(1.0), sfix(1.0)],
        [sfix(3643432.8859562417), sfix(1842029.0211669696), sfix(3200766.7530062385), sfix(2502531.8492614804), sfix(862837.4750256643), sfix(141132.39454775327), sfix(9062.81869627023), sfix(1.0), sfix(1.0)],
        [sfix(-593422143.6649352), sfix(-1632380709.5984304), sfix(-1853471198.774374), sfix(-1118818865.1912522), sfix(-378982626.35815084), sfix(-68312762.64404134), sfix(-5119852.108505643), sfix(1.0), sfix(1.0)],
        [sfix(-903391050.6377012), sfix(-3163031503.5471487), sfix(-4570692125.248592), sfix(-3504476453.5865855), sfix(-1504436421.3994184), sfix(-342925692.73510057), sfix(-32433337.38139521), sfix(1.0), sfix(1.0)],
        [sfix(628204264.6039258), sfix(2459618648.799102), sfix(4017301892.6606092), sfix(3480035587.6465855), sfix(1685026573.7766361), sfix(432284917.15072453), sfix(45896062.601444386), sfix(1.0), sfix(1.0)],
        [sfix(-449765666.3934596), sfix(-2092303510.3617725), sfix(-3984118598.414902), sfix(-4013488574.1006804), sfix(-2257932168.218382), sfix(-672788303.2043025), sfix(-82962595.66193435), sfix(1.0), sfix(1.0)],
        [sfix(248703227.3804917), sfix(1358208750.3277667), sfix(3115110005.3813744), sfix(3772413867.475117), sfix(2542342243.221721), sfix(904530981.5010958), sfix(132819585.39522085), sfix(1.0), sfix(1.0)],
        [sfix(-108492986.78786206), sfix(-766642254.8698528), sfix(-2153004097.363747), sfix(-3195258554.890058), sfix(-2642540268.4294906), sfix(-1153594984.9756153), sfix(-207636975.27324876), sfix(1.0), sfix(1.0)],
        [sfix(16736643.639260162), sfix(172041491.7393442), sfix(783803945.3293512), sfix(1713964176.6067894), sfix(1982115075.5554893), sfix(1174356828.0070457), sfix(281585293.50750184), sfix(1.0), sfix(1.0)],
        [sfix(-595217.6077198474), sfix(-9153110.943194184), sfix(-12362808.169458378), sfix(-169106106.3589874), sfix(-547297875.8220712), sfix(-655478417.6344998), sfix(-275346601.0584473), sfix(1.0), sfix(1.0)],
        [sfix(-497197.74089270545), sfix(-6709351.495169221), sfix(13245487.454090903), sfix(-24148475.124362126), sfix(-77753295.80881941), sfix(173361337.52277115), sfix(349925902.72998583), sfix(1.0), sfix(1.0)],
        [sfix(-496935.18612050865), sfix(-6696921.978746011), sfix(13487630.770031214), sfix(-21672742.456319116), sfix(-63833057.943863586), sfix(213675406.66171318), sfix(395737128.13526064), sfix(1.0), sfix(1.0)],
        [sfix(-496937.67980165646), sfix(-6695357.189388006), sfix(13709575.210094146), sfix(-14224840.572390277), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(-496937.67980165663), sfix(-6703084.775347538), sfix(13889457.276412867), sfix(-30594646.952519454), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(-492042.11211762694), sfix(-6871855.588899768), sfix(15953354.608709872), sfix(-39569360.014696084), sfix(-6442910.507203707), sfix(104153955.46304917), sfix(-89515686.40189448), sfix(1.0), sfix(1.0)],
        [sfix(-813587.7191283613), sfix(-3672061.5098889037), sfix(5906408.71921045), sfix(-40385543.58608414), sfix(65310308.79345328), sfix(-48018125.61420008), sfix(13695234.02935937), sfix(1.0), sfix(1.0)],
        [sfix(-58182.5035088471), sfix(-5235449.226501123), sfix(-3100298.5590428277), sfix(233702.0053128252), sfix(216044.42198997), sfix(-63316.58655551174), sfix(5436.86068376134), sfix(1.0), sfix(1.0)],
        [sfix(2102565.2435011608), sfix(-7394578.849673077), sfix(-2972551.4993782802), sfix(903506.3673903459), sfix(-138584.11078710447), sfix(10855.92159615204), sfix(-347.3029283905), sfix(1.0), sfix(1.0)],
        [sfix(9020494.767582186), sfix(-15636535.835371844), sfix(1037036.7910713946), sfix(-124216.10728133615), sfix(8469.50687910424), sfix(-310.68964993023), sfix(4.77796387915), sfix(1.0), sfix(1.0)],
        [sfix(25956.42499296214), sfix(-10951199.75899683), sfix(445.91904328215), sfix(-18.94442745169), sfix(0.43711832177), sfix(-0.00521388206), sfix(2.52056e-05), sfix(1.0), sfix(1.0)]
    ]
    scaler = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)]
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
        sfix(-50.0),
        sfix(-14.0625),
        sfix(-12.5),
        sfix(-10.9375),
        sfix(-9.375),
        sfix(-7.8125),
        sfix(-6.25),
        sfix(-4.6875),
        sfix(-3.125),
        sfix(-2.34375),
        sfix(-1.953125),
        sfix(-1.5625),
        sfix(-1.171875),
        sfix(-0.78125),
        sfix(-0.390625),
        sfix(-0.048828125),
        sfix(0.0244140625),
        sfix(0.1953125),
        sfix(0.78125),
        sfix(1.5625),
        sfix(2.34375),
        sfix(3.125),
        sfix(6.25),
        sfix(12.5)
    ]
    coeffA = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(8347.23769658282), sfix(1656.46608383113), sfix(132.18608408119), sfix(5.44321453502), sfix(0.12234330236), sfix(0.00142729672), sfix(6.77102e-06), sfix(1.0), sfix(1.0)],
        [sfix(1727508.5405041918), sfix(691648.7289734028), sfix(116519.35229271064), sfix(10558.93491093246), sfix(542.25855823609), sfix(14.94966747198), sfix(0.17271953058), sfix(1.0), sfix(1.0)],
        [sfix(3423364.9384434763), sfix(1512278.1827449135), sfix(282129.6347896518), sfix(28399.74305182758), sfix(1624.30707705252), sfix(49.98075423219), sfix(0.64567256257), sfix(1.0), sfix(1.0)],
        [sfix(5967701.792946223), sfix(2917942.77220817), sfix(606094.8763975359), sfix(68268.1636456945), sfix(4387.36725660972), sfix(152.22768974082), sfix(2.22397233874), sfix(1.0), sfix(1.0)],
        [sfix(8712099.040793633), sfix(4678837.049256113), sfix(1077631.0286717198), sfix(135720.99672735156), sfix(9823.72778624726), sfix(386.27758143254), sfix(6.42912225706), sfix(1.0), sfix(1.0)],
        [sfix(9635415.231384268), sfix(5351729.9459140515), sfix(1281650.2270932533), sfix(168652.94389517116), sfix(12807.51981880644), sfix(530.1021902508), sfix(9.30917215837), sfix(1.0), sfix(1.0)],
        [sfix(6020289.647086955), sfix(1734895.6298184122), sfix(-230300.0802749972), sfix(-169319.8901664084), sfix(-29791.89786624072), sfix(-2339.99028011633), sfix(-71.42632843108), sfix(1.0), sfix(1.0)],
        [sfix(-235424.369568804), sfix(-6373557.726196105), sfix(-4637559.675894038), sfix(-1455019.9447588348), sfix(-242066.45326105304), sfix(-21142.16811994146), sfix(-769.20752637251), sfix(1.0), sfix(1.0)],
        [sfix(-908308.408135387), sfix(-7386619.850160458), sfix(-5241619.158935101), sfix(-1630799.9805370101), sfix(-265821.4552014044), sfix(-21954.23151007407), sfix(-699.26174013234), sfix(1.0), sfix(1.0)],
        [sfix(-99336972.13096029), sfix(-265074865.5065575), sfix(-286296815.52032363), sfix(-165095347.32672355), sfix(-53736411.1033379), sfix(-9348964.253616711), sfix(-678490.9066681914), sfix(1.0), sfix(1.0)],
        [sfix(-34698864.090714015), sfix(-150201767.53820413), sfix(-248491667.79507414), sfix(-215482798.76220456), sfix(-103043933.12167047), sfix(-25741679.007551968), sfix(-2629407.844916754), sfix(1.0), sfix(1.0)],
        [sfix(-13715083.931525914), sfix(-59529115.42871817), sfix(-89227727.06391612), sfix(-69062277.31680472), sfix(-28440670.147472467), sfix(-5713716.931164962), sfix(-411895.30924300913), sfix(1.0), sfix(1.0)],
        [sfix(-5678131.261347499), sfix(-49523930.42329176), sfix(-137802829.21924216), sfix(-208464633.80951276), sfix(-174857674.90228254), sfix(-76510874.53125313), sfix(-13648939.05539518), sfix(1.0), sfix(1.0)],
        [sfix(624154.4753484806), sfix(426256.843124997), sfix(24187913.95737682), sfix(66933113.596672736), sfix(83926028.2375588), sfix(50723698.47141663), sfix(11840232.6025491), sfix(1.0), sfix(1.0)],
        [sfix(163547.0571849936), sfix(-5111109.893035711), sfix(-3058975.19323784), sfix(-2355190.3835121123), sfix(-9254197.050939107), sfix(-7287517.338952154), sfix(2587131.5592050413), sfix(1.0), sfix(1.0)],
        [sfix(163715.97157409322), sfix(-5102077.405744416), sfix(-2876179.4519530023), sfix(-514880.6922343407), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(163715.33023018556), sfix(-5101991.721588166), sfix(-2877809.5159597755), sfix(-527853.2896405866), sfix(-1219898.1093686717), sfix(17062940.221251573), sfix(-22605896.533945963), sfix(1.0), sfix(1.0)],
        [sfix(144372.59561892253), sfix(-4792920.43912735), sfix(-4659731.881713198), sfix(3284497.351912704), sfix(1048140.010014217), sfix(-4525349.473963986), sfix(2313401.5107512353), sfix(1.0), sfix(1.0)],
        [sfix(-781964.0262540224), sfix(-463461.52783018583), sfix(-12765715.123304926), sfix(12402775.875151165), sfix(-7980783.039550121), sfix(2756544.2481777687), sfix(-379353.8916817645), sfix(1.0), sfix(1.0)],
        [sfix(-111930338.70227797), sfix(358134752.3185891), sfix(-487868482.218235), sfix(342230355.2169066), sfix(-133998928.92855415), sfix(27741889.047414877), sfix(-2372377.3825956467), sfix(1.0), sfix(1.0)],
        [sfix(-3217453.5966923945), sfix(2517947.1402387554), sfix(-9719927.161935395), sfix(3771958.282144845), sfix(-840631.8003554456), sfix(104107.98693294328), sfix(-5583.06358005416), sfix(1.0), sfix(1.0)],
        [sfix(1893046.6462090353), sfix(-6657716.203845083), sfix(-2676339.6112352298), sfix(813472.829842618), sfix(-124774.33789294942), sfix(9774.13948600436), sfix(-312.69452675376), sfix(1.0), sfix(1.0)],
        [sfix(8121611.169581462), sfix(-14078370.130111037), sfix(933697.0756725254), sfix(-111838.09207007846), sfix(7625.52869240627), sfix(-279.72972615692), sfix(4.30184438974), sfix(1.0), sfix(1.0)],
        [sfix(23369.89228573278), sfix(-9859923.271980198), sfix(401.48364081982), sfix(-17.05663353219), sfix(0.39355990269), sfix(-0.00469432374), sfix(2.269389e-05), sfix(1.0), sfix(1.0)]
    ]
    scaler = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)]
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
        sfix(-50.0),
        sfix(-25.0),
        sfix(-12.5),
        sfix(-6.25),
        sfix(-3.125),
        sfix(-1.953125),
        sfix(-1.5625),
        sfix(-1.171875),
        sfix(-0.78125),
        sfix(-0.29296875),
        sfix(-0.1953125),
        sfix(-0.048828125),
        sfix(0.0),
        sfix(0.048828125),
        sfix(0.1953125),
        sfix(0.390625),
        sfix(0.78125),
        sfix(1.171875),
        sfix(1.5625),
        sfix(3.125),
        sfix(6.25),
        sfix(12.5)
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
        [sfix(-5.5480473895), sfix(-0.87802690345), sfix(-0.05731571838), sfix(-0.00197582788), sfix(-3.794827e-05), sfix(-3.8516e-07), sfix(-1.61e-09), sfix(1.0), sfix(1.0)],
        [sfix(-258467.00147023867), sfix(-78960.5965640978), sfix(-9999.88034194973), sfix(-671.6390943933), sfix(-25.22359094695), sfix(-0.50211076279), sfix(-0.00413877763), sfix(1.0), sfix(1.0)],
        [sfix(-9061502.923990685), sfix(-4712044.393161284), sfix(-1041751.2737969427), sfix(-124780.8072956886), sfix(-8508.01018395899), sfix(-312.1020790662), sfix(-4.79968502559), sfix(1.0), sfix(1.0)],
        [sfix(-2112123.735427453), sfix(3567381.430879534), sfix(2986065.043813589), sfix(907613.8062200993), sfix(139214.12932201367), sfix(10905.27380384287), sfix(348.88180551291), sfix(1.0), sfix(1.0)],
        [sfix(-118239213.74529661), sfix(-260780696.5861156), sfix(-246310660.8161984), sfix(-123877499.91257061), sfix(-34847917.89299428), sfix(-5201221.75516484), sfix(-322056.86593491916), sfix(1.0), sfix(1.0)],
        [sfix(160398594.05858225), sfix(587496219.2795734), sfix(870902383.8387105), sfix(686732495.491121), sfix(304415936.15999556), sfix(71870335.07807955), sfix(7053130.654272154), sfix(1.0), sfix(1.0)],
        [sfix(70273140.38163641), sfix(339718256.8128361), sfix(644473789.7458885), sfix(649985911.8926154), sfix(367627215.3989919), sfix(110295813.89470585), sfix(13698032.90715997), sfix(1.0), sfix(1.0)],
        [sfix(10027904.835693415), sfix(57674553.604047984), sfix(109519404.66808496), sfix(129590407.31193301), sfix(99332495.91211145), sfix(43793415.82998954), sfix(8252746.288258824), sfix(1.0), sfix(1.0)],
        [sfix(3935696.384923727), sfix(18582173.762622826), sfix(18983566.06483714), sfix(52640332.434803054), sfix(119687891.71639277), sfix(113761206.14662832), sfix(38588946.94559277), sfix(1.0), sfix(1.0)],
        [sfix(3270981.4766251477), sfix(9015953.253580196), sfix(-36305729.7579599), sfix(-108025552.87210809), sfix(-115299786.83668068), sfix(-24332632.704335794), sfix(39632746.17805757), sfix(1.0), sfix(1.0)],
        [sfix(3300020.8610079326), sfix(9846589.19481598), sfix(-26333222.183077496), sfix(-43633336.16332944), sfix(120780955.77191584), sfix(442068816.07330847), sfix(427828509.4377217), sfix(1.0), sfix(1.0)],
        [sfix(3299979.905835862), sfix(9841795.738046523), sfix(-26646120.65376863), sfix(-53276116.811917715), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(3299979.905835862), sfix(9846040.303364953), sfix(-26791514.558867734), sfix(-34186965.05745467), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(3299998.8115380127), sfix(9842215.164043173), sfix(-26423477.871033184), sfix(-45639414.530350365), sfix(93670047.45080371), sfix(360024498.1528505), sfix(-644751914.7249827), sfix(1.0), sfix(1.0)],
        [sfix(3415120.253597974), sfix(6817828.230303185), sfix(7094950.4538308885), sfix(-247008044.67078122), sfix(788148944.6588488), sfix(-948695789.6511303), sfix(411371816.28053313), sfix(1.0), sfix(1.0)],
        [sfix(-1010381.2708881404), sfix(65241300.12030083), sfix(-315023206.5092793), sfix(702218598.5641952), sfix(-787613867.0745771), sfix(446718972.057487), sfix(-102542470.45392445), sfix(1.0), sfix(1.0)],
        [sfix(26922406.489669457), sfix(-144779684.69096705), sfix(346636493.9270171), sfix(-415892450.27611244), sfix(281317658.77224404), sfix(-101413687.2241718), sfix(15226418.977067491), sfix(1.0), sfix(1.0)],
        [sfix(-5360573.208853311), sfix(24875815.3068334), sfix(-26459506.67588124), sfix(23511843.19648616), sfix(-10917779.757162513), sfix(2626798.511779865), sfix(-260143.8663540646), sfix(1.0), sfix(1.0)],
        [sfix(423908.08488645125), sfix(4174573.385493461), sfix(4429224.847146992), sfix(-1067422.418667655), sfix(73543.08855981694), sfix(10591.71710670224), sfix(-1507.15895725727), sfix(1.0), sfix(1.0)],
        [sfix(-2112123.7352931704), sfix(7428195.414665383), sfix(2986065.043906638), sfix(-907613.8062461306), sfix(139214.1293260485), sfix(-10905.27380417171), sfix(348.88180552393), sfix(1.0), sfix(1.0)],
        [sfix(-9061502.924289478), sfix(15707621.239077786), sfix(-1041751.2738502689), sfix(124780.80730327975), sfix(-8508.01018455866), sfix(312.10207909114), sfix(-4.79968502601), sfix(1.0), sfix(1.0)],
        [sfix(-26074.42574170186), sfix(11000985.111985777), sfix(-447.94624004955), sfix(19.03055089192), sfix(-0.43910550949), sfix(0.00523758493), sfix(-2.532019e-05), sfix(1.0), sfix(1.0)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)]
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
        sfix(-50.0),
        sfix(-14.0625),
        sfix(-12.5),
        sfix(-10.9375),
        sfix(-9.375),
        sfix(-7.8125),
        sfix(-6.25),
        sfix(-4.6875),
        sfix(-3.125),
        sfix(-2.34375),
        sfix(-1.953125),
        sfix(-1.5625),
        sfix(-1.171875),
        sfix(-0.78125),
        sfix(-0.5859375),
        sfix(-0.390625),
        sfix(-0.048828125),
        sfix(0.0),
        sfix(0.01220703125),
        sfix(0.390625),
        sfix(0.78125),
        sfix(1.5625),
        sfix(3.125),
        sfix(6.25),
        sfix(12.5)
    ]
    coeffA = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(10287.2702687821), sfix(2041.45549879547), sfix(162.90826045026), sfix(6.70830532065), sfix(0.15077785762), sfix(0.00175902348), sfix(8.34472e-06), sfix(1.0), sfix(1.0)],
        [sfix(2129009.3673898233), sfix(852399.0408166314), sfix(143600.32769574897), sfix(13013.00156148902), sfix(668.28818669529), sfix(18.42421113472), sfix(0.21286233319), sfix(1.0), sfix(1.0)],
        [sfix(4219010.124131834), sfix(1863756.0056348923), sfix(347701.1089668303), sfix(35000.30105258156), sfix(2001.82222053641), sfix(61.59708705002), sfix(0.79573727234), sfix(1.0), sfix(1.0)],
        [sfix(7354691.870425503), sfix(3596119.700635248), sfix(746961.0940376017), sfix(84134.78514755143), sfix(5407.06211777006), sfix(187.60785827388), sfix(2.74085935379), sfix(1.0), sfix(1.0)],
        [sfix(10736931.269836785), sfix(5766274.187819757), sfix(1328089.8477999924), sfix(167264.74376781995), sfix(12106.92045176894), sfix(476.05471695346), sfix(7.92335388711), sfix(1.0), sfix(1.0)],
        [sfix(11874841.024084134), sfix(6595558.238586015), sfix(1579526.3960849792), sfix(207850.60621727176), sfix(15784.19384207789), sfix(653.30648286348), sfix(11.47277380288), sfix(1.0), sfix(1.0)],
        [sfix(7419501.989418924), sfix(2138113.335312291), sfix(-283825.5306513512), sfix(-208672.56155103125), sfix(-36716.015083089), sfix(-2883.84173458122), sfix(-88.02695832875), sfix(1.0), sfix(1.0)],
        [sfix(-290140.78738854587), sfix(-7854875.263730981), sfix(-5715403.287636168), sfix(-1793190.0303259687), sfix(-298326.59835903614), sfix(-26055.94873719176), sfix(-947.98375274225), sfix(1.0), sfix(1.0)],
        [sfix(-4183624.061262418), sfix(-15720291.08541192), sfix(-12402520.667430146), sfix(-4851117.242921303), sfix(-1090369.5032320034), sfix(-136073.85382228033), sfix(-7342.53108878303), sfix(1.0), sfix(1.0)],
        [sfix(569546700.7124778), sfix(1533389686.5357342), sfix(1726625406.6433504), sfix(1034353725.2905457), sfix(347635765.73302484), sfix(62182041.158016935), sfix(4626606.658232255), sfix(1.0), sfix(1.0)],
        [sfix(401220619.2756208), sfix(1460866703.5751758), sfix(2215419978.372683), sfix(1774662683.7041972), sfix(792122625.9139297), sfix(186937603.19963235), sfix(18235387.65703278), sfix(1.0), sfix(1.0)],
        [sfix(-25807607.548923347), sfix(-109625996.48109351), sfix(-172802651.20825428), sfix(-145003804.6843395), sfix(-66617755.48041253), sfix(-15282855.520398851), sfix(-1282641.84594112), sfix(1.0), sfix(1.0)],
        [sfix(933758.2857113722), sfix(-16032887.744585756), sfix(-58842368.44030917), sfix(-106002631.15231916), sfix(-95776777.20914844), sfix(-42534247.2386642), sfix(-7473050.314603121), sfix(1.0), sfix(1.0)],
        [sfix(-4491015.511176379), sfix(-50250982.8661533), sfix(-145598311.74560055), sfix(-216765460.51329708), sfix(-167450549.3168146), sfix(-61927548.42394169), sfix(-7983016.823840482), sfix(1.0), sfix(1.0)],
        [sfix(756604.3224905729), sfix(698165.3962421515), sfix(60809944.08839973), sfix(229872069.35866928), sfix(376988977.30835265), sfix(292544594.13459736), sfix(88317444.98711154), sfix(1.0), sfix(1.0)],
        [sfix(109230.17750956114), sfix(-8977391.414284917), sfix(-276327.1289926716), sfix(20886529.907352183), sfix(-32442567.117732212), sfix(-143639622.26438788), sfix(-109242844.01847184), sfix(1.0), sfix(1.0)],
        [sfix(109237.777932658), sfix(-8975897.374421408), sfix(-184182.60267299516), sfix(23466654.92304704), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(109237.77793265802), sfix(-8976199.6238775), sfix(-220025.144039872), sfix(21313789.8957456), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(109158.36497010458), sfix(-8965852.017437698), sfix(-597103.4174697346), sfix(27088601.772325702), sfix(-54763398.12733848), sfix(-129255.52323577557), sfix(46502469.4124272), sfix(1.0), sfix(1.0)],
        [sfix(958965.9222535519), sfix(-19824388.35279052), sfix(55535816.67432785), sfix(-118190824.1917907), sfix(127074508.6649432), sfix(-70442445.25177866), sfix(16014212.427035555), sfix(1.0), sfix(1.0)],
        [sfix(-1521684.4867274258), sfix(1355057.3938142043), sfix(-18040046.743352648), sfix(16032770.407692567), sfix(-9283503.736003382), sfix(2975128.4872683035), sfix(-396895.4183127758), sfix(1.0), sfix(1.0)],
        [sfix(-489673.46476786205), sfix(-4556636.376048988), sfix(-4949663.616031421), sfix(1210729.6804580681), sfix(-90998.3570054041), sfix(-10109.45975308372), sfix(1557.88416865121), sfix(1.0), sfix(1.0)],
        [sfix(2333021.196766161), sfix(-8205076.751237317), sfix(-3298364.0711920843), sfix(1002537.0261601444), sfix(-153773.90499514213), sfix(12045.80703141626), sfix(-385.36977443923), sfix(1.0), sfix(1.0)],
        [sfix(10009204.500377983), sfix(-17350410.247807745), sfix(1150703.3243282377), sfix(-137831.06714595575), sfix(9397.82446005042), sfix(-344.74342287711), sfix(5.30166235806), sfix(1.0), sfix(1.0)],
        [sfix(28801.43191240032), sfix(-12151528.351691172), sfix(494.79490979215), sfix(-21.02087007275), sfix(0.48502956722), sfix(-0.00578536024), sfix(2.796832e-05), sfix(1.0), sfix(1.0)]
    ]
    scaler = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)]
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

def func12_kan_model_evaluate(x):
    # dim_list required
    input_x = x
    dim_list = [(3, 9), (9, 1)]
    for l in range(len(dim_list)):
        in_dim, out_dim = dim_list[l]
        partial_result = [0]*out_dim
        for i in range(in_dim):
            for j in range(out_dim):
                partial_result[j] += eval(f"neuron{l}{i}{j}")(input_x[i])
        input_x = partial_result
    return input_x

def func12_kan_model_evaluate_vectorized(x):
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

