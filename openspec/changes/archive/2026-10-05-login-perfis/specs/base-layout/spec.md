# Spec Delta

## MODIFIED Requirements

### Requirement: Portal CPA exposes a consistent visual shell
The system SHALL render a top bar with the title "PORTAL CPA" and the subtitle "Comissão Própria de Avaliação", followed by a dark side navigation panel labeled "ACESSO RÁPIDO" and a main content area for page content. Para usuários autenticados, a área principal também deve apresentar o cartão de identidade e a ação de saída.

#### Scenario: Initial app load
- **DADO** que a aplicação iniciou corretamente
- **QUANDO** uma pessoa abre o portal no navegador
- **ENTÃO** a faixa superior, o menu lateral e a área principal aparecem como uma estrutura única e visualmente padronizada; se houver sessão autorizada, o cartão mostra nome e perfil.

### Requirement: Navigation includes the main portal sections
The system SHALL present navigation items according to the authentication state: visitantes veem "Mural de devolutivas", "Relatórios e boletins" e "Contato"; usuários autenticados veem também "Início" e "Dashboards".

#### Scenario: Main navigation is visible
- **DADO** que a interface principal foi carregada
- **QUANDO** o usuário visualiza o menu lateral
- **ENTÃO** cada item permitido para seu estado de autenticação fica visível, com rotulagem clara e organização em ordem de uso.

### Requirement: Visual identity matches the academic context and response requirements
The system SHALL use the institutional palette composed of dark blue for the header and sidebar, a light gray background for the content area and uppercase titles in the main blue tone, preserving readability and responsiveness on desktop and mobile layouts.

#### Scenario: Responsive and branded layout
- **DADO** que a tela é adaptada ao tamanho da janela
- **QUANDO** o portal é exibido em diferentes tamanhos de viewport
- **ENTÃO** o layout mantém a identidade visual da Impacta, os títulos em caixa alta, a navegação autorizada e a leitura sem quebrar.

### Requirement: Pages are prepared as empty placeholders for future flow
The system SHALL keep the initial page stubs available, mas páginas restritas devem aplicar sua verificação de perfil antes de renderizar qualquer conteúdo reservado.

#### Scenario: Empty placeholders are available
- **DADO** que a página correspondente foi acessada por uma pessoa autorizada
- **QUANDO** a pessoa seleciona uma seção do menu
- **ENTÃO** a tela existe como espaço de conteúdo inicial; em página restrita, o conteúdo só aparece depois da verificação de permissão.
