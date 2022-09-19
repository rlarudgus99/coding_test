# 소수찾기
# 백준 1978번 정답
'''
소수찾기 문제

입력한 숫자 중에 소수가 몇개나 있는지를 출력하는 프로그램
소수 : 약수가 1과 자기자신만 존재하는 수, 1은 제외



예시)
입력 :
4
1 3 5 7

출력 :
3
'''

# init
n = int(input())
input_data = list(map(int, input().split()))
ctr = 0


# main

for i in range(0, n):
    # print('i : ',i)
    if input_data[i] == 1:
        ctr += 1
        # print('1은 소수가 아님')
        continue
    elif input_data[i] == 2:
        # print('2 는 소수임')
        continue
    
    else:
        for j in range(2, input_data[i]):
            # print('j : ',j)
            # print('ref_data : ', input_data[i])
            if input_data[i] % j == 0:
                
                # 조건이 참이면 소수가 아님 (약수가 존재)
                # 소수가 아닌 수를 세고(ctr += 1)
                # for j in range 문을 break
                #
                # 전체 숫자의 갯수(n) 에서 뺀 값을 출력
            
                ctr += 1
                # print('ctr : ', ctr)
                break


res = n - ctr
print('res :', res)


