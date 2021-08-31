# pytest methods should start with test
# any code should be wrapped in method only
# method name should have sense
# -k stands for method names execution, -s for logs in output, -v for more info metadata
# you can run specific file with py.test <filename>
# you can mark (tag) tests with @pytest.mark.smoke and then run with -m
# you can skip tests with @pytest.mark.skip
import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_first_program():
    msg = "Hello"
    assert msg == "Hi", 'Test failed because strings do not match'


def test_second_program():
    a = 4
    b = 6
    assert a + 2 == 6, 'Addition do not match'


def test_fixture_demo(setup):
    print("I will execute steps in fixture_demo method")