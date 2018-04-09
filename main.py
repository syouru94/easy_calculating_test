from easy_caculating_game import practice as pr
from easy_caculating_game import testing as testing
from easy_caculating_game import firebase_helper as fh
import pandas as pd

while True:
    your_choice = input("請選擇 1. 練習模式 2. 測驗模式：")
    try:
        if your_choice == "1":
            break
        elif your_choice == "2":
            break
    except:
        print("別開玩笑了，請輸入正確選項")
        pass
#練習模式
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
    #加減乘除模式
    if problem_type=="1":
        while True:
            try:
                question_num = int(input("請輸入您想練習的題數："))
                break
            except ValueError:
                print("別開玩笑了，請輸入正確的數字")
        pr.practice_ASMD(question_num)
    #二元一次方程式練習
    else:

        print ("您現在使用的為: 係數皆為1-20之正整數實數，解在小數點第二位以內之方程式")
        while True:
            try:
                question_num = int(input("請輸入您想練習的題數："))
                break
            except ValueError:
                print("別開玩笑了，請輸入正確的數字")
        LE_result=pr.linear_equa(question_num)
        print("您答對的題數為： " + str(LE_result[0]))
        print("您答錯的題數為： " + str(LE_result[1]))
#測驗模式
elif your_choice=="2":
    test_result_dict=testing.real_test()
    test_result = pd.DataFrame(test_result_dict, columns=[
                               "題型", "正確數", "錯誤數", "答對率", "得分"])

    print(test_result)
    
    points_list=test_result_dict["得分"]
    points=str(sum(points_list))
    print("您的得分為： " + points+" 分")


    upload_grade=input("是否上傳？ y/n:")
    if upload_grade=="y":
        name=input("你的名字：")
        fh.save_data("Grades", name, test_result_dict)
    else:
        print("請再多多練習")



