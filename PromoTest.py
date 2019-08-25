# -*- encoding=utf8 -*-
__author__ = "bambang"

from airtest.core.api import *
from airtest.core.android.android import Android

android = Android()
displaysize = android.get_current_resolution()

auto_setup(__file__)

def ImageSourcePhone():
    global MainMenu
    global QOA
    global FBContinue
    global FirstName
    global LastName
    global Birthday
    global Male
    global PasswordInput
    global CreateAccount
    global CreateAccountRed
    global BirthdayOK
    global EmailButton
    global PhoneNumberInput
    global GoogleButton
    global LoginButtonRed
    global PhoneNumberButton
    global Promo
    
    MainMenu = Template(r"tpl1542188226027.png", record_pos=(0.009, 0.145), resolution=(1080, 1920))
    QOA = Template(r"tpl1542182470439.png", record_pos=(0.399, 0.044), resolution=(1080, 1920))
    FBContinue = Template(r"tpl1543220745484.png", record_pos=(-0.074, 0.296), resolution=(1440, 2560))
    CreateAccount = Template(r"tpl1543230736825.png", record_pos=(-0.006, 0.668), resolution=(1080, 1920))
    Male = Template(r"tpl1543230787630.png", record_pos=(-0.056, -0.223), resolution=(1080, 1920))
    FirstName = Template(r"tpl1543230794732.png", record_pos=(-0.265, 0.047), resolution=(1080, 1920))
    LastName = Template(r"tpl1543230819455.png", record_pos=(0.118, 0.043), resolution=(1080, 1920))
    Birthday = Template(r"tpl1543230861465.png", record_pos=(-0.195, 0.181), resolution=(1080, 1920))
    BirthdayOK = Template(r"tpl1543230871765.png", record_pos=(0.232, 0.63), resolution=(1080, 1920))
    PasswordInput = Template(r"tpl1543230926129.png", record_pos=(-0.249, -0.459), resolution=(1080, 1920))
    CreateAccountRed = Template(r"tpl1543231037347.png", record_pos=(-0.004, 0.704), resolution=(1080, 1920))
    EmailButton = Template(r"tpl1543230769424.png", record_pos=(0.011, 0.205), resolution=(1080, 1920))
    EmailInput = Template(r"tpl1543230891188.png", record_pos=(-0.244, -0.605), resolution=(1080, 1920))
    PhoneNumberInput = Template(r"tpl1543232624703.png", record_pos=(-0.088, 0.316), resolution=(1080, 1920))
    GoogleButton = Template(r"tpl1543233237455.png", record_pos=(0.02, 0.031), resolution=(1080, 1920))
    LoginButtonRed = Template(r"tpl1543233982539.png", record_pos=(-0.002, 0.519), resolution=(1080, 1920))
    PhoneNumberButton = Template(r"tpl1543231755462.png", record_pos=(0.02, 0.378), resolution=(1080, 1920))
    Promo = Template(r"tpl1543476331164.png", record_pos=(0.194, 0.146), resolution=(1440, 2560))

def LoginUsingNumberSuccess():
    clear_app("com.qraved.app")
    start_app("com.qraved.app")
    sleep(7)
    touch(LoginButtonRed)
    touch(PhoneNumberButton)
    touch(PhoneNumberInput)
    text("08159720265")
    touch(Template(r"tpl1543379705540.png", record_pos=(-0.269, -0.094), resolution=(1440, 2560)))
    text("qraved1234")
    touch(Template(r"tpl1543466339572.png", record_pos=(-0.001, 0.099), resolution=(1440, 2560)))
    touch(Template(r"tpl1542610942345.png", record_pos=(0.413, -0.758), resolution=(1080, 1920)))
    sleep(5)
    touch(Template(r"tpl1542610952345.png", record_pos=(0.402, -0.761), resolution=(1080, 1920)))
    sleep(20)
    print (exists(MainMenu)== False)
    
def SeeAllAvailablePromoInQraved():
    while exists(MainMenu)== False:
        keyevent("back")
    sleep(2)
    touch(Promo)
    swipe ((displaysize[0]*0.55,displaysize[1]*0.5), (displaysize[0]*0.55,displaysize[1]*0.22))
    if exists(Template(r"tpl1543478788840.png", record_pos=(-0.175, 0.108), resolution=(1440, 2560)))== True:
        print ('Fail')
        
def SeePromoForSpecificQOA():
    swipe(Template(r"tpl1543479200135.png", record_pos=(-0.372, 0.594), resolution=(1440, 2560)), vector=[0.0104, -0.4054])
    touch(Template(r"tpl1543479232972.png", record_pos=(0.0, -0.144), resolution=(1440, 2560)))
    swipe(Template(r"tpl1543479261690.png", record_pos=(-0.36, 0.674), resolution=(1440, 2560)), vector=[0.0054, -0.4162])
    swipe ((displaysize[0]*0.90,displaysize[1]*0.40) , (displaysize[0]*0.5,displaysize[1]*0.40))
    if exists(Template(r"tpl1543478788840.png", record_pos=(-0.175, 0.108), resolution=(1440, 2560)))== True:
        print ('Fail')

def SeePromoInHomepagePromoSection():
    while exists(MainMenu)== False:
        keyevent("back")
    sleep(2)
    swipe ((displaysize[0]*0.90,displaysize[1]*0.40) , (displaysize[0]*0.5,displaysize[1]*0.40))
    
    
def SeeQOApromosection():
    
def FindComingSoonPromo():
    
def Findsavedpromothatisalreadyexpired():

def Getinformedthatmysavedpromohasbeenexpired():

def Findmysavedpromothatisalreadysoldout():

def Getinformedthatmysavedpromohasbeensoldout():

def Findmysavedpromothatisalreadyunavailable():
    
def Getinformedthatmysavedpromoisnolongeravailable():
    
def Findoutwhenpromocouponisexpiredremaining tatus():
    
def Findouthowmanystockleftforcouponremainingamount():

def Iwanttoaddpromotomyprofile():
    
def Iwanttofindmysavedpromo():
    
def Iwanttousepromocouponwithoutbarcode():
    
def Iwanttousepromocouponwithbarcode():
    
def Iwanttoseewhoisthepromoprovider():

def Iwanttoseewhatisthepromoperiod():
    
def Iwanttoseewherepromocanbeusedoutletwithoutlet():
    
def Iwanttoseewherepromocanbeusedwhentheresnooutlet():
    
def FindpromoinQOAupdatepageQravedCouponinbox():
    
ImageSourcePhone()
LoginUsingNumberSuccess()