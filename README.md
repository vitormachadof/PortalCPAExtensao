# Portal CPA

Plataforma web da CPA da Faculdade Impacta para centralizar informações, dashboards e comunicação institucional.
Sistema pensado para apoiar a Comissão Própria de Avaliação com acesso diferenciado por perfil e organização de dados de forma simples e visual.

## 1. Contexto

O Portal CPA é um projeto de extensão da Faculdade Impacta voltado para a Comissão Própria de Avaliação. A proposta é criar uma interface web para reunir relatórios, dashboards, devolutivas, informações institucionais e área administrativa em um único ponto de acesso, com navegação adaptada ao perfil do usuário.

O projeto foi pensado para uso em ambiente acadêmico, com foco em acessibilidade, organização e manutenção simples. O banco de dados e os arquivos de dados ficam no Supabase, enquanto a interface principal é construída com Streamlit. A modelagem do banco é tratada separadamente pelo Vitor, conforme a regra do projeto.

## 2. Funcionalidades principais

- Login com conta Google, com autenticação centralizada na aplicação.
- Perfil de aluno definido automaticamente pelo e-mail institucional; coordenadores e avaliadores externos cadastrados pelo admin CPA.
- Painel com dashboards do Looker Studio por perfil logado.
- Mural de devolutivas público, com filtros por área e período.
- Publicação e gerenciamento de relatórios e boletins pela administração.
- Página de contato com links institucionais da CPA.
- Área administrativa exclusiva para o perfil admin CPA.
- Controle de acesso no servidor, sem depender apenas de esconder opções na interface.

## 3. Perfis de acesso

Resumo da matriz de acesso do portal:

| Perfil | Visualiza mural | Visualiza relatórios e boletins | Visualiza dashboards | Gestão administrativa |
| --- | --- | --- | --- | --- |
| Visitante | Sim | Sim, públicos | Não | Não |
| Aluno | Sim | Sim | Sim, pesquisa CPA | Não |
| Coordenador | Sim | Sim | Sim | Não |
| Avaliador externo | Sim | Sim | Sim | Não |
| Admin CPA | Sim, com publicação | Sim, com envio | Sim | Sim |

Detalhes do comportamento por perfil:

- Visitante: acesso ao mural público e informações abertas da CPA.
- Aluno: acesso às informações públicas e aos dashboards permitidos, com foco na pesquisa da CPA.
- Coordenador: acesso aos dashboards de CPA, avaliação docente e egressos.
- Avaliador externo: acesso aos dashboards disponíveis e relatórios do contexto institucional.
- Admin CPA: acesso total à administração do sistema, com cadastro, publicação e gestão de conteúdo.

## 4. Tecnologias

- Python 3.14
- Streamlit
- Supabase (Postgres + Storage via supabase-py)
- Looker Studio
- OpenSpec

O projeto segue uma abordagem orientada por especificações, com documentação e mudanças rastreadas em arquivos de spec e change do OpenSpec.

## 5. Como rodar localmente no Windows

1. Crie a virtual environment na raiz do projeto:

   ```powershell
   python -m venv .venv
   ```

2. Ative a ambiente virtual:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

3. Instale as dependências:

   ```powershell
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. Crie o arquivo de segredos do Streamlit:

   ```powershell
   mkdir .streamlit
   ```

   Crie o arquivo .streamlit/secrets.toml com um exemplo sem valores reais:

   ```toml
   [auth]
   redirect_uri = "http://localhost:8501/oauth2callback"
   cookie_secret = "UMA_STRING_ALEATORIA_LONGA"
   client_id = "SEU_CLIENT_ID_GOOGLE"
   client_secret = "SEU_CLIENT_SECRET_GOOGLE"
   server_metadata_url = "https://accounts.google.com/.well-known/openid-configuration"

   [supabase]
   url = "https://SEU_PROJETO.supabase.co"
   key = "SUA_CHAVE_SUPABASE"
   ```

   Importante: nunca commitar segredos reais no repositório. O arquivo .streamlit/secrets.toml deve ficar local e fora do controle de versão.

5. Inicie a aplicação:

   ```powershell
   streamlit run app.py
   ```

## 6. Estrutura de pastas planejada

```text
.
├── app.py
├── README.md
├── requirements.txt
├── docs/
│   └── requisitos.md
├── openspec/
│   ├── config.yaml
│   ├── changes/
│   └── specs/
├── .streamlit/
│   └── secrets.toml # local, não vai para o GitHub
├── .github/
├── services/
│   └── db.py
├── pages/
├── components/
├── utils/
├── assets/
└── tests/
```

A estrutura pode evoluir durante o desenvolvimento, mas a organização acima representa a base esperada para o projeto.

## 7. Como contribuir usando o fluxo do OpenSpec

O projeto utiliza o fluxo OpenSpec para organizar ideias, requisitos e mudanças.

Fluxo recomendado:

1. Propor uma mudança:

   ```text
   /opsx-propose base-layout
   ```

2. Aplicar a mudança após aprovação e validação:

   ```text
   /opsx-apply
   ```

3. Arquivar a mudança quando estiver concluída:

   ```text
   /opsx-archive
   ```

Regras do projeto:

- citar os IDs de requisito atendidos, como RF01, RF07, RNF04;
- escrever especificações no formato Dado/Quando/Então;
- descrever o que cada perfil vê e o que não vê;
- dividir tarefas em itens pequenos e verificáveis no navegador.

## 8. Equipe e orientador

- Projeto: Portal CPA
- Coordenador de projeto: [NOME]
- Desenvolvedores: [NOME], [NOME], [NOME]
- Orientador: [NOME]
- Faculdade: Faculdade Impacta

