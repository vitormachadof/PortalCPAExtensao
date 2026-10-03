# Design

## Context

A aplicação é uma interface em Streamlit para o Portal CPA. A mudança atual define apenas a base visual do sistema, seguindo o estilo institucional da Faculdade Impacta e deixando as regras de autenticação, dados e dashboards em fases posteriores.

## Goals / Non-Goals

**Goals:**
- Definir a identidade visual da aplicação.
- Criar a estrutura de navegação principal do portal.
- Preparar páginas vazias para os módulos futuros.
- Garantir que o layout funcione em diferentes tamanhos de tela.

**Non-Goals:**
- Login com Google.
- Banco de dados do Supabase.
- Conteúdo real de dashboards, relatórios ou devolutivas.
- Lógica de autorização por perfil.

## Decisions

- O tema será definido em `.streamlit/config.toml` para manter cores e tokens centralizados.
- O arquivo de CSS ficará em `assets/style.css` e será carregado uma única vez no `app.py`, antes do render principal, para evitar duplicação de estilos e manter o shell consistente.
- A aplicação usará `st.set_page_config(page_title="Portal CPA", layout="wide")` no `app.py` para garantir a visualização ampla e a identidade da interface.
- A configuração do Streamlit no `config.toml` usará `client.toolbarMode = "minimal"` para esconder o menu de desenvolvedor e manter a tela mais limpa para o usuário final.
- A navegação principal será implementada com `st.navigation`, conforme orientação do projeto.
- A faixa superior e o menu lateral serão construídos a partir do shell da aplicação, mantendo consistência entre todas as páginas.
- Ajustes visuais que o Streamlit não resolve serão centralizados em um único arquivo CSS para reduzir duplicação e facilitar manutenção.
- As páginas serão criadas como placeholders vazios, sem conteúdo funcional, para não mexer em regras de negócio ainda não definidas.

**Alternatives considered:**
- Estilo inline em cada página: descartado porque aumenta repetição e dificulta manutenção.
- Manter a navegação em manual ou sem shell global: descartado porque quebra a identidade visual e a consistência do portal.

## Risks / Trade-offs

- [Aparência pouco consistente em telas pequenas] → Mitigation: usar estrutura responsiva e testar a composição em diferentes larguras.
- [CSS customizado divergindo do tema principal] → Mitigation: centralizar a personalização em um único arquivo e usar tokens do tema.
- [Páginas vazias gerando sensação de incompletude] → Mitigation: manter a estrutura de navegação clara e os títulos em caixa alta para indicar os módulos futuros.

## Migration Plan

Não há migração de dados ou integrações ativas nesta fase. A mudança prepara a camada visual para que os módulos seguintes sejam adicionados sem reestruturação geral do layout.

## Open Questions

Nenhuma pendência crítica. Os detalhes de autenticação, dashboards reais e integração com banco serão tratados em mudanças específicas posteriores.
