import os

restaurantes = [{'nome': 'Sabor de Minas','categoria': 'Comida Brasileira', 'ativo': False},
                {'nome': 'Sushi do Japa', 'categoria': 'Comida Japonesa', 'ativo': True},
                {'nome': 'Hamburgueria do Beco', 'categoria': 'Fast Food', 'ativo': True}
]

def exibir_nome_do_programa ():
    print("""   
        Ｓａｂｏｒ Ｅｘｐｒｅｓｓ    
    """
    )

def exibir_opcoes ():
    print('1 - Cadastrar restaurante' )
    print('2 - Listar restaurantes' )
    print('3 - Alternar estado do restaurante' )
    print('4 - Sair\n' )

def cadastrar_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante
    Inputs:
    - Nome do restaurante
    - Categoria
    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes
    '''
    exibir_subtitulo ('Cadastro de novos restaurantes')

    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = (input(f'Digite a categoria do restaurante {nome_do_restaurante}: '))
    dados_do_restaurante = ({'nome':nome_do_restaurante, 'categoria': categoria, 'ativo':False})
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')            
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Essa função é responsável por listar os restaurantes cadastrados'''
    exibir_subtitulo("Listando os restaurantes\n")

    print(f'{'  Nome do restaurante'.ljust(24)} │ {'Categoria'.ljust(23)}│ Status')
    
    for restaurante in restaurantes:
        nome_do_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_do_restaurante.ljust(22)} │ {categoria.ljust(22)} │ {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    '''Essa função é responsável por alternar o estado do restaurante
    Input 
    - Nome do restaurante
    '''
    exibir_subtitulo('Alternar estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            print(mensagem)
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' \
                if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    
    voltar_ao_menu_principal()

def voltar_ao_menu_principal():    
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def finalizar_app():
    os.system('cls')
    print('Finalizando o app')

def exibir_subtitulo (texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_restaurante()

        elif opcao_escolhida == 2:
            listar_restaurantes()

        elif opcao_escolhida == 3:
            alternar_estado_restaurante()

        elif opcao_escolhida == 4:
            finalizar_app()

        else:
            opcao_invalida()
    except:
        opcao_invalida()

def opcao_invalida():
   print('Opção inválida!')
   voltar_ao_menu_principal()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__': 
    main()