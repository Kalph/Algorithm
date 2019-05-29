
T = int(input())  # 숫자를 받아옴
g,h = 0,0   # 변수 초기화
for aaa in range(T):   # 받아온 숫자만큼 반복
    a,b = input().split()  
    c,d = input().split()  
    e,f = input().split()  
    # 문자열을 정수형으로 변환
    a=int(a)   
    b=int(b)  
    c=int(c)  
    d=int(d)  
    e=int(e)  
    f=int(f)  
    # XOR 연산 ( 같으면 0 다르면 1을 이용함 )
    g=a^c^e  
    h=b^d^f  
    print(g,h)  
    
    
    '''
    먼저 내가 처음 푼 문제에서는 XOR연산을 생각하지도 못했기에 저런 답이 나왔다  
중복을 확인하는 것을 이용해서 풀어야 한다는 생각은 났지만 비트 연산자를 저렇게 활용할 
줄은 몰랐다 처음 썻던 코드들도 정상적으로 답은 나온다 물론 알고스팟의 예문 입력만 만일
저렇게 두 수를 비교하는 방법이 안통하면 오류가 날 수 밖에 없었다는 것을 모르고 있었다.
이 답이 나온 이유는 직접 노트에 그림을 그려보면서 하다가 10진수를 차라리 2진수로 바꿔서
풀어보면 좀 더 쉽게 파악이 가능하지 않을까 그럼 비트 연산자를 이용해 보면 되지 않을까 했다 내가 제일 싫어하는 비트 연산자...

입력된 세 개의 수를  
12 10  
22 20  
32 10  
이라 가정하면 사실상 이 수들은  
1100     1010  
10110    10100  
100000  1010  
이제 이 수들을 XOR 연산한다  
1100 ^ 10110 ^ 100000 = 111010 = 26  
1010 ^ 10100 ^ 1010 = 10100 = 20  

참고한 사이트 : https://wikidocs.net/1161 - 비트 연산자에 대한 내용이 정리되어 있다.

'''

# 다른 답안

'''
def parse(x):
	x = x.split()
	return map(int, x)

def func():
	pos1 = input()
	pos2 = input()
	pos3 = input()

	x1, y1 = parse(pos1)
	x2, y2 = parse(pos2)
	x3, y3 = parse(pos3)
	x4, y4 = 0, 0

	if x1 == x2:
		x4 = x3
	elif x1 == x3:
		x4 = x2
	else:
		x4 = x1

	if y1 == y2:
		y4 = y3
	elif y1 == y3:
		y4 = y2
	else:
		y4 = y1

	print(x4, y4)

count = int(input())
for i in range(count):
	func()
  '''
  
  '''
for i in range(int(input())):  
    X = 0  
    Y = 0  
    for point_i in range(3):  
        x, y = input().split(' ')  
        X ^= int(x)  
        Y ^= int(y)  
    print(X, Y)  
'''
   
'''
for i in range(int(input())):
    x = y = 0  
    for i in range(3):  
        p = input().strip().split()  
        x ^= int(p[0])  
        y ^= int(p[1])  
    print('{0} {1}'.format(x, y))  
'''

