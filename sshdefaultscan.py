#!/usr/bin/env python
"""
sshdefaultscan

Scan networks for SSH servers with default username and password.
"""
import argparse
import logging
from time import time

import nmap
import paramiko

SSH_DEFAULT_USERNAME = 'root'
SSH_DEFAULT_PASSWORD = 'root'

#
# Main
#
if __name__ == '__main__':
    ###########################################################################
    # Bootstrap
    #

    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Scan networks for SSH servers with default username and password.')
    parser.add_argument('hosts', help='An IP address for a hostname or network, ex: 192.168.1.1 for single host or 192.168.1.1-254 for network')
    parser.add_argument('-u', '--username', help='Set username, default is "root"', default=SSH_DEFAULT_USERNAME)
    parser.add_argument('-p', '--password', help='Set password, default is "root"', default=SSH_DEFAULT_PASSWORD)
    parser.add_argument('--fast', help='Change timeout settings for the scanner in order to scan faster (T5)', default=False, action='store_true')
    args = parser.parse_args()

    # Setup logging
    logger = logging.getLogger('sshdefaultscan')
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler = logging.FileHandler('sshdefaultscan.log')
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    ###########################################################################
    # Scan
    #
    logger.debug('Scanning...')
    hosts = list()
    nmap_arguments = '' if not args.fast else '-T5'
    nm = nmap.PortScanner()
    scan = nm.scan(args.hosts, '22', arguments=nmap_arguments)
    stats = scan.get('nmap').get('scanstats')
    logger.debug(
        '{up} hosts up, {total} total in {elapsed_time}s'.format(
            up=stats.get('uphosts'),
            total=stats.get('totalhosts'),
            elapsed_time=stats.get('elapsed')
        )
    )
    for host, data in list(scan.get('scan').items()):
        if data.get('tcp') and data.get('tcp').get(22).get('state') == 'open':
            hosts.append(host)
            logger.debug('{host} Seems to have SSH open'.format(host=host))

    if not hosts:
        logger.debug('No hosts found with port 22 open.')
        exit()

    ###########################################################################
    # Test credentials
    #
    logger.debug('Testing credentials...')
    for host in hosts:
        start_time = time()
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(
                host,
                username=args.username,
                password=args.password
            )
            logger.info('{host} Logged in with {username}:{password} in {elapsed_time}s'.format(
                host=host,
                username=args.username,
                password=args.password,
                elapsed_time=round(time() - start_time, 2)
            ))
        except (
            paramiko.ssh_exception.AuthenticationException,
            paramiko.ssh_exception.SSHException
        ) as e:
            logger.debug('{host} {exception} ({elapsed_time}s)'.format(
                host=host,
                exception=e,
                elapsed_time=round(time() - start_time, 2)
            ))
