# Proposal

## Why

O Portal CPA já expõe o caminho público do mural, mas a página ainda é um
placeholder e não permite consultar as respostas dadas pelas áreas às demandas
das pesquisas. A entrega torna essas devolutivas publicadas acessíveis a
visitantes e perfis autenticados, com filtros para localizar rapidamente o
conteúdo mais relevante.

## What Changes

- Implementar a página pública `pages/mural.py` seguindo o layout institucional
  existente, sem exigir login.
- Criar um serviço em `services/` para consultar apenas registros publicados da
  tabela `devolutivas`, ordenados por `data_publicacao` decrescente.
- Exibir cada devolutiva com área, data, título, demanda e resposta em card
  visualmente consistente com o modelo.
- Adicionar filtros por área, ano e palavra-chave em título, demanda e resposta,
  além de mensagens amigáveis para lista vazia e falha de consulta.
- Usar `st.cache_data` com TTL de cinco minutos e concentrar novos estilos em
  `assets/style.css`.

## Capabilities

### New Capabilities

- `mural-devolutivas`: Consulta pública, filtragem e apresentação das
  devolutivas publicadas da CPA.

### Modified Capabilities

- Nenhuma. A navegação e as regras de autenticação existentes já contemplam a
  página pública; a mudança implementa o comportamento específico do mural.

## Impact

- **Código:** `pages/mural.py`, novo módulo de consulta em `services/` e
  estilos adicionais em `assets/style.css`.
- **Dados:** leitura somente da tabela Supabase `devolutivas` por meio de
  `services/db.py`; não haverá criação ou alteração de tabelas.
- **Requisitos:** atende RF11 (mural de devolutivas), RF13 (consulta pública
  das respostas) e RNF01 (consistência visual e acessibilidade básica da
  interface).
