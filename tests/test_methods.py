"""This is a sample python file for testing functions from the source code."""

import pytest

from nkyx_ds_template.hello_world import hello_world


def hello_test():
    """
    This defines the expected usage, which can then be used in various test cases.
    Pytest will not execute this code directly, since the function does not contain the suffix "test"
    """
    hello_world()


def test_hello():
    """
    This is a simple test, which can use a mock to override online functionality.
    unit_test_mocks: Fixture located in conftest.py, implicitly imported via pytest.
    """
    hello_test()


@pytest.mark.integration
def test_hello_all():
    """
    This test is marked implicitly as an integration test using custom markers
    """
    hello_test()
