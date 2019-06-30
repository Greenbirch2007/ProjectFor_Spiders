
def if_isnull(content):
    if_list =[]

    if  content ==None:
        f_content  = ''
        if_list.append(f_content)

    else:

        f_content =content
        if_list = f_content


    return if_list


a = ['sfa']
b = None

a1 = if_isnull(a)
b1 = if_isnull(b)
big_list = []

for i1,i2 in zip(a1,b1):
    big_list.append((i1,i2))
print(big_list)

# 把为空的部分用函数处理了！
