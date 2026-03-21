import json
import numpy as np

#定义函数读取json文件
def load_json(json_file_path):
    with open(json_file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


#定义函数进行坐标转换
def change_axis(v,old_basis_vector,new_basis_vector):

    #将Python原生列表转换成numpy数组，进行矩阵向量运算
    old_basis_matrix = np.array(old_basis_vector)
    new_basis_matrix = np.array(new_basis_vector)
    v_vector = np.array(v)

    #验证矩阵是否可逆
    try:
        new_basis_inverse = np.linalg.inv(new_basis_matrix)
    except:
        raise ValueError("无法构成有效坐标系")

    #进行坐标转换
    v_new = old_basis_matrix @ v_vector @ new_basis_inverse
    return v_new.tolist()#转换成Python原生数据


#定义向量在坐标投影的函数
def axis_projection(v,basis):
    v = np.array(v)
    #列表用于存储每个基向量的投影长度
    projections = []
    #遍历每一个向量
    for i in basis:
        #统一数据格式
        i = np.array(i)
        #根据公式，投影等于 点积 / 基向量模长
        proj = np.dot(i,v) / np.linalg.norm(i)
        #把投影长度转换成Python数值，添加到列表中
        projections.append(proj.item())

    return projections


#定义向量与坐标轴的夹角弧度函数
def axis_angle(v,basis):
    v = np.array(v)
    #向量模长
    v_norm = np.linalg.norm(v)
    #存储弧度
    angles = []

    for i in basis:
        i = np.array(i)
        i_norm = np.linalg.norm(i)
        angle_cos = np.dot(i,v) / (v_norm * i_norm)
        angles.append(angle_cos.item())

    return angles


#定义面积缩放倍数函数
def area(basis):
    basis_matrix = np.array(basis)
    #在二维空间中，两个向量组成矩阵行列式，其绝对值就是就是这两个向量组成的平行四边形的面积，符号表示方向
    scale = np.linalg.det(basis_matrix)
    #返回绝对值
    return abs(scale)


#判断能否构成坐标系函数
def is_can_basis(basis):

    #如果基向量线性无关，则可以构成坐标系
    basis_matrix = np.array(basis)

    #如果 矩阵的秩 == 矩阵的维度（行数），则基向量线性无关，则可以构成坐标系
    return np.linalg.matrix_rank(basis_matrix) == basis_matrix.shape[0]


class CoordinateSystem:#大写分隔单词
    def __init__(self,ori_axis,vector):
        self.ori_axis = np.array(ori_axis) #基向量
        self.vector = np.array(vector) #当前向量
        self.dim = self.ori_axis.shape[0]

        #判断能否构成坐标系
        if is_can_basis(ori_axis) == False:
            raise ValueError("无法构成坐标系")

    #坐标系转移
    def transfer(self,new_basis):
        new_basis_matrix = np.array(new_basis)
        if is_can_basis(new_basis) == False:
            raise ValueError("新基底无法构成坐标系")

        new_basis_inv = np.linalg.inv(new_basis)
        self.vector = self.vector @ self.ori_axis @ new_basis_inv
        self.ori_axis = new_basis_matrix
        return self.vector.tolist()

    #投影
    def projection(self,basis):
        return axis_projection(self.vector,basis)

    #目标坐标系的夹角弧度
    def v_angle(self,basis):
        return axis_angle(self.vector,basis)

    #面积缩放倍数
    def area_scale(self,basis):
        return area(basis)


def run_tasks(json_path):
    # 读取JSON文件
    data = load_json(json_path)

    # 遍历每一个数据组
    for group in data:
        print(f"\n{'=' * 50}")
        print(f"处理数据组: {group['group_name']}")
        print(f"{'=' * 50}")

        # 获取该组的向量列表
        vectors = group["vectors"]
        ori_axis = group["ori_axis"]
        tasks = group["tasks"]

        # 对每个向量执行任务
        for vec_idx, vector in enumerate(vectors):
            print(f"\n--- 处理第 {vec_idx + 1} 个向量: {vector} ---")

            # 创建坐标系对象
            try:
                cs = CoordinateSystem(ori_axis, vector)
                print("初始状态:")
                print(f"  当前坐标系基向量: {cs.ori_axis.tolist()}")
                print(f"  当前向量坐标: {cs.vector.tolist()}")
            except ValueError as e:
                print(f"错误: {e}")
                continue

            # 执行功能
            for task_idx, task in enumerate(tasks):
                task_type = task["type"]
                print(f"\n任务 {task_idx + 1}: {task_type}")

                try:
                    if task_type == "change_axis":
                        obj_axis = task["obj_axis"]
                        # 检查是否能构成坐标系
                        if not is_can_basis(obj_axis):
                            print(f"无法构成坐标系")
                            continue
                        new_vec = cs.transfer(obj_axis)
                        print(f"转移后向量: {new_vec}")
                        print(f"当前状态:")
                        print(f"当前坐标系基向量: {cs.ori_axis.tolist()}")
                        print(f"当前向量坐标: {cs.vector.tolist()}")

                    elif task_type == "axis_projection":
                        # 投影是在当前坐标系下计算的
                        proj = cs.projection(cs.ori_axis)
                        print(f"在坐标系各轴投影长度: {proj}")

                    elif task_type == "axis_angle":
                        angles = cs.v_angle(cs.ori_axis)
                        print(f"与坐标系各轴夹角(弧度): {angles}")

                    elif task_type == "area":
                        scale = cs.area_scale(cs.ori_axis)
                        print(f"坐标系面积缩放倍数: {scale}")

                except Exception as e:
                    print(f"  任务执行错误: {e}")

            print("-" * 40)


# 运行程序
if __name__ == "__main__":
    run_tasks(r"C:\Users\Lenovo\Desktop\线下训练营\data(1).json")