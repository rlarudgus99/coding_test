# 정렬

# 선택, 삽입, 퀵, 계수


# ex6_1 예제

# 선택정렬
# 입력 데이터 중 가장 작은 값을 첫번째 원소의 위치와 바꾼다.
# 그 다음, 입력 데이터 중 다음으로 작은 값을 두번째 원소의 위치와 바꾼다.
# min_index 는 매 iteration 마다 1씩 증가한다.

# array = [7,5,9,0,3,1,6,2,4,8]

# for i in range(len(array)):
#     min_index = i
#     # i = 0
#     for j in range(i+1, len(array)):
#         if array[i] > array[j]:
#             min_index = j
#             array[j], array[i] = array[i], array[j]

# print(array)

# ex6_3 예제

# 삽입정렬
# 첫번째 for문은 index 1 부터 시작
# 중첩 for문은 index가 큰 수부터 1까지
# 더 작은 수를 가진 인덱스가 나오면 왼쪽으로 당겨버림

# array = [7,5,9,0,3,1,6,2,4,8]
# for i in range(1,len(array)):
#     for j in range(i, 0, -1):
#         if array[j] < array[j-1]:
#             array[j], array[j-1] = array[j-1], array[j]
#         else:
#             break

# print(array)


# 퀵정렬
# 가장 빠른 속도의 정렬 알고리즘
# Pivot 개념이 사용됨 (기준 인덱스가 갖는 값)

# 기준이 되는 Index를 정한다. 일반적으로 리스트 0번째 값
# 리스트를 절반으로 나눈다.
# 절반 기준 우측 pivot보다 작은 수와 좌측 pivot보다 큰 수를 상호교환한다.
#          (우측부터 시작)           (좌측부터 시작)

# 만약 절반 기준 우측에 pivot보다 큰 수가 있고, 절반 기준 좌측에 pivot보다 작은 수가 있는 경우,
# 둘 중 작은 수와 pivot을 switch 한다.

# 그러면 리스트는 pivot 기준 좌측은 pivot 보다 작은 값, pivot 기준 우측은 pivot 보다 큰 값들의 두개 리스트로 나뉜다.
# 좌우 각각의 리스트를 처음의 순서와 같이 다시 정렬한다.


# main

arr = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(arr, start, end):
    if start >= end:
        return
    
    pivot = start

    left = start + 1
    right = end

    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            right -= 1

        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]
    quick_sort(arr, start, right- 1)
    quick_sort(arr, right + 1, end)

quick_sort(arr,0,len(arr) - 1)
print(arr)