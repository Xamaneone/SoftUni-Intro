chicken_meat = 10.35
fish_menu = 12.40
vegetable_menu = 8.15

delivery_fee = 2.50

chicken_order = int(input()) * chicken_meat
fish_order = int(input()) * fish_menu
vegetable_order = int(input()) * vegetable_menu
sum = chicken_order + fish_order + vegetable_order
dessert = sum * 0.20
print(f"Total: {sum + dessert + delivery_fee:.2f}")

