from parser import parse_url
from validator import validate_url
from url_features import results_of_features
from risk_engine import (calculate_score,calculate_risk)
from ssl_check import get_ssl_info
from dns_check import get_dns_info
from domain_info import get_domain_info
from reputation import get_reputation
from  report import generate_report


def main():
    print("="*100)
    print("Phishing URL Detection System".center(100))
    print("="*100)
    print()

    url = input("Enter URL: ")
    print("Analyzing URL...")
    print()

    parsed_url = parse_url(url)

    is_valid = validate_url(parsed_url)
    if is_valid:
        print("URL Validation successful!")
        print()
    else:
        print("INVALID URL!")
        exit()

    domain = parsed_url.hostname
    scheme = parsed_url.scheme

    uses_https, is_long_url, contains_at_symbol, many_subdomains, contains_ip_address = results_of_features(url,scheme,domain)
    valid_ssl, issuer, expiry_date, ssl_error =get_ssl_info(domain)
    valid_dns, ip_address, dns_error = get_dns_info(domain)
    whois_available, domain_age, days_until_expiry, whois_error = get_domain_info(domain)
    data_retrieved, malicious, suspicious, harmless, error = get_reputation(domain)

    analysis_data = {
                     #URL features
                     "uses_https":uses_https,
                     "is_long_url":is_long_url,
                     "contains_at_symbol":contains_at_symbol,
                     "many_subdomains":many_subdomains,
                     "contains_ip_address":contains_ip_address,

                     #SSL
                     "valid_ssl":valid_ssl,

                     #WHOIS
                     "domain_age":domain_age,

                     #VIRUS-TOTAL REPUTATION
                     "malicious":malicious,
                     "suspicious":suspicious,

                     #DNS_INFO
                     "valid_dns":valid_dns
                     }

    score = calculate_score(analysis_data)
    risk  = calculate_risk(score)

    report_data = {
        "url":url,
        "domain":domain,
        "score":score,
        "risk":risk,

        "uses_https":uses_https,
        "is_long_url":is_long_url,
        "contains_at_symbol":contains_at_symbol,
        "many_subdomains":many_subdomains,
        "contains_ip_address":contains_ip_address,

        "valid_ssl":valid_ssl,
        "issuer":issuer,
        "expiry_date":expiry_date,
        "ssl_error":ssl_error,

        "valid_dns":valid_dns,
        "ip_address":ip_address,
        "dns_error":dns_error,

        "whois_available":whois_available,
        "domain_age":domain_age,
        "days_until_expiry":days_until_expiry,
        "whois_error":whois_error,

        "data_retrieved":data_retrieved,
        "malicious":malicious,
        "suspicious":suspicious,
        "harmless":harmless,
        "error":error
    }

    generate_report(report_data)

if __name__ == "__main__":
    main()
