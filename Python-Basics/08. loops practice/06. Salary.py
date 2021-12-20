n = int(input())
Salary = int(input())
Facebook = 0
Instagram = 0
Reddit = 0
for i in range(1, n + 1):
    site = input()
    if site == "Facebook":
        Facebook += 1
    if site == "Instagram":
        Instagram += 1
    if site == "Reddit":
        Reddit += 1
Salary -= (Facebook * 150) + (Instagram * 100) + (Reddit * 50)

if Salary <= 0:
    print ("You have lost your salary.")
else:
    print (Salary)