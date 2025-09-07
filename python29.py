# เขียนโปรแกรมคำนวณพื้นที่วงกลม และเส้นรอบวงกลม โดยรับค่ารัศมีทางแป้นพิมพ์ แล้วแสดงผลพื้นที่และเส้นรอบวงกลมที่คำนวณได้ทางหน้าจอ

# - รับค่ารัศมี
# - คํานวณพื้นที่ (3.1416 * radius * radius)
# - คํานวณเส้นรอบวงกลม (2 * 3.1416 * radius)
# - แสดงผลพื้นที่ และเส้นรอบ
# - แสดงชื่อโปรแกรม

def showProgramName() :
    print('+++++++++++++++++++++++')
    print('  Calucator of Circle')
    print('+++++++++++++++++++++++')

def inputRadius() :
    radius = float( input('ป้อนรัศมี : ') )
    return radius

def calArea( r ) :
    return 3.1416 * r * r

def calLine( r ) :
    return 2 * 3.1416 * r

def showAreaAndLine(area, line) :
    print(f'พื้นที่วงกลม : {area:,.2f} ')
    print(f'เส้นรอบวงกลม : {line:,.2f} ')

showProgramName() 
radius = inputRadius()
print('+++++++++++++++++++++++')
area = calArea(radius)
line = calLine(radius)
showAreaAndLine(area, line)
print('+++++++++++++++++++++++')