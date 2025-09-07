def showProgramName() :
    printPa()
    print('  Calucator of Circle')
    printPa()

def inputRadius() :
    radius = float( input('ป้อนรัศมี : ') )
    return radius

def calAndShow() :
    r = inputRadius()    
    printPa()
    print(f'พื้นที่วงกลม : { 3.1416 * r * r:,.2f} ')
    print(f'เส้นรอบวงกลม : {2 * 3.1416 * r:,.2f} ')
    printPa()

def printPa() : 
    print('=======================')

showProgramName()
calAndShow()