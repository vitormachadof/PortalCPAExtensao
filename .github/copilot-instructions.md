# Portal CPA — instruções para o Copilot

- Projeto de extensão da Faculdade Impacta: portal da CPA em Python 3.14 + Streamlit.
- Responda e comente o código em português do Brasil.
- Interface só com Streamlit (st.navigation, st.columns, st.tabs, st.container).
- Login com st.login (Google). Perfis: visitante, aluno, coordenador, avaliador externo, admin CPA.
- Banco e arquivos no Supabase via supabase-py, com acesso centralizado em services/db.py.
- NÃO crie tabelas nem scripts SQL: o banco é modelado pelo Vitor.
- Nunca escreva chaves ou senhas no código; use st.secrets.
- Siga as specs em openspec/specs e a mudança ativa em openspec/changes.
- Prefira código simples e comentado, que um aluno consiga explicar.