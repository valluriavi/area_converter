# AvinashValluri
print(" Welcome to Area calculator 1.00 \n Enter your units as (eg:'sqkm','ha','ac','sqyd','cent')")
area = float(input('Enter area of land: '))
inu = input("Units of above area:  ")
unit = input("Units of area needed: ")

if inu == "cent":
    if unit == "ac":
        area = area / 100
        print("Area in ac", area)
    elif unit == "ha":
        area = area * 0.407
        print("Area in ha", area)
    elif unit == "sqkm":
        area = area * 0.00004
        print("Area in Square Kilometers", area)
    elif unit == "sqyd":
        area = area * 0.02066
        print("Area in Square yards", area)

    else:
        print("Units to be updated")
if inu == "ac":
    if unit == "ac":
        area = area * 100
        print("Area in cents", area)
    elif unit == "ha":
        area = area * 0.404686
        print("Area in hectares ", area)
    elif unit == "sqkm":
        area = area * 0.00404686
        print("Area in Square kilometers", area)
    elif unit == "sqyd":
        area = area * 4840
        print("Area in Square yards", area)
    else:
        print("Units will be updated")
