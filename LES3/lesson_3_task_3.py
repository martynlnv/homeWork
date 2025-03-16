from address import Address
from mailing import Mailing

to_address = Address("123432", "Псков", "Майская", "2", "3")
from_address = Address("212876", "Волгоград", "Первая", "65", "9")
mailing = Mailing(to_address, from_address, 212, 65111122113421)


print(mailing)