from pydantic import BaseModel
from fastapi import FastAPI, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
import mysql.connector

from fastapi.middleware.cors import CORSMiddleware
from fastapi import Cookie

import render


app = FastAPI()


host = "127.0.0.1"
user = "root"
password = ""
database = "csdl_web"

connect = mysql.connector.connect(host = host, user = user, password = password, database = database)
cursor = connect.cursor(dictionary=True)


# @app.get("/student")
# def get_student_info(logged_in: bool = Cookie(default=False), username: str = Cookie(default=None)):
#     if logged_in:
#         # Người dùng đã đăng nhập, bạn có thể thực hiện các thao tác để lấy thông tin sinh viên từ nguồn dữ liệu của bạn
#         # Ví dụ: truy vấn cơ sở dữ liệu hoặc đọc từ tệp tin
#         return username
#     else:
#         # Người dùng chưa đăng nhập, trả về lỗi không xác thực
#         raise HTTPException(status_code=401, detail="Not authenticated")


@app.post("/grade")
async def sendGrade(request: Request):
    # user = get_student_info()
    columns = [
        {
            "title": "Mã môn học",
            "dataIndex": "ma_hp",
            "key": "ma_hp",
        },
        {
            "title": "Môn học",
            "dataIndex": "ten_hp",
            "key": "ten_hp",
        },
        {
            "title": "Số tín chỉ",
            "dataIndex": "so_tin",
            "key": "so_tin",
        },
        {
            "title": "Điểm hệ 10",
            "dataIndex": "he10",
            "key": "he10",
        },
        {
            "title": "Điểm chữ",
            "dataIndex": "diem",
            "key": "diem",
        },
        {
            "title": "Điểm hệ 4",
            "dataIndex": "he4",
            "key": "he4",
        },
    ]

    expand_columns = [
        {
            "title": "STT",
            "dataIndex": "stt",
            "key": "stt",
        },
        {
            "title": "Bản chất kỳ thi",
            "dataIndex": "type",
            "key": "type",
        },
        {
            "title": "Hệ số",
            "dataIndex": "he_so",
            "key": "he_so",
        },
        {
            "title": "Lần thi",
            "dataIndex": "lan",
            "key": "lan",
        },
        {
            "title": "Điểm",
            "dataIndex": "diem",
            "key": "diem",
        },
    ]

    statement = """
                    with dk as (
                    select *, diem_tx * he_so_tx + diem_gk * he_so_gk + diem_ck * he_so_ck as total_score
                    from dang_ky 
                    where ma_sv = '21002510'
                    )
                    select 
                        row_number() over () as 'key',
                        lh.ma_hp,
                        hp.ten_hp,
                        hp.so_tin,
                        dk.total_score as he10,
                        case
                            when dk.total_score < 4.0 then 'F'
                            when dk.total_score <= 4.9 then 'D'
                            when dk.total_score <= 5.4 then 'D+'
                            when dk.total_score <= 6.4 then 'C'
                            when dk.total_score <= 6.9 then 'C+'
                            when dk.total_score <= 7.9 then 'B'
                            when dk.total_score <= 8.4 then 'B+'
                            when dk.total_score <= 8.9 then 'A'
                            else 'A+'
                        end as diem,
                        case
                            when dk.total_score < 4.0 then 0
                            when dk.total_score <= 4.9 then 1
                            when dk.total_score <= 5.4 then 1.5
                            when dk.total_score <= 6.4 then 2
                            when dk.total_score <= 6.9 then 2.5
                            when dk.total_score <= 7.9 then 3
                            when dk.total_score <= 8.4 then 3.5
                            when dk.total_score <= 8.9 then 3.7
                            else 4
                        end as he4
                    from
                        hoc_phan hp
                        join lich_hoc lh on lh.ma_hp = hp.ma_hp
                        join dk on dk.ma_lh = lh.ma_lh;
                """

    cursor.execute(statement)
    data = cursor.fetchall()

    for element in data:
        element['he10'] = round(element['he10'],1)


    expand_data = [
        {
            "key": "1",
            "stt": 1,
            "type": "Thi cuối kì",
            "he_so": 0.6,
            "lan": 1,
            "diem": 10,
        },
        {
            "key": "2",
            "stt": 2,
            "type": "Giữa kì",
            "he_so": 0.2,
            "lan": 1,
            "diem": 10,
        },
        {
            "key": "3",
            "stt": 3,
            "type": "Thường xuyên",
            "he_so": 0.2,
            "lan": 1,
            "diem": 10,
        },
    ]


    return {"columns": columns, "expand_columns": expand_columns, "data": data, "expand_data": expand_data}


# Cập nhật các URL cho phù hợp với URL của ứng dụng frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)