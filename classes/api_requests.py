'''Class api_requests'''
import requests

class Requests:
    '''Class used to do all request to API'''

    url = None
    last_resp = None
    header = {
        "Content-type": "application/x-www-form-urlencoded",
        "Accept": "text/plain"
      }

    def __init__(self,hwid, host_data):
        ip_address = host_data['DOMAIN']
        port = host_data['PORT']
        self.url = ip_address + ":" + port + "/api"
        response = requests.get(str(self.url) + "/get-setup/" + str(hwid), timeout=10)
        print(response.status_code)

    def get_command(self, cmd_id):
        '''Method used to do get command as json format'''
        response = requests.get(self.url + "/get-commands/" + str(cmd_id), timeout=10)
        return response.json()

    def post_new_setup(self, payload):
        '''Method used to do create new setups'''
        path = str(self.url) + "/post-setup"
        response = requests.post(path, data=payload, headers=self.header, timeout=10)
        self.last_resp = response.json()

    def update_cmd_status(self, cmd_id):
        '''Method used to update status on specific command used'''
        path = str(self.url) + "/update-cmd-status/" + str(cmd_id)
        response = requests.get(path, timeout=10)
        if response.status_code == 200:
            print("Aplicatie deschisa cu success")
