# สร้างโปรแกรมเครื่องคำนวณของตัวเลข 2 จำนวนที่รับทางแป้นพิมพ์ ได้แก่ บวก ลบ คูณ หาร โดยทำเป็นเมนูให้ผู้ใช้เลือก ผู้ใช้เลือกเมนูไหนให้คำนวณตามเมนูนั้นๆ แล้วเสดงผล

# แสดงชื่อโปรแกรม
# รับค่าตัวเลข 2 จำนวน
# แสดงเมนูให้ผู้ใช้เลือก
# การคำนวณตามเมนูที่ผู้ใช้เลือก
# การแสดงผลลัพธ์ที่ได้จากการคำนวณ

def showHeader() :
    print('@@@@@@@@@@@@@@@@@@@@@')
    print('     เครื่องคิดเลข')
    print('@@@@@@@@@@@@@@@@@@@@@')
def showMenuAndSelect() :
    print('1. บวก')
    print('2. ลบ')
    print('3. คูณ')
    print('4. หาร')
    menu = int(input('ป้อนเมนูที่ต้องการคํานวณ : '))
    print('@@@@@@@@@@@@@@@@@@@@@')
    return menu
def calculator() :
    menu = showMenuAndSelect()
    num1 = float(input('ป้อนตัวเลขที่ 1 : '))
    num2 = float(input('ป้อนตัวเลขที่ 2 : '))
    print('@@@@@@@@@@@@@@@@@@@@@')
    if menu == 1 :
        print(f'{num1} + {num2} = {num1 + num2}')
    elif menu == 2 :
        print(f'{num1} - {num2} = {num1 - num2}')
    elif menu == 3 :
        print(f'{num1} * {num2} = {num1 * num2}')
    elif menu == 4 :
        print(f'{num1} / {num2} = {num1 / num2}')
    else :
        print('คุณเลือกเมนูไม่ถูกต้อง')
    print('@@@@@@@@@@@@@@@@@@@@@')
showHeader()
calculator()
    