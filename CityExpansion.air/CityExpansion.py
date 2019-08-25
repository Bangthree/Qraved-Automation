# -*- encoding=utf8 -*-
__author__ = "bambang"

from airtest.core.api import *
from airtest.core.android.android import Android
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

android = Android()
displaysize = android.get_current_resolution()

auto_setup(__file__)

def ImageSourcePhone():
    global MainMenu
    global QOA
    global CityList
    global Nearby
    global EmailButton
    global LoginButtonRed
    global PasswordInput
    global EmailInput
    global PreferenceNext
    global PreferenceFinish

    MainMenu = Template(r"tpl1542188226027.png", record_pos=(0.009, 0.145), resolution=(1080, 1920))
    QOA = Template(r"tpl1542182470439.png", record_pos=(0.399, 0.044), resolution=(1080, 1920))
    CityList = Template(r"tpl1543996847575.png", record_pos=(0.086, -0.761), resolution=(1080, 1920))
    Nearby = Template(r"tpl1543998354807.png", record_pos=(-0.378, 0.155), resolution=(1080, 1920))
    PreferenceNext = Template(r"tpl1542610942345.png", record_pos=(0.413, -0.758), resolution=(1080, 1920))
    PreferenceFinish = Template(r"tpl1542610952345.png", record_pos=(0.402, -0.761), resolution=(1080, 1920))
    LoginButtonRed = Template(r"tpl1543999806831.png", record_pos=(-0.002, 0.518), resolution=(1080, 1920))
    EmailButton = Template(r"tpl1543230769424.png", record_pos=(0.011, 0.205), resolution=(1080, 1920))
    EmailInput = Template(r"tpl1543230891188.png", record_pos=(-0.244, -0.605), resolution=(1080, 1920))
    PasswordInput = Template(r"tpl1543230926129.png", record_pos=(-0.249, -0.459), resolution=(1080, 1920))

    
def ChangeCurrentCitytoNewCities():
    clear_app("com.qraved.app")
    start_app("com.qraved.app")
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
    poco("com.qraved.app:id/tvLogin").click()
    touch(Template(r"tpl1544000437729.png", record_pos=(0.021, 0.199), resolution=(1080, 1920)))
    poco("com.qraved.app:id/etEmail").click()
    text("Rosabella.sarudin@qraved.com")
    poco("com.qraved.app:id/etPassword").click()
    text("qraved1234")
    poco("com.qraved.app:id/bLogin").click()
    sleep(3)
    poco(text="Steak").click()
    poco("com.qraved.app:id/ctvDoNext").click()
    poco("com.qraved.app:id/ctvDoNext").click()
    sleep(10)
    print (exists(MainMenu)== False)
    sleep(10)
    poco("com.qraved.app:id/llCityName").child("android.widget.ImageView").click()
    touch(Template(r"tpl1544001929815.png", record_pos=(-0.368, -0.306), resolution=(1080, 1920)))
    sleep(2)
    touch(Nearby)
    sleep(5)
    print (exists(Template(r"tpl1544081930757.png", record_pos=(0.004, -0.067), resolution=(1080, 1920)))== False)
    sleep(2)
    poco("com.qraved.app:id/ivBack").click()
    poco("com.qraved.app:id/llCityName").child("android.widget.ImageView").click()
    touch(Template(r"tpl1543996884070.png", record_pos=(-0.413, -0.155), resolution=(1080, 1920)))
    sleep(2)
    touch(Nearby)
    sleep(7)
    print (exists(Template(r"tpl1544081960836.png", record_pos=(-0.004, -0.092), resolution=(1080, 1920)))== False)
    sleep(2)
    poco("com.qraved.app:id/ivBack").click()
    poco("com.qraved.app:id/llCityName").child("android.widget.ImageView").click()
    touch(Template(r"tpl1543996902079.png", record_pos=(-0.359, 0.002), resolution=(1080, 1920)))
    sleep(2)
    touch(Nearby)
    sleep(7)
    print (exists(Template(r"tpl1544081996435.png", record_pos=(0.001, -0.069), resolution=(1080, 1920)))== False)
    sleep(2)
    poco("com.qraved.app:id/ivBack").click()
    poco("com.qraved.app:id/llCityName").child("android.widget.ImageView").click()
    touch(Template(r"tpl1543996921425.png", record_pos=(-0.356, 0.152), resolution=(1080, 1920)))
    sleep(2)
    touch(Nearby)
    sleep(7)
    print (exists(Template(r"tpl1544082039421.png", record_pos=(0.004, -0.109), resolution=(1080, 1920)))== False)
    sleep(2)
    poco("com.qraved.app:id/ivBack").click()
    poco("com.qraved.app:id/llCityName").child("android.widget.ImageView").click()
    touch(Template(r"tpl1543996939736.png", record_pos=(-0.384, 0.304), resolution=(1080, 1920)))
    sleep(2)
    touch(Nearby)
    sleep(7)
    print (exists(Template(r"tpl1544082080760.png", record_pos=(0.006, -0.111), resolution=(1080, 1920)))== False)
    sleep(2)
    poco("com.qraved.app:id/ivBack").click()
    poco("com.qraved.app:id/llCityName").child("android.widget.ImageView").click()
    touch(Template(r"tpl1543996957548.png", record_pos=(-0.347, 0.458), resolution=(1080, 1920)))
    sleep(2)
    touch(Nearby)
    sleep(7)
    print (exists(Template(r"tpl1544082114447.png", record_pos=(-0.001, -0.07), resolution=(1080, 1920)))== False)
    sleep(2)
    poco("com.qraved.app:id/ivBack").click()
    
    poco("com.qraved.app:id/llCityName").child("android.widget.ImageView").click()
    touch(Template(r"tpl1544079241714.png", record_pos=(-0.338, 0.609), resolution=(1080, 1920)))
    sleep(2)
    touch(Nearby)
    sleep(7)
    print (exists(Template(r"tpl1544079269856.png", record_pos=(0.001, -0.109), resolution=(1080, 1920)))== False)
    sleep(2)
    poco("com.qraved.app:id/ivBack").click()

    poco("com.qraved.app:id/llCityName").child("android.widget.ImageView").click()
    touch(Template(r"tpl1544079299940.png", record_pos=(-0.371, 0.763), resolution=(1080, 1920)))
    sleep(2)
    touch(Nearby)
    sleep(7)
    print (exists(Template(r"tpl1544079329652.png", record_pos=(0.001, -0.118), resolution=(1080, 1920)))== False)
    sleep(2)
    poco("com.qraved.app:id/ivBack").click()
    poco("com.qraved.app:id/llCityName").child("android.widget.ImageView").click()
    swipe(Template(r"tpl1544080665699.png", record_pos=(-0.341, 0.61), resolution=(1080, 1920)), vector=[-0.0109, -0.3375])
    touch(Template(r"tpl1544080844466.png", record_pos=(-0.344, 0.698), resolution=(1080, 1920)))
    sleep(2)
    touch(Nearby)
    sleep(7)
    print (exists(Template(r"tpl1544080867695.png", record_pos=(-0.004, -0.115), resolution=(1080, 1920)))== False)
    sleep(2)
    poco("com.qraved.app:id/ivBack").click()
    
    poco("com.qraved.app:id/llCityName").child("android.widget.ImageView").click()
    swipe(Template(r"tpl1544080665699.png", record_pos=(-0.341, 0.61), resolution=(1080, 1920)), vector=[-0.0109, -0.3375])
    touch(Template(r"tpl1544080970098.png", record_pos=(-0.405, 0.851), resolution=(1080, 1920)))
    sleep(2)
    touch(Nearby)
    sleep(7)
    print (exists(Template(r"tpl1544080992533.png", record_pos=(-0.002, -0.109), resolution=(1080, 1920)))== False)
    sleep(2)
    poco("com.qraved.app:id/ivBack").click()
    poco("com.qraved.app:id/llCityName").child("android.widget.ImageView").click()
    touch(Template(r"tpl1543996972777.png", record_pos=(-0.335, -0.46), resolution=(1080, 1920)))
    sleep(2)
    touch(Nearby)
    sleep(7)
    print (exists(Template(r"tpl1544082982935.png", record_pos=(-0.001, -0.063), resolution=(1080, 1920)))== False)
    sleep(2)
    poco("com.qraved.app:id/ivBack").click()

ImageSourcePhone()
ChangeCurrentCitytoNewCities()