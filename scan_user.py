#! /usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'zealot'

import yaml,paramiko,threading,sys,threadpool


userfile = sys.argv[1]
default_password = "check in your password"

class Getinfo(object):
    def __init__(self,usersfile):
        self.usersfile = usersfile
        self.f = open(self.usersfile)
        self.usersyaml = yaml.load(self.f)
    def getuserlist(self):
        alluser = []
        for i in self.usersyaml.keys():
            for k in  self.usersyaml.get(i).split():
                alluser.append(k)
        a = set(alluser)
        alluser = []
        for i in a:
            alluser.append(i)
        return alluser
    def getiplist(self):
        iplist = self.usersyaml.keys()
        return iplist




txy = Getinfo(userfile)

def sshconn_test(hostname):
    conn = paramiko.SSHClient()
    conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    for username in txy.getuserlist():
        try:
            conn.connect(hostname=hostname,port=int(your ssh port),username=username,password=default_password,timeout=10)
            print "%s : %s has default password" %(hostname,username)
            conn.close()
        except Exception,e:
            print "%s :check ok!" % hostname


def print_result(request,result):
    print result



if __name__ == '__main__':
    pools = threadpool.ThreadPool(10)
    requests = threadpool.makeRequests(sshconn_test,txy.getiplist(),print_result)
    [pools.putRequest(req) for req in requests]
    pools.wait()


