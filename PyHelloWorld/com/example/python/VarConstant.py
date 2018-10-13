print ('<< 변수, 상수예제 >>')
one = 1
print(one)
two=1.2
print(two)
#두개 이상의 변수에 하나의 값을 할당
a=b=c=10
print(a)
print(b)
print(c)
# a, b 두변수에 동시에 값을 할당
a,b=100, 200
print(a)
print(b)
#a, b 두변수의 값을 바꾸기
tmp = a
a = b 
b = tmp
print('a=' + str(a))
print('b=' + str(b)) 
a = '1'
print(1 + int(a))
print('1' + a)
 