#第一題目
# printMany();
# // 1
# // 2
# // ...
# // 100

# for i in range(1,101):
#     print(i)
# ---------------------------------
#第二題目
# printEvery3();
# // 1
# // 4
# // ... 
# // 88

# for i in range(1,89,3):
#     print(i)
#-----------------------------------
#第三題目
# stars(3); // ***
# stars(10); // **********

# s = int(input('想要幾顆星? '))
# print('*' * s)
#-----------------------------------
#第四題目
# isUpperCase("ABCD"); // returns true
# isUpperCase(""); // returns false
# isUpperCase("aBCD"); // returns false

# s = "aBCD"
# index = ['Q','A','Z','X','S','W','E','D','C','V','F','R','T','G','B','N','H','Y','U','J','M','K','I','O','L','P']

# if s[0] not in index:
#     print('False')
# else:
#     print('True')
#-----------------------------------
#第五題目
# isAllUpperCase("ABCD"); // returns true
# isAllUpperCase(""); // returns false
# isAllUpperCase("ABCDEFGHIJKLm"); // returns false

# s = " "
# print(s.isupper())
#-----------------------------------
#第六題目
# position("abcd"); // prints -1
# position("AbcD"); // prints A 0
# position("abCD"); // prints C 2
#暴力解法
# s = "abcsDdf"
# word = ['Q','A','Z','X','S','W','E','D','C','V','F','R','T','G','B','N','H','Y','U','J','M','K','I','O','L','P']
# box=[]
# for i in word:
#     for k in s:
#         if k == i :
#             k = box.append(i)

# print(box[0] , s.index(box[0]))
#正常解法
# s = "bcsdf"

# for i in range(len(s)):
#     if s[i] not in s.upper()[i]:
#        print('-1')
#        break
#     elif s[i] == s.upper()[i]:
#        print(s[i] , i)
#        break
#-----------------------------------
#第七題目
# findSmallCount([1, 2, 3], 2); // returns 1
# findSmallCount([1, 2, 3, 4, 5], 0); // returns 0


# def findSmallCount(list , num):
#     sum = 0
#     for i in list:
#         if i == num:
#             sum += 1
#     print(sum)

# findSmallCount([1, 2, 3], 0)
#-----------------------------------
#第八題目
# findSmallerTotal([1, 2, 3], 3) // returns 3
# findSmallerTotal([1, 2, 3], 1) // returns 0
# findSmallerTotal([3, 2, 5, 8, 7], 999) // returns 25
# findSmallerTotal([3, 2, 5, 8, 7], 0) // returns 0

# def findSmallerTotal(list , num):
#     num1 = 0
#     for i in list:
#         if i < num :
#             num1 += i
#     print(num1)

# findSmallerTotal([3, 2, 5, 8, 7], 0)
#-----------------------------------
#第九題目
# findAllSmall([1, 2, 3], 10); // returns [1, 2, 3]
# findAllSmall([1, 2, 3], 2); // returns [1]
# findAllSmall([1, 3, 5, 4, 2], 4); // returns [1, 3, 2]

# def findAllSmall(list,num):
#     box = []
#     for i in list:
#         if i < num :
#             box.append(i)
#     print(box)

# findAllSmall([1, 3, 5, 4, 2], 4)
#-----------------------------------
#第十題目
# sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]); // returns 55
# sum([]); // return 0
# sum([-10, -20, -30]); // return -60

# def sum(list):
#     num = 0
#     for i in list:
#         num += i
#     print(num)

# sum([])
#-----------------------------------
#第十一題目
# stars(1);
# // *
# stars(4);
# // *
# // **
# // ***
# // ****

# def stars(num):
#     for i in range(1,num+1):
#         print('*' * i)

# stars(1)
#-----------------------------------
#第十二題目
# makeStars(1);
# // *
# makeStars(2);
# // *\n**
# makeStars(5);
# // *\n**\n***\n****\n*****

# def makeStars(num):
#     for i in range(1, num + 1):
#         if i == 1 :
#             print('*' * i)
#         else:
#             print('\n' + '*' * i)

# makeStars(5)
#-----------------------------------
#第十三題目
# stars2(1);
# // *
# stars2(2);
# // *
# // **
# // *
# stars2(3);
# // *
# // **
# // ***
# // **
# // *
# stars2(4);
# // *
# // **
# // ***
# // ****
# // ***
# // **
# // *

# def stars(num):
#     box = []
#     for i in range(num):
#         if i < num : #滿足輸入的數字以後
#             box.append(i)
#             print('*' * (i+1))
#     for i in box[::-1]: #從滿足的數字開始 -1的跑回
#         if i == 0:
#             break
#         print('*' * i)
# stars(10)
#-----------------------------------
#第十四題目
# table(3);
# // 3 x 1 = 3
# // 3 x 2 = 6
# // ...
# // 3 x 9 = 27

# def table(num):
#     for i in range(1,10):
#         print(num,'x' , i , '=' , num*i)
# table(9)
#-----------------------------------
#第十五題目
# table9to9();
# // 1 x 1 = 1
# // 1 x 2 = 2
# // 1 x 3 = 3
# // ...
# // 1 x 9 = 9
# // 2 x 1 = 2
# // 2 x 2 = 4
# // ...
# // 9 x 9 = 81

# def table9to9():
#     for i in range(1,10):
#         for k in range(1,10):
#             print(i , 'x' , k , '=' , i*k)

# table9to9()
#-----------------------------------
 #第十六題目
#  fib(0); // returns 0
# fib(1); // returns 1
# fib(2); // returns 1
# fib(3); // returns 2
# fib(8); // returns 21

#斐波那契數 第八階 = 第七階 + 第六階     前兩階數相加
# def fib(num):
#     box = [0,1]
#     if num == 0:
#         print('0')
#         return
#     elif num == 1:
#         print('1')
#         return  
#     for i in range(1,num):
#         sun = box[i] + box[i-1]
#         box.append(sun)
#         # print(i)
#         print(sun)
 
# fib(8)
#-----------------------------------