movie = ""
total_tickets = {}
total = 0
student = 0
standard = 0
kids = 0
places = 0
Finish = False


while movie != "Finish":
    total_tickets = 0
    if Finish is True:
        break
    movie = input()
    if movie == "Finish":
        break
    places = int(input())
    while True:
        ticket = input()
        if ticket == "End":
            total_tickets = total_tickets * 100 / places
            print(f"{movie} - {total_tickets:.2f}% full.")
            break
        elif ticket == "Finish":
            Finish = True
            total_tickets = total_tickets * 100 / places
            print(f"{movie} - {total_tickets:.2f}% full.")
            break
        total_tickets += 1
        total += 1
        if ticket == "student":
            student += 1
        elif ticket == "standard":
            standard += 1
        elif ticket == "kid":
            kids += 1
        if total_tickets == places:
            total_tickets = total_tickets * 100 / places
            print(f"{movie} - {total_tickets:.2f}% full.")
            break
print (f"Total tickets: {total}")
student = student * 100 / total
standard = standard * 100 / total
kids = kids * 100 / total
print (f"{student:.2f}% student tickets.")
print (f"{standard:.2f}% standard tickets.")
print (f"{kids:.2f}% kids tickets.")