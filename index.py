
palavraTexto = ""
menu = "Menu de contador de caracteres\nOpção 1 para seguir a contagem de caracteres e 0 para encerrar contagem\n"
quantidade = 0
 

print(menu)
 

opcao = int(input())
 

while(opcao != 0):
 
    
    if(opcao == 1 ):  
 
        
        print("Informe a palavra/texto desejada:\n")
        palavraTexto = input()
 
        
        quantidade = len(palavraTexto.replace(" ",""))
 
        
        print(f"A quantidade de caracteres presentes na palvra/texto é ..: {quantidade}")
 
    
    else:
      print("Opção invalida favor selecione uma das opções apresentadas no menu abaixo:\n")
 
    
    print(menu)
    opcao = int(input())

print("Encerrando aplicação de contagem de caracteres")