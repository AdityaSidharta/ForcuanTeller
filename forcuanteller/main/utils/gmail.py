def validate_gmail(gmail_address):
    assert isinstance(gmail_address, str), "Gmail address should be a string, receives: {} instead".format(
        gmail_address
    )
    assert gmail_address.endswith("@gmail.com"), "Gmail address should end in @gmail.com, receives: {} instead".format(
        gmail_address
    )
    assert len(gmail_address) > 10, "Gmail address should have at least 11 characters, receives: {} instead".format(
        gmail_address
    )
