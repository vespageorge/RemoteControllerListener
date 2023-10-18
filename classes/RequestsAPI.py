'''Class api_requests'''
import os, json
import requests
from .constants import *

class Requests:
    '''Class used to do all request to API'''

    def __init__(self, configFile, systemConfig, debug = False):

        self.header = {
            "Content-type": "application/x-www-form-urlencoded",
            "Accept": "text/plain"
        }

        self.debug = debug
        
        self.url = configFile['HOST']['DOMAIN'] + ":" + configFile['HOST']['PORT'] + "/api"
        
        response = requests.get(self.url + API_GET_DEVICE + str(systemConfig.hwid), headers=self.header)
        statusResp, self.currentDevice = self.VerifyRequestResponse(response)

        if statusResp is True and self.currentDevice == {}:
            self.CreateNewDevice(systemConfig)

    def CreateNewDevice(self, payload):
        '''Method used to do create new setups'''
        path = f"{str(self.url)}/{API_POST_DEVICE}"

        response = requests.post(path, data=vars(payload), headers=self.header)
        _, self.currentDevice = self.VerifyRequestResponse(response) 
    
    def VerifyRequestResponse(self, request):
        if request.status_code == REQUEST_SUCCESS:
            try:
                return True, request.json()
            except:
                return True, {}
        if request.status_code == REQUEST_NOT_FOUND:
            return False, Exception(f"STATUS CODE[{request.status_code}]: Requested URL doesn't exist")
    
    def GetCommandList(self, cmd_id):
        '''Method used to do get command as json format'''
        response = requests.get(self.url + API_GET_CMDS + str(cmd_id), headers=self.header)
        return self.VerifyRequestResponse(response)
    
    def UpdateCommandStatus(self,sysConn, cmd):
        '''Method used to update status on specific command used'''
        response = requests.get(str(self.url) + API_UPDATE_CMD + str(cmd['id']), headers=self.header)
        if cmd['name'] == "screenshot":
            self._uploadFile(sysConn)
        return self.VerifyRequestResponse(response)
    
    def _uploadFile(self,sysConn):
        '''Method used to upload screenshots'''
        data = open(f"tmp/{sysConn}.png", 'rb')
        path = str(self.url) + API_UPLOAD_DATA
        response = requests.post(path,files={"img": data})
        data.close()
        os.remove(f"tmp/{sysConn}.png")
        return self.VerifyRequestResponse(response)
