raw_data = ["85", "92", "ERROR", "105", "78", "WARNING", "99", "120"]
def judge(s):
    try:
        int(s)
        return True
    except:
        return False

result=filter(judge,raw_data)
result_list=list(result)
new_result_list=[]
for i in result_list:
    if int(i) >= 80:
        new_result_list.append(i)

for i in new_result_list:
    value = int(i)
    value /= 100
    if value > 1:
        print(f"{i}-----核心过载")
    else:
        print(f"{i}-----运转正常")