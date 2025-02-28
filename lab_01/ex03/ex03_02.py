def daonguoclist(lst):
    return lst[::-1]
input_list = input("nhap dand sach so cach nhau boi dau phay: ")
numbers= list(map(int, input_list.split(',')))
daonguoc =daonguoclist(numbers)
print("Day so sau khi dao nguoc la: ",daonguoc)