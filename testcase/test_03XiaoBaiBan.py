# coding: utf-8
import unittest
import uiautomator2 as u2
import time
import uiautomator2.ext.htmlreport as htmlreport
import logging


class TestXiaobaiban(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.u = u2.connect_usb()
        cls.u.healthcheck()  # 解锁屏幕并启动uiautomator服务
        #hrp = htmlreport.HTMLReport(cls.u, 'report')
        #hrp.patch_click()
        cls.u.make_toast("测试开始")
        # cls.u.disable_popups(True)  # 允许自动处理弹出框

    @classmethod
    def tearDownClass(cls):
        cls.u.make_toast("测试结束", 3)
        cls.u.app_stop_all()
        cls.u.service(
            "uiautomator").stop()  # 停止uiautomator守护程序，允许其他测试框架如 appium 运行

    def setUp(self):
        self.d = self.u.session("com.esenyun.workline")  # restart app
        time.sleep(5)  # 等待首页广告结束

    def tearDown(self):
        pass

    def test01InterXiaoBaiBan(self):   #查看小白板数据
        time.sleep(3)
        self.d(text=u"我的小白板").click()
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/iv_content_action_2").click()  # 点击排序按钮
        time.sleep(1)
        self.d.press('back')
        time.sleep(3)
        self.d(text=u"我的小白板").click()
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/iv_content_action_1").click()
        time.sleep(2)
        self.d.press("back")
        time.sleep(1)
        self.d(text=u"我的小白板").click()
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/title_iv_right02").click()  # 点击选项按钮
        time.sleep(2)
        self.d.press("back")
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/title_iv_right").click()  # 点击查看数据按钮
        time.sleep(4)
        self.d.click(0.322, 0.14)  # 我发布的
        time.sleep(1)
        self.d.click(0.513, 0.145)  # 我参与的
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/iv_title_left").click()  # 点击返回按钮
        time.sleep(1)

    def test02Draft(self):
        self.d(text=u"我的小白板").click()
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/title_iv_right02").click()  # 点击选项按钮
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/rb_conclusion_draft").click()
        time.sleep(1)
        self.assertTrue(self.d(resourceId="com.esenyun.workline:id/rb_conclusion_draft").exists, "未进入结论草稿")




if __name__ == '__main__':
        unittest.main()
