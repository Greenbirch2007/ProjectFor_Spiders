
# 处理成功
def remove_block(items):
    new_items = []
    for it in items:
        f = "".join(it.split())
        new_items.append(f)
    return new_items



a = ['\n         asra           \n']
b = None
c = ['aer']

# t = remove_block(a)
# print(t)

# 把去除空格和为空值同时进行处理
def ifisnull_removeBlock(content):
    if_list =[]

    if  content ==None:
        f_content  = ''
        if_list.append(f_content)
    else:

        f_content =content
        if_list = f_content

    new_items = []
    for it in if_list:
        f = "".join(it.split())
        new_items.append(f)
    return new_items

print(ifisnull_removeBlock(a))
print(ifisnull_removeBlock(b))
print(ifisnull_removeBlock(c))



