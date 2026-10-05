# Tasks

## 1. Serviços de acesso e configuração

- [x] 1.1 Criar `services/db.py` com cliente Supabase cacheado e leitura exclusiva dos secrets; verificar por importação que o módulo não contém chaves literais nem cria tabelas.
- [x] 1.2 Criar `services/auth.py` com o estado tipado do usuário, consulta por e-mail em `usuarios`, regra de `ativo` e fallback `@aluno.impacta.edu.br`; verificar os cenários de usuário ativo, inexistente, inativo e aluno por domínio sem inserir registros.
- [x] 1.3 Adicionar as dependências de runtime somente se não estiverem disponíveis e verificar que a aplicação inicia usando o interpretador Python 3.14 do projeto.

## 2. Shell, login e navegação

- [x] 2.1 Atualizar `app.py` para resolver o estado antes de montar `st.navigation` e manter o cabeçalho azul-marinho; verificar no navegador que um visitante vê somente Mural, Relatórios e boletins e Contato.
- [x] 2.2 Adicionar o botão "Entrar com conta Impacta" chamando `st.login()` para visitantes e o cartão "Olá, [nome] · Perfil: [perfil]" com botão "Sair" chamando `st.logout()` para usuários autorizados; verificar o fluxo de ida e volta do login no navegador.
- [x] 2.3 Exibir Início e Dashboards somente para perfis autorizados, preservando as áreas públicas; verificar no navegador a diferença entre sessão visitante e sessão autenticada.
- [x] 2.4 Tratar contas não autorizadas com a mensagem exata "Acesso não autorizado" e estado de visitante, sem exibir tokens ou credenciais; verificar o comportamento com conta inexistente e conta inativa.

## 3. Proteção das páginas

- [x] 3.1 Adicionar uma guarda reutilizável no início das páginas restritas e bloquear visitantes ou perfis sem permissão antes do conteúdo; verificar acesso direto à URL de Início e Dashboards.
- [x] 3.2 Aplicar a guarda às páginas autenticadas sem remover os placeholders existentes; verificar que aluno, coordenador, avaliador e admin conseguem visualizar as áreas autenticadas e que as páginas públicas continuam acessíveis sem login.

## 4. Integração e validação

- [x] 4.1 Executar lint, checagem de sintaxe e testes disponíveis para os arquivos alterados; verificar que não há erros novos e que nenhum SQL ou tabela foi adicionado.
- [x] 4.2 Abrir o portal em modo visitante e autenticado e validar visualmente o shell, menu condicional, cartão, logout, mensagem de acesso e bloqueios conforme RF01, RF02, RF03, RF05, RF06, RNF02 e RNF04.
