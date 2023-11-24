Nome: Fernando Paparelli Aracena RM: 551022

Nome: Filipe de Oliveira Mendes RM: 98959

Nome: Miron Gonçalves Martins RM: 551801

Nome: Paulo Henrique de Andrade Juniro RM: 99714

Nome: Vinícius Pedro de Souza RM: 550907

O programa foi feito para manipular(criar,atualizar,checar e eliminar dados) de nosso banco de dados.
A principal função desse programa é criar um login de usuario e atravez dele receber doações para o tratamento
de vitimas da minigite. Assim como, possibilitar que o usuario possa ver um ranking com os maiores doadores 
de nossa aplicação.

Programa "menu.py"

Conta com funções que criar o menus que auxiliaram na interatividade do usuario principal em main.py, sendo esses:
A partir desse menus o usuario poderá decidir suas ações, sendo essas funções:

"menu()": que servirá como menu de navegação pricipal do programa, por onde o usuario poderá decidir suas ações, sendo elas:

"1 gostaria conferir o ranking dos maiores doadores", onde o usuarario poderá conferir uma lista de doadores, mostrará aqueles realizaram 
as maiores doações.
"2 gostaria de realizar uma doação", onde o usuario podera realizar uma doação para a causa da luta contra a meningite
"3 gostaria de alterar uma informação", onde o cliente poderá arterar as informações  de seu cadastro, sendo que as unicas informações
alteraveis serão, seu login, sua senha, seu nome e seu estado civil.
"4 gostaria de consultar meus dados", onde o cliente podará ver seus dados pessoais e os dados de todos os seus veiculos, assim como
os dados de suas chamadas de modal CONTATO QUE ELE TENHA O CODIGO DA CHAMADA!!!
"5 - gostaria de deletar minhas informações", onde o usuario poderá apagar sua conta completamente e encerrar o programa,
sendo que não será possivel utiliza-lo sem um cadastro.
"6 - sair", finaliza o programa

"seuVeiculo()", nostrará o menu pelo qual a usuarario poderá escolha qual informação de seu cadastro gostaria de alterar

"tenhoCadastro()", será o primeiro menu visto pelo usuario nesse programa, não será possivel ao usuario ultizar esse
programa sem um login, logo atravez dele o usuario irá dizer se deseja criar uma nova conta ou se deseja usar uma conta que ele
já possua.

programa "cadastra.py"

Conta três funções
A função "cadastraDoação", pedirá informações ao usuario e criará um dicionario cujas informações serão utizadas para preencher uma
linha na tabela "t_rs_doacao" de nosso banco de dados.
A função "cadastraCliente" pedirá informações sobre o usuario para em seguida criar um dicionario cujas impormações serão
ultizadas para preencher uma linha na tabela tabela "t_ts_usuario" de nosso banco de dados.
A função "seuCadastro" será ulizada para criar um dicionario a partir de uma tupla criada a partir das informações de nosso banco de dados,
que será especificamente utilizado fazer alterações nos dados do usuario que esta utilizando o programa no moemento presente

programa "main.py"

O programa central do nosso projeto, para seu funcinamento importações serão feitas por todos os outros programas.

A varialvel "escolha" é referente as opçoes em "menu.py" enquanto a varialvel opcao será mais usada para navenar nos menus mais 
adentro do programa. 

O usuario só poderá utilizar nosso programa se tirar uma conta cadastrada, sendo assim ele terá a escolha de criar uma conta 
antes de começar a navega-lo e caso decida deletar esse conta o programa altomaticamente se encerrará

caso o usuario já tenha uma conta ele poderá utilizar seu login e senha, por ele cadastrado para entrar em nosso programa
por tanto, O USUARIO DEVE TER EM MENTE LOGIN E SENHA QUE SERÃO FACILMENTE LEMBRADOS, pois caso um deles se informados de maneira incorreta
O USUARIO NÃO SERÁ PERMITIDO NAVEGAR EM NOSSA APLICAÇÃO

programa "rankingAPI.py": gerará um json que mostrará o ranking de todos doadores de nosso banco de dados,
sendo sendo os maiores estarão nas primeiras posições

pasta "ressources"

pasta contendo os programas que contem as funcões que permitiram a manipulação dos dados no banco de dados

programa "cliente_resource.py"

O programa conta os recurssos que permitiram a manipulação dos dados da tabela "t_vs_usuario".
função "create": recebera um dicionario, e importará suas informações para a tabela "t_vs_usuario".
função "find_one_by_SENHA": irá receber um login e senha do usuario 
banco de dados, a função ira retornar um tupla correspondente a linha do BD em o login e senha fazem parte
função "find_one_by_id": o id correspondente ao numero da colona "id_usuario" do BD e retornar um tupla 
correspondente a linha da tabela em esse id faz parte
função "update": deve rebeber um codigo que deve pertencer ao nosso BD e um dicionario com novas imformações que substituiram
as anteriores da linha correspondente a linha em que o codigo se encontra.
função "delete": irá receber um login e senha do usuario  e irá deletar as informações da linha em que esse login e senha se 
encontram

programa "doacao_resource.py"

O programa conta os recursso que permitira criação de uma nova linhas de informação em nosso banco de dados.
função "create": recebera um dicionario, e importará suas informações para a tabela "t_vs_doacao".


programa "ranking_resource.py"

O programa conta os recurssos que permitiram a manipulação dos dados da tabela "t_porto_veiculo_carga".
função "find_all_ranking": ira usar o 'SELECT' com informação de duas tabelas de nosso banco de dados
para gerar uma lista de tuplas que conterá todas as informações dos nomes dos dos login dos usuarios que fizeram
uma doacao em algum momento em nosso banco de dados, e a soma total dessas devoações (se ouverem mais de uma).





   

 


