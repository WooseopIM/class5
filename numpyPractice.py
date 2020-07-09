import numpy as np

# arr1 = np.array([1, 3, 5, 7, 9])
# arr2 = np.array((1, 3, 5, 7, 9))
# print(type(arr1), type(arr2)) # 둘 다 numpy.ndarray

# arr3 = np.arange(0, 10) # 파이썬의 range(start, end)
# arr4 = np.arange(10)
# arr5 = np.arange(0,10,2)
# print(arr3)
# print(arr4)
# print(arr5)
# print(len(arr3), arr3.size) # 배열의 길이는 두 가지 방법으로 구할 수 있다

# arr6 = np.append(arr5, [1, 2, 3])
# print(arr6) # numpy의 append는 파이썬에서 [1, 2, 3] + [4, 5, 6]처럼 쓰는 것과 같음
# print(arr5) # append의 인자로 사용된 배열은 원본 값 그대로 갖고 있음

# arr7 = np.linspace(1, 20, 10)
# print(arr7)

# arr8 = np.ones((2, 3)) # 1로만 이뤄진 2행3열의 2차원 배열
# arr9 = np.zeros((2, 3)) # 0으로만 이뤄진 2행3열의 2차원 배열
# print(arr8)
# print(arr9)

# arr10 = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr10[1, 2]) # arr10의 1번째 인덱스의 2번 인덱스 값
# print(arr10[1:, 1:])

# arr11 = np.arange(20)
# print(arr11.reshape(20, 1))
# print(arr1.reshape(-1, 1))

arr12 = np.array([1, 2, 3])
arr13 = np.array([4, 5, 6])
print(1.0*arr12/arr13)
print(arr12/arr13)
print(np.cumsum(arr12))