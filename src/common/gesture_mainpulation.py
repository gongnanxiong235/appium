# coding:utf-8
__author__ = 'Helen'
'''
description:手势操作
'''
class gesture_mainpulation:
    def swipe_left(self,driver):
        '''左滑'''
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        driver.swipe(x*3/4,y/4,x/4,y/4)

    def swipe_right(self,driver):
        '''右滑'''
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        driver.swipe(x/4,y/4,x*3/4,y/4)

    def swipe_down(self,driver):
        '''下滑'''
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        driver.swipe(x/2,y*3/4,x/2,y/4)

    def swipe_up(self,driver):
        '''上滑'''
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        driver.swipe(x/2,y/4,x/2,y*3/4)