so_gio_lam = float (input("nhap so gio lam moi tuan: "))
luong_gio =float(input("nhap thu lao tren mi gio lam tieu chuan: "))
gio_tieu_chuan = 44
gio_vuot_chuan= max(0,so_gio_lam-gio_tieu_chuan)
thuc_linh = luong_gio*gio_tieu_chuan + gio_vuot_chuan*luong_gio*1.5
print(f"luong thuc linh la: ",{thuc_linh})