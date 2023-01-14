import platform,socket,re,uuid,logging
import subprocess
import webbrowser
class SystemInfo:

    info={}

    def __init__(self):
        print("system conected!")
        self.get_data()

    def get_data(self):
        try:
            self.info['platform']=platform.system()
            self.info['hostname']=socket.gethostname()
            self.info['ip_address']=socket.gethostbyname(socket.gethostname())
            self.info['mac_address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
            self.info['hwid'] = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()
            return self.info
        except Exception as e:
            logging.exception(e)

    def run_cmd(self,command):
        # webbrowser.open("https://google.com")
        try:
            subprocess.call([command])
        except:
            print("no command for you")
