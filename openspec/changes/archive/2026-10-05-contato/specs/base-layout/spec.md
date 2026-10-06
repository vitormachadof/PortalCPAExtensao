# Spec Delta

## MODIFIED Requirements

### Requirement: Navigation includes the main portal sections
The system SHALL present navigation items according to the authentication state: visitantes veem "Mural de devolutivas", "Relatórios e boletins" e "Contato"; usuários autenticados veem também "Início" e "Dashboards". A seção "Contato" deve abrir uma página pública funcional, sem exigir autorização adicional.

#### Scenario: Main navigation is visible
- **DADO** que a interface principal foi carregada
- **QUANDO** o usuário visualiza o menu lateral
- **ENTÃO** cada item permitido para seu estado de autenticação fica visível, com rotulagem clara e organização em ordem de uso.

#### Scenario: Public contact navigation works for visitor
- **DADO** que a pessoa está sem login
- **QUANDO** seleciona "Contato"
- **ENTÃO** a página pública de contato é carregada sem bloqueio ou redirecionamento para login.

#### Scenario: Public contact navigation works for authorized profile
- **DADO** que a pessoa está autenticada com qualquer perfil permitido
- **QUANDO** seleciona "Contato"
- **ENTÃO** a mesma página pública é carregada e o shell preserva a identificação e a ação de saída do usuário.
