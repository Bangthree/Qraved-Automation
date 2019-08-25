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
    global Search
    global BackArrow
    global Updates
    global FollowButton
    global UnfollowButton
    global SeeMore
    global FBContinue
    MainMenu = Template(r"tpl1542188226027.png", record_pos=(0.009, 0.145), resolution=(1080, 1920))
    QOA = Template(r"tpl1542182470439.png", record_pos=(0.399, 0.044), resolution=(1080, 1920))
    Search = Template(r"tpl1542182752229.png", record_pos=(0.429, -0.752), resolution=(1080, 1920))
    BackArrow = Template(r"tpl1542182532301.png", record_pos=(-0.423, -0.75), resolution=(1080, 1920))
    Updates = Template(r"tpl1542190351046.png", record_pos=(0.189, 0.822), resolution=(1080, 1920))
    FollowButton = Template(r"tpl1542189057493.png", record_pos=(-0.351, 0.368), resolution=(1080, 1920))
    UnfollowButton = Template(r"tpl1542254402053.png", record_pos=(-0.003, 0.606), resolution=(1080, 1920))
    SeeMore = Template(r"tpl1542969373372.png", record_pos=(-0.006, 0.77), resolution=(1080, 1920))
    FBContinue = Template(r"tpl1543220745484.png", record_pos=(-0.074, 0.296), resolution=(1440, 2560))

def LoginUser(): #Using Google
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
    sleep(3)

def PermissionHandling():
    Perm_Loc = poco("com.android.packageinstaller:id/permission_message")
    if (Perm_Loc.exists()== True):
        poco("com.android.packageinstaller:id/permission_allow_button").click()
    elif (Perm_Loc.exists()== False):
        sleep(7)
    
def OpenQOAListPage(): #Updated
    poco(text="Official Accounts").click()
    poco("com.qraved.app:id/tvQOACardBannerTitle").wait_for_appearance()
    #checking
    if (poco('com.qraved.app:id/tvQOAListTitle', text='Nge-Hits').exists()== False):
        snapshot(msg="QOA List not appeared.")
    if (poco('com.qraved.app:id/ivBack').exists()== False):
        snapshot(msg="Missing Back Button on QOA List Page.")
    if (poco('com.qraved.app:id/ivSearch').exists()== False):
        snapshot(msg='Missing Search Button on QOA List Page.')
    if (poco('com.qraved.app:id/tvTitle', text='Official Accounts').exists()== False):
        snapshot(msg='Missing Title of the QOA List Page.')
    if (poco('android.widget.TextView', text= 'Following').exists()== False):
        snapshot(msg='Missing Following Tab from QOA List Page.')
    while (poco('android.widget.TextView', text= 'See All').exists()== False):
        swipe ((displaysize[0]*0.55,displaysize[1]*0.9) , (displaysize[0]*0.55,displaysize[1]*0.01))
    if (poco('android.widget.TextView', text= 'See All').exists()== False):
        snapshot(msg='Missing See All Button on QOA List')
    swipe ((displaysize[0]*0.55,displaysize[1]*0.15) , (displaysize[0]*0.55,displaysize[1]*0.9))
    if (poco('android.widget.TextView', text='See More').exists()== False):
        snapshot(msg='Missing See More Button on QOA List Page')

def FollowQOA():
    #FromHomepage
    while (poco("com.qraved.app:id/ivTimeline").exists()== False):
        keyevent("back")
        sleep(1)
    while (poco("android:id/content").child("android.view.ViewGroup").offspring("com.qraved.app:id/swipeRefreshLayout").offspring("com.qraved.app:id/rvHomeRevamp").offspring("com.qraved.app:id/recyHomeMall").offspring("com.qraved.app:id/tvHomeMallFollow").exists()== False):
        swipe ((displaysize[0]*0.55,displaysize[1]*0.9) , (displaysize[0]*0.55,displaysize[1]*0.01))
    poco("android:id/content").child("android.view.ViewGroup").offspring("com.qraved.app:id/swipeRefreshLayout").offspring("com.qraved.app:id/rvHomeRevamp").offspring("com.qraved.app:id/recyHomeMall").offspring("com.qraved.app:id/tvHomeMallFollow").click()
    if (poco('com.qraved.app:id/tvHomeMallFollow', text= "Following").exists()== False):
        snapshot(msg="QOA from Homepage is unfollowable")
    elif (poco('com.qraved.app:id/tvHomeMallFollow', text= "Following").exists()== True):
        sleep(1)
    #FromQOAListPage
    while (poco('com.qraved.app:id/tvQuickName', text ='Official Accounts').exists()== False):
        swipe ((displaysize[0]*0.55,displaysize[1]*0.15) , (displaysize[0]*0.55,displaysize[1]*0.9))
    poco('com.qraved.app:id/tvQuickName', text ='Official Accounts').click()
    if (poco('com.qraved.app:id/tvQOAFollowState', text= 'Follow').exists()== True):
        poco('com.qraved.app:id/tvQOAFollowState', text= 'Follow').click
    if (poco('com.qraved.app:id/tvQOAFollowState', text= 'Follow').exists()== False):
        poco('com.qraved.app:id/tvQOAFollowState', text= 'Followed').click
    elif (poco('com.qraved.app:id/tvQOAFollowState', text= 'Followed').exists()== True):
        poco('com.qraved.app:id/tvQOAFollowState', text= 'Followed').click
    sleep(1)
    
    sleep(3)
    exists(Template(r"tpl1542189095003.png", record_pos=(-0.257, 0.284), resolution=(1080, 1920)))
    stop_app("com.qraved.app")
    start_app("com.qraved.app")
    sleep(10)
    if exists(Template(r"tpl1544596010637.png", record_pos=(-0.002, 0.024), resolution=(1440, 2560))):
        poco("android:id/button2").click()
    print (exists(MainMenu)== False)
    touch(QOA)
    sleep(2)
    exists(Template(r"tpl1542189095003.png", record_pos=(-0.257, 0.284), resolution=(1080, 1920)))
    keyevent("BACK")
    sleep(2)
    poco("com.qraved.app:id/ivTimeline").exists()
    sleep(2)
    (exists(Template(r"tpl1542192167245.png", record_pos=(-0.245, -0.489), resolution=(1080, 1920)))== False)
    keyevent("back")
    sleep(5)
    poco("com.qraved.app:id/ivSearchNavigate").click()
    sleep(2)
    poco("com.qraved.app:id/etSearch").click()
    text("grand indonesia")
    sleep(5)
    touch(Template(r"tpl1542192167245.png", record_pos=(-0.245, -0.489), resolution=(1080, 1920)))
    sleep(5)
    (exists(Template(r"tpl1542192203568.png", record_pos=(0.01, 0.245), resolution=(1080, 1920)))== False)
    if exists(Template(r"tpl1544597611789.png", record_pos=(0.096, 0.391), resolution=(1440, 2560))):
        poco("com.qraved.app:id/tvFollow").click()
    sleep(2)
    (exists(Template(r"tpl1542192271540.png", record_pos=(0.384, 0.307), resolution=(1080, 1920)))== False)
    sleep(2)
    keyevent("back")
    sleep(2)
    keyevent("back")
    sleep(2)
    poco("com.qraved.app:id/ivTimeline").click()
    (exists(Template(r"tpl1542192425892.png", record_pos=(-0.069, -0.579), resolution=(1080, 1920)))== False)

def UnfollowQOA():
    while exists(MainMenu)== False:
        keyevent("back")
    sleep(2)
    swipe(Template(r"tpl1542189947567.png", record_pos=(-0.24, 0.466), resolution=(1080, 1920)), vector=[-0.1544, -0.3494])
    (exists(Template(r"tpl1542611930332.png", record_pos=(0.001, 0.198), resolution=(1080, 1920)))== False)
    touch(Template(r"tpl1542190022558.png", record_pos=(-0.002, 0.075), resolution=(1080, 1920)))
    (exists(Template(r"tpl1542254075673.png", record_pos=(0.0, 0.433), resolution=(1080, 1920)))== False)
    swipe(Template(r"tpl1542190227223.png", record_pos=(-0.24, -0.354), resolution=(1080, 1920)), vector=[-0.1262, 0.524])
    sleep(2)
    touch(QOA)
    sleep(2)
    (exists(Template(r"tpl1542254327337.png", record_pos=(-0.24, 0.019), resolution=(1080, 1920)))== False)
    (touch(Template(r"tpl1542254349602.png", record_pos=(-0.326, 0.37), resolution=(1080, 1920))))
    sleep(3)
    (exists(UnfollowButton)== False)
    touch(UnfollowButton)
    (exists(Template(r"tpl1542335111098.png", record_pos=(-0.241, 0.11), resolution=(1080, 1920)))== False)
    sleep(3)
    stop_app("com.qraved.app")
    start_app("com.qraved.app")
    sleep(10)
    print (exists(MainMenu)== False)
    touch(QOA)
    sleep(2)
    (exists(Template(r"tpl1542189095003.png", record_pos=(-0.257, 0.284), resolution=(1080, 1920)))== False)
    keyevent("BACK")
    sleep(2)
    touch(Updates)
    sleep(2)
    (exists(Template(r"tpl1542192425892.png", record_pos=(-0.069, -0.579), resolution=(1080, 1920)))== False)
    keyevent("back")
    sleep(5)
    touch(Template(r"tpl1542337249924.png", record_pos=(0.429, -0.763), resolution=(1080, 1920)))
    sleep(2)
    touch(Template(r"tpl1542191915469.png", record_pos=(-0.106, -0.742), resolution=(1080, 1920)))
    text("Grand Indonesia")
    sleep(5)
    touch(Template(r"tpl1542192167245.png", record_pos=(-0.245, -0.489), resolution=(1080, 1920)))
    sleep(5)
    if exists(Template(r"tpl1542335279116.png", record_pos=(0.097, 0.363), resolution=(1080, 1920)))== True:
        (touch(Template(r"tpl1542335316700.png", record_pos=(0.386, 0.364), resolution=(1080, 1920))))
    sleep(2)
    (exists(Template(r"tpl1542335339502.png", record_pos=(0.094, 0.362), resolution=(1080, 1920)))== False)
    sleep(5)
    keyevent("back")
    sleep(5)
    keyevent("back")
    sleep(5)
    touch(Updates)
    (exists(Template(r"tpl1542192425892.png", record_pos=(-0.069, -0.579), resolution=(1080, 1920)))== False)

def OpenFollowingTab():
    while exists(MainMenu)== False:
        keyevent("back")
    sleep(2)
    touch(QOA)
    sleep(2)
    touch(Template(r"tpl1542608027486.png", record_pos=(-0.2, -0.606), resolution=(1080, 1920)))
    (exists(Template(r"tpl1542596099594.png", record_pos=(0.006, 0.018), resolution=(1080, 1920)))== False)
    keyevent("back")

def ClickQOATabsorting(): #Updated
    while (poco('com.qraved.app:id/ivTimeline').exists()== False):
        keyevent("back")
        sleep(1)
    poco(text="Official Accounts").click()
    while (poco('com.qraved.app:id/tvQOACardBannerTitle',text='Malls').exists()== False):
        swipe ((displaysize[0]*0.9,displaysize[1]*0.55) , (displaysize[0]*0.01,displaysize[1]*0.55))
    poco("com.qraved.app:id/tvQOAListSortBy").click()
    poco("com.qraved.app:id/tvSortSecond").click()
    sleep(5)
    poco("com.qraved.app:id/tvQOAListSortBy").click()
    poco("com.qraved.app:id/tvSortThird").click()
    sleep(5)
    poco("com.qraved.app:id/tvQOAListSortBy").click()
    poco("com.qraved.app:id/tvSortFour").click()
    sleep(5)
    poco("com.qraved.app:id/tvQOAListSortBy").click()
    poco("com.qraved.app:id/tvSortFive").click()
    while (poco('com.qraved.app:id/tvQOACardBannerTitle',text='Communities').exists()== False):
        swipe ((displaysize[0]*0.01,displaysize[1]*0.55) , (displaysize[0]*0.9,displaysize[1]*0.55))
    poco("com.qraved.app:id/tvQOAListSortBy").click()
    poco("com.qraved.app:id/tvSortThird").click()
    sleep(5)
    poco("com.qraved.app:id/tvQOAListSortBy").click()
    poco("com.qraved.app:id/tvSortFour").click()
    sleep(5)
    poco("com.qraved.app:id/tvQOAListSortBy").click()
    poco("com.qraved.app:id/tvSortFive").click() #Updated
    
def ClickshareCTAonQOADetailPage(): #Updated
    while (poco('com.qraved.app:id/ivTimeline').exists()== False):
        keyevent("back")
        sleep(1)
    swipe ((displaysize[0]*0.55,displaysize[1]*0.9) , (displaysize[0]*0.55,displaysize[1]*0.01))
    poco(text="Plaza Indonesia").click()
    poco("com.qraved.app:id/ivShare").click() 

def slidethecarouselbanner():
    while (poco('com.qraved.app:id/ivTimeline').exists()== False):
        keyevent("back")
        sleep(1)
    if exists(Template(r"tpl1543216456592.png", record_pos=(-0.003, -0.251), resolution=(1440, 2560)))== False:
        swipe ((displaysize[0]*0.55,displaysize[1]*0.22),(displaysize[0]*0.55,displaysize[1]*0.5))
    if exists(Template(r"tpl1543217261496.png", record_pos=(0.005, -0.252), resolution=(1440, 2560)))== False:
        swipe (vector=[-0.5775, 0.0229])
    if exists(Template(r"tpl1543217234341.png", record_pos=(0.01, -0.251), resolution=(1440, 2560)))== False:
        swipe (vector=[-0.5775, 0.0229])
    if exists(Template(r"tpl1543217282622.png", record_pos=(0.009, -0.252), resolution=(1440, 2560)))== False:
        swipe (vector=[-0.5775, 0.0229])
    if exists(Template(r"tpl1543217301652.png", record_pos=(0.009, -0.252), resolution=(1440, 2560)))== False:
        swipe (vector=[-0.5775, 0.0229])

def clickUpdatesbutton():
    while exists(MainMenu)== False:
        keyevent("back")
    sleep(2)
    touch(QOA)
    swipe(Template(r"tpl1542599819372.png", record_pos=(0.269, -0.611), resolution=(1080, 1920)), vector=[-0.5166, -0.0026])
    sleep(2)
    touch(Template(r"tpl1542599833407.png", record_pos=(0.193, -0.609), resolution=(1080, 1920)))
    sleep(2)
    touch(Template(r"tpl1542947613702.png", record_pos=(-0.374, 0.599), resolution=(1080, 1920)))
    sleep(5)
    if exists(Template(r"tpl1542963653199.png", record_pos=(0.017, 0.368), resolution=(1080, 1920)))== False:
        touch(Template(r"tpl1542963678597.png", record_pos=(0.096, 0.368), resolution=(1080, 1920)))
    sleep(2)
    touch(Template(r"tpl1542963653199.png", record_pos=(0.017, 0.368), resolution=(1080, 1920)))
    while exists(MainMenu)== False:
        keyevent("back")
    sleep(2)
    swipe(Template(r"tpl1542189947567.png", record_pos=(-0.24, 0.466), resolution=(1080, 1920)), vector=[-0.1544, -0.3494])
    touch(Template(r"tpl1542947613702.png", record_pos=(-0.374, 0.599), resolution=(1080, 1920)))
    sleep(5)
    if exists(Template(r"tpl1542963653199.png", record_pos=(0.017, 0.368), resolution=(1080, 1920)))== False:
        touch(Template(r"tpl1542963678597.png", record_pos=(0.096, 0.368), resolution=(1080, 1920)))
    sleep(2)
    touch(Template(r"tpl1542963653199.png", record_pos=(0.017, 0.368), resolution=(1080, 1920)))

def SeesectionTablist():
    while (poco('com.qraved.app:id/ivTimeline').exists()== False):
        keyevent("back")
        sleep(1)
    sleep(2)
    poco(text="Official Accounts").click()
    if (poco('com.qraved.app:id/tvQOACardBannerTitle', text='Communities').exists()== False):
        snapshot(msg='Missing Communities section on QOA List Page')
    elif (poco('com.qraved.app:id/tvQOACardBannerTitle', text='Communities').exists()== True):
        sleep(2)
    poco('android.widget.TextView', text= 'See More').click()
    sleep(2)
    if (poco('com.qraved.app:id/tvQOACardBannerTitle', text='Promos').exists()== False):
        snapshot(msg='Missing Promos section on QOA List Page')
    elif (poco('com.qraved.app:id/tvQOACardBannerTitle', text='Promos').exists()== True):
        sleep(2)
    swipe(vector=[0.012, 0.2888])
    sleep(2)
    touch(SeeMore)
    if (poco('com.qraved.app:id/tvQOACardBannerTitle', text='Malls').exists()== False):
        snapshot(msg='Missing Malls section on QOA List Page')
    elif (poco('com.qraved.app:id/tvQOACardBannerTitle', text='Malls').exists()== True):
        sleep(2)
    sleep(2)
    swipe(FollowButton, vector=[0.012, 0.2888])
    sleep(2)
    touch(SeeMore)
    if (poco('com.qraved.app:id/tvQOACardBannerTitle', text='Promos').exists()== False):
        snapshot(msg='Missing Promos section on QOA List Page')
    elif (poco('com.qraved.app:id/tvQOACardBannerTitle', text='Promos').exists()== True):
        sleep(2)
    sleep(2)
    swipe(FollowButton, vector=[0.012, 0.2888])
    sleep(2)
    touch(SeeMore)
    (exists(Template(r"tpl1542969856935.png", record_pos=(0.01, -0.409), resolution=(1080, 1920)))== False)
    sleep(2)
    swipe(FollowButton, vector=[0.012, 0.2888])
    sleep(2)
    touch(SeeMore)
    (exists(Template(r"tpl1542969913758.png", record_pos=(-0.004, -0.418), resolution=(1080, 1920)))== False)
    sleep(2)
    swipe(FollowButton, vector=[0.012, 0.2888])
    sleep(2)
    touch(SeeMore)
    (exists(Template(r"tpl1542969965589.png", record_pos=(-0.002, -0.571), resolution=(1080, 1920)))== False)
    sleep(2)
    swipe(FollowButton, vector=[0.012, 0.2888])
    sleep(2)
    touch(SeeMore)
    (exists(Template(r"tpl1542970022375.png", record_pos=(0.006, 0.028), resolution=(1080, 1920)))== False)
    sleep(2)

def ClickspecificsectionTab():
    while exists(MainMenu)== False:
        keyevent("back")
    sleep(2)
    touch(QOA)
    (exists(Template(r"tpl1542968574967.png", record_pos=(0.0, -0.357), resolution=(1080, 1920)))== False)
    sleep(2)
    touch(SeeMore)
    sleep(2)
    (exists(Template(r"tpl1542968628800.png", record_pos=(0.002, -0.419), resolution=(1080, 1920)))== False)
    sleep(2)
    swipe(FollowButton, vector=[0.012, 0.2888])
    sleep(2)
    touch(SeeMore)
    (exists(Template(r"tpl1542969729339.png", record_pos=(0.0, -0.419), resolution=(1080, 1920)))== False)
    sleep(2)
    touch(Template(r"tpl1543206495625.png", record_pos=(-0.239, 0.415), resolution=(1080, 1920)))
    sleep(3)
    touch(Template(r"tpl1543206578844.png", record_pos=(-0.152, 0.517), resolution=(1080, 1920)))
    sleep(1)
    (exists(Template(r"tpl1543207885794.png", record_pos=(0.002, -0.254), resolution=(1080, 1920)))== False)
    touch(Template(r"tpl1543206629823.png", record_pos=(0.066, -0.608), resolution=(1080, 1920)))
    (exists(Template(r"tpl1543206644534.png", record_pos=(0.004, 0.166), resolution=(1080, 1920)))== False)
    touch(Template(r"tpl1543206665917.png", record_pos=(0.22, -0.606), resolution=(1080, 1920)))
    (exists(Template(r"tpl1543206710908.png", record_pos=(0.01, -0.256), resolution=(1080, 1920)))== False)
    touch(Template(r"tpl1543206741925.png", record_pos=(0.195, -0.606), resolution=(1080, 1920)))
    (exists(Template(r"tpl1543206766472.png", record_pos=(0.008, -0.03), resolution=(1080, 1920)))== False)
    touch(Template(r"tpl1543206789426.png", record_pos=(0.249, -0.605), resolution=(1080, 1920)))
    if exists(Template(r"tpl1543206803270.png", record_pos=(0.008, -0.072), resolution=(1080, 1920)))== True:
        touch(Template(r"tpl1543206834915.png", record_pos=(0.368, -0.46), resolution=(1080, 1920)))
        sleep(2)
        (exists(Template(r"tpl1543206870316.png", record_pos=(0.008, 0.018), resolution=(1080, 1920)))== False)
        keyevent("back")
    touch(Template(r"tpl1543207000846.png", record_pos=(0.393, -0.603), resolution=(1080, 1920)))
    (exists(Template(r"tpl1543207027675.png", record_pos=(0.01, -0.008), resolution=(1080, 1920)))== False)
    
ImageSourcePhone()
#LoginUser()
#PermissionHandling()
#OpenQOAListPage()
FollowQOA()