import fetcher


def test_happy_path():
    url = 'http://www.google.com'
    data = fetcher.fetch(url)
    assert data
    assert len(data) > 0
    assert 'google' in data.lower()

# how many A's?
#
