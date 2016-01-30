#still needs some fixing to remove the need to ctrl-c at the end of the scan

import optparse
from socket import *


def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send('portscanner\r\n')
        results = connSkt.recv(100)
        print ('[*]%d/tcp open' % tgtPort)
        print ('[*]' + str(results))
        connSkt.close()
    except:
        print('[-]%d/tcp closed' % tgtPort)


def portScan(tgtHost, tgtPorts):
    try:
        tgtHost = gethostbyname(tgtHost)
    except:
        print ("[-] Cannot resolve '%s': Unknown host" % tgtHost)
        setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print 'Scanning port ' + tgtPort
        connScan(tgtHost, int(tgtPort))


def main():
    parser = optparse.OptionParser("usage%prog" + " -H <target host> -p <target port>")
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='string', help='specify target port[s] separated by comma')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')
    if (tgtHost is None) | (tgtPorts[0] is None):
        print('[-] You must specify a target host and port[s].')
        exit(0)

    portScan(tgtHost, tgtPorts)



if __name__ == '__main__':
    main()
