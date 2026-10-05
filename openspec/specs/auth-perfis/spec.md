# auth-perfis Specification

## Purpose

Controlar a entrada no Portal CPA e a autorização das áreas conforme o usuário autenticado, preservando uma experiência pública segura para visitantes e contas sem permissão.

## Requirements

### Requirement: Google login identifies the current user
O sistema SHALL permitir que uma pessoa inicie o login com a conta Google Impacta e encerre a sessão pelo portal.

#### Scenario: Visitante inicia login
- **DADO** que a pessoa não está autenticada
- **QUANDO** seleciona "Entrar com conta Impacta"
- **ENTÃO** o sistema inicia `st.login()` e, após o retorno, usa os dados disponíveis em `st.user`.

#### Scenario: Usuário encerra a sessão
- **DADO** que existe uma sessão autenticada
- **QUANDO** a pessoa seleciona "Sair"
- **ENTÃO** o sistema chama `st.logout()` e volta a tratar a pessoa como visitante.

### Requirement: Profile resolution follows the usuarios rules
O sistema SHALL resolver o perfil atual consultando o e-mail autenticado na tabela `usuarios`, sem criar ou alterar registros durante o login.

#### Scenario: Usuário cadastrado e ativo
- **DADO** que o e-mail autenticado existe em `usuarios` com `ativo = true`
- **QUANDO** o perfil é resolvido
- **ENTÃO** o sistema usa o perfil armazenado, entre `aluno`, `coordenador`, `avaliador` e `admin`.

#### Scenario: E-mail de aluno não cadastrado
- **DADO** que o e-mail não existe em `usuarios` e termina em `@aluno.impacta.edu.br`
- **QUANDO** o perfil é resolvido
- **ENTÃO** o sistema trata a pessoa como `aluno` sem gravar o usuário no banco.

#### Scenario: Usuário não autorizado
- **DADO** que o e-mail não existe em `usuarios` ou existe com `ativo = false`, e não atende à regra de aluno
- **QUANDO** o perfil é resolvido
- **ENTÃO** o sistema mostra "Acesso não autorizado" e trata a pessoa como visitante.

### Requirement: Menus reflect authentication state
O sistema SHALL mostrar apenas as áreas permitidas para o estado atual da sessão.

#### Scenario: Visitante navega pelo portal
- **DADO** que a pessoa está sem login ou foi tratada como visitante
- **QUANDO** o menu é exibido
- **ENTÃO** ficam disponíveis somente "Mural de devolutivas", "Relatórios e boletins", "Contato" e o botão "Entrar com conta Impacta"; "Início" e "Dashboards" não ficam disponíveis.

#### Scenario: Usuário autorizado navega pelo portal
- **DADO** que a pessoa está autenticada com perfil `aluno`, `coordenador`, `avaliador` ou `admin`
- **QUANDO** o menu é exibido
- **ENTÃO** ficam disponíveis também "Início" e "Dashboards", além das áreas públicas.

### Requirement: User card shows identity and logout
O sistema SHALL exibir no topo da área principal a identificação do usuário autenticado e uma ação de saída.

#### Scenario: Cartão de usuário autenticado
- **DADO** que o usuário foi autorizado
- **QUANDO** uma página do portal é carregada
- **ENTÃO** o cartão mostra "Olá, [nome] · Perfil: [perfil]" e o botão "Sair", sem exibir credenciais.

### Requirement: Restricted pages enforce permissions
O sistema SHALL verificar a autorização no início de cada página restrita e bloquear o conteúdo quando o perfil não tiver permissão.

#### Scenario: Visitante tenta abrir página restrita
- **DADO** que a pessoa é visitante
- **QUANDO** tenta acessar diretamente uma página restrita
- **ENTÃO** a página bloqueia o conteúdo e informa que o acesso não é autorizado.

#### Scenario: Perfil sem permissão tenta abrir página restrita
- **DADO** que a pessoa está autenticada, mas seu perfil não está autorizado para a página
- **QUANDO** a página é carregada
- **ENTÃO** a página bloqueia o conteúdo e não exibe dados restritos.
