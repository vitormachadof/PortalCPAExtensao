# Design

## Context

O shell atual em `app.py` registra todas as páginas no `st.navigation` e as páginas são placeholders sem serviços compartilhados. O projeto já possui configuração de autenticação Google e credenciais do Supabase em secrets; a tabela `usuarios` é externa ao código e não deve ser criada ou modificada por esta mudança.

## Goals / Non-Goals

**Goals:**

- Manter a base visual e a navegação com `st.navigation`.
- Disponibilizar um único caminho para criar o cliente Supabase e um único serviço para resolver o perfil.
- Aplicar o mesmo estado de autenticação ao menu, cartão do usuário e páginas.
- Garantir que e-mails, nomes e perfis sejam usados apenas para a interface e autorização, sem expor segredos.

**Non-Goals:**

- Criar tabelas, migrations, SQL, registros de usuários ou políticas no Supabase.
- Implementar conteúdo funcional dos dashboards, relatórios ou mural.
- Alterar o provedor Google ou inventar uma segunda forma de login.
- Definir permissões internas mais granulares para cada perfil além da distinção entre áreas públicas e autenticadas.

## Decisions

- **Cliente Supabase em serviço cacheado:** `services/db.py` terá uma função com `@st.cache_resource` que lê exclusivamente `st.secrets["supabase"]["url"]` e `st.secrets["supabase"]["key"]`. A ausência de configuração deve gerar erro explícito, sem fallback silencioso.
- **Resolução de perfil em serviço:** `services/auth.py` concentrará leitura de `st.user`, consulta por `email` na tabela `usuarios` e aplicação das regras de ativo, domínio de aluno e visitante. O retorno deve carregar o estado necessário para a UI, incluindo nome, e-mail, perfil e autorização, sem gravar no banco.
- **Consulta limitada ao usuário atual:** a consulta ao Supabase filtrará por e-mail e solicitará no máximo um registro, evitando buscar a tabela inteira. O serviço tratará resultado vazio como caso de regra de negócio, mas propagará falhas de comunicação como erro visível da aplicação.
- **Menu derivado do estado atual:** `app.py` resolverá o usuário antes de montar `st.navigation`. Visitantes receberão apenas as três páginas públicas e o botão de login; usuários autorizados receberão também Início e Dashboards. O botão de login deve ficar no shell e chamar `st.login()`.
- **Guarda reutilizável nas páginas:** páginas com conteúdo reservado chamarão uma guarda no início, antes de renderizar conteúdo. A guarda encerra o fluxo da página quando o estado é visitante ou não autorizado, evitando que o bloqueio dependa apenas do menu.
- **Identidade no shell:** o cartão do usuário será renderizado na área principal do shell para sessões autorizadas, usando nome da tabela quando disponível e dados do provedor como fallback visual, sem mostrar tokens ou credenciais.
- **Permissões da primeira versão:** todas as áreas autenticadas são acessíveis a qualquer perfil válido (`aluno`, `coordenador`, `avaliador` e `admin`); as três áreas públicas não exigem login. A estrutura da guarda permitirá ampliar a matriz depois sem duplicar consulta ou lógica.

Alternativas consideradas:

- Consultar o Supabase diretamente em cada página: descartado porque duplica credenciais, consultas e regras de fallback.
- Deixar todas as páginas no menu e bloquear apenas no conteúdo: descartado porque revela áreas restritas a visitantes e não atende ao menu condicional.
- Criar usuários de domínio de aluno no banco automaticamente: descartado porque a regra exige fallback sem gravação e o banco é administrado fora do aplicativo.
- Usar apenas o e-mail do Google como perfil: descartado porque perfis ativos e nomes são definidos pela tabela `usuarios`.

## Risks / Trade-offs

- [O cliente Supabase ou a tabela pode estar indisponível] → Propagar erro de configuração/conexão de forma explícita e orientar a correção nos secrets, sem transformar falha técnica em acesso de visitante.
- [O usuário do Google pode não fornecer nome no formato esperado] → Usar o nome disponível em `st.user` e um rótulo neutro apenas para apresentação, mantendo o e-mail como identificador da consulta.
- [O conteúdo restrito pode ser acessado por URL direta] → Executar a guarda no início de cada página restrita, independentemente do menu.
- [Cache de recurso manter cliente após mudança de secrets] → Usar o padrão de cache do Streamlit e exigir reinício da aplicação após alteração de credenciais.

## Migration Plan

1. Confirmar que `supabase-py` está disponível no ambiente e que os secrets existentes contêm as seções necessárias.
2. Implementar os serviços e integrar o shell sem alterar o schema do banco.
3. Validar a aplicação com sessão visitante, conta autorizada, conta inativa, conta inexistente e aluno por domínio.
4. Para rollback, remover a integração de serviços e retornar ao shell anterior; nenhuma migração de dados é necessária.

## Open Questions

Nenhuma pendência que altere o contrato desta mudança. A matriz de permissões específica por funcionalidade pode ser detalhada em uma mudança posterior quando o conteúdo das páginas estiver definido.
