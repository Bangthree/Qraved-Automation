# -*- encoding=utf8 -*-
__author__ = "bambang"

from airtest.core.api import *
from airtest.core.android.android import Android
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

android = Android()
displaysize = android.get_current_resolution()
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

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
    global EmailInput
    global PhoneNumberInput
    global GoogleButton
    global LoginButtonRed
    global PhoneNumberButton
    global ReferralInputSign
    global Profile
    global ReferralCodeSection
    global SettingButton
    
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
    ReferralInputSign = Template(r"tpl1543798302109.png", record_pos=(-0.152, 0.532), resolution=(1080, 1920))
    Profile = Template(r"tpl1543803498956.png", record_pos=(0.399, 0.815), resolution=(1080, 1920))
    ReferralCodeSection = Template(r"tpl1543803594671.png", record_pos=(-0.002, 0.177), resolution=(1080, 1920))
    SettingButton = Template(r"tpl1543803958582.png", record_pos=(0.421, -0.758), resolution=(1080, 1920))
    ReferralHistory = Template(r"tpl1543804109878.png", record_pos=(-0.006, 0.381), resolution=(1080, 1920))
    PhoneVerification = Template(r"tpl1544097332645.png", record_pos=(-0.006, -0.619), resolution=(1080, 1920))
    
def InputVALIDReferralCodewhensignup(): #Done
    clear_app("com.qraved.app")
    start_app("com.qraved.app")
    sleep(7)
    poco("com.qraved.app:id/tvLoginCreateAccount").click()
    touch(EmailButton)
    poco("com.qraved.app:id/ivMale").click()
    poco("com.qraved.app:id/cetFirstName").click()
    text("Arsello")
    poco("com.qraved.app:id/cetLastName").click()
    text("Svennn")
    touch(Birthday) 
    sleep(2)
    touch(BirthdayOK)
    poco("com.qraved.app:id/cetEmail").click()
    text("123@gmail.com")
    poco("com.qraved.app:id/cetPassword").click()
    text("November")
    swipe(Template(r"tpl1544095663687.png", record_pos=(0.302, 0.601), resolution=(1080, 1920)), vector=[-0.0244, -0.2088])
    poco("com.qraved.app:id/editReferralCode").click()
    text("3ARAYJ")
    poco("com.qraved.app:id/btSignUp").click()
    if (exists(Template(r"tpl1544097332645.png", record_pos=(-0.006, -0.619), resolution=(1080, 1920)))):
        print ('Success')

def InputINVALIDReferralCodewhensignup():
    clear_app("com.qraved.app")
    start_app("com.qraved.app")
    sleep(7)
    poco("com.qraved.app:id/tvLoginCreateAccount").click()
    touch(EmailButton)
    poco("com.qraved.app:id/ivMale").click()
    poco("com.qraved.app:id/cetFirstName").click()
    text("Arsello")
    poco("com.qraved.app:id/cetLastName").click()
    text("Svennn")
    touch(Birthday)
    sleep(2)
    touch(BirthdayOK)
    poco("com.qraved.app:id/cetEmail").click()
    text("akunmalessxx@gmail.com")
    poco("com.qraved.app:id/cetPassword").click()
    text("November7")
    swipe(Template(r"tpl1544095663687.png", record_pos=(0.302, 0.601), resolution=(1080, 1920)), vector=[-0.0244, -0.2088])
    poco("com.qraved.app:id/editReferralCode").click()
    text("HAPPYNEWYEAR")
    poco("com.qraved.app:id/btSignUp").click()
    sleep(3)
    if (exists(Template(r"tpl1543808210015.png", record_pos=(-0.004, 0.022), resolution=(1080, 1920)))) : 
        print ('Input INVALID Referral Code when sign up Success')  #Done
    
def Skipreferralcodeusingemailphonenumber(): #Done
    clear_app("com.qraved.app")
    start_app("com.qraved.app")
    sleep(7)
    poco("com.qraved.app:id/tvLoginCreateAccount").click()
    touch(EmailButton)
    poco("com.qraved.app:id/ivMale").click()
    poco("com.qraved.app:id/cetFirstName").click()
    text("Arselle")
    poco("com.qraved.app:id/cetLastName").click()
    text("Emma")
    touch(Birthday)
    sleep(2)
    touch(BirthdayOK)
    poco("com.qraved.app:id/cetEmail").click()
    text("o123@gmail.com")
    poco("com.qraved.app:id/cetPassword").click()
    text("November7")
    swipe(Template(r"tpl1544095663687.png", record_pos=(0.302, 0.601), resolution=(1080, 1920)), vector=[-0.0244, -0.2088])
    poco("com.qraved.app:id/btSignUp").click()
    sleep(7)
    if (exists(Template(r"tpl1544097332645.png", record_pos=(-0.006, -0.619), resolution=(1080, 1920)))):
        print ('Skip referral code using email phone number success')

def Skipreferralcodeusingsocialmedia(): #Make sure there's new account ready on the device
    clear_app("com.qraved.app")
    start_app("com.qraved.app")
    sleep(10)
    poco("com.qraved.app:id/tvLoginCreateAccount").click()
    touch(GoogleButton)
    touch(Template(r"tpl1543233257945.png", record_pos=(-0.101, 0.043), resolution=(1080, 1920)))
    sleep(3)
    touch(Template(r"tpl1542610942345.png", record_pos=(0.413, -0.758), resolution=(1080, 1920)))
    sleep(5)
    touch(Template(r"tpl1542610952345.png", record_pos=(0.402, -0.761), resolution=(1080, 1920)))
    sleep(20)
    if (exists(Template(r"tpl1544097332645.png", record_pos=(-0.006, -0.619), resolution=(1080, 1920)))):
        print ('Skip referral code using social media success')
        touch(Template(r"tpl1543807935538.png", record_pos=(0.415, -0.758), resolution=(1080, 1920)))
    print (exists(MainMenu)== False)

def SkipPhoneVerificationafterinputingvalidreferralcode(): #Done
    clear_app("com.qraved.app")
    start_app("com.qraved.app")
    sleep(7)
    poco("com.qraved.app:id/tvLoginCreateAccount").click()
    touch(EmailButton)
    touch(Male)
    poco("com.qraved.app:id/ivMale").click()
    text("Satua")
    poco("com.qraved.app:id/cetLastName").click()
    text("Satub")
    touch(Birthday)
    sleep(2)
    touch(BirthdayOK)
    poco("com.qraved.app:id/cetEmail").click()
    text("Satu@Satu.com")
    poco("com.qraved.app:id/cetPassword").click()
    text("November7")
    swipe(Template(r"tpl1544095663687.png", record_pos=(0.302, 0.601), resolution=(1080, 1920)), vector=[-0.0244, -0.2088])
    touch(ReferralInputSign)
    text("3ARAYJ")
    poco("com.qraved.app:id/btSignUp").click()
    if (exists(Template(r"tpl1544097332645.png", record_pos=(-0.006, -0.619), resolution=(1080, 1920)))):
        print ('Skip Phone Verification after inputing valid referral code Success')
        touch(Template(r"tpl1543807935538.png", record_pos=(0.415, -0.758), resolution=(1080, 1920)))
    print (exists(MainMenu)== False)

def SeeReferralCodeSection(): #User must already login
    while exists(MainMenu)== False:
        keyevent("back")
    sleep(2)
    poco("com.qraved.app:id/ivSetting").click()
    sleep(3)
    if (exists(Template(r"tpl1543803594671.png", record_pos=(-0.002, 0.177), resolution=(1080, 1920)))): 
        print ('See Referral Code Section Passed')
    poco("com.qraved.app:id/rlHeader").child("android.widget.LinearLayout").child("android.widget.LinearLayout").child("com.qraved.app:id/ivSetting").click()
    poco("com.qraved.app:id/ctvReferralCode").click()
    if (exists(Template(r"tpl1543803594671.png", record_pos=(-0.002, 0.177), resolution=(1080, 1920)))): 
        print ('See Referral Code Section Passed')
    
def SeeReferralHistoryList(): # User must already login
    while exists(MainMenu)== False:
        keyevent("back")
    sleep(2)
    poco("com.qraved.app:id/ivSetting").click()
    poco("com.qraved.app:id/tvViewReferralHistory").click()
    sleep(3)
    if (exists(Template(r"tpl1544151518472.png", record_pos=(0.006, 0.305), resolution=(1080, 1920)))):
        print : ('See Referral History List Passed')
    keyevent("back")
    poco("com.qraved.app:id/rlHeader").child("android.widget.LinearLayout").child("android.widget.LinearLayout").child("com.qraved.app:id/ivSetting").click()
    poco("com.qraved.app:id/ctvReferralCode").click()
    sleep(3)
    if (exists(Template(r"tpl1544151518472.png", record_pos=(0.006, 0.305), resolution=(1080, 1920)))):
        print ('See Referral History List Passed')

def GotoTermsConditionPage(): #User must already login
    while exists(MainMenu)== False:
        keyevent("back")
    sleep(2)
    poco("com.qraved.app:id/ivSetting").click()
    poco("com.qraved.app:id/rlHeader").child("android.widget.LinearLayout").child("android.widget.LinearLayout").child("com.qraved.app:id/ivSetting").click()
    poco("com.qraved.app:id/ctvReferralCode").click()
    touch(Template(r"tpl1543804849643.png", record_pos=(-0.012, -0.218), resolution=(1080, 1920)))
    sleep(5)
    if (exists(Template(r"tpl1543804882589.png", record_pos=(0.008, 0.09), resolution=(1080, 1920)))):
        print ('Go to Terms Condition Page is Passed')
        
        poco("Instagram").click()
        poco("Message").click()

        
ImageSourcePhone()
#InputVALIDReferralCodewhensignup()
#InputINVALIDReferralCodewhensignup()
#Skipreferralcodeusingemailphonenumber()
#Skipreferralcodeusingsocialmedia()
SkipPhoneVerificationafterinputingvalidreferralcode()
SeeReferralCodeSection()
SeeReferralHistoryList()
GotoTermsConditionPage()