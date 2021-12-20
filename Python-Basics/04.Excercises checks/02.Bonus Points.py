starting_points = int(input())

if starting_points <= 100:
    bonus_points = 5

elif starting_points <= 1000:
    bonus_points = starting_points * 0.2

else:
    bonus_points = starting_points * 0.1

if starting_points % 2 == 0:
    bonus_points = bonus_points + 1
elif starting_points % 10 == 5:
    bonus_points = bonus_points + 2

print (bonus_points)
sum = bonus_points + starting_points
print (sum)