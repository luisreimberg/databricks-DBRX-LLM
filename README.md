# Chatbot-RAG-DBRX 🤖
![image](https://github.com/luisreimberg/databricks-DBRX-LLM/assets/94421216/1c6c218f-a32a-4292-8463-ad0b50f34540)

# Objetivo
O objetivo deste projeto é realizar a criação de um chatbot baseado em RAG conectado no LLM do DBRX (Databricks). 

🤔 — Beleza... Mas o que é RAG?

🤠 — Retrieval-Augmented Generation (RAG) é o processo de otimizar a saída de um grande modelo de linguagem, de forma que ele faça referência a uma base de conhecimento confiável fora das suas fontes de dados de treinamento antes de gerar uma resposta.

🤔 — Certo. Acho que entendi o que é RAG... E o que é LLM?

🤠 — LLM ou Large Language Models são modelos de inteligência artificial que utilizam técnicas de machine learning (ML) para entender e gerar linguagem humana. Como por exemplo, o Chat GPT ou o Bard.

🤔 — Nossa, que legal! Na vida real, como isso pode ajudar uma empresa?

🤠 — Existem diversas aplicações. Alguns exemplos do que é possível fazer: sintetizar prontuários de pacientes, identificação de palavras chave em exames, estruturar o texto de contratos em pdf e resumir cláusulas, etc.


# Sobre o projeto

Temos um arquivo de texto (texts.txt) onde está armazenado dados fictícios da empresa LGBR Pharma e seu fundador Luis Reimberg. 

A imagem abaixo representa o funcionamento do projeto:

![image](https://github.com/luisreimberg/databricks-DBRX-LLM/assets/94421216/a2920c55-68b1-4b96-a8eb-9f69248756cf)


Na pasta "codes_langchain" temos o script em Python que vai realizar a ingestão dos dados no Pinecone. Nesse arquivo também realizamos um teste utilizando o DBRX para verificar se a ingestão foi realizada com sucesso.

Na pasta "chatbot", em app.py, ocorre a integração entre o modelo DBRX com o chatbot.

# Demonstração do funcionamento

![Captura de tela de 2024-04-28 02-27-59](https://github.com/luisreimberg/databricks-DBRX-LLM/assets/94421216/b2a2f156-ddce-4eb8-966b-fc4ab2abaedc)







