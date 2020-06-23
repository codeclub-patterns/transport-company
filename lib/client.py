from lib.creators import *


class Client(object):

    def __init__(self, abs_manager: Manager):
        self._abs_manager = abs_manager

    def demo(self) -> None:
        self._abs_manager.delivery_order()
