from abc import ABC, abstractmethod


class Transport(ABC):

	def __init__(self, ttype: str, tmodel: str, tweight: float):
		self._ttype = ttype
		self._tmodel = tmodel
		self._tweight = tweight

	def __str__(self) -> str:
		return f'{self._ttype} - {self._tmodel} / {self._tweight} tonn'

	@abstractmethod
	def deliver(self):
		pass


class Truck(Transport):

	def __init__(self, ttype: str, tmodel: str, tweight: float, height: float):
		super().__init__(ttype, tmodel, tweight)
		self._height = height

	def __str__(self) -> str:
		return super().__str__() + f'; height = {self._height} m'

	def deliver(self):
		print('Перевозка по шоссейным дорогам в пределах Европы')


class Ship(Transport):

	def __init__(self, ttype: str, tmodel: str, tweight: float, draft: float):
		super().__init__(ttype, tmodel, tweight)
		self._draft = draft

	def __str__(self) -> str:
		return super().__str__() + f'; draft = {self._draft} m'

	def deliver(self):
		print('Перевозка по Днепру и судоходным притокам')


class AirPlane(Transport):

	def __init__(self, ttype: str, tmodel: str, tweight: float, distance: float):
		super().__init__(ttype, tmodel, tweight)
		self._distance = distance

	def __str__(self) -> str:
		return super().__str__() + f'; distance = {self._distance} km'

	def deliver(self):
		print('Авиаперевозки по региональным авиалиниям')
