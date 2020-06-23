from abc import ABC, abstractmethod
from lib.products import *


class Manager(ABC):

	def __init__(self, point: str, dest: str, term: float, client: str):
		self._point = point
		self._dest = dest
		self._term = term
		self._client = client

	def delivery_order(self):
		print(f'Принят заказ от {self._client} на перевозку из {self._point} в {self._dest}; срок - {self._term} дней')
		print(f'Транспортная единица - {self.create_transport()}')

	@abstractmethod
	def create_transport(self):
		pass


class RoadManager(Manager):

	def __init__(self, point: str, dest: str, term: float, client: str):
		super().__init__(point, dest, term, client)

	def create_transport(self):
		return Truck('Трейлер', 'GM', 25, 4.5)


class RiverManager(Manager):

	def __init__(self, point: str, dest: str, term: float, client: str):
		super().__init__(point, dest, term, client)

	def create_transport(self):
		return Ship('Сухогруз', 'Днепр', 50000, 6.5)


class AirManager(Manager):

	def __init__(self, point: str, dest: str, term: float, client: str):
		super().__init__(point, dest, term, client)

	def create_transport(self):
		return AirPlane('Транспортник', 'АН-35', 5, 1000)
