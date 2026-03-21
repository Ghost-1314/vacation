# 1.`json`库是什么

总括：

`json`库是编程语言中处理数据格式的工具库，核心作用是**实现`json`字符串**和**编程语言原始数据结构**之间的转换。



关键：

- `json`是一种轻量级的文本数据交换格式，比如`{"name":"张三","age":20}`，容易被人阅读和编写，也更容易被机器解析和生成。

- `json`库就是帮助“翻译”这种格式的工具——把 `json` 文本转成程序能直接操作的变量（反序列化），或者把程序里的变量转成`json`文本（序列化）。

- `json`库处理的是**数据**（变量、值、数据结构等），而**不是代码逻辑**（函数、循环、条件判断、类定义等）。核心本质是“数据格式转换”，而非“代码本身的转换”。

- 只有当数据结构符合`json`语法规则时，`json`库才能把它转成`json`文本；反过来，`json`库也能把`json`文本转回对应语言的原生数据结构。

- 在 Python中，**所有`JSON`格式的内容，不管它的 “内容结构” 是 `JSON`对象、`JSON` 数组还是`JSON`字符串，最终都会以`Python`的`str`类型存储和输出**—— 因为`JSON`的本质就是 “符合特定语法规则的文本字符串”，而文本在`Python`里唯一的存储类型就是`str`。
---
# 2.`json`基础数据类型和`Python`数据类型的对应关系

| JSON数据类型 | 格式示例                        | 对应的Python类型        | 说明                                                                   |
| -------- | --------------------------- | ------------------ | -------------------------------------------------------------------- |
| 字符串      | `"name": "张三"`              | `str`（字符串）         | `JSON`字符串必须用**双引号**，`Python`支持单 / 双引号                                |
| 数字       | `"age": 20`/`"score": 95.5` | `int`/`float`（数字）  | 无引号，支持整数/浮点数                                                         |
| 布尔       | `"is_student": true`        | `True`/`False`（布尔） | `JSON`是`true/false`（小写），`Python` 是`True/False`（大写）                   |
| 数组       | `"hobbies": ["编程", "阅读"]`   | `list`（列表）         | `JSON`数组用`[]`，`Python` 列表也用`[]`，结构一致                                 |
| 对象       | `{"name":"张三", "age":20}`   | `dict`（字典）         | `JSON`的核心结构（键值对），`JSON` 对象用`{}`（键必须双引号），`Python`字典用`{}`（键可单引号 / 无引号） |
| null     | `"score": null`             | `None`（空值）         | `JSON`的空值对应`Python`的`None`，`JSON` 没有`None`，`Python` 没有`null`，互相映射    |

---
# 3.核心功能代码示例

```Python
import json

# ========== 1. 序列化：Python字典 → JSON字符串 ==========
# 定义Python原生数据（字典）
python_data = {
    "name": "张三",
    "age": 20,
    "hobbies": ["编程", "阅读"],
    "is_student": True,
    "score": None
}

# 转成JSON字符串（ensure_ascii=False：保留中文，indent=2：格式化输出）
json_str = json.dumps(python_data, ensure_ascii=False, indent=2)
print("JSON字符串：")
print(json_str)
# 输出：
# {
#   "name": "张三",
#   "age": 20,
#   "hobbies": ["编程", "阅读"],
#   "is_student": true,
#   "score": null
# }

# ========== 2. 反序列化：JSON字符串 → Python字典 ==========
# 定义JSON字符串
json_str2 = '{"name":"李四","age":25,"city":"北京"}'

# 转成Python字典
python_dict = json.loads(json_str2)
print("\nPython字典：")
print(python_dict)  # 输出：{'name': '李四', 'age': 25, 'city': '北京'}
print(python_dict["city"])  # 可以直接操作：输出“北京”

# ========== 3. 读写JSON文件（常用场景） ==========
# 把数据写入JSON文件
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(python_data, f, ensure_ascii=False, indent=2)

# 从JSON文件读取数据
with open("data.json", "r", encoding="utf-8") as f:
    data_from_file = json.load(f)
print("\n从文件读取的内容：")
print(data_from_file["hobbies"])  # 输出：['编程', '阅读']
```

- `json.dumps()`：将`Python`对象转为`JSON`字符串（内存操作）；
    
- `json.loads()`：将`JSON`字符串转为`Python`对象（内存操作）；
    
- `json.dump()`：直接将`Python`对象写入`JSON`文件；
    
- `json.load()`：直接从`JSON`文件读取数据并转为`Python`对象；
    
- 注意`JSON`的语法规则：键必须用双引号，值支持字符串、数字、布尔（`true/false`）、`null`、数组、对象，不支持Python的`None`（会转成`null`）、`True/False`（会转成`true/false`）。


| 函数             | 核心作用                            | 基本语法                           | 常用参数及作用                                                                                                                                                                                                                                  | 示例                                                                                                                                                                              |
| -------------- | ------------------------------- | ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `json.dumps()` | 将`Python`对象序列化为`JSON`字符串（内存操作）  | `json.dumps(obj, **kwargs)`    | `obj`：要序列化的`Python`对象（`dict/list/str/int`等）<br>`ensure_ascii`：是否转义ASCII外的字符（如中文），默认`True`（转义），设为`False`保留中文<br>`indent`：格式化缩进的空格数（int），默认`None`（紧凑格式）<br>`sort_keys`：是否按字母排序`JSON`的键，默认`False`<br>`skipkeys`：是否跳过非字符串的键，默认`False`（遇到会报错） | `python<br>import json<br>data = {"name": "张三", "age": 20}<br># 保留中文+格式化缩进<br>json_str = json.dumps(data, ensure_ascii=False, indent=2)<br>print(json_str)<br>`                 |
| `json.loads()` | 将`JSON`字符串反序列化为`Python`对象（内存操作） | `json.loads(s, **kwargs)`      | `s`：要解析的`JSON`格式字符串（`str`）<br>`encoding`：指定字符串编码（`Python3`基本不用，默认`utf-8`）<br>`strict`：是否严格遵循`JSON`语法，默认`True`（不允许逗号结尾等）                                                                                                                  | `python<br>json_str = '{"name":"张三","age":20}'<br>data = json.loads(json_str)<br>print(data["name"]) # 输出：张三<br>`                                                               |
| `json.dump()`  | 将`Python`对象序列化后写入`JSON`文件       | `json.dump(obj, fp, **kwargs)` | `obj`：要序列化的Python对象<br>`fp`：文件对象（需以`w`/`wb`模式打开）<br>其他参数：同`dumps()`（`ensure_ascii`/`indent`等）<br>`encoding`：文件编码（`Python3`需在`open()`中指定，而非此参数）                                                                                           | `python<br>data = {"name": "张三", "age": 20}<br># 写入文件，保留中文+格式化<br>with open("data.json", "w", encoding="utf-8") as f:<br> json.dump(data, f, ensure_ascii=False, indent=2)<br>` |
| `json.load()`  | 从`JSON`文件读取数据并反序列化为`Python`对象   | `json.load(fp, **kwargs)`      | `fp`：文件对象（需以`r`/`rb`模式打开）<br>其他参数：同`loads()`（`encoding`/`strict`等）<br>`encoding`：文件编码（`Python3`需在`open()`中指定）                                                                                                                            | `python<br># 读取文件并解析<br>with open("data.json", "r", encoding="utf-8") as f:<br> data = json.load(f)<br>print(data["age"]) # 输出：20<br>`                                          |
