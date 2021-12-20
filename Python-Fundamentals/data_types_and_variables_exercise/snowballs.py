snowballs = int(input())
best_snow = 0
best_time = 0
best_quality = 0
best_value = 0
for i in range(1, snowballs + 1):
    snow = int(input())
    time = int(input())
    quality = int(input())
    value = (snow / time) ** quality
    if value > best_value:
        best_snow = snow
        best_time = time
        best_quality = quality
        best_value = value
print(f"{best_snow} : {best_time} = {int(best_value)} ({best_quality})")