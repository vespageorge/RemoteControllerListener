'''Main script used as a lisener'''
import argparse, configparser
from classes.Middleman import Middleman

def main():
    ''' Main function which is used to initialized classes'''

    parser = argparse.ArgumentParser()
    parser.add_argument("-c","--config", help="Use for selecting config_name.ini")

    args = vars(parser.parse_args())

    config = configparser.ConfigParser()
    config.read(f"settings/{args['config']}.ini")

    Middleman(config, True)

if __name__ == "__main__":
    main()
