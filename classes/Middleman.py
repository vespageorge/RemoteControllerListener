from classes.System import SystemInfo
from classes.RequestsAPI import Requests
import time
import multiprocessing
from .constants import *

class Middleman:
    def __init__(self, configFile: object, debug = False) -> None:
        self.debugLevel = debug
        self.sysConn    = SystemInfo()
        self.apiConn    = Requests(configFile, self.sysConn)
        
        self.procShadowListen = multiprocessing.Process(target=self.shadowListener)
        self.procShadowListen.start()
        
        time.sleep(15)
        self.procShadowListen.terminate() # to kill process
    
    def shadowListener(self):
        while True:
            reqStats, reqBody = self.apiConn.GetCommandList(self.apiConn.currentDevice['id'])
            if reqStats is False:
                if self.debugLevel is True:
                    print(reqBody)
                self.procShadowListen.terminate()
                break

            if self.debugLevel is True:
                print(f"Request [{API_GET_CMDS}] runned with success")

            for cmd in reqBody:
                self.sysConn.ExecuteCMD(self.sysConn, cmd)
                self.apiConn.UpdateCommandStatus(self.sysConn.imgName, cmd)
            
            time.sleep(2)