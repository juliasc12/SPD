import subprocess

print("Selecionamos o top 5 da Netflix! Escolha qual você quer assistir")
escolha = str(input("1 - Enola Holmes\n 2 - Emily em Paris\n 3 - O dilema das redes 2\n 4 - Ratched\n 5 - Grey's Anatomy\n Escolha: "))

filme=0

if(escolha == "1"):
    filme = str(81277950)
elif(escolha == "2"):
    filme = str(81037371)
elif(escolha == "3"):
    filme = str(81254224)
elif(escolha == "4"):
    filme = str(80213573)
else:
    filme = str(70158900)

navegador ="C:\Program Files\Google\Chrome\Application\chrome.exe"
assistir = "https://www.netflix.com/watch/"+str(filme)+""
p = subprocess.Popen([navegador,assistir])

p.communicate()
