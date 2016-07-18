import optparse
import nmap


def nmapScan(tgtHost, tgtPort):
    nScan = nmap.PortScanner()
    nScan.scan(tgtHost, tgtPort)
    state = nScan[tgtHost]['tcp'][int(tgtPort)]['state']
    print ("[*]" + tgtHost + "tcp/" + tgtPort + "" + state)


def main():
    parser = optparse.OptionParser("usage %prog" + " -H <target host> -p <target port>")
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='string', help='specify target port[s] separated by comma')
    (options, args) = parser.parse_args()
    tgtHost = optparse.tgtHost
    tgtPorts = str(options.tgtPort).split(',')
    if (tgtHost is None) | (tgtPorts[0] is None):
        print parser.usage
        exit(0)
    for tgtPort in tgtPorts:
        nmapScan(tgtHost, tgtPort)


if __name__ == '__main__':
    main()
