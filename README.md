
# 📚 Thư viện Phép toán với Số nguyên lớn – Báo cáo Bài tập lớn MI3310

## 🧾 Thông tin chung

- **Môn học**: Kỹ thuật lập trình (MI3310)
- **Chủ đề**: Xây dựng thư viện phép toán với số nguyên lớn
- **Giảng viên hướng dẫn**: TS. Nguyễn Thành Nam
- **Sinh viên thực hiện**: Nguyễn Trung Kiên – MSSV 20227180
- **Lớp học**: 150327
- **Thời gian**: Tháng 6/2024

## 📌 Mục tiêu đề tài

Xây dựng một thư viện `BigInt` bằng Python có khả năng xử lý các phép toán cơ bản (cộng, trừ, nhân, chia thực) với số nguyên lớn có độ dài lên tới 1000 chữ số. Đảm bảo:
- Tính **chính xác** trong tính toán.
- Tối ưu **hiệu suất** thực thi.
- Khả năng **mở rộng**, **kiểm thử** và **ứng dụng thực tiễn**.

## 🧮 Chức năng chính của thư viện

- **Nhập số nguyên lớn** từ bàn phím hoặc từ file.
- **Thực hiện phép toán**: `+`, `-`, `*`, `/` (kết quả thực, độ chính xác đến 8 chữ số thập phân).
- **Xuất kết quả** ra màn hình hoặc ghi vào file.
- **Tính toán ứng dụng**: ví dụ số Fibonacci thứ 4782 (có 1000 chữ số).

## 🧠 Cấu trúc thư viện BigInt

```python
class BigInt:
    def __init__(self, gia_tri): ...
    def nhap_tu_ban_phim(): ...
    def nhap_tu_file(ten_file): ...
    def tong(self, so_khac): ...
    def hieu(self, so_khac): ...
    def tich(self, so_khac): ...
    def chia_so_thuc(self, so_khac): ...
    def in_ra_man_hinh(self): ...
    def in_ra_file(self, ten_file): ...
```

## 📁 Cấu trúc dự án

```
├── BigInt.py           # Thư viện xử lý số nguyên lớn
├── main.py             # Hàm main chạy chương trình
├── input.txt           # Tập tin chứa đầu vào mẫu
├── output.txt          # Tập tin chứa kết quả đầu ra
├── Fibonacci.py        # Tính số Fibonacci thứ 4782
└── README.md           # Tệp hướng dẫn (bạn đang đọc nó!)
```

## 🚀 Cách sử dụng

### 1. Yêu cầu
- Python 3.x đã cài sẵn.
- Không yêu cầu thư viện bên ngoài (sử dụng `int` tích hợp của Python).

### 2. Chạy chương trình chính
```bash
python main.py
```
Người dùng chọn:
- Nhập số từ bàn phím hoặc từ file `input.txt`.
- Thực hiện phép toán cộng, trừ, nhân, chia.
- Xuất kết quả ra màn hình hoặc ghi vào file `output.txt`.

### 3. Tính số Fibonacci lớn
```bash
python Fibonacci.py
```
Trả về số Fibonacci thứ 4782 – số Fibonacci đầu tiên có 1000 chữ số.

## ✅ Kiểm thử

Chương trình đã được kiểm thử với:
- Số nguyên có 1, 10, 100, đến 1000 chữ số.
- Các trường hợp biên: số 0, số âm, chia cho 1, chia cho 0.
- Nhập xuất từ cả file và bàn phím.
- Đánh giá hiệu suất và tính chính xác.

## 🧪 Tài liệu kiểm thử
Xem thư mục test case:  
[📂 Bộ test case trên Google Drive](https://drive.google.com/drive/folders/1PhOWZUPTqZ_ymR0N1eC97qRbjz0vm-NP?usp=sharing)

## 🔗 Liên kết tài liệu
- [📄 Báo cáo đầy đủ (Word)](https://drive.google.com/drive/folders/1UAsF5uuVcnt9fCswQ7_QSqIO9KnR_wwI?usp=sharing)
- [💾 BigInt.py (Thư viện)](https://drive.google.com/file/d/1d0L6lcyPnquYYoIQs0OH0BJuA0mr5-RX/view?usp=sharing)
- [🔧 main.py (Hàm chính)](https://drive.google.com/file/d/1rZZjFJkn86H9WDypgMZFoCvxhRlDc3_q/view?usp=sharing)

## 📚 Tài liệu tham khảo tiêu biểu
- Wikipedia: [Thể loại: Số nguyên lớn](https://vi.wikipedia.org/wiki/Th%E1%BB%83_lo%E1%BA%A1i:S%E1%BB%91_nguy%C3%AAn_l%E1%BB%9Bn)
- John Zelle – *Python Programming: An Introduction to CS*
- Luciano Ramalho – *Fluent Python*
- Al Sweigart – *Automate the Boring Stuff with Python*
- David Beazley – *Python Cookbook*

## 🙏 Lời cảm ơn
Em xin trân trọng cảm ơn thầy **TS. Nguyễn Thành Nam** đã tận tình hướng dẫn và truyền cảm hứng nghiên cứu. Cảm ơn các thầy cô Khoa Toán – Tin, Đại học Bách Khoa Hà Nội đã hỗ trợ em trong quá trình học tập và thực hiện đề tài này.

---
