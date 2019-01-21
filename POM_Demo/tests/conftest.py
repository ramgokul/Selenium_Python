import pytest

def pytest_addoption(parser):
    parser.addoption('--url', action='store', dest='url')
    parser.addoption('--browser', action='store', dest='browser', default='chrome')

@pytest.fixture()
def test_get_env_variables(request):
    map = dict()

    map['url'] = request.config.getoption('url')
    map['browser'] = request.config.getoption('browser').lower()
    return map