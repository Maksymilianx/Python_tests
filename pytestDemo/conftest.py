# fixtures are used as setup and tear down methods for test cases - conftest file to generalize fixture and make it
# available to all test cases
# Datadriven and parametrization can be done with return statements in tuple format
# When you define fixture scope to class only, it will run once before class is initiated and at the end
import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will be executed last")


@pytest.fixture()
def data_load():
    print("user profile data is being created")
    return ["Maksymilian", "Krajewski", "krajewski.maksymilian@gmail.com"]


@pytest.fixture(params=["Chrome", "Firefox", "IE"])
def cross_browser(request):
    return request.param
