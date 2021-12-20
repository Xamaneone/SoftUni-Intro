deposit = float(input())
months = int(input())
lihva = float(input())
lihvaa = lihva/100
DEP_SUM = deposit + months
DEP2_SUM = deposit*lihvaa
DEP3_SUM = DEP2_SUM / 12
DEP4_SUM = DEP_SUM * DEP3_SUM
DEP5_SUM = deposit + (months*DEP3_SUM)

print (DEP5_SUM)