"""
برنامه ای بنویسی که نمرات سه درس یک دانش آموز را از ورودی دریافت نماید
معدل او را محاسبه کن
اگر معدلش از 90 بیشتر بود
A
را پرینت کن
اگر معدلش از 80 بیشتر بود
B
را پرینت کن
اگر معدلش از 70 بیشتر بود
C
را پرینت کن
اگر معدلش از 60 بیشتر بود
D
را پرینت کن
در غیر اینصورت 
E
را پرینت کن
"""

score1  = float(input("Enter first score: "))
score2  = float(input("Enter second score: "))
score3  = float(input("Enter third score: "))

average = (score1 + score2 + score3)/3

if average > 90:
    print("A")
elif average > 80:
    print("B")
elif average > 70:
    print("C")
elif average > 60:
    print("D")
else:
    print("E")