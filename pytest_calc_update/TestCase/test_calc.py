import pytest
import yaml
from pytest_assume.plugin import assume


class TestCalc:
    def setup(self):
        pass

    # self.calc = Calc()

    test_add_data = [(-1, -1, -2), (-1, 0, -1), (0, 0, 0), (0, 1, 1), (1, 1, 2),
                     (0.1, 0.1, 0.2), (11111111111111111111, 11111111111111111111, 22222222222222222222),
                     ("a", 2, 'type error'),
                     ([1], 1, 'type error'),
                     ({1}, 1, 'type error'),
                     ({1: 1}, 1, 'type error')
                     ]

    # @pytest.mark.parametrize("a,b,excepted", test_add_data)
    @pytest.mark.parametrize("a,b,excepted", yaml.safe_load(open("../datas/add_params.yaml")))
    def calc_add(self, a, b, excepted, init_calc):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            self.result = init_calc.add(a, b)
            with assume:
                assert self.result == excepted
        else:
            with pytest.raises(TypeError):
                init_calc.add(a, b)

    test_div_data = [(-1, -1, 1), (-1, 0, -1), (0, 0, 0), (0, 1, 0), (1, 1, 1), ("a", 2, 'type error'),
                     ([1], 1, 'type error'),
                     ({1}, 1, 'type error'),
                     ({1: 1}, 1, 'type error')]

    # @pytest.mark.parametrize("a,b,excepted", test_div_data)
    @pytest.mark.parametrize("a,b,excepted", yaml.safe_load(open("../datas/div_params.yaml")))
    def calc_div(self, a, b, excepted, init_calc):
        if b == 0:
            with pytest.raises(ZeroDivisionError):
                init_calc.div(a, b)
        elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
            self.result = init_calc.div(a, b)
            with assume:
                assert self.result == excepted
        else:
            with pytest.raises(TypeError):
                init_calc.div(a, b)

    @pytest.mark.parametrize("steps", yaml.safe_load(open("../datas/action.yaml")))
    @pytest.mark.parametrize("add_data1,add_data2,add_excepted", yaml.safe_load(open("../datas/add_params.yaml")))
    @pytest.mark.parametrize("div_data1,div_data2,div_excepted", yaml.safe_load(open("../datas/div_params.yaml")))
    def calc_math(self, steps, add_data1, add_data2, add_excepted, div_data1, div_data2, div_excepted, init_calc):
        print("steps{}".format(steps))
        # print("div_datas{}".format(div_datas))
        for step in steps:
            if step == 'add':
                if isinstance(add_data1, (int, float)) and isinstance(add_data2, (int, float)):
                    self.result = init_calc.add(add_data1, add_data2)
                    with assume:
                        assert self.result == add_excepted
                else:
                    with pytest.raises(TypeError):
                        init_calc.add(add_data1, add_data2)
            elif step == 'div':
                if div_data2 == 0:
                    with pytest.raises(ZeroDivisionError):
                        init_calc.div(div_data1, div_data2)
                elif isinstance(div_data1, (int, float)) and isinstance(div_data2, (int, float)):
                    self.result = init_calc.div(div_data1, div_data2)
                    with assume:
                        assert self.result == div_excepted
                else:
                    with pytest.raises(TypeError):
                        init_calc.div(div_data1, div_data2)

    @pytest.mark.parametrize("a,b,excepted", yaml.safe_load(open("../datas/sub_params.yaml")))
    def calc_sub(self, a, b, excepted, init_calc):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            self.result = init_calc.add(a, b)
            with assume:
                assert self.result == excepted
        else:
            with pytest.raises(TypeError):
                init_calc.add(a, b)

    @pytest.mark.parametrize("a,b,excepted", yaml.safe_load(open("../datas/mul_params.yaml")))
    def calc_mul(self, a, b, excepted, init_calc):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            self.result = init_calc.add(a, b)
            with assume:
                assert self.result == excepted
        else:
            with pytest.raises(TypeError):
                init_calc.add(a, b)
