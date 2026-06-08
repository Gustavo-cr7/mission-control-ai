"""Motor de análise da Mission Control AI."""
import os
from ollama import Client
from dotenv import load_dotenv
from pathlib import Path
from src.telemetria import coletar, formatar as formatar_telemetria
from src.alertas import avaliar, formatar as formatar_alertas

load_dotenv()

TRILHA = "envirosat"

client = Client(
    host="https://ollama.com",
    headers={'Authorization': 'Bearer ' + os.environ.get('OLLAMA_API_KEY', '')}
)

def llm(prompt, system=None, max_tokens=800, temperature=0.3):
    """Envia prompt ao gpt-oss:120b via Ollama Cloud."""
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})

    try:
        return client.chat(
            model="gpt-oss:120b",
            messages=messages,
            options={"num_predict": max_tokens, "temperature": temperature},
            stream=False
        )['message']['content'].strip()
    except Exception as e:
        return f"⚠️ Erro ao consultar IA: {e}"

def load_system_prompt():
    """Lê o system prompt do arquivo prompts/system_prompt.md"""
    path = Path("prompts/system_prompt.md")
    if path.exists():
        return path.read_text(encoding="utf-8")
    return "Você é um assistente de missão espacial."

class MissionEngine:
    """Motor de análise da missão EnviroSat."""

    def __init__(self):
        self.trilha = TRILHA
        self.system_prompt = load_system_prompt()

    def is_ready(self):
        return True

    def status_snapshot(self):
        """Retorna texto resumindo o estado atual da telemetria."""
        dados = coletar()
        alertas = avaliar(dados)

        resposta = "STATUS ATUAL DA MISSÃO ENVIROSAT\n\n"
        resposta += formatar_telemetria(dados)
        resposta += "\nALERTAS IDENTIFICADOS:\n"
        resposta += formatar_alertas(alertas)

        return resposta

    def analyze(self, pergunta_usuario):
        """Analisa a pergunta com base na telemetria, alertas e IA."""
        dados = coletar()
        alertas = avaliar(dados)

        prompt = f"""
Você recebeu uma pergunta do operador da missão EnviroSat.

PERGUNTA DO USUÁRIO:
{pergunta_usuario}

TELEMETRIA ATUAL:
{formatar_telemetria(dados)}

ALERTAS GERADOS PELO CÓDIGO PYTHON:
{formatar_alertas(alertas)}

Responda como um assistente de centro de controle espacial.
Explique o estado da missão, os riscos encontrados, a ação recomendada
e o impacto terrestre para sustentabilidade, combate a incêndios e monitoramento ambiental.
Use linguagem clara, objetiva e parecida com a de um aluno explicando o projeto.
"""
        return llm(prompt, system=self.system_prompt)
