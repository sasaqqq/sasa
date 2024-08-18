# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 09:48:25 2024

@author: Student
"""

a = float(input("Số km quãng đường taxi đi được:"))
if a == 1:
    b = 20
    print("Tiền taxi: ",b ,"k")
elif a <= 3:
    b = a*13
    print("Tiền taxi: ",b ,"k")
elif a <= 8:
    b = 3*13 + (a-3)*12
    print("Tiền taxi: ",b ,"k")
elif a < 8:
    b = 3*13 + 5*12 + (a-8)*10
    print("Tiền taxi: ",b ,"k")
if b > 100:
    b = b*0.92
    print("Tiền taxi: ", b)
    