# author:Mitchell
# date:11.26
import socket
import re


# 判断输入的ip地址是否合法
def check_ip(ip):
    # 构建正则表达式对象
    ip_moudle = re.compile('((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}')
    if len(ip) != 0 and ip_moudle.match(ip):
        return True
    else:
        return False


# 对传入的ip地址，在一定范围内扫描开放的端口，并打印
def scan_port(ip):
    # 取出范围值
    port_begin, port_end = (1, 1024)
    for pt in range(int(port_begin), int(port_end) + 1):
        # 使用ipv4实现tcp连接
        # AF_INET家族包括Internet地址，AF_UNIX家族用于同一台机器上的进程间通信
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置延迟0.5s
        sk.settimeout(0.5)
        # connect_ex()方法，该方法如果链接成功会返回0，失败会返回errno库中的errorcode中的key
        conn = sk.connect_ex((ip, pt))
        if conn == 0:
            print(f'主机:{ip},端口:{pt}已开放')
        else:
            print(f'主机:{ip},端口:{pt}未开放')
        sk.close()
    print('扫描完毕！')


ip = input('请输入需要扫描的ip：')
if check_ip(ip):
    scan_port(ip)
else:
    print("ip格式有误，请检查！")
