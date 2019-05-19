def before_test_check(base_drive, by):
    bg=base_drive.find_element ( *(by.ID, 'com.huanshou.taojj:id/iv_bg') )
    if (bg is not None):
        # 选择存入账户
        other_account=(by.ID, "com.huanshou.taojj:id/delay_withdraw_deposit_tv")
        withdraw=base_drive.find_element ( *other_account )
        withdraw.click ()
        # 选择其他方式登录
        other_login_text=base_drive.find_element ( *(by.ID, "com.huanshou.taojj:id/pick_other_login_way_tv") )
        other_login_text.click ()
        # 选择以qq的方式登录
        qq_login_text=base_drive.find_element ( *(by.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.TextView") )
        qq_login_text.click ()
        # 调起qq点击登录button
        qq_login_button=base_drive.find_element ( *(by.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.Button") )
        qq_login_button.click ()