# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 08:31:48 2024

@author: Student
"""
import math 
a = float(input("Nhập số thực (a): "))
b = float(input("Nhập số thực (b): "))
c = float(input("Nhập số thực (c): "))
delta= b**2-4*a*c
if delta == 0:
    x = -b/(2*a)
    print("Vậy phương trình có nghiệm kép là: ", x)
elif delta < 0:
    print("Vậy phương trình vô nghiệm")
else:
    x1= (-b + math.sqrt(delta))/(2*a)
    x2= (-b - math.sqrt(delta))/(2*a)
    print("Vậy phương trình có 2 nghiệm phân biệt là: ")
    print("x1:",x1)
    print("x2:",x2)
    