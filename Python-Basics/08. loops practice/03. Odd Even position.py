import sys
n = int(input())
odd_sum = 0
odd_min = sys.maxsize
odd_max = -sys.maxsize
even_sum = 0
even_min = sys.maxsize
even_max = -sys.maxsize


for i in range(1, n + 1):
    nah = float(input())
    if i % 2 == 1:
        odd_sum += nah
        if nah < odd_min:
            odd_min = nah
        if nah > odd_max:
            odd_max = nah
    if i % 2 == 0:
        even_sum += nah
        if nah < even_min:
            even_min = nah
        if nah > even_max:
            even_max = nah

print (f"OddSum={odd_sum:.2f},")
if odd_min == sys.maxsize:
    print (f"OddMin=No,")
else:
    print(f"OddMin={odd_min:.2f},")
if odd_max == -sys.maxsize:
    print (f"OddMax=No,")
else:
    print (f"OddMax={odd_max:.2f},")
print (f"EvenSum={even_sum:.2f},")
if even_min == sys.maxsize:
    print (f"EvenMin=No,")
else:
    print(f"EvenMin={even_min:.2f},")
if even_max == -sys.maxsize:
    print(f"EvenMax=No")
else:
    print (f"EvenMax={even_max:.2f}")
