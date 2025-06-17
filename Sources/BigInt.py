# Name: Nguyễn Trung Kiên
# Student ID: 20227180
# Class: 150327
# Project: 2 - XÂY DỰNG “THƯ VIỆN” PHÉP TOÁN VỚI SỐ NGUYÊN LỚN
# Date: 20/06/2024

class BigInt:
    def __init__(self, gia_tri):
        """
        Khởi tạo đối tượng BigInt với giá trị số nguyên ban đầu.
        
        Tham số:
        gia_tri (str or int): Giá trị số nguyên lớn.
        """
        self.gia_tri = int(gia_tri)

    @staticmethod
    def nhap_tu_ban_phim():
        """
        Nhập một số nguyên lớn từ bàn phím.
        
        Trả về:
        BigInt: Đối tượng BigInt với giá trị đã nhập.
        """
        gia_tri = input("Nhap so hang: ").strip()
        return BigInt(gia_tri)

    @staticmethod
    def nhap_tu_file(ten_file):
        """
        Nhập hai số nguyên lớn từ file.

        Tham số:
        ten_file (str): Tên của file chứa số nguyên lớn.

        Trả về:
        tuple(BigInt, BigInt): Hai đối tượng BigInt từ hai dòng đầu tiên của file.
        """
        with open(ten_file, 'r', encoding='utf-8') as file:
            gia_tri_1 = file.readline().strip()
            gia_tri_2 = file.readline().strip()
        return BigInt(gia_tri_1), BigInt(gia_tri_2)

    def tong(self, so_khac):
        """
        Tính tổng của hai đối tượng BigInt.
        
        Tham số:
        so_khac (BigInt): Đối tượng BigInt thứ hai.
        
        Trả về:
        BigInt: Đối tượng BigInt là tổng của hai số nguyên lớn.
        """
        return BigInt(self.gia_tri + so_khac.gia_tri)

    def hieu(self, so_khac):
        """
        Tính hiệu của hai đối tượng BigInt.
        
        Tham số:
        so_khac (BigInt): Đối tượng BigInt thứ hai.
        
        Trả về:
        BigInt: Đối tượng BigInt là hiệu của hai số nguyên lớn.
        """
        return BigInt(self.gia_tri - so_khac.gia_tri)

    def tich(self, so_khac):
        """
        Tính tích của hai đối tượng BigInt.
        
        Tham số:
        so_khac (BigInt): Đối tượng BigInt thứ hai.
        
        Trả về:
        BigInt: Đối tượng BigInt là tích của hai số nguyên lớn.
        """
        return BigInt(self.gia_tri * so_khac.gia_tri)

    def chia_so_thuc(self, so_khac):
        """
        Chia hai đối tượng BigInt và trả về kết quả dưới dạng số thực với độ chính xác đến 8 chữ số thập phân.
        
        Tham số:
        so_khac (BigInt): Đối tượng BigInt thứ hai.
        
        Trả về:
        float: Kết quả phép chia dưới dạng số thực.
        
        Ngoại lệ:
        ValueError: Nếu chia cho số 0.
        """
        if so_khac.gia_tri == 0:
            raise ValueError("Khong the chia cho so 0")
        return round(self.gia_tri / so_khac.gia_tri, 8)

    def in_ra_man_hinh(self):
        """
        In giá trị của đối tượng BigInt ra màn hình.
        """
        print(self.gia_tri)

    def in_ra_file(self, ten_file):
        """
        Ghi giá trị của đối tượng BigInt vào file.
        
        Tham số:
        ten_file (str): Tên của file để ghi giá trị.
        """
        with open(ten_file, 'a', encoding='utf-8') as file:
            file.write(f"{self.gia_tri}\n")
