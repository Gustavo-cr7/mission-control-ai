"""Regras de decisão e geração de alertas para o EnviroSat."""

def avaliar(dados):
    """Avalia a telemetria e retorna uma lista de alertas."""
    alertas = []

    if dados["sensor_termico_celsius"] > 80:
        alertas.append({
            "nivel": "CRÍTICO",
            "tipo": "Superaquecimento do sensor térmico",
            "mensagem": "O sensor térmico está acima do limite seguro.",
            "impacto": "A detecção de focos de incêndio pode ficar comprometida."
        })

    if dados["energia_percentual"] < 25:
        alertas.append({
            "nivel": "CRÍTICO",
            "tipo": "Energia baixa",
            "mensagem": "A energia disponível está abaixo do limite recomendado.",
            "impacto": "O satélite pode reduzir coletas de imagens ambientais."
        })

    if dados["buffer_imagens_percentual"] > 90:
        alertas.append({
            "nivel": "ALTO",
            "tipo": "Buffer quase cheio",
            "mensagem": "Muitas imagens ainda não foram transmitidas para a base.",
            "impacto": "Pode haver atraso na análise de desmatamento ou incêndios."
        })

    if dados["precisao_geolocalizacao_metros"] > 15:
        alertas.append({
            "nivel": "MÉDIO",
            "tipo": "Geolocalização imprecisa",
            "mensagem": "A precisão da localização está fora do padrão ideal.",
            "impacto": "Brigadas ambientais podem receber coordenadas menos confiáveis."
        })

    if dados["sensor_optico_status"] != "normal":
        alertas.append({
            "nivel": "MÉDIO",
            "tipo": "Instabilidade no sensor óptico",
            "mensagem": "O sensor óptico apresenta instabilidade ou falha parcial.",
            "impacto": "A qualidade das imagens de vegetação pode ser prejudicada."
        })

    if dados["focos_calor_detectados"] >= 10:
        alertas.append({
            "nivel": "ALTO",
            "tipo": "Muitos focos de calor",
            "mensagem": "O satélite detectou uma quantidade elevada de focos de calor.",
            "impacto": "Pode indicar risco de incêndio ambiental na região monitorada."
        })

    if not alertas:
        alertas.append({
            "nivel": "NORMAL",
            "tipo": "Operação estável",
            "mensagem": "Nenhum parâmetro crítico foi identificado.",
            "impacto": "O monitoramento ambiental segue funcionando normalmente."
        })

    return alertas

def formatar(alertas):
    """Formata os alertas para exibição e envio ao prompt."""
    texto = ""
    for alerta in alertas:
        texto += f"Nível: {alerta['nivel']}\n"
        texto += f"Tipo: {alerta['tipo']}\n"
        texto += f"Mensagem: {alerta['mensagem']}\n"
        texto += f"Impacto terrestre: {alerta['impacto']}\n\n"
    return texto.strip()
