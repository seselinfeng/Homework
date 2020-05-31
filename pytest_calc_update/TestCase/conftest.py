import pytest
from pytest_calc_update.TestedClass.Calc import Calc


@pytest.fixture(scope="session")
def init_calc():
    calc = Calc()
    return calc


def pytest_collection_modifyitems(session, config, items: list):
    for item in items:
        # func_name = item.nodeid.split("::")[2]
        # func_name = func_name.split("[")[0]
        # func_name = func_name.split("_")[-1]
        # func_name= 1
        # print(func_name)
        # item.add_marker(pytest.mark.func_name)
        # print(item.__name__)
        # item.add_marker(pytest.mark.item.nodeid)
        if "add" in item.nodeid:
            item.add_marker(pytest.mark.add)
        elif "div" in item.nodeid:
            item.add_marker(pytest.mark.div)
    # items.reverse()
