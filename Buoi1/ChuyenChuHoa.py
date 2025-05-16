print("Nhap cac dong van ban (Nhap 'done' de ket thuc):")
lines=[]
while True:
    line = input()
    if line.lower()=='done':
        break
    lines.append(line)
print("\n cac dong da nhap sao khi chuyen thanh chu hoa la:")
for line in lines :
    print(line.upper())