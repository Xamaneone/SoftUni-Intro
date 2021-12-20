qgodi_cena = float(input())
bananas = float(input())
portokali = float(input())
malini = float(input())
qgodi = float(input())

malini_price = qgodi_cena/2
portokali_price = malini_price - (malini_price * 0.4)
bananas_price = malini_price - (malini_price * 0.8)

malini_sum = malini * malini_price
portokali_sum = portokali * portokali_price
banani_sum = bananas * bananas_price
qgodi_sum = qgodi * qgodi_cena
sum = malini_sum + portokali_sum + banani_sum + qgodi_sum
print (sum)

