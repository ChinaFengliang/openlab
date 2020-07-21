#!/usr/bin/python

import os

def bind_device(ip, account, password):
    cmdline = 'ipmitool -H %s -I lanplus -U %s -P %s\
        sol activate' % (ip, account, password)
    os.system(cmdline)
    return 0

def unbind_device(ip, account, password):
    cmdline = 'ipmitool -H %s -I lanplus -U %s -P %s\
        sol deactivate' % (ip, account, password)
    os.system(cmdline)
    return 0

def reboot_device(ip, account, password):
    cmdline = 'ipmitool -H %s -I lanplus -U %s -P %s\
        chassis power reset' % (ip, account, password)
    os.system(cmdline)
    return 0

def poweron_device(ip, account, password):
    cmdline = 'ipmitool -H %s -I lanplus -U %s -P %s\
        chassis power on' % (ip, account, password)
    os.system(cmdline)
    return 0

def poweroff_device(ip, account, password):
    cmdline = 'ipmitool -H %s -I lanplus -U %s -P %s\
        chassis power off' % (ip, account, password)
    os.system(cmdline)
    return 0

def device_status(ip, account, password):
    cmdline = 'ipmitool -H %s -I lanplus -U %s -P %s\
        chassis status' % (ip, account, password)
    os.system(cmdline)
    return 0
