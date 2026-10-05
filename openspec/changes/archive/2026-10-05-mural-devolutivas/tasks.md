# Tasks

## 1. Serviço de dados do mural

- [x] 1.1 Criar `services/devolutivas.py` com a consulta somente leitura da
  tabela `devolutivas`, selecionando os campos definidos, filtrando
  `publicado = true` e ordenando por `data_publicacao` decrescente; verificar
  com teste usando cliente Supabase simulado que a consulta não cria nem altera
  registros.
- [x] 1.2 Aplicar `st.cache_data(ttl=300)` à consulta e propagar falhas para a
  página tratar; verificar que uma segunda chamada dentro do TTL reutiliza o
  resultado cacheado no teste do serviço.

## 2. Página pública e filtros

- [x] 2.1 Substituir o placeholder de `pages/mural.py` pela página pública
  integrada ao shell existente, sem chamar `require_authenticated`; verificar no
  navegador que visitante, aluno, coordenador, avaliador e admin conseguem
  abrir a página e veem somente o conteúdo público.
- [x] 2.2 Renderizar os cards com área, data em `dd/mm/aaaa`, título, demanda e
  resposta usando `st.container(border=True)`; verificar no navegador a ordem
  decrescente e a presença dos rótulos em caixa alta.
- [x] 2.3 Adicionar controles lado a lado para área, ano e busca textual,
  derivando as opções apenas das devolutivas publicadas e aplicando os três
  filtros em conjunto; verificar no navegador filtros combinados e busca sem
  diferenciação de maiúsculas e minúsculas.
- [x] 2.4 Exibir "Nenhuma devolutiva encontrada." para lista vazia e mensagem
  genérica para falha do banco, sem mostrar exceções ou secrets; verificar
  ambos os estados com dados simulados ou banco indisponível.

## 3. Estilo e integração

- [x] 3.1 Adicionar em `assets/style.css` somente os estilos dos filtros, cards,
  faixa da área, metadados e rótulos do mural; verificar no navegador a
  correspondência com o modelo visual e a leitura em viewport móvel.
- [x] 3.2 Executar a validação OpenSpec e o teste mínimo da aplicação,
  verificando que a navegação pública existente continua exibindo "Mural de
  devolutivas", "Relatórios e boletins" e "Contato" e que não foram criadas
  tabelas ou scripts SQL.
