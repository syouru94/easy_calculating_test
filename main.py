from easy_caculating_game import practice as pr
from easy_caculating_game import testing as testing
from easy_caculating_game import firebase_helper as fh
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

while True:
    your_choice = input("請選擇 1. 練習模式 2. 測驗模式 3. 成績查詢：")
    try:
        if your_choice == "1":
            break
        elif your_choice == "2":
            break
        elif your_choice == "3":
            break
    except:
        print("別開玩笑了，請輸入正確選項")
        pass
# 練習模式
if your_choice == "1":
    while True:
        problem_type = input("請選擇 1. 加減乘除 2. 二元一次方程式：")
        try:
            if problem_type == "1":
                break
            elif problem_type == "2":
                break
        except:
            print("別開玩笑了，請輸入正確選項")
            pass
    # 加減乘除模式
    if problem_type == "1":
        while True:
            try:
                question_num = int(input("請輸入您想練習的題數："))
                break
            except ValueError:
                print("別開玩笑了，請輸入正確的數字")
        pr.practice_ASMD(question_num)
    # 二元一次方程式練習
    else:

        print("您現在使用的為: 係數皆為1-20之正整數實數，解在小數點第二位以內之方程式")
        while True:
            try:
                question_num = int(input("請輸入您想練習的題數："))
                break
            except ValueError:
                print("別開玩笑了，請輸入正確的數字")
        LE_result = pr.linear_equa(question_num)
        print("您答對的題數為： " + str(LE_result[0]))
        print("您答錯的題數為： " + str(LE_result[1]))
# 測驗模式
elif your_choice == "2":
    test_result_dict = testing.real_test()
    test_result = pd.DataFrame(test_result_dict, columns=[
                               "題型", "正確數", "錯誤數", "答對率", "得分"])

    points_list = test_result_dict["得分"]
    points = str(sum(points_list))
    print("您的得分為： " + points+" 分")
    print(test_result)

    test_result_saving = {}
# 將return之測驗dict中之value提出，整理為方面觀察與提取的形式
    test_result_list = list(test_result_dict.values())
    test_result_saving = testing.result_get(test_result_list)

    upload_grade = input("是否上傳？ y/n:")
    if upload_grade == "y":
        name = input("你的名字：")
        fh.save_data("Grades", name, test_result_saving)
        print("上傳成功!歡迎再次測驗以取得更高分數")
    else:
        print("請再多多練習")

else:

    while True:
        result_fun = input("1. 查詢個人  2. 查詢全體表現：")
        if result_fun == "1":
            break
        elif result_fun == "2":
            break
        else:
            continue
    if result_fun == "1":

        print("本功能可以自已上傳之成績，查詢到對應姓名")
        while True:
            name = input("請輸入姓名：")
            data = fh.select(name)
            if type(data) != str:
                break
            else:
                continue

        print(data)
        data＿series = pd.Series(data)
        print(data_series)
        while True:
            q_type = input("您想查詢何種題型之解果呢？")
            try:
                print(data_series[q_type])
                break
            except:
                print("請輸入有效的題型")
    else:
        total_list = fh.total_performance()
        while True:

            overall_result = input(
            "您想搜查 1. 整體加法表現 2. 整體減法表現 3. 整體乘法表現 4. 整體除法表現 5. 整體二元一次")
            if overall_result == "1":
                break
            
            elif overall_result == "2":
                break
            elif overall_result == "3":
                break
            elif overall_result == "4":
                break
            elif overall_result == "5":
                break
            else:
                print("請輸入正確選項")
                continue

        name_array = np.array(total_list[0])

        if overall_result == "1":

            testing.show_histgraph(name_array, total_list, 1)
        elif overall_result == "2":

            testing.show_histgraph(name_array, total_list, 2)
        elif overall_result == "3":

            testing.show_histgraph(name_array, total_list, 3)
        elif overall_result == "4":

            testing.show_histgraph(name_array, total_list, 4)
        elif overall_result == "5":

            testing.show_histgraph(name_array, total_list, 5)

