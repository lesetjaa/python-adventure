from random import randint
dice_images = ["1", "2", "3","4","5","6"]
# dice_num = randint(1, 6)
dice_num = randint(0, 5)
print(dice_images[dice_num])

"""
    To reproduce the error, test dice_num. Replace dice_num with actual values (1, 2, 3, 4, 5, 6)

    - We notice that the value 6 will produce the error on every run
    - To fix this, we should change the random number generator to 0 - 5

"""