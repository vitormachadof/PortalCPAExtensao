# Proposal

## Why

A base visual do portal CPA ainda não está definida, o que dificulta a padronização da identidade da Faculdade Impacta e a navegação do sistema. Esta mudança cria a estrutura inicial da interface para atender os requisitos de responsividade e identidade visual, mantendo as páginas vazias e sem login nem banco de dados no momento.

## What Changes

- Cria a estrutura visual base do portal com faixa azul-marinho no topo e menu lateral escuro.
- Define a paleta e os estilos globais do sistema em configuração do Streamlit.
- Adiciona páginas vazias para Início, Dashboards, Mural de devolutivas, Relatórios e boletins e Contato.
- Centraliza ajustes visuais específicos em um único arquivo CSS.
- Mantém a autenticação e os dados fora do escopo desta etapa.

## Capabilities

### New Capabilities
- `base-layout`: estrutura visual e navegação principal do Portal CPA, incluindo tema, shell e páginas de referência.

### Modified Capabilities
- Nenhuma.

## Impact

- `app.py`: criação da aplicação base e navegação principal.
- `.streamlit/config.toml`: definição do tema visual do portal.
- `pages/`: páginas vazias de navegação.
- `assets/`: arquivos de estilo e recursos visuais compartilhados.
- `services/`: preparação estrutural sem integração ainda ativa.

Esta mudança atende principalmente RNF01 e RNF07, e orienta a base para os próximos incrementos do portal.
