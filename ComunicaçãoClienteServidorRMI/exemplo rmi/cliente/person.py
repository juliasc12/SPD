class Person():
    def __init__(self, name):
        self.name = name

    def retrieve(self, warehouse):
        print("O armazem contem: ", warehouse.list())
        item = input("Item a retirar: ")
        if item:
            warehouse.remove(self.name, item)
        print("Armazem Atualizado: ", warehouse.list())

    def deposit(self, warehouse):
        print("O armazem contem: ", warehouse.list())
        item = input("Item a depositar: ")
        if item:
            warehouse.add(self.name, item)
        print("Armazem Atualizado: ", warehouse.list())
