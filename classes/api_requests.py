import requests, json

class Requests:

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
        response = requests.get(str(self.url)+"/get-setup/"+str(hwid))
        print(response.status_code)

    def get_command(self,id):
        response = requests.get( self.url + "/get-commands/"+str(id))
        return response.json()

    def post_new_setup(self, payload):
        path = str(self.url) + "/post-setup"
        response = requests.post(path, data=payload, headers=self.header)
        self.last_resp = response.json()

    def update_cmd_status(self, cmd_id):
        path = str(self.url) + "/update-cmd-status/"+ str(cmd_id)
        response = requests.get(path)
        print(response.status_code)
