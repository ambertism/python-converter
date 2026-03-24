validInputs = {
    "weight" : ["g", "kg", "mg", "lbs", "oz", "ton"], # done
    "volume" : ["ml", "l", "floz", "cup", "pint", "quart", "gal", "tbsp", "tsp",], # done
    "length" : ["in", "cm", "m", "km", "ft", "mi", "yd", "mm", "ly",], # done
    "temperature" : ["c", "k", "f",] # done
}
def onboarding():
    global usrinp
    global got_input
    print("hello!")
    print("this is a program which will convert common units to other common units.")
    print("what would you like to convert?")
    print("valid options = 'weight', 'volume', 'length', 'temperature'")
    usrinp = input().lower()
    if usrinp == "weight" or usrinp == "volume" or usrinp == "temperature" or usrinp == "length":
        check = True
        what_to_do_if_user_is_incompetent_and_does_a_bad_input(check)
        got_input = True
    else:
        check = False
        got_input = False
        what_to_do_if_user_is_incompetent_and_does_a_bad_input(check)
def what_to_do_if_user_is_incompetent_and_does_a_bad_input(check, valid_options=None):
    if not(check):
        print("you incompetent user. how dare you. how dare you put an invalid response. please leave this program and come back when you want to stop acting childish.")
        if valid_options:
            for option in valid_options:
                print(f"  - {option}")
        exit(code = "i dont like u")
    elif check:
        print("thank you for putting a valid input.")
# - - - - - -
#  WEIGHT
# - - - - - -
def g_g(g):
    g = g
    return g
def g_kg(g):
    kg = g / 1000
    return kg
def g_mg(g):
    mg = g * 1000
    return mg
def g_lbs(g):
    lbs = g / 453.592
    return lbs
def g_oz(g):
    oz = g / 28.3495
    return oz
def g_ton(g):
    ton = g / 907185
    return ton
# - - - readability break - - -
def kg_g(kg):
    g = kg * 1000
    return g
def kg_kg(kg):
    kg = kg
    return kg
def kg_mg(kg):
    mg = kg * 1000000
    return mg
def kg_lbs(kg):
    lbs = kg * 2.20462
    return lbs
def kg_oz(kg):
    oz = kg * 35.274
    return oz
def kg_ton(kg):
    ton = kg / 907.185
    return ton
# - - - readability break - - -
def mg_g(mg):
    g = mg / 1000
    return g
def mg_kg(mg):
    kg = mg / 1000000
    return kg
def mg_mg(mg):
    mg = mg
    return mg
def mg_lbs(mg):
    lbs = mg / 453592
    return lbs
def mg_oz(mg):
    oz = mg / 28349.5
    return oz
def mg_ton(mg):
    ton = mg / 907185000
    return ton
# - - - readability break - - -
def lbs_g(lbs):
    g = lbs * 453.592
    return g
def lbs_kg(lbs):
    kg = lbs / 2.20462
    return kg
def lbs_mg(lbs):
    mg = lbs * 453592
    return mg
def lbs_lbs(lbs):
    lbs = lbs
    return lbs
def lbs_oz(lbs):
    oz = lbs * 16
    return oz
def lbs_ton(lbs):
    ton = lbs / 2000
    return ton
# - - - readability break - - -
def oz_g(oz):
    g = oz * 28.3495
    return g
def oz_kg(oz):
    kg = oz / 35.274
    return kg
def oz_mg(oz):
    mg = oz * 28349.5
    return mg
def oz_lbs(oz):
    lbs = oz / 16
    return lbs
def oz_oz(oz):
    oz = oz
    return oz
def oz_ton(oz):
    ton = oz / 32000
    return ton
# - - - readability break - - -
def ton_g(ton):
    g = ton * 907185
    return g
def ton_kg(ton):
    kg = ton * 907.185
    return kg
def ton_mg(ton):
    mg = ton * 907185000
    return mg
def ton_lbs(ton):
    lbs = ton * 2000
    return lbs
def ton_oz(ton):
    oz = ton * 32000
    return oz
def ton_ton(ton):
    ton = ton
    return ton
# - - - readability break - - -

# - - - - - -
# VOLUME
# - - - - - -
def ml_ml(ml):
    ml = ml
    return ml
def ml_l(ml):
    l = ml / 1000
    return l
def ml_floz(ml):
    floz = ml / 29.5735
    return floz
def ml_cup(ml):
    cup = ml / 236.588
    return cup
def ml_pint(ml):
    pint = ml / 473.176
    return pint
def ml_quart(ml):
    quart = ml / 946.353
    return quart
def ml_gal(ml):
    gal = ml / 3785.41
    return gal
def ml_tbsp(ml):
    tbsp = ml / 14.7868
    return tbsp
def ml_tsp(ml):
    tsp = ml / 4.92892
    return tsp
# - - - readability break - - -
def l_ml(l):
    ml = l * 1000
    return ml
def l_l(l):
    l = l
    return l
def l_floz(l):
    floz = l * 33.814
    return floz
def l_cup(l):
    cup = l * 4.22675
    return cup
def l_pint(l):
    pint = l * 2.11338
    return pint
def l_quart(l):
    quart = l * 1.05669
    return quart
def l_gal(l):
    gal = l / 3.78541
    return gal
def l_tbsp(l):
    tbsp = l * 67.628
    return tbsp
def l_tsp(l):
    tsp = l * 202.884
    return tsp
# - - - readability break - - -
def floz_ml(floz):
    ml = floz * 29.5735
    return ml
def floz_l(floz):
    l = floz / 33.814
    return l
def floz_floz(floz):
    floz = floz
    return floz
def floz_cup(floz):
    cup = floz / 8
    return cup
def floz_pint(floz):
    pint = floz / 16
    return pint
def floz_quart(floz):
    quart = floz / 32
    return quart
def floz_gal(floz):
    gal = floz / 128
    return gal
def floz_tbsp(floz):
    tbsp = floz * 2
    return tbsp
def floz_tsp(floz):
    tsp = floz * 6
    return tsp
# - - - readability break - - -
def cup_ml(cup):
    ml = cup * 236.588
    return ml
def cup_l(cup):
    l = cup / 4.22675
    return l
def cup_floz(cup):
    floz = cup * 8
    return floz
def cup_cup(cup):
    cup = cup
    return cup
def cup_pint(cup):
    pint = cup / 2
    return pint
def cup_quart(cup):
    quart = cup / 4
    return quart
def cup_gal(cup):
    gal = cup / 16
    return gal
def cup_tbsp(cup):
    tbsp = cup * 16
    return tbsp
def cup_tsp(cup):
    tsp = cup * 48
    return tsp
# - - - readability break - - -
def pint_ml(pint):
    ml = pint * 473.176
    return ml
def pint_l(pint):
    l = pint / 2.11338
    return l
def pint_floz(pint):
    floz = pint * 16
    return floz
def pint_cup(pint):
    cup = pint * 2
    return cup
def pint_pint(pint):
    pint = pint
    return pint
def pint_quart(pint):
    quart = pint / 2
    return quart
def pint_gal(pint):
    gal = pint / 8
    return gal
def pint_tbsp(pint):
    tbsp = pint * 32
    return tbsp
def pint_tsp(pint):
    tsp = pint * 96
    return tsp
# - - - readability break - - -
def quart_ml(quart):
    ml = quart * 946.353
    return ml
def quart_l(quart):
    l = quart / 1.05669
    return l
def quart_floz(quart):
    floz = quart * 32
    return floz
def quart_cup(quart):
    cup = quart * 4
    return cup
def quart_pint(quart):
    pint = quart * 2
    return pint
def quart_quart(quart):
    quart = quart
    return quart
def quart_gal(quart):
    gal = quart / 4
    return gal
def quart_tbsp(quart):
    tbsp = quart * 64
    return tbsp
def quart_tsp(quart):
    tsp = quart * 192
    return tsp
# - - - readability break - - -
def gal_ml(gal):
    ml = gal * 3785.41
    return ml
def gal_l(gal):
    l = gal * 3.78541
    return l
def gal_floz(gal):
    floz = gal * 128
    return floz
def gal_cup(gal):
    cup = gal * 16
    return cup
def gal_pint(gal):
    pint = gal * 8
    return pint
def gal_quart(gal):
    quart = gal * 4
    return quart
def gal_gal(gal):
    gal = gal
    return gal
def gal_tbsp(gal):
    tbsp = gal * 256
    return tbsp
def gal_tsp(gal):
    tsp = gal * 768
    return tsp
# - - - readability break - - -
def tbsp_ml(tbsp):
    ml = tbsp * 14.7868
    return ml
def tbsp_l(tbsp):
    l = tbsp / 67.628
    return l
def tbsp_floz(tbsp):
    floz = tbsp / 2
    return floz
def tbsp_cup(tbsp):
    cup = tbsp / 16
    return cup
def tbsp_pint(tbsp):
    pint = tbsp / 32
    return pint
def tbsp_quart(tbsp):
    quart = tbsp / 64
    return quart
def tbsp_gal(tbsp):
    gal = tbsp / 256
    return gal
def tbsp_tbsp(tbsp):
    tbsp = tbsp
    return tbsp
def tbsp_tsp(tbsp):
    tsp = tbsp * 3
    return tsp
# - - - readability break - - -
def tsp_ml(tsp):
    ml = tsp * 4.92892
    return ml
def tsp_l(tsp):
    l = tsp / 202.884
    return l
def tsp_floz(tsp):
    floz = tsp / 6
    return floz
def tsp_cup(tsp):
    cup = tsp / 48
    return cup
def tsp_pint(tsp):
    pint = tsp / 96
    return pint
def tsp_quart(tsp):
    quart = tsp / 192
    return quart
def tsp_gal(tsp):
    gal = tsp / 768
    return gal
def tsp_tbsp(tsp):
    tbsp = tsp / 3
    return tbsp
def tsp_tsp(tsp):
    tsp = tsp
    return tsp
# - - - readability break - - -

# - - - - - -
#  LENGTH
# - - - - - -
def in_in(inches):
    inches = inches
    return inches
def in_cm(inches):
    cm = inches * 2.54
    return cm
def in_m(inches):
    m = inches / 39.37
    return m
def in_km(inches):
    km = inches / 39370
    return km
def in_ft(inches):
    ft = inches / 12
    return ft
def in_mi(inches):
    mi = inches / 63360
    return mi
def in_yd(inches):
    yd = inches / 36
    return yd
def in_mm(inches):
    mm = inches * 25.4
    return mm
def in_ly(inches):
    ly = inches / 372500000000000000000
    return ly
# - - - readability break - - -
def cm_in(cm):
    inches = cm / 2.54
    return inches
def cm_cm(cm):
    cm = cm
    return cm
def cm_m(cm):
    m = cm / 100
    return m
def cm_km(cm):
    km = cm / 100000
    return km
def cm_ft(cm):
    ft = cm / 30.48
    return ft
def cm_mi(cm):
    mi = cm / 160900
    return mi
def cm_yd(cm):
    yd = cm / 91.44
    return yd
def cm_mm(cm):
    mm = cm * 10
    return mm
def cm_ly(cm):
    ly = cm / 946100000000000000
    return ly
# - - - readability break - - -
def m_in(m):
    inches = m * 39.37
    return inches
def m_cm(m):
    cm = m * 100
    return cm
def m_m(m):
    m = m
    return m
def m_km(m):
    km = m / 1000
    return km
def m_ft(m):
    ft = m * 3.281
    return ft
def m_mi(m):
    mi = m / 1609
    return mi
def m_yd(m):
    yd = m * 1.094
    return yd
def m_mm(m):
    mm = m * 1000
    return mm
def m_ly(m):
    ly = m / 9461000000000000
    return ly
# - - - readability break - - -
def km_in(km):
    inches = km * 39370
    return inches
def km_cm(km):
    cm = km * 100000
    return cm
def km_m(km):
    m = km * 1000
    return m
def km_km(km):
    km = km
    return km
def km_ft(km):
    ft = km * 3281
    return ft
def km_mi(km):
    mi = km / 1.609
    return mi
def km_yd(km):
    yd = km * 1094
    return yd
def km_mm(km):
    mm = km * 1000000
    return mm
def km_ly(km):
    ly = km / 9461000000000
    return ly
# - - - readability break - - -
def ft_in(ft):
    inches = ft * 12
    return inches
def ft_cm(ft):
    cm = ft * 30.48
    return cm
def ft_m(ft):
    m = ft / 3.281
    return m
def ft_km(ft):
    km = ft / 3281
    return km
def ft_ft(ft):
    ft = ft
    return ft
def ft_mi(ft):
    mi = ft / 5280
    return mi
def ft_yd(ft):
    yd = ft / 3
    return yd
def ft_mm(ft):
    mm = ft * 304.8
    return mm
def ft_ly(ft):
    ly = ft / 31040000000000000
    return ly
# - - - readability break - - -
def mi_in(mi):
    inches = mi * 63360
    return inches
def mi_cm(mi):
    cm = mi * 160900
    return cm
def mi_m(mi):
    m = mi * 1609
    return m
def mi_km(mi):
    km = mi * 1.609
    return km
def mi_ft(mi):
    ft = mi * 5280
    return ft
def mi_mi(mi):
    mi = mi
    return mi
def mi_yd(mi):
    yd = mi * 1760
    return yd
def mi_mm(mi):
    mm = mi * 1609000
    return mm
def mi_ly(mi):
    ly = mi / (5879000000000)
    return ly
# - - - readability break - - -
def yd_in(yd):
    inches = yd * 36
    return inches
def yd_cm(yd):
    cm = yd * 91.44
    return cm
def yd_m(yd):
    m = yd / 1.094
    return m
def yd_km(yd):
    km = yd / 1094
    return km
def yd_ft(yd):
    ft = yd * 3
    return ft
def yd_mi(yd):
    mi = yd / 1760
    return mi
def yd_yd(yd):
    yd = yd
    return yd
def yd_mm(yd):
    mm = yd * 914.4
    return mm
def yd_ly(yd):
    ly = yd / 10350000000000000
    return ly
# - - - readability break - - -
def mm_in(mm):
    inches = mm / 25.4
    return inches
def mm_cm(mm):
    cm = mm / 10
    return cm
def mm_m(mm):
    m = mm / 1000
    return m
def mm_km(mm):
    km = mm / 1000000
    return km
def mm_ft(mm):
    ft = mm / 304.8
    return ft
def mm_mi(mm):
    mi = mm / 1609000
    return mi
def mm_yd(mm):
    yd = mm / 914.4
    return yd
def mm_mm(mm):
    mm = mm
    return mm
def mm_ly(mm):
    ly = mm / 9461000000000000000
    return ly
# - - - readability break - - -
def ly_in(ly):
    inches = ly * 372500000000000000
    return inches
def ly_cm(ly):
    cm = ly * 946100000000000000
    return cm
def ly_m(ly):
    m = ly * 9461000000000000
    return m
def ly_km(ly):
    km = ly * 9461000000000
    return km
def ly_ft(ly):
    ft = ly * 31040000000000000
    return ft
def ly_mi(ly):
    mi = ly * 5879000000000
    return mi
def ly_yd(ly):
    yd = ly * 10350000000000000
    return yd
def ly_mm(ly):
    mm = ly * 9461000000000000000
    return mm
def ly_ly(ly):
    ly = ly
    return ly
# - - - readability break - - -

# - - - - - -
# TEMPERATURE
# - - - - - -
def c_c(c):
    c = c
    return c
def c_k(c):
    k = c + 273.15
    return k
def c_f(c):
    f = ((c * (9/5)) + 32)
    return f
# - - - readability break - - -
def k_c(k):
    c = k - 273.15
    return c
def k_k(k):
    k = k
    return k
def k_f(k):
    f = (((k - 273.15) * (9/5)) + 32)
    return f
# - - - readability break - - -
def f_c(f):
    c = (f - 32) * (5/9)
    return c
def f_k(f):
    k = (((f - 32) * (9/5)) + 273.15)
    return k
def f_f(f):
    f = f
    return f
# - - - readability break - - -
def output(func, conv):
    conv = float(conv)
    print(f"your output was {func(conv)}, and your input was {conv}")

got_input = False
while got_input == False:
    onboarding()
validInputStatement = f"what unit would you like to start from?\nvalid inputs are {validInputs[usrinp]}"

if usrinp == "weight":
    print(validInputStatement)
    inp2 = input().lower()
    inp3 = input("what would you like to convert to?: ").lower()
    if inp2 not in validInputs[usrinp]:
        what_to_do_if_user_is_incompetent_and_does_a_bad_input(False)
    if inp3 not in validInputs[usrinp]:
        what_to_do_if_user_is_incompetent_and_does_a_bad_input(False)
    conv = input("what number would you like to convert from?: ")

    if inp2 == "g" and inp3 == "g":
        output(g_g, conv)
    elif inp2 == "g" and inp3 == "kg":
        output(g_kg, conv)
    elif inp2 == "g" and inp3 == "mg":
        output(g_mg, conv)
    elif inp2 == "g" and inp3 == "lbs":
        output(g_lbs, conv)
    elif inp2 == "g" and inp3 == "oz":
        output(g_oz, conv)
    elif inp2 == "g" and inp3 == "ton":
        output(g_ton, conv)

    elif inp2 == "kg" and inp3 == "g":
        output(kg_g, conv)
    elif inp2 == "kg" and inp3 == "kg":
        output(kg_kg, conv)
    elif inp2 == "kg" and inp3 == "mg":
        output(kg_mg, conv)
    elif inp2 == "kg" and inp3 == "lbs":
        output(kg_lbs, conv)
    elif inp2 == "kg" and inp3 == "oz":
        output(kg_oz, conv)
    elif inp2 == "kg" and inp3 == "ton":
        output(kg_ton, conv)

    elif inp2 == "mg" and inp3 == "g":
        output(mg_g, conv)
    elif inp2 == "mg" and inp3 == "kg":
        output(mg_kg, conv)
    elif inp2 == "mg" and inp3 == "mg":
        output(mg_mg, conv)
    elif inp2 == "mg" and inp3 == "lbs":
        output(mg_lbs, conv)
    elif inp2 == "mg" and inp3 == "oz":
        output(mg_oz, conv)
    elif inp2 == "mg" and inp3 == "ton":
        output(mg_ton, conv)

    elif inp2 == "lbs" and inp3 == "g":
        output(lbs_g, conv)
    elif inp2 == "lbs" and inp3 == "kg":
        output(lbs_kg, conv)
    elif inp2 == "lbs" and inp3 == "mg":
        output(lbs_mg, conv)
    elif inp2 == "lbs" and inp3 == "lbs":
        output(lbs_lbs, conv)
    elif inp2 == "lbs" and inp3 == "oz":
        output(lbs_oz, conv)
    elif inp2 == "lbs" and inp3 == "ton":
        output(lbs_ton, conv)

    elif inp2 == "oz" and inp3 == "g":
        output(oz_g, conv)
    elif inp2 == "oz" and inp3 == "kg":
        output(oz_kg, conv)
    elif inp2 == "oz" and inp3 == "mg":
        output(oz_mg, conv)
    elif inp2 == "oz" and inp3 == "lbs":
        output(oz_lbs, conv)
    elif inp2 == "oz" and inp3 == "oz":
        output(oz_oz, conv)
    elif inp2 == "oz" and inp3 == "ton":
        output(oz_ton, conv)

    elif inp2 == "ton" and inp3 == "g":
        output(ton_g, conv)
    elif inp2 == "ton" and inp3 == "kg":
        output(ton_kg, conv)
    elif inp2 == "ton" and inp3 == "mg":
        output(ton_mg, conv)
    elif inp2 == "ton" and inp3 == "lbs":
        output(ton_lbs, conv)
    elif inp2 == "ton" and inp3 == "oz":
        output(ton_oz, conv)
    elif inp2 == "ton" and inp3 == "ton":
        output(ton_ton, conv)

elif usrinp == "volume":
    print(validInputStatement)
    inp2 = input().lower()
    inp3 = input("what would you like to convert to?: ").lower()
    if inp2 not in validInputs[usrinp]:
        what_to_do_if_user_is_incompetent_and_does_a_bad_input(False)
    if inp3 not in validInputs[usrinp]:
        what_to_do_if_user_is_incompetent_and_does_a_bad_input(False)
    conv = input("what number would you like to convert from?: ")

    if inp2 == "ml" and inp3 == "ml":
        output(ml_ml, conv)
    elif inp2 == "ml" and inp3 == "l":
        output(ml_l, conv)
    elif inp2 == "ml" and inp3 == "floz":
        output(ml_floz, conv)
    elif inp2 == "ml" and inp3 == "cup":
        output(ml_cup, conv)
    elif inp2 == "ml" and inp3 == "pint":
        output(ml_pint, conv)
    elif inp2 == "ml" and inp3 == "quart":
        output(ml_quart, conv)
    elif inp2 == "ml" and inp3 == "gal":
        output(ml_gal, conv)
    elif inp2 == "ml" and inp3 == "tbsp":
        output(ml_tbsp, conv)
    elif inp2 == "ml" and inp3 == "tsp":
        output(ml_tsp, conv)

    elif inp2 == "l" and inp3 == "ml":
        output(l_ml, conv)
    elif inp2 == "l" and inp3 == "l":
        output(l_l, conv)
    elif inp2 == "l" and inp3 == "floz":
        output(l_floz, conv)
    elif inp2 == "l" and inp3 == "cup":
        output(l_cup, conv)
    elif inp2 == "l" and inp3 == "pint":
        output(l_pint, conv)
    elif inp2 == "l" and inp3 == "quart":
        output(l_quart, conv)
    elif inp2 == "l" and inp3 == "gal":
        output(l_gal, conv)
    elif inp2 == "l" and inp3 == "tbsp":
        output(l_tbsp, conv)
    elif inp2 == "l" and inp3 == "tsp":
        output(l_tsp, conv)

    elif inp2 == "floz" and inp3 == "ml":
        output(floz_ml, conv)
    elif inp2 == "floz" and inp3 == "l":
        output(floz_l, conv)
    elif inp2 == "floz" and inp3 == "floz":
        output(floz_floz, conv)
    elif inp2 == "floz" and inp3 == "cup":
        output(floz_cup, conv)
    elif inp2 == "floz" and inp3 == "pint":
        output(floz_pint, conv)
    elif inp2 == "floz" and inp3 == "quart":
        output(floz_quart, conv)
    elif inp2 == "floz" and inp3 == "gal":
        output(floz_gal, conv)
    elif inp2 == "floz" and inp3 == "tbsp":
        output(floz_tbsp, conv)
    elif inp2 == "floz" and inp3 == "tsp":
        output(floz_tsp, conv)

    elif inp2 == "cup" and inp3 == "ml":
        output(cup_ml, conv)
    elif inp2 == "cup" and inp3 == "l":
        output(cup_l, conv)
    elif inp2 == "cup" and inp3 == "floz":
        output(cup_floz, conv)
    elif inp2 == "cup" and inp3 == "cup":
        output(cup_cup, conv)
    elif inp2 == "cup" and inp3 == "pint":
        output(cup_pint, conv)
    elif inp2 == "cup" and inp3 == "quart":
        output(cup_quart, conv)
    elif inp2 == "cup" and inp3 == "gal":
        output(cup_gal, conv)
    elif inp2 == "cup" and inp3 == "tbsp":
        output(cup_tbsp, conv)
    elif inp2 == "cup" and inp3 == "tsp":
        output(cup_tsp, conv)

    elif inp2 == "pint" and inp3 == "ml":
        output(pint_ml, conv)
    elif inp2 == "pint" and inp3 == "l":
        output(pint_l, conv)
    elif inp2 == "pint" and inp3 == "floz":
        output(pint_floz, conv)
    elif inp2 == "pint" and inp3 == "cup":
        output(pint_cup, conv)
    elif inp2 == "pint" and inp3 == "pint":
        output(pint_pint, conv)
    elif inp2 == "pint" and inp3 == "quart":
        output(pint_quart, conv)
    elif inp2 == "pint" and inp3 == "gal":
        output(pint_gal, conv)
    elif inp2 == "pint" and inp3 == "tbsp":
        output(pint_tbsp, conv)
    elif inp2 == "pint" and inp3 == "tsp":
        output(pint_tsp, conv)

    elif inp2 == "quart" and inp3 == "ml":
        output(quart_ml, conv)
    elif inp2 == "quart" and inp3 == "l":
        output(quart_l, conv)
    elif inp2 == "quart" and inp3 == "floz":
        output(quart_floz, conv)
    elif inp2 == "quart" and inp3 == "cup":
        output(quart_cup, conv)
    elif inp2 == "quart" and inp3 == "pint":
        output(quart_pint, conv)
    elif inp2 == "quart" and inp3 == "quart":
        output(quart_quart, conv)
    elif inp2 == "quart" and inp3 == "gal":
        output(quart_gal, conv)
    elif inp2 == "quart" and inp3 == "tbsp":
        output(quart_tbsp, conv)
    elif inp2 == "quart" and inp3 == "tsp":
        output(quart_tsp, conv)

    elif inp2 == "gal" and inp3 == "ml":
        output(gal_ml, conv)
    elif inp2 == "gal" and inp3 == "l":
        output(gal_l, conv)
    elif inp2 == "gal" and inp3 == "floz":
        output(gal_floz, conv)
    elif inp2 == "gal" and inp3 == "cup":
        output(gal_cup, conv)
    elif inp2 == "gal" and inp3 == "pint":
        output(gal_pint, conv)
    elif inp2 == "gal" and inp3 == "quart":
        output(gal_quart, conv)
    elif inp2 == "gal" and inp3 == "gal":
        output(gal_gal, conv)
    elif inp2 == "gal" and inp3 == "tbsp":
        output(gal_tbsp, conv)
    elif inp2 == "gal" and inp3 == "tsp":
        output(gal_tsp, conv)

    elif inp2 == "tbsp" and inp3 == "ml":
        output(tbsp_ml, conv)
    elif inp2 == "tbsp" and inp3 == "l":
        output(tbsp_l, conv)
    elif inp2 == "tbsp" and inp3 == "floz":
        output(tbsp_floz, conv)
    elif inp2 == "tbsp" and inp3 == "cup":
        output(tbsp_cup, conv)
    elif inp2 == "tbsp" and inp3 == "pint":
        output(tbsp_pint, conv)
    elif inp2 == "tbsp" and inp3 == "quart":
        output(tbsp_quart, conv)
    elif inp2 == "tbsp" and inp3 == "gal":
        output(tbsp_gal, conv)
    elif inp2 == "tbsp" and inp3 == "tbsp":
        output(tbsp_tbsp, conv)
    elif inp2 == "tbsp" and inp3 == "tsp":
        output(tbsp_tsp, conv)

    elif inp2 == "tsp" and inp3 == "ml":
        output(tsp_ml, conv)
    elif inp2 == "tsp" and inp3 == "l":
        output(tsp_l, conv)
    elif inp2 == "tsp" and inp3 == "floz":
        output(tsp_floz, conv)
    elif inp2 == "tsp" and inp3 == "cup":
        output(tsp_cup, conv)
    elif inp2 == "tsp" and inp3 == "pint":
        output(tsp_pint, conv)
    elif inp2 == "tsp" and inp3 == "quart":
        output(tsp_quart, conv)
    elif inp2 == "tsp" and inp3 == "gal":
        output(tsp_gal, conv)
    elif inp2 == "tsp" and inp3 == "tbsp":
        output(tsp_tbsp, conv)
    elif inp2 == "tsp" and inp3 == "tsp":
        output(tsp_tsp, conv)

elif usrinp == "length":
    print(validInputStatement)
    inp2 = input().lower()
    inp3 = input("what would you like to convert to?: ").lower()
    if inp2 not in validInputs[usrinp]:
        what_to_do_if_user_is_incompetent_and_does_a_bad_input(False)
    if inp3 not in validInputs[usrinp]:
        what_to_do_if_user_is_incompetent_and_does_a_bad_input(False)
    conv = input("what number would you like to convert from?: ")

    if inp2 == "in" and inp3 == "in":
        output(in_in, conv)
    elif inp2 == "in" and inp3 == "cm":
        output(in_cm, conv)
    elif inp2 == "in" and inp3 == "m":
        output(in_m, conv)
    elif inp2 == "in" and inp3 == "km":
        output(in_km, conv)
    elif inp2 == "in" and inp3 == "ft":
        output(in_ft, conv)
    elif inp2 == "in" and inp3 == "mi":
        output(in_mi, conv)
    elif inp2 == "in" and inp3 == "yd":
        output(in_yd, conv)
    elif inp2 == "in" and inp3 == "mm":
        output(in_mm, conv)
    elif inp2 == "in" and inp3 == "ly":
        output(in_ly, conv)

    elif inp2 == "cm" and inp3 == "in":
        output(cm_in, conv)
    elif inp2 == "cm" and inp3 == "cm":
        output(cm_cm, conv)
    elif inp2 == "cm" and inp3 == "m":
        output(cm_m, conv)
    elif inp2 == "cm" and inp3 == "km":
        output(cm_km, conv)
    elif inp2 == "cm" and inp3 == "ft":
        output(cm_ft, conv)
    elif inp2 == "cm" and inp3 == "mi":
        output(cm_mi, conv)
    elif inp2 == "cm" and inp3 == "yd":
        output(cm_yd, conv)
    elif inp2 == "cm" and inp3 == "mm":
        output(cm_mm, conv)
    elif inp2 == "cm" and inp3 == "ly":
        output(cm_ly, conv)

    elif inp2 == "m" and inp3 == "in":
        output(m_in, conv)
    elif inp2 == "m" and inp3 == "cm":
        output(m_cm, conv)
    elif inp2 == "m" and inp3 == "m":
        output(m_m, conv)
    elif inp2 == "m" and inp3 == "km":
        output(m_km, conv)
    elif inp2 == "m" and inp3 == "ft":
        output(m_ft, conv)
    elif inp2 == "m" and inp3 == "mi":
        output(m_mi, conv)
    elif inp2 == "m" and inp3 == "yd":
        output(m_yd, conv)
    elif inp2 == "m" and inp3 == "mm":
        output(m_mm, conv)
    elif inp2 == "m" and inp3 == "ly":
        output(m_ly, conv)

    elif inp2 == "km" and inp3 == "in":
        output(km_in, conv)
    elif inp2 == "km" and inp3 == "cm":
        output(km_cm, conv)
    elif inp2 == "km" and inp3 == "m":
        output(km_m, conv)
    elif inp2 == "km" and inp3 == "km":
        output(km_km, conv)
    elif inp2 == "km" and inp3 == "ft":
        output(km_ft, conv)
    elif inp2 == "km" and inp3 == "mi":
        output(km_mi, conv)
    elif inp2 == "km" and inp3 == "yd":
        output(km_yd, conv)
    elif inp2 == "km" and inp3 == "mm":
        output(km_mm, conv)
    elif inp2 == "km" and inp3 == "ly":
        output(km_ly, conv)

    elif inp2 == "ft" and inp3 == "in":
        output(ft_in, conv)
    elif inp2 == "ft" and inp3 == "cm":
        output(ft_cm, conv)
    elif inp2 == "ft" and inp3 == "m":
        output(ft_m, conv)
    elif inp2 == "ft" and inp3 == "km":
        output(ft_km, conv)
    elif inp2 == "ft" and inp3 == "ft":
        output(ft_ft, conv)
    elif inp2 == "ft" and inp3 == "mi":
        output(ft_mi, conv)
    elif inp2 == "ft" and inp3 == "yd":
        output(ft_yd, conv)
    elif inp2 == "ft" and inp3 == "mm":
        output(ft_mm, conv)
    elif inp2 == "ft" and inp3 == "ly":
        output(ft_ly, conv)

    elif inp2 == "mi" and inp3 == "in":
        output(mi_in, conv)
    elif inp2 == "mi" and inp3 == "cm":
        output(mi_cm, conv)
    elif inp2 == "mi" and inp3 == "m":
        output(mi_m, conv)
    elif inp2 == "mi" and inp3 == "km":
        output(mi_km, conv)
    elif inp2 == "mi" and inp3 == "ft":
        output(mi_ft, conv)
    elif inp2 == "mi" and inp3 == "mi":
        output(mi_mi, conv)
    elif inp2 == "mi" and inp3 == "yd":
        output(mi_yd, conv)
    elif inp2 == "mi" and inp3 == "mm":
        output(mi_mm, conv)
    elif inp2 == "mi" and inp3 == "ly":
        output(mi_ly, conv)

    elif inp2 == "yd" and inp3 == "in":
        output(yd_in, conv)
    elif inp2 == "yd" and inp3 == "cm":
        output(yd_cm, conv)
    elif inp2 == "yd" and inp3 == "m":
        output(yd_m, conv)
    elif inp2 == "yd" and inp3 == "km":
        output(yd_km, conv)
    elif inp2 == "yd" and inp3 == "ft":
        output(yd_ft, conv)
    elif inp2 == "yd" and inp3 == "mi":
        output(yd_mi, conv)
    elif inp2 == "yd" and inp3 == "yd":
        output(yd_yd, conv)
    elif inp2 == "yd" and inp3 == "mm":
        output(yd_mm, conv)
    elif inp2 == "yd" and inp3 == "ly":
        output(yd_ly, conv)

    elif inp2 == "mm" and inp3 == "in":
        output(mm_in, conv)
    elif inp2 == "mm" and inp3 == "cm":
        output(mm_cm, conv)
    elif inp2 == "mm" and inp3 == "m":
        output(mm_m, conv)
    elif inp2 == "mm" and inp3 == "km":
        output(mm_km, conv)
    elif inp2 == "mm" and inp3 == "ft":
        output(mm_ft, conv)
    elif inp2 == "mm" and inp3 == "mi":
        output(mm_mi, conv)
    elif inp2 == "mm" and inp3 == "yd":
        output(mm_yd, conv)
    elif inp2 == "mm" and inp3 == "mm":
        output(mm_mm, conv)
    elif inp2 == "mm" and inp3 == "ly":
        output(mm_ly, conv)

    elif inp2 == "ly" and inp3 == "in":
        output(ly_in, conv)
    elif inp2 == "ly" and inp3 == "cm":
        output(ly_cm, conv)
    elif inp2 == "ly" and inp3 == "m":
        output(ly_m, conv)
    elif inp2 == "ly" and inp3 == "km":
        output(ly_km, conv)
    elif inp2 == "ly" and inp3 == "ft":
        output(ly_ft, conv)
    elif inp2 == "ly" and inp3 == "mi":
        output(ly_mi, conv)
    elif inp2 == "ly" and inp3 == "yd":
        output(ly_yd, conv)
    elif inp2 == "ly" and inp3 == "mm":
        output(ly_mm, conv)
    elif inp2 == "ly" and inp3 == "ly":
        output(ly_ly, conv)

elif usrinp == "temperature":
    print(validInputStatement)
    inp2 = input().lower()
    inp3 = input("what would you like to convert to?: ").lower()
    if inp2 not in validInputs[usrinp]:
        what_to_do_if_user_is_incompetent_and_does_a_bad_input(False)
    if inp3 not in validInputs[usrinp]:
        what_to_do_if_user_is_incompetent_and_does_a_bad_input(False)
    conv = input("what number would you like to convert from?: ")

    if inp2 == "c" and inp3 == "c":
        output(c_c, conv)
    elif inp2 == "c" and inp3 == "k":
        output(c_k, conv)
    elif inp2 == "c" and inp3 == "f":
        output(c_f, conv)

    elif inp2 == "k" and inp3 == "c":
        output(k_c, conv)
    elif inp2 == "k" and inp3 == "k":
        output(k_k, conv)
    elif inp2 == "k" and inp3 == "f":
        output(k_f, conv)

    elif inp2 == "f" and inp3 == "c":
        output(f_c, conv)
    elif inp2 == "f" and inp3 == "k":
        output(f_k, conv)
    elif inp2 == "f" and inp3 == "f":
        output(f_f, conv)
