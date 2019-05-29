#입력할 횟수
a = int(input())
#딕셔너리를 만들어 준다
dic={'kg':2.2046,
     'lb':0.4536,
     'l':0.2642,
     'g':3.7854}
#입력받은 횟수만큼 반복
for b in range(1,a+1):
#변환한 값을 입력받고
    null = input()
    #공백을 기준으로 나누어준다
    null = null.split()
    #인덱싱을 이용해 값 부분을 소수로 변환후
    null[0] = float(null[0])
    #임시적으로 단위를 저장해줄 변수를 선언
    tem = dic.get(null[1])
    #조건식을 통해서 단위를 변경
    if null[1]=='kg':
        tem2='lb'
    elif null[1]=='lb':
        tem2='kg'
    elif null[1]=='g':
        tem2='l'
    else:
        tem2='g'
    #출력부분 0.4f 출력을 신경써준다.
    print("%d %0.4f %s" % (b, null[0]*tem, tem2))


## 다른 정답
'''
size = int(input())

for i in range(size):
    tar = int(input())
    data = list(map(int,input().split()))

    sum = 0
    for j in data:
        sum += j

    if tar >= sum:
        print('YES')
    else:
        print('NO')
'''
    
