# Tasks

## 1. Serviço de documentos

- [x] 1.1 Criar `services/documentos.py` com consulta somente leitura dos
  campos de `documentos`, aplicando `publico = true` no servidor quando o
  acesso não for autorizado e retornando todos os documentos para usuários
  autorizados; verificar com cliente Supabase simulado que a consulta do
  visitante contém o filtro e não expõe registros restritos.
- [x] 1.2 Aplicar `st.cache_data(ttl=300)` à listagem, recebendo a condição de
  acesso como argumento do cache e ordenando por ano decrescente e título;
  verificar com teste ou inspeção que chamadas com permissões diferentes não
  compartilham resultados indevidos.
- [x] 1.3 Implementar a geração de signed URL no bucket privado `documentos`
  com validade de 600 segundos, sem cachear o link; verificar com cliente
  Storage simulado o bucket, o caminho e o prazo enviados, sem tornar o bucket
  público.

## 2. Página pública de relatórios e filtros

- [x] 2.1 Substituir o placeholder de `pages/relatorios.py`, obtendo o
  `UserState` existente e carregando a lista adequada para visitante,
  autenticado sem autorização e usuário autorizado; verificar no navegador que
  todos acessam a página e que somente o perfil autorizado vê documentos
  restritos.
- [x] 2.2 Adicionar filtros lado a lado para tipo e ano, com as opções "Todos",
  "Relatório", "Boletim" e "Todos os anos" mais os anos existentes; verificar
  no navegador que os filtros são combinados e preservam a ordenação.
- [x] 2.3 Renderizar cada documento em `st.container(border=True)` com título,
  tipo, ano, etiqueta "Restrito" quando aplicável e botão "Baixar PDF";
  verificar no navegador a correspondência com o modelo visual e o link
  temporário do PDF.
- [x] 2.4 Exibir "Nenhum documento encontrado." quando a lista filtrada estiver
  vazia e mensagens genéricas para falha do banco ou do Storage, sem revelar
  exceções, caminhos ou secrets; verificar esses estados com dependências
  simuladas.

## 3. Estilo e integração

- [x] 3.1 Adicionar somente em `assets/style.css` os estilos dos filtros,
  cards, etiquetas e ação de download, mantendo a paleta do Portal CPA;
  verificar no navegador a leitura em desktop e viewport móvel.
- [x] 3.2 Executar validação OpenSpec, compilação Python e smoke test do
  Streamlit, verificando também que a navegação pública existente continua
  apresentando "Relatórios e boletins" e que nenhum SQL, bucket ou tabela foi
  criado pelo código.
