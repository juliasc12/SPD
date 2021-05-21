import Pyro4
from person import Person
#from warehouse import Warehouse
#w = Pyro4.Proxy("PYRO:Pyro.NameServer@localhost:9090")

w = Pyro4.Proxy("PYRONAME:warehouse")
julia = Person('julia')
julia.deposit(w)
julia.retrieve(w)
