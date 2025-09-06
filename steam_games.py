import requests
import openpyxl

# Sua API Key e Steam ID
STEAM_API_KEY = "STEAM API KEY"
STEAM_ID = "STEAM ID"

# URLs da Steam API
OWNED_GAMES_URL = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/"
ACHIEVEMENTS_URL = "https://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v1/"
GAME_SCHEMA_URL = "https://api.steampowered.com/ISteamUserStats/GetSchemaForGame/v2/"

# 1. Buscar todos os jogos da conta
params = {
    "key": STEAM_API_KEY,
    "steamid": STEAM_ID,
    "include_appinfo": True  # retorna nomes dos jogos
}
response = requests.get(OWNED_GAMES_URL, params=params)

print("Status da requisição:", response.status_code)  # Debug
print("Resposta bruta (primeiros 500 caracteres):")
print(response.text[:500])  # Mostra resposta parcial

# Verifica se deu erro
if response.status_code != 200:
    print("❌ Erro ao acessar a Steam API. Verifique sua chave API e conexão.")
    exit()

try:
    games_data = response.json().get("response", {}).get("games", [])
except Exception as e:
    print("❌ Não consegui converter a resposta em JSON. Verifique se o perfil está público.")
    print("Erro:", e)
    exit()

if not games_data:
    print("⚠️ Nenhum jogo encontrado! Seu perfil pode estar privado.")
    exit()

# Criar planilha
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "Jogos Steam"
sheet.append(["Nome do Jogo", "% de Conquistas"])

# 2. Iterar pelos jogos
for game in games_data:
    appid = game["appid"]
    name = game["name"]
    print(f"🔎 Processando: {name}")  # Debug

    percent = 0
    try:
        # 3. Buscar conquistas desbloqueadas
        achievements_params = {
            "key": STEAM_API_KEY,
            "steamid": STEAM_ID,
            "appid": appid
        }
        achievements_response = requests.get(ACHIEVEMENTS_URL, params=achievements_params).json()

        # 4. Buscar total de conquistas do jogo
        schema_params = {
            "key": STEAM_API_KEY,
            "appid": appid
        }
        schema_response = requests.get(GAME_SCHEMA_URL, params=schema_params).json()

        if "playerstats" in achievements_response and "achievements" in achievements_response["playerstats"]:
            unlocked = sum(1 for a in achievements_response["playerstats"]["achievements"] if a["achieved"] == 1)
            total = len(schema_response.get("game", {}).get("availableGameStats", {}).get("achievements", []))
            percent = (unlocked / total * 100) if total > 0 else 0
    except Exception as e:
        print(f"⚠️ Erro ao processar {name}: {e}")

    # 5. Salvar na planilha
    sheet.append([name, f"{percent:.2f}%"])

# Salvar arquivo Excel
workbook.save("jogos_steam.xlsx")
print("✅ Planilha salva como jogos_steam.xlsx")
