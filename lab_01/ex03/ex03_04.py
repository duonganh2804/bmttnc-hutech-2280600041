def truycapphantu(tuple_data):
    first_element = tuple_data[0]
    last_element = tuple_data[-1]
    return first_element, last_element
input_tuple =eval(input("nhap tuple, vi du (1,2,3): "))
first,last = truycapphantu(input_tuple)
print("Phan tu dau tien va cuoi cung cua tuple la: ",first,last)