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
        sfix(-4.199999809265137),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-28034331.159324277), sfix(-72555763.54830694), sfix(-80673055.6382809), sfix(-50711376.675865754), sfix(-19745135.30812292), sfix(-4879515.71094044), sfix(-747758.3589022445), sfix(-64995.42817954702), sfix(-2454.31765684659)],
        [sfix(-21570782.092339225), sfix(-123520364.43488957), sfix(-285865814.9547414), sfix(-356923004.60892993), sfix(-266644276.23199457), sfix(-123356769.25100444), sfix(-34783837.74271361), sfix(-5497001.959748628), sfix(-374283.71943952853)],
        [sfix(304085.65472462075), sfix(-2377930.447614375), sfix(-2871550.736891955), sfix(-179651.87852603264), sfix(-12627027.534212578), sfix(-30894479.480998844), sfix(-27382499.38548536), sfix(-10766618.200933), sfix(-1583445.6681701513)],
        [sfix(316238.7309124914), sfix(-2187548.2618586416), sfix(-1777207.7672059764), sfix(3530164.386543054), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(316238.73091249145), sfix(-2168487.7140001967), sfix(-1365264.4773818746), sfix(6457662.983036236), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(316220.04997607996), sfix(-2168153.781167169), sfix(-1355163.9413728542), sfix(6181289.953385268), sfix(2039451.3673349535), sfix(-3308279.832386761), sfix(-11784533.092440002), sfix(14970174.80142011), sfix(-4914209.530832417)],
        [sfix(-2105606.8579134373), sfix(19441384.219117295), sfix(-82772711.28419346), sfix(173365666.47012466), sfix(-197460457.9566199), sfix(129392083.05819023), sfix(-49067212.16626618), sfix(10054586.790716007), sfix(-864864.2527225637)],
        [sfix(68951733.2735631), sfix(-167911206.98676738), sfix(176720717.81383425), sfix(-105842717.46294114), sfix(39352125.542766705), sfix(-9306966.420330036), sfix(1368139.5904201977), sfix(-114343.45053075916), sfix(4161.2031959449)]
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
        sfix(-999.0),
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
        [sfix(-69935530.35595913), sfix(-193296341.8772523), sfix(-219844035.13830882), sfix(-140645758.35909945), sfix(-55698162.18472963), sfix(-13986470.025936265), sfix(-2174847.6653309907), sfix(-191515.85645628272), sfix(-7315.56873765334)],
        [sfix(1773427.7179723652), sfix(9597022.403330445), sfix(56620265.89564047), sfix(139834719.5655595), sfix(185236190.0480859), sfix(139655532.2385209), sfix(60073974.90525785), sfix(13770187.354377022), sfix(1308435.664666149)],
        [sfix(191147.01985919368), sfix(-5505652.3000025265), sfix(-4609986.966675133), sfix(3150616.1562890443), sfix(3968789.6687058527), sfix(-2554320.2468178333), sfix(34444.51356775846), sfix(4399341.22814668), sfix(2064147.104998615)],
        [sfix(191142.45509069524), sfix(-5522990.022372547), sfix(-5020157.051966622), sfix(639301.0521843543), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(191142.4550906953), sfix(-5504650.529168006), sfix(-4672056.381941771), sfix(3929832.0644966955), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(257258.43483399792), sfix(-6772791.481137852), sfix(4502570.788306244), sfix(-29141987.49624985), sfix(66319408.09643649), sfix(-72560210.84137626), sfix(40739089.29567006), sfix(-11388174.127137898), sfix(1260899.4598612348)],
        [sfix(336887658.9642038), sfix(-848824189.2305738), sfix(906877048.2742825), sfix(-551946039.6634418), sfix(207319192.20331025), sfix(-49317135.1122569), sfix(7267814.693725002), sfix(-607412.2543574424), sfix(22062.78531701652)]
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
        [sfix(-3435919.8766162703), sfix(-8983873.504043879), sfix(-11812760.31315142), sfix(-8363215.5906010205), sfix(-3507306.3172221356), sfix(-908487.5577710049), sfix(-143593.85146970846), sfix(-12746.90359822281), sfix(-488.48413647152)],
        [sfix(7856673.95570668), sfix(43230152.78536009), sfix(127556880.25526688), sfix(207991652.10629562), sfix(194767170.294524), sfix(108645603.03790559), sfix(35888641.08336581), sfix(6506870.933994267), sfix(500618.2987850635)],
        [sfix(1209399.983766922), sfix(-803833.0622781535), sfix(-1331283.5457167907), sfix(-8832323.346601263), sfix(-32700412.424259666), sfix(-41623973.622139715), sfix(-23637941.461351257), sfix(-5756610.958361826), sfix(-360811.1133946808)],
        [sfix(1232024.9787091813), sfix(-405281.13614422624), sfix(1760057.100735321), sfix(4527459.211254952), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(1232024.9787091815), sfix(-431833.0657145914), sfix(1900378.6918720074), sfix(-97485.53755181258), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(1448753.8323159092), sfix(-3080847.858237709), sfix(14477052.980369646), sfix(-29420325.74980597), sfix(36561911.694297485), sfix(-28262249.04622297), sfix(13212051.812460933), sfix(-3372791.500154808), sfix(357865.3178356759)],
        [sfix(231145996.27410442), sfix(-605232695.0455184), sfix(683217142.3907148), sfix(-432357203.79953396), sfix(168890479.13031122), sfix(-41773551.2437459), sfix(6396983.804264814), sfix(-555044.29213751), sfix(20907.74842007586)]
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
        sfix(-999.0),
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
        [sfix(2857723.397027261), sfix(10195799.967838952), sfix(-668987.1739309875), sfix(-12138375.68261021), sfix(-10230005.016290616), sfix(-4026299.2797558485), sfix(-856998.9714564114), sfix(-95517.34604708696), sfix(-4385.55208485929)],
        [sfix(2782546.4726171275), sfix(9676633.663399022), sfix(-1094242.295192773), sfix(-8608937.52327258), sfix(-818082.0537290296), sfix(3598447.773106283), sfix(-1533721.0776085246), sfix(-3915807.03332749), sfix(-1423818.5584583613)],
        [sfix(2782550.946416326), sfix(9686189.018694937), sfix(-878173.4947902082), sfix(-7450616.846063497), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(2782550.9464163263), sfix(9682605.82929823), sfix(-1215840.7384509086), sfix(-8043393.653883929), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(2435729.426600208), sfix(14100607.797981035), sfix(-23943976.57801133), sfix(53733213.19692869), sfix(-98600754.57417157), sfix(94981919.9313203), sfix(-47049077.91979668), sfix(11619447.042396624), sfix(-1142438.32543744)],
        [sfix(658240178.353548), sfix(-1732304366.193548), sfix(1956867596.9943411), sfix(-1236353618.7276032), sfix(481391791.2449581), sfix(-118562659.28829546), sfix(18067966.8431735), sfix(-1559559.0550974868), sfix(58432.59291940728)]
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
        sfix(-999.0),
        sfix(-999.0),
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
        [sfix(48561689.20515542), sfix(190372981.49697617), sfix(293019917.25410753), sfix(244334113.16495398), sfix(122134876.40410002), sfix(37707660.00392645), sfix(7054945.300618506), sfix(734116.0605820036), sfix(32629.40436529713)],
        [sfix(1750890.7832126876), sfix(2879049.38471894), sfix(-6113601.584242072), sfix(-1120422.9507202206), sfix(-5514178.004530923), sfix(-34469964.89288326), sfix(-41379401.448237255), sfix(-19509322.08643355), sfix(-3315068.863511272)],
        [sfix(1762478.8627600556), sfix(3037851.9322963953), sfix(-5624937.378099256), sfix(-1190566.5217896227), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(1762478.8627600556), sfix(3092026.0478330664), sfix(-5008892.785897533), sfix(8006223.411403355), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(1820435.7024661198), sfix(2083355.1410670783), sfix(2613571.7267341404), sfix(-24372840.918387473), sfix(81261367.02394995), sfix(-113492125.02153254), sfix(75930669.58439222), sfix(-23635955.88918071), sfix(2600078.98917104)],
        [sfix(-9311.84752229993), sfix(32334785.494140007), sfix(-140849941.0203226), sfix(309882039.6020523), sfix(-366045341.5864558), sfix(246466916.38204083), sfix(-94711565.99300599), sfix(19385022.77863592), sfix(-1644006.126502173)],
        [sfix(680390911.8692826), sfix(-1752104265.6253262), sfix(1940377471.757838), sfix(-1204114015.0370953), sfix(461039363.5338739), sfix(-111771098.00325812), sfix(16780594.654912233), sfix(-1428087.6262716742), sfix(52793.01819755493)]
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
        sfix(-999.0),
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
        [sfix(147961.76406784548), sfix(21139849.90176488), sfix(49026761.73533448), sfix(51326941.46174416), sfix(29765499.413944148), sfix(10188083.628423044), sfix(2053852.939221568), sfix(225982.8774376998), sfix(10484.09981543877)],
        [sfix(-279454.15065029275), sfix(7638471.256688046), sfix(17224942.35449129), sfix(58880750.71364893), sfix(138074008.64568788), sfix(168819587.9420393), sfix(111103588.86866353), sfix(38014493.38612311), sfix(5358124.424472471)],
        [sfix(-519629.10614832654), sfix(4428868.371805867), sfix(-1753001.7074615257), sfix(-6643439.811004655), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-520536.4015655865), sfix(4417419.017693758), sfix(-1608965.450385445), sfix(-3478817.9504708657), sfix(7268368.519939459), sfix(9535520.777396746), sfix(-32659077.85555202), sfix(28247361.085890934), sfix(-8165434.867507621)],
        [sfix(-3324869.6676888065), sfix(30687696.1293299), sfix(-105358120.71903224), sfix(219039292.12674364), sfix(-268374548.45319214), sfix(197870070.62894157), sfix(-85479321.8688055), sfix(19884428.152920548), sfix(-1922951.2835254122)],
        [sfix(97626875.51501237), sfix(-318762502.47832435), sfix(428802009.4786909), sfix(-308499608.15186965), sfix(133887546.33091547), sfix(-36175374.38692298), sfix(5973195.068161077), sfix(-553090.5877227973), sfix(22048.71928294316)]
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
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
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
        [sfix(-22647949.104180835), sfix(-53945134.83779338), sfix(-57765280.266974404), sfix(-33116547.941288073), sfix(-10729504.358400822), sfix(-1888136.381952309), sfix(-138661.5649274398), sfix(3824.83994507269), sfix(842.2658455381)],
        [sfix(-1872551.2831361983), sfix(9095605.591157211), sfix(7288385.499513435), sfix(-322259.26708988816), sfix(32797195.019365154), sfix(71175343.7743593), sfix(57306015.52979217), sfix(20676628.740409568), sfix(2782075.9117031433)],
        [sfix(-1899688.232917152), sfix(8570838.276517808), sfix(3644305.521634437), sfix(-12735756.708960207), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-1900882.0985902096), sfix(8606613.773055037), sfix(3746748.797112579), sfix(-15069793.820317922), sfix(-1447116.5986150405), sfix(9017636.524198167), sfix(21409024.011688903), sfix(-31912322.9197628), sfix(11238952.886139037)],
        [sfix(3557715.329497972), sfix(-42702030.48513731), sfix(207960138.24859682), sfix(-459991154.27513784), sfix(567533386.810418), sfix(-409104557.6417756), sfix(171609028.75921142), sfix(-38864161.27747098), sfix(3677842.816228739)],
        [sfix(79020626.84237637), sfix(-159483516.33443156), sfix(134258516.0530029), sfix(-53879531.24753834), sfix(9553166.775764724), sfix(318629.9824153143), sfix(-435482.75704378146), sfix(69330.59936428978), sfix(-3727.00801937865)]
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
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-2.0999999046325684),
        sfix(-0.5249999761581421),
        sfix(-0.26249998807907104),
        sfix(0.0),
        sfix(0.5249999761581421)
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
        [sfix(-180452405.83684164), sfix(-512173264.08969796), sfix(-609411161.5865741), sfix(-403780995.88313025), sfix(-163958823.55645645), sfix(-41925696.84362702), sfix(-6608709.3463544445), sfix(-588162.2056915947), sfix(-22658.6545145235)],
        [sfix(2644115.843363975), sfix(40491331.5672765), sfix(178631454.71811154), sfix(375344465.2818573), sfix(449901249.99868107), sfix(319970846.88609487), sfix(133130101.2619491), sfix(29935455.63377853), sfix(2812236.599862789)],
        [sfix(-2127680.51145546), sfix(-3646245.473040361), sfix(6048151.484359479), sfix(7141703.125588315), sfix(-7781064.152890924), sfix(-243933.83486264263), sfix(32916741.73502053), sfix(35905184.176030785), sfix(11491940.575024508)],
        [sfix(-2127730.264290767), sfix(-3636214.8728903364), sfix(6348711.014027193), sfix(9724855.923595764), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-2127730.264290767), sfix(-3936867.1335039577), sfix(9566686.949175416), sfix(-4960358.73164872), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(2204400.2247343934), sfix(-33506646.13881613), sfix(88569714.64418566), sfix(-108223031.8936351), sfix(69403764.17566873), sfix(-25608757.12967014), sfix(5485515.261820226), sfix(-635248.3235026078), sfix(30804.47838781178)]
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
        [sfix(-10336462.895726724), sfix(-49713627.70467006), sfix(-96431613.78124587), sfix(-93880075.23270732), sfix(-52156859.06553633), sfix(-17368251.17029966), sfix(-3437809.4024514114), sfix(-373508.73075021495), sfix(-17172.63507165084)],
        [sfix(700420.5043195799), sfix(2261195.92477183), sfix(88157.16650123459), sfix(-8280531.919398869), sfix(-21916561.63962989), sfix(-22323961.325476542), sfix(-9448435.637764541), sfix(-936084.2933061593), sfix(251442.53698400533)],
        [sfix(714929.0679947381), sfix(2524500.254714164), sfix(2251515.971717134), sfix(1322734.3199341667), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(714929.067994738), sfix(2501962.772326627), sfix(2111894.338022309), sfix(-2675406.027719067), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(669335.9545643654), sfix(3293244.9120597676), sfix(-3814008.950806179), sfix(22052772.920520123), sfix(-60794809.25693061), sfix(85240415.79471071), sfix(-62795941.851386346), sfix(22904932.557591937), sfix(-3204572.8658610834)],
        [sfix(-101840338.16024958), sfix(586768734.43498), sfix(-1425417690.276565), sfix(1942173190.523479), sfix(-1611361191.451965), sfix(832651063.3070931), sfix(-261940792.64632362), sfix(45975015.30524419), sfix(-3457038.597894187)],
        [sfix(288690148.4904913), sfix(-698868611.9327382), sfix(732595309.81048), sfix(-430699243.0946093), sfix(156509326.57985803), sfix(-36048922.042900555), sfix(5145045.466827119), sfix(-416370.2011390861), sfix(14638.00686186867)]
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
        [sfix(200178052.75960466), sfix(569463373.8573939), sfix(679197120.3782666), sfix(450831647.03172827), sfix(183308849.97537965), sfix(46921520.752166525), sfix(7402174.695454567), sfix(659213.6664384089), sfix(25409.87798814868)],
        [sfix(79673056.73827897), sfix(449636138.60429376), sfix(1095846600.1073515), sfix(1482386406.853083), sfix(1204470075.5730927), sfix(602994303.7047861), sfix(182701777.39418593), sfix(30819926.974708613), sfix(2227901.374909676)],
        [sfix(1062616.2865951944), sfix(2047716.8033588217), sfix(6144151.366945868), sfix(16539393.11435469), sfix(36661770.11952174), sfix(63177294.31368962), sfix(58557121.435894504), sfix(26021193.598202802), sfix(4442254.705698809)],
        [sfix(985846.9530221144), sfix(1030300.2432826431), sfix(238433.26320077575), sfix(-3068378.772586024), sfix(-4059332.613763945), sfix(9016292.909025215), sfix(13509077.587171098), sfix(4601051.9226823645), sfix(-15356.99594922546)],
        [sfix(985833.2134578555), sfix(1051899.3484660697), sfix(755610.1170718396), sfix(51971.0390192814), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(985833.2134578554), sfix(1029505.2659172677), sfix(266870.64710398606), sfix(-3961927.7665534457), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(935987.4675661882), sfix(1885919.5616983457), sfix(-6016161.237209704), sfix(22061738.25243962), sfix(-66102306.54202554), sfix(97697746.42517199), sfix(-68844927.67941986), sfix(22584987.008544702), sfix(-2686077.1892488115)],
        [sfix(-19340843.434139322), sfix(103108276.97224548), sfix(-202608048.24533853), sfix(186554039.13089097), sfix(-70913476.56610496), sfix(-4638206.752464881), sfix(12946282.661275439), sfix(-4003100.334027875), sfix(411866.1266348397)],
        [sfix(-165557335.94611254), sfix(401595544.56508684), sfix(-418358886.88171923), sfix(250426317.7175352), sfix(-93147388.74202783), sfix(22055804.174131967), sfix(-3248231.3641451686), sfix(272131.0174010754), sfix(-9932.05524549754)]
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
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-1.0499999523162842),
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
        [sfix(-16090395.190841982), sfix(-28086707.90134596), sfix(-20572253.581857383), sfix(-3682631.272450386), sfix(3323846.8806730183), sfix(2253150.5452102055), sfix(599029.5724511301), sfix(76754.09928163426), sfix(3918.33350013014)],
        [sfix(-1013299.6370143679), sfix(15289888.430180907), sfix(29623213.000917375), sfix(70910352.98001504), sfix(168142248.31970525), sfix(221751864.1705966), sfix(155749430.5278599), sfix(56051645.55789574), sfix(8213176.8496082)],
        [sfix(-1321689.1778535952), sfix(11384438.038421296), sfix(7891551.168722715), sfix(-4206171.444252788), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-1321689.1778535952), sfix(11163084.420088114), sfix(5483740.882737232), sfix(-9187276.909167143), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-1321704.8753098524), sfix(11163793.870236006), sfix(5477454.00248574), sfix(-9263002.192966089), sfix(252034.01658366725), sfix(12353467.576077424), sfix(-27833220.841512393), sfix(25202507.242260456), sfix(-7769549.921909823)],
        [sfix(-5323589.875230577), sfix(48272139.402797334), sfix(-140240808.2446202), sfix(304006612.54393524), sfix(-394996747.8961548), sfix(298593130.46956706), sfix(-128721027.4162892), sfix(29440416.732213125), sfix(-2780290.3646330507)],
        [sfix(501297267.86014223), sfix(-1366093073.0701385), sfix(1607415877.080972), sfix(-1055046172.6635875), sfix(426518285.25299996), sfix(-108922076.62434925), sfix(17180707.478035927), sfix(-1531956.1124532484), sfix(59174.53242961013)]
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
        [sfix(44309057.54005645), sfix(174950581.74193114), sfix(270883341.4539298), sfix(228270645.5928336), sfix(115325472.98162481), sfix(35922937.02477617), sfix(6767299.493576534), sfix(707789.3985287612), sfix(31576.48918722424)],
        [sfix(1324721.3764562996), sfix(5553170.392164634), sfix(-1826075.1943281568), sfix(-16843032.588327415), sfix(-50067597.25095467), sfix(-77336079.71370713), sfix(-59312515.63279389), sfix(-21711458.812151738), sfix(-2998959.120109142)],
        [sfix(1363797.238486089), sfix(6261091.028676354), sfix(4047309.526976499), sfix(14639202.094497165), sfix(79164612.34919713), sfix(341330272.9899481), sfix(912810648.8680712), sfix(1350190557.8607464), sfix(860538154.6562814)],
        [sfix(1362440.353994505), sfix(6201816.675541302), sfix(2934764.510771591), sfix(2796306.1187806167), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(1362440.3539945045), sfix(6181042.8736453615), sfix(3377372.0526875183), sfix(-428124.67097051954), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(461833.52567831136), sfix(17575034.075213954), sfix(-54949838.22316587), sfix(156174131.3312484), sfix(-235127253.40259913), sfix(191833968.58639646), sfix(-86179958.0367569), sfix(20182540.413021132), sfix(-1933370.6126079124)],
        [sfix(264484525.06775314), sfix(-669934213.9838169), sfix(737600525.2382765), sfix(-450601045.7766511), sfix(169934175.0600807), sfix(-40595315.4409691), sfix(6007279.487496836), sfix(-504007.4713201847), sfix(18371.71234673402)]
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
        sfix(-999.0),
        sfix(-999.0),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-69050304.55295303), sfix(-207203088.4123967), sfix(-250163294.99473947), sfix(-167375659.16069746), sfix(-68576751.42434376), sfix(-17679586.396388624), sfix(-2806889.113047222), sfix(-251352.84226163896), sfix(-9734.22598561319)],
        [sfix(2467104.507854312), sfix(-3952156.766657419), sfix(5166250.153169522), sfix(38990575.88426805), sfix(67096124.332214765), sfix(56735797.8171204), sfix(25983494.353296176), sfix(6188090.342968171), sfix(602712.7885935197)],
        [sfix(2264819.9785974957), sfix(-6498099.406811473), sfix(-8145684.442004369), sfix(-101696.1227806381), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(2264672.0066288314), sfix(-6497964.615762375), sfix(-8674559.857617354), sfix(3693447.4067314905), sfix(966797.0095307955), sfix(11755458.305560505), sfix(-17616323.198967464), sfix(8379660.515094026), sfix(-1280476.1176840153)],
        [sfix(47201064.46321141), sfix(-190833421.66607967), sfix(295876999.59989125), sfix(-256474721.13230765), sfix(131511363.70207456), sfix(-41336314.04864979), sfix(7838249.598235193), sfix(-824199.0160744545), sfix(36941.14567045876)]
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
        sfix(0.06562499701976776),
        sfix(1.0499999523162842),
        sfix(1.5749999284744263)
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
        [sfix(83134489.18677513), sfix(218233057.0754878), sfix(247352758.39912865), sfix(158003539.0223098), sfix(62310953.125128336), sfix(15558029.401321774), sfix(2404586.8600927605), sfix(210519.0259747833), sfix(7998.88529330063)],
        [sfix(129118570.84530282), sfix(719884969.3208803), sfix(1662183411.4023564), sfix(2093129334.5786362), sfix(1587926853.7335093), sfix(749131730.1049472), sfix(215938125.62792543), sfix(34931430.17301802), sfix(2436271.6507847453)],
        [sfix(444631.3145463033), sfix(14450713.561887246), sfix(44825828.643791296), sfix(132111415.46289955), sfix(322052640.7938038), sfix(439561131.1893115), sfix(320785755.54080397), sfix(119464540.33945607), sfix(18004139.079239167)],
        [sfix(-141969.5533041004), sfix(6616389.8181245085), sfix(-935199.3902503751), sfix(-20586300.10976418), sfix(3669007.680314719), sfix(14776637.120099284), sfix(-33376383.142503858), sfix(-49247629.76773416), sfix(-17154222.82843205)],
        [sfix(-141912.13004080477), sfix(6644201.17190663), sfix(-368413.6877890611), sfix(-18381207.583516818), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-141912.1300408048), sfix(6619180.239256967), sfix(-941462.2182165736), sfix(-19081691.693675168), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-143552.6864654673), sfix(6680827.802683367), sfix(-1772995.9622345467), sfix(-14137634.601621365), sfix(-16421882.542260427), sfix(72597247.92710619), sfix(-64295398.52965455), sfix(18933276.274259094), sfix(-592296.4152664302)],
        [sfix(21346172.58400448), sfix(-189987711.98598215), sfix(749109341.5211471), sfix(-1593187368.943369), sfix(1990043412.4716203), sfix(-1500014438.4803798), sfix(670317844.4783161), sfix(-163605926.2511033), sfix(16826226.504135784)],
        [sfix(-472572336.4569147), sfix(1503108443.1829805), sfix(-2013108947.3327696), sfix(1491177008.2881424), sfix(-671839418.3373034), sfix(189214825.57850006), sfix(-32623107.900873177), sfix(3155298.3527067867), sfix(-131317.38403786984)]
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
        sfix(-999.0),
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
        [sfix(-230144282.35499683), sfix(-638559055.4688365), sfix(-744394153.4941946), sfix(-485770763.2708579), sfix(-195061080.97559926), sfix(-49461907.27619122), sfix(-7746187.852042007), sfix(-685855.1312714892), sfix(-26312.28900484282)],
        [sfix(-141332946.0081129), sfix(-820443465.1396166), sfix(-2006655603.489059), sfix(-2691101566.133934), sfix(-2161168963.4561653), sfix(-1070464081.5612118), sfix(-321612057.8695999), sfix(-53917471.68430257), sfix(-3880829.812032192)],
        [sfix(869004.7385039339), sfix(-8831231.118830318), sfix(-22189024.553328656), sfix(612206.8801513625), sfix(21360605.75725541), sfix(-17663496.38778104), sfix(-45424119.17915886), sfix(-25295327.223631237), sfix(-4517552.379223053)],
        [sfix(870444.7779474298), sfix(-8766708.603212899), sfix(-21551192.61315182), sfix(-649226.2417218013), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(870781.4852764375), sfix(-8785671.231094677), sfix(-21725987.708313614), sfix(3283580.0606854283), sfix(29518929.436670627), sfix(2851396.351548405), sfix(-25146067.23364058), sfix(7170433.13459856), sfix(1503506.7962938682)],
        [sfix(6470617.541023828), sfix(-63758651.09081891), sfix(208156348.43490055), sfix(-529084002.27676094), sfix(770784752.0277065), sfix(-624205772.8137751), sfix(280922075.60472), sfix(-66138403.987703286), sfix(6377552.334880306)],
        [sfix(-1184990620.6271746), sfix(3227494755.310827), sfix(-3772746545.913013), sfix(2466076391.218798), sfix(-992147115.3932532), sfix(252086206.48714417), sfix(-39562486.06665583), sfix(3510590.139650857), sfix(-134981.78416009733)]
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
        [sfix(119023248.03345227), sfix(327731734.76222336), sfix(387238180.1875717), sfix(255281440.00180483), sfix(103107762.13398579), sfix(26225428.572495293), sfix(4113258.2774794465), sfix(364412.76626278), sfix(13981.92849192299)],
        [sfix(-8769988.825025743), sfix(231725032.88021702), sfix(821033326.0613211), sfix(1190363706.3878422), sfix(950624453.3158349), sfix(454568338.060955), sfix(130422600.99923497), sfix(20812040.280876), sfix(1425941.587587425)],
        [sfix(-53017692.20262363), sfix(-396527132.12749726), sfix(-1492793645.1636677), sfix(-2952217967.110039), sfix(-3334117810.485795), sfix(-2254450782.295646), sfix(-908784728.657916), sfix(-202387007.96440667), sfix(-19241472.48938073)],
        [sfix(-1961892.254988767), sfix(28178861.735566717), sfix(26127145.512661498), sfix(99450728.50839777), sfix(427496423.5417994), sfix(648014387.3166951), sfix(451061494.02914876), sfix(147053970.5743176), sfix(17602291.401523195)],
        [sfix(-2278655.0953299953), sfix(22753209.339569025), sfix(-13544919.29794255), sfix(-65501783.0392046), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-2278979.3711422035), sfix(22732854.117061876), sfix(-13625621.338807577), sfix(-60954769.20888269), sfix(34524342.31703101), sfix(71400230.2123805), sfix(-58074924.02299644), sfix(-9449434.590079684), sfix(12780938.251524096)],
        [sfix(-3101461.5317491665), sfix(33720735.44560552), sfix(-77826946.23924981), sfix(153361920.88096696), sfix(-412618475.02443916), sfix(668618306.2213448), sfix(-556961028.5815475), sfix(229016857.72869766), sfix(-37209465.19138629)],
        [sfix(-602450198.0029967), sfix(3445392308.7640343), sfix(-8378901212.2496), sfix(11306334550.449736), sfix(-9276821911.61184), sfix(4745023656.065963), sfix(-1480525195.2949712), sfix(258285760.2006702), sfix(-19339728.177116353)],
        [sfix(1720100780.218541), sfix(-4459501761.33272), sfix(4972087485.500035), sfix(-3129488169.5129213), sfix(1217234701.0412927), sfix(-300034805.68750757), sfix(45818474.72367169), sfix(-3966683.1936234185), sfix(149153.94020627422)]
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
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-2.0999999046325684),
        sfix(-1.0499999523162842),
        sfix(-0.5249999761581421),
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
        [sfix(-16382393.864008494), sfix(-39726795.48266165), sfix(-39765091.25571517), sfix(-22680710.570087586), sfix(-8125296.042468567), sfix(-1870009.0885285514), sfix(-269433.3237345714), sfix(-22184.23067162717), sfix(-798.32625770938)],
        [sfix(679246.9237642718), sfix(7663567.806974551), sfix(14944484.111968253), sfix(10182987.68637867), sfix(1783358.9769380733), sfix(-1263538.9198116432), sfix(-797116.1374707972), sfix(-179237.50780351608), sfix(-15142.64863724472)],
        [sfix(-1058461.6175441274), sfix(468515.4880571632), sfix(7371536.907373688), sfix(21331645.250475317), sfix(40138562.15888331), sfix(43861399.83825354), sfix(27074012.32489137), sfix(8892381.937471358), sfix(1219332.8693322658)],
        [sfix(-1131186.752156271), sfix(-556526.5830911313), sfix(1034841.8217593004), sfix(203915.70152154504), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-1131186.752156271), sfix(-674310.9509666194), sfix(3496303.376271077), sfix(-1876264.338104956), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-6460839.252503027), sfix(48638896.59887086), sfix(-190362419.52292943), sfix(413622746.9090157), sfix(-517673258.01580817), sfix(376040893.37864083), sfix(-157097614.84718838), sfix(35120448.25749539), sfix(-3263586.3047775966)],
        [sfix(423011418.72455245), sfix(-1151435356.368663), sfix(1337236659.9416912), sfix(-873695827.0362973), sfix(351280271.9168795), sfix(-89189406.10776421), sfix(13987500.274526639), sfix(-1240382.1755642628), sfix(47665.28757087621)]
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
        sfix(-999.0),
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
        [sfix(31805412.01103617), sfix(122392299.61602263), sfix(189651764.1276632), sfix(160707380.83497876), sfix(81667002.20978242), sfix(25567706.20116672), sfix(4836470.134332838), sfix(507510.3255983835), sfix(22700.23996193322)],
        [sfix(567631.791104908), sfix(553699.3450956901), sfix(-8471148.259092674), sfix(-33898281.37474551), sfix(-84344601.47980219), sfix(-116106585.06344447), sfix(-85873817.50971185), sfix(-32413945.957188904), sfix(-4941305.2004198255)],
        [sfix(717203.0342000237), sfix(2552296.6995282024), sfix(3207593.159539076), sfix(5084574.187951171), sfix(-3042304.5596133284), sfix(-7612268.382946811), sfix(4596570.91822056), sfix(10688331.267940596), sfix(4041634.396528904)],
        [sfix(717194.7150341676), sfix(2547848.9635405624), sfix(3131506.0170824644), sfix(5095447.525525852), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(717194.7150341676), sfix(2526145.4856305956), sfix(3799544.092845769), sfix(1651172.6220070538), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(785263.3818677898), sfix(1382219.512527232), sfix(11744360.169822184), sfix(-29585798.49056961), sfix(81578367.54088145), sfix(-137822099.2119402), sfix(116305211.51360928), sfix(-46555051.13909725), sfix(7055801.625257214)],
        [sfix(189322101.5513525), sfix(-1070243696.053677), sfix(2616673455.03278), sfix(-3533420148.551334), sfix(2887864973.7044287), sfix(-1465796228.0236235), sfix(452856938.77012736), sfix(-78157667.25107716), sfix(5789316.40764922)],
        [sfix(-254654595.97932816), sfix(638200938.9412439), sfix(-682596527.2253968), sfix(415478591.37640184), sfix(-156330719.03969088), sfix(37296812.96197701), sfix(-5517093.989321398), sfix(463104.2399690344), sfix(-16901.45198385777)]
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
        sfix(-1.0499999523162842),
        sfix(-0.26249998807907104),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-56362794.62792413), sfix(-229891583.86727265), sfix(-379524381.62171656), sfix(-334057814.08244354), sfix(-173665602.36425933), sfix(-55175003.206658766), sfix(-10544595.134874392), sfix(-1114912.883503935), sfix(-50161.94432533252)],
        [sfix(288744.9748783092), sfix(196163.53014460005), sfix(4381651.1067720745), sfix(18228198.443806075), sfix(48502718.47647481), sfix(73365726.03218874), sfix(57030430.719939664), sfix(21326066.188416153), sfix(3013336.961891472)],
        [sfix(250883.33895342567), sfix(-449938.5988921827), sfix(-316427.41047884483), sfix(-996572.9742320688), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(250991.78136292493), sfix(-452204.79716563824), sfix(-354309.3512893037), sfix(-882607.6804293857), sfix(1509275.4444505582), sfix(4209156.178998434), sfix(-5557995.301581161), sfix(622325.421991938), sfix(753472.2220135103)],
        [sfix(163783.0191370329), sfix(710764.4911672345), sfix(-7139273.728394235), sfix(21737458.380925458), sfix(-45625560.84783814), sfix(67075398.031914264), sfix(-57973572.43571739), sfix(25603630.694164563), sfix(-4458412.895619898)],
        [sfix(4443492.563846275), sfix(-45026503.762815274), sfix(185491358.862305), sfix(-416027198.9749416), sfix(554362893.3225274), sfix(-446780710.8667361), sfix(212496189.34649503), sfix(-54758910.872294135), sfix(5893601.670165369)],
        [sfix(523969420.76261646), sfix(-2187402975.359499), sfix(3893841722.897426), sfix(-3839659017.349666), sfix(2281547793.6616764), sfix(-831369397.3422383), sfix(179764561.1826859), sfix(-20731486.367755197), sfix(940129.6563755175)],
        [sfix(-1323393767.4020588), sfix(4369459536.342192), sfix(-6182507120.772198), sfix(4897718970.322231), sfix(-2378943943.042964), sfix(726855931.2758713), sfix(-136698123.09719017), sfix(14496275.81657813), sfix(-664849.7958553259)],
        [sfix(-4863114677.48373), sfix(10510994573.27134), sfix(-9892824577.76167), sfix(5299274186.87906), sfix(-1767894861.7942555), sfix(376286568.2186082), sfix(-49917352.49932814), sfix(3774513.9844191032), sfix(-124585.67193348856)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)]
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
        [sfix(41583572.33622346), sfix(113767985.30940214), sfix(137147407.67298594), sfix(91837486.70017736), sfix(37475709.649458304), sfix(9597657.852462409), sfix(1512709.2917784636), sfix(134518.36842642422), sfix(5176.73201910221)],
        [sfix(-972022.8587702075), sfix(-24760230.04079211), sfix(-77730574.17931747), sfix(-131883703.35335365), sfix(-136762509.99061352), sfix(-88310640.42737858), sfix(-34483385.56477007), sfix(-7434434.933103806), sfix(-678762.1640793144)],
        [sfix(1073845.9237080677), sfix(-6553192.7058919305), sfix(-9944040.729491876), sfix(3054784.707072688), sfix(12357826.508029724), sfix(-9640929.890863068), sfix(-36058588.57129938), sfix(-29264969.77460543), sfix(-8079638.758054862)],
        [sfix(1073893.133506706), sfix(-6593153.245674464), sfix(-10941397.875273203), sfix(-3547042.772158742), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(1073893.133506706), sfix(-6545656.57333249), sfix(-10185843.794687238), sfix(6985654.820791699), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(1077372.7805041184), sfix(-6638399.771150667), sfix(-9036029.835225474), sfix(-1180391.9480990684), sfix(27689577.047811426), sfix(-21921937.683837283), sfix(-4093864.1378098447), sfix(10295236.30479366), sfix(-3078279.37744549)],
        [sfix(-37777750.890713245), sfix(224701423.71919367), sfix(-607226027.641113), sfix(871197366.0177208), sfix(-746849944.2612789), sfix(393555379.12450826), sfix(-124560636.92137052), sfix(21661439.62472465), sfix(-1588097.7092406529)],
        [sfix(4155524730.775985), sfix(-10476093566.034058), sfix(11262582604.275784), sfix(-6755800552.047228), sfix(2474061156.6531506), sfix(-566947657.594368), sfix(79435384.7604685), sfix(-6221613.913982002), sfix(208405.64688086597)]
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
        sfix(-4.199999809265137),
        sfix(-2.0999999046325684),
        sfix(-1.5749999284744263),
        sfix(-1.0499999523162842),
        sfix(-0.26249998807907104),
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
        [sfix(-124920273.46891788), sfix(-342387023.3147002), sfix(-400441505.68449485), sfix(-261964141.8924692), sfix(-105253290.516874), sfix(-26674031.617628317), sfix(-4172691.9853622783), sfix(-368956.3236664281), sfix(-14134.91636086882)],
        [sfix(43044401.37149632), sfix(-51627340.95041262), sfix(-460285177.3050472), sfix(-809919509.0335789), sfix(-711850795.340993), sfix(-361770839.59907764), sfix(-108433975.65464686), sfix(-17895083.451465383), sfix(-1259734.4512824777)],
        [sfix(48430082.64843945), sfix(373482029.75581145), sfix(1383931008.1830175), sfix(2706083166.0443377), sfix(3045636488.8157735), sfix(2061014105.6416516), sfix(832978598.526832), sfix(186098136.92681327), sfix(17749370.73794001)],
        [sfix(983473.4894812597), sfix(-21027412.885645308), sfix(-25631870.609687712), sfix(-121162969.39689305), sfix(-430082730.4680075), sfix(-609695517.2597924), sfix(-410044537.286807), sfix(-129850879.44804287), sfix(-14912977.682443215)],
        [sfix(1298783.266902721), sfix(-15568971.949580582), sfix(15113785.803932277), sfix(49978973.29719637), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(1298783.266902721), sfix(-15614635.076595193), sfix(14094982.473492369), sfix(32204128.135795318), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(1298837.3928412679), sfix(-15615033.867662426), sfix(13919699.158182671), sfix(37459509.347810246), sfix(-37294714.80878179), sfix(-62480082.463718064), sfix(122428299.66930622), sfix(-74765359.89182143), sfix(16081894.796572791)],
        [sfix(1025568.4386113468), sfix(-11978006.721702605), sfix(-7247159.063239299), sfix(107758815.79317062), sfix(-182805490.19179922), sfix(129213071.5886995), sfix(-33766899.490993425), sfix(-3427032.910526412), sfix(2331672.468807613)],
        [sfix(257713581.41552162), sfix(-1513553679.1077132), sfix(3793058208.118891), sfix(-5309909847.924937), sfix(4551253975.147709), sfix(-2445208953.4320507), sfix(804091332.7762302), sfix(-148028763.75484887), sfix(11689620.490566984)],
        [sfix(-6614335579.186953), sfix(18041883540.199615), sfix(-20724909106.94179), sfix(12926835971.14749), sfix(-4672969408.261763), sfix(949443754.044849), sfix(-88822799.86087479), sfix(-233360.26659135852), sfix(464816.6192031451)],
        [sfix(-37395534438.825294), sfix(80765751699.76872), sfix(-75966855631.60419), sfix(40669352895.16817), sfix(-13560620911.260057), sfix(2884928950.7098265), sfix(-382541708.2778556), sfix(28914386.765504472), sfix(-954024.2358087538)]
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
        sfix(-0.26249998807907104),
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
        [sfix(319716655.00415295), sfix(891352294.4820843), sfix(1048407460.1390669), sfix(688748521.7707013), sfix(277823764.10479146), sfix(70666854.03356498), sfix(11091289.442657342), sfix(983598.576909375), sfix(37780.02677621966)],
        [sfix(-3058036.8797614533), sfix(-11817223.087643078), sfix(-135360970.2340094), sfix(-416785880.6227956), sfix(-590722140.4349765), sfix(-451386142.251544), sfix(-192780846.56770656), sfix(-43488361.653431825), sfix(-4049410.0761326705)],
        [sfix(-727414.6825256839), sfix(17578933.13521467), sfix(14773332.2648704), sfix(-15359908.590163436), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-727414.6825256833), sfix(17492862.007299993), sfix(12829307.971448569), sfix(-28145139.3903991), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-728772.24030094), sfix(17544577.51613486), sfix(12062398.455201803), sfix(-21921388.196139034), sfix(-30559548.309697192), sfix(62858279.50222396), sfix(-26740340.918192282), sfix(-5168279.421036555), sfix(4170223.3985639294)],
        [sfix(-6406191.198297383), sfix(20766961.87519778), sfix(103737649.9461363), sfix(-336041575.49241304), sfix(441125407.6844462), sfix(-311508358.40909755), sfix(123518791.39685777), sfix(-25921456.646875247), sfix(2245802.750043648)],
        [sfix(-860995325.5849129), sfix(2374429374.9673147), sfix(-2755779198.5856037), sfix(1790409586.7417247), sfix(-714991357.8199264), sfix(180434302.72047207), sfix(-28167439.61596626), sfix(2490603.2784676924), sfix(-95589.32766452128)]
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
        sfix(-0.06562499701976776),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(-25541792.20586459), sfix(-80938310.25880516), sfix(-114221682.45740214), sfix(-91072915.32751614), sfix(-44408075.21821248), sfix(-13517602.580776362), sfix(-2508277.4736087453), sfix(-259716.8356128995), sfix(-11508.48932221893)],
        [sfix(218726.8690408588), sfix(8469709.42004984), sfix(1760570.2396854449), sfix(-16578235.35346746), sfix(2146387.7595341033), sfix(36066701.623365164), sfix(32141151.371941388), sfix(9876453.178689051), sfix(671913.131959361)],
        [sfix(218260.14725138107), sfix(8452309.578177148), sfix(1542865.825039392), sfix(-17501224.298060775), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(218260.14725138096), sfix(8474036.019747823), sfix(1047757.2446951326), sfix(-16749244.88359487), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(99842.70036357586), sfix(10486375.469188798), sfix(-13341369.752737958), sfix(41686693.315731905), sfix(-151655309.7989135), sfix(239505359.68210617), sfix(-180730040.854314), sfix(65015063.35297975), sfix(-8844463.995574718)],
        [sfix(-194930875.30009764), sfix(1106094076.9058669), sfix(-2631221630.5618167), sfix(3472255277.048932), sfix(-2786024379.19386), sfix(1395238567.7471187), sfix(-426983962.9538281), sfix(73186064.44078563), sfix(-5391815.217913461)],
        [sfix(-1411938158.5322342), sfix(4471274259.815673), sfix(-6095609222.84086), sfix(4676742147.764555), sfix(-2207707225.837506), sfix(656580398.6674458), sfix(-120183810.88415697), sfix(12387720.97400268), sfix(-550927.5911248361)],
        [sfix(-7830620648.244052), sfix(17072429580.26334), sfix(-16186658180.186874), sfix(8725216462.32729), sfix(-2926582418.92597), sfix(625829729.2994039), sfix(-83361069.15819135), sfix(6326008.106298057), sfix(-209464.23957625747)]
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
        sfix(-1.0499999523162842),
        sfix(-0.26249998807907104),
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
        [sfix(57675919.65196402), sfix(167412125.39869463), sfix(204848549.6970999), sfix(138521403.6653013), sfix(57053422.530382544), sfix(14739228.014676519), sfix(2341275.4639975373), sfix(209623.43768274024), sfix(8114.70681307699)],
        [sfix(-17310869.555810407), sfix(-106686542.66408426), sfix(-221759014.21288878), sfix(-230797143.17399415), sfix(-136644611.5914058), sfix(-47611889.245758176), sfix(-9407090.668094723), sfix(-908573.2467078071), sfix(-25593.26176070382)],
        [sfix(670823.008846208), sfix(-10538450.023384403), sfix(-9952610.35747546), sfix(8186456.464332552), sfix(-6572189.90807036), sfix(-40187953.96652983), sfix(-39114810.69316866), sfix(-15573424.14335792), sfix(-2287527.868503886)],
        [sfix(683961.6915683291), sfix(-10363183.973015469), sfix(-9499409.351903072), sfix(7688183.41410047), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(683961.6915683292), sfix(-10311778.956447963), sfix(-8339395.180699368), sfix(16211217.534248313), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(672344.3559535429), sfix(-9995732.283180365), sfix(-10880611.681076316), sfix(22258425.451484784), sfix(8120726.638448222), sfix(-33467796.305224713), sfix(24527831.95877453), sfix(-7635972.679975852), sfix(894884.8074572316)],
        [sfix(729079444.965217), sfix(-1646030648.2182631), sfix(1517063126.3188162), sfix(-732882221.5295326), sfix(192660437.6899244), sfix(-23761298.20678468), sfix(-69599.46230645812), sfix(327634.16389008734), sfix(-24315.64413556059)]
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
        sfix(-1.0499999523162842),
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
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0), sfix(1.0)],
        [sfix(239237912.14220926), sfix(679901266.8655454), sfix(818592902.528657), sfix(547220640.7484792), sfix(223506667.91638678), sfix(57376257.68990677), sfix(9069008.565792782), sfix(808765.3134279246), sfix(31206.39029498342)],
        [sfix(94131939.34536733), sfix(521167836.0005781), sfix(1273247156.5262034), sfix(1722676453.0076892), sfix(1399859515.9106228), sfix(701083624.1655004), sfix(212514276.29371315), sfix(35859538.56504677), sfix(2592385.335022818)],
        [sfix(-190047.56403959132), sfix(-11588908.762647374), sfix(-12098927.527194768), sfix(5841962.262434441), sfix(24114649.94518349), sfix(28088112.50062145), sfix(12538675.917283375), sfix(-1245047.470683831), sfix(-1710819.4710493071)],
        [sfix(-190870.09158560575), sfix(-11620601.797493162), sfix(-12598053.503686756), sfix(1219886.2995526814), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-190870.09158560637), sfix(-11272579.68152355), sfix(-16836316.98789133), sfix(17364540.331048764), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(5748356.95667435), sfix(-69513423.40440455), sfix(227152289.73418927), sfix(-543952869.0792983), sfix(756992585.547965), sfix(-597183400.3207316), sfix(266411549.17165318), sfix(-62916996.4321208), sfix(6126981.478074784)],
        [sfix(4577250665.459838), sfix(-11397563599.215517), sfix(12072595715.189331), sfix(-7111557070.794822), sfix(2547172325.5338974), sfix(-567891177.4025674), sfix(76870173.01923633), sfix(-5760163.162895764), sfix(182000.89138146013)]
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
        sfix(-1.0499999523162842),
        sfix(-0.5249999761581421),
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
        [sfix(5974735.916777855), sfix(21502243.516689736), sfix(31591893.11548987), sfix(23884473.377559558), sfix(10557497.958180593), sfix(2861323.873981358), sfix(470483.01478290686), sfix(43237.62297851027), sfix(1708.30153134485)],
        [sfix(5277278.597725509), sfix(34779316.95442935), sfix(90913295.05079195), sfix(125091801.72011597), sfix(102653979.9567917), sfix(52037246.59938818), sfix(16005192.020838417), sfix(2743896.064442685), sfix(201604.6689297528)],
        [sfix(-1091658.1267020907), sfix(-1647059.241688608), sfix(1630860.117710229), sfix(3705698.9350461396), sfix(4163687.9671669016), sfix(4837527.25306569), sfix(4072021.0502847596), sfix(1785942.3428655092), sfix(306261.785391867)],
        [sfix(-1101972.6721518687), sfix(-1790281.2282822172), sfix(801096.1954869537), sfix(1255176.4630526914), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-1101972.6721518687), sfix(-1872807.3293541037), sfix(1799179.307790283), sfix(-2059487.3930171009), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-1040836.2519718426), sfix(2679225.0026923115), sfix(-36287992.91387923), sfix(121782239.48559855), sfix(-205943411.4853118), sfix(187842800.1687059), sfix(-94370446.34835073), sfix(24668268.20446317), sfix(-2626308.023043683)],
        [sfix(750480361.1682163), sfix(-1319329136.7994616), sfix(705303218.4021071), sfix(72266286.81283964), sfix(-239284638.95944768), sfix(112703164.68561162), sfix(-25541467.32738066), sfix(2933695.5093185445), sfix(-137223.52832761186)]
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
        sfix(-2.0999999046325684),
        sfix(-1.0499999523162842),
        sfix(-0.5249999761581421),
        sfix(0.13124999403953552),
        sfix(0.5249999761581421),
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
        [sfix(-63596833.898079306), sfix(-188289368.5335708), sfix(-232377585.288939), sfix(-158036427.61301938), sfix(-65378856.72653997), sfix(-16949772.81535035), sfix(-2700115.7179221227), sfix(-242315.17568710257), sfix(-9398.17440598035)],
        [sfix(-19079202.687009543), sfix(-93805045.34729311), sfix(-208878919.98417905), sfix(-269986675.87612635), sfix(-215439437.5775475), sfix(-107141178.1625408), sfix(-32340451.86941293), sfix(-5430662.689593763), sfix(-389978.8388861028)],
        [sfix(-1414932.1429214166), sfix(1085108.564016173), sfix(1176199.167224651), sfix(-32449090.455128063), sfix(-88463136.06760922), sfix(-106387609.73876935), sfix(-69205904.78735222), sfix(-23795562.1899925), sfix(-3403726.70066702)],
        [sfix(-1277821.6852090287), sfix(2847552.757224252), sfix(12367042.795903608), sfix(8882373.504168218), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-1273881.2833857494), sfix(2965189.0817938466), sfix(12126273.108020147), sfix(4015701.854487203), sfix(-13412102.367774216), sfix(-7125068.274678614), sfix(4569252.537103684), sfix(8361543.464644582), sfix(-4625165.2692933185)],
        [sfix(-8610765.077867415), sfix(67876790.15590487), sfix(-231895936.4164623), sfix(510662383.6716191), sfix(-642488733.5186604), sfix(460495037.3183732), sfix(-187058892.32615042), sfix(40181996.873354636), sfix(-3550759.2615848267)],
        [sfix(3211404526.504734), sfix(-8164256836.057108), sfix(8464731253.166015), sfix(-4449636108.381767), sfix(1123052412.1512022), sfix(-35370899.53102019), sfix(-50587293.163056016), sfix(11455824.0918952), sfix(-808748.0130463192)],
        [sfix(12627820285.182001), sfix(-26931365439.00468), sfix(25057513470.744442), sfix(-13287616813.502897), sfix(4393726771.319466), sfix(-927876778.7141885), sfix(122236006.99946415), sfix(-9185657.664121415), sfix(301508.06005656713)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)]
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
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-1.0499999523162842),
        sfix(-0.26249998807907104),
        sfix(-0.06562499701976776),
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
        [sfix(2007364.3408297938), sfix(-4141349.9931728), sfix(-21176414.181712862), sfix(-26212456.006519776), sfix(-16155266.927631544), sfix(-5694140.171753386), sfix(-1168415.1267737783), sfix(-130186.49837977586), sfix(-6099.63994262003)],
        [sfix(-159099.14043477117), sfix(-1238787.8929921936), sfix(436070.8460892195), sfix(-10929765.955916), sfix(-48846617.14377461), sfix(-67703453.04553403), sfix(-42881531.753623165), sfix(-12515104.335686201), sfix(-1260991.3448023926)],
        [sfix(-125174.17235379932), sfix(-656073.2672785899), sfix(4687286.082289041), sfix(6261710.962610924), sfix(-6760098.949776311), sfix(-3987719.4486817787), sfix(15385965.165409628), sfix(17766822.984624676), sfix(6749637.654281082)],
        [sfix(-125084.78724894077), sfix(-650986.9359213659), sfix(4642985.611435935), sfix(5144312.338742241), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-124812.87818467533), sfix(-665558.2765636476), sfix(4783614.874572705), sfix(5631215.781025398), sfix(-5078481.590274925), sfix(-11688058.638010088), sfix(16510369.513308872), sfix(-7554236.203233121), sfix(1199043.6147084956)],
        [sfix(14886005.723453725), sfix(-83485621.22042924), sfix(196990893.3557788), sfix(-233579610.2185997), sfix(160309901.86169246), sfix(-66447816.562900074), sfix(16449006.652201572), sfix(-2237815.1868070774), sfix(128219.37545222718)],
        [sfix(3513677.983851195), sfix(16040205.371401573), sfix(-37237790.31668942), sfix(35233024.33782926), sfix(-17550844.55040344), sfix(5133926.378279939), sfix(-890711.2025540739), sfix(85200.15307495181), sfix(-3472.4396126736)]
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
        [sfix(-333310032.0487174), sfix(-1004120972.5906174), sfix(-1245129075.494091), sfix(-846580664.0002434), sfix(-349295925.87609893), sfix(-90203217.64841613), sfix(-14304321.268875904), sfix(-1277535.1098872533), sfix(-49308.06085155802)],
        [sfix(-228895738.8948637), sfix(-1264472419.1158206), sfix(-3013616090.407104), sfix(-4018523946.241519), sfix(-3250132656.637027), sfix(-1630289753.0041258), sfix(-496725570.70777285), sfix(-84408492.27769154), sfix(-6150486.877342295)],
        [sfix(-2999054.3610125054), sfix(-7494468.766474907), sfix(-61298767.22059715), sfix(-279170286.4027782), sfix(-592173291.6911117), sfix(-700538391.0475557), sfix(-473972258.06536424), sfix(-170906535.126597), sfix(-25491274.598903637)],
        [sfix(-1966879.171372228), sfix(6756467.049643259), sfix(25705723.63407204), sfix(16404948.97574086), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-1966879.171372228), sfix(6256422.29693373), sfix(19729421.483702525), sfix(-22728519.201192338), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-1966681.9536121245), sfix(6264155.251543609), sfix(19100512.37475), sfix(-13937122.061965164), sfix(-33195337.295990963), sfix(-27853336.737339232), sfix(150101099.3903366), sfix(-134873872.9675437), sfix(39047509.065686524)],
        [sfix(10931174.358711032), sfix(-107872473.33791767), sfix(443103731.00006455), sfix(-862559308.5703871), sfix(928017008.6434544), sfix(-586480780.6266711), sfix(217991114.79676732), sfix(-44287217.80267852), sfix(3806359.594670999)],
        [sfix(-123830751.14045656), sfix(317468272.1571642), sfix(-348850861.6229379), sfix(219094059.48067573), sfix(-85218247.77678308), sfix(21036200.625317294), sfix(-3220538.994315436), sfix(279721.2992327737), sfix(-10557.30509332664)]
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
        [sfix(-9337876.120654808), sfix(-62930978.61596331), sfix(-146587944.6884497), sfix(-155626391.26707542), sfix(-90588726.22757877), sfix(-30998436.22009816), sfix(-6238707.728044448), sfix(-684933.8831893071), sfix(-31699.94949836174)],
        [sfix(3658275.5304749985), sfix(1587332.0673492863), sfix(19521847.059109427), sfix(144588848.69064382), sfix(300474945.2666932), sfix(313907505.7247769), sfix(184946249.212571), sfix(59047457.720577426), sfix(7988034.348884148)],
        [sfix(3165287.661054604), sfix(-4980135.864671456), sfix(-18760986.304103207), sfix(17053413.85873148), sfix(34899235.715691805), sfix(-40064198.44543315), sfix(-109946520.61676286), sfix(-81347158.78449444), sfix(-21256048.265175518)],
        [sfix(3165428.437360044), sfix(-5110164.146239391), sfix(-21966507.858716533), sfix(-3556053.7391225784), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(3165428.437360044), sfix(-4890902.8900600495), sfix(-20806206.924944557), sfix(33909805.797374554), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(3165256.535955725), sfix(-4967628.123411691), sfix(-18782739.178030934), sfix(19243003.63433112), sfix(33539408.794089414), sfix(14678641.712462563), sfix(-123544719.27861904), sfix(114167165.161299), sfix(-33397303.166593432)],
        [sfix(4080535.824880208), sfix(-17194146.12109643), sfix(52645426.99832562), sfix(-219133705.7449703), sfix(530620624.2476867), sfix(-648576665.3792338), sfix(429476500.835022), sfix(-149288463.28945184), sfix(21506996.326988984)],
        [sfix(152732302.77024633), sfix(-835398563.419631), sfix(1940028726.0782845), sfix(-2532247641.3207393), sfix(2060250913.1177404), sfix(-1063676086.5403838), sfix(338128304.24857956), sfix(-60293844.22803554), sfix(4613640.252411857)],
        [sfix(-1088527559.6381135), sfix(2788215560.9504933), sfix(-3044787222.4270186), sfix(1872021414.7275276), sfix(-709293204.5939844), sfix(170024616.36467403), sfix(-25228019.784448884), sfix(2121415.326351349), sfix(-77484.20550765103)]
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
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
        sfix(-999.0),
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
        [sfix(-30178801.125584), sfix(-105560418.98223211), sfix(-145548508.9272309), sfix(-106086415.56341504), sfix(-45939103.35932645), sfix(-12296648.91771139), sfix(-2005358.159631247), sfix(-183211.7903483995), sfix(-7206.20718539817)],
        [sfix(-867254.5414721986), sfix(-3933610.7529624696), sfix(-6288639.570592954), sfix(-13103386.45944774), sfix(-20379407.374743093), sfix(-16404239.991441477), sfix(-6970313.035007034), sfix(-1516902.1341791882), sfix(-134498.6752678976)],
        [sfix(-444699.08501547854), sfix(-332883.1385700498), sfix(6225788.760863011), sfix(8811515.470239941), sfix(-2965855.3010665295), sfix(-18457827.223162275), sfix(-22562132.188324906), sfix(-13229074.204479543), sfix(-3145944.300630347)],
        [sfix(-444841.9897457379), sfix(-324731.90090336435), sfix(6219094.161169591), sfix(8515704.233028809), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-444741.7677544116), sfix(-328541.5970325494), sfix(6196112.287456986), sfix(9567394.8360671), sfix(-4791684.8107017325), sfix(335778.7301646598), sfix(-40611955.6462511), sfix(53678105.63205713), sfix(-19170986.303194284)],
        [sfix(299674.8002789778), sfix(-10257837.72096387), sfix(64134514.622046895), sfix(-183608926.5238585), sfix(397748818.8954179), sfix(-536507099.8883051), sfix(406880232.0579024), sfix(-159495503.79634577), sfix(25266321.81736244)],
        [sfix(398197417.2503766), sfix(-2276810270.954922), sfix(5584190960.29993), sfix(-7610254545.604816), sfix(6313292325.200677), sfix(-3268329759.9632406), sfix(1032889404.5361778), sfix(-182560610.89288512), sfix(13846866.652178146)],
        [sfix(-1835369786.6556456), sfix(5046140614.542869), sfix(-5946787111.79585), sfix(3938265799.931103), sfix(-1604588162.086991), sfix(412536634.41319805), sfix(-65449374.97862252), sfix(5865257.334821999), sfix(-227541.3398292029)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)]
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
        [sfix(5430032.309931843), sfix(25611281.33727641), sfix(25016793.9332869), sfix(13699475.210183442), sfix(4990209.380418857), sfix(1222539.7577538546), sfix(191656.45384308184), sfix(17264.52873564457), sfix(677.8205384168)],
        [sfix(-24913.66227894939), sfix(8849601.792284286), sfix(4701030.946263676), sfix(682222.9132252656), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-24913.66227894958), sfix(8957975.497321019), sfix(4838076.9352284055), sfix(191532.71172723625), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-22259.54542957695), sfix(8904725.763434727), sfix(5244217.111942705), sfix(-1339810.5304031677), sfix(3288785.3500959706), sfix(-4888856.088641894), sfix(3115034.1613580175), sfix(-926297.6396423017), sfix(106272.98708473999)],
        [sfix(11268495.504408749), sfix(-15756687.497479774), sfix(28325451.493503418), sfix(-12573404.776584659), sfix(3489269.653298138), sfix(-626099.3320472101), sfix(70332.20176335443), sfix(-4450.73901837739), sfix(118.77890983996)]
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
        [sfix(1875779502.119688), sfix(5246785385.998406), sfix(6286965111.834456), sfix(4229368432.42169), sfix(1749513540.4577842), sfix(456245954.98507583), sfix(73341087.51620811), sfix(6651860.599744307), sfix(260890.63195506317)],
        [sfix(-5682347.812035728), sfix(1901878.1905812025), sfix(15262232.458865646), sfix(57677830.27453368), sfix(132648880.20675088), sfix(153346959.0451736), sfix(90649421.42165625), sfix(26475304.822388507), sfix(3041070.060302188)],
        [sfix(-3824657.0382589544), sfix(11464030.759834418), sfix(22795770.383194488), sfix(11571110.030143628), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-3823651.6011196687), sfix(11509572.810419338), sfix(22869740.877087846), sfix(10298732.660310239), sfix(-17032303.512876607), sfix(-2726881.677960149), sfix(-52759065.78271277), sfix(78408089.43928999), sfix(-28831442.465339936)],
        [sfix(-19854461.47736855), sfix(163031760.13339815), sfix(-584383592.9752849), sfix(1345843547.832641), sfix(-1750076535.4866233), sfix(1306011934.1939583), sfix(-557785018.6288782), sfix(127225080.18389153), sfix(-12050082.827175263)],
        [sfix(256655092.14251068), sfix(-628441003.8239506), sfix(690921338.0738932), sfix(-421234357.88412845), sfix(160076743.936995), sfix(-38800836.4467499), sfix(5853710.789772089), sfix(-502313.94403826783), sfix(18766.57499162915)]
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
        sfix(-999.0),
        sfix(-999.0),
        sfix(-4.199999809265137),
        sfix(-2.625),
        sfix(-2.0999999046325684),
        sfix(-1.5749999284744263),
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
        [sfix(3005140748.713975), sfix(7255434142.366538), sfix(7564134537.229863), sfix(4457831670.580796), sfix(1627229026.1155698), sfix(377241030.7771964), sfix(54297365.81807225), sfix(4439696.119235041), sfix(157989.45416634378)],
        [sfix(-200908349.273783), sfix(-302373247.7681785), sfix(191361454.52042907), sfix(726249885.4805527), sfix(671113125.937112), sfix(314257630.88176906), sfix(81984118.57661377), sfix(11389879.718090177), sfix(659697.7502768483)],
        [sfix(447133998.4339267), sfix(1765791687.0058653), sfix(2945348327.508785), sfix(2660706149.512599), sfix(1393168854.3420355), sfix(417148026.50024045), sfix(63158709.90057833), sfix(2576598.5482677314), sfix(-260937.72903727787)],
        [sfix(21408282.302211963), sfix(141419364.0850609), sfix(494564759.38697994), sfix(988592049.1174273), sfix(1195572959.3257463), sfix(889647573.2959458), sfix(396650462.4296122), sfix(97003164.14621256), sfix(10004997.020565147)],
        [sfix(5723172.015629048), sfix(2062300.2676684365), sfix(-27010068.039613146), sfix(-93647721.4096957), sfix(-169665114.28608644), sfix(-181267144.63767856), sfix(-110751175.60773335), sfix(-34240502.2912147), sfix(-3850559.5425935346)],
        [sfix(5850458.250723238), sfix(4335030.018930608), sfix(-9016945.338330727), sfix(-17156190.20718866), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(5850458.250723238), sfix(4282065.266259496), sfix(-11773050.278545784), sfix(-28764736.965459127), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(5850721.312248444), sfix(4236224.504768348), sfix(-10926021.538134914), sfix(-31609447.88064084), sfix(-4785685.280279226), sfix(-9134685.18335593), sfix(163017497.00647682), sfix(-182909602.2389), sfix(59499662.39189344)],
        [sfix(3932975.007758421), sfix(29830999.463294294), sfix(-160344548.66420496), sfix(466757018.47286385), sfix(-1043545610.0410931), sfix(1376391042.4970381), sfix(-991914790.7119707), sfix(367176677.906196), sfix(-55120252.218215145)],
        [sfix(-360275275.4934273), sfix(2015062964.0996985), sfix(-4668238539.726367), sfix(5833363172.811889), sfix(-4356122901.362038), sfix(2012571150.2093627), sfix(-566467752.9506224), sfix(89339161.91141456), sfix(-6070117.719295587)],
        [sfix(-415782797.75020474), sfix(1015214725.1969149), sfix(-1083427241.9314942), sfix(656505259.746714), sfix(-247646264.53472435), sfix(59539374.778110884), sfix(-8908186.864392688), sfix(758274.211153275), sfix(-28113.14480738019)]
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
        sfix(-0.06562499701976776),
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
        [sfix(165435222.5118589), sfix(344467113.26729953), sfix(314420588.1473175), sfix(163985163.17716303), sfix(53427263.64186241), sfix(11134424.925313016), sfix(1449542.7370675497), sfix(107781.96245013869), sfix(3504.57643462104)],
        [sfix(-168922248.60996434), sfix(-454294391.8457942), sfix(-501047059.79004925), sfix(-296218337.69746387), sfix(-100945014.1963444), sfix(-19318110.031344447), sfix(-1707864.280542239), sfix(3132.68732929987), sfix(7902.9190495746)],
        [sfix(-7366602.995126769), sfix(-53445094.14571534), sfix(-187389523.13793346), sfix(-338460006.99591416), sfix(-335021154.2944974), sfix(-191911020.39822495), sfix(-63960317.63969024), sfix(-11577098.964548508), sfix(-883847.1120597709)],
        [sfix(422325.8523723899), sfix(4778760.894714232), sfix(3092809.791778165), sfix(15615474.314457076), sfix(70610403.00272207), sfix(97763284.42467731), sfix(59409282.702009894), sfix(15926426.200806057), sfix(1320899.921205216)],
        [sfix(372191.7112269619), sfix(3917768.1588773723), sfix(-3186065.6700528557), sfix(-9749248.692688605), sfix(8688857.730040027), sfix(4757149.144330301), sfix(-23679842.40867963), sfix(-24311846.791246906), sfix(-7568347.492377976)],
        [sfix(372077.199791418), sfix(3911258.6411659215), sfix(-3128472.6589712594), sfix(-8308775.269822882), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(373727.5816685968), sfix(3879730.106540519), sfix(-2801030.0361402496), sfix(-11626061.267396245), sfix(14696606.919480113), sfix(1116832.6445891897), sfix(-12297890.87895164), sfix(8368382.328722692), sfix(-1868393.8436555462)],
        [sfix(325359.2904600055), sfix(6665809.653396975), sfix(-16462552.006657662), sfix(14922100.458822276), sfix(-7488210.193730462), sfix(2241055.6175758704), sfix(-399688.8674978366), sfix(39334.91221231215), sfix(-1648.33237279593)]
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
        sfix(-0.06562499701976776),
        sfix(-0.03281249850988388),
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
        [sfix(109712113.61784169), sfix(316929830.74759656), sfix(393822276.9902846), sfix(276491130.14472365), sfix(119829106.67269336), sfix(32795923.02218773), sfix(5533940.921864566), sfix(526475.4337798015), sfix(21630.73200816702)],
        [sfix(36040538.6785225), sfix(285966404.9750854), sfix(1061283268.3420657), sfix(2031834339.5846088), sfix(2219501073.6720495), sfix(1455838910.9008298), sfix(571405391.0531487), sfix(124364780.40314306), sfix(11595740.737174233)],
        [sfix(-844609.51025354), sfix(-14102480.145481585), sfix(17434233.42404225), sfix(18834469.76036302), sfix(-98745948.18784693), sfix(-125712221.10683092), sfix(-4669632.7273459025), sfix(51178610.70597491), sfix(18846001.623189524)],
        [sfix(-840276.9783918395), sfix(-13939652.309582293), sfix(19700581.049753845), sfix(33976455.89646786), sfix(-45757326.68631332), sfix(-30438769.17304396), sfix(60121832.87592528), sfix(13219268.687588643), sfix(-44258547.90694465)],
        [sfix(-843619.4107785722), sfix(-13929767.202942256), sfix(22306763.596638218), sfix(11076614.9916284), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0), sfix(0.0)],
        [sfix(-948894.623464269), sfix(-12076281.924946135), sfix(6149762.065984035), sfix(88296620.82805397), sfix(-175398750.93522608), sfix(150726640.97054747), sfix(-62719083.815906055), sfix(8753673.312156381), sfix(870380.5984698473)],
        [sfix(33874834.52021218), sfix(-236306657.04679117), sfix(641535299.8832222), sfix(-942322457.0239503), sfix(862028192.9882365), sfix(-501552112.3150477), sfix(178825975.3285943), sfix(-35399172.52265506), sfix(2970233.2439791304)],
        [sfix(-1555100045.3916593), sfix(4428438370.414555), sfix(-5361466193.407015), sfix(3626278091.415812), sfix(-1502779705.5474658), sfix(391794201.0353), sfix(-62888301.4078033), sfix(5691776.099047764), sfix(-222692.36101386993)]
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
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)],
        [sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08), sfix(5.96e-08)]
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

def func15_kan_model_evaluate(x):
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

def func15_kan_model_evaluate_vectorized(x):
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
