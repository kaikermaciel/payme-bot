# Payme Bot (Cobrança Automática)

Este projeto é uma automação em **Python** para gerenciar a cobrança mensal do plano **Spotify Família** que pode ser facilmente adaptado para qualquer tipo de cobrança da sua preferência. Ele roda na nuvem via **GitHub Actions**, enviando e-mails automáticos com os dados do Pix para os membros do plano todo dia 05 de cada mês.

A lista de assinantes é mantida segura através de **Variáveis de Ambiente (Secrets)**, garantindo que nomes e e-mails não fiquem expostos no código público.

---

## Funcionalidades

* **Envio Agendado:** Dispara os e-mails automaticamente no dia **05 de todo mês** (configurável via Cron).
* **Segurança:** A lista de e-mails e nomes não fica no código fonte.
* **E-mails HTML:** Envia lembretes formatados com valor, chave Pix e nome do titular.
* **Serverless:** Roda gratuitamente no GitHub Actions.

---

## Tecnologias Utilizadas

* **Python 3.x**
* **GitHub Actions** (Automação/Cron)
* **SMTP Lib** (Envio de E-mails)
* **JSON** (Manipulação da lista de assinantes)

---

## Configuração Local

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/spotify-bot.git](https://github.com/seu-usuario/spotify-bot.git)
    cd spotify-bot
    ```

2.  **Crie um ambiente virtual e instale as dependências:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    # venv\Scripts\activate   # Windows
    
    pip install -r requirements.txt
    ```

3.  **Configure as Variáveis de Ambiente (.env):**
    Crie um arquivo `.env` na raiz com o seguinte conteúdo.
    **Atenção:** A lista deve estar em formato JSON, toda na mesma linha e envolta por aspas simples (`'`).

    ```env
    EMAIL_USER=seu_email@gmail.com
    EMAIL_PASSWORD=sua_senha_de_app_google
    LISTA_ASSINANTES='[{"nome": "Nome 1", "email": "email1@teste.com"}, {"nome": "Nome 2", "email": "email2@teste.com"}]'
    ```

4.  **Edite os Dados de Pagamento:**
    No arquivo `script.py`, atualize as variáveis `CHAVE_PIX`, `NOME_TITULAR` e `VALOR_INDIVIDUAL`.

5.  **Teste Localmente:**
    ```bash
    python script.py
    ```

---

## Configuração no GitHub

Para rodar automaticamente sem expor seus dados:

1.  Vá na aba **Settings** > **Secrets and variables** > **Actions** do seu repositório.
2.  Adicione as seguintes *Repository Secrets*:

    * `EMAIL_USER`: Seu e-mail do Gmail.
    * `EMAIL_PASSWORD`: Sua Senha de App Google.
    * `LISTA_ASSINANTES`: A lista de pessoas em formato JSON puro (sem aspas simples em volta aqui, apenas o JSON):
        ```json
        [
          {"nome": "Primo João", "email": "joao@gmail.com"},
          {"nome": "Tia Maria", "email": "maria@hotmail.com"}
        ]
        ```

3.  O Workflow está configurado em `.github/workflows/build.yml` para rodar todo dia 05 às **09:00 AM (Horário de Manaus)**.

---

## Estrutura do Projeto

```text
.
├── .github/
│   └── workflows/
│       └── build.yml  # Configuração do Cron Job
├── script.py            # Lógica principal (Lê JSON da env)
├── requirements.txt     # Dependências (python-dotenv)
├── .env                 # Variáveis locais (Ignorado pelo Git)
└── README.md            # Documentação
