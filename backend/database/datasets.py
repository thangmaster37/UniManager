from connector import *
import pandas as pd
from database_model import *
import random
from datetime import datetime, timedelta

# Danh sach hoc phan
df = pd.read_excel("./backend/database/TKB-HKI-2023-2024.xlsx", engine="openpyxl")
danh_sach_hoc_phan = []
hoc_phan_dict = dict()
for x, y, z in zip(df["Mã \nhọc phần"][1:], df["Học phần"][1:], df["Số\nTC"].fillna(2)[1:]):
    if x not in hoc_phan_dict:
        hoc_phan_dict[x] = 1
        danh_sach_hoc_phan.append((x, y, z))
        
with open('./backend/database/danh_sach_hoc_phan.csv', 'w', encoding='utf-8') as file_a:
    file_a.write('ma_hp,ten_hp,so_tin\n')
    for element in danh_sach_hoc_phan:
        ma_hp, ten_hp, so_tin = element[0], element[1], str(element[2])
        file_a.write(f"{ma_hp},{ten_hp},{so_tin}\n")

# Nhap vao database
# try:
#     for element in danh_sach_hoc_phan:
#         cursor.execute("""
#                        INSERT INTO hoc_phan (ma_hp, ten_hp, so_tin)
#                        VALUES(%s, %s, %s)
#                        """, element)
#         conn.commit()
# except Exception as e:
#     print(f"Error: {e}")

# Danh sach nganh
danh_sach_nganh = [
    ('QHT01', 'Toán học'),
    ('QHT02', 'Toán tin'),
    ('QHT98', 'Khoa học máy tính và thông tin (*)(**)'),
    ('QHT93', 'Khoa học dữ liệu (*)')
]

# Nhap vao database
# try:
#     for element in danh_sach_nganh:
#         cursor.execute("""
#                     INSERT into nganh
#                     VALUES (%s, %s)
#                     """, element)
#         conn.commit()
# except Exception as e:
#     print(f"Error: {e}")

# Danh sach phong
danh_sach_phong = []
for i in range(1, 6):
    for k in range(1, 16):
        if k < 10: danh_sach_phong.append((f'{i}0{k}-T{i}',80,f'Phòng {i}0{k} tòa T{i}'))
        else: danh_sach_phong.append((f'{i}{k}-T{i}',80,f'Phòng {i}{k} tòa T{i}'))

with open('./backend/database/danh_sach_phong.csv', 'w', encoding='utf-8') as file_a:
    file_a.write('phong,suc_chua,mo_ta\n')
    for element in danh_sach_phong:
        phong, suc_chua, mo_ta = element
        file_a.write(f'{phong},{suc_chua},{mo_ta}\n')

# Nhap vao database
# try:
#     for row in danh_sach_phong:
#         for element in row:
#             cursor.execute("""
#                            INSERT INTO phong
#                            VALUES (%s, %s, %s)
#                            """, element)
#             conn.commit()
# except Exception as e:
#     print(f"Error: {e}") 

# Danh sach hoc phan tien quyet
danh_sach_hoc_phan_tien_quyet = [
    ("PEC1008", "PHI1006"),
    ("MAT2502", "MAT2501"),
    ("MAT2503", "MAT2502"),
    ("MAT2503", "MAT2400"),
    ("MAT2403", "MAT2501"),
    ("MAT2403", "AMT2400"),
    ("MAT2034", "MAT2502"),
    ("MAT2034", "MAT2403"),
    ("MAT2034", "MAT3372"),
    ("MAT2323", "MAT2502"),
    ("MAT2323", "MAT2316"),
    ("MAT2323", "MAT2317"),
    ("MAT2323", "MAT2318"),
    ("MAT2323", "MAT2319"),
    ("MAT2407", "MAT2502"),
    ("MAT2315", "MAT3514"),
    ("MAT2315", "MAT2323"),
    ("MAT2315", "MAT2506"),
    ("MAT2315", "MAT2034"),
    ("MAT2316", "INM1000"),
    ("MAT2317", "INM1000"),
    ("MAT2318", "INM1000"),
    ("MAT2319", "INM1000"),
    ("MAT3500", "MAT2400"),
    ("MAT3500", "MAT2501"),
    ("MAT3372", "MAT2316"),
    ("MAT3372", "MAT2317"),
    ("MAT3372", "MAT3218"),
    ("MAT3372", "MAT2319"),
    ("MAT3514", "MAT3372"),
    ("MAT3514", "MAT3500"),
    ("MAT3507", "MAT2316"),
    ("MAT3507", "MAT2317"),
    ("MAT3507", "MAT2318"),
    ("MAT3507", "MAT2319"),
    ("MAT2278", "MAT3507"),
    ("MAT2278", "MAT3372"),
    ("MAT3148", "MAT3514"),
    ("MAT3148", "MAT3557"),
    ("MAT3379", "MAT2323"),
    ("MAT3379", "MAT2400"),
    ("MAT3379", "MAT2316"),
    ("MAT3379", "MAT2317"),
    ("MAT3379", "MAT2318"),
    ("MAT3379", "MAT2319"),
    ("MAT3533", "MAT2034"),
    ("MAT3533", "MAT3514"),
    ("MAT3533", "MAT2323"),
    ("MAT3533", "MAT2400"),
    ("MAT3380", "MAT3514"),
    ("MAT3380", "MAT2323"),
    ("MAT3381", "MAT3372"),
    ("MAT3381", "MAT3507"),
    ("MAT3381", "MAt2506"),
    ("MAT3382", "MAT3514"),
    ("MAT3383", "MAT3372"),
    ("MAT3383", "MAT3500"),
    ("MAT3384", "MAT3533"),
    ("MAT3385", "MAT3372"),
    ("MAT3504", "MAT3514"),
    ("MAT3508", "MAT3372"),
    ("MAT3508", "MAT3507"),
    ("MAT3534", "MAT3507"),
    ("MAT3534", "MAT2323"),
    ("MAT3386", "MAT2323"),
    ("MAT3387", "MAT2323"),
    ("MAT3388", "MAT3507"),
    ("MAT3388", "MAT2323"),
    ("MAT3389", "MAT2323"),
    ("MAT3390", "MAT3533"),
    ("MAT3391", "MAT3372"),
    ("MAT3391", "MAT3500"),
    ("MAT3392", "MAT3507"),
    ("MAT3392", "MAT2323"),
    ("MAT3393", "MAT3533"),
    ("MAT3394", "MAT2403"),
    ("MAT3562", "MAT3533"),
    ("MAT3395", "MAT2323"),
    ("MAT3535", "MAT3514"),
    ("MAT3399", "MAT3533"),
    ("MAT3397", "MAT3533"),
    ("MAT3398", "MAT3533")
]

with open('./backend/database/hoc_phan_tien_quyet.csv', 'w', encoding='utf-8') as file_a:
    file_a.write('ma_hp,hp_tien_quyet\n')
    for element in danh_sach_hoc_phan_tien_quyet:
        ma_hp, hp_tien_quyet = element
        file_a.write(f'{ma_hp},{hp_tien_quyet}\n')
        
# Nhap vao database
# try:
#     for element in danh_sach_hoc_phan_tien_quyet:
#         cursor.execute("""
#                        INSERT INTO hp_tien_quyet
#                        VALUES (%s, %s)
#                        """, element)
#         conn.commit()
# except Exception as e:
#     print(f"Error: {e}")

# Danh sach chuong trinh
danh_sach_chuong_trinh = [
    ('KCT_01', 'QHT01'),
    ('KCT_02', 'QHT02'),
    ('KCT_98', 'QHT98'),
    ('KCT_93', 'QHT93') 
]

with open('danh_sach_chuong_trinh.csv', 'w', encoding='utf-8') as file_a:
    file_a.write('ma_ct,ma_nganh\n')
    for element in danh_sach_chuong_trinh:
        ma_ct, ma_nganh = element
        file_a.write(f'{ma_ct},{ma_nganh}\n')

# Nhap vao database        
# try:
#     for element in danh_sach_chuong_trinh:
#         cursor.execute("""
#                        INSERT INTO chuong_trinh
#                        VALUES (%s, %s)
#                        """, element)
#         conn.commit()
# except Exception as e:
#     print(f"Error: {e}")
    
# Danh sach chuong trinh hoc
df2 = pd.read_csv("./backend/database/danh_sach_chuong_trinh_hoc.csv")
danh_sach_chuong_trinh = [(a1, a2, a3, a4, a5) for a1, a2, a3, a4, a5 in zip(df2["ma_chuong_trinh"], df2["ma_nganh"], df2["ma_hp"], df2["nam"], df2["ki"])]

# Nhap vao database
# try:
#     for element in danh_sach_chuong_trinh:
#         cursor.execute("""
#                        INSERT INTO chuong_trinh_hoc
#                        values (%s, %s, %s, %s, %s)
#                        """, element)
#         conn.commit()
# except Exception as e:
#     print(f"Error: {e}")

# Danh sach ten giang vien
danh_sach_ten_giang_vien = [
    "Nguyen Thanh Hoa",
    "Tran Minh Duc",
    "Le Thi Mai Anh",
    "Pham Van Hieu",
    "Hoang Thi Linh",
    "Vo Quoc Khanh",
    "Ngo Thi Bich",
    "Do Van Tuan",
    "Luong Thi Ha",
    "Nguyen Duc Thang",
    "Tran Thi Thu Trang",
    "Phan Van Quan",
    "Mai Ngoc Lan",
    "Bui Van Phuc",
    "Nguyen Thi Thuy Duong",
    "Hoang Van An",
    "Le Thi Phuong Thao",
    "Vu Ngoc Hien",
    "Truong Minh Quang",
    "Dang Thi Ngoc Thanh",
    "Nguyen Quang Huy",
    "Pham Thi Mai",
    "Trinh Van Long",
    "Vo Thi Nga",
    "Le Van Thanh",
    "Nguyen Thi Ngoc Anh",
    "Do Quang Nam",
    "Hoang Van Minh",
    "Nguyen Thi Ha Vy",
    "Tran Van Hien",
    "Nguyen Van Binh",
    "Luu Thi Kim Ngan",
    "Nguyen Duc Khanh",
    "Le Van Hoang",
    "Pham Thi Thuy Linh",
    "Truong Van Phuoc",
    "Vu Thi Mai",
    "Bui Van Hieu",
    "Nguyen Thi Hong Ngoc",
    "Hoang Van Cuong",
    "Tran Thi Thanh Thuy",
    "Phan Van Vinh",
    "Nguyen Thi Hoai An",
    "Vo Van Thanh",
    "Le Thi Thanh Huyen",
    "Do Van Hung",
    "Nguyen Thi Mai Lan",
    "Trinh Van Tung",
    "Nguyen Van Tien",
    "Nguyen Ha Khanh Linh"
]

def generate_student_names(count):
    first_names = ["Nguyen", "Tran", "Le", "Pham", "Hoang", "Vo", "Ngo", "Do", "Luong", "Truong", "Dang", "Mai", "Bui"]
    middle_names = ["Van", "Thi", "Minh", "Duc", "Thi", "Quang", "Van", "Thi", "Van", "Thi", "Van", "Van", "Van"]
    last_names = ["An", "Bao", "Chau", "Dung", "Lan", "Hieu", "Anh", "Cuong", "Diep", "Duong", "Ha", "Hung", "Huong",
                  "Khoi", "Lien", "Minh", "Ngoc", "Phuc", "Quyen", "Son", "Thu", "Thang", "Uyen", "Xuan", "Yen", "Mai",
                  "Nhan", "Oanh", "Phuong", "Quang", "Lan Anh", "Thanh", "Trang", "Tuan", "Thao", "Anh", "Binh", "Cam",
                  "Dinh", "Ha", "Hieu", "Long", "Mai", "Nam", "Nga", "Quoc", "Thuy", "Thanh", "Truc"]

    student_names = []
    for _ in range(count):
        full_name = f"{random.choice(first_names)} {random.choice(middle_names)} {random.choice(last_names)}"
        student_names.append(full_name)

    return student_names

# Danh sach ten sinh vien
danh_sach_ten_sinh_vien = generate_student_names(200)

def generate_hanoi_addresses(count):
    streets = ["Hang Bai", "Trang Tien", "Ngo Quyen", "Dien Bien Phu", "Phan Boi Chau", "Ba Trieu", "Le Duan", "Hoang Dieu",
               "Ton Duc Thang", "Ly Thuong Kiet", "Cau Go", "Hang Cot", "Hang Vai", "Hang Be", "Hang Trong", "Hang Ma",
               "Hang Bong", "Hang Gai", "Hang Dong", "Hang Hom", "Hang Da", "Hang Buom", "Hang Khay", "Hang Khoai",
               "Hang Duong", "Hang Tre", "Hang Non", "Hang Thiec", "Hang Ca", "Hang Can", "Hang Chieu", "Hang Bac",
               "Hang Bo", "Hang Luoc", "Hang Quat", "Hang Kho", "Hang Chao", "Hang Dong", "Hang Duong", "Hang Trong",
               "Hang Ngang", "Hang Dao", "Hang Than", "Hang Ruoi", "Hang Voi", "Hang Go", "Hang Son"]

    districts = ["Hoan Kiem", "Ba Dinh", "Hai Ba Trung", "Dong Da", "Cau Giay", "Thanh Xuan", "Tay Ho", "Ha Dong", "Nam Tu Liem"]

    hanoi_addresses = []
    for _ in range(count):
        address = f"{random.choice(streets)}, {random.choice(districts)}, Hanoi"
        hanoi_addresses.append(address)

    return hanoi_addresses

# Danh sach dia chi
danh_sach_dia_chi_giang_vien = generate_hanoi_addresses(50)

def generate_random_phone_number():
    phone_number = "0" + str(random.randint(9, 9))  # Random first digit
    phone_number += "".join([str(random.randint(0, 9)) for _ in range(8)])  # Random remaining 9 digits
    return phone_number

# Danh sach sdt
danh_sach_sdt_giang_vien = [generate_random_phone_number() for _ in range(50)]
danh_sach_sdt_sinh_vien = [generate_random_phone_number() for _ in range(200)]

def generate_random_dates(start_date, end_date, count):
    date_list = []
    for _ in range(count):
        random_days = random.randint(0, (end_date - start_date).days)
        random_date = start_date + timedelta(days=random_days)
        date_list.append(random_date.strftime('%Y-%m-%d'))
    return date_list

start_date1 = datetime(2001, 1, 1)
end_date1 = datetime(2003, 12, 31)

danh_sach_ngsinh_sinh_vien = generate_random_dates(start_date1, end_date1, 200)

start_date2 = datetime(1960, 1, 1)
end_date2 = datetime(1980, 12, 31)

danh_sach_ngsinh_giang_vien = generate_random_dates(start_date2, end_date2, 50)

# Danh sach giang vien
danh_sach_giang_vien = [
    (f'GV_{i+1}', danh_sach_ten_giang_vien[i], 'Nam' if i % 2 == 0 else 'Nu', round(random.random(), 2) * 100000, danh_sach_ngsinh_giang_vien[i], danh_sach_sdt_giang_vien[i], danh_sach_dia_chi_giang_vien[i], '2001/01/01', '2030/01/01') for i in range(0, 50)
]

# Nhap vao database
# try:
#     for element in danh_sach_giang_vien:
#         cursor.execute("""
#                        INSERT INTO giang_vien
#                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
#                        """, element)
#         conn.commit()
# except Exception as e:
#     print(f"Error: {e}")

# Danh sach sinh vien
danh_sach_sinh_vien = [
    (f'{21000000 + i + 1}', danh_sach_ten_sinh_vien[i], 'Nu' if i % 2 == 0 else 'Nam', danh_sach_ngsinh_sinh_vien[i], danh_sach_sdt_sinh_vien[i], random.choice(danh_sach_nganh)[0], 2021, f'K66A{i % 4 + 1}') for i in range(0, 200)
]

# Nhap vao database
# try:
#     for element in danh_sach_sinh_vien:
#         cursor.execute("""
#                        INSERT INTO sinh_vien
#                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
#                        """, element)
#         conn.commit()
# except Exception as e:
#     print(f"Error: {e}")

danh_sach_lich_hoc = []
