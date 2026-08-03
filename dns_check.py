import socket

def get_dns_info(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return True, ip_address, None

    except socket.gaierror:
        return False, None, 'DNS_LOOKUP_FAILED'

    except Exception as e:
        return False, None, str(e)
