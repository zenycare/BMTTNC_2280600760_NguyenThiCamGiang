def kiem_tra_so_nguyen_to(n):
    if n<=1:
        return False
    for i in range (2, int (n**0.5)+1):
        if n%i ==0:
            return False
        return True

number = int(input("Nhap so can kiem tra"))
if(kiem_tra_so_nguyen_to(number)):
    print("so nguyen to la", number)
else:
    print(number, ("Khong phai la so nguyen to"))