# Any pytest file should start with test_ or end with _test
import pytest


@pytest.mark.smoke
def test_first_program(setup):
    print("Hello")


@pytest.mark.xfail
def test_greet():
    print("Hello there")


def test_cross_browser(cross_browser):
    print(cross_browser[0])