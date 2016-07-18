import ftplib
import optparse


def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous', 'me@example.com')
        print ('\n[*]' + str(hostname) + ' FTP Anonymous Logon Successful')
        ftp.quit()
        return True
    except Exception, e:
        print('\n[-]' + str(hostname) + ' FTP Anonymous Logon Failed')
        return False
        # host = '192.168.95.179'
        # anonLogin(host)


# added in a file reader
def main():
    parser = optparse.OptionParser('uasge%prog -F <host list file>')
    parser.add_option('-F', dest='hostFile', type='string', help='Name of the host file')
    (options, args) = parser.parse_args()
    hostFile = options.hostFile

    if hostFile is None:
        print parser.usage
        exit(0)
    fn = open(hostFile, 'r')
    for line in fn.readlines():
        host = str(line)
        anonLogin(host)
    fn.close()


if __name__ == '__main__':
    main()
