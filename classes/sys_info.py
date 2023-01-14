'''Class sys_info'''
import platform
import socket
import re
import uuid
import logging
import subprocess
import webbrowser

class SystemInfo:
    '''Class used to run and collect information about current setup'''
    info={}

    def __init__(self):
        print("system conected!")
        self.get_data()

    def get_data(self):
        '''Method used to do get data from current setup'''
        try:
            self.info['platform']=platform.system()
            self.info['hostname']=socket.gethostname()
            self.info['ip_address']=socket.gethostbyname(socket.gethostname())
            self.info['mac_address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
            self.info['hwid'] = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()
            return self.info
        except Exception as error_msg: # pylint: disable=W0703
            logging.exception(error_msg)

    def run_cmd(self,command):
        '''Method used to do get data from current setup'''
        webbrowser.open("https://google.com")
        try:
            subprocess.call([command])
        except: # pylint: disable=W0702
            print("no command for you")
