import ssl
import socket

def get_ssl_info(domain):
    context = ssl.create_default_context()
    try:
       with socket.create_connection((domain, 443)) as sock:
           with context.wrap_socket(sock, server_hostname=domain) as secure_socket:
               certificate = secure_socket.getpeercert()
               expiry_date = certificate['notAfter']
               issuer = None
               for item in certificate['issuer']:

                   field_name, field_value = item[0]
                   if field_name == "organizationName":
                       issuer = field_value
                       break
               return True,issuer,expiry_date,None

    except ssl.SSLCertVerificationError:
        return False,None,None,"CERT_VERIFICATION_FAILED"

    except socket.timeout:
        return False,None,None,"CONNECTION_TIMEOUT"

    except socket.gaierror:
        return False,None,None,"DNS_LOOKUP_FAILED"

    except ssl.SSLError:
        return False,None,None,"SSL_ERROR"

    except Exception as e:
        return False,None,None,str(e)


