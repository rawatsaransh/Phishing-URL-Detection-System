def validate_url(parsed_url):

    if parsed_url.scheme and parsed_url.netloc:
        return True
    else:
        return False

