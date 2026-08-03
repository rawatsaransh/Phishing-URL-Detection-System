def generate_report(report_data):
    print("=" * 100)
    print("PHISHING URL DETECTION REPORT".center(100))
    print("=" * 100)
    print(f"URL                   : {report_data['url']}")
    print(f"Domain                : {report_data['domain']}")
    print()
    print(f"Overall Risk          :{report_data['risk']}")
    print(f"Risk Score            : {report_data['score']}")

    print()
    print("-" * 100)
    print("URL FEATURES".center(100))
    print("-" * 100)
    print()
    print(f"HTTPS Used            : {format_boolean(report_data['uses_https'])}")
    print(f"Long URL              : {format_boolean(report_data['is_long_url'])}")
    print(f"Contains @ Symbol     : {format_boolean(report_data['contains_at_symbol'])}")
    print(f"Many Subdomains       : {format_boolean(report_data['many_subdomains'])}")
    print(f"IP Address In URL     : {format_boolean(report_data['contains_ip_address'])}")

    print()
    print("-" * 100)
    print("SSL INFORMATION 🔒".center(100))
    print("-" * 100)
    print()

    if report_data["valid_ssl"]:
        print(f"SSL Certificate       : Valid")
        print(f"Issuer                : {report_data['issuer']}")
        print(f"Expiry Date           : {report_data['expiry_date']}")
    else:
        print(f"SSL Certificate       : Invalid")
        print(f"Reason                : {report_data['ssl_error']}")

    print()
    print("-" * 100)
    print("DNS INFORMATION 🌐".center(100))
    print("-" * 100)

    if report_data["valid_dns"]:
        print(f"DNS Resolution        : ✓ Success")
        print(f"IP Address            : {report_data['ip_address']}")
    else:
        print(f"DNS Resolution        : ✗ Failed")
        print(f"Reason                : {report_data['dns_error']}")

    print()
    print("-" * 100)
    print("DOMAIN INFORMATION 📅".center(100))
    print("-" * 100)

    if report_data["whois_available"]:
        print(f"WHOIS Available       : ✓ Yes")
        print(f"Domain Age            : {report_data['domain_age']} days")
        print(f"Expires In            : {report_data['days_until_expiry']} days")
    else:
        print(f"WHOIS Available       : ✗ No")
        print(f"Reason                : {report_data['whois_error']}")

    print()
    print("-" * 100)
    print("VIRUS-TOTAL REPUTATION 🛡️".center(100))
    print("-" * 100)

    if report_data["data_retrieved"]:
        print(f"Malicious Engines     : {report_data['malicious']}")
        print(f"Suspicious Engines    : {report_data['suspicious']}")
        print(f"Harmless Engines      : {report_data['harmless']}")
    else:
        print(f"VirusTotal Data       : Not Available")
        print(f"Reason                : {report_data['error']}")

    print()
    print("=" * 100)
    print("FINAL RESULT".center(100))
    print("=" * 100)
    print()

    if report_data['risk'] == '🟢 LOW':
        print("No strong phishing indicators detected.")

    elif report_data['risk'] == '🟡 MEDIUM':
        print("This URL contains several suspicious indicators.")
        print("Exercise caution before visiting it.")

    else:
        print("WARNING: This URL appears to be HIGH RISK.")
        print("Avoid visiting or entering sensitive information.")

    print()
    print("-" * 100)

def format_boolean(value):
    if value:
        return "✓ Yes"
    else:
        return "✗ No"

