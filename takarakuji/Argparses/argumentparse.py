import argparse

def argumentParse():
    parse = argparse.ArgumentParser(description='Takarakuji Analysis')
    subparsers = parse.add_subparsers()

    checksite = subparsers.add_parser('checksite')
    checksite.add_help = """
        (checksite) 
    """
    checksite.add_argument('-c', '--check', action='store_true', help='')
    checksite.add_argument('-u', '--update', action='store_true')

    analyze = subparsers.add_parser('analyse', help='See `analyze -h`')
    analyze.add_argument('-r', '--run', action='store_true')



    return parse.parse_args()

if __name__ == '__main__':
    print(argumentParse())