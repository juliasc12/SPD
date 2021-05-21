import Pyro4
#from servidor import Servidor

s = Pyro4.Proxy("PYRONAME:tarefa5")
msg = input("Mensagem a ser lida: ")
nome = input("Nome do audio: ")
s.audio(msg, nome)
