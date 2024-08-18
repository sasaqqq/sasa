# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 07:37:53 2024

@author: Student
"""

GPA = float(input("Nhập điểm trung bình (GPA):"))
if GPA < 3.5:
    print("Học lực Kém")
elif 3.5 <= GPA < 5.0:
    print("Học lực Yếu")
elif 5.0 <= GPA < 7.0:
    print("Học lực Trung bình")
elif 7.0 <= GPA < 8.0:
    print("Học lực Khá")
elif 8.0 <= GPA < 9.0:
    print("Học lực Giỏi")
elif 9.0 <= GPA < 10:
    print("Học lực Xuất sắc")
else:
    print("Không xác định")