import pytest
from pytest_assume.plugin import assume

from pytest_calc.TestedClass.Calc import *


class TestCalc:
    def setup(self):
        self.calc = Calc()

    test_add_data = [(-1, -1, -2), (-1, 0, -1), (0, 0, 0), (0, 1, 1), (1, 1, 2),
                     (0.1, 0.1, 0.2), (11111111111111111111, 11111111111111111111, 22222222222222222222),
                     ("a", 2, 'type error'),
                     ([1], 1, 'type error'),
                     ({1}, 1, 'type error'),
                     ({1: 1}, 1, 'type error'),
                     ]

    @pytest.mark.parametrize("a,b,excepted", test_add_data)
    def test_add(self, a, b, excepted):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            self.result = self.calc.add(a, b)
            with assume:
                assert self.result == excepted
        else:
            with pytest.raises(TypeError):
                self.calc.add(a, b)

    test_div_data = [(-1, -1, 1), (-1, 0, -1), (0, 0, 0), (0, 1, 0), (1, 1, 1), ("a", 2, 'type error'),
                     ([1], 1, 'type error'),
                     ({1}, 1, 'type error'),
                     ({1: 1}, 1, 'type error'), ]

    @pytest.mark.parametrize("a,b,excepted", test_div_data)
    def test_div(self, a, b, excepted):
        if b == 0:
            with pytest.raises(ZeroDivisionError):
                self.calc.div(a, b)
        elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
            self.result = self.calc.div(a, b)
            with assume:
                assert self.result == excepted
        else:
            with pytest.raises(TypeError):
                self.calc.div(a, b)
