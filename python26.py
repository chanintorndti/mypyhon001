# 3. Function ไม่มี parameter และมี return 
# มี return คือ มีคำสั่ง return ในตัวฟังก์ชันพร้อมกับข้อมูลที่จะส่งกลับไปยังจุดเรียกใช้ฟังก์ชัน

def funcWow() :
    return 'Wow wow wow'

def funcHi() :
    print('Hi hi hi')
    return 'สวัสดี...'

print( funcWow() )
dti = funcWow()
print(dti, dti , dti)

print(f'{funcHi()} สมชาย')