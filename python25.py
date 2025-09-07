# 2. Function มี parameter และไม่มี return
# มี parameter คือ มีอะไรในวงเล็บหลังชื่อฟังก์ชัน
# parameter ถือว่าเป็นตัวแปรประเภทหนึ่ง แต่จะใช้ได้เฉพาะในฟังก์ชันนั้นเท่านั้น
# ไม่มี return คือ ไม่มีคำสั่ง return ในตัวฟังก์ชัน

def sumNumber(aa, bb) : #อย่าลืม colon 
    print(f'ผลรวมของ {aa} และ {bb} เท่ากับ {aa + bb}')
    print('Ok นะ จ๊ะ ^_^')

def avarageNumber(n1, n2, n3, n4) : #อย่าลืม colon 
    print(f'ค่าเฉลี่ยของเลข {n1}, {n2}, {n3}, {n4} คือ {(n1 + n2 + n3 + n4) / 4}')
    print('เข้าใจตรงกัน...')

sumNumber(10, 20 )  #ข้อมูลที่ส่งให้พารามิเตอร์ เรียก Argument
sumNumber(111, 222 )
print('------------------')
avarageNumber(10, 20, 32, 10)
print('------------------')
print('     ^_^')