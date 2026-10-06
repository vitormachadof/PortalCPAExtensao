# Proposal

## Why

A navegação pública do Portal CPA já oferece a seção "Contato", mas a página
atual é apenas um placeholder e não orienta visitantes ou perfis autenticados
sobre como falar com a equipe. A mudança entrega um ponto de contato direto,
com os canais configurados pela instituição e uma apresentação alinhada ao
modelo visual do portal.

## What Changes

- Implementar `pages/contato.py` como página pública acessível a visitantes e
  todos os perfis autenticados.
- Exibir o título, texto introdutório, cards de Google Chat e Google Meet com
  ações `st.link_button`.
- Exibir horário de atendimento e e-mail em uma faixa informativa inferior,
  incluindo link `mailto` para o e-mail.
- Ler `chat_url`, `meet_url`, `email` e `horario` de `st.secrets["contato"]`.
- Substituir individualmente valores ausentes por "Informação indisponível no
  momento", sem impedir a renderização do restante da página.
- Adicionar somente em `assets/style.css` os estilos específicos dos cards e da
  faixa de informações.

## Capabilities

### New Capabilities

- `contato-publico`: Apresentação pública dos canais de contato da CPA, com
  links configuráveis, atendimento e tratamento de informações indisponíveis.

### Modified Capabilities

- `base-layout`: A navegação pública já prevista passa a renderizar uma página
  de contato funcional, preservando o shell visual e a responsividade.

## Impact

- **Código:** `pages/contato.py` e `assets/style.css`.
- **Configuração:** leitura somente das chaves existentes em
  `st.secrets["contato"]`; nenhuma tabela, SQL ou alteração no Supabase.
- **Acesso:** nenhuma mudança nas regras de login ou autorização; a página
  permanece pública para visitantes, alunos, coordenadores, avaliadores
  externos e admin CPA.
- **Requisitos:** atende RF17 (canais públicos de contato) e RNF01
  (identidade visual, responsividade e tratamento amigável de falhas de
  configuração).
