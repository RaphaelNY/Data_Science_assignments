import random

target_number = random.randint(1, 1000)

guess_count = 0

while True:
    guess = int(input("猜数字1-1000："))
    guess_count += 1

    if guess < target_number:
        print("猜小了")
    elif guess > target_number:
        print("猜大了")
    else:
        print("恭喜你！答案是 {}。你用了 {} 次。".format(target_number, guess_count))
        break
