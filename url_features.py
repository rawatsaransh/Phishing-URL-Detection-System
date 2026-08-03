import re

def results_of_features(url,scheme,domain):
    uses_https = is_using_https(scheme)
    is_long_url = is_url_too_long(url)
    contains_at_symbol = has_at_symbol(url)
    many_subdomains = has_many_subdomains(domain)
    contains_ip_address = has_ip_address(url)
    return uses_https,is_long_url,contains_at_symbol,many_subdomains,contains_ip_address

def is_using_https(scheme):
    return scheme == "https"

def is_url_too_long(url):
    return len(url) > 75

def has_at_symbol(url):
    return "@" in url

def has_many_subdomains(domain):
    domain_parts = domain.split(".")
    parts = len(domain_parts)
    return parts > 3

def has_ip_address(url):
    matches = re.findall(r"[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+", url)

    for ip in matches:
        octets = ip.split(".")

        if all(0 <= int(octet) <= 255 for octet in octets):
            return True

    return False




