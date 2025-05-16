so_gio_lm=float(input("Nhap so gio lm moi tuan"))
luong_theo_gio=float(input("nhap luong"))
gio_tieu_chuan=44
gio_tang_ca=max(0,so_gio_lm-gio_tieu_chuan)
luong=gio_tieu_chuan*luong_theo_gio+(gio_tang_ca*luong_theo_gio*1.5)
print("Luong ban la ",luong)