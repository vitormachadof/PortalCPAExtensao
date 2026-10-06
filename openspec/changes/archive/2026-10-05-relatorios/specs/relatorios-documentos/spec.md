# Spec Delta

## Purpose

Disponibilizar relatórios e boletins da CPA em uma biblioteca pública e
autorizada, com filtros claros e downloads protegidos por links temporários.

## ADDED Requirements

### Requirement: Documentos respeitam a visibilidade do perfil no servidor

O sistema SHALL exibir documentos públicos para visitantes e todos os documentos
para usuários autenticados e autorizados, aplicando essa regra na consulta ao
banco antes da renderização.

#### Scenario: Visitante acessa a biblioteca

- **DADO** que a pessoa não está autenticada
- **QUANDO** abre "Relatórios e boletins"
- **ENTÃO** vê somente documentos com `publico = true` e não vê documentos
  restritos nem seus metadados

#### Scenario: Usuário autorizado acessa a biblioteca

- **DADO** que a pessoa está autenticada e autorizada como aluno, coordenador,
  avaliador externo ou admin CPA
- **QUANDO** abre "Relatórios e boletins"
- **ENTÃO** vê documentos públicos e restritos, com a etiqueta "Restrito" nos
  documentos não públicos

#### Scenario: Usuário autenticado sem autorização acessa a biblioteca

- **DADO** que a pessoa está autenticada, mas foi tratada como visitante pelo
  controle de perfis
- **QUANDO** abre "Relatórios e boletins"
- **ENTÃO** vê somente documentos públicos, sem acesso aos documentos restritos

### Requirement: Biblioteca lista e filtra documentos

O sistema SHALL listar documentos por ano decrescente e título, oferecendo
filtros por tipo e ano com opções abrangentes.

#### Scenario: Lista ordenada

- **DADO** que existem documentos de anos e títulos diferentes
- **QUANDO** a biblioteca é carregada
- **ENTÃO** os documentos aparecem do ano mais recente para o mais antigo e,
  dentro do mesmo ano, em ordem de título

#### Scenario: Filtro por tipo e ano

- **DADO** que existem relatórios e boletins de anos diferentes
- **QUANDO** a pessoa seleciona um tipo e um ano
- **ENTÃO** vê somente os documentos que correspondem aos dois filtros

#### Scenario: Nenhum documento corresponde aos filtros

- **DADO** que os filtros selecionados não correspondem a nenhum documento
- **QUANDO** a lista filtrada é renderizada
- **ENTÃO** vê a mensagem "Nenhum documento encontrado."

### Requirement: Documento oferece download protegido

O sistema SHALL exibir título, tipo, ano e a ação "Baixar PDF", gerando o
download por URL assinada do bucket privado com validade de dez minutos.

#### Scenario: Download de PDF

- **DADO** que a pessoa visualiza um documento permitido
- **QUANDO** seleciona "Baixar PDF"
- **ENTÃO** o sistema disponibiliza o PDF por um link temporário válido por
  dez minutos sem tornar público o bucket

#### Scenario: Documento restrito identificado

- **DADO** que um usuário autorizado visualiza um documento com `publico = false`
- **QUANDO** o card é renderizado
- **ENTÃO** o card mostra a etiqueta discreta "Restrito" e mantém o download
  protegido

### Requirement: Falhas de banco ou Storage são tratadas com segurança

O sistema SHALL informar uma mensagem amigável quando a consulta ou o download
falhar, sem revelar exceções, credenciais, caminhos internos ou configurações.

#### Scenario: Falha na consulta de documentos

- **DADO** que o banco está indisponível ou a consulta falha
- **QUANDO** a pessoa abre a biblioteca
- **ENTÃO** vê uma mensagem amigável sem detalhes técnicos ou chaves

#### Scenario: Falha ao gerar link de download

- **DADO** que o Storage não consegue gerar uma URL assinada
- **QUANDO** a pessoa tenta baixar o PDF
- **ENTÃO** vê uma mensagem amigável e o bucket permanece privado
