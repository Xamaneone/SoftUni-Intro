cards = input().split(" ")
shuffles = int(input())
top = cards[0]
bottom = cards[-1]

half = int(len(cards) / 2)

left_cards = []
right_cards = []
result = []
result_for_print = []
for index in range(1, half):
    left_cards.append(cards[index])
for index in range(half, half + half - 1):
    right_cards.append(cards[index])


for i in range(0, shuffles):
    result.clear()
    for index in range(len(left_cards)):
        result.append(right_cards[index])
        result.append(left_cards[index])
    half = len(right_cards)
    left_cards.clear()
    right_cards.clear()
    for index in range(0, half):
        left_cards.append(result[index])
    for index in range(half, half + half):
        right_cards.append(result[index])

result_for_print.append(top)
for index in result:
    result_for_print.append(index)
result_for_print.append(bottom)
print(result_for_print)