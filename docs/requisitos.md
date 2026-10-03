# Requisitos do Portal CPA

## Matriz de acesso por perfil

| Conteúdo | Visitante | Aluno | Coordenador | Avaliador externo | Admin CPA |
| --- | --- | --- | --- | --- | --- |
| Mural de devolutivas | Sim | Sim | Sim | Sim | Sim + publica |
| Relatórios e boletins | Sim (públicos) | Sim | Sim | Sim | Sim + envia |
| Contato | Sim | Sim | Sim | Sim | Sim |
| Dashboard pesquisa CPA | Não | Sim | Sim | Sim | Sim |
| Dashboard avaliação docente | Não | Não | Sim | Sim | Sim |
| Dashboard egressos | Não | Não | Sim | Sim | Sim |
| Gestão de usuários e dashboards | Não | Não | Não | Não | Sim |

## Requisitos funcionais

| ID | Módulo | Requisito |
| --- | --- | --- |
| RF01 | Acesso | O sistema permite login com conta Google. |
| RF02 | Acesso | O sistema define o perfil do usuário (aluno, coordenador, avaliador externo, admin CPA). |
| RF03 | Acesso | E-mails do domínio de aluno da Impacta recebem o perfil aluno automaticamente. |
| RF04 | Acesso | O admin cadastra, altera e remove coordenadores e avaliadores externos. |
| RF05 | Acesso | O usuário vê no menu apenas as páginas permitidas ao seu perfil. |
| RF06 | Acesso | O usuário pode sair (logout) a qualquer momento. |
| RF07 | Dashboards | A página inicial exibe os dashboards do Looker Studio do perfil logado. |
| RF08 | Dashboards | Aluno vê a pesquisa da CPA; coordenador vê CPA, avaliação docente e egressos; avaliador externo vê tudo. |
| RF09 | Dashboards | O admin cadastra um dashboard (título, URL de incorporação, perfis que podem ver). |
| RF10 | Dashboards | Cada dashboard tem um botão para abrir em tela cheia no Looker Studio. |
| RF11 | Mural | O mural de devolutivas é público, sem login. |
| RF12 | Mural | O admin publica, edita e despublica devolutivas (título, área, demanda, resposta, data). |
| RF13 | Mural | O visitante filtra as devolutivas por área e por período. |
| RF14 | Relatórios | O admin envia documentos em PDF com título, tipo (relatório ou boletim) e ano. |
| RF15 | Relatórios | O usuário lista, filtra e baixa os documentos. |
| RF16 | Relatórios | O admin remove ou substitui um documento. |
| RF17 | Contato | A página de contato mostra links para Google Chat e Google Meet da CPA. |
| RF18 | Contato | O admin altera os links de contato sem mexer no código. |
| RF19 | Admin | Existe uma área administrativa visível só para o perfil admin CPA. |
| RF20 | Admin | A área administrativa mostra pré-visualização e confirmação antes de publicar. |

## Requisitos não funcionais

| ID | Categoria | Requisito |
| --- | --- | --- |
| RNF01 | Responsividade | Todas as páginas funcionam em celular, tablet e notebook. |
| RNF02 | Segurança | O controle de acesso é checado no servidor, não só escondendo páginas. |
| RNF03 | Segurança | Os relatórios do Looker Studio são compartilhados só com os grupos certos. |
| RNF04 | Segurança | Segredos (chaves do Supabase, OAuth) ficam fora do código, em secrets.toml. |
| RNF05 | Usabilidade | A CPA consegue usar a área administrativa sem conhecimento técnico. |
| RNF06 | Acessibilidade | Contraste adequado, textos alternativos e navegação clara. |
| RNF07 | Identidade | O portal usa as cores e o logo da Impacta. |
| RNF08 | Disponibilidade | O portal fica no ar sem hibernar. |
| RNF09 | Manutenção | O código fica versionado no GitHub, com README e comentários. |
| RNF10 | Documentação | O projeto entrega manual do usuário e documentação técnica. |