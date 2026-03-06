import numpy as np

#创建形状为(3,4)的数组，元素为0~11的连续整数
arr = np.arange(12)
arr_1 = arr.reshape((3,4))
print(arr_1)

#查看属性
print(f"数组的shape属性：{arr_1.shape}")
print(f"数组的dtype属性：{arr_1.dtype}")
print(f"数组的ndim属性：{arr_1.ndim}")

#变型为(4,3)
arr_2 = arr_1.reshape((4,3))
print(arr_2)

#展平为一维数组
arr_3 = arr_2.reshape(-1)
print(arr_3)