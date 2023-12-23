#計算一時
k1 = 0
k2 = 0 
k_result = 0

# 計算方法
keisan = ["和","差","乗","商","累乗"]
for i in range(len(keisan)):
    print(keisan[i] + str(i))

choice = int(input("計算方法をお選びください"))

k1 = int(input("一つ目の数を入力"))

k2 = int(input("二つ目の数を入力"))
#計算分岐
if choice == 0:
    print("タス")
    k_result = k1 + k2
elif choice == 1:
    print("ヒク")
    k_result = k1 - k2
    
elif choice == 2:
    print("カケル")
    k_result = k1 * k2
elif choice == 3:
    print("ワル")
    k_result = k1 / k2
elif choice == 4:
    print("累乗")
    if k2 == 1:
        k_result = k1
    elif k2 == 0:
        k_result = 0
    else:
        k_result += k1
        for i in range(k2 - 1):
            k_result *= k1

print("計算結果" + str(k_result))

