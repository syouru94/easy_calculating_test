from easy_caculating_game import generater as ge
from easy_caculating_game import practice as pr
from easy_caculating_game import caculator as ca
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def real_test():
    
    print("測驗內容為： 加減乘除各十題(一題2分)，加上解二元一次方程式五題(一題4分)，共100分")
    addi_right = 0
    addi_wrong = 0
    sub_right = 0
    sub_wrong = 0
    mul_right = 0
    mul_wrong = 0
    div_right = 0
    div_wrong = 0
    print("加法:")
    for i in range(1, 11):
        number1 = ge.number_generator(-10, 10)
        number2 = ge.number_generator(-10, 10)
        print("題目 "+str(i) + ": "+ca.addition_generator(number1, number2))
        ans = pr.ans_input()
        if ans == ca.addition_check(number1, number2):
            addi_right += 1
        else:
            addi_wrong += 1
    print("減法:")
    for i in range(1, 11):
        number1 = ge.number_generator(-10, 10)
        number2 = ge.number_generator(-10, 10)
        print("題目 "+str(i) + ": "+ca.substraction_generator(number1, number2))
        ans = pr.ans_input()
        if ans == ca.substraction_check(number1, number2):
            sub_right += 1
        else:
            sub_wrong += 1
    print("乘法:")
    for i in range(1, 11):
        number1 = ge.number_generator(-10, 10)
        number2 = ge.number_generator(-10, 10)
        print("題目 "+str(i) + ": "+ca.multiplication_generator(number1, number2))
        ans = pr.ans_input()
        if ans == ca.multiplication_check(number1, number2):
            mul_right += 1
        else:
            mul_wrong += 1
    print("除法")

    for i in range(1, 11):
        while True:
            number1 = ge.number_generator(-10, 10)
            number2 = ge.number_generator(-10, 10)
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
        ans = pr.ans_input()
        if ans == answer:
            div_right += 1
        else:
            div_wrong += 1
    print("解二元一次方程式")
    
    LE_result=pr.linear_equa(5)
    print("測驗結束！為您呈現結果")

#([[題型],正確數,錯誤數,答對率,得分])
    test_result＿dict={"題型":["加法題","減法題","乘法題","除法題","二元一次方程式"],
                      "正確數":[addi_right,sub_right,mul_right,div_right,LE_result[0]],
                      "錯誤數":[addi_wrong,sub_wrong,mul_wrong,div_wrong,LE_result[1]],
                      "答對率":[addi_right/10.0,sub_right/10.0,mul_right/10.0,div_right/10.0,LE_result[0]/5.0],
                      "得分":[addi_right*2,sub_right*2,mul_right*2,div_right*2,LE_result[0]*2]



    }
    #以pandas呈現
    return test_result_dict
    #分數計算
    #資料處理


def result_get(test_result_list):
    test_result_saving={}
    for i in range(0, 5):
        test_result_saving[test_result_list[0][i]] = {"正確數": (test_result_list[1][i]),
                                                      "錯誤數": (test_result_list[2][i]),
                                                      "答對率": (test_result_list[3][i]),
                                                      "得分": (test_result_list[4][i])}
    return test_result_saving

def show_histgraph(name,list,num):
    array = np.array(list[num])

    plt.bar(range(len(array)), array, tick_label=name)
    plt.show()

