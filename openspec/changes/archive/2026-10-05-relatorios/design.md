# Design

## Context

A página [pages/relatorios.py](../../../pages/relatorios.py) é atualmente um
placeholder. A navegação já disponibiliza a seção para visitantes e usuários
autorizados, enquanto [services/db.py](../../../services/db.py) fornece o
cliente Supabase a partir de `st.secrets`. A tabela `documentos` e o bucket
privado `documentos` já existem remotamente e não devem ser criados ou
alterados pelo projeto.

## Goals / Non-Goals

**Goals:**

- Centralizar em `services/documentos.py` a consulta de documentos e a criação
  de URLs assinadas.
- Aplicar a visibilidade no banco: visitantes consultam com `publico = true`;
  usuários autorizados consultam todos os registros.
- Cachear somente a lista de documentos por cinco minutos, sem cachear links
  assinados além dos dez minutos de validade.
- Manter o bucket privado, a autenticação existente e o layout institucional.

**Non-Goals:**

- Criar ou alterar tabelas, buckets, políticas RLS ou scripts SQL.
- Tornar arquivos públicos ou persistir URLs assinadas.
- Adicionar upload, edição, publicação ou exclusão de documentos.
- Alterar as regras de autenticação ou o menu global.

## Decisions

### Serviço com consulta condicionada ao perfil

O serviço receberá uma indicação de acesso autorizado e montará a consulta
Supabase com os campos `id, titulo, tipo, ano, caminho_arquivo, publico`.
Quando o acesso não for autorizado, aplicará `.eq("publico", True)` no servidor;
quando for autorizado, não aplicará esse filtro. A página obterá o
`UserState` com `get_current_user()` apenas para escolher a consulta, sem
reimplementar as regras de perfil.

**Alternativa considerada:** carregar todos os documentos e filtrar em Python.
Foi rejeitada porque violaria RNF02 ao expor metadados restritos ao cliente.

### Lista cacheada e signed URL sem cache

Aplicar `@st.cache_data(ttl=300)` somente à função de listagem, com a condição
de visibilidade como argumento do cache. A função de Storage ficará sem
`st.cache_data`; cada renderização solicitará uma nova signed URL com
`expires_in=600`, mantendo o tempo de validade sob o limite exigido.

**Alternativa considerada:** cachear a URL por dez minutos. Foi rejeitada
porque a expiração e a invalidação podem não coincidir exatamente com o
cache da página, criando risco de link expirado.

### Renderização e download

Usar `st.columns` para tipo e ano e `st.container(border=True)` para cada
documento. A ação "Baixar PDF" será um link/botão de link com a URL assinada
gerada no servidor. Erros de Storage serão tratados sem interpolar a exceção
na interface.

### Ordenação e filtros

A consulta buscará documentos visíveis e a página derivará os anos disponíveis.
A ordenação por ano decrescente e título será feita na consulta ou em uma
camada determinística do serviço, preservando a mesma ordem para todos os
perfis e combinações de filtro.

## Risks / Trade-offs

- **[Signed URL expira durante uma sessão longa]** → Não armazenar a URL no
  cache; gerar novamente em cada execução da página.
- **[Mudança de visibilidade pode aguardar o TTL da lista]** → Usar TTL de 300
  segundos conforme requisito e permitir nova consulta após expiração.
- **[Documento com caminho inválido ou removido]** → Exibir mensagem genérica
  de download indisponível, registrar o erro apenas no log e não revelar o
  caminho ao usuário.
- **[Perfil autorizado muda durante a sessão]** → Reutilizar `get_current_user`
  a cada execução para que a condição da consulta acompanhe o estado atual.

## Migration Plan

Não há migração. Após a publicação, validar visitante e usuário autorizado com
documentos públicos e restritos, conferir expiração de signed URL e manter o
rollback limitado à restauração do placeholder da página.
