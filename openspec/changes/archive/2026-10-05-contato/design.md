# Design

## Context

A navegação do `app.py` já inclui `pages/contato.py` entre as páginas públicas,
e o shell carrega `assets/style.css` antes de executar a página. O arquivo de
contato ainda é um placeholder. A configuração local já possui uma seção
`contato`, mas a página precisa tolerar instalações em que uma ou mais chaves
não estejam definidas. Ver a motivação em `proposal.md` e os contratos em
`specs/contato-publico/spec.md` e `specs/base-layout/spec.md`.

## Goals / Non-Goals

**Goals:**

- Ler os quatro valores de contato sem acessar banco ou alterar a configuração.
- Manter a página pública e independente de `services/auth.py`.
- Renderizar dois cards com `st.columns`, ações de link somente quando houver
  URL válida e uma faixa inferior com os dados de atendimento.
- Isolar os seletores CSS da página para não alterar o mural, relatórios ou o
  shell existente.
- Tratar chaves ausentes individualmente, preservando os demais elementos.

**Non-Goals:**

- Criar tabelas, SQL, serviços Supabase ou novas dependências.
- Alterar `app.py`, o fluxo de login, perfis, regras de navegação ou o conteúdo
  das demais páginas.
- Validar ou transformar URLs além do necessário para passá-las aos controles
  de link do Streamlit.

## Decisions

### Leitura defensiva da seção de secrets

Ler a seção `contato` e cada chave com acesso tolerante a ausência, convertendo
valores vazios ou ausentes para um estado indisponível. A página não deve
envolver toda a renderização em um fallback único, porque uma chave ausente não
pode ocultar canais que continuam configurados.

**Alternativa considerada:** acessar `st.secrets["contato"]["chave"]`
diretamente. Foi rejeitada porque um `KeyError` interromperia a página e
violaria o requisito de continuidade.

### Fallback visual por item

Quando uma URL não estiver disponível, o card mantém título e descrição e
substitui apenas o botão pela mensagem discreta "Informação indisponível no
momento". Quando o e-mail ou horário faltar, a mesma mensagem ocupa somente o
valor correspondente; um e-mail disponível continua sendo apresentado como
link `mailto`.

**Alternativa considerada:** desabilitar todos os controles ou mostrar um
`st.error` global. Foi rejeitada porque transforma uma configuração parcial em
falha da página e expõe uma experiência técnica desnecessária.

### Estrutura visual com Streamlit e CSS

Usar `st.title`/`st.write` para o cabeçalho textual, duas colunas para os
cards e um container para a faixa informativa. Os cards receberão classes
HTML próprias para aplicar fundo `#24557a` e texto branco, enquanto o CSS
existente controlará a adaptação das colunas em viewport estreito. Botões de
link permanecem componentes nativos do Streamlit para manter acessibilidade e
comportamento de abertura de links.

**Alternativa considerada:** montar toda a tela em um bloco HTML único. Foi
rejeitada porque dificultaria os `st.link_button`, a responsividade nativa e a
manutenção por alunos.

## Risks / Trade-offs

- **[Secrets podem conter strings vazias ou tipos inesperados]** → Normalizar
  valores para texto não vazio antes de exibir ou usar em links; tratar vazio
  como indisponível.
- **[Seletores internos do Streamlit podem variar entre versões]** → Limitar o
  CSS novo às classes próprias da página e usar `st.columns`/componentes
  nativos como estrutura principal.
- **[A faixa de informações não tem o terceiro campo do modelo visual]** →
  Exibir somente Atendimento e E-mail, conforme o escopo solicitado, sem
  inventar dados de coordenação.

## Migration Plan

Não há migração de banco nem alteração de secrets obrigatória. Publicar os dois
arquivos de código e os estilos; validar a página com a configuração completa e
com chaves ausentes. Para rollback, restaurar o placeholder de
`pages/contato.py` e remover apenas as classes CSS adicionadas pela mudança.
