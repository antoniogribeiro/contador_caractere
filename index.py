#Declaração de variáveis base para aplicação
palavraTexto = ""
menu = "Menu de contador de caracteres\nOpção 1 para seguir a contagem de caracteres e 0 para encerrar contagem\n"
quantidade = 0
 
#Exibe o menu para o usuário
print(menu)
 
#Captura o que foi informado pelo usuário
opcao = int(input())
 
#Definindo condição de saída do loop
while(opcao != 0):
 
    #Caso a opção válida seja informada então realizará os passos normalmente
    if(opcao == 1 ):  
 
        #Pede o texto e o captura logo em seguida
        print("Informe a palavra/texto desejada:\n")
        palavraTexto = input()
 
        #Captura a quantidade de caracteres das palavras existentes no texto
        quantidade = len(palavraTexto.replace(" ",""))
 
        #Exibe em tela o resultado final da aplicação
        print(f"A quantidade de caracteres presentes na palvra/texto é ..: {quantidade}")
 
    #Excessões serão consideradas como erro e então deverá ser selecionada a opção de acordo com o menu
    else:
      print("Opção invalida favor selecione uma das opções apresentadas no menu abaixo:\n")
 
    #Exibe novamente as opções de menu para definir se vamso encerrar ou seguir na aplicação
    print(menu)
    opcao = int(input())
 
#finalizando ...
print("Encerrando aplicação de contagem de caracteres")