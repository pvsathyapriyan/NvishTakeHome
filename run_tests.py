import pytest


if __name__ == "__main__":
    pytest.main(["tests/",
                 "-v",
                 "--html=tests_report.html",
                 "--self-contained-html"])
