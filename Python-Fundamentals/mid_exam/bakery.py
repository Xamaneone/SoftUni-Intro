biscuits_per_worker = int(input())
workers = int(input())
competetor_biscuits = int(input())

production_for_month = 0

daily_production = biscuits_per_worker * workers
production_for_month += daily_production * 20
for i in range(0, 10):
    production_for_month += int((biscuits_per_worker * workers) * 0.75)
print(f"You have produced {int(production_for_month)} biscuits for the past month.")
if production_for_month > competetor_biscuits:
    percentage = ((production_for_month - competetor_biscuits) / competetor_biscuits) * 100
    print(f"You produce {percentage:.2f} percent more biscuits.")
elif production_for_month < competetor_biscuits:
    percentage = ((competetor_biscuits - production_for_month) / competetor_biscuits) * 100
    print(f"You produce {(percentage):.2f} percent less biscuits.")

