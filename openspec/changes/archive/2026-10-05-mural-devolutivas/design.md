# Design

## Context

A navegação pública já aponta para `pages/mural.py`, que atualmente é um
placeholder. O shell carrega `assets/style.css`, e `services/db.py` fornece um
cliente Supabase cacheado a partir de `st.secrets`. A tabela `devolutivas` já
existe no Supabase e não deve ser criada ou alterada por esta mudança.

## Goals / Non-Goals

**Goals:**

- Separar a leitura de dados em `services/devolutivas.py`, mantendo a página
  responsável apenas por estado de filtros e renderização.
- Consultar somente os campos necessários, restringir a publicação no banco e
  ordenar por `data_publicacao` decrescente.
- Cachear a consulta bruta por cinco minutos, mantendo os filtros locais e
  evitando uma nova chamada ao banco a cada interação.
- Preservar o shell e a linguagem visual existentes, acrescentando estilos
  somente em `assets/style.css`.

**Non-Goals:**

- Criar tabelas, índices, registros de exemplo ou scripts SQL.
- Permitir edição, publicação ou exclusão de devolutivas.
- Alterar login, perfis, páginas restritas ou o modelo de navegação.

## Decisions

### Serviço dedicado para a consulta

Criar uma função de serviço que use `get_supabase_client()`, selecione
`id, titulo, area, demanda, resposta, data_publicacao`, aplique
`publicado = true` e faça a ordenação por `data_publicacao` descendente. A
camada de página não conhecerá a chamada Supabase, facilitando testes e
mantendo o acesso ao banco centralizado.

**Alternativa considerada:** consultar diretamente na página. Foi rejeitada
porque mistura acesso a dados com apresentação e dificulta o tratamento comum
de erros.

### Cache e filtragem local

Aplicar `@st.cache_data(ttl=300)` à função que busca as devolutivas publicadas.
A página derivará áreas e anos a partir do resultado cacheado e aplicará os
filtros localmente, inclusive a busca sem distinção de maiúsculas e minúsculas.

**Alternativa considerada:** enviar cada filtro ao Supabase. Foi rejeitada para
evitar consultas por clique e porque o conjunto público pode ser reutilizado
por todos os filtros durante o TTL.

### Renderização e estado público

Usar `st.columns` para os três controles, `st.container(border=True)` para cada
card e elementos Markdown com classes próprias para a faixa da área, rótulos e
textos. A página não chamará `require_authenticated`; visitantes e perfis
autenticados executarão o mesmo fluxo.

### Erros e dados incompletos

Tratar falhas do serviço com uma mensagem genérica no nível da página, sem
interpolar a exceção na interface. Campos textuais ausentes serão apresentados
de forma segura e a data somente será formatada quando puder ser interpretada,
evitando que um registro impeça os demais de aparecer.

## Risks / Trade-offs

- **[Alteração no schema remoto]** → Selecionar explicitamente os campos
  definidos para `devolutivas` e deixar o erro visível como mensagem amigável,
  sem criar compatibilidade inventada.
- **[Cache mantém conteúdo por até cinco minutos]** → Aplicar TTL de 300
  segundos conforme requisito; uma nova execução após expiração busca o estado
  atualizado.
- **[CSS específico pode não refletir todos os temas do Streamlit]** →
  Reutilizar a paleta existente, limitar seletores às classes da página e
  conferir a leitura em viewport desktop e móvel.

## Migration Plan

Não há migração de banco. Após publicar o código, validar com registros
publicados e não publicados no Supabase; o rollback consiste em restaurar o
placeholder anterior caso a página apresente regressão.
