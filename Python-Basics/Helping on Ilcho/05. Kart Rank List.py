import sys
record_name = ""
record_minutes = ""
record_seconds = ""
record_sum = sys.maxsize
Gold_numbers = 0
Silver_numbers = 0
Bronze_numbers = 0
while True:
    sum = 0
    name = input()
    if name == "Finish":
        break
    minutes = int(input())
    seconds = int(input())
    sum = (minutes * 60) + seconds
    if sum < 55:
        Gold_numbers += 1
    elif sum <= 85:
        Silver_numbers += 1
    elif sum <= 120:
        Bronze_numbers += 1
    if sum < record_sum:
        record_name = name
        record_sum = sum
        record_minutes = minutes
        record_seconds = seconds
print(f"With {record_minutes} minutes and {record_seconds} seconds {record_name} is the winner of the day!")
print(f"Today's prizes are {Gold_numbers} Gold {Silver_numbers} Silver and {Bronze_numbers} Bronze cards!")