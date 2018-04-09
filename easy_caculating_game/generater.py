# %%
def number_generator(num1, num2):
    import random
    # 檢查輸入的數字是否會產生錯誤
    try:
        number = random.randint(num1, num2)
    except ValueError:
        print('請輸入整數之數字')
    # 檢查產生的數字是否為零
    while True:
        number = random.randint(num1, num2)
        if number != 0:
            return number
        else:
            continue
