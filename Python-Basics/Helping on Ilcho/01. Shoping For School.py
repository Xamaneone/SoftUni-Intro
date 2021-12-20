molivi = float(4.75)
fulmasteri = float(1.80)
skicnik = float(6.50)
tetradki = float(2.50)


molivi_number = int(input())
fulmasteri_number = int(input())
skicnik_number = int(input())
tetradki_number = int(input())

sum = (molivi*molivi_number) + (fulmasteri * fulmasteri_number) + (skicnik * skicnik_number) + (tetradki * tetradki_number)
sum -= (sum * 0.05)
print(f"Your total is {sum:.2f}lv")

