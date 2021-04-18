print('从1936年2月开始')
from borax.calendars.lunardate import LunarDate
def input_():
    def year():
        y=input(f"请输入年份：\t")
        if y.isdigit()==True:
            y=eval(y)
            return y
        else:
            print('输入错误，请重新输入')
            year()
    def month():
        m=input(f"请输入月份：\t")
        if m.isdigit()==True:
            m=eval(m)
            return m
        else:
            print('输入错误，请重新输入')
            month()
    def day():
        d=input(f"请输入日期：\t")
        if d.isdigit()==True:
            d=eval(d)
            return d
        else:
            print('输入错误，请重新输入')
            day()
    def time():
        t=input(f"请输入小时(24小时制)：\t")
        if t.isdigit()==True:
            t=eval(t)
            return t
        else:
            print('输入错误，请重新输入')
            time()
    y=year()
    m=month()
    d=day()
    t=time()
    return y,m,d,t
def leap_count(y):
    count=0
    for i in range(1936,y):
        if i%400==0 or (i%4==0 and i%100!=0):
            count+=1
    return count
def year_di(y):
    global dizhi
    dizhi=['子','丑','寅','卯','辰','巳','午','未','申','酉','戌','亥']
    for i in range(13):
        if (y-1924)%12==i:
            p=dizhi[i]
        else:
            continue
    return p
def year_tian(y):
    global tiangan
    tiangan=['甲','乙','丙','丁','戊','己','庚','辛','壬','癸']
    for i in range(11):
        if (y-1924)%10==i:
            q=tiangan[i]
        else:
            continue
    return q
def month_tian(y,m):
    tiangan_yue=['丙','丁','戊','己','庚','辛','壬','癸','甲','乙']
    c=(y-1924)*12+m
    r=c%10
    for i in range(10):
        if r==i:
            return tiangan_yue[i-1]
        else:
            pass
def month_di(y,m):
    dizhi_yue=['寅','卯','辰','巳','午','未','申','酉','戌','亥','子','丑']
    c=(y-1924)*12+m
    r=c%12
    for i in range(12):
        if r==i:
            return dizhi_yue[i-1]
def day_ganzhi(y,m,d):
    ganzhi=['壬子','癸丑','甲寅','乙卯','丙辰','丁巳','戊午','己未','庚申','辛酉','壬戌','癸亥','甲子','乙丑','丙寅','丁卯','戊辰','己巳','庚午','辛未','壬申','癸酉','甲戌','乙亥','丙子','丁丑','戊寅','己卯','庚辰','辛巳','壬午','癸未','甲申','乙酉','丙戌','丁亥','戊子','己丑','庚寅','辛卯','壬辰','癸巳','甲午','乙未','丙申','丁酉','戊戌','己亥','庚子','辛丑','壬寅','癸卯','甲辰','乙巳','丙午','丁未','戊申','己酉','庚戌','辛亥']
    t=leap_count(y)
    d_sum=366*t+365*((y-1936)-t)-30
    d_sum+=count_day(y,m,d)
    for i in range(61):
        if d_sum%60==i:
            return ganzhi[i-1]
        else:
            pass
def count_day(y,m,d):
    yue=[31,28,31,30,31,30,31,31,30,31,30,31]
    if y%400==0 or (y%4==0 and y%100!=0):
        yue[1]=29
    else:
        pass
    sum=0
    for i in range(1,13):
        if i<m:
            sum+=yue[i-1]
        else:
            break
    sum+=d
    return sum     
def Time_dizhi(t):
    l1=[1,3,5,7,9,11,13,15,17,19,21]
    l2=[2,4,6,8,10,12,14,16,18,20,22]
    if t>=23 or t<1:
        return dizhi[0]
    if t in l1:
        for i in range(1,24,2):
            if t<=i:
                return dizhi[int(i/2+0.5)]
    if t in l2:
        for i in range(1,24,2):
            if t<=i:
                return dizhi[int(i/2)]
def Time_tiangan(t):
    tiangan_=[['甲','乙','丙','丁','戊','己','庚','辛','壬','癸','甲','乙'],['丙','丁','戊','己','庚','辛','壬','癸','甲','乙','丙','丁'],['戊','己','庚','辛','壬','癸','甲','乙','丙','丁','戊','己'],['庚','辛','壬','癸','甲','乙','丙','丁','戊','己','庚','辛'],['壬','癸','甲','乙','丙','丁','戊','己','庚','辛','壬','癸']]
    for i in range(5):
        if (dn[0]==tiangan[i] or dn[0]==tiangan[5+i]):
            count=0
            for di in dizhi:
                if Time_dizhi(t)==di:
                    return tiangan_[i][count]
                else:
                    count+=1
                    continue
        else:
            continue
def main():
    global dn
    y,m,d,t=input_()
    day=LunarDate.from_solar_date(y,m,d)
    yn=year_tian(y)+year_di(y)
    mn=month_tian(y,day.month)+month_di(y,day.month)
    dn=day_ganzhi(y,m,d)  
    tn=Time_tiangan(t)+Time_dizhi(t)
    print(f'这天是农历{day.month}月{day.day}日')
    print(yn)
    print(mn)
    print(dn)
    print(tn)
    input('')
main()