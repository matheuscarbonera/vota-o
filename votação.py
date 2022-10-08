ficha = []
num = []
resultado = []


print('#'*40)
print("       Votação CIPA Tabajara Ltda")
print('#'*40)

def menu():
    while True:

        print('#'*40)
        print('\n1 - Cadastrar candidato')
        print('2 - Lista de candidatos')
        print('3 - Votar')
        print('4 - Resultado')
        print('\n')
        print('Para encerrar precione ENTER')
        

        x=input()

        if x=='1':
            cadastro()
                
        if x=='2':
            lista()


        if x=='3':
            votacao()

        if x=='4':
            apuracao()

        if x=='':
            print("FIM DO PROGRAMA!")
            break

def cadastro():
    
            print('#'*40)
            print('CADASTRO DE CANDIDATO')
            print('#'*40)

            while True:
                nome=str(input('Nome: '))
                num=int(input('Código: '))
                voto=int(0)
                ficha.append([nome,num,voto])
                resp=str(input("Quer continuar? Se não pressione ENTER!"))
                if resp in '':
                    break
            
def lista():
    
            print('#'*40)
            print('LISTA DE CANDIDATOS')
            print('#'*40,'\n')
            #print(ficha)
            print(f'{"Nome":<16}{"Número":5}')
            for i, a in enumerate(ficha):
                print(f'{a[0]:<16}{a[1]:5}')
            menu()

def votacao():
    
            print('#'*40)
            print('VOTAÇÃO')
            print('#'*40)

            print('Digite seu voto!')
            voto=int(input())
            while True:
                for i in range(0,len(ficha),1):

                    if ficha[i][1] == voto:
                        ficha[i][2]+=1
                        print(ficha)
                        menu()
                    
                    if ficha[i][1] != voto:
                        print('\n')
                        print("#"*40)
                        print('CANDIDATO NÃO CADASTRADO!')
                        print("#"*40)
                        print('\n')
                        menu()                
                    
                    
                    if voto=='':
                        menu()
                print('Digite seu voto!')
                voto=int(input())              
            
def apuracao():
    
            print('#'*40)
            print('RESULTADO')
            print('#'*40)
            print(resultado)

menu()