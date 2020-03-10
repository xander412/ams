from tkinter import *
from threading import *
import os
from tkinter import ttk
from tkinter import scrolledtext as srctext
from tkinter import PhotoImage
import subprocess
class Installer:
    def __init__(self):
        self.host = ''
        self.port = ''
        self.user = ''
        self.pwd =  ''
        self.gui()
        self.root.mainloop()
    def gui(self):
        self.root = Tk()
        self.root.config(bg = 'white')
        self.root.title('Xattendance Installer')
        self.root.geometry('730x450')
        self.root.resizable(False, False)
        self.f1 = Frame(self.root,
                        bg = 'white')
        self.f1.pack(side = LEFT)
        self.img = PhotoImage(file = 'icon.png')
        self.imf = Label(self.f1,
                         image = self.img,
                         bg = 'white')
        self.imf.pack(side = LEFT)
        self.imf.image = self.img
        self.f2 = Frame(self.root,
                        bg = 'white')
        self.f2.pack(side = BOTTOM)
        self.back = Button(self.f2,
                           width = 15,
                           text = '<Back')
        self.back.pack(side = LEFT, fill = X)
        self.next = Button(self.f2,
                           width = 15,
                           text = 'Next>')
        self.next.pack(side = LEFT, fill = X)
        self.cancel = Button(self.f2,
                             width = 15,
                           text = 'Cancel')
        self.cancel.pack(side = RIGHT, fill = X)
        self.f3 = Frame(self.root,
                        bg = 'white')
        self.f3.pack()
        self.start_permit()
    def start_permit(self):
        self.f3.destroy()
        self.f3 = Frame(self.root,
                        bg = 'white')
        self.f3.pack()
        self.l1 = Label(self.f3,
                        text = 'Welcome to Installation Wizard of Xattendance',
                        font = ('TlwgTypist', 12, 'bold'),
                        bg = 'white')
        self.l1.pack(side = TOP, pady = 10)
        self.l2 = Message(self.f3,
                        text = 'This will install Offline Attendance Management System(Xattendance) on your PC.Click "Next" to continue....',
                        bg = 'white',
                        width = 515,
                        font = ('aakar', 12))
        self.l2.pack(pady = 120, padx = 10)
        self.l3 = Message(self.f3,
                        text = 'NOTE:This installation requires internet access unless you already installed the dependencies.',
                        bg = 'white',
                        width = 525,
                        font = ('aakar', 12))
        self.l3.pack()
        self.next['command'] = self.network_access
        self.back['command'] = None
    def network_access(self):
        self.f3.destroy()
        self.f3 = Frame(self.root,
                        bg = 'white')
        self.f3.pack()
        self.r1 = Label(self.f3,
                        text = 'Network Configuration:',
                        font = ('TlwgTypist', 12, 'bold'),
                        bg = 'white')
        self.r1.pack()
        self.f4 = Frame(self.f3,
                        bg = 'white')
        self.f4.pack(side = LEFT, anchor = NW, pady = 30, fill = X)
        self.flag = IntVar()
        self.r2 = Radiobutton(self.f4,
                        text = 'No Proxy',
                        bg = 'white',
                        font = ('URWGothic', 12),
                        activebackground = 'white',
                        highlightthickness = 0,
                        value = 0,
                        variable = self.flag)
        self.r2.pack(side = TOP, anchor = NW)
        self.r3 = Radiobutton(self.f4,
                        text = 'Manual Proxy',
                        bg = 'white',
                        activebackground = 'white',
                        highlightthickness = 0,
                        value = 1,
                        variable = self.flag,
                        font = ('URWGothic', 12))
        self.r3.pack(side = TOP, anchor = NW)
        self.flag.set(0)
        self.manual_proxy()
        self.r2.bind('<Button-1>', self.e_deactive)
        self.r3.bind('<Button-1>', self.e_active)
        self.next['command'] = self.details_prompt
        self.back['command'] = self.start_permit
    def manual_proxy(self):
        f4 = Frame(self.f4,
                   bg = 'white')
        f4.pack(fill = X)
        l1 = Label(f4,
                   text = 'Proxy Host:',
                   bg = 'white',
                   font = ('URWGothic', 12))
        l1.pack(side = TOP, anchor = NW)
        self.e1 = Entry(f4,
                   bg = 'white',
                   font = ('TlwgTypist', 12))
        self.e1.pack(side = TOP, anchor = NW)
        l2 = Label(f4,
                   text = 'Port:',
                   bg = 'white',
                   font = ('URWGothic', 12))
        l2.pack(side = TOP, anchor = NW)
        self.e2 = Entry(f4,
                   bg = 'white',
                   font = ('TlwgTypist', 12))
        self.e2.pack(side = TOP, anchor = NW)
        l3 = Label(f4,
                   text = 'UserName:',
                   bg = 'white',
                   font = ('URWGothic', 12))
        l3.pack(side = TOP, anchor = NW)
        self.e3 = Entry(f4,
                   bg = 'white',
                   font = ('TlwgTypist', 12))
        self.e3.pack(side = TOP, anchor = NW)
        f5 = Frame(f4,
                   bg = 'white')
        f5.pack(side = TOP, anchor = NW)
        l4 = Label(f5,
                   text = 'Password:',
                   bg = 'white',
                   font = ('URWGothic', 12))
        l4.pack(side = TOP, anchor = NW)
        self.e4 = Entry(f5,
                   bg = 'white',
                   font = ('TlwgTypist', 12),
                   show = '*')
        self.e4.pack(side = LEFT)
        self.show_var = 0
        self.show = Button(f5,
                           text = 'Show',
                           bg = 'white',
                           command = self.show_func,
                           font = ('URWGothic', 12))
        self.show.pack(side = LEFT)
        self.e_deactive()
        self.update = Button(f4,
                             text = 'UPDATE',
                             font = ('TlwgTypist', 11, 'bold'),
                             highlightthicknes = 0,
                             command = self.proxy_update)
        self.update.pack(side = TOP, anchor = NW, pady = 3)
    def show_func(self):
        if self.show_var == 0:
            self.e4['show'] = ''
            self.show['text'] = 'Hide'
            print('Entered Hide Block')
            self.show_var = 1
        else:
            self.e4['show'] = '*'
            print('Enter the show bloack')
            self.show['text'] = 'Show'
            self.show_var = 0
    def e_active(self, *args):
        self.e1['state'] = self.e2['state'] = self.e3['state'] = self.e4['state'] = ['normal']
    def e_deactive(self, *args):
        self.e1['state'] = self.e2['state'] = self.e3['state'] = self.e4['state'] = ['disabled']
    def proxy_update(self):
        try:
            with open('/etc/apt/apt.conf', 'w') as file:
                if self.flag == 0:
                    os.system("notify-send 'Proxy Configuration updated to No Proxy.'")
                else:
                    self.host = self.e1.get()
                    self.port = self.e2.get()
                    self.user = self.e3.get()
                    self.pwd =  self.e4.get()
                    file.write(f'Acquire::http::proxy "http://{self.user}:{self.pwd}@{self.user}:{self.pwd}/";')
                    file.write(f'Acquire::https::proxy "https://{self.user}:{self.pwd}@{self.user}:{self.pwd}/";')
                    os.system("notify-send 'Proxy COnfiguration Updated Successfully.'")
        except:
            print('Entered')
            os.system("notify-send 'Proxy Configuration Not Updated.'")
    def details_prompt(self):
        self.f3.destroy()
        self.f3 = Frame(self.root,
                        bg = 'white')
        self.f3.pack()
        self.r1 = Label(self.f3,
                        text = 'USER DETAILS',
                        font = ('TlwgTypist', 12, 'bold'),
                        bg = 'white')
        self.r1.pack(fill = X)
        self.f4 = Frame(self.f3,
                        bg = 'white')
        self.f4.pack(side = LEFT, anchor = NW, pady = 40, fill = X)
        self.r2 = Label(self.f4,
                        text = 'Name:',
                        bg = 'white',
                        font = ('URWGothic', 12))
        self.r2.pack(side = TOP, anchor = NW)
        self.name = Entry(self.f4,
                        font = ('TlwgTypist', 12))
        self.name.pack(side = TOP, anchor = NW)
        self.r2 = Label(self.f4,
                        text = 'Department:',
                        bg = 'white',
                        font = ('URWGothic', 12))
        self.r2.pack(side = TOP, anchor = NW)
        self.dept = Entry(self.f4,
                        font = ('TlwgTypist', 12))
        self.dept.pack(side = TOP, anchor = NW)
        self.next['command'] = self.package_installer
        self.back['command'] = self.network_access
    def package_installer(self):
        self.next['text'] = 'Start'
        self.f3.destroy()
        self.f3 = Frame(self.root,
                        bg = 'white')
        self.f3.pack(side = LEFT,anchor = NW)
        Message(self.f3,
                bg = 'white',
                text = '''After this process the following packges will be installed in your PC:
1.Python3-tk
2.Python3-numpy
3.Python3-pandas
4.Python3-pyperclip
And so 1.2 GB disk space is required to continue the installation.
Press "Start" to continue the installtion.........''',
                font = ('URWGothic', 11, 'italic')).pack(side = LEFT)
        self.progressbar = ttk.Progressbar(self.root)
        self.progressbar.place(relx = 0.289, rely = 0.5)
        self.progressbar['maximum'] = 100
        self.progressbar['length'] = 500
        self.progressbar['value'] = 100
        self.progress_text = srctext.ScrolledText(self.root,
                                                  width = 60,
                                                  height = 8)
        self.progress_text.place(relx = 0.289, rely = 0.55)
        self.next['command'] = None
        self.back['command'] = self.details_prompt
    def dependency_installation(self):
        os.system('apt install python3-tk')
        os.system('apt install python3-numpy')
        os.system('apt install python3-pandas')
        os.system('apt install python3-pyperclip')
if __name__ == '__main__':
    obj = Installer()
