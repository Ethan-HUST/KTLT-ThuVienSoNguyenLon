# Name: Nguyễn Trung Kiên
# Student ID: 20227180
# Class: 150327
# Project: 2 - XÂY DỰNG “THƯ VIỆN” PHÉP TOÁN VỚI SỐ NGUYÊN LỚN
# Date: 20/06/2024

#Chương trình tính số Fibonacci thứ n ứng dụng thư viện BigInt
from BigInt import BigInt # Import thư viện BigInt

def fibonacci(n):
    """
    Hàm đệ quy tính số Fibonacci thứ n
    Đầu vào: Thứ nguyên của số Fibonacci
    Đầu ra: Số Fibonacci thứ n
    """
    if n == 0:
        return BigInt("0")
    elif n == 1:
        return BigInt("1")
    else:
        a, b = BigInt("0"), BigInt("1")
        for i in range(2, n + 1):
            c = a.tong(b)
            a = b
            b = c
        return b

def main():
    n = int(input("Nhap vao so thu n: "))
    print("So Fibonacci thu {n} la: ")
    fibonacci(n).in_ra_man_hinh()

if __name__ == "__main__":
    main()
