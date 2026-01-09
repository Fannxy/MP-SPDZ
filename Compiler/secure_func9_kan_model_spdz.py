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
        sfix(-4.199999809265137),
        sfix(-2.0999999046325684),
        sfix(-1.0499999523162842),
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
        [sfix(35954755.86995401), sfix(105000902.81853184), sfix(131781432.23796998), sfix(90729210.87166564), sfix(37801263.24187225), sfix(9839975.76845085), sfix(1571355.8691683558), sfix(141242.3723838738), sfix(5484.26275774499)],
        [sfix(8152567.214577628), sfix(63241335.11759505), sfix(198687670.07296237), sfix(311482646.2735767), sfix(278707939.7143864), sfix(149635259.81559813), sfix(47885221.16697139), sfix(8451138.363426277), sfix(635201.0146296322)],
        [sfix(-2450118.6609617686), sfix(-7284455.057094543), sfix(-10422866.805294357), sfix(-50080802.799900785), sfix(-120291216.41114591), sfix(-138013497.00199705), sfix(-84234953.35705443), sfix(-26825225.910989296), sfix(-3546629.7189717134)],
        [sfix(-2247900.6956513724), sfix(-4587508.108673065), sfix(5312464.764546207), sfix(2378235.869773119), sfix(-10989063.416819243), sfix(7735288.677882737), sfix(37230324.81862081), sfix(31018293.17067717), sfix(8504580.7991172)],
        [sfix(-2247949.772437293), sfix(-4556052.494957025), sfix(6112869.811782419), sfix(7849084.059724905), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-2247949.7724372935), sfix(-4625819.984834879), sfix(6178143.289287292), sfix(-4101888.288783146), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-2279533.8731827945), sfix(-4047557.1003903192), sfix(1335656.3793921098), sfix(17854424.279958226), sfix(-51000360.29429879), sfix(52499869.572411895), sfix(-21705529.30922026), sfix(1474625.5619830957), sfix(810422.4461301988)],
        [sfix(74620485.130178), sfix(-459117408.76870036), sfix(1170608961.7038054), sfix(-1681570602.437683), sfix(1469589573.6555305), sfix(-796918401.5006434), sfix(261723721.0845844), sfix(-47700285.24039639), sfix(3706244.052092764)],
        [sfix(-592267986.1885519), sfix(1517486032.352295), sfix(-1681957343.575503), sfix(1048807047.0648835), sfix(-404561420.60617185), sfix(98976349.30042483), sfix(-15011981.379224697), sfix(1291519.2217575202), sfix(-48282.52030197327)]
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
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-2.0999999046325684),
        sfix(-1.0499999523162842),
        sfix(-0.13124999403953552),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(88725955.60107422), sfix(256179126.60165513), sfix(317963349.25418997), sfix(217247607.0630827), sfix(90038327.07164373), sfix(23348474.452344228), sfix(3717760.2241870114), sfix(333411.7762823972), sfix(12922.04123649302)],
        [sfix(39058754.78530126), sfix(224189943.9062693), sfix(577142801.329654), sfix(807334108.2620089), sfix(672406306.1421627), sfix(343693657.42169136), sfix(106057375.9502669), sfix(18186598.860429768), sfix(1334384.6677902066)],
        [sfix(-1583504.5149472933), sfix(-9850171.65916938), sfix(-2532818.3687459235), sfix(5751693.355397925), sfix(2457167.770876694), sfix(3432022.6524344147), sfix(7245238.488630428), sfix(4560305.9559236765), sfix(902921.0682727426)],
        [sfix(-1583257.5849731925), sfix(-9873682.978175221), sfix(-2674603.3510615947), sfix(5867024.882515726), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-1801145.171725266), sfix(-6975832.059784506), sfix(-19348986.339597624), sfix(60789084.7266326), sfix(-113952590.28807724), sfix(150414232.73232916), sfix(-118559035.85161613), sfix(48259242.6144759), sfix(-7834821.716312138)],
        [sfix(-112165638.10250236), sfix(617445034.4269168), sfix(-1524974012.4011955), sfix(2054825871.329205), sfix(-1659298823.6996877), sfix(824495269.536371), sfix(-247843001.00590345), sfix(41480866.20619067), sfix(-2975873.2255082848)],
        [sfix(-306357911.2204093), sfix(840538394.2354802), sfix(-995442492.714582), sfix(651687484.9101938), sfix(-262351809.69305938), sfix(66662190.428529784), sfix(-10457987.54170797), sfix(927344.5829729568), sfix(-35623.62220311444)]
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
        sfix(-4.199999809265137),
        sfix(-3.1499998569488525),
        sfix(-2.0999999046325684),
        sfix(-1.0499999523162842),
        sfix(-0.13124999403953552),
        sfix(0.0),
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
        [sfix(-55450254.452137075), sfix(-117785838.97631341), sfix(-107251166.13070881), sfix(-55670104.09151116), sfix(-18079494.074948687), sfix(-3762455.8139247214), sfix(-489768.208011815), sfix(-36445.5430932901), sfix(-1186.63427941064)],
        [sfix(422391613.17483497), sfix(1189764781.9322531), sfix(1448268905.9127173), sfix(995948067.8585273), sfix(424081521.4538698), sfix(114687741.57559484), sfix(19260223.8975037), sfix(1837933.2785198314), sfix(76346.9629482083)],
        [sfix(9708709.364957867), sfix(67528223.57960844), sfix(390296876.20157635), sfix(834774204.297941), sfix(883988753.7321111), sfix(525223071.11496747), sfix(179664050.3424312), sfix(33242907.85438986), sfix(2589290.9843149344)],
        [sfix(4083963.6420639167), sfix(-16987881.951961555), sfix(8226617.078202886), sfix(-5697661.877468081), sfix(-140662164.6138312), sfix(-167100708.59494424), sfix(-40319001.21082801), sfix(28188775.491085034), sfix(12552520.796844186)],
        [sfix(4107111.7195746745), sfix(-16389780.017418027), sfix(14945595.36977519), sfix(36695223.33850908), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(4107111.7195746745), sfix(-16429059.097441163), sfix(15123674.30139316), sfix(11727722.510978), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(4107324.4040220734), sfix(-16415935.506814992), sfix(14228477.768689692), sfix(23602125.371716786), sfix(-40264732.56684399), sfix(-55021362.434429504), sfix(158495367.02891266), sfix(-124155908.42523849), sfix(33764308.2805696)],
        [sfix(13945693.257915508), sfix(-101368650.50349607), sfix(320334087.6742656), sfix(-564085219.5509747), sfix(581049373.5493473), sfix(-357031296.1711778), sfix(128307286.52190791), sfix(-24850161.444561824), sfix(2002129.9755396943)],
        [sfix(-1010494179.8889381), sfix(2718669252.8794565), sfix(-3136518214.018847), sfix(2029833718.9084225), sfix(-809240366.7609009), sfix(203917792.710773), sfix(-31763507.112975717), sfix(2799438.7139041107), sfix(-106976.9810471912)]
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
        sfix(-4.199999809265137),
        sfix(-2.0999999046325684),
        sfix(-1.0499999523162842),
        sfix(-0.26249998807907104),
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
        [sfix(209581741.5256648), sfix(611180300.024658), sfix(739611163.0396032), sfix(495919666.1226954), sfix(203158848.965178), sfix(52301290.565005146), sfix(8287796.8594656065), sfix(740698.8207773083), sfix(28631.91544567918)],
        [sfix(159574313.9491998), sfix(895191518.8439873), sfix(1959801724.238557), sfix(2331192476.241648), sfix(1675594693.205735), sfix(750667569.2607752), sfix(205610995.290571), sfix(31580726.190801747), sfix(2087369.4795984484)],
        [sfix(-3313623.5547004063), sfix(22649451.62819512), sfix(25388393.56970877), sfix(101624608.01674944), sfix(353657371.6981799), sfix(496031937.19315135), sfix(330496567.9021129), sfix(103601831.78717601), sfix(11715132.756110387)],
        [sfix(-3573418.7107327078), sfix(18147390.116574645), sfix(-8286128.946614772), sfix(-39842217.58889381), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-3573418.7107327078), sfix(18204541.132198364), sfix(-7943753.598586278), sfix(-19569413.290946), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-3573572.883897854), sfix(18194017.473764054), sfix(-7250948.2450763965), sfix(-28544459.34922755), sfix(28059451.545885164), sfix(54596290.068871595), sfix(-120254532.58209771), sfix(84333679.2466587), sfix(-21238045.39180934)],
        [sfix(-3151282.754386063), sfix(12561876.889861967), sfix(25610723.39162182), sfix(-138104970.13930103), sfix(256355508.84922373), sfix(-249872098.74020508), sfix(133559232.82914296), sfix(-36599504.47332856), sfix(3980579.0250018556)],
        [sfix(-169857255.5139606), sfix(1001175547.425613), sfix(-2524992014.3313093), sfix(3598959831.218336), sfix(-3141632811.1422315), sfix(1710892215.5564191), sfix(-566168696.7190697), sfix(104129974.54349497), sfix(-8167311.777503257)],
        [sfix(1819998720.9457884), sfix(-4823260662.736477), sfix(5489770023.348518), sfix(-3508951205.736615), sfix(1383206222.0652587), sfix(-344977160.31150776), sfix(53232923.10335751), sfix(-4651499.149124763), sfix(176361.02477082718)]
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
        sfix(-4.199999809265137),
        sfix(-3.1499998569488525),
        sfix(-2.0999999046325684),
        sfix(-1.0499999523162842),
        sfix(-0.26249998807907104),
        sfix(-0.13124999403953552),
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
        [sfix(-47221036.59781295), sfix(-102720073.66451603), sfix(-92839323.86669336), sfix(-47672949.58293655), sfix(-15349100.342339445), sfix(-3174831.0592521797), sfix(-411567.84831223846), sfix(-30540.76062527624), sfix(-992.48344143096)],
        [sfix(128700937.74203214), sfix(327856698.39892423), sfix(350425159.0938798), sfix(199105437.43452036), sfix(63275550.86802854), sfix(10294687.611016577), sfix(408284.68800201133), sfix(-105110.28075851745), sfix(-11176.1915706403)],
        [sfix(48639430.480004564), sfix(281428191.5215424), sfix(708908222.8852341), sfix(966648361.5362746), sfix(784104907.6121525), sfix(390808479.0268219), sfix(117842118.45892917), sfix(19790777.76651765), sfix(1425134.3070141333)],
        [sfix(-1417267.4607590514), sfix(-5377870.410206054), sfix(3906940.9551452626), sfix(3496041.3767628614), sfix(-4221663.679297938), sfix(6283058.116023615), sfix(16164928.066138847), sfix(9659780.375908252), sfix(1871875.3099020356)],
        [sfix(-1420577.0629501704), sfix(-5465927.483337014), sfix(2661814.4609535797), sfix(-8121265.97596367), sfix(-77137802.10507645), sfix(-294601272.14491457), sfix(-763312563.3444206), sfix(-1138851293.0380244), sfix(-732544931.183055)],
        [sfix(-1419429.7322418955), sfix(-5412311.359991157), sfix(3774596.314886293), sfix(4217890.342939537), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-1419429.7322418957), sfix(-5437264.510813359), sfix(4166373.3401604677), sfix(-1301473.6618984807), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-1441289.7374706499), sfix(-5039944.826038351), sfix(890962.2536056009), sfix(13347812.735679276), sfix(-34308498.97107406), sfix(39155743.43299933), sfix(-25535220.20427839), sfix(8896852.194780957), sfix(-1232375.6951176755)],
        [sfix(-65326219.35301224), sfix(362510436.3085506), sfix(-908597386.3354398), sfix(1270511184.7739823), sfix(-1086991582.7140687), sfix(578524516.4107106), sfix(-186901011.86661148), sfix(33581145.79364005), sfix(-2577291.7834811453)],
        [sfix(340462270.8857893), sfix(-874584587.2676052), sfix(956472872.1230397), sfix(-594196259.0125425), sfix(227890017.13605037), sfix(-55362130.89263933), sfix(8332025.4036261365), sfix(-711057.0120857101), sfix(26366.3918609287)]
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
        sfix(-4.199999809265137),
        sfix(-3.1499998569488525),
        sfix(-2.0999999046325684),
        sfix(-1.0499999523162842),
        sfix(-0.13124999403953552),
        sfix(0.0),
        sfix(0.06562499701976776),
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
        [sfix(-59152749.66166957), sfix(-126196951.97651787), sfix(-114732107.33400302), sfix(-59424230.03253841), sfix(-19264869.428713165), sfix(-4004046.6465503257), sfix(-520745.7202643885), sfix(-38725.40562917614), sfix(-1260.25119385135)],
        [sfix(320055579.02870876), sfix(868212940.0231446), sfix(1011684103.9725149), sfix(659836726.853048), sfix(263455174.7222185), sfix(65866750.50845587), sfix(10039090.531636503), sfix(847890.8710053596), sfix(30062.80619270428)],
        [sfix(23691313.834440846), sfix(149576512.28927913), sfix(533126852.6384212), sfix(934286212.432563), sfix(895997009.6496549), sfix(501859989.03824526), sfix(164977914.1194889), sfix(29645877.81461126), sfix(2256969.596847385)],
        [sfix(1185246.0321624768), sfix(-15234237.205860224), sfix(8455025.181744523), sfix(-892709.9022553506), sfix(-100213574.22172818), sfix(-115830219.47288196), sfix(-23414147.96495175), sfix(22578720.93761314), sfix(9290493.978792867)],
        [sfix(1201107.2843143432), sfix(-14823048.288197374), sfix(13126841.419345554), sfix(29064754.541756764), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(1201107.2843143432), sfix(-14838630.065588359), sfix(12664028.325964607), sfix(15076696.130567286), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(1201155.6375254246), sfix(-14839135.0876399), sfix(12520817.698032098), sfix(19501354.020501155), sfix(-33087652.28915383), sfix(-35500167.13738407), sfix(104238387.34526362), sfix(-77778930.30959736), sfix(19759947.651642673)],
        [sfix(716609.3864840695), sfix(-8382862.986710743), sfix(-25103944.238334447), sfix(144706949.49842778), sfix(-293122024.341718), sfix(309183677.4026353), sfix(-179871323.52837083), sfix(54824272.66655166), sfix(-6881753.882942835)],
        [sfix(106379056.65032008), sfix(-645914951.5445442), sfix(1658312645.3568215), sfix(-2399931065.4502263), sfix(2119844733.2976382), sfix(-1164125016.517688), sfix(387392654.09962404), sfix(-71510383.8458772), sfix(5622277.873981909)],
        [sfix(-1202340064.3939214), sfix(3165945096.4090443), sfix(-3585427844.392264), sfix(2282090085.4386), sfix(-896409796.2394655), sfix(222895264.804115), sfix(-34305202.61292329), sfix(2990787.0168419294), sfix(-113168.64596718633)]
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
        [sfix(30257892.963793706), sfix(60055481.45652493), sfix(55880359.92593979), sfix(29898822.231465742), sfix(9940019.954815984), sfix(2101979.4355383213), sfix(276541.4140393725), sfix(20723.70780651978), sfix(677.92381621205)],
        [sfix(-65069118.18074634), sfix(-176343415.7996418), sfix(-189818939.00772732), sfix(-107708283.34060872), sfix(-33951701.297505826), sfix(-5344271.90113781), sfix(-142420.00678924454), sfix(69883.06651780083), sfix(6889.91916601616)],
        [sfix(-30979504.542428266), sfix(-172460083.07304344), sfix(-390582335.0185067), sfix(-496495172.49932045), sfix(-384685027.866187), sfix(-185620048.17768753), sfix(-54588727.383785255), sfix(-8977649.065856617), sfix(-634424.4992200158)],
        [sfix(-632433.287291429), sfix(-4987838.336501366), sfix(-49624.01965843033), sfix(-775512.8420651575), sfix(-17140038.509104457), sfix(-25465941.205518454), sfix(-12845693.059602544), sfix(-712784.4423588988), sfix(808787.348453769)],
        [sfix(-629163.50800488), sfix(-4905719.862209863), sfix(780856.5015967077), sfix(3619242.494444174), sfix(-3938389.8803737634), sfix(-3064202.0701855426), sfix(5767280.596770401), sfix(1331299.1034528113), sfix(-4570672.742826206)],
        [sfix(-629387.4604136386), sfix(-4893428.609843865), sfix(890935.6651496482), sfix(1893871.1443296173), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-451904.12497018627), sfix(-7078701.224662798), sfix(11318735.919958897), sfix(-22224663.719253283), sfix(29658953.4636324), sfix(-24398140.14755589), sfix(11223414.661425108), sfix(-2653375.645038466), sfix(252108.51183460435)],
        [sfix(-178635883.90888655), sfix(487499835.4541702), sfix(-575083535.5274043), sfix(375467886.27591157), sfix(-150842220.74922785), sfix(38266968.22862073), sfix(-5995733.516751977), sfix(531118.2787032514), sfix(-20385.62098764945)]
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
        sfix(-4.199999809265137),
        sfix(-3.1499998569488525),
        sfix(-2.0999999046325684),
        sfix(-1.0499999523162842),
        sfix(-0.5249999761581421),
        sfix(-0.26249998807907104),
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
        [sfix(35651667.85727421), sfix(72438609.26269872), sfix(66890796.90050375), sfix(35416333.80884842), sfix(11680945.963519447), sfix(2456859.507717663), sfix(322085.35177027946), sfix(24080.20986204263), sfix(786.48824320906)],
        [sfix(-97207293.91981761), sfix(-261340095.34867576), sfix(-287990391.34725446), sfix(-171189555.1740161), sfix(-59034821.545907825), sfix(-11536665.687931063), sfix(-1071670.5579748184), sfix(-7027.75634358958), sfix(4240.23371127344)],
        [sfix(-49715210.34142284), sfix(-272835942.55570513), sfix(-632210351.684653), sfix(-816963068.6756982), sfix(-640092362.8998464), sfix(-311544099.24753135), sfix(-92327901.48595695), sfix(-15297884.615573075), sfix(-1089275.805472432)],
        [sfix(-2175314.33060922), sfix(-8145927.757185272), sfix(-9840598.141498059), sfix(-27041201.690195985), sfix(-76086839.08730376), sfix(-111555721.14214471), sfix(-85129113.19214542), sfix(-32755963.167180292), sfix(-5060851.778777863)],
        [sfix(-2033127.4245864057), sfix(-6249716.700839077), sfix(1222326.9865967098), sfix(9839458.473239064), sfix(754516.0416775052), sfix(-9093886.658432206), sfix(260011.7369475667), sfix(7907111.638623079), sfix(3410890.866354846)],
        [sfix(-2033594.4674863783), sfix(-6238600.007160362), sfix(1254531.1115420589), sfix(8978892.60000241), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-1991039.6470980798), sfix(-6973168.702544871), sfix(6498855.1437088335), sfix(-11565974.513422983), sfix(52871331.28198896), sfix(-88646009.25317895), sfix(67085756.81444695), sfix(-23948329.89799564), sfix(3238442.911853922)],
        [sfix(74018514.69963002), sfix(-436031202.92310977), sfix(1039002861.3158448), sfix(-1379613813.0044653), sfix(1123208888.5333843), sfix(-575609163.8268518), sfix(181158060.98392585), sfix(-31991943.284826174), sfix(2427977.4736717236)],
        [sfix(-466912098.7970385), sfix(1225834704.0870306), sfix(-1384436614.5713513), sfix(876327565.0952969), sfix(-342187904.52790606), sfix(84570563.69944932), sfix(-12937212.856046943), sfix(1121178.3629779355), sfix(-42179.35070501344)]
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
        sfix(-4.199999809265137),
        sfix(-2.0999999046325684),
        sfix(-0.13124999403953552),
        sfix(-0.06562499701976776),
        sfix(0.0),
        sfix(0.13124999403953552),
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
        [sfix(-39522232.15201608), sfix(-103757924.63400929), sfix(-120707408.19069417), sfix(-78734689.36019282), sfix(-31501102.32527931), sfix(-7944524.330211865), sfix(-1236830.243113115), sfix(-108882.12208886573), sfix(-4155.12931012702)],
        [sfix(288020.6534952576), sfix(3585230.6126499143), sfix(-94698.5382414078), sfix(5283554.72608266), sfix(23148549.326193936), sfix(27847439.719840616), sfix(15450841.00582285), sfix(4166211.0757075967), sfix(443972.43661291746)],
        [sfix(279233.9161240432), sfix(3396115.9536660514), sfix(-1701760.2258252422), sfix(-1817294.4230025532), sfix(5178936.282962077), sfix(1432603.3422487418), sfix(-5095883.862207644), sfix(-608320.6997005121), sfix(3028611.36838819)],
        [sfix(279233.9161223135), sfix(3395854.703978288), sfix(-1727083.6987314138), sfix(-2474786.5986031815), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(279233.91612231353), sfix(3398365.723314314), sfix(-1810282.846639743), sfix(-428225.23683075095), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(279529.46272155724), sfix(3388827.820045519), sfix(-1630727.1304375136), sfix(-2163305.9549642913), sfix(6012032.035039551), sfix(934312.0896943887), sfix(-7336214.882856766), sfix(4880588.375733438), sfix(-1023191.5536891782)],
        [sfix(-21286187.93441684), sfix(127815327.57045037), sfix(-310338822.2472935), sfix(424784961.4179509), sfix(-348972951.48423237), sfix(177349580.5897921), sfix(-54740832.11403861), sfix(9427005.399776522), sfix(-696314.2291726988)],
        [sfix(8349655.716035106), sfix(-11331701.444478136), sfix(8598378.972426424), sfix(-491023.85216671875), sfix(-1396760.2295239922), sfix(674643.7256872974), sfix(-146625.6542003206), sfix(16017.85532684844), sfix(-713.82387380004)]
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
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-2.0999999046325684),
        sfix(-0.26249998807907104),
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
        [sfix(71112015.73617412), sfix(217582077.40715602), sfix(269780832.5985686), sfix(183970234.92801756), sfix(76348356.26049492), sfix(19858741.73049546), sfix(3173259.372825491), sfix(285556.3427851689), sfix(11101.64828117656)],
        [sfix(-586006.6592368209), sfix(-981125.9300803212), sfix(-15709144.301617578), sfix(-50370466.7641894), sfix(-82241286.5675139), sfix(-72873660.28713454), sfix(-35374094.63533586), sfix(-8881092.679536166), sfix(-904901.2647870712)],
        [sfix(-322221.4083461896), sfix(2405356.2556585963), sfix(2132749.0813329234), sfix(201641.20152951183), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-322042.3670736563), sfix(2414679.068871995), sfix(2052774.1917076355), sfix(-1207671.1064790823), sfix(-2632405.078671148), sfix(13489.77086152042), sfix(9173303.637498343), sfix(-9483933.469952887), sfix(2878986.186486604)],
        [sfix(941486.1913337731), sfix(-8915633.785267292), sfix(44896905.19775839), sfix(-89250805.55113694), sfix(101852569.92340767), sfix(-67986252.71254794), sfix(26424700.56329839), sfix(-5564065.757210146), sfix(492207.8291638513)],
        [sfix(-24872756.2198215), sfix(61505324.8850671), sfix(-60648035.67265115), sfix(36720571.07801605), sfix(-13758744.710458148), sfix(3271762.981778288), sfix(-483138.820063037), sfix(40559.426348243), sfix(-1483.12431090244)]
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
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-2.0999999046325684),
        sfix(-0.5249999761581421),
        sfix(-0.26249998807907104),
        sfix(0.03281249850988388),
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
        [sfix(127739815.35053122), sfix(407831183.03048337), sfix(519821536.062913), sfix(361469933.8964413), sfix(152215096.20632544), sfix(40044446.90703161), sfix(6457514.213929181), sfix(585499.8135517384), sfix(22907.48526993523)],
        [sfix(-789524.85476424), sfix(-909660.463319541), sfix(-27661256.210303508), sfix(-85168260.61553), sfix(-137533205.79504713), sfix(-123014723.6611125), sfix(-60520051.533235975), sfix(-15377867.78063336), sfix(-1581753.6832893253)],
        [sfix(-326250.38898523885), sfix(5157273.137137327), sfix(3520949.9984091637), sfix(-725591.1602996285), sfix(-4349774.545028978), sfix(2315768.272311022), sfix(7425144.214002758), sfix(3342097.545252327), sfix(202509.17736766703)],
        [sfix(-326553.5384801862), sfix(5156046.5287088), sfix(3747009.134993314), sfix(1319325.4523310836), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-326256.1255210825), sfix(5156919.989748594), sfix(3518665.8216671403), sfix(-808929.6501566768), sfix(-4344836.838905011), sfix(-323616.3751476811), sfix(8666743.647000886), sfix(-7413408.827839236), sfix(1919892.246453964)],
        [sfix(257687.00922495784), sfix(162977.16966309558), sfix(21238917.18395188), sfix(-33912951.28155537), sfix(28648028.659326095), sfix(-13280708.462640967), sfix(3325248.6132613146), sfix(-392863.62565911066), sfix(13087.34285635822)],
        [sfix(18854573.19105202), sfix(-41647632.40335346), sfix(49690519.594675854), sfix(-28474338.01055863), sfix(10314284.400670793), sfix(-2412125.0024305545), sfix(354052.2353089981), sfix(-29722.16929227206), sfix(1090.34455196831)]
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
        sfix(-4.199999809265137),
        sfix(-3.1499998569488525),
        sfix(-2.0999999046325684),
        sfix(-1.0499999523162842),
        sfix(-0.13124999403953552),
        sfix(0.0),
        sfix(0.03281249850988388),
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
        [sfix(437481373.7906634), sfix(908097761.9663734), sfix(831561647.7949432), sfix(435358793.57681596), sfix(142312368.28496742), sfix(29739992.67210486), sfix(3880729.2717124354), sfix(289140.8651050212), sfix(9418.71262039295)],
        [sfix(-260526115.32799843), sfix(-351525793.47097135), sfix(180860032.81305444), sfix(626914082.5486137), sfix(516574844.130908), sfix(217334988.6590843), sfix(51367413.64392465), sfix(6512304.484486153), sfix(346262.72833737143)],
        [sfix(-96826207.58613198), sfix(-543527824.742622), sfix(-1274813930.029105), sfix(-1654495409.812326), sfix(-1276520984.2902296), sfix(-598529481.7063111), sfix(-167455214.30122995), sfix(-25727168.78349174), sfix(-1670993.3232804905)],
        [sfix(214014.59112672205), sfix(-3895904.2824182226), sfix(-2539895.7288910695), sfix(-14588758.175835656), sfix(-36850039.49720114), sfix(-50786582.19865343), sfix(-31691959.30764117), sfix(-5760111.095446164), sfix(829522.3686622826)],
        [sfix(221591.29732695405), sfix(-3703053.361808071), sfix(-491535.8657257607), sfix(-2794515.68099967), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(221591.29732695405), sfix(-3705628.2032270343), sfix(-606820.866348871), sfix(-4792231.200659366), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(221595.74378828143), sfix(-3705935.127889053), sfix(-604282.53411454), sfix(-4545207.532341803), sfix(-4911999.443668768), sfix(-4669948.843125123), sfix(30016387.26307799), sfix(-27289856.59509864), sfix(7543672.286132617)],
        [sfix(3552361.928992772), sfix(-33244698.573087215), sfix(109532745.42793919), sfix(-226521380.07202747), sfix(250522501.76364967), sfix(-160714633.9125621), sfix(60202062.62613461), sfix(-12269435.016314631), sfix(1054791.8241418747)],
        [sfix(-34314780.17528655), sfix(75853415.37210649), sfix(-86540533.23805115), sfix(49151630.322918884), sfix(-17594768.34303827), sfix(4057939.397104862), sfix(-586847.9856395876), sfix(48530.64791054286), sfix(-1754.25784605558)]
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
        sfix(-4.199999809265137),
        sfix(-3.1499998569488525),
        sfix(-2.0999999046325684),
        sfix(-0.5249999761581421),
        sfix(-0.06562499701976776),
        sfix(0.0),
        sfix(0.13124999403953552),
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
        [sfix(-1085069469.3646216), sfix(-2256581515.0922337), sfix(-2063334093.2893307), sfix(-1078296428.6207218), sfix(-351937217.16639775), sfix(-73455125.05614021), sfix(-9575215.951735629), sfix(-712794.4852497986), sfix(-23201.2109239871)],
        [sfix(63199496.244241305), sfix(-899376176.3414037), sfix(-2723370639.172152), sfix(-3189757176.5827055), sfix(-2004176227.6587965), sfix(-741104221.1539348), sfix(-162339458.2065502), sfix(-19573995.29375866), sfix(-1004369.9848810349)],
        [sfix(-11328826.631732991), sfix(-100851275.84231648), sfix(-410296456.423545), sfix(-852070003.0792421), sfix(-1039908294.8782722), sfix(-750440566.5003297), sfix(-312543940.91035503), sfix(-69463627.70984337), sfix(-6391321.942994743)],
        [sfix(450726.6790296387), sfix(5830848.368531996), sfix(-1490619.6959839724), sfix(4575239.5649298355), sfix(10727149.666555854), sfix(-17205140.287784465), sfix(-73133646.57693149), sfix(-70811655.67635301), sfix(-21776123.11391636)],
        [sfix(450766.61030856817), sfix(5832221.164283569), sfix(-1517236.584596346), sfix(3233491.204568699), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(450766.61030856846), sfix(5838696.832078705), sfix(-1722234.0665276195), sfix(8800219.53621754), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(460612.4162502761), sfix(5586128.909181386), sfix(1044580.7941143403), sfix(-7939750.738337247), sfix(53349032.38123304), sfix(-62534666.81057431), sfix(17219621.19139582), sfix(9465414.510434382), sfix(-4641132.236835681)],
        [sfix(30314513.93310378), sfix(-144708070.47032005), sfix(301720177.4752771), sfix(-294530244.91349334), sfix(159770203.45095518), sfix(-45882822.36643123), sfix(4953161.940510326), sfix(495407.6743919784), sfix(-122301.09149410074)],
        [sfix(54623225.53622006), sfix(-121394485.52604635), sfix(137975650.59291932), sfix(-78642290.53244253), sfix(28236754.358902056), sfix(-6528696.303184978), sfix(946175.345100198), sfix(-78392.36954597119), sfix(2838.46596442527)]
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
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-2.0999999046325684),
        sfix(-0.5249999761581421),
        sfix(0.03281249850988388),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5656035.720819853), sfix(21541972.311475262), sfix(28177005.396723196), sfix(19883298.60193004), sfix(8497085.33219591), sfix(2266885.5357512506), sfix(370107.4436574319), sfix(33913.93683022338), sfix(1338.72767691981)],
        [sfix(-100875.64622138783), sfix(864072.0544167226), sfix(-2491244.8575976295), sfix(-9901140.212383773), sfix(-16286948.832345365), sfix(-14420279.1972873), sfix(-7012352.5266829), sfix(-1766041.590556556), sfix(-180547.68663961688)],
        [sfix(-51839.31602022158), sfix(1539123.8532468486), sfix(1179621.8513415616), sfix(444499.0048259392), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-51421.62864976008), sfix(1532888.5307289425), sfix(1002722.6171693469), sfix(-159271.34989238036), sfix(-1153434.831656533), sfix(938585.3757825329), sfix(535307.1004293329), sfix(-849667.4931474025), sfix(258950.59961145197)],
        [sfix(-230794.64311489472), sfix(2942677.5986021403), sfix(-2347891.661543254), sfix(2904626.413034844), sfix(-1661830.382325619), sfix(541313.6411186628), sfix(-103699.0331707191), sfix(10917.6293181544), sfix(-488.4987575157)]
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
        sfix(-4.199999809265137),
        sfix(-3.1499998569488525),
        sfix(-2.0999999046325684),
        sfix(-1.0499999523162842),
        sfix(-0.06562499701976776),
        sfix(-0.03281249850988388),
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
        [sfix(190478991.06986853), sfix(392574009.0039304), sfix(360575786.6256832), sfix(189537911.47528464), sfix(62158386.84756949), sfix(13020812.60180017), sfix(1702075.6438652596), sfix(126987.28160322768), sfix(4141.01645493856)],
        [sfix(-297674630.37883884), sfix(-740337016.2990513), sfix(-713315524.5037489), sfix(-327240323.00654924), sfix(-55972040.20860892), sfix(11266953.6413602), sfix(7014774.039012296), sfix(1229434.4511476068), sfix(77590.44778252447)],
        [sfix(-74716046.03170007), sfix(-428113046.8158995), sfix(-1038154901.3630449), sfix(-1408902657.6541252), sfix(-1148406686.550085), sfix(-574543475.7707067), sfix(-173230533.16488418), sfix(-28977993.713748056), sfix(-2071949.0009913074)],
        [sfix(-90841.35678270808), sfix(-3209646.3308399883), sfix(-1745731.339020217), sfix(-4673945.963842471), sfix(-4540713.801899035), sfix(-9073811.768894654), sfix(-10070947.332313767), sfix(-3631442.246549737), sfix(-183242.8962325549)],
        [sfix(-90471.69979868383), sfix(-3195677.6934449305), sfix(-1549267.8666181834), sfix(-3333098.535078736), sfix(376096.1489987913), sfix(877520.8153610467), sfix(352734.4190234629), sfix(340214.62017559), sfix(-1070647.915741824)],
        [sfix(-90471.69979113418), sfix(-3195679.8089868594), sfix(-1549682.0203974692), sfix(-3355163.1287153154), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-90471.69979113422), sfix(-3192571.4482037113), sfix(-1620514.5491011012), sfix(-2940118.501325963), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-109166.5202972767), sfix(-2936430.0698638754), sfix(-3048011.95562448), sfix(1409904.8872956596), sfix(-8649010.53730597), sfix(11352055.687692909), sfix(-6377100.995762411), sfix(1701716.0972835089), sfix(-178056.1383339519)],
        [sfix(23506729.89534208), sfix(-61693377.34450426), sfix(57040774.97887262), sfix(-35894014.88912512), sfix(13813618.83997433), sfix(-3346135.85108465), sfix(500867.15667085507), sfix(-42497.35044771245), sfix(1567.78879209601)]
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
        sfix(-4.199999809265137),
        sfix(-3.1499998569488525),
        sfix(-2.0999999046325684),
        sfix(-0.5249999761581421),
        sfix(-0.13124999403953552),
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
        [sfix(-25637366.493114006), sfix(-54519552.0359355), sfix(-49460722.20839049), sfix(-25565822.9270517), sfix(-8271060.766593966), sfix(-1715427.9914734897), sfix(-222622.15331675217), sfix(-16519.95579207008), sfix(-536.47280860508)],
        [sfix(-7018914.179902024), sfix(-46719270.08022922), sfix(-94044503.68482406), sfix(-94500988.84611337), sfix(-54837463.75064849), sfix(-19314033.472279083), sfix(-4093259.617394462), sfix(-481840.35638676054), sfix(-24276.23019213396)],
        [sfix(-76809.39061540294), sfix(-2254720.674617362), sfix(-4145049.3944151876), sfix(-5961061.67275413), sfix(-6786493.486838335), sfix(-4901823.21471638), sfix(-2015533.4914619902), sfix(-429779.4281089104), sfix(-36881.32327268076)],
        [sfix(41510.71301816788), sfix(-1246661.8074394106), sfix(-560182.872807043), sfix(848819.2003363647), sfix(401567.5429093392), sfix(-1263166.6640298767), sfix(-2063077.262905369), sfix(-1340085.2046328413), sfix(-334181.3412775293)],
        [sfix(41512.35774844383), sfix(-1246872.2033627827), sfix(-572295.2975276741), sfix(699289.1289843506), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(41512.35774844383), sfix(-1246475.1017158295), sfix(-564401.8017629931), sfix(953818.4801495896), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(29520.58917988522), sfix(-1027735.9907277315), sfix(-2003780.6948798206), sfix(5239053.488577951), sfix(-5764217.118260026), sfix(2585759.210033301), sfix(-214111.99659084683), sfix(-165208.47891707387), sfix(35977.78735444132)],
        [sfix(7481092.4278852735), sfix(-18699368.98216324), sfix(17991996.569910884), sfix(-10949928.399954498), sfix(4112429.206907754), sfix(-978191.4553899429), sfix(144316.08053252517), sfix(-12096.43579969523), sfix(441.49964196806)]
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
        sfix(-2.0999999046325684),
        sfix(-0.5249999761581421),
        sfix(-0.06562499701976776),
        sfix(0.0),
        sfix(0.13124999403953552),
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
        [sfix(415197932.78310645), sfix(1156075794.2163167), sfix(1359121652.4609787), sfix(892101383.5474983), sfix(359428682.2475132), sfix(91302538.52467822), sfix(14310452.120126948), sfix(1267360.7878675284), sfix(48615.70656764099)],
        [sfix(-3040393.769439395), sfix(-29154012.329382583), sfix(-124064287.61489819), sfix(-264151016.41025332), sfix(-330597048.6792852), sfix(-245542847.161047), sfix(-105565126.3497654), sfix(-24261006.348303385), sfix(-2309708.582213023)],
        [sfix(316504.41622636473), sfix(2109948.3462323425), sfix(-858974.0970865937), sfix(1269350.4020814286), sfix(4031150.3059898834), sfix(-4953725.8010717835), sfix(-23334033.253460545), sfix(-22949889.207076065), sfix(-7136821.122629821)],
        [sfix(316517.0702677865), sfix(2110353.973671715), sfix(-870308.0447823437), sfix(767529.266486395), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(316517.07026778645), sfix(2112762.126882789), sfix(-947862.6827360358), sfix(2800572.821570261), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(319077.6101952526), sfix(2046484.6332290964), sfix(-198667.2816335772), sfix(-1931264.3687627194), sfix(15194906.340724295), sfix(-15078531.698948754), sfix(1227792.92851515), sfix(4380457.372677684), sfix(-1576239.9404315604)],
        [sfix(-326588.0819146455), sfix(11070567.771092564), sfix(-39974506.774767816), sfix(84032856.28455746), sfix(-87478466.34794396), sfix(51806760.479235716), sfix(-17809285.78564241), sfix(3324270.295428409), sfix(-261577.79239630903)],
        [sfix(5873541.911357501), sfix(-10177569.90356296), sfix(14677344.498685542), sfix(-7233103.7112768), sfix(2266394.976946066), sfix(-464371.68815264094), sfix(60379.82170168994), sfix(-4523.22671872627), sfix(148.66173449142)]
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
        sfix(-4.199999809265137),
        sfix(-2.0999999046325684),
        sfix(-0.5249999761581421),
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
        [sfix(77738159.54680045), sfix(219326291.7335016), sfix(259908194.9098068), sfix(171759566.46239558), sfix(69628741.24514203), sfix(17786023.584475007), sfix(2801776.56889073), sfix(249256.930924453), sfix(9600.52327876228)],
        [sfix(-411703.85419701546), sfix(-5643730.69375778), sfix(-25416109.15908237), sfix(-57179823.21727352), sfix(-76189371.23661716), sfix(-59568469.51103643), sfix(-26626956.279995218), sfix(-6305726.775398922), sfix(-614856.2969208434)],
        [sfix(233273.6342665968), sfix(599579.5420480508), sfix(177404.5977056266), sfix(334008.7033525196), sfix(49407.33731485462), sfix(-601974.5346913282), sfix(-2987071.177628853), sfix(-3546680.6089390144), sfix(-1251211.8837504587)],
        [sfix(233278.74480922523), sfix(599751.2474393545), sfix(178252.23636438663), sfix(319328.6343862604), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(233278.74480922523), sfix(600727.2505924294), sfix(157856.78982659694), sfix(522497.68582590774), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(233652.22018232843), sfix(582618.345255278), sfix(365861.0937613848), sfix(-534378.8802158902), sfix(2656316.4255641703), sfix(-3190666.9423115756), sfix(1731315.0071607435), sfix(-455957.859481776), sfix(47575.42367812835)],
        [sfix(-2466049.1458641686), sfix(6959754.080002868), sfix(-5743054.659563811), sfix(3788465.1993386312), sfix(-1498398.8346548495), sfix(368444.2642401246), sfix(-55604.5835125179), sfix(4739.32571748884), sfix(-175.28406521597)]
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
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-2.0999999046325684),
        sfix(-0.5249999761581421),
        sfix(0.03281249850988388),
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
        [sfix(267925622.27236557), sfix(749667525.6606356), sfix(880247965.309417), sfix(576726429.9547709), sfix(231964709.09146973), sfix(58829059.06653542), sfix(9206407.046953388), sfix(814114.1237972712), sfix(31183.88136274726)],
        [sfix(-928437.9862611304), sfix(-3077005.5993075627), sfix(-26442891.037375517), sfix(-67682788.21328521), sfix(-99066916.61126359), sfix(-82892156.77173446), sfix(-38676972.641320474), sfix(-9392827.160134444), sfix(-928465.2572800005)],
        [sfix(-244474.72779764864), sfix(3814302.908125086), sfix(3121481.2279427624), sfix(2437612.4353060042), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-244029.1879833575), sfix(3808083.6374388603), sfix(2933881.6626237542), sfix(1386535.6786914582), sfix(-2011832.1974939571), sfix(-687764.0574810384), sfix(1121343.380529729), sfix(23995.63385613502), sfix(-180443.3976302728)],
        [sfix(-540383.6555819298), sfix(6586117.847603435), sfix(-8161580.224053849), sfix(25910571.61561774), sfix(-34491607.76308411), sfix(25180485.02705833), sfix(-10424865.820615608), sfix(2302804.923942611), sfix(-211585.41585810037)],
        [sfix(9553425.303548034), sfix(-18815102.69507862), sfix(26042321.25381907), sfix(-14137298.708573826), sfix(4914575.092812027), sfix(-1117858.3414667817), sfix(161125.17101845398), sfix(-13363.97927538928), sfix(486.17141870394)]
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
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-2.0999999046325684),
        sfix(-0.26249998807907104),
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
        [sfix(106753532.13743168), sfix(313137995.8019205), sfix(378955680.9979922), sfix(254195068.06464523), sfix(104240197.1701703), sfix(26871703.30773001), sfix(4264314.394314866), sfix(381657.22819369694), sfix(14773.23526967224)],
        [sfix(-390652.17986067606), sfix(122592.24765308994), sfix(-5706547.809789909), sfix(-21417048.52116455), sfix(-43965841.2245159), sfix(-45218121.93300281), sfix(-23987707.14431118), sfix(-6361939.935408621), sfix(-671801.5724467464)],
        [sfix(-270694.7600773175), sfix(1693405.0439503996), sfix(2780742.8366420916), sfix(3580769.2397128497), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-270627.27836874506), sfix(1697313.2309493297), sfix(2756189.2486488284), sfix(2983908.4166321517), sfix(-2517780.969524383), sfix(-2418170.026635238), sfix(1352164.8380652624), sfix(1343107.1137574448), sfix(-781829.1459355955)],
        [sfix(-1038781.4345160773), sfix(8783219.53531981), sfix(-25039873.579865288), sfix(63131866.517161444), sfix(-80023568.90307033), sfix(56799131.42334595), sfix(-23005608.736709274), sfix(4991390.153297684), sfix(-451810.660266148)],
        [sfix(20936405.91700386), sfix(-47314393.967859864), sfix(53414223.64167385), sfix(-30814174.59885891), sfix(11182867.1646298), sfix(-2609719.6667292276), sfix(381325.11203000555), sfix(-31827.9523034414), sfix(1160.30148154727)]
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
        sfix(-4.199999809265137),
        sfix(-3.1499998569488525),
        sfix(-2.0999999046325684),
        sfix(-1.0499999523162842),
        sfix(-0.13124999403953552),
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
        [sfix(558964704.915101), sfix(1160432056.954955), sfix(1063522948.7396984), sfix(557298643.2246215), sfix(182322980.4636289), sfix(38129938.70391074), sfix(4978982.460108178), sfix(371210.8906829308), sfix(12099.66329092657)],
        [sfix(-661490573.1098366), sfix(-1433238068.044268), sfix(-1023387726.8494221), sfix(-95143273.25356977), sfix(265879584.81755707), sfix(168070348.7682049), sfix(46766727.768046446), sfix(6481053.028571449), sfix(364500.5759836571)],
        [sfix(-209898474.72312054), sfix(-1186627007.0346367), sfix(-2836436184.3075786), sfix(-3761855147.716545), sfix(-2988331020.8283134), sfix(-1456011452.4300177), sfix(-427406597.8146251), sfix(-69584383.69041231), sfix(-4840191.78891195)],
        [sfix(389976.1942010583), sfix(-4568763.170576962), sfix(-5294675.143481024), sfix(-25156789.651265237), sfix(-57992051.08107765), sfix(-84240339.85869384), sfix(-58155003.65707108), sfix(-13830852.554972196), sfix(421449.28051044187)],
        [sfix(402491.363604938), sfix(-4251300.824531966), sfix(-1966164.788561023), sfix(-6402442.0531717185), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(402491.363604938), sfix(-4254641.183447825), sfix(-2078297.3613756935), sfix(-9148548.500018392), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(402518.59854150674), sfix(-4255751.36100124), sfix(-2079602.3696788878), sfix(-8656156.58646938), sfix(-4380398.345144304), sfix(-8477094.159938121), sfix(48530968.28159977), sfix(-45775925.30044022), sfix(13408839.005471269)],
        [sfix(5932555.306453773), sfix(-53390767.12565662), sfix(181664014.46921873), sfix(-380806312.07253253), sfix(427681980.3397374), sfix(-277436820.7374475), sfix(104673074.76826496), sfix(-21423516.286183253), sfix(1845791.4935644474)],
        [sfix(-81121179.78661811), sfix(184844476.0881177), sfix(-202546035.95266494), sfix(116933671.33052604), sfix(-42364024.5920948), sfix(9850086.000566402), sfix(-1432344.2273576926), sfix(118912.72353423708), sfix(-4310.99205279453)]
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
        sfix(-4.199999809265137),
        sfix(-2.0999999046325684),
        sfix(-0.5249999761581421),
        sfix(-0.13124999403953552),
        sfix(0.0),
        sfix(0.06562499701976776),
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
        [sfix(1228544905.0269413), sfix(3338844591.7268405), sfix(3865614936.9533124), sfix(2506190023.607459), sfix(999109871.8913419), sfix(251464884.88558838), sfix(39096406.87970594), sfix(3437881.8875142955), sfix(131047.6414842094)],
        [sfix(-6219896.542907784), sfix(-60568350.30216447), sfix(-232445681.77245966), sfix(-473050368.6335819), sfix(-568670198.8668927), sfix(-405206953.72044057), sfix(-167030825.1332751), sfix(-36810943.77740493), sfix(-3362962.6561379735)],
        [sfix(400519.7247719808), sfix(-862216.6427281152), sfix(-4764553.815971837), sfix(1174872.6161345248), sfix(7902019.803626795), sfix(-9482487.935790673), sfix(-44829023.15182403), sfix(-43494283.4208376), sfix(-13479593.037776807)],
        [sfix(400577.6407497334), sfix(-863819.9536919993), sfix(-4917303.764843874), sfix(-981764.1967395557), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(400577.6407497334), sfix(-859230.9636347479), sfix(-4776245.291466134), sfix(3039370.7610366046), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(400577.28968059534), sfix(-859780.7603550269), sfix(-4721597.596499526), sfix(1630691.0985447636), sfix(10652944.500250228), sfix(2479996.6780201187), sfix(-17529145.862655483), sfix(1050230.2209238145), sfix(10143704.848938892)],
        [sfix(400523.09868237854), sfix(-857622.0300665593), sfix(-4759149.978933368), sfix(2003029.5771361068), sfix(8352549.532071774), sfix(11545015.66613016), sfix(-39773120.207278915), sfix(32118589.08216703), sfix(-8763466.4251679)],
        [sfix(609687.0412148559), sfix(-3653870.6236007493), sfix(11587035.173894182), sfix(-52576405.888304), sfix(122210837.01904233), sfix(-140423018.7344837), sfix(86967823.18766029), sfix(-28270967.855314065), sfix(3823489.2730088094)],
        [sfix(-836181.567814545), sfix(14058637.358787978), sfix(-66459304.987366974), sfix(127352659.71531917), sfix(-124705586.90913661), sfix(70039881.237424), sfix(-22983536.21864608), sfix(4121481.7228208277), sfix(-313429.8624795007)],
        [sfix(-22255795.552855067), sfix(54865682.58510766), sfix(-57039460.422605544), sfix(34707863.5233505), sfix(-13116127.339182006), sfix(3153670.504520102), sfix(-471458.5334833), sfix(40082.15156762794), sfix(-1484.07640171698)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
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
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-2.0999999046325684),
        sfix(-0.5249999761581421),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(7397858.175675947), sfix(28402472.044896636), sfix(37587710.52430425), sfix(26737180.470561594), sfix(11485243.766111538), sfix(3074768.457025298), sfix(503271.8597157848), sfix(46205.38941614304), sfix(1826.77251234021)],
        [sfix(118328.41893895976), sfix(3298265.844076567), sfix(8629807.105023192), sfix(14662022.048808357), sfix(12153153.609295446), sfix(4304094.833168272), sfix(112793.09015661669), sfix(-297686.36950774194), sfix(-53149.87261023036)],
        [sfix(-142153.62999763864), sfix(1139303.774027114), sfix(1134246.1048404486), sfix(1186712.2899295196), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-142153.62999763864), sfix(1161434.089704693), sfix(1369457.4430583215), sfix(1470370.6785272758), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-142154.35278913393), sfix(1161521.8989822846), sfix(1363906.220212772), sfix(1595604.3270586345), sfix(-804617.935880516), sfix(-1296551.085179822), sfix(-429292.8891229309), sfix(1813140.1423076408), sfix(-732958.9969720853)],
        [sfix(-668123.7143365162), sfix(5963631.055018935), sfix(-17237054.613158353), sfix(41184144.31841435), sfix(-50593829.030465744), sfix(35177928.86001888), sfix(-14039196.63513665), sfix(3011712.5203795247), sfix(-270149.443325322)],
        [sfix(12706085.63769964), sfix(-28678270.65858979), sfix(32375595.043193005), sfix(-18658327.728325017), sfix(6765041.86997147), sfix(-1577409.3159375107), sfix(230309.13592125435), sfix(-19209.47178103488), sfix(699.82550382961)]
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
        sfix(-4.199999809265137),
        sfix(-3.1499998569488525),
        sfix(-2.0999999046325684),
        sfix(-1.0499999523162842),
        sfix(-0.26249998807907104),
        sfix(0.0),
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
        [sfix(191507159.40909016), sfix(398976715.20911527), sfix(364984472.23596376), sfix(190804621.8986104), sfix(62301337.85072511), sfix(13009970.523126498), sfix(1696890.559369817), sfix(126397.53240650691), sfix(4116.83999194496)],
        [sfix(-194359177.5250094), sfix(-425962670.63741374), sfix(-311903848.8232076), sfix(-38089416.83476649), sfix(73118430.23268555), sfix(47889706.542093545), sfix(13468970.88122619), sfix(1876111.9416693393), sfix(105819.97360702683)],
        [sfix(-53784111.34427591), sfix(-305868104.00490963), sfix(-734298469.4953406), sfix(-979118669.8077298), sfix(-782049496.9485363), sfix(-382747661.6566177), sfix(-112709499.41748038), sfix(-18385179.93272822), sfix(-1280013.6913780763)],
        [sfix(319373.2047819963), sfix(-1058953.8953403656), sfix(-2810178.2558122533), sfix(-14221647.033707764), sfix(-33477628.77083532), sfix(-48721515.48589772), sfix(-39076013.662433706), sfix(-15312908.46877528), sfix(-2272323.4259884763)],
        [sfix(345385.96767785377), sfix(-610033.0592679468), sfix(505029.5550105996), sfix(-601514.8271909318), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(345385.96767785377), sfix(-612600.9089250983), sfix(477346.33583584987), sfix(-1369718.5647529038), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(345398.9883155302), sfix(-612541.9528077086), sfix(458983.5149960655), sfix(-1106487.8603218289), sfix(-816631.9420196704), sfix(-2235155.0060476013), sfix(6451191.266379883), sfix(-4898920.359607781), sfix(1283084.0438414642)],
        [sfix(557692.9127095697), sfix(-2306118.329797691), sfix(5868850.061281852), sfix(-9431677.46395785), sfix(3773567.2536303047), sfix(2055850.1214042527), sfix(-2321955.420634509), sfix(756650.8662226094), sfix(-86723.08992223814)],
        [sfix(16695246.155533751), sfix(-41372819.51090184), sfix(41889637.10803093), sfix(-25497722.991670933), sfix(9617811.540893054), sfix(-2304682.0786072845), sfix(343096.59512627183), sfix(-29038.22140558257), sfix(1070.31336342215)]
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
        sfix(-4.199999809265137),
        sfix(-2.0999999046325684),
        sfix(-0.5249999761581421),
        sfix(-0.03281249850988388),
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
        [sfix(61092923.97749703), sfix(161170654.32516608), sfix(184977600.4171572), sfix(119094294.23206317), sfix(47132577.74811678), sfix(11776222.025801564), sfix(1818159.012677558), sfix(158844.92024348507), sfix(6019.23150008559)],
        [sfix(-814201.9102388157), sfix(-8434143.799300252), sfix(-27902547.14666036), sfix(-55390856.20761558), sfix(-63211757.01850444), sfix(-42172984.9680454), sfix(-16341386.597482609), sfix(-3417997.4097565953), sfix(-299267.3390808245)],
        [sfix(-28661.09604930946), sfix(-1423961.0056003644), sfix(-1498109.8438651424), sfix(-1225485.0604212764), sfix(1293727.9656622875), sfix(625522.2863205248), sfix(-4223616.213195187), sfix(-4722730.623643352), sfix(-1435133.3709135929)],
        [sfix(-28660.46082359808), sfix(-1423920.5157559365), sfix(-1498404.3199564193), sfix(-1295718.7999575664), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-28660.46082359808), sfix(-1417437.5673534365), sfix(-1651016.7206795353), sfix(-251870.86081167907), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(35249.62152419666), sfix(-2244424.7468858217), sfix(2783641.2977986), sfix(-13044620.342494592), sfix(20463258.089857202), sfix(-16338022.218114017), sfix(7122723.693133604), sfix(-1622359.6373182153), sfix(151780.78811080128)],
        [sfix(-11080790.787448604), sfix(24953157.32673706), sfix(-28813784.91373508), sfix(16649396.620157894), sfix(-6061867.445529634), sfix(1420950.3889937685), sfix(-208680.9012410191), sfix(17510.16340057719), sfix(-641.70312707207)]
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
        sfix(-2.0999999046325684),
        sfix(-0.5249999761581421),
        sfix(0.0),
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
        [sfix(186762983.35997108), sfix(521286127.41897225), sfix(613210512.5614172), sfix(402670461.6144725), sfix(162305659.1611655), sfix(41246161.34500332), sfix(6467244.115647893), sfix(572945.7023693199), sfix(21984.63575008028)],
        [sfix(-1388884.2158440053), sfix(-10158901.93629067), sfix(-43235809.47419725), sfix(-92083782.25763033), sfix(-117127181.97226252), sfix(-88667742.64789794), sfix(-38718719.29413123), sfix(-8999738.049641784), sfix(-863593.5105080977)],
        [sfix(-201881.82360138785), sfix(887339.5500591916), sfix(52587.92761004025), sfix(502444.453862476), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-201881.82360138785), sfix(922393.1323184265), sfix(476578.5769186475), sfix(2698143.935347925), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-201902.3793927529), sfix(922567.3247288415), sfix(494227.81949763495), sfix(2393104.1865229076), sfix(1253882.1122163339), sfix(1664324.3591595797), sfix(-11947517.366744464), sfix(11648650.448830476), sfix(-3523439.0466572866)],
        [sfix(-1549295.1422549463), sfix(12900415.606265513), sfix(-44329903.80893679), sfix(93268540.64393993), sfix(-104370916.71337873), sfix(67396543.07405125), sfix(-25332805.360740796), sfix(5171386.309896909), sfix(-444846.0821127828)],
        [sfix(14600451.268129122), sfix(-32628355.163767003), sfix(36471460.1978683), sfix(-20808957.68457141), sfix(7468680.524115571), sfix(-1724184.5213575207), sfix(249314.83029150023), sfix(-20601.96826170173), sfix(743.88977302958)]
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
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-3.1499998569488525),
        sfix(-2.0999999046325684),
        sfix(-1.0499999523162842),
        sfix(-0.26249998807907104),
        sfix(-0.13124999403953552),
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
        [sfix(40197103.07885998), sfix(82146648.69111113), sfix(75686869.8200309), sfix(39953702.638745636), sfix(13146175.208915934), sfix(2760275.4037770703), sfix(361407.74650657777), sfix(26994.49323887852), sfix(881.01185849236)],
        [sfix(-55017152.441371016), sfix(-127257574.10939494), sfix(-104421711.34545064), sfix(-29103900.33334103), sfix(9082403.203218494), sfix(9199100.293637125), sfix(2846373.841538534), sfix(413461.1737599467), sfix(23878.40058502238)],
        [sfix(-12842694.963619541), sfix(-72860660.75548579), sfix(-174540299.79664207), sfix(-236614715.95264536), sfix(-192537494.8720192), sfix(-95793954.84663364), sfix(-28617382.688052986), sfix(-4729349.703265829), sfix(-333354.0496787586)],
        [sfix(-250088.10725327831), sfix(-1417746.064838726), sfix(-1272806.6953182288), sfix(-4215511.084845206), sfix(-7034948.891118015), sfix(-8320776.8258496905), sfix(-6469110.846896256), sfix(-2595551.9085999085), sfix(-395124.110608659)],
        [sfix(-245123.772646488), sfix(-1344015.4032942583), sfix(-957873.4849816669), sfix(-5378718.318564987), sfix(-26360492.54736783), sfix(-108212162.20502813), sfix(-284975946.8334262), sfix(-423470708.63444436), sfix(-271843316.27000034)],
        [sfix(-244695.01022623523), sfix(-1325421.9105289257), sfix(-606427.2952808194), sfix(-1465809.0906798914), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-103660.5096837633), sfix(-3069323.9500571326), sfix(7986946.73460582), sfix(-23120567.43949453), sfix(29177120.28646987), sfix(-19679339.038707253), sfix(7349791.016675855), sfix(-1432528.9899494532), sfix(113441.39378681386)],
        [sfix(-18958921.596959986), sfix(43522939.029593654), sfix(-47966042.678232804), sfix(27888502.030605696), sfix(-10174317.304320483), sfix(2381579.913137898), sfix(-348551.69272805034), sfix(29115.00676185918), sfix(-1061.71914790794)]
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
def neuron030(x):
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
        sfix(-0.26249998807907104),
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
        [sfix(-35999795.0820277), sfix(-98444616.81810747), sfix(-110746742.0185675), sfix(-70214099.35580932), sfix(-27607006.880322162), sfix(-6892553.103991631), sfix(-1066708.317369784), sfix(-93562.65852923802), sfix(-3561.91708247969)],
        [sfix(-14364392.703254305), sfix(-72966378.22046278), sfix(-152655950.35586667), sfix(-181557241.90173462), sfix(-131644450.84293549), sfix(-59269471.69612109), sfix(-16210098.179544969), sfix(-2470699.032633609), sfix(-161163.64220857417)],
        [sfix(-1532527.8428613849), sfix(-5375465.982751896), sfix(-8235782.046634199), sfix(-30480336.0365435), sfix(-70970498.77394044), sfix(-86737008.4013689), sfix(-58005343.473949924), sfix(-20311081.37165514), sfix(-2931941.985961874)],
        [sfix(-1407568.5542137984), sfix(-3710666.781396296), sfix(1469173.176646318), sfix(1852275.229388048), sfix(-3639583.3984632813), sfix(3007455.664918946), sfix(16762308.16958574), sfix(15285548.210037267), sfix(4482940.286871083)],
        [sfix(-1407592.2526219806), sfix(-3701586.32528225), sfix(1708466.5052315712), sfix(3557196.628979304), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-1407592.2526219806), sfix(-3767900.442950814), sfix(2230263.968197322), sfix(-1591310.62717427), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(15460.57144599012), sfix(-16076260.278154265), sfix(46536635.24572595), sfix(-87011364.1041469), sfix(94928025.47866379), sfix(-61744654.39209726), sfix(23296715.110501304), sfix(-4695182.985342619), sfix(390945.5612678882)],
        [sfix(-243154017.55817658), sfix(639869596.8496798), sfix(-729768594.2315047), sfix(464626782.4449522), sfix(-182642357.6036005), sfix(45460793.435488425), sfix(-7004544.63477918), sfix(611348.4685251968), sfix(-23157.5152202469)]
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
def neuron031(x):
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
        [sfix(-27881092.97051529), sfix(-60606518.06430998), sfix(-54797814.432451315), sfix(-28152976.94451261), sfix(-9068292.908200061), sfix(-1876353.961113798), sfix(-243308.05781448775), sfix(-18059.02265241078), sfix(-586.97866204486)],
        [sfix(67415219.0052888), sfix(176478635.9693929), sfix(193853242.4839073), sfix(113668684.88633916), sfix(37846738.379123025), sfix(6800934.39630742), sfix(465961.7038028273), sfix(-30104.13738333468), sfix(-4801.62279165958)],
        [sfix(29524066.095427915), sfix(172446680.04935285), sfix(423549438.69415504), sfix(563304567.3281759), sfix(448239897.5133567), sfix(220275213.10918778), sfix(65722759.79002818), sfix(10947204.963772602), sfix(782996.5727716365)],
        [sfix(-1202870.22692647), sfix(-1320809.4879278885), sfix(4831232.690509982), sfix(9315997.608116305), sfix(19637714.63729842), sfix(33969066.2219208), sfix(30404134.06567125), sfix(13016970.444666164), sfix(2156379.749568577)],
        [sfix(-1244278.775186715), sfix(-1876514.3444524575), sfix(1572682.0997015878), sfix(-1590933.2523900787), sfix(-3159193.6019368744), sfix(3496100.791003264), sfix(4960485.5409896085), sfix(882999.544210276), sfix(-374338.2630137441)],
        [sfix(-1244282.7937005637), sfix(-1862717.5704808088), sfix(1903508.1024188772), sfix(454034.7194407796), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-1244282.7937005637), sfix(-1881409.8684615653), sfix(1697696.3279236413), sfix(-2674207.1427057483), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-1263623.75636108), sfix(-1544459.3711819716), sfix(-853560.7285275066), sfix(8171915.899154093), sfix(-27199221.996710304), sfix(38215847.92972485), sfix(-26674249.055114333), sfix(8975288.848190721), sfix(-1127792.1296551242)],
        [sfix(-20408923.956033878), sfix(103646923.51502928), sfix(-243834430.89530438), sfix(309507067.9861733), sfix(-236543573.70411423), sfix(111351768.82519658), sfix(-31697438.086298876), sfix(5018864.740506137), sfix(-340199.9472658272)],
        [sfix(-82609127.28197134), sfix(219503125.64271456), sfix(-255094555.03851527), sfix(163467455.24923393), sfix(-64637219.59533506), sfix(16174844.507859897), sfix(-2504144.2313038814), sfix(219485.83926127243), sfix(-8345.09647929791)]
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
def neuron032(x):
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
        sfix(-1.5749999284744263),
        sfix(-1.0499999523162842),
        sfix(-0.26249998807907104),
        sfix(0.0),
        sfix(0.13124999403953552),
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
        [sfix(-90952953.65813786), sfix(-255433901.88935274), sfix(-305309404.73918533), sfix(-202925539.48564145), sfix(-82477631.8925859), sfix(-21082601.283471555), sfix(-3319875.129818559), sfix(-295080.91858511174), sfix(-11352.10514659176)],
        [sfix(-57938184.077441804), sfix(-393934058.9346713), sfix(-910471209.8009328), sfix(-1082756480.475206), sfix(-760578335.1841383), sfix(-330025272.16634035), sfix(-87361289.98734857), sfix(-12988741.851601563), sfix(-834428.1004158782)],
        [sfix(34069057.012122326), sfix(231380108.13686308), sfix(848390920.8133217), sfix(1647825337.5356786), sfix(1827682949.458084), sfix(1214349174.522353), sfix(481620862.62562793), sfix(105703343.28698866), sfix(9921464.48103343)],
        [sfix(4307459.285667338), sfix(-13615940.04947135), sfix(-19808559.067410287), sfix(-80809084.06007704), sfix(-281818468.7093659), sfix(-392976923.0383038), sfix(-258293437.71614474), sfix(-79298691.45424104), sfix(-8660325.40897714)],
        [sfix(4513586.148698196), sfix(-10040774.1284854), sfix(6988886.602860603), sfix(31992821.266571127), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(4513586.148698196), sfix(-10089926.106785879), sfix(6663287.08169359), sfix(14958426.0097312), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(4507088.020725394), sfix(-9914019.663013468), sfix(4382884.457959442), sfix(31609645.27699255), sfix(-52289336.10884138), sfix(9849675.9598374), sfix(39252910.733885415), sfix(-33074623.610478915), sfix(8096573.271734185)],
        [sfix(157329797.74967852), sfix(-909465215.0635759), sfix(2296856473.8238993), sfix(-3255570055.4961543), sfix(2818755414.2794876), sfix(-1519316567.7642589), sfix(497313685.57259965), sfix(-90514528.11962949), sfix(7032328.262944373)],
        [sfix(-1271337889.1081164), sfix(3353598306.812001), sfix(-3793537981.7383685), sfix(2416521058.019535), sfix(-949663135.904446), sfix(236193633.53583908), sfix(-36355585.1271984), sfix(3169603.004825129), sfix(-119931.37038037083)]
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
def neuron033(x):
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
        [sfix(-16921979.418798767), sfix(-44754382.37339559), sfix(-42351059.080986574), sfix(-22635992.072279736), sfix(-7704847.501850415), sfix(-1709212.641383217), sfix(-239890.2514142104), sfix(-19375.05413567787), sfix(-687.00703395406)],
        [sfix(-1471905.93326358), sfix(-13354760.590597488), sfix(-38151268.09577911), sfix(-67794594.577095), sfix(-66463630.84668088), sfix(-37484146.063206896), sfix(-12302812.007199714), sfix(-2199676.357696953), sfix(-166420.23440204174)],
        [sfix(-378935.07906318264), sfix(-3871354.694093306), sfix(-3825978.364736063), sfix(-1668020.7298956956), sfix(3503146.684894263), sfix(-3715040.052699619), sfix(-16017122.411415605), sfix(-13383891.942195259), sfix(-3635031.940672112)],
        [sfix(-377590.56413602066), sfix(-3877210.73499468), sfix(-4073072.3555817534), sfix(442163.42592658533), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-2798012.183893814), sfix(18000425.005233377), sfix(-87387559.65146577), sfix(172745197.2448825), sfix(-208024100.63638568), sfix(147986725.93668), sfix(-60817758.88164912), sfix(13380459.481929835), sfix(-1222942.6912955833)],
        [sfix(312888095.8565802), sfix(-850109582.1334968), sfix(971228227.3454828), sfix(-630177413.3747212), sfix(251308963.43562552), sfix(-63255110.99895681), sfix(9834462.865112547), sfix(-864806.281147525), sfix(32968.9353824486)]
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
def neuron034(x):
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
        sfix(-1.5749999284744263),
        sfix(-1.3125),
        sfix(-1.0499999523162842),
        sfix(-0.5249999761581421),
        sfix(-0.26249998807907104),
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
        [sfix(-38268154.03052681), sfix(-80764572.84819798), sfix(-73687764.38593578), sfix(-38358464.02141143), sfix(-12485588.164139023), sfix(-2602415.53880686), sfix(-339118.37466831214), sfix(-25252.6276943381), sfix(-822.58186880121)],
        [sfix(93772199.60155411), sfix(245398789.67031494), sfix(265154571.1117648), sfix(152220877.1937493), sfix(49085755.806102745), sfix(8227147.867298499), sfix(394683.21989476104), sfix(-70788.1251054972), sfix(-8094.57158821386)],
        [sfix(-50828458.971726276), sfix(-185061578.78544053), sfix(-265393999.4217542), sfix(-185403134.2831812), sfix(-56689673.57482884), sfix(2984847.4283939954), sfix(7325409.834636247), sfix(1977684.2186504095), sfix(180082.27254832143)],
        [sfix(41271732.31778822), sfix(228600210.15455642), sfix(544302173.6221756), sfix(716059060.47039), sfix(567065018.238928), sfix(277304610.738593), sfix(82076205.40180497), sfix(13488788.072916197), sfix(944387.7106880473)],
        [sfix(-4907446.211969403), sfix(-36651857.346234806), sfix(-122159191.19112043), sfix(-240650477.91977045), sfix(-291145132.7469804), sfix(-215321026.27806985), sfix(-94629957.5062212), sfix(-22725597.3570271), sfix(-2302168.115570111)],
        [sfix(-371242.9553943777), sfix(-362572.57079076994), sfix(4851768.905258405), sfix(13367558.00177149), sfix(26371362.023993228), sfix(38686209.97978413), sfix(32370029.590398), sfix(13558860.739772694), sfix(2233201.7155449623)],
        [sfix(-423371.9319123107), sfix(-1058128.988614669), sfix(792012.6883050228), sfix(-171135.1739804384), sfix(-1844302.054638975), sfix(1054960.500951485), sfix(1004057.7538935499), sfix(-1379682.1200032576), sfix(-879359.0576262817)],
        [sfix(-423371.1037506251), sfix(-1050872.2180478347), sfix(965688.2734720111), sfix(918424.7575041084), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-423371.10375062504), sfix(-1060271.186808182), sfix(864983.3480106716), sfix(-804653.1479054663), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(22240.46920998626), sfix(-5133834.9136655135), sfix(16534869.560539912), sfix(-33289733.39027829), sfix(38723769.77998418), sfix(-26841420.444629554), sfix(10917760.696208533), sfix(-2408523.1503690006), sfix(222795.64419875905)],
        [sfix(1980092.6917766042), sfix(-7116927.872967379), sfix(7283158.008418665), sfix(-4578937.6585033415), sfix(1627772.3246189654), sfix(-339340.04194769805), sfix(40163.6125777087), sfix(-2362.07445377011), sfix(45.01430758598)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
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
def neuron035(x):
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
        sfix(-0.5249999761581421),
        sfix(-0.26249998807907104),
        sfix(0.0),
        sfix(0.13124999403953552),
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
        [sfix(31301542.71738016), sfix(91002839.55087547), sfix(107677677.70641679), sfix(71017401.74059588), sfix(28792029.943011977), sfix(7364159.658187108), sfix(1162054.7296279764), sfix(103563.26829314652), sfix(3995.42704890614)],
        [sfix(7831049.002447101), sfix(44020141.06080197), sfix(114497191.86319214), sfix(171660608.55512777), sfix(152480979.5166962), sfix(81830480.36300565), sfix(26177692.115439817), sfix(4613340.571853385), sfix(345880.83121950406)],
        [sfix(799908.5064387011), sfix(799115.3414650012), sfix(-2448864.5234625326), sfix(-10765351.721408414), sfix(-27519231.890831523), sfix(-33586845.79266832), sfix(-20935688.31258398), sfix(-6609577.67767235), sfix(-850583.1972338179)],
        [sfix(846376.994136566), sfix(1423628.936075109), sfix(1217393.3802085156), sfix(1517410.599656553), sfix(-1828405.5805024493), sfix(773376.6121928827), sfix(7765800.148738514), sfix(7082463.959056353), sfix(2005792.9103078342)],
        [sfix(846366.2409633198), sfix(1427224.2531399857), sfix(1315499.1685454806), sfix(2262283.5922026373), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(846366.2409633197), sfix(1422166.1809289092), sfix(1259612.1750396264), sfix(809950.2571418087), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(845658.4097994814), sfix(1440916.701741412), sfix(1031857.4270354216), sfix(2371781.3348920373), sfix(-5002503.475191728), sfix(3105255.202730591), sfix(692515.6204058989), sfix(-1543185.0013493204), sfix(474165.58581051417)],
        [sfix(1320690.9429211116), sfix(-2823161.0528109623), sfix(16594839.719611645), sfix(-28032048.43180598), sfix(29297799.514312938), sfix(-18668412.692527484), sfix(7048182.042780956), sfix(-1445390.6018889055), sfix(123959.00493291416)],
        [sfix(-78947751.49941187), sfix(222591273.0424544), sfix(-259882874.30635163), sfix(171931277.84636077), sfix(-69577727.17748562), sfix(17713814.469284665), sfix(-2779208.9244957115), sfix(246213.2833569124), sfix(-9444.24127812344)]
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
def neuron036(x):
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
        sfix(-0.13124999403953552),
        sfix(0.0),
        sfix(0.13124999403953552),
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
        [sfix(8515381.611413585), sfix(34488348.36591502), sfix(53738409.18382097), sfix(44827700.169302285), sfix(22288074.1519613), sfix(6827090.328671401), sfix(1266153.4119275513), sfix(130591.53027407797), sfix(5755.26503945024)],
        [sfix(170971.41024245264), sfix(858583.6127184429), sfix(-669008.8656317018), sfix(-78765.98738681561), sfix(1301234.8578374188), sfix(-1173300.5405518946), sfix(-3139653.035133136), sfix(-1828562.6717525076), sfix(-346982.2743837657)],
        [sfix(170987.56328411284), sfix(858382.3711440932), sfix(-695109.9007240726), sfix(-443234.1358890787), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(170987.56328411284), sfix(859594.5088793811), sfix(-690444.8451679917), sfix(322424.8533484061), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(171591.43875475437), sfix(843883.0987793928), sfix(-510237.696491566), sfix(-845869.376961048), sfix(3918681.7594725606), sfix(-4518943.246352501), sfix(1626216.7451669588), sfix(335466.58501636685), sfix(-244903.9408187922)],
        [sfix(1309947.7443398803), sfix(-4140263.2920643263), sfix(6576072.783796952), sfix(-932796.4286431166), sfix(-6522682.922160229), sfix(7152872.852121442), sfix(-3364780.090916112), sfix(766934.6978425839), sfix(-69410.65623208674)],
        [sfix(33804079.796631776), sfix(-84992827.00960352), sfix(93056307.27896133), sfix(-56896317.34482991), sfix(21524423.468223047), sfix(-5166579.095706594), sfix(769162.2165089379), sfix(-64981.83744196952), sfix(2386.80548997931)]
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
def neuron037(x):
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
        [sfix(-11401657.137589172), sfix(-36009172.53628188), sfix(-44001994.92497607), sfix(-29682484.701577682), sfix(-12256434.663722534), sfix(-3182675.024909522), sfix(-508544.981419966), sfix(-45793.79267637063), sfix(-1782.00198302732)],
        [sfix(-465446.88621748704), sfix(-404632.43160945806), sfix(4502906.0868343515), sfix(8542689.203805508), sfix(9298598.407426069), sfix(6921780.325153393), sfix(3202837.3206474334), sfix(803362.1935559878), sfix(82905.98286767818)],
        [sfix(-576645.1495936125), sfix(-1459591.8560794455), sfix(325515.99894245557), sfix(-279316.2561912545), sfix(-1042300.7674958305), sfix(1039603.734193985), sfix(3040357.328936482), sfix(2310158.89998849), sfix(623158.8884733237)],
        [sfix(-576649.0404993463), sfix(-1455845.2590008492), sfix(417996.7877026992), sfix(318841.62215541746), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-576649.0404993464), sfix(-1463445.2147160533), sfix(400400.2653619845), sfix(-833701.45809367), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-283255.5416579581), sfix(-3937568.8487628293), sfix(9036939.707201831), sfix(-16619853.027460326), sfix(15688746.81566799), sfix(-8215652.594425187), sfix(2314699.7188844015), sfix(-303790.3610450162), sfix(11017.65928447684)],
        [sfix(-15909005.387530865), sfix(34644237.71553763), sfix(-36320516.60075816), sfix(20147992.4480675), sfix(-7028440.70155165), sfix(1577573.1026123075), sfix(-222055.59345819868), sfix(17891.60002531223), sfix(-631.06067710861)]
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
def neuron038(x):
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
        sfix(-2.0999999046325684),
        sfix(-1.0499999523162842),
        sfix(-0.13124999403953552),
        sfix(0.0),
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
        [sfix(20251672.650331065), sfix(41268835.8750042), sfix(38071847.18550414), sfix(20131035.102809623), sfix(6632829.151514316), sfix(1394116.7314848064), sfix(182679.04189503356), sfix(13653.49004845016), sfix(445.84558966731)],
        [sfix(-63598454.45623795), sfix(-172298258.98225453), sfix(-193581998.1676025), sfix(-118828936.45418814), sfix(-43250192.48117207), sfix(-9353817.713105554), sfix(-1113533.552426788), sfix(-56001.91054862465), sfix(63.81883677183)],
        [sfix(-18469095.448470637), sfix(-108566603.95530768), sfix(-271222538.5988817), sfix(-373927795.5614525), sfix(-308137221.6472947), sfix(-155937490.12546244), sfix(-47663582.211755015), sfix(-8101096.606674236), sfix(-589579.8992398034)],
        [sfix(233262.70399063916), sfix(-419111.34197780915), sfix(-2061931.2546843307), sfix(-50583.69577577353), sfix(4597519.106891324), sfix(781852.0150802282), sfix(-5040984.9001768585), sfix(-3914771.5694807074), sfix(-879439.9820910023)],
        [sfix(232918.9438111732), sfix(-429078.88689196494), sfix(-2215893.9482060643), sfix(-1376743.4869188205), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(232918.9438111732), sfix(-426268.7545629135), sfix(-2212535.415887648), sfix(400762.04156402213), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(232909.70395564497), sfix(-427232.15707739827), sfix(-2153571.0023872806), sfix(-391630.9716880806), sfix(2980406.965443738), sfix(1775054.7563023027), sfix(-9265556.24992216), sfix(8214559.010756288), sfix(-2375405.7963064094)],
        [sfix(-583568.6402782287), sfix(6884193.416764108), sfix(-29695280.541810375), sfix(55710865.63560909), sfix(-62258738.033001944), sfix(41899351.311744004), sfix(-16626856.912816735), sfix(3585292.8822204378), sfix(-324387.0926207362)],
        [sfix(50598386.322625615), sfix(-139001010.48507428), sfix(160275232.59847197), sfix(-104991874.85164683), sfix(42237656.2646681), sfix(-10716910.452209942), sfix(1678491.1254812854), sfix(-148599.75317944094), sfix(5700.2356839529)]
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
def neuron040(x):
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
        [sfix(-33390752.455931053), sfix(-78063697.64512207), sfix(-81557983.1667415), sfix(-48358703.35572057), sfix(-17747469.95544386), sfix(-4133687.4716493734), sfix(-597628.1933143509), sfix(-49087.99900685123), sfix(-1755.14848686648)],
        [sfix(36814.41878016588), sfix(3364464.4070230904), sfix(8384601.2607081635), sfix(11367667.944067495), sfix(5053106.123615397), sfix(-2785530.75737255), sfix(-3620463.969771584), sfix(-1300087.7790301957), sfix(-161384.3779781917)],
        [sfix(-279097.042999398), sfix(944299.2132471112), sfix(1067695.273150074), sfix(1039099.157211116), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-278751.85905585164), sfix(954516.3096723704), sfix(1054447.3480816318), sfix(531796.8243214993), sfix(-968905.0472585894), sfix(-1133596.3637274744), sfix(4582039.480284557), sfix(-4190827.7819808284), sfix(1247164.0533439412)],
        [sfix(232525.6580202463), sfix(-3668163.571807948), sfix(18688653.70755813), sfix(-36050999.10246123), sfix(42920203.944159985), sfix(-30128460.93766487), sfix(12227320.008641897), sfix(-2665479.3074736963), sfix(242372.89341546115)],
        [sfix(-20548937.790752664), sfix(50711947.530824885), sfix(-50717427.603257515), sfix(30720495.087512728), sfix(-11528150.663694082), sfix(2747756.1343689566), sfix(-406885.2752585757), sfix(34258.84874335343), sfix(-1256.46739122077)]
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
def neuron041(x):
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
        [sfix(59032094.25668443), sfix(191836866.4940463), sfix(246996130.466976), sfix(172795294.4695308), sfix(73038075.10443698), sfix(19261161.255471624), sfix(3110969.5866923686), sfix(282369.82358000946), sfix(11055.50703242084)],
        [sfix(-457851.7615755498), sfix(-202213.5283621048), sfix(-9062143.06376249), sfix(-27706953.189873036), sfix(-47755549.07506476), sfix(-45549807.388038576), sfix(-23474262.73376733), sfix(-6159471.53867107), sfix(-648032.1602074773)],
        [sfix(-366109.1273994969), sfix(1457810.9613721727), sfix(733893.7672965274), sfix(1035118.8944887496), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-366121.39875117614), sfix(1458322.3213274064), sfix(754817.47798224), sfix(939404.7346759811), sfix(-611980.1340986138), sfix(-611488.3530695867), sfix(1419213.211087036), sfix(-1098352.413750288), sfix(303771.8806120452)],
        [sfix(-245127.2571239898), sfix(323419.96154660557), sfix(5247971.002192373), sfix(-8743845.927484214), sfix(11505900.362605955), sfix(-9109835.119305171), sfix(4077129.8913614065), sfix(-959522.0955132295), sfix(92712.90247698098)],
        [sfix(-9339441.77606647), sfix(24180972.08796804), sfix(-22876723.640513662), sfix(14280579.919386925), sfix(-5470460.168946266), sfix(1322054.5564692763), sfix(-197689.1769318801), sfix(16768.06063627901), sfix(-618.63056646608)]
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
def neuron042(x):
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
        sfix(-2.0999999046325684),
        sfix(-0.5249999761581421),
        sfix(-0.13124999403953552),
        sfix(0.0),
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
        [sfix(305591129.38562477), sfix(634950395.3241539), sfix(580727675.5917989), sfix(303603944.23103094), sfix(99120519.65968783), sfix(20692274.712515406), sfix(2697688.566732465), sfix(200837.18474310808), sfix(6537.5292928599)],
        [sfix(-4508788.848074963), sfix(275450700.947108), sfix(776823706.0960357), sfix(893138743.0736816), sfix(556879210.8415401), sfix(205128144.5223864), sfix(44835938.825269766), sfix(5398970.555132288), sfix(276796.90406167094)],
        [sfix(3118466.1832489157), sfix(20045394.6525796), sfix(80759370.10244058), sfix(160773719.95419878), sfix(191231747.3598817), sfix(136335966.53050175), sfix(56287702.07910148), sfix(12384540.532710595), sfix(1125037.7458372787)],
        [sfix(702870.8268359969), sfix(-1464461.8023512673), sfix(-28523.28615745774), sfix(-4252095.621951881), sfix(-3759406.7555425344), sfix(9608338.768604346), sfix(23962776.22958648), sfix(19680116.550791964), sfix(5684715.116536377)],
        [sfix(702834.5175241816), sfix(-1463446.5571711983), sfix(64386.60573791742), sfix(-3008824.6402026536), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(702834.5175241816), sfix(-1467540.6805257613), sfix(28697.41442352744), sfix(-5632413.794551728), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(702880.9364406649), sfix(-1467691.318866238), sfix(-22812.18177329814), sfix(-4790988.54808248), sfix(-3462538.190799928), sfix(-3426720.305494176), sfix(26611470.090671863), sfix(-26099653.031101897), sfix(7926742.284309647)],
        [sfix(3722163.959747871), sfix(-28419941.71389507), sfix(101309958.53955731), sfix(-211348299.87160945), sfix(238326090.69614705), sfix(-155773438.05815142), sfix(59361772.97873763), sfix(-12292430.55920792), sfix(1072600.1970448387)],
        [sfix(-27529798.16777071), sfix(62426587.961912885), sfix(-68799093.35640098), sfix(39605982.868093), sfix(-14317411.38308714), sfix(3323567.82398064), sfix(-482698.65263766627), sfix(40033.52564242676), sfix(-1450.11405149178)]
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
def neuron043(x):
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
        sfix(0.0),
        sfix(0.06562499701976776),
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
        [sfix(1247886887.1901283), sfix(3411531168.1945624), sfix(3962172117.8573117), sfix(2574531344.1665683), sfix(1028145244.7955183), sfix(259133709.42552608), sfix(40334014.87910171), sfix(3549943.4233942786), sfix(135420.01667362778)],
        [sfix(-5607733.02039623), sfix(-46317448.37265562), sfix(-188539383.1543042), sfix(-380969284.41076815), sfix(-455195062.1041057), sfix(-324566330.5191486), sfix(-134113198.46097292), sfix(-29597861.86622059), sfix(-2702921.8207309735)],
        [sfix(-171464.4704871785), sfix(2421066.8563823476), sfix(-4438421.251034574), sfix(-2776750.066246299), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-171464.4704871785), sfix(2497075.612716422), sfix(-3328427.3532259515), sfix(4325241.08228877), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-171483.0746634164), sfix(2497539.1473408467), sfix(-3299115.8523368468), sfix(3264152.3890588977), sfix(8383060.618039607), sfix(7468631.99524068), sfix(-36224129.8233342), sfix(31091676.75311843), sfix(-8591528.17828056)],
        [sfix(67918.45949474389), sfix(-701545.7213713748), sfix(15389446.499045616), sfix(-59061875.2269024), sfix(138107352.87545326), sfix(-164931927.42852196), sfix(106405841.6003648), sfix(-35877518.336234435), sfix(5003744.365693854)],
        [sfix(7574016.876015593), sfix(-32114633.74205182), sfix(50178782.996093296), sfix(-16444249.509916073), sfix(-19373637.140957087), sfix(22724754.97005983), sfix(-10134436.030228082), sfix(2178391.1354310187), sfix(-187500.47484468343)],
        [sfix(-3283580.2557554725), sfix(12077385.09663467), sfix(-8289602.4401959665), sfix(6578366.658787872), sfix(-2898026.358868916), sfix(765540.283666349), sfix(-121883.6215914406), sfix(10847.97178127888), sfix(-416.24914377495)]
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
def neuron044(x):
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-27077251.466477234), sfix(-78771497.76051454), sfix(-92122329.15569443), sfix(-60314240.31862588), sfix(-24379916.65189815), sfix(-6233841.6672611), sfix(-984855.271901048), sfix(-87941.80238027517), sfix(-3400.58511497797)],
        [sfix(-35334808.11541853), sfix(-199407539.92784566), sfix(-469535818.16475064), sfix(-613593485.8565533), sfix(-484580291.53462774), sfix(-237463077.03531128), sfix(-70860274.52010302), sfix(-11828327.311945675), sfix(-848974.0440166912)],
        [sfix(-395908.0140852721), sfix(-3424887.38425218), sfix(-1759109.2035902431), sfix(163106.13284114777), sfix(-8437854.331006557), sfix(-19327754.80934762), sfix(-14886786.523664424), sfix(-4215843.4935241155), sfix(-193305.0253165016)],
        [sfix(-393828.10923316434), sfix(-3372534.136172274), sfix(-1227323.8677234445), sfix(3003105.522497301), sfix(271627.9771333291), sfix(-3758695.126127758), sfix(338792.71794005396), sfix(1978264.480673041), sfix(-541545.5370719918)],
        [sfix(-393883.8567677172), sfix(-3369637.1967450776), sfix(-1190983.7128657575), sfix(2652870.6774196047), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-573377.112896865), sfix(-1127807.4575722169), sfix(-12469556.439940542), sfix(32162852.825708076), sfix(-41823644.52342613), sfix(29322980.08339276), sfix(-11499732.62532612), sfix(2389230.4079691195), sfix(-205526.956265304)],
        [sfix(3423091.111829875), sfix(-10707702.493823843), sfix(7232799.489071294), sfix(-5151941.402727324), sfix(2115470.856466047), sfix(-528702.6895263955), sfix(80228.1859213198), sfix(-6837.62375679394), sfix(252.1535687042)]
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
def neuron045(x):
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
        sfix(-0.06562499701976776),
        sfix(0.0),
        sfix(0.13124999403953552),
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
        [sfix(-486558279.372831), sfix(-1294841973.3839595), sfix(-1479728304.3662171), sfix(-948499824.1988646), sfix(-374142183.95541495), sfix(-93244216.84353769), sfix(-14365782.429427072), sfix(-1252706.481899437), sfix(-47386.25998492641)],
        [sfix(-735757.2146903742), sfix(-6610232.147086013), sfix(-63282795.3267205), sfix(-168551154.1370505), sfix(-221135794.4151263), sfix(-164657818.15701857), sfix(-71095698.41909574), sfix(-16606347.79903919), sfix(-1623324.7576417401)],
        [sfix(823591.310526318), sfix(9184021.944044048), sfix(4168938.458347162), sfix(-11134239.057571959), sfix(-4553199.365659652), sfix(10209184.651298808), sfix(4128177.0902747707), sfix(-4957762.138948346), sfix(-2718864.6900603687)],
        [sfix(823591.4462993636), sfix(9184338.2872791), sfix(4198410.693957108), sfix(-10416597.045239821), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(823591.4462993635), sfix(9183320.591965396), sfix(4208033.812239327), sfix(-11798092.215159284), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(819933.902515017), sfix(9275975.504783908), sfix(3237401.6948732724), sfix(-6180917.431282292), sfix(-19557734.593647953), sfix(36411293.81204225), sfix(-19294357.93347086), sfix(1636314.753027071), sfix(936691.3003665353)],
        [sfix(-14489323.216519339), sfix(87854846.8522083), sfix(-159106430.8768749), sfix(158180768.52544573), sfix(-90961790.3311986), sfix(31583263.87604138), sfix(-6428749.270382639), sfix(677114.5699397972), sfix(-25187.1661364318)],
        [sfix(37027491.085642375), sfix(-85473242.21982333), sfix(96374814.02216443), sfix(-56514609.19032393), sfix(20814586.955630407), sfix(-4921376.629708039), sfix(727572.0282142601), sfix(-61378.01670057825), sfix(2259.55763327506)]
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
def neuron046(x):
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
        sfix(-0.01640624925494194),
        sfix(0.13124999403953552),
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
        [sfix(208376705.82326642), sfix(575483084.6393527), sfix(669623297.3418257), sfix(435862086.84274006), sfix(174456547.43856147), sfix(44080801.582853116), sfix(6878588.365425577), sfix(606886.8083135745), sfix(23203.88879245658)],
        [sfix(-1658352.9046888014), sfix(-11829223.298883788), sfix(-64001500.91141364), sfix(-149674956.44825104), sfix(-192495616.0480036), sfix(-142926627.0211009), sfix(-60883197.504336804), sfix(-13839609.246415433), sfix(-1304089.2062457486)],
        [sfix(96621.31054893132), sfix(4674165.539178158), sfix(1968341.9161771815), sfix(-4327159.6300555365), sfix(-2001761.7342463278), sfix(5009265.464583182), sfix(1130793.1253694936), sfix(-4073292.156463315), sfix(-1981816.5808079178)],
        [sfix(96618.548547167), sfix(4674213.660213656), sfix(1977313.4007187374), sfix(-4550375.322092207), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(94447.27415416935), sfix(4728855.085293789), sfix(1414027.237098916), sfix(-1368677.057747969), sfix(-10946496.114809966), sfix(21099070.403962303), sfix(-12808370.59102188), sfix(2051915.8058633383), sfix(330402.855211705)],
        [sfix(-12701863.918387948), sfix(72200018.88615406), sfix(-144638541.7278275), sfix(160922080.03885862), sfix(-102062207.49709803), sfix(38177168.69083899), sfix(-8133748.022980994), sfix(861477.8674554083), sfix(-29277.77488348806)],
        [sfix(-25484625.97635131), sfix(63671108.44607945), sfix(-60990758.09452632), sfix(37083136.97322078), sfix(-13910396.040090708), sfix(3304167.326914055), sfix(-486755.0298479719), sfix(40737.93497989719), sfix(-1484.64786485754)]
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
def neuron047(x):
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
        sfix(-0.26249998807907104),
        sfix(-0.13124999403953552),
        sfix(0.0),
        sfix(0.13124999403953552),
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
        [sfix(194980564.22277263), sfix(543746318.8961173), sfix(640494976.6334214), sfix(420662248.9868653), sfix(169416161.3626285), sfix(42992158.37000239), sfix(6729536.164179347), sfix(595100.3791518484), sfix(22792.91917676558)],
        [sfix(-34914.99322070344), sfix(-1301808.1717996385), sfix(-10393935.270010043), sfix(-26254752.381546695), sfix(-40142087.369020656), sfix(-35047632.97772982), sfix(-16797216.32895997), sfix(-4134928.993047471), sfix(-410542.44803252)],
        [sfix(114795.63237328826), sfix(601774.3057394542), sfix(-569547.8533587506), sfix(935162.3849971286), sfix(6764350.650980196), sfix(28627291.48574262), sfix(73325237.25542676), sfix(107320957.16656828), sfix(68795922.24234448)],
        [sfix(114686.9829598429), sfix(596984.1836482622), sfix(-661244.9095356924), sfix(-64759.91549512663), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(114686.98295984288), sfix(597141.1636541197), sfix(-668319.7464414205), sfix(28840.89113703958), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(114057.40671899993), sfix(612822.3516066081), sfix(-821771.7538812296), sfix(804030.4705299371), sfix(-2448748.329326268), sfix(5359270.346961966), sfix(-4020474.2361203004), sfix(997361.8049471295), sfix(2581.16544814188)],
        [sfix(-5930332.489942729), sfix(33490440.251351755), sfix(-75688189.03088291), sfix(91844210.09036614), sfix(-64258704.20686965), sfix(27004746.83184839), sfix(-6719987.7481945045), sfix(907597.1129389801), sfix(-50680.96528413165)],
        [sfix(-21115980.089538574), sfix(51078836.461387984), sfix(-52318807.402982175), sfix(31307367.97246912), sfix(-11648434.78021268), sfix(2760377.9373012055), sfix(-407084.65561001754), sfix(34170.35544607208), sfix(-1250.14140943792)]
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
def neuron048(x):
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
        sfix(-0.26249998807907104),
        sfix(-0.06562499701976776),
        sfix(0.0),
        sfix(0.13124999403953552),
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
        [sfix(55772839.08653608), sfix(141354576.64581397), sfix(152951134.05101812), sfix(93867533.18080744), sfix(35818798.67032383), sfix(8701553.129621841), sfix(1313918.4299264357), sfix(112738.48834776517), sfix(4208.65550694332)],
        [sfix(87999.97191262814), sfix(289313.2917070267), sfix(287637.5204483742), sfix(3568518.172781896), sfix(8427989.582568288), sfix(9322719.189406985), sfix(5363301.195245315), sfix(1543621.6280592778), sfix(175844.91669080092)],
        [sfix(96493.80772984424), sfix(348768.86685899226), sfix(221145.2416350317), sfix(1871814.9266835214), sfix(2351800.510973928), sfix(263864.53831956617), sfix(2912035.347939546), sfix(11717595.654006714), sfix(10842091.7763432)],
        [sfix(96492.42148095484), sfix(348562.8022056393), sfix(207556.59865837632), sfix(1553873.659811552), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(96492.42148095486), sfix(349300.2453193586), sfix(187698.4748682445), sfix(2266298.8811441823), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(97979.76178910864), sfix(311343.2528117367), sfix(595906.4375315628), sfix(-157413.82447508612), sfix(7978237.607584026), sfix(-11554578.645934023), sfix(4821879.180702736), sfix(502983.3588179492), sfix(-555844.2469124068)],
        [sfix(5092185.584357594), sfix(-24826028.256596558), sfix(50749553.54317639), sfix(-47261079.195055604), sfix(23553024.77236569), sfix(-5506807.514845176), sfix(38278.8554987249), sfix(233803.09948649295), sfix(-32407.39800170908)],
        [sfix(7275033.429029141), sfix(-15666211.528526956), sfix(18233700.969987795), sfix(-10181627.439663636), sfix(3591686.1723200427), sfix(-818308.9769375382), sfix(117118.29063119445), sfix(-9597.20424545975), sfix(344.05229110004)]
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
def neuron050(x):
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
        sfix(-0.5249999761581421),
        sfix(-0.26249998807907104),
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
        [sfix(-32221044.601490535), sfix(-68456163.72330885), sfix(-62316264.43914642), sfix(-32335492.713302705), sfix(-10498231.683717456), sfix(-2184192.0482478854), sfix(-284258.1000698752), sfix(-21148.46952539953), sfix(-688.44654875621)],
        [sfix(53818992.21363169), sfix(121228486.4786573), sfix(101581264.19988625), sfix(31287389.59592479), sfix(-6106142.896778393), sfix(-7748359.600535698), sfix(-2476046.726062546), sfix(-364080.6727192133), sfix(-21154.34361861288)],
        [sfix(40146886.46085261), sfix(230588990.17844144), sfix(548118376.1368332), sfix(707407127.7720788), sfix(547228934.729804), sfix(261854301.734636), sfix(76194358.34803297), sfix(12394375.210084006), sfix(866747.4535047665)],
        [sfix(-1135265.5634645543), sfix(1530998.6370322246), sfix(12470191.116468), sfix(34018844.006304674), sfix(75825468.43469426), sfix(104399763.99216248), sfix(78579919.01949528), sfix(30125810.229099836), sfix(4645432.810086948)],
        [sfix(-1276584.3078455064), sfix(-358587.9331670933), sfix(1422505.88559979), sfix(-2873419.9970153975), sfix(-1142772.0697292436), sfix(1661859.2758133763), sfix(-7107952.073518554), sfix(-10704430.264763486), sfix(-3865031.571929992)],
        [sfix(-1275803.0851564233), sfix(-362592.5785447931), sfix(1377536.561447396), sfix(-2446374.190407474), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-1057177.4083129428), sfix(-3137125.47754796), sfix(15629600.738339683), sfix(-40773918.08565307), sfix(57228681.340942144), sfix(-45931491.357103035), sfix(20904666.290715434), sfix(-5025005.146501361), sfix(496520.8832463906)],
        [sfix(-3724857.160417049), sfix(12883888.134627989), sfix(-19620500.019760873), sfix(13917757.900159555), sfix(-5954568.157261897), sfix(1587151.2098180014), sfix(-258631.19381906855), sfix(23642.16389471768), sfix(-930.84220031934)]
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
def neuron051(x):
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
        sfix(-2.0999999046325684),
        sfix(-1.0499999523162842),
        sfix(-0.5249999761581421),
        sfix(-0.26249998807907104),
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
        [sfix(11517234.179253593), sfix(23034771.131339535), sfix(21372841.367762815), sfix(11392549.72672629), sfix(3776576.244259609), sfix(797009.661418921), sfix(104709.92548281344), sfix(7839.04192831696), sfix(256.24595835201)],
        [sfix(-25919595.154833447), sfix(-63914942.57517005), sfix(-61137800.10701837), sfix(-28391623.67422354), sfix(-5366708.192256398), sfix(634843.5994617483), sfix(506668.623164666), sfix(91784.522560173), sfix(5860.77915029361)],
        [sfix(-10832313.450967997), sfix(-58627612.16576526), sfix(-137029758.23304373), sfix(-180464916.74555746), sfix(-143587532.65078175), sfix(-70531081.60410878), sfix(-20984247.541631), sfix(-3477294.799969497), sfix(-246994.87160230603)],
        [sfix(-491017.2784886764), sfix(-1344267.1658871963), sfix(-3450829.280884108), sfix(-13403139.620628336), sfix(-27946069.633196313), sfix(-33313846.310304567), sfix(-22804832.68207746), sfix(-8295068.8076101085), sfix(-1243469.4732168482)],
        [sfix(-441308.1213488432), sfix(-682773.2789654022), sfix(401725.60934941453), sfix(-577800.6325407835), sfix(-1253908.4777163093), sfix(2247192.246031232), sfix(6810992.983406219), sfix(5801030.572216594), sfix(1692173.280757912)],
        [sfix(-441317.7331962117), sfix(-678099.1646453305), sfix(519468.51103403606), sfix(188614.10866450943), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-441317.7331962117), sfix(-676666.8537900199), sfix(375145.62557274994), sfix(-1075280.3631665574), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(415365.5978231603), sfix(-8241256.719161852), sfix(28476073.806468125), sfix(-57271293.46349046), sfix(64277448.247608736), sfix(-42236990.39428698), sfix(16111020.512750905), sfix(-3308355.660137302), sfix(283461.4221349129)],
        [sfix(-91627004.65775299), sfix(241999844.83452874), sfix(-276799110.18342876), sfix(176732417.70551032), sfix(-69649073.47393322), sfix(17375658.954935927), sfix(-2682744.6360231554), sfix(234585.2544025951), sfix(-8901.09669070413)]
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
def neuron052(x):
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
        sfix(-0.5249999761581421),
        sfix(-0.26249998807907104),
        sfix(0.0),
        sfix(0.13124999403953552),
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
        [sfix(-44540936.30942183), sfix(-117806094.56203477), sfix(-136894076.0274893), sfix(-89165377.58086714), sfix(-35642201.068140365), sfix(-8983755.39368132), sfix(-1398011.205561777), sfix(-123022.25248430824), sfix(-4692.8471832616)],
        [sfix(-28715657.99014208), sfix(-167576171.39300644), sfix(-383931289.3277454), sfix(-464863254.5891817), sfix(-334676768.0762633), sfix(-148879343.74362683), sfix(-40298259.69275914), sfix(-6100096.1904024165), sfix(-396704.05352998694)],
        [sfix(2071646.1327094482), sfix(-1852479.813783252), sfix(-15634660.041069392), sfix(-44781185.75200291), sfix(-103983770.42489372), sfix(-138844227.4900714), sfix(-99671335.9956142), sfix(-36585219.35621033), sfix(-5444661.634160977)],
        [sfix(2260685.0734987864), sfix(679006.0170418423), sfix(-816014.6806649746), sfix(4751603.149716054), sfix(-564944.740157547), sfix(-718033.7159406631), sfix(15584493.685920924), sfix(18353256.81310093), sfix(6009463.943757179)],
        [sfix(2260659.74654004), sfix(672313.2148794304), sfix(-947760.7128905643), sfix(4242025.326629189), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(2260659.74654004), sfix(676811.8361659485), sfix(-778353.5585153308), sfix(3924210.508160438), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(2260498.80554829), sfix(681859.8727393603), sfix(-869409.3618452115), sfix(4725766.268969412), sfix(-1867196.6466998465), sfix(-5951940.671961599), sfix(8503149.030266805), sfix(-4416115.075654869), sfix(836591.1544369595)],
        [sfix(23390195.336063426), sfix(-121690694.35859545), sfix(304397944.8230543), sfix(-421058294.62583977), sfix(357360474.1235163), sfix(-189679191.71280956), sfix(61428510.25207773), sfix(-11105034.726938823), sfix(859374.0895825416)],
        [sfix(-187198060.27455994), sfix(512647873.5212721), sfix(-592000361.896815), sfix(385317486.7875086), sfix(-153995043.64368448), sfix(38819981.92521124), sfix(-6041625.084167699), sfix(531614.5750065288), sfix(-20273.54216301765)]
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
def neuron053(x):
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
        [sfix(47091402.53185322), sfix(130030172.4658837), sfix(156260519.5825135), sfix(104351882.39214198), sfix(42519881.15065617), sfix(10881622.919488307), sfix(1714457.5140341967), sfix(152427.56185399095), sfix(5865.07996784105)],
        [sfix(30958920.718474027), sfix(176596779.5985879), sfix(407203421.0765125), sfix(503338827.4794874), sfix(372962878.5013714), sfix(171561555.50462338), sfix(48162628.904326044), sfix(7578988.887470008), sfix(513585.8134228948)],
        [sfix(-1192104.8641917326), sfix(2090628.4678122667), sfix(13797841.76252307), sfix(41518194.58214615), sfix(98049186.17823307), sfix(130907307.60904598), sfix(93999895.58893767), sfix(34573856.41511542), sfix(5160304.879325733)],
        [sfix(-1370287.977590947), sfix(-294607.82066038845), sfix(-160577.87385573098), sfix(-5128256.615645125), sfix(674686.2215338794), sfix(872623.1812403565), sfix(-14492129.19297595), sfix(-17136142.005881492), sfix(-5620014.384851762)],
        [sfix(-1370264.3588678078), sfix(-288537.02773638803), sfix(-42433.71547078696), sfix(-4694182.9815239115), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-1370264.3588678078), sfix(-282011.07903860416), sfix(-416537.58244488726), sfix(-3384850.922787033), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-1288641.0823550306), sfix(-1380507.4081037191), sfix(5811646.852949389), sfix(-22552078.629892502), sfix(32380527.42012534), sfix(-26872369.830146007), sfix(13152187.25632032), sfix(-3467506.0394236064), sfix(376915.8442654653)],
        [sfix(243307855.98890713), sfix(-652239912.6673551), sfix(741481530.3285295), sfix(-476633630.3691713), sfix(188596048.3366378), sfix(-47153549.142147034), sfix(7288286.966869502), sfix(-637571.8872199996), sfix(24192.32052813568)]
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
def neuron054(x):
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
        [sfix(-48242281.54676417), sfix(-134050594.21614502), sfix(-159158318.32462123), sfix(-105329511.88615231), sfix(-42688488.72213401), sfix(-10891229.254087085), sfix(-1712914.4313740307), sfix(-152129.4472039159), sfix(-5849.86839468811)],
        [sfix(57793.40664567738), sfix(4965180.101562552), sfix(14267269.418033823), sfix(29425219.329921197), sfix(41419551.686534986), sfix(34518599.8194966), sfix(16191188.540207177), sfix(3969001.3339448897), sfix(396864.682770559)],
        [sfix(-263253.87368605984), sfix(1777536.2693597581), sfix(1042647.8435043923), sfix(-706348.047472236), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-263253.8736860599), sfix(1748307.2267690606), sfix(702097.8512227421), sfix(-1945956.3949401036), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-263249.0770984268), sfix(1748291.9358080071), sfix(696224.9655334081), sfix(-1840903.7492343518), sfix(-540715.207884678), sfix(128376.24704508921), sfix(3656908.0856347866), sfix(-3684900.5869067046), sfix(1078623.9233610416)],
        [sfix(-289823.92580134794), sfix(2103413.973441066), sfix(-1378944.1483976233), sfix(5085374.955645778), sfix(-14983128.807330066), sfix(19392894.788287316), sfix(-12394441.67767782), sfix(3951620.1431152024), sfix(-509104.9356495572)],
        [sfix(5064422.79024098), sfix(-30512285.033320516), sfix(85850602.85098258), sfix(-129007088.6632959), sfix(114966880.0795778), sfix(-62163797.81210339), sfix(20086797.761238288), sfix(-3578930.0530540757), sfix(271275.91468551743)],
        [sfix(9491245.61264103), sfix(-31141433.110245008), sfix(42424185.120210215), sfix(-29821221.25604684), sfix(12644717.51514888), sfix(-3341823.727975496), sfix(540505.5371533115), sfix(-49097.71989864841), sfix(1922.92507637572)]
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
def neuron055(x):
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
        sfix(0.13124999403953552),
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
        [sfix(-55592626.218236774), sfix(-153559241.8043561), sfix(-186909886.46603808), sfix(-126010321.08899307), sfix(-51664016.75207556), sfix(-13276745.698162118), sfix(-2097985.7560407077), sfix(-186938.39099730132), sfix(-7205.49052787336)],
        [sfix(3855871.8190787383), sfix(22015067.887736462), sfix(71954364.62314536), sfix(157230230.3774532), sfix(195832228.33750814), sfix(140877466.4912428), sfix(58462315.63814271), sfix(13042269.126753103), sfix(1214051.2491630665)],
        [sfix(1955619.8980695545), sfix(4298446.053215884), sfix(1851932.219627364), sfix(4788692.693548529), sfix(-137112.09819654815), sfix(-6097513.064885406), sfix(1984015.1221723799), sfix(7633382.402734203), sfix(3134316.6337770247)],
        [sfix(1955638.8135551498), sfix(4298254.785488607), sfix(1829692.6931940431), sfix(4549331.892223461), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(1959861.9157698574), sfix(4190368.906027938), sfix(2931962.7819753126), sfix(-1114637.0534961093), sfix(17306614.936904743), sfix(-39290828.595587984), sfix(30293633.918906692), sfix(-8367168.27222999), sfix(302797.527314517)],
        [sfix(55751906.41248811), sfix(-292827759.6769086), sfix(695228221.9400963), sfix(-875983684.0603858), sfix(654247395.8584975), sfix(-298482491.15979713), sfix(81932739.53838632), sfix(-12461901.29158343), sfix(808427.3709333343)],
        [sfix(245931465.2542911), sfix(-632823656.1427735), sfix(714066072.627498), sfix(-448910698.2970824), sfix(174774889.31089696), sfix(-43182126.89717979), sfix(6615073.786992737), sfix(-574703.0407886638), sfix(21688.55641869704)]
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
def neuron056(x):
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
        sfix(-0.03281249850988388),
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
        [sfix(1083085.870713907), sfix(2039991.7707428052), sfix(3816191.532677382), sfix(3247539.3104083547), sfix(1492648.277692638), sfix(407208.5943472488), sfix(66560.62550990647), sfix(6055.28292330696), sfix(236.64866143717)],
        [sfix(184819.43382431587), sfix(411940.8795533596), sfix(11212585.344486019), sfix(27688955.952933457), sfix(31929752.893906858), sfix(20652650.7869757), sfix(7721746.173295455), sfix(1566500.535754395), sfix(134039.62495167874)],
        [sfix(-166012.16038265356), sfix(-2747425.2742767003), sfix(-847018.4546659201), sfix(2423921.776288741), sfix(711479.5251388071), sfix(-1708678.416377343), sfix(-293921.3288659581), sfix(1026369.9223055833), sfix(452213.84824448486)],
        [sfix(-166023.93772261348), sfix(-2747522.1218345426), sfix(-837653.0189632614), sfix(2440750.8763998095), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-140557.30994244438), sfix(-3098050.2865063287), sfix(1161470.2819706888), sfix(-3863176.013447521), sfix(12527238.872611843), sfix(-15549168.781888468), sfix(8940460.247178447), sfix(-2463925.988800052), sfix(265341.8389137103)],
        [sfix(-67927320.18483539), sfix(186769167.64830834), sfix(-221894752.66504765), sfix(145056173.0852045), sfix(-58278115.01133668), sfix(14774221.330507698), sfix(-2312157.976969921), sfix(204520.0640506888), sfix(-7837.30701067314)]
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
def neuron057(x):
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
        sfix(-2.0999999046325684),
        sfix(-1.0499999523162842),
        sfix(-0.5249999761581421),
        sfix(-0.26249998807907104),
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
        [sfix(-29461392.859629855), sfix(-62635693.501088224), sfix(-57018699.10172768), sfix(-29585058.057198923), sfix(-9605204.31561822), sfix(-1998490.1426675555), sfix(-260112.95485782583), sfix(-19354.29538898923), sfix(-630.12257077387)],
        [sfix(57905869.41458587), sfix(148235346.56990746), sfix(154172479.1688697), sfix(82023649.73309545), sfix(22258022.383381195), sfix(1931473.8100962578), sfix(-477472.08148246905), sfix(-133836.88907514611), sfix(-9759.58292147619)],
        [sfix(26722218.225625325), sfix(153444881.52382952), sfix(366532501.5330471), sfix(478341467.3336854), sfix(375396380.1445723), sfix(182377043.08651334), sfix(53853604.38580035), sfix(8881678.216319239), sfix(629094.5622873398)],
        [sfix(-690609.4028506018), sfix(758759.8642452992), sfix(7285529.91173191), sfix(21833983.537327282), sfix(48617456.21697486), sfix(65614820.8010495), sfix(48893319.8396721), sfix(18694164.825699493), sfix(2884643.342038747)],
        [sfix(-780348.4758113798), sfix(-441950.8595062472), sfix(261665.07564656765), sfix(-1631302.5168051615), sfix(-354601.04722683784), sfix(229318.43616061332), sfix(-5652063.296836251), sfix(-7300702.799733264), sfix(-2534235.6525236513)],
        [sfix(-780338.4456935042), sfix(-437775.69648677635), sfix(351726.5002887229), sfix(-1168636.3072138214), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-780338.4456935042), sfix(-413024.0879096589), sfix(-62110.91405522788), sfix(-654890.243957251), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-729594.4924108044), sfix(-677538.6871386612), sfix(330855.8945834149), sfix(-47189.63647153415), sfix(-3533844.467824324), sfix(5676036.5787578225), sfix(-3705109.0659725256), sfix(1117683.1252397676), sfix(-129193.66504759013)],
        [sfix(-31610654.67509936), sfix(71106595.36324845), sfix(-71097881.74806756), sfix(38994894.622434504), sfix(-13195022.058567889), sfix(2819402.1747406805), sfix(-371010.7437312284), sfix(27441.99296808346), sfix(-871.39317906097)]
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
def neuron058(x):
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
        sfix(-2.625),
        sfix(-2.0999999046325684),
        sfix(-1.0499999523162842),
        sfix(-0.5249999761581421),
        sfix(-0.13124999403953552),
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
        [sfix(20967740.25066928), sfix(43853796.31552641), sfix(40125683.72789762), sfix(20972787.903634086), sfix(6848487.670082717), sfix(1430632.3840264957), sfix(186702.75579916604), sfix(13916.80030469085), sfix(453.63301547527)],
        [sfix(-156632860.85741785), sfix(-448486811.8237468), sfix(-553428779.636535), sfix(-385902419.54312015), sfix(-166746996.4974118), sfix(-45805476.1627573), sfix(-7822637.381400056), sfix(-760144.3919832106), sfix(-32203.68743652791)],
        [sfix(18895666.732711714), sfix(93063730.6807546), sfix(177408739.7824406), sfix(177585322.89502466), sfix(104743608.69191411), sfix(37896967.76776576), sfix(8303873.915692875), sfix(1015063.0224516352), sfix(53280.42547832854)],
        [sfix(-19960854.449699618), sfix(-113645863.1045896), sfix(-275535856.0971551), sfix(-368389086.2812613), sfix(-295979866.62867326), sfix(-146797199.91236103), sfix(-44138065.53948855), sfix(-7397768.157172061), sfix(-531780.44128941)],
        [sfix(83778.16027414052), sfix(-488668.01246914), sfix(-3618154.233792021), sfix(-10274607.722685331), sfix(-21258476.203938503), sfix(-29639311.9124021), sfix(-23472010.278486844), sfix(-9467670.988096563), sfix(-1521818.5903257478)],
        [sfix(124234.36793878138), sfix(51077.28273494758), sfix(-468013.66433887504), sfix(230800.53869622745), sfix(638477.9840893848), sfix(-425891.29488934274), sfix(893172.5493585567), sfix(2150028.966751057), sfix(903628.2159977518)],
        [sfix(124231.27884730812), sfix(50646.45390259678), sfix(-484753.76564585016), sfix(34346.72303018137), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(124231.27884730815), sfix(51206.09023448225), sfix(-478787.10636616754), sfix(319778.9307738247), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(124229.92882684832), sfix(51013.60899020028), sfix(-470920.26340120425), sfix(221478.58918757073), sfix(466230.15005231206), sfix(-629969.092809806), sfix(-777202.781206872), sfix(1471727.2889697482), sfix(-567314.2684594828)],
        [sfix(147767.10623211216), sfix(-262743.29976895463), sfix(1358968.9626438352), sfix(-5877154.580017275), sfix(13170022.789425889), sfix(-17566554.390195075), sfix(13335435.366981355), sfix(-5248140.020347722), sfix(832588.535108544)],
        [sfix(10933121.288532715), sfix(-61150860.83240122), sfix(147675697.8896194), sfix(-198571620.3477995), sfix(160977813.653622), sfix(-80580983.23239757), sfix(24434675.641304534), sfix(-4126174.984408063), sfix(298566.09983152663)],
        [sfix(28123500.46376909), sfix(-80886558.82955591), sfix(97403312.03722638), sfix(-65007725.55285514), sfix(26495162.618136052), sfix(-6785443.648072167), sfix(1069832.4694417354), sfix(-95161.37568728375), sfix(3662.37448569879)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
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
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-2.0999999046325684),
        sfix(-1.0499999523162842),
        sfix(-0.26249998807907104),
        sfix(-0.06562499701976776),
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
        [sfix(-1124699592.7602768), sfix(-2868897659.720548), sfix(-3167089501.7686677), sfix(-1976747964.5328157), sfix(-763811519.4728501), sfix(-187282401.05070007), sfix(-28478895.508188266), sfix(-2457038.648503035), sfix(-92128.05484656947)],
        [sfix(441630133.47758454), sfix(2534455665.080386), sfix(6222071769.938569), sfix(8507912736.605105), sfix(7062052691.033933), sfix(3644245290.5928917), sfix(1144298041.9698267), sfix(200518849.8914107), sfix(15061276.220036892)],
        [sfix(1757353.7550205076), sfix(13051293.79365132), sfix(18995712.75545319), sfix(16953363.73302617), sfix(78269370.85734028), sfix(193003328.5919046), sfix(194879547.65085736), sfix(87556203.6962994), sfix(14641830.439030591)],
        [sfix(1677365.5143714268), sfix(11675242.254287755), sfix(8921326.126846334), sfix(-24108399.340026997), sfix(-23983813.37462035), sfix(32757413.80726496), sfix(39282498.38501787), sfix(1610314.139129485), sfix(-5413977.992890853)],
        [sfix(1677363.3788372716), sfix(11676589.277003566), sfix(9059587.690530308), sfix(-20617944.191122312), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(1677363.3788372716), sfix(11659909.712582234), sfix(9423122.730430616), sfix(-29814867.495008014), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(1491272.583544143), sfix(14871573.858915126), sfix(-14399277.889740754), sfix(70029942.88927683), sfix(-254000361.71617287), sfix(370256532.76568604), sfix(-256421044.5232879), sfix(84039680.57017158), sfix(-10153736.9744367)],
        [sfix(-150153458.38048637), sfix(839476515.1697671), sfix(-1887810280.035428), sfix(2327146519.027707), sfix(-1732150044.1883762), sfix(803203505.7790774), sfix(-227764052.67373678), sfix(36252311.073502526), sfix(-2487142.156007658)],
        [sfix(-152249426.85048264), sfix(434489852.8947436), sfix(-515143387.5332279), sfix(343577328.6188463), sfix(-140045513.3674198), sfix(35885707.246641435), sfix(-5663063.924024908), sfix(504314.60343140847), sfix(-19435.0235806201)]
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
        sfix(-4.199999809265137),
        sfix(-3.1499998569488525),
        sfix(-2.0999999046325684),
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
        [sfix(-4115565680.752301), sfix(-8994503182.962246), sfix(-8532263874.027994), sfix(-4599961763.541632), sfix(-1543129079.211027), sfix(-330039248.71676695), sfix(-43967988.7999893), sfix(-3336994.1743539553), sfix(-110502.56654935476)],
        [sfix(524243900.2679076), sfix(2997455261.154235), sfix(5888872060.43525), sfix(5863762677.217634), sfix(3398354748.5796347), sfix(1202058940.8099105), sfix(256813816.63221878), sfix(30548204.31519442), sfix(1557393.3921371219)],
        [sfix(526578494.51809055), sfix(2916034049.8490067), sfix(7052465305.604354), sfix(9541388013.605799), sfix(7893780527.643771), sfix(4087971250.5205297), sfix(1294328157.6557603), sfix(229306912.71870336), sfix(17432525.786237214)],
        [sfix(6861617.754261592), sfix(-18855524.58307049), sfix(-30346782.03820182), sfix(61742956.62265054), sfix(243861793.33543026), sfix(268176419.18753102), sfix(97254149.16065341), sfix(-17166417.70308717), sfix(-13850792.02066506)],
        [sfix(6821099.086800008), sfix(-19905029.44519002), sfix(-42206128.70640873), sfix(-13222672.27456872), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(6821099.086800008), sfix(-19839153.94344118), sfix(-42216350.25923261), sfix(28597202.838386282), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(6820799.209158282), sfix(-19859667.64263632), sfix(-40837464.03264591), sfix(9968467.631340716), sfix(67902835.13915528), sfix(61309299.23568813), sfix(-258039533.9412118), sfix(214724415.81298003), sfix(-59242532.50049832)],
        [sfix(8285390.239985813), sfix(-39415417.38621499), sfix(73361882.63274291), sfix(-370984416.15964264), sfix(861872562.2966425), sfix(-997278845.8185487), sfix(623559243.0736021), sfix(-204450499.58593345), sfix(27836561.64481191)],
        [sfix(-3185921.8970045503), sfix(96098424.36700094), sfix(-514988431.21291405), sfix(974776325.7633014), sfix(-976161775.0665339), sfix(564613401.3700973), sfix(-190765420.97341087), sfix(35135819.12594962), sfix(-2735873.3114056834)],
        [sfix(24584836.483633973), sfix(-62072021.457659006), sfix(42373271.40517671), sfix(-24642913.21571112), sfix(8547230.947427785), sfix(-1815803.5805236108), sfix(231994.14887131125), sfix(-16308.10626785498), sfix(480.31627502104)]
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
        sfix(-4.199999809265137),
        sfix(-3.1499998569488525),
        sfix(-2.0999999046325684),
        sfix(-1.0499999523162842),
        sfix(-0.13124999403953552),
        sfix(0.0),
        sfix(0.06562499701976776),
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
        [sfix(58101667.675234705), sfix(116404270.89778954), sfix(107895846.23947002), sfix(57440547.26345433), sfix(19021849.25898595), sfix(4011214.801871369), sfix(526659.13959977), sfix(39407.7205847389), sfix(1287.60491977518)],
        [sfix(1457600759.9392738), sfix(4232571274.0480065), sfix(5410723189.649651), sfix(3962919548.2018924), sfix(1816469449.153359), sfix(533133051.06378067), sfix(97783824.02676879), sfix(10242264.302418765), sfix(468901.32500694954)],
        [sfix(318402230.7211812), sfix(1854913920.7178102), sfix(5204615899.451427), sfix(7850926089.908359), sfix(6894306421.64344), sfix(3660824678.2104197), sfix(1163869470.6734543), sfix(204686710.68296608), sfix(15361533.898219882)],
        [sfix(5326269.917472538), sfix(-67482958.2114161), sfix(49069673.21452152), sfix(16312816.33311206), sfix(-367439497.5031937), sfix(-386299328.48808545), sfix(-25237370.981809888), sfix(112864512.83985122), sfix(38879266.87502952)],
        [sfix(5379780.693883119), sfix(-66084399.322665595), sfix(65400780.40220266), sfix(124881984.81599835), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(5379780.693883119), sfix(-66150943.33106303), sfix(63406468.55449235), sfix(65626148.40154698), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(5379971.376851773), sfix(-66152415.54416599), sfix(62791291.64589405), sfix(84379167.68673916), sfix(-140638365.7502811), sfix(-137684377.25472778), sfix(411490900.9335595), sfix(-311817366.88821656), sfix(81298014.00545853)],
        [sfix(3140270.029760364), sfix(-36314282.84010082), sfix(-111083659.8407834), sfix(663035273.59744), sfix(-1342802861.4736106), sfix(1456993282.105474), sfix(-904897483.3974977), sfix(304333570.8908734), sfix(-43155877.17059433)],
        [sfix(-375544587.6279296), sfix(2085619058.8036952), sfix(-5146689149.711777), sfix(7149848523.143743), sfix(-6107276504.307671), sfix(3279949125.893614), sfix(-1080087875.794338), sfix(199170770.67874262), sfix(-15742682.69339348)],
        [sfix(2567538825.2060924), sfix(-4881614435.765494), sfix(2176659635.232891), sfix(1798141320.9498813), sfix(-2510692554.822317), sfix(1252876256.499565), sfix(-325537038.7935848), sfix(44015046.914432116), sfix(-2456274.638512633)],
        [sfix(1767895115.013337), sfix(-2978454153.08512), sfix(2114749523.594715), sfix(-818904519.2140218), sfix(182103454.07389045), sfix(-21776118.888525575), sfix(903527.9254128389), sfix(64649.51302588729), sfix(-6040.13950270293)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
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
        sfix(-4.199999809265137),
        sfix(-3.1499998569488525),
        sfix(-2.0999999046325684),
        sfix(-1.0499999523162842),
        sfix(-0.13124999403953552),
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
        [sfix(-14485741381.554655), sfix(-31118149008.00309), sfix(-29155731792.24889), sfix(-15557531293.350494), sfix(-5172429981.132927), sfix(-1097556506.6804807), sfix(-145199415.55924898), sfix(-10952123.882319085), sfix(-360689.9019476176)],
        [sfix(-3104372577.252877), sfix(-8272968459.925882), sfix(-9224103841.780123), sfix(-5487777326.708473), sfix(-1825233200.6407826), sfix(-307738131.42554307), sfix(-11216479.913710104), sfix(3796168.9787145243), sfix(406992.0639215988)],
        [sfix(97822995.68669017), sfix(619585802.4040848), sfix(1540035689.67335), sfix(2160790431.097522), sfix(1867955302.0772076), sfix(1016271253.0492421), sfix(339219837.8227424), sfix(63430649.15335593), sfix(5084624.929915055)],
        [sfix(-6247280.494175212), sfix(21415990.157772798), sfix(55647467.193052694), sfix(78675249.40499796), sfix(42154218.25511503), sfix(-41448628.957029395), sfix(-82495106.90498784), sfix(-51147659.42366063), sfix(-11524458.72465504)],
        [sfix(-6259421.42520952), sfix(21116993.321510807), sfix(52567055.00691757), sfix(61117457.301299535), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-6260102.576244101), sfix(21131381.114144985), sfix(52228749.92044094), sfix(66932019.2406093), sfix(-23998064.328707803), sfix(-1561793.8844379773), sfix(-311524967.56765), sfix(388195885.95636374), sfix(-132001926.40748201)],
        [sfix(-1732411.3197318038), sfix(-39198980.77343217), sfix(403969308.030779), sfix(-1105036142.5226161), sfix(2416791259.524866), sfix(-3255159311.2515006), sfix(2399400369.4546747), sfix(-902664751.1840976), sfix(136952382.6015811)],
        [sfix(929818299.2368691), sfix(-5121449772.779247), sfix(11962713609.53161), sfix(-14909297791.788969), sfix(11006876347.431503), sfix(-4988541005.846462), sfix(1368899006.4275572), sfix(-209440547.41652575), sfix(13747800.662293188)],
        [sfix(2088776524.6481774), sfix(-5104063733.384198), sfix(5478300840.769354), sfix(-3323543954.471786), sfix(1255416439.308314), sfix(-302269809.1593327), sfix(45290996.46728952), sfix(-3860574.721059413), sfix(143316.73660495842)]
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
        sfix(-4.199999809265137),
        sfix(-2.0999999046325684),
        sfix(-1.8374998569488525),
        sfix(-1.0499999523162842),
        sfix(-0.5249999761581421),
        sfix(-0.26249998807907104),
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
        [sfix(342812359.915106), sfix(833578522.8359542), sfix(881891146.3845228), sfix(530501437.2418572), sfix(198506478.1160371), sfix(47319190.70458106), sfix(7018106.895669279), sfix(592167.2484205482), sfix(21765.23240293994)],
        [sfix(984513825.9469928), sfix(4088826144.3039136), sfix(7340582853.740919), sfix(7415019443.830885), sfix(4610059397.210152), sfix(1809045967.8888464), sfix(438368065.6647033), sfix(60081019.57645017), sfix(3571587.3694003704)],
        [sfix(-110880929.98716713), sfix(-609395595.6434468), sfix(-1400011543.499171), sfix(-1775510462.2197428), sfix(-1343949307.6776533), sfix(-612857790.4770539), sfix(-161248368.0576899), sfix(-21525203.37472192), sfix(-998061.9395175339)],
        [sfix(-3263946.827071989), sfix(-13549974.663030261), sfix(-30746917.54008737), sfix(-138114985.88584277), sfix(-350971664.67140853), sfix(-461246786.73148197), sfix(-329500280.9485564), sfix(-122338597.6326747), sfix(-18566449.655264817)],
        [sfix(-2650392.032504316), sfix(-5354836.27619281), sfix(17125565.87722775), sfix(21638727.72249141), sfix(-17858688.22411966), sfix(-16792468.078885145), sfix(41073290.16588637), sfix(54195862.32938474), sfix(18222725.701768596)],
        [sfix(-2650454.6529175527), sfix(-5342314.034191376), sfix(17551527.699718136), sfix(26098732.80401066), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-2650454.6529175527), sfix(-5368832.492735231), sfix(17626350.776497167), sfix(14571883.001113946), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-2650497.8179697725), sfix(-5355857.262166386), sfix(17059631.674020372), sfix(21389547.713056248), sfix(-21624187.19918542), sfix(-24095196.73570856), sfix(5321516.385527851), sfix(26286763.712807), sfix(-12964107.31739199)],
        [sfix(-2055056.7970006452), sfix(-13298632.832402073), sfix(63412533.87769209), sfix(-133196536.1899734), sfix(300648623.31197786), sfix(-454246364.7887856), sfix(364406421.22030747), sfix(-145205688.02314106), sfix(22936928.68587596)],
        [sfix(237904259.99910942), sfix(-1355111352.7048457), sfix(3240252632.894852), sfix(-4213831305.6398063), sfix(3285394180.3682895), sfix(-1586498303.6039152), sfix(466746604.79429257), sfix(-76910414.49464782), sfix(5456947.828548531)],
        [sfix(158574853.12922534), sfix(-396737823.4073417), sfix(432057421.24721456), sfix(-267011698.10751897), sfix(102520719.013843), sfix(-25044026.197637334), sfix(3801306.918930411), sfix(-327805.23686332017), sfix(12297.42609374032)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
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
        sfix(-4.199999809265137),
        sfix(-3.1499998569488525),
        sfix(-2.0999999046325684),
        sfix(-1.0499999523162842),
        sfix(-0.26249998807907104),
        sfix(-0.13124999403953552),
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
        [sfix(-264789750.22047532), sfix(-557570067.3313823), sfix(-508857593.9957721), sfix(-265031794.90909064), sfix(-86298273.72365227), sfix(-17990204.463786677), sfix(-2344283.5055334074), sfix(-174550.0518807968), sfix(-5684.8417261484)],
        [sfix(546458926.4104878), sfix(465621786.43481463), sfix(-820313801.4231449), sfix(-1596945908.3799095), sfix(-1161920687.4548583), sfix(-458116151.11287504), sfix(-103748183.09778056), sfix(-12750682.61161621), sfix(-661986.7710054978)],
        [sfix(1138019645.6356487), sfix(6331610020.23497), sfix(14949035232.522802), sfix(19179440494.927586), sfix(14704790344.000721), sfix(6961919190.237294), sfix(2003674375.6624577), sfix(322513751.94189847), sfix(22332809.711235672)],
        [sfix(-2839057.784862684), sfix(7434953.559431365), sfix(140994693.17972696), sfix(402360616.1865276), sfix(1114928347.9290168), sfix(1725761860.970445), sfix(1315166146.0980768), sfix(474301820.8896254), sfix(63973017.3960957)],
        [sfix(-3733100.0624783426), sfix(-7962375.456640722), sfix(27891775.734244976), sfix(-63202555.41944525), sfix(-78201604.7443515), sfix(-299683980.5673189), sfix(-1089341982.0942798), sfix(-1543997517.5844574), sfix(-883066372.5344288)],
        [sfix(-3732378.939807943), sfix(-7904164.80987868), sfix(29342125.823002927), sfix(-48071819.3016835), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-3709975.8972791727), sfix(-8440199.525166629), sfix(34562146.02530186), sfix(-78113144.2781935), sfix(93190258.24498007), sfix(-41068369.969463974), sfix(-24463544.31335067), sfix(33438456.333341416), sfix(-10140935.80871898)],
        [sfix(547050811.0865027), sfix(-3193471980.449868), sfix(7980016412.144561), sfix(-11216033330.983524), sfix(9670126990.584862), sfix(-5222277886.035326), sfix(1721572953.6420498), sfix(-316626615.7841023), sfix(24899474.63823939)],
        [sfix(-1046715982.1557755), sfix(-471252341.1454688), sfix(5700440315.421585), sfix(-8210962811.958928), sfix(5685954167.573107), sfix(-2238778712.186035), sfix(513968143.8987135), sfix(-64359942.85896117), sfix(3408949.206651672)],
        [sfix(-4604677072.171718), sfix(9499309514.816288), sfix(-8583040564.324266), sfix(4428575755.614877), sfix(-1428277834.2848208), sfix(294828135.3662627), sfix(-38037244.13738412), sfix(2804094.2827523747), sfix(-90430.69912629273)]
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
        sfix(-4.199999809265137),
        sfix(-3.1499998569488525),
        sfix(-2.0999999046325684),
        sfix(-1.8374998569488525),
        sfix(-1.0499999523162842),
        sfix(-0.5249999761581421),
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
        [sfix(10319264.72064233), sfix(17268341.02631091), sfix(14660996.260750402), sfix(7222927.969892491), sfix(2182454.6573480447), sfix(411544.6003082645), sfix(47210.81304182648), sfix(3001.90057561624), sfix(80.38412797761)],
        [sfix(2484863158.254086), sfix(7939360728.0376005), sfix(10854663246.468977), sfix(8342972347.882536), sfix(3959161540.5225096), sfix(1191212782.3815472), sfix(222350116.27992997), sfix(23574616.565975286), sfix(1088122.6557318298)],
        [sfix(-3618304876.4394755), sfix(-15109799667.423836), sfix(-27046916112.73747), sfix(-27124661128.544315), sfix(-16710595427.804287), sfix(-6494181053.708444), sfix(-1558772153.004199), sfix(-211737901.83182153), sfix(-12484419.273569683)],
        [sfix(370364990.4289217), sfix(2103412379.482512), sfix(5230277382.702633), sfix(7163979197.041551), sfix(5806826548.781884), sfix(2835751260.9927797), sfix(811889299.2614826), sfix(123550447.5607388), sfix(7483327.486704797)],
        [sfix(6988934.704299141), sfix(-2481344.47569473), sfix(24128441.94222537), sfix(79777243.32555959), sfix(136898455.14894843), sfix(243154183.61657414), sfix(253696569.57338238), sfix(123649962.98500174), sfix(22535168.1861219)],
        [sfix(6679770.298338603), sfix(-6568975.167994283), sfix(456763.32615190453), sfix(1394466.036587498), sfix(-25295387.320536822), sfix(28632670.54910482), sfix(76907551.09390663), sfix(40886084.08582355), sfix(5760659.420727862)],
        [sfix(6679622.9312838325), sfix(-6561130.925225411), sfix(1006344.0177894923), sfix(8712495.752043238), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(6679622.9312838325), sfix(-6584574.336334481), sfix(882188.8737096074), sfix(-6186740.260173367), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(6679815.410739994), sfix(-6581552.48316879), sfix(495733.6709170139), sfix(-506019.89772080525), sfix(-22562230.056846548), sfix(-14221914.702314932), sfix(105752232.72219007), sfix(-104178006.42482363), sfix(32081896.612293653)],
        [sfix(5747641.308422519), sfix(5873689.148174064), sfix(-72289640.61066356), sfix(242499451.7331775), sfix(-529629913.4042923), sfix(663120542.7715821), sfix(-460113919.77295125), sfix(166293644.1639788), sfix(-24599058.23043193)],
        [sfix(-150084350.28316426), sfix(853977805.1108348), sfix(-1992876762.4627926), sfix(2516673493.9987597), sfix(-1913993567.1257918), sfix(905603222.1737288), sfix(-261968484.54381952), sfix(42551440.72002848), sfix(-2981066.7300202125)],
        [sfix(-32344881.278792303), sfix(78408430.2193931), sfix(-88207268.70305389), sfix(53570425.1835795), sfix(-20327875.2075765), sfix(4928579.3365994925), sfix(-744466.3383321), sfix(63990.90546195341), sfix(-2395.13248363177)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
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
        sfix(-4.199999809265137),
        sfix(-3.1499998569488525),
        sfix(-2.0999999046325684),
        sfix(-1.0499999523162842),
        sfix(-0.13124999403953552),
        sfix(0.0),
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
        [sfix(853871824.0567256), sfix(1759976906.733056), sfix(1598840052.7117698), sfix(830724857.4815052), sfix(269650371.06361914), sfix(55986141.63292958), sfix(7261678.078344499), sfix(538013.8163230113), sfix(17433.77224172627)],
        [sfix(310137943.7565091), sfix(1545736279.8793323), sfix(2861661738.597958), sfix(2735531130.0487037), sfix(1531716619.7840846), sfix(524981870.68438315), sfix(108877310.03829803), sfix(12590998.58655156), sfix(624972.8947444182)],
        [sfix(-108075223.0749204), sfix(-629985840.4945679), sfix(-1420155994.006485), sfix(-1688821706.6075983), sfix(-1152249728.5891953), sfix(-459671658.72395504), sfix(-103218709.21426287), sfix(-11397741.125367643), sfix(-400991.25308659056)],
        [sfix(4051052.0055096117), sfix(-18672154.29033362), sfix(-24670032.252004296), sfix(9129184.779482365), sfix(-11493239.739296965), sfix(-88841174.57569124), sfix(-89434250.93697992), sfix(-32347514.47259222), sfix(-3408348.495519253)],
        [sfix(4059385.868991558), sfix(-18474421.131444618), sfix(-23120324.21822155), sfix(13314840.976971703), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(4059385.868991558), sfix(-18454264.264108025), sfix(-22909337.491497383), sfix(25952140.904489525), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(4059353.6240193807), sfix(-18460536.460871685), sfix(-22554028.5484902), sfix(20959350.576709088), sfix(22640825.954829138), sfix(-13785582.837974062), sfix(-35981096.14615317), sfix(39477777.215779245), sfix(-11714810.432773795)],
        [sfix(190320.1775852146), sfix(14930930.028522806), sfix(-142917674.8409015), sfix(252627799.70840573), sfix(-224390371.49360406), sfix(110684584.79711238), sfix(-30583934.300648257), sfix(4339972.310737175), sfix(-234330.5023918922)],
        [sfix(-98511955.2985508), sfix(229062213.16892722), sfix(-254585304.37960383), sfix(149738347.8630137), sfix(-55234158.509500876), sfix(13064218.753457626), sfix(-1930725.4391919924), sfix(162756.95088555827), sfix(-5986.22661691656)]
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
        sfix(-4.199999809265137),
        sfix(-2.0999999046325684),
        sfix(-1.0499999523162842),
        sfix(-0.26249998807907104),
        sfix(-0.13124999403953552),
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
        [sfix(-176362106.7187368), sfix(-488636727.6302999), sfix(-582472556.3941386), sfix(-386698068.49999124), sfix(-157037406.98052347), sfix(-40116264.57322497), sfix(-6314667.784816311), sfix(-561174.444158383), sfix(-21589.41101407773)],
        [sfix(-131148762.63372667), sfix(-768050289.0156738), sfix(-1882091504.807795), sfix(-2497504478.4567575), sfix(-1982409693.4791734), sfix(-972338522.7377733), sfix(-289863219.5660818), sfix(-48293697.21395267), sfix(-3458417.894767937)],
        [sfix(3815789.0719644674), sfix(570564.8771940855), sfix(-10132012.023675954), sfix(22093267.289375238), sfix(26881160.712591734), sfix(-41837739.469773084), sfix(-74896651.0939524), sfix(-39589987.083370626), sfix(-7216243.800192539)],
        [sfix(3820404.8428004794), sfix(803351.9291698952), sfix(-5471213.021978836), sfix(73277613.4425471), sfix(370584268.2914596), sfix(1413533845.9450727), sfix(3730478355.511514), sfix(5584247628.754532), sfix(3591525220.4979715)],
        [sfix(3814773.4796594637), sfix(540339.2613948616), sfix(-10915090.949341156), sfix(13371484.601757038), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(3814773.4796594637), sfix(583952.6984715925), sfix(-11052374.402208952), sfix(30115993.17860639), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(4031114.6877233195), sfix(-3160549.567306787), sfix(16889374.092355408), sfix(-87257162.00651935), sfix(295546502.04345787), sfix(-421667214.6973582), sfix(288129965.8643346), sfix(-92855446.0776845), sfix(10909967.867515853)],
        [sfix(143220961.66972956), sfix(-746421399.9017658), sfix(1655504585.3674238), sfix(-1954062016.858955), sfix(1367188766.5719173), sfix(-585700698.1545868), sfix(151076601.9974207), sfix(-21540920.23081576), sfix(1301354.449201678)],
        [sfix(292963245.2263294), sfix(-709029856.1126282), sfix(760648716.0558127), sfix(-458220547.0504086), sfix(172054152.87456524), sfix(-41216127.79187514), sfix(6148530.944093045), sfix(-522059.4299447844), sfix(19312.9552569969)]
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
    "neuron050": neuron050,
    "neuron051": neuron051,
    "neuron052": neuron052,
    "neuron053": neuron053,
    "neuron054": neuron054,
    "neuron055": neuron055,
    "neuron056": neuron056,
    "neuron057": neuron057,
    "neuron058": neuron058,
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

def func9_kan_model_evaluate(x):
    # dim_list required
    input_x = x
    dim_list = [(6, 9), (9, 1)]
    for l in range(len(dim_list)):
        in_dim, out_dim = dim_list[l]
        partial_result = [0]*out_dim
        for i in range(in_dim):
            for j in range(out_dim):
                partial_result[j] += neuron_func_dict[f"neuron{l}{i}{j}"](input_x[i])
        input_x = partial_result
    return input_x

def func9_kan_model_evaluate_vectorized(x):
    dim_list = [(6, 9), (9, 1)]
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