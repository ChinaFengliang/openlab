#!/usr/bin/python

import os


def bind_device(ip):
    cmdline = 'ipmitool -H %s -I lanplus -U root -P Huawei12#$\
        sol activate' % ip
    os.system(cmdline)
    return 0


def unbind_device(ip):
    cmdline = 'ipmitool -H %s -I lanplus -U root -P Huawei12#$\
        sol deactivate' % ip
    os.system(cmdline)
    return 0


def reset_device(ip):
    cmdline = 'ipmitool -H %s -I lanplus -U root -P Huawei12#$\
        chassis power reset' % ip
    os.system(cmdline)
    return 0


def poweron_device(ip):
    cmdline = 'ipmitool -H %s -I lanplus -U root -P Huawei12#$\
        chassis power on' % ip
    os.system(cmdline)
    return 0


def poweroff_device(ip):
    cmdline = 'ipmitool -H %s -I lanplus -U root -P Huawei12#$\
        chassis power off' % ip
    os.system(cmdline)
    return 0
