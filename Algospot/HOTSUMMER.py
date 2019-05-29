# 반복할 횟수를 입력
T = int(input())

#반복
for a in range(T):
#비교할 값
    b = int(input())
    #입력받은 값
    c = input().split()
    #g는 입력받은 값의 총합이다
    g=0
    #입력받은 값의 총합을 구하는 과정
    for f in range(len(c)):
        c[f]=int(c[f])
        g+=c[f]
        
# 조건문으로 입력받은 값과 입력받은 값을 총합을 비교한다
    if g<=b:
        print("YES")
    else:
        print("NO")
