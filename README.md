# 📊 Steam Games Exporter

Este projeto é um script em **Python** que coleta todos os jogos da sua
biblioteca Steam e exporta as informações para uma planilha do **Excel
(.xlsx)**.\
O objetivo é facilitar a visualização de dados como **nome dos jogos,
horas jogadas e porcentagem de conquistas**.

------------------------------------------------------------------------

## 🚀 Funcionalidades

-   Exporta **todos os jogos** da conta Steam (mesmo os que não possuem
    conquistas).\
-   Mostra:
    -   Nome do jogo 🎮\
    -   Horas jogadas ⏱️\
    -   \% de conquistas desbloqueadas 🏆\
-   Trata erros de jogos sem conquistas ou falhas na API.\
-   Gera uma planilha `jogos_steam.xlsx` pronta para abrir no Excel.

------------------------------------------------------------------------

## 🛠️ Tecnologias Utilizadas

-   **Python 3.11+**
-   **Requests** → para fazer chamadas à API da Steam.\
-   **OpenPyXL** → para gerar a planilha Excel.

------------------------------------------------------------------------

## 📋 Pré-requisitos

1.  Ter o **Python 3** instalado.\

2.  Instalar as dependências com:

    ``` bash
    pip install requests openpyxl
    ```

3.  Ter uma **Steam API Key** válida:

    -   Acesse: <https://steamcommunity.com/dev/apikey>\
    -   Copie sua chave.\

4.  Saber seu **SteamID64**:

    -   Descubra em: <https://steamid.io>.

------------------------------------------------------------------------

## ⚙️ Como Usar

1.  Clone ou copie o código deste repositório.\

2.  Abra o arquivo `steam_games.py` e coloque sua **API Key** e
    **SteamID64**:

    ``` python
    STEAM_API_KEY = "SUA_API_KEY"
    STEAM_ID = "SEU_STEAM_ID64"
    ```

3.  Execute o script no terminal:

    ``` bash
    python steam_games.py
    ```

4.  Ao finalizar, será gerado o arquivo:

        jogos_steam.xlsx

    localizado na mesma pasta do script.

------------------------------------------------------------------------

## 📊 Estrutura da Planilha

A planilha contém as seguintes colunas:

  Nome do Jogo          Horas Jogadas   \% de Conquistas
  --------------------- --------------- ------------------
  Counter-Strike 2      120.5           35.00%
  Dota 2                15.0            0.00%
  Jogo sem conquistas   2.5             0.00%
  Jogo com erro         0.0             Erro

------------------------------------------------------------------------

## ⚠️ Possíveis Problemas

-   **Perfil privado**: Se os "detalhes do jogo" da Steam estiverem
    privados, a API não retorna dados.
    -   Vá em: **Configurações → Privacidade → Detalhes do jogo →
        Público**.\
-   **API Key inválida**: Confirme que colou a chave corretamente.\
-   **Planilha vazia**: Pode indicar que o perfil está privado ou que
    houve erro na chamada da API.

------------------------------------------------------------------------

## 📌 Melhorias Futuras

-   Adicionar ícones e imagens dos jogos.\
-   Exportar para outros formatos (CSV, JSON).\
-   Interface gráfica para facilitar o uso.

------------------------------------------------------------------------

## 👨‍💻 Autor

Projeto desenvolvido por **Gilvan Pedro**, 2025.\
Facilitando o gerenciamento de bibliotecas Steam via Python 🚀
