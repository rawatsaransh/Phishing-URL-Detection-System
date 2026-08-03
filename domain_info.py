import whois
import datetime

def get_domain_info(domain):
    try:
        domain_info = whois.whois(domain)

        creation_date = domain_info.creation_date
        if type(creation_date) == datetime.datetime:
            creation_date = creation_date.date()
        else:
            creation_date = creation_date[0]
            creation_date = creation_date.date()

        expiration_date = domain_info.expiration_date
        if type(expiration_date) == datetime.datetime:
            expiration_date = expiration_date.date()
        else:
            expiration_date = expiration_date[0]
            expiration_date = expiration_date.date()

        today = datetime.date.today()
        domain_age = (today - creation_date).days
        days_until_expiry = (expiration_date - today).days

        return True, domain_age, days_until_expiry,None


    except TimeoutError:
        return False, None, None, "WHOIS_REQUEST_TIMEOUT"

    except Exception as e:
        return False, None, None, "WHOIS_LOOKUP_FAILED"
