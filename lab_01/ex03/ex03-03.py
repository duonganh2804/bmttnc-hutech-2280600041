def tao_tuple_tu_list(list):
    return tuple(list)
input_list = input("nhap dand sach so cach nhau boi dau phay: ")
numbers= list(map(int, input_list.split(',')))
tuple = tao_tuple_tu_list(numbers)
print("list: ",tuple)
print("tuble tu list: ",tuple)