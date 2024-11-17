from qrcode import QRCode

def QrCode(link, frente="black", fundo="white"):
    """-> A função QrCode gera um qrcode com os dados informados.\n
    param link: Item que ficará contido no qrcode gerado.\n
    param frente: Cor de frente (Inglês)\n
    param fundo: Cor de fundo (Inglês)"""
    
    # Define o tamanho da imagem gerada, o tamanho das bordas.
    qr = QRCode(version=1,
                box_size=20, 
                border=3) 

    # Adiciona o que o usuário digitou ao qrcode, por exemplo um link.
    qr.add_data(link)

    # Defini as cores de fundo e frente do Qrcode
    qr.make(fit=True)
    gerado = qr.make_image(fill_color =f"{frente}", back_color =f"{fundo}")
    
    # Programa salva o Qrcode gerado na pasta em que o programa está sendo executado.
    gerado.save("qrcode.png")
    return print("\033[1;32m" + "\nQrcode gerado com sucesso!")

dado = input(">>> Digite o link do QrCode: ")
frent = input(">>> Digite a cor da frente do QrCode(Em inglês): ")
fund = input(">>> Digite a cor de fundo do QrCode(Em inglês): ")

QrCode(dado, frent, fund)
