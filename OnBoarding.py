# -*- encoding=utf8 -*-
__author__ = "bambang"

from airtest.core.api import *
from airtest.core.android.android import Android
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

android = Android()
displaysize = android.get_current_resolution()
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)

#def ImageSourcePhone():
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
    global CarouselPicA
    global CarouselPicB
    global CarouselPicC
    global CarouselPicD
    global CarouselPicE
    global PreferenceNext
    global PreferenceFinish
    global FalsePassword
    global FBSignup
    MainMenu = Template(r"tpl1542188226027.png", record_pos=(0.009, 0.145), resolution=(1080, 1920))
    QOA = Template(r"tpl1542182470439.png", record_pos=(0.399, 0.044), resolution=(1080, 1920))
    FBContinue = Template(r"tpl1543220745484.png", record_pos=(-0.074, 0.296), resolution=(1440, 2560))
    CreateAccount = Template(r"tpl1543230736825.png", record_pos=(-0.006, 0.668), resolution=(1080, 1920))
    Male = Template(r"tpl1543230787630.png", record_pos=(-0.056, -0.223), resolution=(1080, 1920))
    FirstName = Template(r"tpl1543230794732.png", record_pos=(-0.265, 0.047), resolution=(1080, 1920))
    LastName = Template(r"tpl1543230819455.png", record_pos=(0.118, 0.043), resolution=(1080, 1920))
    Birthday = Template(r"tpl1543230861465.png", record_pos=(-0.195, 0.181), resolution=(1080, 1920))
    BirthdayOK = Template(r"tpl1543230871765.png", record_pos=(0.232, 0.63), resolution=(1080, 1920))
    PreferenceNext = Template(r"tpl1542610942345.png", record_pos=(0.413, -0.758), resolution=(1080, 1920))
    PreferenceFinish = Template(r"tpl1542610952345.png", record_pos=(0.402, -0.761), resolution=(1080, 1920))
    PasswordInput = Template(r"tpl1543230926129.png", record_pos=(-0.249, -0.459), resolution=(1080, 1920))
    CreateAccountRed = Template(r"tpl1543231037347.png", record_pos=(-0.004, 0.704), resolution=(1080, 1920))
    EmailButton = Template(r"tpl1543230769424.png", record_pos=(0.011, 0.205), resolution=(1080, 1920))
    EmailInput = Template(r"tpl1543230891188.png", record_pos=(-0.244, -0.605), resolution=(1080, 1920))
    PhoneNumberInput = Template(r"tpl1543232624703.png", record_pos=(-0.088, 0.316), resolution=(1080, 1920))
    GoogleButton = Template(r"tpl1543233237455.png", record_pos=(0.02, 0.031), resolution=(1080, 1920))
    LoginButtonRed = Template(r"tpl1543233982539.png", record_pos=(-0.002, 0.519), resolution=(1080, 1920))
    PhoneNumberButton = Template(r"tpl1543231755462.png", record_pos=(0.02, 0.378), resolution=(1080, 1920))
    CarouselPicA = Template(r"tpl1543393080762.png", record_pos=(0.01, -0.286), resolution=(1080, 1920))
    CarouselPicB = Template(r"tpl1543392632635.png", record_pos=(0.008, -0.286), resolution=(1080, 1920))
    CarouselPicC = Template(r"tpl1543392559885.png", record_pos=(0.008, -0.282), resolution=(1080, 1920))
    CarouselPicD = Template(r"tpl1543392526892.png", record_pos=(0.008, -0.286), resolution=(1080, 1920))
    CarouselPicE = Template(r"tpl1543392390448.png", record_pos=(0.0, -0.292), resolution=(1080, 1920))
    FalsePassword = Template(r"tpl1544099719535.png", record_pos=(-0.006, 0.019), resolution=(1080, 1920))
    FBSignup = Template(r"tpl1546934025384.png", record_pos=(0.01, -0.616), resolution=(1080, 1920))

#def SignUpUsingFacebook():
    clear_app("com.qraved.app")
    start_app("com.qraved.app")
    sleep(10)
    poco("com.qraved.app:id/tvLoginCreateAccount").click()
    poco("com.qraved.app:id/ctvFacebook").click()
    sleep(7)
    if poco('android.webkit.WebView').exists()== True():
        poco("m_login_email").click()
        text("akunmales@gmail.com")
        sleep(2)
        poco("m_login_password").click()
        text("November7")
        sleep(2)
        poco('android.view.View', text='u_0_4').click()
    elif poco('android.webkit.WebView').exists()== False():
        sleep(5)
    sleep(5)
    
    if exists(PreferenceNext):
        touch(PreferenceNext)
        sleep(5)
        touch(PreferenceFinish)
        sleep(3)
    print (exists(MainMenu)== False) #Okay
        
#def SignUpUsingEmailNew():
    clear_app("com.qraved.app")
    start_app("com.qraved.app")
    sleep(7)
    poco("com.qraved.app:id/tvLoginCreateAccount").click()
    touch(EmailButton)
    poco("com.qraved.app:id/ivMale").click()
    poco("com.qraved.app:id/cetFirstName").click()
    text("Arselle")
    poco("com.qraved.app:id/cetLastName").click()
    text("Svennn")
    touch(Birthday)
    sleep(2)
    touch(BirthdayOK)
    poco("com.qraved.app:id/cetEmail").click()
    text("12@Coba.com")
    poco("com.qraved.app:id/cetPassword").click()
    text("November7")
    swipe(Template(r"tpl1544095663687.png", record_pos=(0.302, 0.601), resolution=(1080, 1920)), vector=[-0.0244, -0.2088])
    poco("com.qraved.app:id/btSignUp").click()
    sleep(3)
    poco("com.qraved.app:id/skipVerify").click()
    touch(PreferenceNext)
    sleep(5)
    touch(PreferenceFinish)
    sleep(3)
    print (exists(MainMenu)== False)

#def SignUpUsingEmailRegistered():
#Do email & phone cleanup before performing Signup using email
    clear_app("com.qraved.app")
    start_app("com.qraved.app")
    sleep(7)
    poco("com.qraved.app:id/tvLoginCreateAccount").click()
    touch(EmailButton)
    poco("com.qraved.app:id/ivMale").click()
    poco("com.qraved.app:id/cetFirstName").click()
    text("Arselle")
    poco("com.qraved.app:id/cetLastName").click()
    text("Sven")
    touch(Birthday)
    touch(BirthdayOK)
    poco("com.qraved.app:id/cetEmail").click()
    text("akunmalessss@gmail.com")
    poco("com.qraved.app:id/cetPassword").click()
    text("November7")
    swipe(Template(r"tpl1544095663687.png", record_pos=(0.302, 0.601), resolution=(1080, 1920)), vector=[-0.0244, -0.2088])
    poco("com.qraved.app:id/btSignUp").click()
    sleep(7)
    print (exists(Template(r"tpl1544096273931.png", record_pos=(-0.002, 0.024), resolution=(1080, 1920)))== False)

#def SignUpUsingPhoneNumberSuccessAndExist():
    clear_app("com.qraved.app")
    start_app("com.qraved.app")
    sleep(7)
    poco("com.qraved.app:id/tvLoginCreateAccount").click()
    touch(Template(r"tpl1543231755462.png", record_pos=(0.02, 0.378), resolution=(1080, 1920)))
    poco("com.qraved.app:id/ivMale").click()
    poco("com.qraved.app:id/cetFirstName").click()
    text("Arselle")
    poco("com.qraved.app:id/cetLastName").click()
    text("Sven")
    touch(Birthday)
    touch(BirthdayOK)
    poco("com.qraved.app:id/etPhoneNumberLogin").click()
    text("085643628232")
    poco("com.qraved.app:id/cetPassword").click()
    text("November7")
    swipe(Template(r"tpl1544095663687.png", record_pos=(0.302, 0.601), resolution=(1080, 1920)), vector=[-0.0244, -0.2088])
    poco("com.qraved.app:id/btSignUp").click()
    sleep(3)
    print (exists(Template(r"tpl1544097332645.png", record_pos=(-0.006, -0.619), resolution=(1080, 1920)))== False)
    sleep(2)
    clear_app("com.qraved.app")
    start_app("com.qraved.app")
    sleep(7)
    poco("com.qraved.app:id/tvLoginCreateAccount").click()
    touch(Template(r"tpl1543231755462.png", record_pos=(0.02, 0.378), resolution=(1080, 1920)))
    poco("com.qraved.app:id/ivMale").click()
    poco("com.qraved.app:id/cetFirstName").click()
    text("Arselle")
    poco("com.qraved.app:id/cetLastName").click()
    text("Sven")
    touch(Birthday)
    touch(BirthdayOK)
    poco("com.qraved.app:id/etPhoneNumberLogin").click()
    text("085123456789")
    poco("com.qraved.app:id/cetPassword").click()
    text("November7")
    swipe(Template(r"tpl1544095663687.png", record_pos=(0.302, 0.601), resolution=(1080, 1920)), vector=[-0.0244, -0.2088])
    poco("com.qraved.app:id/btSignUp").click()
    sleep(7)
    print (exists(MainMenu)== False)

#def SignUpUsingGoogle():
    clear_app("com.qraved.app")
    start_app("com.qraved.app")
    sleep(10)
    poco("com.qraved.app:id/tvLoginCreateAccount").click()
    touch(GoogleButton)
    touch(Template(r"tpl1543233257945.png", record_pos=(-0.101, 0.043), resolution=(1080, 1920)))
    sleep(7)
    if exists(PreferenceNext):
        touch(PreferenceNext)
        sleep(5)
        touch(PreferenceFinish)
        sleep(15)
    print (exists(MainMenu)== False)
    
def LoginUsingFacebook():
    clear_app("com.qraved.app")
    start_app("com.qraved.app")
    sleep(7)
    poco('com.qraved.app:id/ctvFacebook', text='Continue with Facebook').click()
    poco('login_form').wait_for_appearance(10)
    poco("m_login_email").click()
    text('arsentiga@gmail.com')
    poco("m_login_password").click()
    text('November7')
    poco("u_0_4").click()
    poco("u_0_3").wait_for_appearance(10)
    poco("u_0_3").click()
    sleep(5)
    poco("u_0_3").wait_for_disappearance(10)
    if (poco("com.qraved.app:id/ivTimeline").exists()== False):
        snapshot(msg="Login using Facebook unsuccessful!")
    elif (poco("com.qraved.app:id/ivTimeline").exists()== True):
        snapshot(msg="Successfully Login using Facebook")

def LoginUsingGoogle():
    clear_app("com.qraved.app")
    start_app("com.qraved.app")
    poco('com.qraved.app:id/tvLogin',text= 'Log In').wait_for_appearance()
    poco('com.qraved.app:id/tvLogin',text= 'Log In').click()
    poco('android.widget.TextView', text= 'GOOGLE').click()
    poco('com.google.android.gms:id/account_name').wait_for_appearance()
    poco('com.google.android.gms:id/account_name', text='arsentiga@gmail.com').click()
    poco("com.qraved.app:id/rvLoved").wait_for_appearance(10)
    poco('com.qraved.app:id/ctvDoNext', text='Next').click()
    poco('com.qraved.app:id/ctvDoNext', text='Finish').click()
    Perm_Loc = poco("com.android.packageinstaller:id/permission_message")
    if (Perm_Loc.exists()== True):
        poco("com.android.packageinstaller:id/permission_allow_button").click()
    elif (Perm_Loc.exists()== False):
        sleep(7)
    poco("com.qraved.app:id/ivTimeline").wait_for_appearance(10)
    if (poco("com.qraved.app:id/ivTimeline").exists()== False):
        snapshot(msg="Login using GOOGLE unsuccessful!")
    elif (poco("com.qraved.app:id/ivTimeline").exists()== True):
        snapshot(msg="Successfully Login using GOOGLE")    
    
def LoginUsingEmailExist():
    clear_app("com.qraved.app")
    start_app("com.qraved.app")
    poco('com.qraved.app:id/tvLogin',text= 'Log In').wait_for_appearance()
    poco('com.qraved.app:id/tvLogin',text= 'Log In').click()
    poco('android.widget.TextView', text= 'EMAIL').click()   
    poco('com.qraved.app:id/etEmail', text= 'Email address').click()
    text("Rosabella.sarudin@qraved.com")
    poco("com.qraved.app:id/etPassword").click()
    text("qraved1234")
    poco("com.qraved.app:id/bLogin").click()
    poco("com.qraved.app:id/rvLoved").wait_for_appearance(10)
    poco('com.qraved.app:id/ctvDoNext', text='Next').click()
    poco('com.qraved.app:id/ctvDoNext', text='Finish').click()
    Perm_Loc = poco("com.android.packageinstaller:id/permission_message")
    if (Perm_Loc.exists()== True):
        poco("com.android.packageinstaller:id/permission_allow_button").click()
    elif (Perm_Loc.exists()== False):
        sleep(7)
    poco("com.qraved.app:id/ivTimeline").wait_for_appearance(10)
    if (poco("com.qraved.app:id/ivTimeline").exists()== False):
        snapshot(msg="Login using EMAIL unsuccessful!")
    elif (poco("com.qraved.app:id/ivTimeline").exists()== True):
        snapshot(msg="Successfully Login using EMAIL")

def LoginUsingEmailNonExist():
    clear_app("com.qraved.app")
    start_app("com.qraved.app")
    poco('com.qraved.app:id/tvLogin',text= 'Log In').wait_for_appearance()
    poco('com.qraved.app:id/tvLogin',text= 'Log In').click()
    poco('android.widget.TextView', text= 'EMAIL').click()
    poco('com.qraved.app:id/etEmail', text= 'Email address').click()
    text("Lalalayeyeye@qraved.com")
    poco("com.qraved.app:id/etPassword").click()
    text("qraved1234")
    poco("com.qraved.app:id/bLogin").click()
    poco('android:id/message').wait_for_appearance(10)
    if (poco('android:id/message', text = 'This email address is not registered. Please create an account first.').exists()== True):
        snapshot(msg='Alert Message Appear!!! Unregistered email login attempt is PASSED')
    elif (poco('android:id/message', text = 'This email address is not registered. Please create an account first.').exists()== False):
        snapshot(msg='Alert Message NOT Appear!!! Unregistered email login attempt is FAILED')
        
def LoginUsingNumberSuccess():
    clear_app("com.qraved.app")
    start_app("com.qraved.app")
    poco('com.qraved.app:id/tvLogin',text= 'Log In').wait_for_appearance()
    poco('com.qraved.app:id/tvLogin',text= 'Log In').click()
    poco('android.widget.TextView', text= 'PHONE NUMBER').click()
    poco("com.qraved.app:id/etPhoneNumberLogin", text= 'Phone Number').click()
    text("08159720265")
    poco("com.qraved.app:id/etPassword").click()
    text("qraved1234")
    poco("com.qraved.app:id/bLogin").click()
    poco("com.qraved.app:id/rvLoved").wait_for_appearance(10)
    poco('com.qraved.app:id/ctvDoNext', text='Next').click()
    poco('com.qraved.app:id/ctvDoNext', text='Finish').click()
    Perm_Loc = poco("com.android.packageinstaller:id/permission_message")
    if (Perm_Loc.exists()== True):
        poco("com.android.packageinstaller:id/permission_allow_button").click()
    elif (Perm_Loc.exists()== False):
        sleep(7)
    poco("com.qraved.app:id/ivTimeline").wait_for_appearance(10)
    if (poco("com.qraved.app:id/ivTimeline").exists()== False):
        snapshot(msg="Login using PHONE NUMBER unsuccessful!")
    elif (poco("com.qraved.app:id/ivTimeline").exists()== True):
        snapshot(msg="Successfully Login using PHONE NUMBER")
    
def LoginUsingNumberFailed():
    clear_app("com.qraved.app")
    start_app("com.qraved.app")
    poco('com.qraved.app:id/tvLogin',text= 'Log In').wait_for_appearance()
    poco('com.qraved.app:id/tvLogin',text= 'Log In').click()
    poco('android.widget.TextView', text= 'PHONE NUMBER').click()
    poco("com.qraved.app:id/etPhoneNumberLogin", text= 'Phone Number').click()
    text("0000000001")
    poco("com.qraved.app:id/etPassword").click()
    text("qraved1234")
    poco("com.qraved.app:id/bLogin").click()
    poco('android:id/message').wait_for_appearance(10)
    if (poco('android:id/message', text = 'This phone number is not registered. Please create an account first.').exists()== True):
        snapshot(msg='Alert Message Appear!!! Unregistered email login attempt is PASSED')
    elif (poco('android:id/message', text = 'This phone number is not registered. Please create an account first.').exists()== False):
        snapshot(msg='Alert Message NOT Appear!!! Unregistered email login attempt is FAILED')
    
def LoginUsingWrongPassword():
    clear_app("com.qraved.app")
    start_app("com.qraved.app")
    poco('com.qraved.app:id/tvLogin',text= 'Log In').wait_for_appearance(10)
    poco('com.qraved.app:id/tvLogin',text= 'Log In').click()
    poco('android.widget.TextView', text= 'PHONE NUMBER').click()
    poco("com.qraved.app:id/etPhoneNumberLogin", text= 'Phone Number').click()
    text("0000000000")
    poco("com.qraved.app:id/etPassword").click()
    text("qraved1234")
    poco("com.qraved.app:id/bLogin").click()
    poco('android:id/message').wait_for_appearance(10)
    if (poco('android:id/message', text = 'The password you entered is incorrect. Please try again.').exists()== True):
        snapshot(msg='Wrong Password Message Appeared!!!, PASSED')
    elif (poco('android:id/message', text = 'The password you entered is incorrect. Please try again.').exists()== False):
        snapshot(msg='Wrong Password Message Not Appeared!!!, FAILED')
    clear_app("com.qraved.app")
    start_app("com.qraved.app")
    poco('com.qraved.app:id/tvLogin',text= 'Log In').wait_for_appearance()
    poco('com.qraved.app:id/tvLogin',text= 'Log In').click()
    poco('android.widget.TextView', text= 'EMAIL').click()   
    poco('com.qraved.app:id/etEmail', text= 'Email address').click()
    text("Rosabella.sarudin@qraved.com")
    poco("com.qraved.app:id/etPassword").click()
    text("lalalayeyeye")
    poco("com.qraved.app:id/bLogin").click()
    if (poco('android:id/message', text = 'The password you entered is incorrect. Please try again.').exists()== True):
        snapshot(msg='Wrong Password Message Appeared!!!, PASSED')
    elif (poco('android:id/message', text = 'The password you entered is incorrect. Please try again.').exists()== False):
        snapshot(msg='Wrong Password Message Not Appeared!!!, FAILED')

def OnBoardingCarousel():
    clear_app("com.qraved.app")
    start_app("com.qraved.app")
    wait (CarouselPicA)
    if (exists(CarouselPicA)): print('Pass')
    sleep(3)
    wait (CarouselPicB)
    if (exists(CarouselPicB)): print('Pass')
    sleep(3)
    wait (CarouselPicC)
    if (exists(CarouselPicC)): print('Pass')
    sleep(3)
    wait (CarouselPicD)
    if (exists(CarouselPicD)): print('Pass')
    sleep(4)
    wait (CarouselPicE)
    if (exists(CarouselPicE)): print('Pass')
    sleep(3)
    
#Automation ended

ImageSourcePhone()
#LoginUsingFacebook()
#LoginUsingGoogle()
#LoginUsingEmailExist()
#LoginUsingEmailNonExist()
#LoginUsingNumberSuccess()
#LoginUsingNumberFailed()
#LoginUsingWrongPassword()
#OnBoardingCarousel()