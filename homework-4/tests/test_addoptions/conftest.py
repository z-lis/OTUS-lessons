def pytest_addoption(parser):
    parser.addoption("--url", default="https://ya.ru", help="URL for testing")
    parser.addoption("--status_code", default=200, help="Expected status code")
