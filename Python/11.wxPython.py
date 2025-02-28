import wx

# #创建应用程序对象
# app = wx.App()

# #创建窗口对象
# frm=wx.Frame(None,title="Hello World",size=(400,300),pos=(100,100))
# #显示窗口
# frm.Show()

# #进入主事件循环
# app.MainLoop()


#自定义应用程序类
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None,title="Hello MyApp",size=(400,300),pos=(100,100))

#创建应用程序对象
myapp = wx.App()
#创建窗口对象
frm=MyFrame()
#显示窗口
frm.Show()

#进入主事件循环
myapp.MainLoop()