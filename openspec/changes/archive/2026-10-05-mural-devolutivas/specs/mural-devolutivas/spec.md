# Spec Delta

## Purpose

Oferecer um mural público para que a comunidade acadêmica consulte as
devolutivas publicadas pelas áreas da CPA, com organização e filtros simples.

## ADDED Requirements

### Requirement: Mural público exibe apenas devolutivas publicadas

O sistema SHALL permitir que qualquer visitante e qualquer perfil autenticado
consulte o mural sem login adicional, mostrando somente registros marcados como
publicados e ordenados pela data de publicação mais recente.

#### Scenario: Visitante consulta o mural

- **DADO** que a pessoa acessa o portal sem estar autenticada
- **QUANDO** abre o item "Mural de devolutivas"
- **ENTÃO** vê as devolutivas publicadas, sem ver registros não publicados ou
  áreas restritas de aluno, coordenador, avaliador ou admin CPA

#### Scenario: Perfil autenticado consulta o mural

- **DADO** que a pessoa está autenticada como aluno, coordenador, avaliador
  externo ou admin CPA
- **QUANDO** abre o item "Mural de devolutivas"
- **ENTÃO** vê o mesmo conteúdo público do visitante, sem receber dados
  adicionais por causa do perfil

#### Scenario: Publicações são ordenadas

- **DADO** que existem duas ou mais devolutivas publicadas com datas distintas
- **QUANDO** o mural é carregado
- **ENTÃO** a devolutiva com a data mais recente aparece antes das demais

### Requirement: Cada devolutiva apresenta seu conteúdo essencial

O sistema SHALL apresentar cada devolutiva em um card com área destacada, data
formatada como `dd/mm/aaaa`, título, demanda e resposta da área.

#### Scenario: Card de devolutiva publicado

- **DADO** que existe uma devolutiva publicada com todos os campos de conteúdo
- **QUANDO** a pessoa visualiza o mural
- **ENTÃO** vê a área em destaque, o texto "Publicado em dd/mm/aaaa", o título,
  os rótulos "DEMANDA DA PESQUISA" e "RESPOSTA DA ÁREA" e seus respectivos
  textos

### Requirement: Filtros reduzem a lista pública

O sistema SHALL oferecer filtros por área, ano de publicação e palavra-chave
pesquisada no título, na demanda ou na resposta.

#### Scenario: Filtragem por área e ano

- **DADO** que existem devolutivas publicadas de áreas ou anos diferentes
- **QUANDO** a pessoa seleciona uma área e um ano
- **ENTÃO** o mural mostra somente as devolutivas que correspondem aos dois
  filtros selecionados

#### Scenario: Busca por palavra-chave

- **DADO** que existem devolutivas publicadas com termos diferentes
- **QUANDO** a pessoa informa uma palavra-chave
- **ENTÃO** o mural mostra as devolutivas cujo título, demanda ou resposta
  contenha o termo, sem diferenciar maiúsculas de minúsculas

#### Scenario: Nenhum resultado após filtro

- **DADO** que os filtros selecionados não correspondem a nenhuma devolutiva
- **QUANDO** a lista filtrada é renderizada
- **ENTÃO** a pessoa vê a mensagem "Nenhuma devolutiva encontrada."

### Requirement: Falhas de consulta não expõem detalhes técnicos

O sistema SHALL informar uma mensagem amigável quando não conseguir consultar
as devolutivas, sem exibir detalhes da exceção, credenciais ou configuração.

#### Scenario: Banco indisponível

- **DADO** que a consulta ao banco falha
- **QUANDO** a pessoa abre ou atualiza o mural
- **ENTÃO** vê uma mensagem amigável de indisponibilidade e nenhum detalhe
  técnico ou chave é exibido
