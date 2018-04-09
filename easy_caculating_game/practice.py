from easy_caculating_game import caculator as ca
from easy_caculating_game import generater as ge
import numpy as np
import random
# 請使用者輸入欲產生問題之範圍，並轉換為整數值
def ans_input():
    while True:
        try:
            ans = float(input("您的答案："))
            break
        except ValueError:
            print("請輸入有效數字，別輕易放棄")
    return ans

def practice_ASMD(question_num):

    string_range = "請指定所出數字之範圍"
    print(string_range)
    while True:

        try:
            num1 = int(input("範圍之最小值為："))
            num2 = int(input("範圍之最大值為："))
            if num1 < num2:
                break
        except ValueError:
            print("別開玩笑了，請輸入正確的數字")
# 請使用者選擇要「產生的問題類型
    question = "請鍵入想產生的問題組合： 1. 全為加法 2. 全為減法 3. 全為乘法 4. 全為除法 5. 加法與減法 6. 加法與乘法 7. 加法與除法 8. 減法與乘法 9. 減法與除法 10.乘法與除法 11.隨機"
    print(question)
    while True:
        your_choice = input("您的選擇：")
        try:
            if your_choice == "1":
                break
            elif your_choice == "2":
                break
            elif your_choice == "3":
                break
            elif your_choice == "4":
                break
            elif your_choice == "5":
                break
            elif your_choice == "6":
                break
            elif your_choice == "7":
                break
            elif your_choice == "8":
                break
            elif your_choice == "9":
                break
            elif your_choice == "10":
                break
            elif your_choice == "11":
                break

        except:
            print("別開玩笑了，請輸入1~7之數字")
            pass


# 問題產生！




# 1. 全為加法
    if your_choice == "1":
        right_ans = 0
        wrong_ans = 0
        for i in range(1, question_num+1):
            number1 = ge.number_generator(num1, num2)
            number2 = ge.number_generator(num1, num2)
            print("題目 "+str(i) + ": "+ca.addition_generator(number1, number2))
        # while True:
        # try:
        # e=int(input("您的答案："))
        # break
        # except ValueError:
        # print("請輸入有效數字，別輕易放棄")
            ans = ans_input()
            if ans == ca.addition_check(number1, number2):
                right_ans += 1
            else:
                wrong_ans += 1
# 2. 全為減法
    elif your_choice == "2":
        right_ans = 0
        wrong_ans = 0
        for i in range(1, question_num+1):
            number1 = ge.number_generator(num1, num2)
            number2 = ge.number_generator(num1, num2)
            print("題目 "+str(i) + ": "+ca.substraction_generator(number1, number2))
            ans = ans_input()
            if ans == ca.substraction_check(number1, number2):
                right_ans += 1
            else:
                wrong_ans += 1
# 3. 全為乘法
    elif your_choice == "3":
        right_ans = 0
        wrong_ans = 0
        for i in range(1, question_num+1):
            number1 = ge.number_generator(num1, num2)
            number2 = ge.number_generator(num1, num2)
            print("題目 "+str(i) + ": " +
                  ca.multiplication_generator(number1, number2))
            ans = ans_input()
            if ans == ca.multiplication_check(number1, number2):
                right_ans += 1
            else:
                wrong_ans += 1

    # 4. 全為除法
    elif your_choice == "4":
        right_ans = 0
        wrong_ans = 0
        for i in range(1, question_num+1):
            while True:
                number1 = ge.number_generator(num1, num2)
                number2 = ge.number_generator(num1, num2)
                while True:
                    try:
                        answer = float(str(number1))/float(str(number2))
                        break
                    except ValueError:
                        continue

                if float(answer)-round(float(answer), 2) == 0.0:
                    break
                else:
                    continue
            print("題目 "+str(i) + ": "+ca.division_generator(number1, number2))
            ans = ans_input()
            if ans == answer:
                right_ans += 1
            else:
                wrong_ans += 1


# 5. 加減
    elif your_choice == "5":
        right_ans = 0
        wrong_ans = 0
        for i in range(1, question_num+1):
            number1 = ge.number_generator(num1, num2)
            number2 = ge.number_generator(num1, num2)
            a = random.randint(1, 100)
            if a < 50:
                print("題目 "+str(i) + ": " +
                      ca.addition_generator(number1, number2))
                ans = ans_input()
                if ans == ca.addition_check(number1, number2):
                    right_ans += 1
                else:
                    wrong_ans += 1
            if a >= 50:
                print("題目 "+str(i) + ": " +
                      ca.substraction_generator(number1, number2))
                ans = ans_input()
                if ans == ca.substraction_check(number1, number2):
                    right_ans += 1
                else:
                    wrong_ans += 1
# 6. 加乘
    elif your_choice == "6":
        right_ans = 0
        wrong_ans = 0
        for i in range(1, question_num+1):
            number1 = ge.number_generator(num1, num2)
            number2 = ge.number_generator(num1, num2)
            a = random.randint(1, 100)
            if a < 50:
                print("題目 "+str(i) + ": " +
                      ca.addition_generator(number1, number2))
                ans = ans_input()
                if ans == ca.addition_check(number1, number2):
                    right_ans += 1
                else:
                    wrong_ans += 1
            if a >= 50:
                print("題目 "+str(i) + ": " +
                      ca.multiplication_generator(number1, number2))
                ans = ans_input()
                if ans == ca.multiplication_check(number1, number2):
                    right_ans += 1
                else:
                    wrong_ans += 1
# 7. 加除
    elif your_choice == "7":
        right_ans = 0
        wrong_ans = 0
        for i in range(1, question_num+1):
            number1 = ge.number_generator(num1, num2)
            number2 = ge.number_generator(num1, num2)
            a = random.randint(1, 100)
            if a > 50:
                print("題目 "+str(i) + ": " +
                      ca.addition_generator(number1, number2))
                ans = ans_input()
                if ans == ca.addition_check(number1, number2):
                    right_ans += 1
                else:
                    wrong_ans += 1

            else:
                while True:
                    number1 = ge.number_generator(num1, num2)
                    number2 = ge.number_generator(num1, num2)
                    while True:
                        try:
                            answer = number1/number2
                            break
                        except ValueError:
                            continue
                    value = number1/number2
                    if float(value)-round(float(value), 2) == 0.0:
                        break
                    else:
                        continue
                print("題目 "+str(i) + ": " +
                      ca.division_generator(number1, number2))
                ans = ans_input()
                if ans == answer:
                    right_ans += 1
                else:
                    wrong_ans += 1


# 8. 減乘
    elif your_choice == "8":
        right_ans = 0
        wrong_ans = 0
        for i in range(1, question_num+1):
            number1 = ge.number_generator(num1, num2)
            number2 = ge.number_generator(num1, num2)
            a = random.randint(1, 100)
            if a < 50:
                print("題目 "+str(i) + ": " +
                      ca.substraction_generator(number1, number2))
                ans = ans_input()
                if ans == ca.addition_check(number1, number2):
                    right_ans += 1
                else:
                    wrong_ans += 1
            if a >= 50:
                print("題目 "+str(i) + ": " +
                      ca.multiplication_generator(number1, number2))
                ans = ans_input()
                if ans == ca.multiplication_check(number1, number2):
                    right_ans += 1
                else:
                    wrong_ans += 1
# 9. 減除
    elif your_choice == "9":
        right_ans = 0
        wrong_ans = 0
        for i in range(1, question_num+1):
            number1 = ge.number_generator(num1, num2)
            number2 = ge.number_generator(num1, num2)
            a = random.randint(1, 100)
            if a > 50:
                print("題目 "+str(i) + ": " +
                      ca.substraction_generator(number1, number2))
                ans = ans_input()
                if ans == ca.substraction_check(number1, number2):
                    right_ans += 1
                else:
                    wrong_ans += 1

            else:
                while True:
                    number1 = ge.number_generator(num1, num2)
                    number2 = ge.number_generator(num1, num2)
                    while True:
                        try:
                            answer = number1/number2
                            break
                        except ValueError:
                            continue
                    value = number1/number2
                    if float(value)-round(float(value), 2) == 0.0:
                        break
                    else:
                        continue
                print("題目 "+str(i) + ": " +
                      ca.division_generator(number1, number2))
                ans = ans_input()
                if ans == answer:
                    right_ans += 1
                else:
                    wrong_ans += 1
# 10. 乘除
    elif your_choice == "10":
        right_ans = 0
        wrong_ans = 0
        for i in range(1, question_num+1):
            number1 = ge.number_generator(num1, num2)
            number2 = ge.number_generator(num1, num2)
            a = random.randint(1, 100)
            if a > 50:
                print("題目 "+str(i) + ": " +
                      ca.multiplication_generator(number1, number2))
                ans = ans_input()
                if ans == ca.addition_check(number1, number2):
                    right_ans += 1
                else:
                    wrong_ans += 1

            else:
                while True:
                    number1 = ge.number_generator(num1, num2)
                    number2 = ge.number_generator(num1, num2)
                    while True:
                        try:
                            answer = number1/number2

                            break
                        except ValueError:
                            continue
                    value = number1/number2
                    if float(value)-round(float(value), 2) == 0.0:
                        break
                    else:
                        continue
                print("題目 "+str(i) + ": " +
                      ca.division_generator(number1, number2))
                ans = ans_input()
                if ans == answer:
                    right_ans += 1
                else:
                    wrong_ans += 1
# 11. 加減乘除
    elif your_choice == "11":
        right_ans = 0
        wrong_ans = 0
        for i in range(1, question_num+1):
            number1 = ge.number_generator(num1, num2)
            number2 = ge.number_generator(num1, num2)
            a = random.randint(1, 100)
            if a < 25:
                print("題目 "+str(i) + ": " +
                      ca.substraction_generator(number1, number2))
                ans = ans_input()
                if ans == ca.addition_check(number1, number2):
                    right_ans += 1
                else:
                    wrong_ans += 1
            elif 50 > a >= 25:
                print("題目 "+str(i) + ": " +
                      ca.multiplication_generator(number1, number2))
                ans = ans_input()
                if ans == ca.multiplication_check(number1, number2):
                    right_ans += 1
                else:
                    wrong_ans += 1
            elif 75 > a >= 50:
                while True:
                    number1 = ge.number_generator(num1, num2)
                    number2 = ge.number_generator(num1, num2)
                    while True:
                        try:
                            answer = number1/number2
                            break
                        except ValueError:
                            continue
                    value = number1/number2
                    if float(value)-round(float(value), 2) == 0.0:
                        break
                    else:
                        continue
                print("題目 "+str(i) + ": " +
                      ca.division_generator(number1, number2))
                ans = ans_input()
                if ans == answer:
                    right_ans += 1
                else:
                    wrong_ans += 1

            else:
                print("題目 "+str(i) + ": " +
                      ca.addition_generator(number1, number2))
                ans = ans_input()
                if ans == ca.addition_check(number1, number2):
                    right_ans += 1
                else:
                    wrong_ans += 1

    print("您答對的題數為：" + str(right_ans))
    print("您答錯的題數為：" + str(wrong_ans))

    # 二元一次方程式練習


def linear_equa(question_num):
    right_ans = 0
    wrong_ans = 0

    for i in range(1, question_num+1):
        while True:
            number1 = str(random.randint(1, 20))
            number2 = str(random.randint(1, 20))
            number3 = str(random.randint(1, 20))
            number4 = str(random.randint(1, 20))
            number5 = str(random.randint(1, 20))
            number6 = str(random.randint(1, 20))
            A = np.mat(number1+","+number2+";"+number3+","+number4)
            b = np.mat(number5+","+number6).T
            while True:
                try:
                    result = np.linalg.solve(A, b)
                    break
                except Exception:
                    number1 = str(random.randint(1, 20))
                    number2 = str(random.randint(1, 20))
                    number3 = str(random.randint(1, 20))
                    number4 = str(random.randint(1, 20))
                    A = np.mat(number1+","+number2+";"+number3+","+number4)

            if (str(float(result[0])-round(float(result[0]), 2)) == "0.0") and (str(float(result[1])-round(float(result[1]), 2)) == "0.0"):
                break
            else:
                continue
        print("題目 "+str(i) + ": ")
        print(number1+"x+"+number2+"y="+number5)
        print(number3+"x+"+number4+"y="+number6)


        print("x為：")
        x_ans = ans_input()
        print("y為：")
        y_ans = ans_input()

        if x_ans == float(result[0]) and y_ans == float(result[1]):
            right_ans += 1
        else:
            wrong_ans += 1
        # print(float(result[0]))
        # print(float(result[1]))

    return[right_ans,wrong_ans]
