def dem_so_lan_xuat_hien(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict
input_list = input("nhap danh sach cac tu cach nhau boi dau cach: ")
words_list= input_string.split()
so_lan_xuat_hien = dem_so_lan_xuat_hien(words_list)
print("So lan xuat hien cua moi tu: ",so_lan_xuat_hien)