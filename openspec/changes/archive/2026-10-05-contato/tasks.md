# Tasks

## 1. Página pública e configuração

- [x] 1.1 Substituir o placeholder de `pages/contato.py` pela estrutura pública com título, frase introdutória, dois cards em `st.columns` e faixa de atendimento; verificar no navegador que visitantes e perfis autenticados conseguem abrir "Contato" sem bloqueio.
- [x] 1.2 Implementar a leitura defensiva de `st.secrets["contato"]` para `chat_url`, `meet_url`, `email` e `horario`, renderizando `st.link_button` e `mailto` quando disponíveis; verificar com a configuração completa que cada ação aponta para o valor correspondente.
- [x] 1.3 Adicionar o fallback individual "Informação indisponível no momento" para URLs, e-mail ou horário ausentes; verificar removendo uma chave por vez que os demais itens continuam visíveis e nenhum erro técnico aparece na tela.

## 2. Identidade visual e responsividade

- [x] 2.1 Adicionar em `assets/style.css` somente as classes da página de contato para cards azuis `#24557a`, texto branco, faixa cinza e mensagens discretas; verificar visualmente a correspondência com o modelo anexado sem alterar as páginas existentes.
- [x] 2.2 Ajustar o comportamento responsivo das colunas e conteúdos dos cards; verificar no navegador em viewport desktop e estreito que os cards ficam lado a lado no desktop e empilham no celular sem cortar textos ou botões.

## 3. Integração

- [x] 3.1 Executar a validação do OpenSpec e iniciar a aplicação Streamlit; verificar a navegação de visitante e de usuário autenticado, o shell institucional e a ausência de regressões nas páginas públicas existentes.
