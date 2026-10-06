# Proposal

## Why

A página pública de "Relatórios e boletins" ainda é um placeholder, impedindo
que a comunidade consulte os PDFs institucionais e que usuários autorizados
acessem documentos restritos. A mudança cria uma biblioteca única, com controle
de visibilidade no servidor e downloads protegidos por links temporários.

## What Changes

- Implementar a página `pages/relatorios.py` para visitantes e perfis
  autenticados autorizados, seguindo o shell e o modelo visual do Portal CPA.
- Criar `services/documentos.py` para consultar documentos do Supabase com
  visibilidade definida no servidor conforme o estado de autenticação.
- Adicionar filtros por tipo e ano, ordenação por ano decrescente e título.
- Exibir documentos em cards com título, tipo, ano, etiqueta "Restrito" quando
  aplicável e ação "Baixar PDF".
- Gerar URLs assinadas do bucket privado `documentos` com validade de dez
  minutos, sem armazená-las em cache além desse prazo.
- Tratar falhas de banco e Storage com mensagens amigáveis, sem detalhes
  técnicos ou credenciais, e adicionar estilos somente a `assets/style.css`.

## Capabilities

### New Capabilities

- `relatorios-documentos`: Consulta, filtragem e download seguro de relatórios e
  boletins institucionais.

### Modified Capabilities

- Nenhuma. As regras existentes de navegação pública, autenticação e identidade
  visual permanecem compatíveis; a mudança implementa o comportamento da seção
  de documentos.

## Impact

- **Código:** `pages/relatorios.py`, novo serviço `services/documentos.py` e
  estilos adicionais em `assets/style.css`.
- **Dados e Storage:** leitura da tabela `documentos` e criação de signed URLs
  no bucket privado `documentos`, usando `services/db.py`; não haverá tabelas,
  buckets ou SQL.
- **Requisitos:** atende RF15, RNF01 e RNF02, especialmente a filtragem
  server-side de documentos públicos para visitantes.
