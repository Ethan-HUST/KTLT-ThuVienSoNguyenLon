# Name: Nguyễn Trung Kiên
# Student ID: 20227180
# Class: 150327
# Project: 2 - XÂY DỰNG “THƯ VIỆN” PHÉP TOÁN VỚI SỐ NGUYÊN LỚN
# Date: 20/06/2024

from BigInt import BigInt  # Import thư viện BigInt

def chon_nguon_nhap():
    """
    Hiển thị menu cho người dùng chọn nguồn nhập số nguyên lớn.
    
    Trả về:
    str: Lựa chọn của người dùng ('1' hoặc '2').
    """
    print("Chon nguon nhap so:")
    print("1. Nhap tu ban phim")
    print("2. Nhap tu file 'input.txt'")
    lua_chon = input("Lua chon cua ban (1/2): ").strip()
    return lua_chon

def chon_nguon_xuat():
    """
    Hiển thị menu cho người dùng chọn nơi xuất kết quả.
    
    Trả về:
    str: Lựa chọn của người dùng ('1' hoặc '2').
    """
    print("Chon noi xuat ket qua:")
    print("1. In ra man hinh")
    print("2. In ra file 'output.txt'")
    lua_chon = input("Lua chon cua ban (1/2): ").strip()
    return lua_chon

def main():
    """
    Chương trình chính để nhập số nguyên lớn, thực hiện các phép toán và xuất kết quả.
    """
    # Nhập số nguyên lớn
    lua_chon_nhap = chon_nguon_nhap()
    if lua_chon_nhap == "1":
        so_thu_nhat = BigInt.nhap_tu_ban_phim()
        so_thu_hai = BigInt.nhap_tu_ban_phim()
    elif lua_chon_nhap == "2":
        so_thu_nhat, so_thu_hai = BigInt.nhap_tu_file('input.txt')
    else:
        print("Lua chon khong hop le!")
        return

    # Tính toán
    tong = so_thu_nhat.tong(so_thu_hai)
    hieu = so_thu_nhat.hieu(so_thu_hai)
    tich = so_thu_nhat.tich(so_thu_hai)
    ket_qua_chia = so_thu_nhat.chia_so_thuc(so_thu_hai)

    # Xuất kết quả
    lua_chon_xuat = chon_nguon_xuat()
    if lua_chon_xuat == "1":
        print("Ket qua cac phep tinh:")
        print("Tong: ", end=""); tong.in_ra_man_hinh()
        print("Hieu: ", end=""); hieu.in_ra_man_hinh()
        print("Tich: ", end=""); tich.in_ra_man_hinh()
        print("Chia so thuc: ", ket_qua_chia)
    elif lua_chon_xuat == "2":
        with open('output.txt', 'w', encoding='utf-8') as file:
            file.write("Ket qua cac phep tinh:\n")
            file.write(f"Tong: {tong.gia_tri}\n")
            file.write(f"Hieu: {hieu.gia_tri}\n")
            file.write(f"Tich: {tich.gia_tri}\n")
            file.write(f"Thuong: {ket_qua_chia}\n")
        print("Ket qua da duoc in ra file 'output.txt'")
    else:
        print("Lua chon khong hop le!")
        return

    input("Nhan Enter de ket thuc...")

if __name__ == "__main__":
    main()
