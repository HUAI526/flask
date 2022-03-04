h = float(input("請輸入身高（公分)"))
g = float(input("請輸入體重（公斤)"))

BMI = g / (h/100)**2

if BMI <18.5:
    print("BMI=", BMI, "身體狀況太輕")
elif BMI >= 18.5 and BMI <25:
    print("BMI=", BMI, "身體狀況正常")
elif BMI >= 25 and BMI <30:
    print("BMI=", BMI, "身體狀況過重")
else :
    print("BMI=", BMI, "身體狀況肥胖")
