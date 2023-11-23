Nome: Fernando Paparelli Aracena RM: 551022

Nome: Filipe de Oliveira Mendes RM: 98959

Nome: Miron Gonçalves Martins RM: 551801

Nome: Paulo Henrique de Andrade Juniro RM: 99714

Nome: Vinícius Pedro de Souza RM: 550907

O programa foi feito para manipular(criar,atualizar,checar e eliminar dados) de nosso banco de dados.
o program irá criar diverços dicionarios, cujas informações neles colocas serão importadas para suas 
respectivas tabelas atraves das funções nos arquivos dentro da pasta ressources para nosso banco de dados.
o programa tambem conta com os arquivo auxilio.py que contará com dicionarios contendo valores equivalentes aos valores 
de tabelas em nosso banco de dados que foram feita para a manipulação do cliente, mas seus dados serviram
para constriuir um "resumo de chamada" ao final de uma chamada realizada, o arquivo codigo gerará um codigo numerico de oito 
digitos, o qual o cliente ultilizará para verificar ou manipular seus dados. main.py será o programa principal do cliente, será
atrave´z dele que o cliente interatividade com o programa total.

Programa "menu.py"

Conta com a função que criará o menu principal em main.py. A partir desse menu o usurio poderá decidir suas ações
sendo elas: " 1 Criar cadastro", onde o usuarario deverá colocar suas informações e as informações de seu veiculo para serem
quardadas no dicinario "cliente", que será quardado na lista "usuario". vale resaltar que o cliente tambem deverá colocar 
as informações de seu veiculo logo em seguida. Os veiculos estarão em uma lista "veiculos" no artributo "veiculos" do dicionario
cliente. Cada veiculo corresponde a um dicionario "V"
"2 cadastrar outro veiculo", onde o cliente podera adicionar outro veiculo (dicionario) à sua lista "veiculos"
"3 alterar informações", onde o cliente poderá arterar as informações apenas de seu veiculo, sendo as informações
de cliente são em grande parte imutaveis (id, cpf), não achamos que haveria necessidade de implementar um opção
para alterá-las
"4 consutar dados", onde o cliente podará ver seus dados pessoais e os dados de todos os seus veiculos, assim como
os dados de suas chamadas de modal CONTATO QUE ELE TENHA O CODIGO DA CHAMADA!!!
"5 - solicitação de modal", onde o cliente informará seu id e a placa do veiculo nessecitado, alem se esta carregando
alguma carga externa e qual dos problema mostrados no menu melhor definem seu situação, para poder chamar o auxilio mais
indicado. Pois as informações forem preenchidas o cliente receberá um codigo de chamada e escolherá se quiser ver o resumo 
de chamada
"6 - deletar impormações", onde o cliente deverá passar seu id para ou apagar sua conta completamente ou apenas apagar um 
veiculo de sua conta
"7 - sair", finaliza o programa

e a função seuVeiculo, que mostrará ao cliente atributos de veiculo correspondente aos dados de veiculos inseridos em nosso banco
de dados

Programa "codigo.py"

Conta apenas com uma função que criará um codigo de 8 digitos que servirá como codigo do cliente, codigo de chamada de modal e codigo de
carga de veiculo

Programa "auxilio.py"

Conta com sete funções que auxiliaram na indetentifaicação de um problema durante uma chamada de modal e na escolha de uma ajuda
apropriada, alem de criar uma lista com o resumo dos dados dessa chamada.
A função "auxilio", conta com o tipo de ajuda que será madanda para o cliente.
A função "problema", conta com um dicionarios de atributos numerados, cujos valores são referentes a tipos de problemas genricos que o cliente
pode estar tendo
A função "expecificacao", conta com valores numerados onde para onde o cliente poderá afunilar ainda mais o problema que o cliente
pode estar tendo.
A função "veiculoTotal", pega as informações do veiculo (peso,altura,comprimento,largura) e as junta com as informações de uma carga externa(se ouver)
de modo que os pesos e comprimetos serão somados e a maior altura e largura serão colocadas no dicionario veiculoTotal e essas informações
serão usadas para a excolha do melhor modal para essa chamada
A função "escolhaModal", usara as informações de pesoTotal da função veiculoTotal para selecionar o modal generico mais apropriado para o tipo
de veiculo necessitado
A função "resumoChamada", ela recebe as informações de problemas e de veiculo e as coloca no dicionerio resumoChamada, para em seguida
a colocalo na lista "chamada"
A função "dbResumoChamada" mostrará as informação pertinentes a chamada feita pela cliente utilizando dados de diversas tabelas de nosso
banco de dados, e posicionando essas informações em forma de um texto que resume todas as informações

programa "cadastra.py"

Conta quatro funções
A função "cadastraCliente" pedirá informações ao usuario e criará um dicionario cujas impormações serão ultizadas para preencher uma
linha na tabela "t_porto_cliente" de nosso banco de dados.
A função "cadastraV" pedirá informações sobre o veiculo do cliente para em seguida criar um dicionario cujas impormações serão
ultizadas para preencher uma linha na tabela tabela "t_porto_veiculo_cliente" de nosso banco de dados.
A função "carga", permitira ao usuario inserir as informações da carga de seu veiculo(se ouver) em um dicioanario cujas impormações
 serão ultizadas para preencher uma linha na tabela "t_porto_veiculo_carga" de nosso banco de dados. 
A função "seuVeiculo" será ulizada para criar um dicionario que será especificamente utilizado fazer alterações nos dados de um
veiculo em nosso banco de dados

programa "main.py"

O programa central do nosso projeto, para seu funcinamento importações serão feitas por todos os outros programas.

A varialvel "escolha" é referente as opçoes em "menu.py" enquanto a varialvel opcao será mais usada para navenar nos menus mais 
adentro do programa. 

É indicado que o usuario crie uma conta na opcao "1 - gostaria de realizar meu cadastro" antes de começar qualquer operação ou
pois cada opção no menu principal irá pedir por codigo de usuario valido ou uma placa de carro existente em nosso banco de dados
poderá cair num looping que só será solucionado com a reinicilização do programa.

Lembrando de SEMPRE GUARDAR O CÓDIGO DADO AO USOARIO AO FINAL DA REALIZAÇÃO DE SEU CADASTRO, ASSIM COMO A PLACA CADASTRADA DE SEU
VEICULO e CODIGO DE CHAMADA AO FINAL DE UMA CHAMADA pois é com esses codigos que o usoario poderá usar as funcionalidades desse programa

Vale resaltar que toda vez que um código for digitado de forma errada uma lista de opções aparecerá na tela
e o usoario poderá tentar digitar o código denovo

pasta "ressources"

pasta contendo os programas que contem as funcões que permitiram a manipulação dos dados no banco de dados

programa "cliente_resource.py"

O programa conta os recurssos que permitiram a manipulação dos dados da tabela "t_porto_cliente".
função "create": recebera um dicionario, e importará suas informações para a tabela "t_porto_cliente".
função "find_all": ira gerar uma lista de tupla que conterá todas as informações da tabela "t_porto_cliente"
função "find_one_by_codigo": irá receber um codigo numero providenciado pelo nosso programa e se ele estiver em nosso
banco de dados, a função ira retornar um tupla correspondente a linha do BD em o codigo faz parte
função "find_one_by_id": o id correspondente ao numero da colona "id_cliente" do BD e retornar um tupla 
correspondente a linha da tabela em esse id faz parte
função "update": deve rebeber um codigo que deve pertencer ao nosso BD e um dicionario com novas imformações que substituiram
as anteriores da linha correspondente a linha em que o codigo se encontra.
função "delete": irá receber um codigo existente em nossa tabela, e irá deletar as informações da linha em que esse codigo se 
encontra 

programa "veiculo_resource.py"

O programa conta os recurssos que permitiram a manipulação dos dados da tabela "t_porto_cliente_veiculo".
função "create": recebera um dicionario, e importará suas informações para a tabela "t_porto_cliente_veiculo".
função "find_all": ira gerar uma lista de tupla que conterá todas as informações da tabela "t_porto_cliente_veiculo"
função "find_one_by_placa": irá receber o codigo da placa do carro cadastrada pelo cliente e se ela estiver em nosso
banco de dados, a função ira retornar um tupla correspondente a linha do BD em em que a placa
função "find_one_by_idVeiculo": o id correspondente ao numero da colona "id_cliente_veiculo" do BD e retornar um tupla 
correspondente a linha da tabela em esse id faz parte
função "update": deve rebeber o codigo da placa de carro que deve pertencer ao nosso BD e um dicionario com novas 
informações que substituiram as anteriores da linha correspondente a linha em que o codigo se encontra.
função "delete": irá receber o codigo de placa de carro existente em nossa tabela, e irá deletar as informações da 
linha em que essa placa se encontra.

programa "carga_resource.py"

O programa conta os recurssos que permitiram a manipulação dos dados da tabela "t_porto_veiculo_carga".
função "create": recebera um dicionario, e importará suas informações para a tabela "t_porto_veiculo_carga".
função "find_all": ira gerar uma lista de tupla que conterá todas as informações da tabela "t_porto_veiculo_carga"
função "find_one_by_placa": o codigo da placa do carro cadastrada pelo cliente, que corresponde a carga cadastrada 
e se ela estiver em nosso banco de dados, a função ira retornar um tupla correspondente a linha do BD em em que a placa
função "find_one_by_id": irá receber o id correspondente ao numero da colona "t_porto_veiculo_carga" do BD e retornar um tupla 
correspondente a linha da tabela em esse id faz parte
função find_one_by_codigo: irá receber um codigo numerico providenciado pelo nosso programa e se ele estiver em nosso
banco de dados, a função ira retornar um tupla correspondente a linha do BD em o codigo faz parte

OBS:como colocamos sequences em nosso banco de dados e o mesmo carros pode usar cargas diferentes, precisamos de uma maneira
imediata para chamar as impormações de um carga especifica, por isso nosso programa ira atribuir um codigo para cada 
carga cadastrada
 
função "update": deve rebeber o codigo da placa de carro correspondente a carga cadastrada e que deve pertencer 
ao nosso BD e um dicionario com novas informações que substituiram as anteriores da linha correspondente a 
linha em que o codigo se encontra.
função "delete": irá receber o codigo de placa de carro correspondente a carga cadastrada em nossa tabela,
e irá deletar as informações da linha em que essa placa se encontra.

programa "auxilio_resourse.py"

O programa conta os recurssos que permitiram a consulta das informações contidas nas tabelas "t_porto_problema", 
"t_porto_especificacao" e "t_porto_auxilio.
função "find_all_problemas": ira gerar uma lista de tupla que conterá todas as informações da tabela "t_porto_veiculo_carga"
função "find_one_by_id_problema": ira rebecer o id de uma linha na tabela "t_porto_veiculo_carga" e devolver uma tupla correspondente
a essa linha
função "find_all_especificacao": ira gerar uma lista de tupla que conterá todas as informações da tabela "t_porto_especificacao"
função "find_one_by_id_especificacao": ira rebecer o id de uma linha na tabela "t_porto_especificacao" e devolver uma tupla correspondente
a essa linha
função "find_all_auxilio": ira gerar uma lista de tupla que conterá todas as informações da tabela "t_porto_auxilio"
função "find_one_by_id_auxilio": ira rebecer o id de uma linha na tabela "t_porto_auxilio" e devolver uma tupla correspondente
a essa linha

programa "chamada_ressource.py"

O programa conta os recurssos que permitiram a criação, consulta e deleção de dados da tabela "t_porto_chamada".
função "create": recebera um dicionario, e importará suas informações para a tabela "t_porto_chamada".
função "find_all": ira gerar uma lista de tupla que conterá todas as informações da tabela "t_porto_cliente_veiculo"
função "find_one_by_codigo": irá receber um codigo numerico providenciado pelo nosso programa e se ele estiver em nosso
banco de dados, a função ira retornar um tupla correspondente a linha do BD em o codigo faz parte
função "find_one_by_id": irá receber o id correspondente ao numero da coluna "id_chamada" do BD e retornar uma tupla 
correspondente a linha da tabela em esse id faz parte
função "deletePorIdVeiculo": irá receber id correspondente a coluna id_veiculo e irá deletar as informações da linha
correspondente a esse id.
função "deletePorIdCliente": irá receber id correspondente a coluna id_cliente e irá deletar as informações da linha
correspondente a esse id.



 



   

 


