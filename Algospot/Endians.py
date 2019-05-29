num1 = int(input())

for i in range(0, num1):

b = int(input())

print((b & 0xff000000) >> 24) | ((b & 0xff0000) >> 8)|((b & 0xff00) << 8) | ((b & 0xff) << 24)

'''
# 다른 답안

for i in range(int(input())):
x = int(input())
print(((x & 0x000000ff) << 24) |\
((x & 0x0000ff00) << 8) |\
((x & 0x00ff0000) >> 8) |\
((x & 0xff000000) >> 24))
'''

'''해설
 간단하게 프린트로 출력하고 싶었고 제일 앞 부터 78 56 34 12를 12 34 56 78 따로따로 하나의 코드로 묶어준 것임 그리고
 | 를 넣은것은 사실 보면 | 비트연산자는 의미가 서로 달라도 참 이라는 것 이 점을 이용하면 된다는 것이었다는 것이다.
'''

# 그 외 답안

'''
def endian():
	a = []
	b = []
	sum = 0
	num = input()
	while (num / 2.0 > 0):
		a.append(num % 2)
		num = num / 2

	if (num == 1):
		a.append(1)

	while (a.count(0) + a.count(1) != 32):
		a.append(0)

	while (a):
		b.append(a.pop())

	b[:8], b[24:] = b[24:], b[:8]
	b[8:16], b[16:24] = b[16:24], b[8:16]

	for i in range(32):
		sum += b[i] * (2 ** (31 - i))

	print(sum)

count = input()
for i in range(count):
	endian()
  '''
  
  '''
T = int(input())
for ti in range(T):
  num = int(input())
  a = (num & 0xff000000) >> 24
  b = (num & 0xff0000) >> 8
  c = (num & 0xff00) << 8
  d = (num & 0xff) << 24
  print(a + b +c +d)
  '''
  
  # struct 이용한 답
  '''
  import sys  
import struct  

def swap32(i):  
    return struct.unpack("<I", struct.pack(">I", i))[0]  

rl = lambda: sys.stdin.readline()  
n = int(rl())  
for i in range(n):  
    print swap32(int(rl()))  
    '''
