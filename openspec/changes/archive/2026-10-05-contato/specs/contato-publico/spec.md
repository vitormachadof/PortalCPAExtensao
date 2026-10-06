# Spec Delta

## Purpose

Oferecer um canal público, claro e responsivo para visitantes e usuários do
Portal CPA entrarem em contato com a equipe por chat, reunião, e-mail e
horário de atendimento configurados pela instituição.

## ADDED Requirements

### Requirement: Public contact page presents the CPA channels
The system SHALL render the contact page for visitors and all authorized profiles with the title, introductory text, two channel cards, and an attendance information strip.

#### Scenario: Visitor views contact page
- **DADO** que a pessoa está sem autenticação
- **QUANDO** seleciona "Contato" na navegação
- **ENTÃO** vê "FALE COM A CPA", a frase introdutória, os cards "GOOGLE CHAT" e "GOOGLE MEET", e a faixa com "Atendimento" e "E-mail"; não precisa fazer login e não vê conteúdo restrito.

#### Scenario: Authorized profile views contact page
- **DADO** que a pessoa está autenticada como aluno, coordenador, avaliador externo ou admin CPA
- **QUANDO** seleciona "Contato"
- **ENTÃO** vê o mesmo conteúdo público da página e mantém seu cartão de identidade e ação de saída no shell; nenhum perfil recebe conteúdo exclusivo nesta página.

### Requirement: Contact channels expose configured actions
The system SHALL use the configured Chat and Meet URLs for their respective link buttons and render the configured e-mail as a `mailto` link and the configured attendance schedule.

#### Scenario: Configuration is available
- **DADO** que `st.secrets["contato"]` contém `chat_url`, `meet_url`, `email` e `horario`
- **QUANDO** a página é renderizada
- **ENTÃO** o card de chat exibe "Abrir o Chat", o card de Meet exibe "Entrar na sala", os botões abrem suas URLs configuradas, e o e-mail aparece como link `mailto` com o horário configurado.

### Requirement: Missing contact configuration is non-blocking
The system SHALL keep rendering the contact page when one or more contact keys are absent and SHALL show "Informação indisponível no momento" only in the affected item.

#### Scenario: One contact value is missing
- **DADO** que uma chave individual de `st.secrets["contato"]` está ausente
- **QUANDO** a página é renderizada
- **ENTÃO** os demais textos e ações permanecem disponíveis, o item afetado mostra discretamente "Informação indisponível no momento" e a página não exibe erro técnico.

#### Scenario: All contact values are missing
- **DADO** que nenhuma das chaves de contato está disponível
- **QUANDO** a página é renderizada
- **ENTÃO** a estrutura completa da página aparece com a mensagem discreta nos itens afetados, sem interromper a navegação pública.

### Requirement: Contact page preserves responsive visual identity
The system SHALL present the cards side by side on wide screens, allow them to stack on narrow screens, and use the institutional blue cards with white text and a gray information strip.

#### Scenario: Contact page adapts to viewport
- **DADO** que a página é exibida em desktop ou em uma tela estreita
- **QUANDO** a largura do viewport muda
- **ENTÃO** os cards usam `st.columns`, permanecem legíveis e empilham no celular sem quebrar o conteúdo, mantendo fundo azul `#24557a`, texto branco e a faixa inferior cinza.
