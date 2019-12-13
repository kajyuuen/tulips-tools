import argparse

from utils.config import save_config, load_config
from utils.viewer import Viewer

def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter)
    subparsers = parser.add_subparsers(title='commands',
                                       dest='command')
    subparsers.required = True
    parse_config(subparsers)
    parse_tulips(subparsers)
    args = parser.parse_args()

    if args.command == "set":
        save_config(args.user, args.password)
    else:
        # Setting user, password
        if args.user is None or args.password is None:
            user, password = load_config()
        else:
            user, password = args.user, args.password

        viewer = Viewer(user, password)
        if args.command == "history":
            viewer.history()
        elif args.command == "borrow":
            viewer.borrow()

def parse_config(subparsers):
    parser_config = subparsers.add_parser('config')
    subparsers_config = parser_config.add_subparsers(title='commands',
                                                     dest='command')
    subparsers_config.required = True

    parser_config_set = subparsers_config.add_parser('set')
    parser_config_set_required = parser_config_set.add_argument_group('required arguments')
    parser_config_set_required.add_argument('-u',
                                            '--user',
                                            dest='user',
                                            required=True)
    parser_config_set_required.add_argument('-p',
                                            '--password',
                                            dest='password',
                                            required=True)

def parse_tulips(subparsers):
    parser_config = subparsers.add_parser('view')
    subparsers_config = parser_config.add_subparsers(title='commands',
                                                     dest='command')
    subparsers_config.required = True

    # history
    parser_config_set = subparsers_config.add_parser('history')
    parser_config_set_required = parser_config_set.add_argument_group('required arguments')
    parser_config_set_required.add_argument('-u',
                                            '--user',
                                            dest='user')
    parser_config_set_required.add_argument('-p',
                                            '--password',
                                            dest='password')

    # borrow
    parser_config_set = subparsers_config.add_parser('borrow')
    parser_config_set_required = parser_config_set.add_argument_group('required arguments')
    parser_config_set_required.add_argument('-u',
                                            '--user',
                                            dest='user')
    parser_config_set_required.add_argument('-p',
                                            '--password',
                                            dest='password')

if __name__ == "__main__":
    main()