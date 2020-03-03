import re
import socket


def check_ip_by_re(ip_address):
    if re.match("([0-9]{1,3}[\.]){3}[0-9]{1,3}", str(ip_address)):
        return True
    return False


def check_ip_by_socket(ip_address):
    str_ip = str(ip_address)
    try:
        socket.inet_aton(str_ip)
        return str_ip.count('.') == 3
    except OSError:
        return False


assert check_ip_by_re('') is False
assert check_ip_by_re('192.168.0.1') is True
assert check_ip_by_re('0.0.0.1') is True
assert check_ip_by_re('10.100.500.32') is True
assert check_ip_by_re(700) is False
assert check_ip_by_re('127.0.1') is False

assert check_ip_by_socket('') is False
assert check_ip_by_socket('192.168.0.1') is True
assert check_ip_by_socket('0.0.0.1') is True
assert check_ip_by_socket('10.100.500.32') is False
assert check_ip_by_socket(700) is False
assert check_ip_by_socket('127.0.1') is False
