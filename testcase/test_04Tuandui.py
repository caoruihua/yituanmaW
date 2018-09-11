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




    def test01TuanduiKanban(self):
        self.d(text=u"团队").click()
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/title_img_right").click() #进入团队数据看板
        time.sleep(3)
        self.d.press("back")

    def test02InterMessage(self):
        self.d(text=u"团队").click()
        time.sleep(1)
        self.d(text=u"消息").click()  # 进入消息
        time.sleep(2)
        self.assertTrue(self.d(resourceId="com.esenyun.workline:id/buttonAudioMessage").exists,"未进入消息")
        time.sleep(2)




if __name__ == '__main__':
        unittest.main()
