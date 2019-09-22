dic={'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5, 'six':6,'seven':7,'eight':8,'nine':9,'ten':10 } 
dic2={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten'}

T=int(input())
tem_count=3
first=''
second=''

# 기본 구성
for a in range(T):
    #input()
    null = input()
    # =의 위치
    fin = null.find('=')
    # 정답
    ans=null[fin+2:]
    
    # 처음 들어온 두번째 들어온 숫자 인식
    if null[0:3] in dic:
        first=null[0:3]
        
        if null[6:9] in dic:
            second=null[6:9]
        elif null[6:10] in dic:
            second=null[6:10]
        elif null[6:11] in dic:
            second=null[6:11]
        tem2=3

    elif null[0:4] in dic:
        first=null[0:4]
        
        if null[7:10] in dic:
            second=null[7:10]
        elif null[7:11] in dic:
            second=null[7:11]
        elif null[7:12] in dic:
            second=null[7:12]
            
        tem2=4

    elif null[0:5] in dic:
        first=null[0:5]
        
        if null[8:11] in dic:
            second=null[8:11]
        elif null[8:12] in dic:
            second=null[8:12]
        elif null[8:13] in dic:
            second=null[8:13]
            
        tem2=5

    # 연산 시작 부분.
    if null[tem2+1:tem2+2] == '+':
        tem_first=dic.get(first)
        tem_second=dic.get(second)
        tem_answer=tem_first+tem_second
        
    elif null[tem2+1:tem2+2] == '-':
        tem_first=dic.get(first)
        tem_second=dic.get(second)
        tem_answer=tem_first-tem_second
        
    elif null[tem2+1:tem2+2] == '/':
        tem_first=dic.get(first)
        tem_second=dic.get(second)
        tem_answer=tem_first/tem_second
        
    elif null[tem2+1:tem2+2] == '*':
        tem_first=dic.get(first)
        tem_second=dic.get(second)
        tem_answer=tem_first*tem_second

    # 정답 간주 부분.
    if tem_answer < 0 or tem_answer>10:
        print("No")

    else:
        ans = sorted(ans)
        ans=''.join(ans)
        tem_answer=dic2[tem_answer]
        tem_answer=sorted(tem_answer)
        tem_answer=''.join(tem_answer)

        if ans == tem_answer:
            print('Yes')
        else:
            print('No')
