# Proposal

## Why

O Portal CPA precisa identificar usuários da Faculdade Impacta e aplicar as regras de acesso previstas antes que as páginas deixem de ser apenas placeholders. Esta mudança habilita o login federado com Google e uma autorização centralizada por perfil, mantendo visitantes com acesso somente às áreas públicas.

## What Changes

- Adicionar login e logout com `st.login()`, `st.user` e `st.logout()`, usando a seção `[auth]` do `secrets.toml`.
- Centralizar a conexão com o Supabase em `services/db.py`, usando as credenciais já fornecidas em `st.secrets["supabase"]` e cache de recurso.
- Criar em `services/auth.py` a resolução do perfil atual a partir da tabela `usuarios`, incluindo a regra de fallback para e-mails `@aluno.impacta.edu.br`.
- Restringir o menu conforme o estado de autenticação e exibir o cartão do usuário no topo para pessoas logadas.
- Fazer cada página restrita verificar o perfil no início e bloquear acessos sem permissão.
- Atualizar o shell visual existente para preservar a base-layout com as novas regras de navegação e autorização.
- Não criar tabelas, SQL, usuários ou registros automáticos no Supabase.

## Capabilities

### New Capabilities

- `auth-perfis`: login federado, resolução de perfil, autorização por página, logout e tratamento de visitantes.

### Modified Capabilities

- `base-layout`: adaptar a navegação e o shell para mostrar menus e cartão de usuário conforme autenticação, sem perder a identidade visual existente.

## Impact

- `app.py` e `pages/`: navegação condicional, apresentação do usuário e verificações de acesso.
- `services/db.py` e `services/auth.py`: novos serviços compartilhados para Supabase e autenticação.
- `.streamlit/secrets.toml`: consumo das configurações existentes de `[auth]` e `[supabase]`, sem expor segredos.
- Dependência de runtime: `supabase-py`, caso ainda não esteja declarada ou instalada.
- Requisitos atendidos: RF01, RF02, RF03, RF05, RF06, RNF02 e RNF04.
