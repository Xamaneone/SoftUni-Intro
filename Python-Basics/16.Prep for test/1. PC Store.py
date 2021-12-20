processor = float(input())
video_card = float(input())
ram = float(input())
ram_counter = int(input())
discount = float(input())


#  1dollar = 1.57 lv

video_card = video_card * 1.57 - (video_card * 1.57 * discount)
processor = processor * 1.57 - (processor * 1.57 * discount)
ram = ram * 1.57
print(f"Money needed - {processor+video_card+(ram*ram_counter):.2f} leva.")