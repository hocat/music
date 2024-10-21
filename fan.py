import RPi.GPIO as GPIO  #导入gpio口驱动模块
import time              #导入时间模块
pwm_pin = 12             #定义pwm输出引脚(注意BCM编码的对应关系)


GPIO.setmode(GPIO.BCM)   #定义树莓派gpio引脚以BCM方式编号
GPIO.setup(pwm_pin,GPIO.OUT)  #使能gpio口为输出
pwm = GPIO.PWM(pwm_pin,100)   #定义pwm输出频率
pwm.start(50)   #占空比（范围：0.0 <=  >= 100.0）


while(1):
    # 打开文件
    file = open("/sys/class/thermal/thermal_zone0/temp")
    # 读取结果，并转换为浮点数
    temp = float(file.read()) / 1000
    # 关闭文件
    file.close()

    if(temp >= 60):
        Duty = 100
    elif(temp >= 55):
        Duty = 90
    elif(temp >= 53):
        Duty = 75
    elif(temp >= 50):
        Duty = 60
    elif(temp >= 45):
        Duty = 45
    elif(temp >= 43):
        Duty = 40
    else:
        Duty = 35

    pwm.ChangeDutyCycle(Duty)
    # 向控制台打印
    print("temp : %.1f,duty : %d" %(temp,Duty))
    time.sleep(10)