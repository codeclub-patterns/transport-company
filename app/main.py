from lib.client import *
from lib.creators import *


if __name__ == '__main__':

    client1 = Client(RoadManager('Киев', 'Жмеринка', 3, 'Проминвест'))
    client2 = Client(RiverManager('Черкассы', 'Одесса', 12, 'ЧеркассХлеб'))
    client3 = Client(AirManager('Херсон', 'Харьков', 1, 'БахчаСбыт'))

    clients = [client1, client2, client3]

    for c in clients:
        c.demo()
