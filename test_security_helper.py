from unittest.mock import Mock, patch
from security_helper import SecurityScanner


@patch("security_helper.requests.get")
def test_fetch_site(mock_get):

    mock_response = Mock()

    mock_response.status_code = 200
    mock_response.headers = {
        "X-Frame-Options": "DENY",
        "Strict-Transport-Security": "max-age=31536000"
    }

    mock_get.return_value = mock_response

    scanner = SecurityScanner("https://google.com")

    headers, status = scanner.fetch_site()

    assert status == 200
    assert "X-Frame-Options" in headers
    

def test_init():

    scanner = SecurityScanner("https://google.com")

    assert scanner.url == "https://google.com"