won = float(input())
months = int(input())
simple = 0.03
complex = 0.027
simple_sum = won
complex_sum = won
for i in range(0, months):
    simple_sum += won * simple
    complex_sum += complex_sum * complex
print(f"Simple interest rate: {simple_sum:.2f} lv.")
print(f"Complex interest rate: {complex_sum:.2f} lv.")
if simple_sum > complex_sum:
    print(f"Choose a simple interest rate. You will win {simple_sum-complex_sum:.2f} lv.")
elif simple_sum < complex_sum:
    print(f"Choose a complex interest rate. You will win {complex_sum-simple_sum:.2f} lv.")