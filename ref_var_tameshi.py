# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 23:12:13 2022

スライス操作をすると、新しいオブジェクトが作られる。
https://qiita.com/tanuk1647/items/276d2be36f5abb8ea52e#python%E3%82%B9%E3%83%A9%E3%82%A4%E3%82%B9%E6%93%8D%E4%BD%9C%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6%E3%81%BE%E3%81%A8%E3%82%81

"""

def edit(a):
    a[0] = 12

def do_slice(t):
    a = t[:2]
    print(f"at do_slice: {a}") #スライスした時点で別オブジェクトなので元のaには影響しない
    
    b = a
    b[1] = 30
    print(f"at do_slice: {b}")
    
    print(f"{a},{b}")

a = [0,1,2]
print(f"{id(a)}")

edit(a)

print(a)

do_slice(a)

print(a)