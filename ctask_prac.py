validInputs = {
    "weight" : ["g", "kg", "mg", "lbs", "oz", "ton"], # done
    "volume" : ["ml", "l", "fl oz", "cup", "pint", "quart", "gal", "tbsp", "tsp",], # done
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
def what_to_do_if_user_is_incompetent_and_does_a_bad_input(check):
    if not(check):
        print("you incompetent user. how dare you. how dare you put an invalid response. please leave this program and come back when you want to stop acting childish.")
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
    c = (f - 32) * (9/5)
    return c
def f_k(f):
    k = (((f - 32) * (9/5)) + 273.15)
    return k
def f_f(f):
    f = f
    return f
# - - - readability break - - -
def output(func, conv):
    print(f"your output was {func(conv)}, and your input was {conv}")

got_input = False
while got_input == False:
    onboarding()
validInputStatement = f"what unit would you like to start from?\nvalid inputs are {validInputs[usrinp]}"

if usrinp == "weight":
    print(validInputStatement)
    inp2 = input().lower()
    inp3 = input("what would you like to convert to?: ").lower()
    check = False
    check2 = False
    for i in validInputs[usrinp]:
        while check == False:
            if inp2 == i:
                check = True
            else:
                check = False
                what_to_do_if_user_is_incompetent_and_does_a_bad_input(check)
        while check2 == False:
            if inp3 == i:
                check2 = True
            else:
                check2 = False
                what_to_do_if_user_is_incompetent_and_does_a_bad_input(check2)

elif usrinp == "volume":
    print(validInputStatement)
    inp2 = input().lower()
    inp3 = input("what would you like to convert to?: ").lower()
    check = False
    check2 = False
    for i in validInputs[usrinp]:
        while check == False:
            if inp2 == i:
                check = True
            else:
                check = False
                what_to_do_if_user_is_incompetent_and_does_a_bad_input(check)
        while check2 == False:
            if inp3 == i:
                check2 = True
            else:
                check2 = False
                what_to_do_if_user_is_incompetent_and_does_a_bad_input(check2)

elif usrinp == "length":
    print(validInputStatement)
    inp2 = input().lower()
    inp3 = input("what would you like to convert to?: ").lower()
    check = False
    check2 = False
    for i in validInputs[usrinp]:
        while check == False:
            if inp2 == i:
                check = True
            else:
                check = False
                what_to_do_if_user_is_incompetent_and_does_a_bad_input(check)
        while check2 == False:
            if inp3 == i:
                check2 = True
            else:
                check2 = False
                what_to_do_if_user_is_incompetent_and_does_a_bad_input(check2)

elif usrinp == "temperature":
    print(validInputStatement)
    inp2 = input().lower()
    inp3 = input("what would you like to convert to?: ").lower()
    check = False
    check2 = False
    for i in validInputs[usrinp]:
        while check == False:
            if inp2 == i:
                check = True
            else:
                check = False
                what_to_do_if_user_is_incompetent_and_does_a_bad_input(check)
        while check2 == False:
            if inp3 == i:
                check2 = True
            else:
                check2 = False
                what_to_do_if_user_is_incompetent_and_does_a_bad_input(check2)
    conv = input("what number would you like to convert from?").lower()
    if inp2 == "c" and inp3 == "c":
        output(c_c, conv)
    elif inp2 == "c" and inp3 == "k":
        c_k(conv)
    elif inp2 == "c" and inp3 == "f":
        c_f(conv)

    elif inp2 == "k" and inp3 == "c":
        k_c(conv)
    elif inp2 == "k" and inp3 == "k":
        k_k(conv)
