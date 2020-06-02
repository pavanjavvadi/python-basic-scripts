print("max attendence required is 75%")
a = int(input("enter no of classes held:"))
b = int(input("enter no of classes attended:"))

c = float((b/a) * 100)
round_value = round(c , 2)

print(f"percentage of classes you attended is {round_value}%")
if c < 75:
    d = 75 - c
    round_value_d = round (d , 2)
    e = int((d/100) * a)
    print(f"if you want to attend the exam you need attend {round_value_d}% of classes i.e {e} no of classes ")
    print("eligible for exam if student has medical cause")
    d = bool(input("enter yes if you have medical cause , if no directly press enter:"))
    if d == True:
        print("eligible for exam due to medical issues")
    else:
        print("not eligible")
else:
    print("eligible")