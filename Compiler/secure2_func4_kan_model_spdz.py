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
        sfix(-4.199999809265137),
        sfix(-3.1499998569488525),
        sfix(-2.0999999046325684),
        sfix(-1.0499999523162842),
        sfix(-0.5249999761581421),
        sfix(0.0),
        sfix(0.03281249850988388),
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
        [sfix(-48577744.682396285), sfix(-59861604.09292966), sfix(-30942152.799085587), sfix(-8268800.785746912), sfix(-1161326.010698133), sfix(-75859.07021263942), sfix(-1417.95997951365), sfix(1.0), sfix(1.0)],
        [sfix(-74485521.4930766), sfix(-155156620.51030058), sfix(-132838265.56130801), sfix(-58026849.39699186), sfix(-13468776.107008234), sfix(-1548085.0469653844), sfix(-66199.69609516174), sfix(1.0), sfix(1.0)],
        [sfix(27867.85433840068), sfix(2357821.807685045), sfix(-2143581.9135970045), sfix(-5968478.748745714), sfix(-4283643.236430795), sfix(-1314129.0508879705), sfix(-148544.89388578228), sfix(1.0), sfix(1.0)],
        [sfix(6476.50698200705), sfix(3369569.930820013), sfix(2484303.5082426234), sfix(2239748.796254197), sfix(2974882.6826709337), sfix(1905281.0693092807), sfix(425759.4659082597), sfix(1.0), sfix(1.0)],
        [sfix(-17445.86908066674), sfix(3128653.497163587), sfix(1459921.8675699164), sfix(-100980.52227452458), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(-17445.86908066674), sfix(3129490.5726512084), sfix(1470048.6861009197), sfix(-75575.30346349311), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(-17444.92696262296), sfix(3129431.44830617), sfix(1471295.4242746762), sfix(-86345.34107987398), sfix(41818.21040084538), sfix(-332772.9222211969), sfix(201055.28696857352), sfix(1.0), sfix(1.0)],
        [sfix(-38023.88849504448), sfix(3334829.1682216735), sfix(610589.501045767), sfix(1854634.544228567), sfix(-2445496.4414545326), sfix(1385944.4617192757), sfix(-299372.1893842735), sfix(1.0), sfix(1.0)],
        [sfix(-1502567.059468424), sfix(8975455.851777704), sfix(-7559296.622512594), sfix(6827228.978464469), sfix(-2871929.4417979363), sfix(578467.6494081916), sfix(-44401.792459473), sfix(1.0), sfix(1.0)],
        [sfix(1580636.5008375668), sfix(-2986865.3636285723), sfix(9477973.424264992), sfix(-5151474.028390484), sfix(1595524.8294075332), sfix(-263683.81753323314), sfix(17964.29849642834), sfix(1.0), sfix(1.0)],
        [sfix(2402952.141969223), sfix(-1676565.7989405883), sfix(5441633.357398739), sfix(-1848223.8856161141), sfix(345224.406483984), sfix(-34451.83255820324), sfix(1444.43120885618), sfix(1.0), sfix(1.0)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)]
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
        sfix(0.06562499701976776),
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
        [sfix(-2816040120.8893194), sfix(-4165203009.18935), sfix(-2574304730.142053), sfix(-849288927.904807), sfix(-157637461.63425618), sfix(-15604671.890733091), sfix(-643580.7988323288), sfix(1.0), sfix(1.0)],
        [sfix(9406866242.065996), sfix(16867968793.648518), sfix(12487705437.952356), sfix(4896804728.772157), sfix(1074176316.3865485), sfix(125103002.84536524), sfix(6047829.220595415), sfix(1.0), sfix(1.0)],
        [sfix(-11451897188.226377), sfix(-24391019117.48642), sfix(-21495838842.72912), sfix(-10023706986.388615), sfix(-2608966922.4071374), sfix(-359601755.686029), sfix(-20521128.159852713), sfix(1.0), sfix(1.0)],
        [sfix(5117942481.174187), sfix(13260113309.02357), sfix(14162387358.985504), sfix(7992675358.22666), sfix(2512792121.681879), sfix(417152853.5797448), sfix(28574685.081948575), sfix(1.0), sfix(1.0)],
        [sfix(-742162138.9240563), sfix(-2376644645.660197), sfix(-3160670423.5329676), sfix(-2198341266.3142233), sfix(-841735834.8391162), sfix(-167915266.6523195), sfix(-13597969.800818175), sfix(1.0), sfix(1.0)],
        [sfix(7934127.574534724), sfix(29076296.67309488), sfix(-32314827.931819122), sfix(-115768184.07889289), sfix(-112573342.10239467), sfix(-48155296.1691571), sfix(-7767380.245196969), sfix(1.0), sfix(1.0)],
        [sfix(-115075.37823634833), sfix(23501810.656815525), sfix(43230628.16316889), sfix(85310142.03646083), sfix(101924740.58216155), sfix(59388840.92738745), sfix(13285791.573412618), sfix(1.0), sfix(1.0)],
        [sfix(-991690.5597070479), sfix(14609142.14802844), sfix(5408594.849181944), sfix(-1136007.6969936925), sfix(-10218521.073881026), sfix(-19011727.35067033), sfix(-9821867.445324576), sfix(1.0), sfix(1.0)],
        [sfix(-990420.6457400649), sfix(14642345.720055874), sfix(5788786.21285701), sfix(1450674.2307413102), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(-990405.9930349798), sfix(14644110.650488138), sfix(5784095.818271188), sfix(1245514.9085565733), sfix(-2766195.2000112617), sfix(-1053593.1085845046), sfix(3678681.3808243275), sfix(1.0), sfix(1.0)],
        [sfix(-993763.3242058926), sfix(14712173.657406248), sfix(5195931.559072579), sfix(4034337.4360792427), sfix(-10456172.391938481), sfix(10674220.308625521), sfix(-4052887.8116616737), sfix(1.0), sfix(1.0)],
        [sfix(-586094.5887414202), sfix(10800220.048730496), sfix(20885546.472658217), sfix(-29666345.45941071), sfix(30473704.11090603), sfix(-15999433.12783409), sfix(3239249.0119059137), sfix(1.0), sfix(1.0)],
        [sfix(-8009913.281740283), sfix(53445997.203432806), sfix(-81387962.12979355), sfix(101415226.06324865), sfix(-64229392.79732449), sfix(20570290.783469103), sfix(-2657394.680531706), sfix(1.0), sfix(1.0)],
        [sfix(80808389.93632407), sfix(-279959256.7317881), sfix(442613248.4254896), sfix(-340008361.3636082), sfix(146007019.9297024), sfix(-33106222.114704672), sfix(3082038.201182101), sfix(1.0), sfix(1.0)],
        [sfix(-793041585.5650438), sfix(2151868921.1465626), sfix(-2380395738.2275863), sfix(1409840632.0599313), sfix(-464845223.60174644), sfix(80763602.28164822), sfix(-5773605.561046692), sfix(1.0), sfix(1.0)],
        [sfix(2573089271.8830433), sfix(-5633468406.038673), sfix(5124738333.848415), sfix(-2450216629.268061), sfix(652316644.8973192), sfix(-91744694.52170675), sfix(5330228.309822955), sfix(1.0), sfix(1.0)],
        [sfix(784009179.4524088), sfix(-1076379982.21419), sfix(630625749.0788417), sfix(-189679659.6169921), sfix(31545157.585199628), sfix(-2739121.865257817), sfix(96314.99693059226), sfix(1.0), sfix(1.0)]
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
        sfix(-0.26249998807907104),
        sfix(0.0),
        sfix(0.19687499105930328),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-88711786.01978557), sfix(-123458773.03570177), sfix(-74607684.51303457), sfix(-24342395.86007586), sfix(-4476104.412203106), sfix(-438304.6571051767), sfix(-17836.93417825493), sfix(1.0), sfix(1.0)],
        [sfix(-114653024.7733223), sfix(-279664897.42059755), sfix(-286615179.1679789), sfix(-153029279.2920713), sfix(-44864505.668520436), sfix(-6875095.182761348), sfix(-431876.2476579802), sfix(1.0), sfix(1.0)],
        [sfix(36255889.17264188), sfix(123080511.19350284), sfix(158558944.90352544), sfix(107573735.32808916), sfix(40232515.9015012), sfix(7794387.4881288605), sfix(608443.3751253237), sfix(1.0), sfix(1.0)],
        [sfix(-8381101.152427631), sfix(-35481467.040292345), sfix(-76255053.76365863), sfix(-77975415.20696652), sfix(-42274574.00193948), sfix(-11777897.91676703), sfix(-1326292.3610759475), sfix(1.0), sfix(1.0)],
        [sfix(-886488.2545568331), sfix(3777034.0822181534), sfix(8160062.36147251), sfix(16366552.75575488), sfix(14432230.99880832), sfix(4945897.004390569), sfix(381469.05771699967), sfix(1.0), sfix(1.0)],
        [sfix(-953176.7619213596), sfix(2893859.0630089273), sfix(3514369.393782906), sfix(4344255.268839844), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(-953176.7619213596), sfix(2889984.3593933615), sfix(3662377.525202421), sfix(2942212.719110503), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(-971751.8917729718), sfix(3373179.921234785), sfix(-1610342.7578575744), sfix(33335915.505342904), sfix(-95704771.9112076), sfix(155775002.23457658), sfix(-110047872.4631555), sfix(1.0), sfix(1.0)],
        [sfix(-954716.6973787885), sfix(2923486.4842444947), sfix(3289649.8357699877), sfix(5060449.440906237), sfix(-4424503.187134988), sfix(-703364.6596296511), sfix(1322590.257416311), sfix(1.0), sfix(1.0)],
        [sfix(-1074651.2984601401), sfix(4141185.881961667), sfix(-1921286.6248641713), sfix(17117692.200306684), sfix(-20367575.66788751), sfix(10739532.84711785), sfix(-2164617.9852166246), sfix(1.0), sfix(1.0)],
        [sfix(2987719.8936043684), sfix(-19321031.466966994), sfix(54773684.94251138), sfix(-56268287.37468877), sfix(33307749.36292997), sfix(-10296203.158277113), sfix(1286646.467961601), sfix(1.0), sfix(1.0)],
        [sfix(-19965141.777452685), sfix(70301792.57660075), sfix(-91595924.4856504), sfix(71701760.47635417), sfix(-29855813.42043183), sfix(6389415.552053558), sfix(-556057.6731574077), sfix(1.0), sfix(1.0)],
        [sfix(-9044630.11742353), sfix(12827451.121708838), sfix(3851612.9380009067), sfix(-3691721.2546498366), sfix(1616468.750876132), sfix(-349787.88515775104), sfix(29613.9551898246), sfix(1.0), sfix(1.0)],
        [sfix(-94586552.86660348), sfix(141578284.42913783), sfix(-77714757.98045427), sfix(24955419.249074038), sfix(-4509040.395599098), sfix(433128.6867172328), sfix(-17257.48714243274), sfix(1.0), sfix(1.0)]
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
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-3.1499998569488525),
        sfix(-2.625),
        sfix(-2.0999999046325684),
        sfix(-1.5749999284744263),
        sfix(-1.0499999523162842),
        sfix(-0.06562499701976776),
        sfix(-0.03281249850988388),
        sfix(0.0),
        sfix(0.06562499701976776),
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
        [sfix(81667263.78381875), sfix(90673825.54453816), sfix(34869406.70608141), sfix(3978442.9894218724), sfix(-741711.0157227027), sfix(-227761.76756152464), sfix(-16079.32331610105), sfix(1.0), sfix(1.0)],
        [sfix(1423884670.7115119), sfix(3017656205.301975), sfix(2641333887.7284436), sfix(1223306287.0746214), sfix(316392646.5092641), sfix(43359519.24123918), sfix(2461594.239045658), sfix(1.0), sfix(1.0)],
        [sfix(-669473908.3557988), sfix(-1728031205.4542165), sfix(-1842722537.010752), sfix(-1036970032.5550635), sfix(-324648366.1431699), sfix(-53626910.13838168), sfix(-3653698.550029597), sfix(1.0), sfix(1.0)],
        [sfix(102078376.25384024), sfix(332606465.4053803), sfix(442692817.6429252), sfix(309375009.893598), sfix(119277586.75767398), sfix(23963529.893313453), sfix(1954135.3511646106), sfix(1.0), sfix(1.0)],
        [sfix(-3166018.525025499), sfix(-11626138.242544292), sfix(-17394705.511498038), sfix(-9645221.500293348), sfix(-71535.70785430736), sfix(1732243.1231164816), sfix(442794.92384848057), sfix(1.0), sfix(1.0)],
        [sfix(75308.86353353514), sfix(1395746.8688972907), sfix(1496646.4112887261), sfix(-30894.99056216683), sfix(-2914509.716846858), sfix(-2895986.7180332523), sfix(-838867.7241515752), sfix(1.0), sfix(1.0)],
        [sfix(75711.88434576402), sfix(1408411.0476251158), sfix(1633614.4350648625), sfix(644864.2425633551), sfix(-1195679.6019184233), sfix(-584176.4423716158), sfix(582832.8369603948), sfix(1.0), sfix(1.0)],
        [sfix(75711.88446452546), sfix(1408418.7178042482), sfix(1635096.6657374671), sfix(721499.9869508741), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(75711.88446452546), sfix(1408344.1713066443), sfix(1640045.513270301), sfix(481754.4231315096), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(75704.47611156692), sfix(1408714.1061075337), sfix(1628893.0768646912), sfix(681149.176180609), sfix(-1342724.7896633802), sfix(-262975.6318808737), sfix(389617.37813732424), sfix(1.0), sfix(1.0)],
        [sfix(42771.60903579081), sfix(1696133.6030859626), sfix(587463.5831946317), sfix(2699627.952303167), sfix(-3576861.169361435), sfix(1103192.4074954048), sfix(18964.34696057573), sfix(1.0), sfix(1.0)],
        [sfix(2056516.5609357296), sfix(-6548429.823489775), sfix(13062702.184189789), sfix(-4689791.510480267), sfix(-3983898.313993503), sfix(3326804.2201658622), sfix(-652574.1194700281), sfix(1.0), sfix(1.0)],
        [sfix(-33398447.684334885), sfix(101684093.82905665), sfix(-117389192.8449946), sfix(71544047.50836691), sfix(-24258935.43875475), sfix(4441007.568062805), sfix(-343988.88178789814), sfix(1.0), sfix(1.0)],
        [sfix(291508953.69847244), sfix(-769468200.6041175), sfix(852629643.339566), sfix(-502214110.8145152), sfix(165713475.4596345), sfix(-28906821.19324885), sfix(2077249.4193726978), sfix(1.0), sfix(1.0)],
        [sfix(-1011704692.3220404), sfix(2242120844.9360905), sfix(-2047600424.4262705), sfix(987650020.4558194), sfix(-264884770.57101223), sfix(37481977.07656551), sfix(-2188673.5970232603), sfix(1.0), sfix(1.0)],
        [sfix(-367069141.67841285), sfix(513053749.3279515), sfix(-292982793.6502874), sfix(88942366.73715541), sfix(-14987336.334828226), sfix(1323969.8027634202), sfix(-47641.3711622628), sfix(1.0), sfix(1.0)]
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
        sfix(0.13124999403953552),
        sfix(0.26249998807907104),
        sfix(0.39374998211860657),
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
        [sfix(-809839122.733897), sfix(-1198252718.181221), sfix(-740629964.1686134), sfix(-244336418.77836818), sfix(-45349685.07443444), sfix(-4489017.669408913), sfix(-185133.00262934892), sfix(1.0), sfix(1.0)],
        [sfix(2616319041.182367), sfix(4700980167.303252), sfix(3486132472.6745453), sfix(1368947450.328988), sfix(300651641.5768511), sfix(35050245.413674206), sfix(1695879.6895502575), sfix(1.0), sfix(1.0)],
        [sfix(-3162663978.3144665), sfix(-6734722322.12052), sfix(-5936589174.371264), sfix(-2769510806.244522), sfix(-721242583.3930291), sfix(-99468796.1558018), sfix(-5679561.76632782), sfix(1.0), sfix(1.0)],
        [sfix(1444860696.8642735), sfix(3717105891.4226646), sfix(3944357425.610638), sfix(2213455969.708405), sfix(692515856.8018475), sfix(114488242.37041849), sfix(7813845.092804343), sfix(1.0), sfix(1.0)],
        [sfix(-216021576.1700112), sfix(-672351348.6376578), sfix(-863518365.2498922), sfix(-576750188.5005206), sfix(-210874686.96569464), sfix(-39892843.76694299), sfix(-3031868.3687079214), sfix(1.0), sfix(1.0)],
        [sfix(-2352077.9909119606), sfix(-16767110.617165785), sfix(-66365553.87076252), sfix(-102765541.64292681), sfix(-79018443.6017766), sfix(-29962838.16486137), sfix(-4463232.073169615), sfix(1.0), sfix(1.0)],
        [sfix(-384756.40056573786), sfix(8916924.06343964), sfix(26643220.93125947), sfix(53221813.02048289), sfix(58058429.51703684), sfix(31656318.759079117), sfix(6774174.767967146), sfix(1.0), sfix(1.0)],
        [sfix(-990430.1235059594), sfix(2934644.6692999704), sfix(1880020.5448663775), sfix(-1845271.8448573833), sfix(-11426016.695555713), sfix(-15582848.912746942), sfix(-6762717.528815582), sfix(1.0), sfix(1.0)],
        [sfix(-987934.7326423944), sfix(2994741.980061706), sfix(2541945.763413443), sfix(1990043.7066179102), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(-987934.7326423944), sfix(2987291.911045513), sfix(2451161.220680122), sfix(-114278.20218623818), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(-987943.189468387), sfix(2989213.3754489566), sfix(2371682.3367707306), sfix(893285.5795269986), sfix(-4143416.278146963), sfix(1666135.931514797), sfix(2348861.180306886), sfix(1.0), sfix(1.0)],
        [sfix(-989737.9201501962), sfix(3029360.032252814), sfix(1990630.5567337603), sfix(2861454.6033388525), sfix(-9984594.292045947), sfix(11111246.627269303), sfix(-4145294.0967646744), sfix(1.0), sfix(1.0)],
        [sfix(-990230.7831929172), sfix(3042777.982747863), sfix(1867433.701555369), sfix(3410138.153641601), sfix(-11287802.937062697), sfix(12707385.253647467), sfix(-4941409.152596398), sfix(1.0), sfix(1.0)],
        [sfix(-520501.3343028225), sfix(-1481683.5540760993), sfix(20097723.593254145), sfix(-35973973.75268679), sfix(36892506.26983394), sfix(-18980839.914847896), sfix(3823261.3805669406), sfix(1.0), sfix(1.0)],
        [sfix(-8181804.689010233), sfix(43543779.57364079), sfix(-90086509.1586614), sfix(107806327.29238299), sfix(-68665264.87895472), sfix(22372045.5150762), sfix(-2932063.9158041445), sfix(1.0), sfix(1.0)],
        [sfix(40821463.57142416), sfix(-155597099.86302993), sfix(247100492.76035386), sfix(-196757587.69124523), sfix(86142851.61353098), sfix(-19619063.185811218), sfix(1816962.4285775307), sfix(1.0), sfix(1.0)],
        [sfix(-284576582.7902959), sfix(763817010.7771883), sfix(-837852414.3500216), sfix(487710332.2638755), sfix(-157349951.06349108), sfix(26694237.880486753), sfix(-1862768.9722288193), sfix(1.0), sfix(1.0)],
        [sfix(712784009.060831), sfix(-1522994059.3761547), sfix(1348372282.5770962), sfix(-627759994.6385876), sfix(163015450.7490653), sfix(-22411825.083545055), sfix(1275697.153113613), sfix(1.0), sfix(1.0)],
        [sfix(21411512.58133152), sfix(-11596364.44119463), sfix(-205911.96425008937), sfix(4184485.3827186567), sfix(-1591121.464764757), sfix(242309.3111973034), sfix(-13655.78902582296), sfix(1.0), sfix(1.0)]
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
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-3.1499998569488525),
        sfix(-2.625),
        sfix(-2.0999999046325684),
        sfix(-1.5749999284744263),
        sfix(-1.0499999523162842),
        sfix(-0.26249998807907104),
        sfix(-0.13124999403953552),
        sfix(0.06562499701976776),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-159984282.70566428), sfix(-246204518.57998943), sfix(-159076881.2682437), sfix(-54928507.0660019), sfix(-10671325.826528499), sfix(-1105356.2883162287), sfix(-47683.30167128937), sfix(1.0), sfix(1.0)],
        [sfix(809236855.950054), sfix(1636803223.6327548), sfix(1364167441.612335), sfix(601869623.0151157), sfix(148551240.56513038), sfix(19472549.737267856), sfix(1060074.8029655032), sfix(1.0), sfix(1.0)],
        [sfix(-591344882.1596401), sfix(-1461603876.4791622), sfix(-1488797432.5939205), sfix(-797433404.5780649), sfix(-236941683.84304625), sfix(-37070736.05640187), sfix(-2388771.7752545536), sfix(1.0), sfix(1.0)],
        [sfix(110964608.40329027), sfix(343740529.5900212), sfix(422733546.7157269), sfix(265896629.97426766), sfix(89102476.31055771), sfix(14752797.56455134), sfix(900960.975760323), sfix(1.0), sfix(1.0)],
        [sfix(1315950.4380396227), sfix(23336132.710460298), sfix(64361882.3043507), sfix(87011391.98248725), sfix(62378343.506339096), sfix(22714581.986724697), sfix(3305641.030862647), sfix(1.0), sfix(1.0)],
        [sfix(-453339.3112477129), sfix(3618231.971686023), sfix(-3482486.746241422), sfix(-23380539.35244998), sfix(-32251856.20478651), sfix(-18780306.346422896), sfix(-4055110.0160502936), sfix(1.0), sfix(1.0)],
        [sfix(-382031.0077175735), sfix(4610183.497251937), sfix(2153848.8421257874), sfix(-6464358.726483097), sfix(-3471120.4156858027), sfix(8244945.497627259), sfix(7280497.337648139), sfix(1.0), sfix(1.0)],
        [sfix(-382012.018727486), sfix(4605842.315437706), sfix(2115411.667697831), sfix(-5915654.23610496), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(-382077.40370999824), sfix(4609584.891575197), sfix(2125274.189422298), sfix(-6426429.916504093), sfix(-4924290.9552296065), sfix(10787302.53040308), sfix(-1716260.6981053483), sfix(1.0), sfix(1.0)],
        [sfix(-384454.54714112985), sfix(4661132.490901562), sfix(1648250.6091807578), sfix(-4006900.002522123), sfix(-12033727.23169518), sfix(22265784.56090904), sfix(-9659177.78148696), sfix(1.0), sfix(1.0)],
        [sfix(462020.9504714699), sfix(-3456767.475444071), sfix(34259455.07810916), sfix(-74385060.0034265), sfix(74200153.18440378), sfix(-34733682.635585934), sfix(6250847.586618528), sfix(1.0), sfix(1.0)],
        [sfix(-16380285.144974876), sfix(87125142.86370675), sfix(-169378453.75615162), sfix(170511256.74401614), sfix(-91911170.96797301), sfix(25492820.334638145), sfix(-2862402.3838867135), sfix(1.0), sfix(1.0)],
        [sfix(104445682.35898651), sfix(-339728494.10292214), sfix(458834780.42746735), sfix(-322424076.8399629), sfix(125540531.84598352), sfix(-25626350.6636897), sfix(2138961.961865394), sfix(1.0), sfix(1.0)],
        [sfix(-550669979.7656915), sfix(1427312917.3093653), sfix(-1523504230.7747307), sfix(861052516.4051479), sfix(-270846859.67611253), sfix(44955924.37165877), sfix(-3077582.2719922476), sfix(1.0), sfix(1.0)],
        [sfix(1208651391.2845168), sfix(-2569606690.8494925), sfix(2261331941.878323), sfix(-1051065924.7484782), sfix(272711855.70437735), sfix(-37479136.93540327), sfix(2133098.984359636), sfix(1.0), sfix(1.0)],
        [sfix(87798668.86035594), sfix(-100078946.81419103), sfix(45397143.04383133), sfix(-8317666.177344503), sfix(232611.41001361905), sfix(113745.63695453243), sfix(-10616.81884161835), sfix(1.0), sfix(1.0)]
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
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-3.674999713897705),
        sfix(-3.1499998569488525),
        sfix(-2.625),
        sfix(-2.0999999046325684),
        sfix(-1.8374998569488525),
        sfix(-1.5749999284744263),
        sfix(-1.0499999523162842),
        sfix(-0.5249999761581421),
        sfix(-0.06562499701976776),
        sfix(0.0),
        sfix(0.06562499701976776),
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
        [sfix(1200985880.5281646), sfix(1777397005.35226), sfix(1098640287.9758458), sfix(362440441.99850863), sfix(67268382.8499825), sfix(6658495.66566048), sfix(274598.51966573944), sfix(1.0), sfix(1.0)],
        [sfix(-4053345365.3213573), sfix(-7262490037.201402), sfix(-5373736856.560931), sfix(-2106341564.3277223), sfix(-461895328.14963776), sfix(-53778504.107398264), sfix(-2599141.571434435), sfix(1.0), sfix(1.0)],
        [sfix(5043303225.201872), sfix(10717339815.01841), sfix(9425128327.783081), sfix(4386769725.523797), sfix(1139918679.3817294), sfix(156894360.39549455), sfix(8942188.598285278), sfix(1.0), sfix(1.0)],
        [sfix(-2337945879.8457975), sfix(-6017241137.767033), sfix(-6386823975.604709), sfix(-3582947279.8915796), sfix(-1120044071.163492), sfix(-184948546.65698743), sfix(-12605358.46426047), sfix(1.0), sfix(1.0)],
        [sfix(864117893.9960457), sfix(2719223203.6854362), sfix(3549752812.5511193), sfix(2447569005.2176847), sfix(939748589.6226686), sfix(190482731.1086182), sfix(15922898.598227853), sfix(1.0), sfix(1.0)],
        [sfix(-77253447.39006536), sfix(-370760702.52114797), sfix(-680158176.3802799), sfix(-643391700.9886672), sfix(-331889645.3890175), sfix(-88780532.9018948), sfix(-9652925.708264183), sfix(1.0), sfix(1.0)],
        [sfix(868548.3772889299), sfix(14875324.755338972), sfix(80902193.18710256), sfix(135679974.96778244), sfix(107882569.94032505), sfix(41669083.253950804), sfix(6287202.265110122), sfix(1.0), sfix(1.0)],
        [sfix(-100895.40021577464), sfix(-13169365.865095297), sfix(-35477708.542898335), sfix(-71046978.55730358), sfix(-79670196.70305513), sfix(-44381783.22830413), sfix(-9632932.770765861), sfix(1.0), sfix(1.0)],
        [sfix(696899.9908787919), sfix(-5278722.856720109), sfix(-2873782.326440901), sfix(926233.9380858126), sfix(9661303.602979666), sfix(14489988.454614887), sfix(6350469.897334577), sfix(1.0), sfix(1.0)],
        [sfix(696620.5195474977), sfix(-5290444.956894627), sfix(-3073823.0720281797), sfix(-962401.7854224746), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(696620.5195474977), sfix(-5290078.143553432), sfix(-3074564.6922756364), sfix(-44145.68332755658), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(696620.8661470242), sfix(-5290291.551846276), sfix(-3055630.0080597624), sfix(-524265.79320963606), sfix(3691061.444081417), sfix(-136397.4277207288), sfix(-6085694.710855939), sfix(1.0), sfix(1.0)],
        [sfix(697704.6939864331), sfix(-5321060.356462706), sfix(-2696958.0435962677), sfix(-2743524.059092623), sfix(11488662.136019941), sfix(-15155076.030857924), sfix(6550202.079292346), sfix(1.0), sfix(1.0)],
        [sfix(-1023.53851021807), sfix(1587664.4775660774), sfix(-31262525.640636276), sfix(60488279.33169289), sfix(-67522060.92258397), sfix(37637918.950767905), sfix(-8159947.857220106), sfix(1.0), sfix(1.0)],
        [sfix(-2209120.023947102), sfix(-7738115.588859885), sfix(39088703.54345904), sfix(-85740225.1999903), sfix(75185057.05515036), sfix(-30631401.816724397), sfix(4813148.218690499), sfix(1.0), sfix(1.0)],
        [sfix(374802217.9883028), sfix(-1199330622.4638188), sfix(1555945154.9878566), sfix(-1062127021.4252797), sfix(396979489.0408203), sfix(-76590019.40680268), sfix(5925574.05577775), sfix(1.0), sfix(1.0)],
        [sfix(-2271981175.7520537), sfix(5787752324.22838), sfix(-6088054653.291011), sfix(3368393580.2601533), sfix(-1035543938.9761566), sfix(167846736.48920333), sfix(-11217419.312329272), sfix(1.0), sfix(1.0)],
        [sfix(4114640059.940245), sfix(-8565844002.979236), sfix(7353447463.5262), sfix(-3344677652.3068905), sfix(850196496.8782756), sfix(-114628917.91899016), sfix(6409706.895032782), sfix(1.0), sfix(1.0)],
        [sfix(-291532262.3998773), sfix(508967020.5729477), sfix(-372649454.90188044), sfix(140917386.73679757), sfix(-29646211.918222945), sfix(3297222.2327686795), sfix(-151666.0299714674), sfix(1.0), sfix(1.0)]
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
        sfix(-4.199999809265137),
        sfix(-3.1499998569488525),
        sfix(-2.625),
        sfix(-2.0999999046325684),
        sfix(-1.5749999284744263),
        sfix(-1.0499999523162842),
        sfix(-0.26249998807907104),
        sfix(0.03281249850988388),
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
        [sfix(-197311594.4297243), sfix(-233816999.8741837), sfix(-109576070.89853497), sfix(-24258377.960388537), sfix(-2183317.2924870034), sfix(26108.27923787076), sfix(11611.79178316268), sfix(1.0), sfix(1.0)],
        [sfix(-2078536598.7090092), sfix(-4439599937.195481), sfix(-3923756639.2155623), sfix(-1833658468.9700496), sfix(-478018556.8657759), sfix(-65963025.10824302), sfix(-3767538.121686154), sfix(1.0), sfix(1.0)],
        [sfix(861160164.4616224), sfix(2270232765.996755), sfix(2460562399.2447166), sfix(1407650169.774421), sfix(448068415.0341537), sfix(75220321.5093276), sfix(5204760.0561636), sfix(1.0), sfix(1.0)],
        [sfix(-118477612.95099951), sfix(-398246522.95522016), sfix(-566302222.1133369), sfix(-422106863.0325718), sfix(-173525597.5563134), sfix(-37269313.90431608), sfix(-3265291.172891294), sfix(1.0), sfix(1.0)],
        [sfix(6695861.661080519), sfix(41621303.27232865), sfix(77278718.03281178), sfix(79630199.33587575), sfix(46233941.40685849), sfix(13986285.483950425), sfix(1705774.376008658), sfix(1.0), sfix(1.0)],
        [sfix(-305208.9253267245), sfix(5208470.359117512), sfix(-876803.6565883771), sfix(-8325078.153387167), sfix(-7830982.583646488), sfix(-2841534.529129517), sfix(-268676.3547326621), sfix(1.0), sfix(1.0)],
        [sfix(-262903.0727483541), sfix(5763765.641890623), sfix(1966877.2532383488), sfix(-1347117.1366937025), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(-262955.17855317437), sfix(5763435.599453613), sfix(2008366.4730672413), sfix(-888819.8771709395), sfix(1766447.9174375022), sfix(776080.7390928292), sfix(-1889010.4800674887), sfix(1.0), sfix(1.0)],
        [sfix(-269183.9549639138), sfix(5833992.8429062115), sfix(1739519.068244096), sfix(-666728.2003661141), sfix(2871194.868364485), sfix(-2303332.4786797184), sfix(581445.60900601), sfix(1.0), sfix(1.0)],
        [sfix(859170.8457541564), sfix(883035.6897188869), sfix(10071745.380123306), sfix(-6806215.241965234), sfix(3899955.705942361), sfix(-1285524.8423389143), sfix(164773.8853262578), sfix(1.0), sfix(1.0)],
        [sfix(84689662.92423294), sfix(-194912416.91613853), sfix(194609521.60269502), sfix(-94943219.24435143), sfix(25505135.990131196), sfix(-3587650.2832437414), sfix(206825.23082957856), sfix(1.0), sfix(1.0)],
        [sfix(46300594.265816934), sfix(-58897903.77156019), sfix(40805117.29875108), sfix(-12129127.690759787), sfix(1972958.2479237472), sfix(-166286.76034755868), sfix(5618.80827255893), sfix(1.0), sfix(1.0)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)]
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
        sfix(-4.199999809265137),
        sfix(-3.674999713897705),
        sfix(-3.1499998569488525),
        sfix(-2.625),
        sfix(-2.0999999046325684),
        sfix(-1.8374998569488525),
        sfix(-1.5749999284744263),
        sfix(-1.0499999523162842),
        sfix(-0.5249999761581421),
        sfix(-0.13124999403953552),
        sfix(0.0),
        sfix(0.06562499701976776),
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
        [sfix(855403774.9411348), sfix(1266625256.3158157), sfix(783002273.7290382), sfix(258303919.42916003), sfix(47937797.85609198), sfix(4744774.214962544), sfix(195665.10436923), sfix(1.0), sfix(1.0)],
        [sfix(-2847960837.7595243), sfix(-5106472951.943566), sfix(-3781046851.0637426), sfix(-1482939767.1962965), sfix(-325354966.69209445), sfix(-37897301.79861054), sfix(-1832264.0844329703), sfix(1.0), sfix(1.0)],
        [sfix(3491386626.527116), sfix(7430404883.6265545), sfix(6543184490.592201), sfix(3049103309.9057527), sfix(793188500.1385293), sfix(109279001.11257312), sfix(6233836.323467321), sfix(1.0), sfix(1.0)],
        [sfix(-1590468605.3556888), sfix(-4103616662.241464), sfix(-4367220435.387363), sfix(-2456503796.3090053), sfix(-769921843.3360858), sfix(-127455624.94860838), sfix(-8707950.925414894), sfix(1.0), sfix(1.0)],
        [sfix(559810311.7911638), sfix(1768707788.809401), sfix(2318418377.295974), sfix(1605270956.9747105), sfix(618958164.5518465), sfix(125985718.8496274), sfix(10574189.99545945), sfix(1.0), sfix(1.0)],
        [sfix(-35847397.859174095), sfix(-187887568.7773174), sfix(-361864533.7485852), sfix(-354669156.7167249), sfix(-187919743.9003907), sfix(-51330209.70573124), sfix(-5675601.874713229), sfix(1.0), sfix(1.0)],
        [sfix(-1719133.495081473), sfix(-3744021.0461192518), sfix(21797690.132671613), sfix(52636763.850422494), sfix(48063194.458617695), sfix(20045631.70098404), sfix(3178274.2537293253), sfix(1.0), sfix(1.0)],
        [sfix(343487.59763680585), sfix(-6325645.998336053), sfix(-15963193.646424826), sfix(-32800798.36819329), sfix(-38277629.761198364), sfix(-22091500.274839465), sfix(-4938791.22107736), sfix(1.0), sfix(1.0)],
        [sfix(684208.9240008699), sfix(-2885476.3744145352), sfix(-1410093.7992440367), sfix(248831.6768306535), sfix(4256302.599420274), sfix(7344259.5072540585), sfix(3624082.3244127464), sfix(1.0), sfix(1.0)],
        [sfix(683827.4720219419), sfix(-2896807.5022441517), sfix(-1558133.35363243), sfix(-830345.8537663196), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(683827.4720219419), sfix(-2896385.5625923877), sfix(-1547272.362806128), sfix(-407041.5908773475), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(683829.9458074879), sfix(-2896592.0123817995), sfix(-1537456.9934556733), sfix(-613719.977356148), sfix(1454039.6675129535), sfix(310821.49973419943), sfix(-1643498.2044751507), sfix(1.0), sfix(1.0)],
        [sfix(660946.2052308519), sfix(-2605345.627042659), sfix(-2972570.548684685), sfix(2733906.7586953742), sfix(-1850121.261896657), sfix(186399.2560825809), sfix(226526.08210281795), sfix(1.0), sfix(1.0)],
        [sfix(8131546.2608646685), sfix(-38895838.29215092), sfix(68963782.54711278), sfix(-70714551.46374792), sfix(37780852.73537955), sfix(-9844076.875163825), sfix(958096.6780727578), sfix(1.0), sfix(1.0)],
        [sfix(-122829184.77008814), sfix(401299331.4222035), sfix(-541053686.6695882), sfix(373864181.68605477), sfix(-141017250.16413727), sfix(27476933.22181424), sfix(-2157390.221998963), sfix(1.0), sfix(1.0)],
        [sfix(610136311.0915173), sfix(-1541027823.3300822), sfix(1593803168.5664558), sfix(-870613862.7879283), sfix(264235828.3022575), sfix(-42298581.90669967), sfix(2793446.7547275373), sfix(1.0), sfix(1.0)],
        [sfix(-963559961.2292486), sfix(1982780835.771271), sfix(-1693332020.3040287), sfix(764381331.9058236), sfix(-193062642.29713976), sfix(25889298.86429047), sfix(-1440923.6573121126), sfix(1.0), sfix(1.0)],
        [sfix(56842605.011910714), sfix(-102928702.30231695), sfix(71060887.46123596), sfix(-27249665.716362346), sfix(5806244.835702068), sfix(-652446.4643387735), sfix(30255.69244287263), sfix(1.0), sfix(1.0)]
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
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-3.1499998569488525),
        sfix(-2.625),
        sfix(-2.0999999046325684),
        sfix(-1.5749999284744263),
        sfix(-0.5249999761581421),
        sfix(-0.26249998807907104),
        sfix(-0.06562499701976776),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(310649643.19747746), sfix(516382294.538835), sfix(350948548.2055027), sfix(126277341.74902892), sfix(25458348.39529084), sfix(2729547.8479584125), sfix(121631.13424659373), sfix(1.0), sfix(1.0)],
        [sfix(-2803269857.6260533), sfix(-5758551521.039126), sfix(-4894159445.601445), sfix(-2203239828.4846497), sfix(-554668143.3878114), sfix(-74114813.90714166), sfix(-4109925.206834552), sfix(1.0), sfix(1.0)],
        [sfix(1660022306.3843398), sfix(4282264705.052552), sfix(4519698826.875005), sfix(2504865088.014645), sfix(770014476.7940083), sfix(124688295.41720147), sfix(8322358.40715974), sfix(1.0), sfix(1.0)],
        [sfix(-265887426.75835884), sfix(-916571384.4777784), sfix(-1318879160.7505596), sfix(-985822771.4509232), sfix(-401306119.3416772), sfix(-84374402.23567101), sfix(-7175008.3877573), sfix(1.0), sfix(1.0)],
        [sfix(2333890.3182223355), sfix(8738747.974835249), sfix(3793859.2980264495), sfix(15053839.23175728), sfix(20421063.514072686), sfix(9075550.61341886), sfix(1281990.1757743515), sfix(1.0), sfix(1.0)],
        [sfix(2181661.0206674943), sfix(7328371.941562491), sfix(-1753737.7645338601), sfix(3143103.1949215718), sfix(5646259.258451367), sfix(-988152.4966815383), sfix(-1661414.4637782131), sfix(1.0), sfix(1.0)],
        [sfix(2180345.9038135996), sfix(7303527.448657573), sfix(-1951741.0382076572), sfix(2284327.965468282), sfix(3486944.1063683857), sfix(-4006138.5462182984), sfix(-3511430.309673786), sfix(1.0), sfix(1.0)],
        [sfix(2180347.0681778165), sfix(7303373.9809154915), sfix(-1970897.808629268), sfix(1787078.9670210925), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(2180347.068177816), sfix(7304648.048525445), sfix(-2003510.073040705), sfix(3040113.280526583), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(2180738.301906025), sfix(7292315.9405922135), sfix(-1816481.1134646693), sfix(1443724.3767366067), sfix(6716703.170586662), sfix(-10315655.7820634), sfix(4592275.100193944), sfix(1.0), sfix(1.0)],
        [sfix(1720530.423132167), sfix(11764371.94410988), sfix(-20027919.54511363), sfix(41283921.803424045), sfix(-42733363.823572256), sfix(22741261.231856667), sfix(-4713387.086265453), sfix(1.0), sfix(1.0)],
        [sfix(15435558.317767674), sfix(-63715484.68755777), sfix(154016273.78690898), sfix(-173978891.2710617), sfix(107902780.70053436), sfix(-33808326.90926742), sfix(4183540.573601789), sfix(1.0), sfix(1.0)],
        [sfix(-144873612.98349962), sfix(510975591.7065982), sfix(-706205125.10364), sfix(514334389.30359495), sfix(-202678673.39244762), sfix(41136500.94618308), sfix(-3373602.77046777), sfix(1.0), sfix(1.0)],
        [sfix(606451865.6306566), sfix(-1504523135.2444286), sfix(1541619830.2267296), sfix(-819123401.3178372), sfix(240841122.1323525), sfix(-37231395.98836504), sfix(2368444.4996665777), sfix(1.0), sfix(1.0)],
        [sfix(-610567804.4115196), sfix(1176412296.3490355), sfix(-916466044.476963), sfix(381355185.5342026), sfix(-88453188.14642659), sfix(10858007.503232121), sfix(-551726.0779230313), sfix(1.0), sfix(1.0)],
        [sfix(241135605.0557322), sfix(-354599498.16099125), sfix(229726873.9814057), sfix(-76014423.55243011), sfix(14123674.919956531), sfix(-1398967.587884676), sfix(57732.23480683), sfix(1.0), sfix(1.0)]
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
        sfix(-4.199999809265137),
        sfix(-3.674999713897705),
        sfix(-3.1499998569488525),
        sfix(-2.625),
        sfix(-2.0999999046325684),
        sfix(-1.5749999284744263),
        sfix(-1.0499999523162842),
        sfix(-0.13124999403953552),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-2424267804.570168), sfix(-3584147182.264465), sfix(-2214999653.3376074), sfix(-730770385.8174683), sfix(-135646464.83872294), sfix(-13428502.644846823), sfix(-553856.2352037736), sfix(1.0), sfix(1.0)],
        [sfix(6983105382.91969), sfix(12648006420.86588), sfix(9437564325.072582), sfix(3724574937.315171), sfix(821410977.0571427), sfix(96097891.64307533), sfix(4663599.312812494), sfix(1.0), sfix(1.0)],
        [sfix(-8286813662.887183), sfix(-17633123822.56093), sfix(-15562300128.915926), sfix(-7275296557.873605), sfix(-1899315926.5987391), sfix(-262609807.4516438), sfix(-15032301.725965735), sfix(1.0), sfix(1.0)],
        [sfix(3788862147.708969), sfix(9800112550.777235), sfix(10411706150.223364), sfix(5843694099.110543), sfix(1828702641.8214872), sfix(302509708.74539673), sfix(20667750.52058788), sfix(1.0), sfix(1.0)],
        [sfix(-649601767.6018724), sfix(-2027564327.843982), sfix(-2671411873.530444), sfix(-1839177688.2198079), sfix(-694841018.5328424), sfix(-136495148.17041665), sfix(-10876814.237278868), sfix(1.0), sfix(1.0)],
        [sfix(11767050.976959484), sfix(147958772.7168633), sfix(258747526.67242384), sfix(214848617.3669536), sfix(86420444.14263852), sfix(13148095.531651353), sfix(-112233.09757129032), sfix(1.0), sfix(1.0)],
        [sfix(-17528110.363168824), sfix(15370895.62957723), sfix(19759837.611823745), sfix(2846841.671597366), sfix(-2471144.233723835), sfix(2606434.786562397), sfix(1930468.8652648584), sfix(1.0), sfix(1.0)],
        [sfix(-17529063.99420053), sfix(15348564.698426286), sfix(19619838.218361855), sfix(3019583.9141326565), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(-17529063.99420053), sfix(15343003.627819996), sfix(19654413.77237834), sfix(-409725.1170650423), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(-17528577.151185375), sfix(15331907.219319928), sfix(19676775.82220978), sfix(334330.57376206986), sfix(-2130845.2556929165), sfix(-13140313.164351188), sfix(9033495.097688358), sfix(1.0), sfix(1.0)],
        [sfix(-18361581.4184702), sfix(23745062.911046565), sfix(-16007856.31896797), sfix(81843756.9006374), sfix(-108077661.2210036), sfix(61302662.31166335), sfix(-13096246.766158415), sfix(1.0), sfix(1.0)],
        [sfix(-16602651.84665948), sfix(-13471917.003480168), sfix(132739197.34616502), sfix(-178860495.99345094), sfix(127036271.0936973), sfix(-46285212.76288448), sfix(6792632.606909514), sfix(1.0), sfix(1.0)],
        [sfix(491044819.9372754), sfix(-1631072301.8566895), sfix(2216700710.5918274), sfix(-1546257922.1230724), sfix(593866907.602356), sfix(-118869182.44951102), sfix(9660105.682927184), sfix(1.0), sfix(1.0)],
        [sfix(-3637229257.2843447), sfix(9388324517.432228), sfix(-9996017214.437521), sfix(5641901787.563598), sfix(-1773629643.5286703), sfix(294350092.2782484), sfix(-20152401.759391658), sfix(1.0), sfix(1.0)],
        [sfix(8017118232.39039), sfix(-17082752976.663248), sfix(15063948879.658464), sfix(-7014740170.7040615), sfix(1823059757.9110837), sfix(-250909056.89031306), sfix(14298536.613595026), sfix(1.0), sfix(1.0)],
        [sfix(655048833.8587062), sfix(-767680678.9411641), sfix(362224989.43072164), sfix(-74339005.78996661), sfix(4904037.8893293915), sfix(442473.0721231373), sfix(-58460.24547608732), sfix(1.0), sfix(1.0)]
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
        sfix(-4.199999809265137),
        sfix(-3.674999713897705),
        sfix(-3.1499998569488525),
        sfix(-2.625),
        sfix(-2.0999999046325684),
        sfix(-1.5749999284744263),
        sfix(-1.3125),
        sfix(-0.9187499284744263),
        sfix(-0.7874999642372131),
        sfix(-0.13124999403953552),
        sfix(0.0),
        sfix(0.26249998807907104),
        sfix(0.5249999761581421),
        sfix(1.0499999523162842),
        sfix(1.5749999284744263),
        sfix(2.0999999046325684),
        sfix(2.625),
        sfix(3.1499998569488525),
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
        [sfix(2002529151.1747785), sfix(2951247799.639479), sfix(1822765202.1011004), sfix(601474455.2743572), sfix(111688501.86517492), sfix(11060981.386521619), sfix(456361.0753148968), sfix(1.0), sfix(1.0)],
        [sfix(-6158792265.072261), sfix(-11116356053.806349), sfix(-8266615851.16192), sfix(-3252997103.985431), sfix(-715678969.8736274), sfix(-83560236.7516027), sfix(-4048346.090403423), sfix(1.0), sfix(1.0)],
        [sfix(5152177708.445048), sfix(11497191360.215406), sfix(10545319328.494402), sfix(5083364410.351398), sfix(1360117794.0247557), sfix(191856165.6306149), sfix(11165183.061615113), sfix(1.0), sfix(1.0)],
        [sfix(-792850203.9203154), sfix(-2502263043.612186), sfix(-3190591528.3116384), sfix(-2105015369.0671031), sfix(-756198518.2092189), sfix(-140500597.2228665), sfix(-10587475.728941347), sfix(1.0), sfix(1.0)],
        [sfix(-186144689.8330689), sfix(-484122035.4829281), sfix(-440618074.41866827), sfix(-131915547.23190087), sfix(32304623.089182258), sfix(26254139.41018923), sfix(4015365.4724793937), sfix(1.0), sfix(1.0)],
        [sfix(99236126.19123657), sfix(459919831.4707492), sfix(846644633.1889445), sfix(791412125.6607293), sfix(398129976.90941995), sfix(101653175.04703502), sfix(10261153.293163454), sfix(1.0), sfix(1.0)],
        [sfix(-15648235.46607396), sfix(-54121779.517095834), sfix(-113620723.31506374), sfix(-167316087.0499779), sfix(-141478202.93593788), sfix(-60698804.01111672), sfix(-10140270.347527053), sfix(1.0), sfix(1.0)],
        [sfix(-10853709.703818005), sfix(-24073565.660339236), sfix(-34999184.16361919), sfix(-57373547.67383853), sfix(-54811269.859061964), sfix(-24180106.879790135), sfix(-3713813.6711388216), sfix(1.0), sfix(1.0)],
        [sfix(-9699701.260380512), sfix(-14947350.398234187), sfix(-4626315.6605236875), sfix(-2875101.1047523688), sfix(828823.7348577256), sfix(6475430.320807227), sfix(3406567.526724144), sfix(1.0), sfix(1.0)],
        [sfix(-9700342.142140675), sfix(-14963016.92988712), sfix(-4751732.826503792), sfix(-3209608.290049756), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(-9700342.142140677), sfix(-14971800.360923475), sfix(-4620429.9174489295), sfix(-5107996.636331782), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(-9701329.256289426), sfix(-14951458.120105129), sfix(-4844994.2225913685), sfix(-4089024.810869504), sfix(-700824.0643910796), sfix(-4525849.54461202), sfix(5069352.029125705), sfix(1.0), sfix(1.0)],
        [sfix(-10433517.809563193), sfix(-7659317.694450276), sfix(-35345667.15614119), sfix(64617427.86494668), sfix(-88777603.01612052), sfix(56507357.87330436), sfix(-12820454.728608744), sfix(1.0), sfix(1.0)],
        [sfix(25153644.38166679), sfix(-205155247.6562499), sfix(424432417.5985155), sfix(-510303052.36784536), sfix(318562661.6541919), sfix(-98562643.99855536), sfix(11960532.87548551), sfix(1.0), sfix(1.0)],
        [sfix(-338703393.07215613), sfix(1102196127.2260828), sfix(-1537522504.1043413), sfix(1064160250.121071), sfix(-394203290.061782), sfix(74063022.94714123), sfix(-5517374.114004496), sfix(1.0), sfix(1.0)],
        [sfix(550001711.1700932), sfix(-1183514536.1664019), sfix(887161944.9427843), sfix(-289703455.3145965), sfix(23657088.78243225), sfix(6912746.8543736), sfix(-1174688.4021134975), sfix(1.0), sfix(1.0)],
        [sfix(1500520249.1448555), sfix(-3665441715.2230062), sfix(3549146306.327327), sfix(-1795643749.409423), sfix(498677779.548845), sfix(-72434199.8962088), sfix(4315766.068623422), sfix(1.0), sfix(1.0)],
        [sfix(-2888438057.030229), sfix(5212833626.408619), sfix(-3915660957.7945924), sfix(1544612623.040584), sfix(-340499120.31233066), sfix(39823562.83178501), sfix(-1932287.3649166774), sfix(1.0), sfix(1.0)],
        [sfix(998124738.5785395), sfix(-1494897407.1423657), sfix(900724859.9208398), sfix(-297345453.6619551), sfix(55262315.22747549), sfix(-5477667.531642644), sfix(226174.878693755), sfix(1.0), sfix(1.0)]
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
        sfix(-4.199999809265137),
        sfix(-3.674999713897705),
        sfix(-3.1499998569488525),
        sfix(-2.625),
        sfix(-2.0999999046325684),
        sfix(-1.5749999284744263),
        sfix(-1.3125),
        sfix(-1.0499999523162842),
        sfix(-0.5249999761581421),
        sfix(-0.13124999403953552),
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
        [sfix(2622032104.1439953), sfix(3879459070.074574), sfix(2397844779.6983786), sfix(791059519.5269669), sfix(146824125.4608659), sfix(14533716.344476575), sfix(599392.3241571843), sfix(1.0), sfix(1.0)],
        [sfix(-8140796281.432604), sfix(-14667670257.457163), sfix(-10901186994.59338), sfix(-4288506061.724781), sfix(-943292224.8987795), sfix(-110113152.0217467), sfix(-5333725.2435104055), sfix(1.0), sfix(1.0)],
        [sfix(8064283538.158888), sfix(17576503117.806896), sfix(15803924104.3948), sfix(7496909898.896879), sfix(1980015313.0233448), sfix(276344261.05520004), sfix(15940499.791981174), sfix(1.0), sfix(1.0)],
        [sfix(-2692183055.3495784), sfix(-7165084364.808714), sfix(-7918665468.026597), sfix(-4639438557.187505), sfix(-1514070650.598324), sfix(-260414193.668367), sfix(-18432504.486813243), sfix(1.0), sfix(1.0)],
        [sfix(311618589.2044051), sfix(1075101580.37626), sfix(1499862424.6693003), sfix(1101529516.3288243), sfix(453937432.53201663), sfix(99283248.06559697), sfix(8948644.949619658), sfix(1.0), sfix(1.0)],
        [sfix(-34145734.381421484), sfix(-153540744.57799894), sfix(-321407914.6640641), sfix(-340266514.40688527), sfix(-189055154.45726967), sfix(-53905363.208332), sfix(-6285745.566720381), sfix(1.0), sfix(1.0)],
        [sfix(-20630185.412290595), sfix(-89174038.84556612), sfix(-193613906.98559865), sfix(-204874384.10062423), sfix(-108325382.18433122), sfix(-28218836.968868684), sfix(-2878571.794237481), sfix(1.0), sfix(1.0)],
        [sfix(-5412106.855244544), sfix(-2524154.4626784157), sfix(12849638.935550641), sfix(58672358.51107538), sfix(81773854.98496981), sfix(45252120.65249679), sfix(9008159.116410237), sfix(1.0), sfix(1.0)],
        [sfix(-5930111.256109886), sfix(-7741045.445809842), sfix(-9375258.51265076), sfix(7192424.709179364), sfix(13102255.173887998), sfix(-4956323.914387659), sfix(-6752596.895281073), sfix(1.0), sfix(1.0)],
        [sfix(-5930780.895487124), sfix(-7764171.858815564), sfix(-9812633.001587313), sfix(3116578.080366823), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(-5930780.895487126), sfix(-7748462.5611196235), sfix(-9874258.299317945), sfix(8802302.988461712), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(-5926422.419381734), sfix(-7850715.903520901), sfix(-8743644.090025127), sfix(1897772.016215667), sfix(22423288.51300509), sfix(-33205146.908546582), sfix(13398238.91878692), sfix(1.0), sfix(1.0)],
        [sfix(-7084776.839219239), sfix(3115067.775767654), sfix(-52165498.832959265), sfix(94125790.64630547), sfix(-88620720.44297703), sfix(38801554.05660265), sfix(-6287455.7538608), sfix(1.0), sfix(1.0)],
        [sfix(15388549.645051979), sfix(-110298474.68860684), sfix(185052445.87709132), sfix(-168446787.8035079), sfix(72990424.65783593), sfix(-13338833.437680893), sfix(536794.838462317), sfix(1.0), sfix(1.0)],
        [sfix(-62155113.35242735), sfix(113414543.33034803), sfix(-58876714.368123), sfix(-54563429.74029474), sfix(62497674.807845846), sfix(-21776930.736548126), sfix(2613446.9931102013), sfix(1.0), sfix(1.0)],
        [sfix(-470326645.2067063), sfix(1370315911.0155396), sfix(-1668028653.8142772), sfix(1042233101.8216162), sfix(-357418721.241353), sfix(63868859.470981225), sfix(-4658404.3063233495), sfix(1.0), sfix(1.0)],
        [sfix(2005887551.96509), sfix(-4402061569.94699), sfix(3941855375.389381), sfix(-1867180280.6144226), sfix(491843171.1661839), sfix(-68426880.97680268), sfix(3933986.003227265), sfix(1.0), sfix(1.0)],
        [sfix(113701729.11207251), sfix(-116694466.21316202), sfix(18759098.990844954), sfix(7414958.248631117), sfix(-4014535.638051686), sfix(672657.6997235641), sfix(-39714.63493301544), sfix(1.0), sfix(1.0)]
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
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-3.674999713897705),
        sfix(-3.4124999046325684),
        sfix(-3.1499998569488525),
        sfix(-2.625),
        sfix(-2.0999999046325684),
        sfix(-1.5749999284744263),
        sfix(-1.0499999523162842),
        sfix(-0.26249998807907104),
        sfix(0.0),
        sfix(0.13124999403953552),
        sfix(0.5249999761581421),
        sfix(1.0499999523162842),
        sfix(1.5749999284744263),
        sfix(1.8374998569488525),
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
        [sfix(629944523.0602009), sfix(934368054.3291017), sfix(577796129.0756184), sfix(190591039.8796343), sfix(35364246.58718808), sfix(3499575.571506241), sfix(144290.4501677514), sfix(1.0), sfix(1.0)],
        [sfix(250381476.44902027), sfix(242390978.3890688), sfix(58583298.6956513), sfix(-15139900.679735363), sfix(-10118695.511486461), sfix(-1827060.5279522503), sfix(-114148.03268669626), sfix(1.0), sfix(1.0)],
        [sfix(-2030576089.8399105), sfix(-3745019579.535956), sfix(-2846438886.7944202), sfix(-1144164319.0902498), sfix(-256993641.4113971), sfix(-30624062.759856246), sfix(-1514072.759849365), sfix(1.0), sfix(1.0)],
        [sfix(1079057197.9983027), sfix(2348488586.375172), sfix(2131306998.2438095), sfix(1025580007.8476572), sfix(275251801.8664618), sfix(39040537.9521159), sfix(2286876.7101191855), sfix(1.0), sfix(1.0)],
        [sfix(-247263235.87221333), sfix(-769142071.4803746), sfix(-922212193.8330297), sfix(-569612228.3108552), sfix(-193571757.05890077), sfix(-34459454.24447851), sfix(-2515491.3050938193), sfix(1.0), sfix(1.0)],
        [sfix(-8020728.6183702955), sfix(-22408725.248145293), sfix(45076895.7845567), sfix(96493196.82215622), sfix(63767259.25967724), sfix(18449086.59285787), sfix(2008886.0878734326), sfix(1.0), sfix(1.0)],
        [sfix(16457818.004989875), sfix(20004200.54593179), sfix(32782670.7752944), sfix(19079209.027136993), sfix(-5065611.646479431), sfix(-7230635.252683007), sfix(-1591274.6393849484), sfix(1.0), sfix(1.0)],
        [sfix(10961312.265294917), sfix(-2523844.290357089), sfix(-693978.3927096727), sfix(1528702.0890013487), sfix(226755.14796116904), sfix(1764221.8668320728), sfix(1005722.2111424152), sfix(1.0), sfix(1.0)],
        [sfix(10971509.49072507), sfix(-2405713.4713682984), sfix(-201772.14904761384), sfix(2297014.4138146695), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(10971509.49072507), sfix(-2407222.044588158), sfix(-189995.3003480718), sfix(1690286.9167015431), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(10971949.07266455), sfix(-2419302.66969014), sfix(-69836.28619206886), sfix(1090237.01969714), sfix(2701195.299887262), sfix(-10220316.780266937), sfix(5723241.9743469395), sfix(1.0), sfix(1.0)],
        [sfix(10394810.871354029), sfix(3263515.9399901135), sfix(-23539143.781103916), sfix(53207675.79973786), sfix(-63035130.43169364), sfix(34494732.300028704), sfix(-7106590.846046615), sfix(1.0), sfix(1.0)],
        [sfix(19337467.652079016), sfix(-53841177.713339865), sfix(126094275.47713082), sfix(-153658543.20853293), sfix(96606726.90243128), sfix(-30859923.337800156), sfix(4000974.773999639), sfix(1.0), sfix(1.0)],
        [sfix(-27959880.934532188), sfix(156615918.66918615), sfix(-259444435.784691), sfix(219513867.20373657), sfix(-105062745.08084513), sfix(26916275.839699436), sfix(-2861632.3278274913), sfix(1.0), sfix(1.0)],
        [sfix(259911269.27454606), sfix(-788573679.9765855), sfix(1034772162.5872003), sfix(-726439458.9838243), sfix(284186518.8225193), sfix(-58581266.87478144), sfix(4969648.666664934), sfix(1.0), sfix(1.0)],
        [sfix(-370742331.9879589), sfix(969874259.5129275), sfix(-1008696940.5844133), sfix(540394885.912351), sfix(-157701052.2808821), sfix(23647403.155627582), sfix(-1407804.9456385418), sfix(1.0), sfix(1.0)],
        [sfix(1290597268.6153007), sfix(-2737529894.399295), sfix(2410203599.712701), sfix(-1124088295.2660077), sfix(292300802.8799211), sfix(-40165431.51361725), sfix(2279072.534961911), sfix(1.0), sfix(1.0)],
        [sfix(465152545.72184783), sfix(-646727690.2656091), sfix(370012354.31141955), sfix(-111779420.42305808), sfix(18714675.370590344), sfix(-1639392.1518531586), sfix(58324.58897332419), sfix(1.0), sfix(1.0)]
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
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-3.937499761581421),
        sfix(-3.674999713897705),
        sfix(-3.4124999046325684),
        sfix(-3.1499998569488525),
        sfix(-2.8874998092651367),
        sfix(-2.625),
        sfix(-2.362499952316284),
        sfix(-2.0999999046325684),
        sfix(-1.8374998569488525),
        sfix(-1.0499999523162842),
        sfix(-0.26249998807907104),
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
        [sfix(104816044.08608729), sfix(152511159.90379623), sfix(92505685.66361201), sfix(29929314.111677334), sfix(5447064.9797457345), sfix(528720.2755749631), sfix(21383.16529917944), sfix(1.0), sfix(1.0)],
        [sfix(667523469.8422551), sfix(1012973722.511344), sfix(640876224.8606172), sfix(216360439.6026268), sfix(41107615.86229403), sfix(4167522.8520465447), sfix(176129.0250809069), sfix(1.0), sfix(1.0)],
        [sfix(-228784134.28207248), sfix(-478024174.9355383), sfix(-392526786.2533426), sfix(-165624610.98668623), sfix(-38312757.418939754), sfix(-4638984.102090722), sfix(-230738.1813446194), sfix(1.0), sfix(1.0)],
        [sfix(-1973737912.2057648), sfix(-3519519045.317171), sfix(-2601775543.049914), sfix(-1021610933.5808369), sfix(-224898223.714839), sfix(-26333704.577132195), sfix(-1281939.3715515675), sfix(1.0), sfix(1.0)],
        [sfix(611908960.0955226), sfix(1454439180.2047312), sfix(1386239050.9631522), sfix(684239733.3922342), sfix(185661828.39064726), sfix(26381738.883768406), sfix(1539121.062553421), sfix(1.0), sfix(1.0)],
        [sfix(1564808097.5223422), sfix(3349558091.6296797), sfix(2954212478.5826726), sfix(1374949826.3007128), sfix(356487898.72021604), sfix(48867159.278393716), sfix(2769456.7016643016), sfix(1.0), sfix(1.0)],
        [sfix(-567673325.3732845), sfix(-1523867911.678066), sfix(-1688563332.2590446), sfix(-985122650.955636), sfix(-318663163.5902027), sfix(-54190542.53259006), sfix(-3788270.6362573397), sfix(1.0), sfix(1.0)],
        [sfix(-411411825.02195585), sfix(-1081098844.1861076), sfix(-1171105690.1733382), sfix(-665260846.0941242), sfix(-208211110.90536964), sfix(-33967008.69097091), sfix(-2253036.709211367), sfix(1.0), sfix(1.0)],
        [sfix(104833996.32451463), sfix(370295719.9311308), sfix(530151271.70051366), sfix(398949198.61766464), sfix(166493425.40875039), sfix(36443583.818452366), sfix(3263561.2211597837), sfix(1.0), sfix(1.0)],
        [sfix(-1893340.3547786097), sfix(-4029300.0805328866), sfix(-18079881.354681317), sfix(-30211402.027895648), sfix(-22879162.368623145), sfix(-8213991.937027997), sfix(-1132827.5656002427), sfix(1.0), sfix(1.0)],
        [sfix(-1623110.823359188), sfix(1216917.4200770329), sfix(1882095.1946201085), sfix(3211875.052782484), sfix(5934206.250804583), sfix(4387070.484818817), sfix(1092024.7025763365), sfix(1.0), sfix(1.0)],
        [sfix(-1636479.576010147), sfix(1027886.9369486312), sfix(763146.2238011971), sfix(-321772.7471362477), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(-1636479.576010147), sfix(1029307.2365657049), sfix(825573.0405497248), sfix(-31669.44485026268), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(-1660014.3272700186), sfix(1341066.346922396), sfix(-820678.4413219561), sfix(4282635.174781025), sfix(-5360547.308488318), sfix(2093511.1928402374), sfix(-179401.93926142986), sfix(1.0), sfix(1.0)],
        [sfix(-404816.0692196416), sfix(-5574298.3605687795), sfix(14590803.424136097), sfix(-13181343.638489129), sfix(4884154.1136159375), sfix(-604495.3447466854), sfix(-13419.91039574515), sfix(1.0), sfix(1.0)],
        [sfix(-85657591.85435605), sfix(230605251.5273013), sfix(-250290604.9803878), sfix(139960167.2400751), sfix(-42754606.41360898), sfix(6799213.588588388), sfix(-441705.24855905614), sfix(1.0), sfix(1.0)],
        [sfix(-93581735.08743918), sfix(140763832.2209579), sfix(-88360251.82034263), sfix(29544026.671061777), sfix(-5556002.221941824), sfix(557213.7158454282), sfix(-23282.87011198972), sfix(1.0), sfix(1.0)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)]
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
        sfix(-0.13124999403953552),
        sfix(0.13124999403953552),
        sfix(0.5249999761581421),
        sfix(1.0499999523162842),
        sfix(1.5749999284744263),
        sfix(2.0999999046325684),
        sfix(2.625),
        sfix(3.1499998569488525),
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
        [sfix(-1160341532.4295888), sfix(-1733771045.673184), sfix(-1073615108.7745059), sfix(-353991542.4937216), sfix(-65626167.94688838), sfix(-6488496.8594156625), sfix(-267318.58378561446), sfix(1.0), sfix(1.0)],
        [sfix(3533720228.387609), sfix(6358508170.821014), sfix(4730956339.741741), sfix(1863790152.8717475), sfix(410470216.7774016), sfix(47964565.7950139), sfix(2325266.939460017), sfix(1.0), sfix(1.0)],
        [sfix(-3367117110.877241), sfix(-7389986946.369946), sfix(-6669164876.864499), sfix(-3172769466.9052935), sfix(-840089967.7859249), sfix(-117514638.6168771), sfix(-6792342.909899694), sfix(1.0), sfix(1.0)],
        [sfix(979315676.2607526), sfix(2631784002.370973), sfix(2962721490.900158), sfix(1766361144.4767263), sfix(585163658.4004011), sfix(101926646.23946285), sfix(7291604.35170331), sfix(1.0), sfix(1.0)],
        [sfix(-98498855.3381334), sfix(-310962627.517976), sfix(-382625040.3272213), sfix(-260122024.539596), sfix(-104589117.59966038), sfix(-23117746.228656214), sfix(-2138624.3632322303), sfix(1.0), sfix(1.0)],
        [sfix(5755383.117947705), sfix(36286536.99911343), sfix(92678941.43203816), sfix(80376088.35280487), sfix(28999491.856658656), sfix(3735324.4797292645), sfix(-32492.76537488326), sfix(1.0), sfix(1.0)],
        [sfix(-4745335.655190225), sfix(-16907236.875025813), sfix(-19217051.365194067), sfix(-44530106.951923884), sfix(-48847457.71400453), sfix(-21855539.47170865), sfix(-3479739.3785546185), sfix(1.0), sfix(1.0)],
        [sfix(-4298659.680755901), sfix(-12655696.648297641), sfix(-2276742.366552171), sfix(-8294640.33821741), sfix(-4878261.929285275), sfix(6896551.10390159), sfix(4449763.218071431), sfix(1.0), sfix(1.0)],
        [sfix(-4291043.4871261), sfix(-12545640.565954827), sfix(-1612216.3098138238), sfix(-6149000.402058035), sfix(-972511.0664539421), sfix(10694649.347038671), sfix(5989880.718345868), sfix(1.0), sfix(1.0)],
        [sfix(-4290950.618387701), sfix(-12547191.002692189), sfix(-1660894.523052352), sfix(-6090473.853144976), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(-4291586.898324682), sfix(-12531497.195509348), sfix(-1807422.2437251308), sfix(-5110305.298321581), sfix(-5986330.544122739), sfix(18108761.377613362), sfix(-8677387.353256091), sfix(1.0), sfix(1.0)],
        [sfix(-3502461.654169495), sfix(-20122677.27689831), sfix(28797325.16805121), sfix(-71426106.90194471), sfix(75624496.09462753), sfix(-36070662.965465836), sfix(6504402.753560009), sfix(1.0), sfix(1.0)],
        [sfix(-22795191.560550734), sfix(82513303.74187045), sfix(-199491024.03914532), sfix(200309526.37051225), sfix(-106911741.26512997), sfix(29520338.797518577), sfix(-3340981.473640018), sfix(1.0), sfix(1.0)],
        [sfix(225837631.74718627), sfix(-789170639.8198973), sfix(1072261620.3635488), sfix(-787691438.3931109), sfix(323974840.76188266), sfix(-70446873.58039325), sfix(6291161.588266403), sfix(1.0), sfix(1.0)],
        [sfix(-1880669835.7584767), sfix(4967587659.236978), sfix(-5480583347.827432), sfix(3188570858.740943), sfix(-1032382567.4838834), sfix(176117042.60013264), sfix(-12365956.408400754), sfix(1.0), sfix(1.0)],
        [sfix(5249622709.88728), sfix(-11379262936.645826), sfix(10142186572.10592), sfix(-4778368327.993078), sfix(1254059918.591169), sfix(-174023341.49631763), sfix(9986669.887564577), sfix(1.0), sfix(1.0)],
        [sfix(-4902981210.986688), sfix(8753968583.357492), sfix(-6480801798.391613), sfix(2536655106.1825023), sfix(-555587372.5744832), sfix(64621813.20990982), sfix(-3120557.6847281056), sfix(1.0), sfix(1.0)],
        [sfix(1403059039.782576), sfix(-2089821058.8961465), sfix(1279578712.536375), sfix(-422194034.72906697), sfix(78382419.29410037), sfix(-7761005.162526821), sfix(320153.02125170967), sfix(1.0), sfix(1.0)]
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
        sfix(-4.199999809265137),
        sfix(-3.1499998569488525),
        sfix(-2.4937500953674316),
        sfix(-2.362499952316284),
        sfix(-2.0999999046325684),
        sfix(-1.5749999284744263),
        sfix(-1.0499999523162842),
        sfix(-0.13124999403953552),
        sfix(0.0),
        sfix(0.26249998807907104),
        sfix(0.5249999761581421),
        sfix(1.0499999523162842),
        sfix(1.5749999284744263),
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
        [sfix(830408908.1874201), sfix(1329883489.6277828), sfix(881346406.5083758), sfix(310642219.70532995), sfix(61489170.794987656), sfix(6483070.695617958), sfix(284463.52041676926), sfix(1.0), sfix(1.0)],
        [sfix(-3288446810.150222), sfix(-6999011387.592356), sfix(-6095247059.204516), sfix(-2790781177.370456), sfix(-710815714.893933), sfix(-95720494.9621376), sfix(-5333760.246202964), sfix(1.0), sfix(1.0)],
        [sfix(1953211041.3276756), sfix(5024160822.802614), sfix(5401128617.232301), sfix(3074878991.662725), sfix(973498499.0065598), sfix(162367558.0409749), sfix(11153673.071488757), sfix(1.0), sfix(1.0)],
        [sfix(835182190.7764657), sfix(2107602904.9435039), sfix(2230490653.668575), sfix(1236275011.4226983), sfix(373685193.5735353), sfix(57990841.04491395), sfix(3584683.1057191207), sfix(1.0), sfix(1.0)],
        [sfix(-196507957.6967823), sfix(-703754220.5088674), sfix(-950643386.9851621), sfix(-675704586.9632745), sfix(-269603837.0831545), sfix(-56772816.206803314), sfix(-4886214.542615935), sfix(1.0), sfix(1.0)],
        [sfix(25779859.33490129), sfix(35620953.69660581), sfix(60077894.16002781), sfix(47533380.546095036), sfix(13911237.827149909), sfix(204320.78303469392), sfix(-412716.3682985527), sfix(1.0), sfix(1.0)],
        [sfix(18151628.597480047), sfix(1738438.5354660435), sfix(611903.1254130843), sfix(-3001028.9931856366), sfix(-5405094.819481442), sfix(-1040336.481078511), sfix(336139.90869025927), sfix(1.0), sfix(1.0)],
        [sfix(18152994.176851247), sfix(1770476.791144644), sfix(945922.9413561749), sfix(-1021220.897188153), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(18152994.176851247), sfix(1770914.3132066764), sfix(866212.9382807188), sfix(-1846010.6011440014), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(18151954.726887945), sfix(1794221.4576563386), sfix(634141.2219730046), sfix(-263804.63726723625), sfix(-6797105.616806794), sfix(13398185.66510668), sfix(-6517033.51313219), sfix(1.0), sfix(1.0)],
        [sfix(18787368.872534752), sfix(-4375414.239768895), sfix(25756916.299204316), sfix(-55286597.69084169), sfix(61704177.624008626), sfix(-32658855.619655997), sfix(6573182.787660098), sfix(1.0), sfix(1.0)],
        [sfix(2466180.535751421), sfix(86109734.6357606), sfix(-184323431.38219258), sfix(206186051.45469165), sfix(-122303893.05235831), sfix(36760308.2483055), sfix(-4394205.402115992), sfix(1.0), sfix(1.0)],
        [sfix(162749831.7841495), sfix(-472192093.9329113), sfix(630734504.4737372), sfix(-432585050.3788147), sfix(161306936.90281308), sfix(-30912919.764819983), sfix(2388244.754716263), sfix(1.0), sfix(1.0)],
        [sfix(-1099366806.1201262), sfix(2533268579.6337423), sfix(-2350962557.789245), sfix(1145064350.954566), sfix(-308277380.38629055), sfix(43642885.71228717), sfix(-2544990.2518030666), sfix(1.0), sfix(1.0)],
        [sfix(-87708962.32232231), sfix(89878387.44007415), sfix(-16537108.048850616), sfix(-4876887.245717694), sfix(2912014.9698758814), sfix(-497623.1647479272), sfix(29625.5169703722), sfix(1.0), sfix(1.0)]
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
        sfix(-1.3125),
        sfix(-1.0499999523162842),
        sfix(-0.5249999761581421),
        sfix(-0.26249998807907104),
        sfix(0.0),
        sfix(0.26249998807907104),
        sfix(1.0499999523162842),
        sfix(1.5749999284744263),
        sfix(2.0999999046325684),
        sfix(2.625),
        sfix(3.1499998569488525),
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
        [sfix(1209651324.0755496), sfix(1791274272.1760976), sfix(1107344073.5867999), sfix(365300516.33796877), sfix(67794682.61712144), sfix(6710135.845733434), sfix(276711.80841513537), sfix(1.0), sfix(1.0)],
        [sfix(-3155687094.12521), sfix(-5756486209.256928), sfix(-4321051881.836472), sfix(-1713753276.993038), sfix(-379498135.3059928), sfix(-44550630.41798441), sfix(-2168332.504631745), sfix(1.0), sfix(1.0)],
        [sfix(2810721741.257004), sfix(6171603881.280541), sfix(5600416955.9472), sfix(2681825277.160307), sfix(714666770.7457747), sfix(100564175.0779644), sfix(5843741.919154647), sfix(1.0), sfix(1.0)],
        [sfix(-1020290329.4450557), sfix(-2606178950.4759064), sfix(-2781001117.4621425), sfix(-1587144964.8327324), sfix(-508615620.2319329), sfix(-86420203.61794288), sfix(-6067290.389842698), sfix(1.0), sfix(1.0)],
        [sfix(123708778.82483923), sfix(394736554.7632527), sfix(475508847.8051939), sfix(280695876.1626718), sfix(87131416.27385321), sfix(13412993.594669387), sfix(764418.8276668012), sfix(1.0), sfix(1.0)],
        [sfix(-73154747.18000887), sfix(-252102425.32778025), sfix(-398709077.5258346), sfix(-338933317.8726614), sfix(-154338759.43961254), sfix(-35172470.09707883), sfix(-3112189.385193642), sfix(1.0), sfix(1.0)],
        [sfix(3149063.748128674), sfix(84778827.99727331), sfix(221581684.17515087), sfix(270791351.91346306), sfix(183133410.31238064), sfix(64552913.30703349), sfix(9180535.49280061), sfix(1.0), sfix(1.0)],
        [sfix(-13331605.00787338), sfix(-12215214.307935918), sfix(-17369290.917483233), sfix(-44627988.76433465), sfix(-52154352.32005373), sfix(-29481944.474251516), sfix(-6548303.873829336), sfix(1.0), sfix(1.0)],
        [sfix(-12890445.913105559), sfix(-7758628.100306117), sfix(1517449.2638322297), sfix(-1584747.847262496), sfix(3567751.6253529345), sfix(9427061.79285685), sfix(4916477.872007377), sfix(1.0), sfix(1.0)],
        [sfix(-12890674.602574062), sfix(-7763333.4266361855), sfix(1488407.7539018188), sfix(-2015619.53563204), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(-12890674.602574062), sfix(-7762261.739343887), sfix(1272238.5160462353), sfix(-1720974.4104144222), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(-12946092.039210266), sfix(-7021434.122121431), sfix(-2631940.8071284113), sfix(8695994.573126731), sfix(-15700419.60445074), sfix(13970923.870501379), sfix(-4018264.755077701), sfix(1.0), sfix(1.0)],
        [sfix(-4045466.5924963183), sfix(-64913047.28488224), sfix(151190535.72184387), sfix(-206168229.46202207), sfix(151285894.6804717), sfix(-54649024.1558835), sfix(7648030.3090300765), sfix(1.0), sfix(1.0)],
        [sfix(-214508064.04658967), sfix(744373975.2221657), sfix(-1151825062.7637877), sfix(918221035.1917105), sfix(-397112521.70986056), sfix(88672594.13686498), sfix(-8029624.700929968), sfix(1.0), sfix(1.0)],
        [sfix(1475280216.8005881), sfix(-3954402432.3812447), sfix(4300072269.649942), sfix(-2460524748.7669125), sfix(782543649.3802347), sfix(-131338956.26901443), sfix(9095580.176657429), sfix(1.0), sfix(1.0)],
        [sfix(-3481535977.591288), sfix(7407387211.476189), sfix(-6556773363.047614), sfix(3075343695.9387593), sfix(-806071463.1073049), sfix(111926323.17910478), sfix(-6434053.211036111), sfix(1.0), sfix(1.0)],
        [sfix(3005064837.404134), sfix(-5507192801.484454), sfix(4144681666.370822), sfix(-1649352384.6226249), sfix(366256734.90397066), sfix(-43094799.77917744), sfix(2101455.81821769), sfix(1.0), sfix(1.0)],
        [sfix(-1226859690.8923855), sfix(1818378690.3689144), sfix(-1129377201.934315), sfix(372469257.3598611), sfix(-69086828.34476209), sfix(6834183.6271871505), sfix(-281688.27279332274), sfix(1.0), sfix(1.0)]
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
        sfix(-50.0),
        sfix(-18.75),
        sfix(-12.5),
        sfix(-6.25),
        sfix(-3.125),
        sfix(-2.34375),
        sfix(-1.5625),
        sfix(-0.78125),
        sfix(-0.09765625),
        sfix(0.048828125),
        sfix(0.1953125),
        sfix(0.390625),
        sfix(0.78125),
        sfix(1.171875),
        sfix(1.5625),
        sfix(1.953125),
        sfix(2.34375),
        sfix(3.125),
        sfix(3.90625),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-188.83124938671), sfix(-33.52859267372), sfix(-2.42910565207), sfix(-0.0920001157), sfix(-0.00192341339), sfix(-2.107304e-05), sfix(-9.465e-08), sfix(1.0), sfix(1.0)],
        [sfix(-353219.717143139), sfix(-124453.09747026271), sfix(-18340.04905767295), sfix(-1445.6174463255), sfix(-64.23371099347), sfix(-1.52451764051), sfix(-0.01509117172), sfix(1.0), sfix(1.0)],
        [sfix(-4339865.773935507), sfix(-2256760.314340816), sfix(-498930.55666686577), sfix(-59761.8253140856), sfix(-4074.77904177486), sfix(-149.47643258245), sfix(-2.29873443103), sfix(1.0), sfix(1.0)],
        [sfix(-899362.5944085381), sfix(1850862.135098417), sfix(1504568.590084816), sfix(455244.06301799853), sfix(69836.61526908119), sfix(5479.92390628447), sfix(175.71790998551), sfix(1.0), sfix(1.0)],
        [sfix(-28082891.49083652), sfix(-43076017.081788726), sfix(-27930934.502383277), sfix(-9020737.229098855), sfix(-1387374.8869134774), sfix(-66100.98664516729), sfix(3071.45081829016), sfix(1.0), sfix(1.0)],
        [sfix(2322950.2343840846), sfix(-19178883.920135826), sfix(-63635090.52350235), sfix(-66596592.83745518), sfix(-32646061.182795547), sfix(-7769215.306655798), sfix(-727464.3286367627), sfix(1.0), sfix(1.0)],
        [sfix(11310719.104434727), sfix(77622560.21561056), sfix(184237194.7781032), sfix(219320135.0302045), sfix(138246429.18762356), sfix(44139208.09593921), sfix(5637989.739694602), sfix(1.0), sfix(1.0)],
        [sfix(-370780.28913428454), sfix(6329301.230750551), sfix(5874992.6580720255), sfix(-12188996.381732587), sfix(-22362377.545872703), sfix(-9233031.755053218), sfix(154549.35648937544), sfix(1.0), sfix(1.0)],
        [sfix(-367567.3712192902), sfix(6413365.717800892), sfix(6748799.981930692), sfix(-6510536.45590518), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(-367606.25086602115), sfix(6416334.720881566), sfix(6775926.113434291), sfix(-7501336.909912454), sfix(-10294362.278272368), sfix(11011263.011958981), sfix(2940031.982543868), sfix(1.0), sfix(1.0)],
        [sfix(-368987.0374151247), sfix(6452574.297180276), sfix(6374011.042860113), sfix(-5076613.582700972), sfix(-18738138.022277668), sfix(27195450.759300668), sfix(-10454051.536881382), sfix(1.0), sfix(1.0)],
        [sfix(-206016.30996828683), sfix(4512845.572503511), sfix(15889202.733949615), sfix(-29628482.182859648), sfix(16225077.027803482), sfix(1390723.02404155), sfix(-2887996.223649614), sfix(1.0), sfix(1.0)],
        [sfix(-2471636.07547572), sfix(16869292.06420209), sfix(-8169751.14143687), sfix(-14339439.57838381), sfix(26120025.861227904), sfix(-16406867.438462062), sfix(3708225.911716871), sfix(1.0), sfix(1.0)],
        [sfix(-1121749.0217950875), sfix(27780242.205726616), sfix(-69378355.87714942), sfix(98718209.66007388), sfix(-74420840.4552591), sfix(27747667.53869888), sfix(-4012963.9578756373), sfix(1.0), sfix(1.0)],
        [sfix(50585078.89837432), sfix(-207201289.23572874), sfix(365839650.3322317), sfix(-324289186.4870446), sfix(154029027.11239165), sfix(-37430944.03693646), sfix(3677351.2370438897), sfix(1.0), sfix(1.0)],
        [sfix(-110156525.19262707), sfix(344953758.3803368), sfix(-416726275.19280374), sfix(262606769.73804158), sfix(-91972916.59683056), sfix(17272702.505737234), sfix(-1368868.4974109565), sfix(1.0), sfix(1.0)],
        [sfix(-981636643.1653103), sfix(2219671875.510992), sfix(-2059056327.8897083), sfix(1005409191.0394466), sfix(-271836297.96283364), sfix(38633948.59177717), sfix(-2258458.440198256), sfix(1.0), sfix(1.0)],
        [sfix(565539503.1872286), sfix(-1122491451.1315327), sfix(895833750.5825392), sfix(-368671423.02823424), sfix(83600311.02165866), sfix(-9954429.2248552), sfix(487890.5438788729), sfix(1.0), sfix(1.0)],
        [sfix(-2251415.801951386), sfix(5095671.163402922), sfix(641219.0657938705), sfix(-220525.13317837924), sfix(34220.26271136664), sfix(-2619.49715179787), sfix(80.70807898635), sfix(1.0), sfix(1.0)],
        [sfix(-4339865.774047253), sfix(7522920.687333589), sfix(-498930.5566864809), sfix(59761.82531685235), sfix(-4074.77904199136), sfix(149.47643259137), sfix(-2.29873443118), sfix(1.0), sfix(1.0)],
        [sfix(-12487.94033357449), sfix(5268750.57786265), sfix(-214.53687892429), sfix(9.11438611942), sfix(-0.21030274864), sfix(0.00250845978), sfix(-1.212671e-05), sfix(1.0), sfix(1.0)]
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
        sfix(-1.5625),
        sfix(-0.78125),
        sfix(-0.09765625),
        sfix(0.0),
        sfix(0.01220703125),
        sfix(0.78125),
        sfix(1.5625),
        sfix(2.34375),
        sfix(3.125),
        sfix(4.6875),
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
        [sfix(11450.23860465191), sfix(2272.24054110073), sfix(181.32491944776), sfix(7.46667430206), sfix(0.1678231835), sfix(0.00195787979), sfix(9.28808e-06), sfix(1.0), sfix(1.0)],
        [sfix(2369692.310123727), sfix(948762.1252957826), sfix(159834.23909912125), sfix(14484.11181471963), sfix(743.83767456031), sfix(20.50705464932), sfix(0.23692626336), sfix(1.0), sfix(1.0)],
        [sfix(4695966.114904667), sfix(2074452.250982001), sfix(387008.46354633494), sfix(38957.05933836224), sfix(2228.12674991648), sfix(68.56059242688), sfix(0.8856947856), sfix(1.0), sfix(1.0)],
        [sfix(8186134.375766931), sfix(4002658.387242238), sfix(831404.4962031686), sfix(93646.16071319843), sfix(6018.32651237933), sfix(208.81678863452), sfix(3.05071148737), sfix(1.0), sfix(1.0)],
        [sfix(11950733.451038454), sfix(6418147.242664194), sfix(1478229.4280533656), sfix(186173.8999983511), sfix(13475.59890207294), sfix(529.8723524825), sfix(8.81908321501), sfix(1.0), sfix(1.0)],
        [sfix(13217283.065914486), sfix(7341181.245315503), sfix(1758090.6931548042), sfix(231347.96434098305), sfix(17568.58534398576), sfix(727.16230013374), sfix(12.76976244112), sfix(1.0), sfix(1.0)],
        [sfix(8258271.2309488375), sfix(2379825.474835118), sfix(-315911.7981328427), sfix(-232262.84113113655), sfix(-40866.73357888062), sfix(-3209.85792123165), sfix(-97.97834121244), sfix(1.0), sfix(1.0)],
        [sfix(-7387198.904779261), sfix(-18983281.8358726), sfix(-12537678.84112498), sfix(-3979563.17423246), sfix(-689880.9682442776), sfix(-63374.26068366179), sfix(-2428.76712759385), sfix(1.0), sfix(1.0)],
        [sfix(-30827876.321616687), sfix(-80983714.06926936), sfix(-75842022.21841094), sfix(-36918719.66068073), sfix(-10046660.268149097), sfix(-1451548.2096804285), sfix(-86936.05164169398), sfix(1.0), sfix(1.0)],
        [sfix(20228755.572427392), sfix(63041658.31816638), sfix(91819860.82336736), sfix(66389856.51645617), sfix(25543927.543323334), sfix(5056020.0943411365), sfix(406894.5153407759), sfix(1.0), sfix(1.0)],
        [sfix(-1096605.376375255), sfix(-13111471.451126859), sfix(-21593080.09735245), sfix(-23713375.18537878), sfix(-14694144.999202024), sfix(-4508757.091866908), sfix(-536948.2720091721), sfix(1.0), sfix(1.0)],
        [sfix(49205.68392839873), sfix(-6093217.410219561), sfix(-3879990.3522242187), sfix(-295471.4038295298), sfix(2178556.2474201485), sfix(1591972.0648831066), sfix(265648.7768449414), sfix(1.0), sfix(1.0)],
        [sfix(48972.46891618662), sfix(-6099820.77229105), sfix(-3960195.1263319827), sfix(-872583.1140754613), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(48972.46891618661), sfix(-6099616.404776497), sfix(-3947131.2036737218), sfix(-611235.8550625957), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(48978.25368113561), sfix(-6100251.160191977), sfix(-3932367.1531858933), sfix(-761572.433224404), sfix(1682086.792721871), sfix(-701396.9956488658), sfix(63062.09537831884), sfix(1.0), sfix(1.0)],
        [sfix(-213826.34070505117), sfix(-4490592.296564722), sfix(-7990273.293558679), sfix(4564866.971196989), sfix(-2056536.2292239044), sfix(541605.7111662354), sfix(-55034.52024268248), sfix(1.0), sfix(1.0)],
        [sfix(10959609.975487787), sfix(-42626899.44536641), sfix(45893717.89843912), sfix(-35675745.40934704), sfix(14633718.585417861), sfix(-3083051.8212264264), sfix(264041.5314603136), sfix(1.0), sfix(1.0)],
        [sfix(56842954.66639009), sfix(-125209952.97488368), sfix(98285422.59662956), sfix(-45914376.400114805), sfix(11849978.666113213), sfix(-1602065.252372764), sfix(88800.91464204344), sfix(1.0), sfix(1.0)],
        [sfix(22714199.49087065), sfix(-38138403.895687066), sfix(13740906.552478649), sfix(-4454564.348702321), sfix(830478.4232932532), sfix(-82570.58199443082), sfix(3399.66280192791), sfix(1.0), sfix(1.0)],
        [sfix(8258271.214125172), sfix(-15898425.911940005), sfix(-315911.80683462886), sfix(232262.84327965215), sfix(-40866.73387672078), sfix(3209.85794321107), sfix(-97.97834188701), sfix(1.0), sfix(1.0)],
        [sfix(11140737.705943692), sfix(-19311861.36234598), sfix(1280789.4886532035), sfix(-153412.76789542098), sfix(10460.24160210293), sfix(-383.71641323877), sfix(5.90101138776), sfix(1.0), sfix(1.0)],
        [sfix(32057.41260281503), sfix(-13525249.692359067), sfix(550.73111036917), sfix(-23.39726397154), sfix(0.53986180301), sfix(-0.00643939095), sfix(3.113011e-05), sfix(1.0), sfix(1.0)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)]
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
        sfix(-50.0),
        sfix(-14.0625),
        sfix(-12.5),
        sfix(-10.9375),
        sfix(-9.375),
        sfix(-7.8125),
        sfix(-6.25),
        sfix(-4.6875),
        sfix(-3.90625),
        sfix(-3.125),
        sfix(-2.734375),
        sfix(-2.34375),
        sfix(-1.953125),
        sfix(-1.5625),
        sfix(-0.78125),
        sfix(-0.1953125),
        sfix(-0.09765625),
        sfix(0.0),
        sfix(0.0244140625),
        sfix(0.1953125),
        sfix(0.78125),
        sfix(1.5625),
        sfix(2.34375),
        sfix(3.125),
        sfix(4.6875),
        sfix(6.25),
        sfix(12.5)
    ]
    coeffA = [
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(12586.7217645907), sfix(2497.76973743049), sfix(199.32216164898), sfix(8.20777236107), sfix(0.18448032301), sfix(0.00215220739), sfix(1.020996e-05), sfix(1.0), sfix(1.0)],
        [sfix(2604893.9943656093), sfix(1042930.6588484587), sfix(175698.44310372625), sfix(15921.71933830338), sfix(817.66661560664), sfix(22.54246396042), sfix(0.26044216706), sfix(1.0), sfix(1.0)],
        [sfix(5162060.018542704), sfix(2280350.148006874), sfix(425420.64138087514), sfix(42823.70731159582), sfix(2449.27747145125), sfix(75.36551251699), sfix(0.97360362691), sfix(1.0), sfix(1.0)],
        [sfix(8998641.798830958), sfix(4399938.654371193), sfix(913924.8035542761), sfix(102940.92637710932), sfix(6615.67011081559), sfix(229.54271164273), sfix(3.35350711898), sfix(1.0), sfix(1.0)],
        [sfix(13136892.777924154), sfix(7055174.689086763), sfix(1624949.7637160404), sfix(204652.42341350944), sfix(14813.10738122062), sfix(582.46435744321), sfix(9.6944134073), sfix(1.0), sfix(1.0)],
        [sfix(14529152.638498971), sfix(8069823.60353834), sfix(1932588.4075963215), sfix(254310.19898247515), sfix(19312.33952018394), sfix(799.33614183753), sfix(14.03721375536), sfix(1.0), sfix(1.0)],
        [sfix(9077938.53305848), sfix(2616032.917377088), sfix(-347267.34016858623), sfix(-255315.88103392965), sfix(-44922.9245538959), sfix(-3528.44948927341), sfix(-107.70309356193), sfix(1.0), sfix(1.0)],
        [sfix(4170455.1281578178), sfix(-3201674.8172385325), sfix(-3212354.845362248), sfix(-1005070.8965325305), sfix(-154781.37262558035), sfix(-12064.61942422049), sfix(-382.08635463627), sfix(1.0), sfix(1.0)],
        [sfix(-226524555.81002247), sfix(-416594297.77050436), sfix(-307988264.4443118), sfix(-119635430.41140582), sfix(-25913908.29410371), sfix(-2974598.0062755668), sfix(-141520.21580798036), sfix(1.0), sfix(1.0)],
        [sfix(541643993.960411), sfix(1151061354.6119435), sfix(1018357664.007829), sfix(476330946.8342054), sfix(124173021.84602746), sfix(17121953.608225185), sfix(976720.6202990072), sfix(1.0), sfix(1.0)],
        [sfix(-194897560.77477992), sfix(-519465897.18825495), sfix(-560056171.8040944), sfix(-318953401.7972701), sfix(-101195836.34786703), sfix(-16936276.718966417), sfix(-1167682.3671187293), sfix(1.0), sfix(1.0)],
        [sfix(61271979.679689474), sfix(187879649.9665964), sfix(250273169.13813868), sfix(174336425.2754431), sfix(67188609.83898936), sfix(13635670.083777143), sfix(1139653.408992348), sfix(1.0), sfix(1.0)],
        [sfix(-13057096.206881974), sfix(-75716655.60726604), sfix(-132761925.97812967), sfix(-118736177.8481032), sfix(-57684322.21766477), sfix(-14513275.983822817), sfix(-1486961.6016234404), sfix(1.0), sfix(1.0)],
        [sfix(3910535.142018256), sfix(15700037.067974754), sfix(57447490.39340396), sfix(83056577.59939969), sfix(59253457.9126647), sfix(20898782.003846675), sfix(2915742.102110993), sfix(1.0), sfix(1.0)],
        [sfix(277280.5991584373), sfix(-7404791.170133187), sfix(-3605288.3127451697), sfix(-2614451.137568004), sfix(-7872368.468072357), sfix(-6791548.262250124), sfix(-1735153.8972795832), sfix(1.0), sfix(1.0)],
        [sfix(281137.7583787111), sfix(-7332062.300242468), sfix(-3042805.758253938), sfix(-304315.3355145017), sfix(-2465860.1472783023), sfix(198915.78037005867), sfix(2261319.4967335444), sfix(1.0), sfix(1.0)],
        [sfix(281139.1944781483), sfix(-7331572.600106674), sfix(-3014196.7992110895), sfix(179431.2699746597), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(281139.1944781483), sfix(-7331997.127952818), sfix(-3039665.7679695874), sfix(-401513.062842304), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(281139.1332776584), sfix(-7331984.115153911), sfix(-3041589.0300447186), sfix(-281904.08368355513), sfix(-2418266.7279300704), sfix(929667.1278417669), sfix(1871747.5775792329), sfix(1.0), sfix(1.0)],
        [sfix(280580.89244698366), sfix(-7317325.014027756), sfix(-3198422.1471017404), sfix(605329.3317436671), sfix(-5264262.977860765), sfix(5931695.387249374), sfix(-1960862.9134005648), sfix(1.0), sfix(1.0)],
        [sfix(-179993.07638556077), sfix(-5226935.278535173), sfix(-5818244.823242554), sfix(-1209329.1518221842), sfix(2148409.7898693644), sfix(-712154.2831469487), sfix(79590.51413627721), sfix(1.0), sfix(1.0)],
        [sfix(-14756486.519655757), sfix(43700337.60462172), sfix(-73899442.27645166), sfix(49040080.195538476), sfix(-18595453.374493215), sfix(3829486.1778922807), sfix(-332661.5614724407), sfix(1.0), sfix(1.0)],
        [sfix(-299471769.7960016), sfix(664511393.9286803), sfix(-626319483.363103), sfix(303619267.38548803), sfix(-81735920.09739028), sfix(11592038.69219608), sfix(-677230.5707001574), sfix(1.0), sfix(1.0)],
        [sfix(-207564044.07108173), sfix(296098643.3878089), sfix(-189319949.40142113), sfix(60936199.14029193), sfix(-10993635.391399395), sfix(1055874.517965278), sfix(-42198.55227913108), sfix(1.0), sfix(1.0)],
        [sfix(9077938.511188315), sfix(-17476409.90891074), sfix(-347267.3512562527), sfix(255315.88374318555), sfix(-44922.92492549763), sfix(3528.44951640097), sfix(-107.70309438541), sfix(1.0), sfix(1.0)],
        [sfix(12246501.631702008), sfix(-21228642.835820366), sfix(1407913.1002428848), sfix(-168639.61453260272), sfix(11498.46349747422), sfix(-421.8018415665), sfix(6.48671097869), sfix(1.0), sfix(1.0)],
        [sfix(35239.24232104775), sfix(-14867686.216176474), sfix(605.39343243166), sfix(-25.71953840609), sfix(0.59344530167), sfix(-0.00707852692), sfix(3.421991e-05), sfix(1.0), sfix(1.0)]
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
        sfix(-50.0),
        sfix(-25.0),
        sfix(-12.5),
        sfix(-4.6875),
        sfix(-3.90625),
        sfix(-3.125),
        sfix(-2.5390625),
        sfix(-2.34375),
        sfix(-2.1484375),
        sfix(-1.953125),
        sfix(-1.5625),
        sfix(-1.171875),
        sfix(-1.07421875),
        sfix(-0.390625),
        sfix(-0.09765625),
        sfix(0.0),
        sfix(0.09765625),
        sfix(0.29296875),
        sfix(0.390625),
        sfix(0.5859375),
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
        [sfix(-6.17538630631), sfix(-0.97730876026), sfix(-0.06379662566), sfix(-0.00219924228), sfix(-4.223923e-05), sfix(-4.2871e-07), sfix(-1.8e-09), sfix(1.0), sfix(1.0)],
        [sfix(-287692.8529000921), sfix(-87888.97291724168), sfix(-11130.60502064254), sfix(-747.58389305449), sfix(-28.07571875185), sfix(-0.55888634524), sfix(-0.00460676503), sfix(1.0), sfix(1.0)],
        [sfix(-11179896.80042939), sfix(-6002002.87677584), sfix(-1374570.1569160647), sfix(-170958.42612670487), sfix(-12119.78457936639), sfix(-462.46691297386), sfix(-7.39582189392), sfix(1.0), sfix(1.0)],
        [sfix(17718001.52267476), sfix(31795627.696544115), sfix(19381446.456888597), sfix(5947053.289220482), sfix(1007683.8404705669), sfix(90594.9524107284), sfix(3392.19228634244), sfix(1.0), sfix(1.0)],
        [sfix(-908202288.590403), sfix(-1771905658.5783472), sfix(-1394397267.7779927), sfix(-570717740.4574434), sfix(-128912043.50115502), sfix(-15302653.960220935), sfix(-748123.8863483417), sfix(1.0), sfix(1.0)],
        [sfix(2584879781.4984646), sfix(5611708393.633575), sfix(5041001143.384195), sfix(2395714685.647549), sfix(634997795.3946898), sfix(89023170.41871095), sfix(5160416.1563557405), sfix(1.0), sfix(1.0)],
        [sfix(-930386628.1756163), sfix(-2479281025.3941994), sfix(-2723403494.3058414), sfix(-1580722370.7445867), sfix(-511278284.02900016), sfix(-87326745.11878148), sfix(-6151790.869265265), sfix(1.0), sfix(1.0)],
        [sfix(-794722007.9756851), sfix(-2107189090.30435), sfix(-2299899625.7227154), sfix(-1324559421.7375693), sfix(-424395754.39919865), sfix(-71654376.12872724), sfix(-4976778.554060356), sfix(1.0), sfix(1.0)],
        [sfix(-119526681.45452943), sfix(-226750685.26042292), sfix(-116794714.990779), sfix(27784019.705259383), sfix(47038368.531302325), sfix(16036332.489984976), sfix(1822694.4285069706), sfix(1.0), sfix(1.0)],
        [sfix(200871798.41487488), sfix(760293848.9152025), sfix(1151504603.4469535), sfix(897867797.9020072), sfix(383149671.5233318), sfix(85357790.75467908), sfix(7786278.280528142), sfix(1.0), sfix(1.0)],
        [sfix(-4155962.633921292), sfix(-50655486.30957993), sfix(-188081004.5036458), sfix(-284957762.9583584), sfix(-205601158.75533196), sfix(-71259097.96208484), sfix(-9607264.67341216), sfix(1.0), sfix(1.0)],
        [sfix(-25499560.744684894), sfix(-145801351.07107526), sfix(-363474225.4808002), sfix(-455826261.2070111), sfix(-298184625.64547926), sfix(-97634851.74882053), sfix(-12680357.237117345), sfix(1.0), sfix(1.0)],
        [sfix(-802452.5616912006), sfix(2339099.638811239), sfix(8954734.302197916), sfix(46486028.19118927), sfix(85123023.30527905), sfix(59238459.432747886), sfix(14212014.835283956), sfix(1.0), sfix(1.0)],
        [sfix(-932277.3668140928), sfix(556783.0102948525), sfix(-1369329.1538309618), sfix(13957039.449166263), sfix(25883313.04372792), sfix(-266271.0209772558), sfix(-11642803.032708414), sfix(1.0), sfix(1.0)],
        [sfix(-932620.647788496), sfix(540397.0406907301), sfix(-1801448.0898270311), sfix(8362376.408858249), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(-932620.647788496), sfix(547043.5770524044), sfix(-1743165.6253496406), sfix(15894088.911463419), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(-932438.3650696448), sfix(536613.9468606274), sfix(-1425096.5282779527), sfix(11307299.872625098), sfix(26034872.952750497), sfix(-33309300.224201772), sfix(3067762.0162857138), sfix(1.0), sfix(1.0)],
        [sfix(-923337.5902651001), sfix(343804.08866634563), sfix(305322.4164465757), sfix(2882232.683343655), sfix(49500182.25707107), sfix(-68723554.11278312), sfix(25659054.25486985), sfix(1.0), sfix(1.0)],
        [sfix(-939782.5382335632), sfix(538036.3818105593), sfix(-602318.1482049745), sfix(4949183.18780988), sfix(47321342.25673437), sfix(-68157407.06333211), sfix(26066928.84302194), sfix(1.0), sfix(1.0)],
        [sfix(-4209865.1791303195), sfix(29646796.23574578), sfix(-109424327.76903735), sfix(223974913.77805653), sfix(-203337144.78335047), sfix(86677023.95264655), sfix(-14300541.450680532), sfix(1.0), sfix(1.0)],
        [sfix(37706256.59122697), sfix(-182970686.12807053), sfix(342687033.31302273), sfix(-291954027.36644816), sfix(129920365.18392801), sfix(-28848627.910273388), sfix(2488478.2687652837), sfix(1.0), sfix(1.0)],
        [sfix(-103249825.59157787), sfix(277463319.8524472), sfix(-276839775.4358765), sfix(145936295.70130572), sfix(-40593301.50231535), sfix(5519893.790376977), sfix(-268244.44448507065), sfix(1.0), sfix(1.0)],
        [sfix(63271206.0848915), sfix(-113973662.56222421), sfix(99039749.7325533), sfix(-41306598.03887831), sfix(9768513.635192016), sfix(-1243577.4378829417), sfix(66510.6951092194), sfix(1.0), sfix(1.0)],
        [sfix(-1682582.419562172), sfix(7420577.687803124), sfix(3766926.7817900386), sfix(-1132615.1887778935), sfix(173777.3349543237), sfix(-13667.95228422508), sfix(439.66419243636), sfix(1.0), sfix(1.0)],
        [sfix(-10086121.682886155), sfix(17483741.989618905), sfix(-1159546.0707909288), sfix(138890.2499572504), sfix(-9470.04340417138), sfix(347.39265367625), sfix(-5.34240375088), sfix(1.0), sfix(1.0)],
        [sfix(-29022.7606875399), sfix(12244908.53213623), sfix(-498.59723295608), sfix(21.18240799435), sfix(-0.48875684721), sfix(0.00582981867), sfix(-2.818324e-05), sfix(1.0), sfix(1.0)]
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
        sfix(-50.0),
        sfix(-25.0),
        sfix(-12.5),
        sfix(-6.25),
        sfix(-3.125),
        sfix(-2.34375),
        sfix(-1.5625),
        sfix(-0.9765625),
        sfix(-0.87890625),
        sfix(-0.78125),
        sfix(-0.68359375),
        sfix(-0.09765625),
        sfix(0.0),
        sfix(0.09765625),
        sfix(0.390625),
        sfix(0.5859375),
        sfix(1.171875),
        sfix(1.953125),
        sfix(2.34375),
        sfix(3.125),
        sfix(4.6875),
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
        [sfix(-9.27018209973), sfix(-1.46708719518), sfix(-0.09576831438), sfix(-0.00330139289), sfix(-6.340742e-05), sfix(-6.4355e-07), sfix(-2.7e-09), sfix(1.0), sfix(1.0)],
        [sfix(-431870.170203132), sfix(-131934.54515857864), sfix(-16708.70943185384), sfix(-1122.2356755824), sfix(-42.14586950531), sfix(-0.83897232278), sfix(-0.00691544603), sfix(1.0), sfix(1.0)],
        [sfix(-15140783.108944124), sfix(-7873312.270052379), sfix(-1740652.7617252548), sfix(-208495.1199895384), sfix(-14215.95710607365), sfix(-521.48853524961), sfix(-8.01975020846), sfix(1.0), sfix(1.0)],
        [sfix(-3696567.020812306), sfix(5747284.166919233), sfix(4877286.11502683), sfix(1485452.0761918246), sfix(227816.64512484643), sfix(17830.71463582189), sfix(569.79440103017), sfix(1.0), sfix(1.0)],
        [sfix(60563606.328977376), sfix(158987322.27521843), sfix(153224671.7065107), sfix(76625335.49143617), sfix(21325101.395152777), sfix(3140844.723192935), sfix(191410.34464248907), sfix(1.0), sfix(1.0)],
        [sfix(-46022216.98350899), sfix(-253684226.58702415), sfix(-445840784.0499585), sfix(-361031726.08902913), sfix(-152100434.7759935), sfix(-32615701.69275657), sfix(-2826319.383401533), sfix(1.0), sfix(1.0)],
        [sfix(-17943399.631125227), sfix(15152419.97618891), sfix(233740890.07374206), sfix(427456146.3328261), sfix(325704081.5448543), sfix(115247527.51530895), sfix(15716450.37680784), sfix(1.0), sfix(1.0)],
        [sfix(-4723713.05782844), sfix(79569587.56771259), sfix(361837156.9450253), sfix(559495575.7127032), sfix(399142800.1670368), sfix(135624489.52320898), sfix(17795326.553364776), sfix(1.0), sfix(1.0)],
        [sfix(-9276044.33913091), sfix(48436297.16909765), sfix(273056043.6856854), sfix(424372414.0972652), sfix(283378346.26385313), sfix(82690900.08919327), sfix(7703124.000128126), sfix(1.0), sfix(1.0)],
        [sfix(-12924277.968281409), sfix(20441319.475653097), sfix(183464301.15819097), sfix(271314015.2159842), sfix(136156716.53077725), sfix(7096980.287973303), sfix(-8484809.661510045), sfix(1.0), sfix(1.0)],
        [sfix(-16264534.312173469), sfix(-10179791.149198921), sfix(66147583.40238444), sfix(31145252.58796023), sfix(-140564900.89104614), sfix(-162797295.84079048), sfix(-51837864.33998021), sfix(1.0), sfix(1.0)],
        [sfix(-16255788.469875539), sfix(-9905478.930658689), sfix(70019159.76248793), sfix(63640013.16769432), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(-16255788.469875539), sfix(-9931908.90441226), sfix(70195025.4377733), sfix(33844018.99241878), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(-16256447.103285875), sfix(-9893212.4103567), sfix(68893961.18806414), sfix(52619591.14248878), sfix(-88770530.66919202), sfix(-17657015.484302744), sfix(36822975.79095852), sfix(1.0), sfix(1.0)],
        [sfix(-16387145.97651619), sfix(-7952377.196086401), sfix(56649538.691998675), sfix(94757763.40305924), sfix(-172392344.73132807), sfix(73161889.1590382), sfix(-5325401.799218358), sfix(1.0), sfix(1.0)],
        [sfix(-17691310.143169437), sfix(4277566.322684417), sfix(8357102.627649817), sfix(197644683.61266634), sfix(-297227976.1702974), sfix(154990130.6471048), sfix(-27966967.55690323), sfix(1.0), sfix(1.0)],
        [sfix(210709512.7336376), sfix(-1042357227.999924), sfix(2017372192.9314399), sfix(-1872276450.7942085), sfix(911512354.2768472), sfix(-224762616.17435846), sfix(22236004.708844382), sfix(1.0), sfix(1.0)],
        [sfix(-1328120995.7122643), sfix(3772609942.8769026), sfix(-4273903238.257598), sfix(2521170744.5872545), sfix(-817831598.527196), sfix(138987483.4708969), sfix(-9702740.68231961), sfix(1.0), sfix(1.0)],
        [sfix(1893118484.8271046), sfix(-3862066643.935737), sfix(3265125326.911058), sfix(-1448995312.7254825), sfix(358126581.232585), sfix(-46764778.59049404), sfix(2521241.9326071762), sfix(1.0), sfix(1.0)],
        [sfix(130187366.91374467), sfix(-176123303.41557997), sfix(115536640.94013329), sfix(-36021095.17838388), sfix(6279306.757258822), sfix(-582335.6153437675), sfix(22472.34265665636), sfix(1.0), sfix(1.0)],
        [sfix(-16782703.79457489), sfix(27382317.233631916), sfix(-2063436.2016134711), sfix(256634.26756725743), sfix(-18193.61647776314), sfix(694.23227724724), sfix(-11.10223916885), sfix(1.0), sfix(1.0)],
        [sfix(-43567.52166000541), sfix(18381446.318836365), sfix(-748.46931279016), sfix(31.79797501276), sfix(-0.73369741623), sfix(0.0087514332), sfix(-4.230728e-05), sfix(1.0), sfix(1.0)]
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
        sfix(-50.0),
        sfix(-12.5),
        sfix(-10.9375),
        sfix(-9.375),
        sfix(-7.8125),
        sfix(-6.25),
        sfix(-4.6875),
        sfix(-3.90625),
        sfix(-3.125),
        sfix(-2.734375),
        sfix(-2.34375),
        sfix(-1.953125),
        sfix(-1.5625),
        sfix(-1.171875),
        sfix(-0.78125),
        sfix(-0.390625),
        sfix(-0.09765625),
        sfix(0.0),
        sfix(0.048828125),
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
        [sfix(3731.87301484425), sfix(774.05205914974), sfix(64.11180449194), sfix(2.72372630704), sfix(0.06284648482), sfix(0.00074962348), sfix(3.62392e-06), sfix(1.0), sfix(1.0)],
        [sfix(546667.6128522649), sfix(241491.491265086), sfix(45052.49564053668), sfix(4535.07587385546), sfix(259.38107339306), sfix(7.98128744551), sfix(0.1031056533), sfix(1.0), sfix(1.0)],
        [sfix(952965.6790979749), sfix(465958.15474072733), sfix(96785.60282045336), sfix(10901.55292379286), sfix(700.60645826398), sfix(24.30881581619), sfix(0.35513994895), sfix(1.0), sfix(1.0)],
        [sfix(1391210.8323958088), sfix(747150.4577109204), sfix(172083.89773806726), sfix(21672.90798092716), sfix(1568.72373085566), sfix(61.68359118631), sfix(1.02664862797), sfix(1.0), sfix(1.0)],
        [sfix(1538652.6233991857), sfix(854602.8503446437), sfix(204663.15533226592), sfix(26931.71890732274), sfix(2045.19717054791), sfix(84.65054241069), sfix(1.48655577564), sfix(1.0), sfix(1.0)],
        [sfix(961363.2870653945), sfix(277040.6513879926), sfix(-36775.97842953122), sfix(-27038.22170071364), sfix(-4757.38519908535), sfix(-373.66653090034), sfix(-11.40587146305), sfix(1.0), sfix(1.0)],
        [sfix(218756.83606954844), sfix(-646323.3361970563), sfix(-516546.2934868689), sfix(-160382.924693224), sfix(-25666.76066012614), sfix(-2127.60238266115), sfix(-72.89283433664), sfix(1.0), sfix(1.0)],
        [sfix(2637897.615145025), sfix(3033771.341635109), sfix(1814754.065832009), sfix(626749.6156839896), sfix(123711.41501684645), sfix(12978.1956046795), sfix(562.95647450906), sfix(1.0), sfix(1.0)],
        [sfix(-33490809.851561755), sfix(-65887648.78044631), sfix(-53016542.646718495), sfix(-22658560.70544196), sfix(-5443460.89412514), sfix(-697512.061977084), sfix(-37249.71851049442), sfix(1.0), sfix(1.0)],
        [sfix(39558845.056727044), sfix(96523852.82882364), sfix(97557047.02027315), sfix(51852065.156732924), sfix(15312474.79311229), sfix(2388448.5413113604), sfix(154063.53682740266), sfix(1.0), sfix(1.0)],
        [sfix(106963.16925812209), sfix(-8664111.920708345), sfix(-19261035.12840387), sfix(-17320567.031496752), sfix(-7722305.270654188), sfix(-1701844.2482819317), sfix(-148524.45888923074), sfix(1.0), sfix(1.0)],
        [sfix(3691958.915174503), sfix(5684734.128678393), sfix(3382826.646024107), sfix(1071245.6874701194), sfix(475127.8319632723), sfix(211837.42315685985), sfix(35079.23458036646), sfix(1.0), sfix(1.0)],
        [sfix(-4803084.384888703), sfix(-28962313.478614513), sfix(-55448405.40115808), sfix(-52175020.684248276), sfix(-26620962.546348263), sfix(-7140006.344193996), sfix(-795912.0122754956), sfix(1.0), sfix(1.0)],
        [sfix(-17044.71828204219), sfix(-2597326.384546804), sfix(5077418.9090503985), sfix(21961279.683390003), sfix(24488043.904571243), sfix(11664706.223694956), sfix(2089165.7982380174), sfix(1.0), sfix(1.0)],
        [sfix(197288.4931228002), sfix(-1987388.5418429186), sfix(3766175.6441866616), sfix(14138252.885030687), sfix(11496202.958485024), sfix(2089758.1339457375), sfix(-614086.9725279001), sfix(1.0), sfix(1.0)],
        [sfix(146064.5078708152), sfix(-2612122.482128919), sfix(600793.7847391285), sfix(5606992.31779634), sfix(-1400779.479012631), sfix(-8265709.729990411), sfix(-4053059.339052664), sfix(1.0), sfix(1.0)],
        [sfix(146092.88325869228), sfix(-2611125.5342573323), sfix(613302.0891230749), sfix(5722749.260176608), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(146092.88325869228), sfix(-2611067.708412215), sfix(621370.9672623038), sfix(5642063.904319932), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(146093.5163855885), sfix(-2611086.2922118455), sfix(619253.6904934504), sfix(5728423.2126796795), sfix(-484278.27007468184), sfix(-7242760.95380414), sfix(2345906.0823180596), sfix(1.0), sfix(1.0)],
        [sfix(138995.6084670833), sfix(-2489577.3244785545), sfix(-192003.22954749365), sfix(8353361.236676881), sfix(-4456201.216049513), sfix(-5653107.226773742), sfix(3849617.1316579552), sfix(1.0), sfix(1.0)],
        [sfix(6379094.204734982), sfix(-38338202.65469609), sfix(81799723.02802469), sfix(-83457717.48941404), sfix(42819731.319632955), sfix(-10684285.587564962), sfix(1010255.5374140184), sfix(1.0), sfix(1.0)],
        [sfix(-35952216.9372729), sfix(113131047.35366066), sfix(-142045076.35168043), sfix(90634609.47291712), sfix(-31833242.065120764), sfix(5874871.409555022), sfix(-446981.83202211896), sfix(1.0), sfix(1.0)],
        [sfix(28720439.76960249), sfix(-59353175.38054347), sfix(49426211.7524971), sfix(-22627451.442242313), sfix(5827819.978017179), sfix(-800404.5985767803), sfix(45805.19870818833), sfix(1.0), sfix(1.0)],
        [sfix(303217.50285751827), sfix(-1064328.66711451), sfix(-426758.7379203877), sfix(129729.6662467785), sfix(-19898.37772384198), sfix(1558.64504793835), sfix(-49.86060792102), sfix(1.0), sfix(1.0)],
        [sfix(1296917.4687310709), sfix(-2248135.717408838), sfix(149099.48563674153), sfix(-17859.11344972282), sfix(1217.69943951915), sfix(-44.66926091226), sfix(0.68694954979), sfix(1.0), sfix(1.0)],
        [sfix(3731.87301403142), sfix(-1574503.6871439968), sfix(64.11180447507), sfix(-2.72372630629), sfix(0.0628464848), sfix(-0.00074962348), sfix(3.62392e-06), sfix(1.0), sfix(1.0)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)]
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
        sfix(-50.0),
        sfix(-25.0),
        sfix(-12.5),
        sfix(-4.6875),
        sfix(-3.90625),
        sfix(-3.125),
        sfix(-2.9296875),
        sfix(-2.734375),
        sfix(-2.34375),
        sfix(-1.953125),
        sfix(-1.5625),
        sfix(-1.3671875),
        sfix(-1.26953125),
        sfix(-0.78125),
        sfix(-0.09765625),
        sfix(0.048828125),
        sfix(0.1953125),
        sfix(0.390625),
        sfix(0.78125),
        sfix(1.171875),
        sfix(1.953125),
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
        [sfix(-2.08676534942), sfix(-0.33024882258), sfix(-0.02155793682), sfix(-0.00074316041), sfix(-1.427333e-05), sfix(-1.4487e-07), sfix(-6.1e-10), sfix(1.0), sfix(1.0)],
        [sfix(-97216.1816169063), sfix(-29699.14013196948), sfix(-3761.21585324404), sfix(-252.62098376249), sfix(-9.48725053713), sfix(-0.18885695593), sfix(-0.00155670223), sfix(1.0), sfix(1.0)],
        [sfix(-3777872.3623219333), sfix(-2028176.215891121), sfix(-464490.03050602874), sfix(-57769.68470275358), sfix(-4095.4760152996), sfix(-156.27523224947), sfix(-2.49917075519), sfix(1.0), sfix(1.0)],
        [sfix(47993085.035455324), sfix(68648738.78802696), sfix(39783800.09559354), sfix(12175662.152267635), sfix(2088459.060499376), sfix(190788.24915774484), sfix(7257.70259894946), sfix(1.0), sfix(1.0)],
        [sfix(-2207441694.158732), sfix(-4348208949.082451), sfix(-3434694427.0895767), sfix(-1408710439.5714657), sfix(-318658798.4342502), sfix(-37870499.3340513), sfix(-1853220.2692186648), sfix(1.0), sfix(1.0)],
        [sfix(-123102337.65965404), sfix(790779845.1655757), sfix(1532084508.5087028), sfix(1053870488.6966515), sfix(349920452.34292346), sfix(57053334.708534054), sfix(3678833.972630158), sfix(1.0), sfix(1.0)],
        [sfix(6464572416.1791935), sfix(14135712963.875525), sfix(12797435992.638943), sfix(6126440694.065199), sfix(1634884765.2696476), sfix(230677769.41410643), sfix(13455219.540164022), sfix(1.0), sfix(1.0)],
        [sfix(-1208560766.8247406), sfix(-3159648863.9222527), sfix(-3452436854.910611), sfix(-2019438541.5076358), sfix(-662912293.3596385), sfix(-115135305.65803972), sfix(-8237364.615162582), sfix(1.0), sfix(1.0)],
        [sfix(520494013.02696556), sfix(1761037450.9203725), sfix(2328704041.6325603), sfix(1575819122.3267944), sfix(586963898.3532847), sfix(115402524.53126092), sfix(9402503.115145637), sfix(1.0), sfix(1.0)],
        [sfix(48508317.54738104), sfix(8470103.884959197), sfix(-305059219.24024665), sfix(-491650098.1494761), sfix(-311857097.36761194), sfix(-90518722.77430478), sfix(-10069275.991307892), sfix(1.0), sfix(1.0)],
        [sfix(-198821801.41612273), sfix(-839069901.3802034), sfix(-1506707745.0744934), sfix(-1392564045.6646957), sfix(-687799222.9435136), sfix(-173074452.12100902), sfix(-17492584.01512551), sfix(1.0), sfix(1.0)],
        [sfix(-46502370.4756613), sfix(-182512352.727541), sfix(-326898755.02922857), sfix(-261241484.59198993), sfix(-77243881.22332154), sfix(2761459.681205979), sfix(3619335.5023540985), sfix(1.0), sfix(1.0)],
        [sfix(7286809.226266049), sfix(73402944.67469224), sfix(180577773.36234742), sfix(275577992.3793303), sfix(242217113.62293187), sfix(104156896.03161515), sfix(17027648.19240251), sfix(1.0), sfix(1.0)],
        [sfix(-840708.1728694963), sfix(14419919.256996768), sfix(-474733.1632215951), sfix(-25845009.085579004), sfix(-45218015.54306252), sfix(-44800871.665364414), sfix(-15744240.32026851), sfix(1.0), sfix(1.0)],
        [sfix(-835318.7580152034), sfix(14569595.64517727), sfix(1205463.7449703112), sfix(-14544429.060819363), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(-835374.4172492861), sfix(14573828.19511859), sfix(1241265.402641058), sfix(-15872581.472279882), sfix(-15144260.084323805), sfix(14901274.31873599), sfix(14791400.075431155), sfix(1.0), sfix(1.0)],
        [sfix(-839240.3371919299), sfix(14674674.082357928), sfix(131104.8869333257), sfix(-9234570.746007772), sfix(-38019263.15297758), sfix(58228695.38818754), sfix(-20610435.72627888), sfix(1.0), sfix(1.0)],
        [sfix(-558226.2015755152), sfix(11405776.01731874), sfix(15645960.555876298), sfix(-47326605.68750528), sfix(12066733.277382603), sfix(26147573.82402942), sfix(-13685333.663184479), sfix(1.0), sfix(1.0)],
        [sfix(1356758.4897245856), sfix(-8343384.401383887), sfix(95636325.42758946), sfix(-214236602.21903488), sfix(203759134.36100915), sfix(-89608815.94338447), sfix(15162554.407373058), sfix(1.0), sfix(1.0)],
        [sfix(-43836734.30012286), sfix(223975741.25749442), sfix(-404713371.60350114), sfix(363715398.73307866), sfix(-173872270.46974128), sfix(42718234.357171446), sfix(-4262378.860324205), sfix(1.0), sfix(1.0)],
        [sfix(165413283.59910578), sfix(-460953524.3155429), sfix(531284666.8908695), sfix(-319793317.8029492), sfix(107414387.47080697), sfix(-19130480.777005643), sfix(1413538.123512774), sfix(1.0), sfix(1.0)],
        [sfix(-55287770.40980692), sfix(114856156.50680916), sfix(-94919679.44154625), sfix(43574643.65580163), sfix(-11247834.517428748), sfix(1547357.2278873594), sfix(-88660.39662776756), sfix(1.0), sfix(1.0)],
        [sfix(-795203.1544483111), sfix(2794931.368492901), sfix(1122614.6507960444), sfix(-341232.32684763044), sfix(52339.68643763828), sfix(-4099.93270745802), sfix(131.16209920906), sfix(1.0), sfix(1.0)],
        [sfix(-3408267.6279796506), sfix(5908046.096649985), sfix(-391829.829194902), sfix(46933.31665605272), sfix(-3200.08457017243), sfix(117.38973343391), sfix(-1.80528674276), sfix(1.0), sfix(1.0)],
        [sfix(-9807.27170028402), sfix(4137757.4720497886), sfix(-168.48426602415), sfix(7.1578866218), sfix(-0.16515903663), sfix(0.00196999232), sfix(-9.52358e-06), sfix(1.0), sfix(1.0)]
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
        sfix(-50.0),
        sfix(-25.0),
        sfix(-12.5),
        sfix(-6.25),
        sfix(-4.6875),
        sfix(-3.125),
        sfix(-2.34375),
        sfix(-1.5625),
        sfix(-0.78125),
        sfix(-0.390625),
        sfix(-0.1953125),
        sfix(-0.09765625),
        sfix(0.0),
        sfix(0.09765625),
        sfix(0.78125),
        sfix(1.5625),
        sfix(2.34375),
        sfix(3.125),
        sfix(3.90625),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-7.75182779754), sfix(-1.22679437995), sfix(-0.08008251333), sfix(-0.00276066089), sfix(-5.302198e-05), sfix(-5.3815e-07), sfix(-2.26e-09), sfix(1.0), sfix(1.0)],
        [sfix(-361134.56610599026), sfix(-110325.11159042067), sfix(-13972.0058183816), sfix(-938.42576249128), sfix(-35.24283765605), sfix(-0.70155784462), sfix(-0.00578277171), sfix(1.0), sfix(1.0)],
        [sfix(-12660888.655453198), sfix(-6583749.947640467), sfix(-1455552.9027419903), sfix(-174345.90274485346), sfix(-11887.5390232869), sfix(-436.07442444575), sfix(-6.70620295551), sfix(1.0), sfix(1.0)],
        [sfix(-9385110.331727494), sfix(-2704552.0821435614), sfix(359017.8860677086), sfix(263955.0492869883), sfix(46442.98943230823), sfix(3647.84225359536), sfix(111.3474620318), sfix(1.0), sfix(1.0)],
        [sfix(56270794.920219995), sfix(92230108.99953951), sfix(57607505.5318533), sfix(18683329.122288655), sfix(3379871.815064757), sfix(325259.4278339245), sfix(13031.19085437282), sfix(1.0), sfix(1.0)],
        [sfix(-101787871.77682993), sfix(-180222541.7419452), sfix(-132484829.98634064), sfix(-49172266.66221064), sfix(-9383586.315559296), sfix(-811673.5390333863), sfix(-18523.99372467058), sfix(1.0), sfix(1.0)],
        [sfix(-4205958.8397984635), sfix(-47591241.25261142), sfix(-116425187.36522354), sfix(-112191873.76706585), sfix(-53084418.10293119), sfix(-12394844.510678895), sfix(-1145609.2199442373), sfix(1.0), sfix(1.0)],
        [sfix(8080587.5909435395), sfix(47742552.83181175), sfix(108481800.09913653), sfix(138152358.73271143), sfix(93811912.39913538), sfix(31785523.89135403), sfix(4246260.135435099), sfix(1.0), sfix(1.0)],
        [sfix(771808.669538291), sfix(3524460.5874157124), sfix(-1308652.315183873), sfix(-4069876.188533699), sfix(-6304660.675973874), sfix(-3631875.3164142114), sfix(-390018.7802013015), sfix(1.0), sfix(1.0)],
        [sfix(835450.3445727149), sfix(4279226.090201426), sfix(2376472.276480129), sfix(5379875.02077937), sfix(7039139.0167032555), sfix(6099232.636324331), sfix(2411118.7265321864), sfix(1.0), sfix(1.0)],
        [sfix(834692.8337056439), sfix(4260308.077558976), sfix(2176827.653611787), sfix(4236085.143320561), sfix(3273286.5930498587), sfix(-679487.5955038945), sfix(-2814242.5456820326), sfix(1.0), sfix(1.0)],
        [sfix(834688.418480927), sfix(4259532.595039858), sfix(2136391.5270609646), sfix(3575077.606875388), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(834688.4184809269), sfix(4260509.961289928), sfix(2144273.3653550777), sfix(4687787.901369252), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(835004.7922528371), sfix(4249037.297610242), sfix(2326737.7062250087), sfix(3070065.395044281), sfix(7347381.392389171), sfix(-11444402.426806796), sfix(4514543.709345667), sfix(1.0), sfix(1.0)],
        [sfix(6624113.107309867), sfix(-29797279.73828321), sfix(82674004.71752962), sfix(-91355704.0189519), sfix(61115943.336156614), sfix(-21344533.38777465), sfix(2958424.990772104), sfix(1.0), sfix(1.0)],
        [sfix(155814412.99733025), sfix(-502143803.9436324), sfix(687661135.4284447), sfix(-486353109.33177483), sfix(195501492.34095386), sfix(-42241866.898632996), sfix(3800142.1956106466), sfix(1.0), sfix(1.0)],
        [sfix(3083595997.555004), sfix(-6808923948.604466), sfix(6207444151.873772), sfix(-2969871597.86778), sfix(788583903.9553912), sfix(-110293645.81797165), sfix(6355601.230831493), sfix(1.0), sfix(1.0)],
        [sfix(-1743144568.3151853), sfix(3343260945.7849655), sfix(-2577253593.5928288), sfix(1042380687.2476264), sfix(-233328012.88003257), sfix(27502231.606093436), sfix(-1336956.457929204), sfix(1.0), sfix(1.0)],
        [sfix(-6093246.891815387), sfix(14311958.29595718), sfix(2138413.3108165422), sfix(-712031.4527963025), sfix(109693.60229482171), sfix(-8393.46077932574), sfix(259.20338813179), sfix(1.0), sfix(1.0)],
        [sfix(-12660888.65565544), sfix(21946960.14743403), sfix(-1455552.9027763288), sfix(174345.90274959884), sfix(-11887.53902364971), sfix(436.07442446031), sfix(-6.70620295575), sfix(1.0), sfix(1.0)],
        [sfix(-36431.63875468979), sfix(15370766.722857917), sfix(-625.87823643618), sfix(26.58981495057), sfix(-0.61352581476), sfix(0.00731804428), sfix(-3.537781e-05), sfix(1.0), sfix(1.0)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0)]
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
        sfix(-50.0),
        sfix(-12.5),
        sfix(-9.375),
        sfix(-7.8125),
        sfix(-6.25),
        sfix(-4.296875),
        sfix(-3.90625),
        sfix(-3.7109375),
        sfix(-3.515625),
        sfix(-3.125),
        sfix(-2.734375),
        sfix(-2.5390625),
        sfix(-2.44140625),
        sfix(-1.953125),
        sfix(-1.3671875),
        sfix(-1.26953125),
        sfix(-1.171875),
        sfix(-0.78125),
        sfix(-0.5859375),
        sfix(-0.09765625),
        sfix(0.0),
        sfix(0.09765625),
        sfix(0.1953125),
        sfix(0.390625),
        sfix(0.78125),
        sfix(1.171875),
        sfix(1.3671875),
        sfix(1.5625),
        sfix(2.34375),
        sfix(3.125),
        sfix(12.5)
    ]
    coeffA = [
        [sfix(545.35371414407), sfix(113.11536156752), sfix(9.36891758136), sfix(0.39802915371), sfix(0.00918401129), sfix(0.00010954552), sfix(5.2958e-07), sfix(1.0), sfix(1.0)],
        [sfix(111129.77336321273), sfix(51796.58679285282), sfix(10214.29050700419), sfix(1088.25178267164), sfix(65.93340356402), sfix(2.15012289288), sfix(0.02944148281), sfix(1.0), sfix(1.0)],
        [sfix(203303.2719981819), sfix(109184.1216227896), sfix(25147.31674992807), sfix(3167.1497975741), sfix(229.24395060349), sfix(9.0140729389), sfix(0.15002832094), sfix(1.0), sfix(1.0)],
        [sfix(224849.537915262), sfix(124886.5748373368), sfix(29908.25557683901), sfix(3935.64113137121), sfix(298.87294360402), sfix(12.37032651531), sfix(0.21723641461), sfix(1.0), sfix(1.0)],
        [sfix(118479.03303894402), sfix(15949.21388172898), sfix(-16739.81204225425), sfix(-6751.39078795019), sfix(-1082.22385063746), sfix(-83.05524586667), sfix(-2.53589166442), sfix(1.0), sfix(1.0)],
        [sfix(323716003.36843836), sfix(467473013.0691666), sfix(281312811.0550417), sfix(90282470.02694802), sfix(16296645.373079091), sfix(1568707.0920337287), sfix(62910.28967119154), sfix(1.0), sfix(1.0)],
        [sfix(2912138055.621665), sfix(4420337494.764224), sfix(2797250900.359211), sfix(944580163.6912559), sfix(179512970.73840433), sfix(18204334.267689396), sfix(769595.2938540194), sfix(1.0), sfix(1.0)],
        [sfix(391138379.018911), sfix(279510704.9295623), sfix(-36470987.75670487), sfix(-89595996.26162635), sfix(-32774313.792091597), sfix(-5034962.33703444), sfix(-290348.08764375147), sfix(1.0), sfix(1.0)],
        [sfix(-11554614786.621607), sfix(-20312740321.506252), sfix(-14831337708.643227), sfix(-5760393372.790902), sfix(-1255772136.879387), sfix(-145746816.95845488), sfix(-7037925.267642398), sfix(1.0), sfix(1.0)],
        [sfix(10593176010.023472), sfix(22814279251.912037), sfix(20178390034.760944), sfix(9405020539.995964), sfix(2441365786.4816494), sfix(335197377.6691681), sfix(19043229.248882364), sfix(1.0), sfix(1.0)],
        [sfix(6784310004.778314), sfix(14056886692.928413), sfix(11812766354.804174), sfix(5153768106.578742), sfix(1228886010.4096153), sfix(151141020.2078366), sfix(7422708.088111844), sfix(1.0), sfix(1.0)],
        [sfix(-178419062.26362792), sfix(-2230701107.3572445), sfix(-4065233496.6389637), sfix(-3102947798.3316884), sfix(-1186663770.3181167), sfix(-225821955.74445796), sfix(-17093099.93330371), sfix(1.0), sfix(1.0)],
        [sfix(-4685358522.107598), sfix(-13506328667.9396), sfix(-15826355049.211882), sfix(-9649541003.39813), sfix(-3237653860.843729), sfix(-568722617.5544603), sfix(-40994206.40989708), sfix(1.0), sfix(1.0)],
        [sfix(1182122805.5208378), sfix(4946388919.334165), sfix(8412584986.241039), sfix(7372089787.714909), sfix(3501747693.5556655), sfix(857608053.0586652), sfix(85058886.39190818), sfix(1.0), sfix(1.0)],
        [sfix(88251310.0149836), sfix(357615962.9543534), sfix(382413396.46500814), sfix(-131722706.56792715), sfix(-447472041.60834247), sfix(-252350786.7347983), sfix(-45100303.38308591), sfix(1.0), sfix(1.0)],
        [sfix(-65503053.0011814), sfix(-364321334.82966125), sfix(-1030434287.1136523), sfix(-1606840125.3805542), sfix(-1314071711.6119149), sfix(-523962654.4957035), sfix(-80582346.06053407), sfix(1.0), sfix(1.0)],
        [sfix(-32732998.99692687), sfix(-160659034.52284104), sfix(-511326816.95262975), sfix(-909790099.3215468), sfix(-792722950.4308103), sfix(-317660800.2097289), sfix(-46794909.48905071), sfix(1.0), sfix(1.0)],
        [sfix(-4746577.641526471), sfix(31139004.08617107), sfix(37185162.20349998), sfix(-71519208.27437127), sfix(-70321521.05882514), sfix(15360879.147674698), sfix(17398641.254066598), sfix(1.0), sfix(1.0)],
        [sfix(-4855819.80274654), sfix(30096931.672590926), sfix(33501238.497021083), sfix(-76845571.7622682), sfix(-70999312.4794156), sfix(21059923.84854893), sfix(21486869.840124503), sfix(1.0), sfix(1.0)],
        [sfix(-4853174.665037069), sfix(30190147.32373723), sfix(35188783.87478518), sfix(-59384923.07952712), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(-4853174.665037069), sfix(30173510.494393747), sfix(34943272.390622586), sfix(-78179381.89211686), sfix(0.0), sfix(0.0), sfix(0.0), sfix(1.0), sfix(1.0)],
        [sfix(-4853238.692267851), sfix(30183010.830453124), sfix(34455991.43458805), sfix(-69597517.33599374), sfix(-54326489.555858895), sfix(82060841.55275276), sfix(3421786.304565713), sfix(1.0), sfix(1.0)],
        [sfix(-4860798.032700744), sfix(30379126.554874774), sfix(32314843.726280473), sfix(-56958869.96677117), sfix(-97029963.42502372), sfix(160651322.26883194), sfix(-58304454.187555335), sfix(1.0), sfix(1.0)],
        [sfix(-4195152.449416609), sfix(22553664.313005), sfix(70037869.78280152), sfix(-151830576.21795437), sfix(32814957.282543775), sfix(70969462.79678503), sfix(-35122992.69938443), sfix(1.0), sfix(1.0)],
        [sfix(2225086.7537699006), sfix(-36376524.44864035), sfix(291554385.085212), sfix(-591024688.7937543), sfix(519150035.45319873), sfix(-214951443.88273814), sfix(34718395.53950399), sfix(1.0), sfix(1.0)],
        [sfix(-66365090.58052821), sfix(325589121.8278932), sfix(-507365356.2116313), sfix(352936197.9147194), sfix(-110506503.72110678), sfix(9837411.884858323), sfix(1168507.4823311325), sfix(1.0), sfix(1.0)],
        [sfix(-120514956.03943998), sfix(565250025.1004199), sfix(-949842490.1025509), sfix(789132074.2850834), sfix(-352656931.38962746), sfix(81611723.2589647), sfix(-7705358.36328788), sfix(1.0), sfix(1.0)],
        [sfix(126835018.01731697), sfix(-265307810.78877723), sfix(209145267.2665407), sfix(-70937397.24209948), sfix(5197217.68158298), sfix(2494243.9695725436), sfix(-448351.2243188876), sfix(1.0), sfix(1.0)],
        [sfix(-11437232.178306337), sfix(22227374.61423753), sfix(-18275773.38841791), sfix(7936498.363445962), sfix(-1941985.4947436652), sfix(253881.82610932583), sfix(-13851.92500755695), sfix(1.0), sfix(1.0)],
        [sfix(171299.7851128577), sfix(-310895.3357343775), sfix(15354.57532705407), sfix(-1443.70112200523), sfix(65.36379994015), sfix(-0.97821990733), sfix(-0.00956338922), sfix(1.0), sfix(1.0)],
        [sfix(545.35371404888), sfix(-230088.59902307185), sfix(9.36891757859), sfix(-0.39802915356), sfix(0.00918401129), sfix(-0.00010954551), sfix(5.2958e-07), sfix(1.0), sfix(1.0)]
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

def func4_kan_model_evaluate(x):
    # dim_list required
    input_x = x
    dim_list = [(2, 9), (9, 1)]
    for l in range(len(dim_list)):
        in_dim, out_dim = dim_list[l]
        partial_result = [0]*out_dim
        for i in range(in_dim):
            for j in range(out_dim):
                partial_result[j] += eval(f"neuron{l}{i}{j}")(input_x[i])
        input_x = partial_result
    return input_x

def func4_kan_model_evaluate_vectorized(x):
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

