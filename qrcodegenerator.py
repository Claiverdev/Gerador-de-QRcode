#Biblioteca qrcode
import qrcode # type: ignore

#aqui é a entrada do dado que se deseja gerar, pode ser um texto ou uma URL
data = "oi"

#Gere uma image qrcode com esse dado
img =  qrcode.make(data)

#Diretório para onde será encaminhado o qrcode
img.save("c:/Users/Revialc/Desktop/qrcode.png")
