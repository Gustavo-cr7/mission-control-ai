"""Geração de dados simulados da telemetria do EnviroSat."""
import random
from datetime import datetime

def coletar():
    """Simula a coleta de dados atuais do satélite."""
    dados = {
        "missao": "EnviroSat",
        "horario": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "sensor_termico_celsius": random.randint(45, 95),
        "sensor_optico_status": random.choice(["normal", "instavel", "falha parcial"]),
        "buffer_imagens_percentual": random.randint(20, 100),
        "precisao_geolocalizacao_metros": random.randint(3, 25),
        "energia_percentual": random.randint(10, 100),
        "focos_calor_detectados": random.randint(0, 18),
        "area_monitorada": random.choice([
            "Amazônia Legal",
            "Pantanal",
            "Cerrado",
            "Mata Atlântica",
            "Área de Proteção Ambiental"
        ])
    }
    return dados

def formatar(dados):
    """Formata os dados para exibição no terminal."""
    texto = ""
    texto += f"Missão: {dados['missao']}\n"
    texto += f"Horário da coleta: {dados['horario']}\n"
    texto += f"Área monitorada: {dados['area_monitorada']}\n"
    texto += f"Temperatura do sensor térmico: {dados['sensor_termico_celsius']} °C\n"
    texto += f"Sensor óptico: {dados['sensor_optico_status']}\n"
    texto += f"Buffer de imagens: {dados['buffer_imagens_percentual']}%\n"
    texto += f"Precisão de geolocalização: {dados['precisao_geolocalizacao_metros']} metros\n"
    texto += f"Energia disponível: {dados['energia_percentual']}%\n"
    texto += f"Focos de calor detectados: {dados['focos_calor_detectados']}\n"
    return texto
