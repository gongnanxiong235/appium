class Before_Case:
    def __init__(self, base_drive, by):
        self.base_drive = base_drive
        self.by = by

    def before_test_check(self):
        bg = self.base_drive.find_element(*(self.by.ID, 'com.huanshou.taojj:id/iv_bg'))
        print("bg:", bg)
        if (bg is not None):
            ''' 选择存入账户 '''
            other_account = (self.by.ID, "com.huanshou.taojj:id/delay_withdraw_deposit_tv")
            withdraw = self.base_drive.find_element(*other_account)
            withdraw.click()
            ''' 选择其他方式登录 '''
            other_login_text = self.base_drive.find_element(
                *(self.by.ID, "com.huanshou.taojj:id/pick_other_login_way_tv"))
            other_login_text.click()
            '''选择以qq的方式登录 '''
            qq_login_text = self.base_drive.find_element(*(self.by.XPATH,
                                                           "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.TextView"))
            qq_login_text.click()
            ''' 调起qq点击登录button'''
            qq_login_button = self.base_drive.find_element(*(self.by.XPATH,
                                                             "/hierarchy/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.Button"))
            qq_login_button.click()

            '''如果是新客，领取任务'''
            self.new_user_pop()

        else:
            print("无抽奖弹框")
            self.new_user_pop()
        print("测试前校验已经完成")

    def new_user_pop(self):
        new_user_window = self.base_drive.find_element(*(self.by.XPATH,
                                                         "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup"))
        if (new_user_window is not None):
            el1 = self.base_drive.find_element(self.by.ID, "com.huanshou.taojj:id/bottom_bt").click()
        else:
            print("没有任务弹框")
