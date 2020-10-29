from socket import *
import time

start_time = time.time()

if __name__ == '__main__':
    target = input('Enter the host to be scanned: ')
    target_IP = gethostbyname(target)
    print('Starting scan on host: ', target_IP)

    for i in range(50,500):
        port = socket(AF_INET, SOCK_STREAM)

        connection = port.connect_ex((target_IP,i))
        if (connection == 0):
            print ('Port %d: OPEN' % (i))
        port.close()
print('Time take:', time.time() - start_time)
