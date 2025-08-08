import oracledb
import os

# กำหนดข้อมูลการเชื่อมต่อ
username = "SYS"
password = "welcome1"
host = "10.151.1.75"
port = "1521"
service_name = "bmatraffice"

try:
    # เชื่อมต่อในโหมด SYSDBA
    connection = oracledb.connect(
        user=username,
        password=password,
        dsn=f"{host}:{port}/{service_name}",
        mode=oracledb.SYSDBA
    )
    
    print("การเชื่อมต่อสำเร็จ!")
    
    # สร้าง cursor
    cursor = connection.cursor()
    
    # ทดลองรันคำสั่ง SQL
    cursor.execute("SELECT * FROM BMA_PHASE_II.USERS WHERE ROWNUM <= 5")
    
    # ดึงผลลัพธ์
    for row in cursor:
        print(row)
    
    # ปิด cursor และ connection
    cursor.close()
    connection.close()
    
except Exception as error:
    print(f"เกิดข้อผิดพลาด: {error}")