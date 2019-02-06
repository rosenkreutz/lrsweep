#!env/bin/python

import argparse
import json
import requests


def run():
    aws_ips = requests.get('https://ip-ranges.amazonaws.com/ip-ranges.json')
    aws_ips = json.loads(aws_ips.content)

    for site in aws_ips['prefixes']:
        if args.search_region in site['region']:
            if 'gov' not in site['region']:
                print(site['ip_prefix'])


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Grabs AWS EC2 IP ranges', prog='search_aws_ips')
    # parser.add_argument('-iF', action='store', dest='inputFile', help='nmap ping sweep output file', required=True)
    parser.add_argument('-r', action='store', dest='search_region', help='AWS EC2 Region to get IPs for', required=True)
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    args = parser.parse_args()

    run()
