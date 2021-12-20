from collections import deque

def match(male, female):
    if male == female:
        return True
    return False

def divisible_by_25(male, female, males, females):
    if male % 25 == 0:
        males.pop()
        females.appendleft(female)
        return True

    elif female % 25 == 0:
        females.popleft()
        males.append(male)
        return True

    return False

def check_value_for_zero(male, female, males, females):
    if male <= 0:
        females.appendleft(female)
        return True

    elif female <= 0:
        males.append(male)
        return True

    return False


males = deque(map(int, input().split(" ")))
females = deque(map(int, input().split(" ")))

matches = 0


while males and females:
    male = males.pop()
    female = females.popleft()
    if check_value_for_zero(male, female, males, females):
        continue
    if divisible_by_25(male, female, males, females):
        continue
    if not match(male, female):
        males.append(male - 2)
        continue
    matches += 1


print(f'Matches: {matches}')

if males:
    print(f"Males left: {', '.join(list(map(str, males))[::-1])}")
else:
    print(f"Males left: none")
if females:
    print(f"Females left: {', '.join(map(str, females))}")
else:
    print(f"Females left: none")