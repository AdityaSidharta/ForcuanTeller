def validate_gmail(gmail_address):
    assert isinstance(gmail_address, str)
    assert gmail_address.endswith("@gmail.com")
    assert len(gmail_address) > 10
