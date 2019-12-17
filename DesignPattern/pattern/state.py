from abc import ABCMeta, abstractmethod


class Context(metaclass=ABCMeta):

    def __init__(self):
        self._state = []
        self._cur_state = None
        self._state_info = 0

    def add_state(self, state):
        if state not in self._state:
            self._state.append(state)

    def change_state(self, state):
        if not state:
            return False
        if not self._cur_state:
            print("初始化为 ", state.get_name())
        else:
            print("由", self._cur_state.get_name(), "变为", state.get_name())

        self._cur_state = state
        self.add_state(state)
        return True

    def get_state(self):
        return self._cur_state

    def _set_state_info(self, state_info):
        self._state_info = state_info
        for state in self._state:
            if state.is_match(state_info):
                self.change_state(state)

    def _get_state_info(self):
        return self._state_info


class State:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def is_match(self, state_info):
        return False

    @abstractmethod
    def behavior(self, context):
        pass


class Water(Context):

    def __init__(self):
        super().__init__()
        self.add_state(SolidState("固态"))
        self.add_state(LiquidState("液态"))
        self.add_state(GasState("气态"))
        self.set_temperature(25)

    def set_temperature(self, temperature):
        self._set_state_info(temperature)

    def get_temperature(self):
        return self._get_state_info()

    def rise_temperature(self, step):
        self.set_temperature(self.get_temperature() + step)

    def reduce_temperature(self, step):
        self.set_temperature(self.get_temperature() - step)

    def behavior(self):
        state = self.get_state()
        if isinstance(state, State):
            state.behavior(self)


def singleton(cls, *args, **kwargs):
    instance = {}

    def _singleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)

        return instance[cls]

    return _singleton


@singleton
class SolidState(State):

    def __init__(self, name):
        super().__init__(name)

    def is_match(self, state_info):
        return state_info < 0

    def behavior(self, context):
        print("硬邦邦", context._get_state_info(), "嘿嘿")


@singleton
class LiquidState(State):

    def __init__(self, name):
        super().__init__(name)

    def is_match(self, state_info):
        return 0 <= state_info < 100

    def behavior(self, context):
        print("上上上善若水", context._get_state_info(), "哗啦呼啦 ")


@singleton
class GasState(State):

    def __init__(self, name):
        super().__init__(name)

    def is_match(self, state_info):
        return state_info >= 100

    def behavior(self, context):
        print("汽汽汽水吗？", context._get_state_info(), "轻飘飘  ")


def test_state():
    water = Water()
    water.behavior()
    water.set_temperature(-4)
    water.behavior()
    water.set_temperature(18)
    water.behavior()
    water.set_temperature(110)
    water.behavior()
