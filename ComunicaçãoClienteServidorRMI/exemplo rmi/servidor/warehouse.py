import Pyro4

@Pyro4.expose
class Warehouse:
    def __init__(self):
        self.contents = ["maça","uva","laranja","banana"]

    def list(self):
        return self.contents

    def remove(self, name, item):
        self.contents.remove(item)
        print("---- "+name+" retirou "+item+" -----\n")

    def add(self, name, item):
        self.contents.append(item)
        print("---- "+name+" armazenou "+item+" -----\n")

def main():
    Pyro4.Daemon.serveSimple(
        {
            Warehouse: "warehouse"
        }
    )

#if __name__ == "__main__":
main()
