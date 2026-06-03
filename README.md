# Mission Control AI — EnviroSat

Projeto da Global Solution 2026.1 — FIAP.

## Trilha escolhida
EnviroSat — Observação Ambiental.

## Proposta
O sistema simula o monitoramento de um satélite ambiental capaz de acompanhar focos de calor, desmatamento e áreas protegidas. A aplicação gera telemetria simulada, avalia alertas por regras em Python e usa IA generativa via Ollama Cloud para explicar o estado da missão em linguagem natural.

## Impacto terrestre
O EnviroSat ajuda órgãos ambientais, brigadas de incêndio e analistas de compliance ambiental a receberem informações sobre riscos ambientais. Quando sensores, energia ou transmissão falham, o impacto pode chegar diretamente ao combate a incêndios, fiscalização de desmatamento e proteção de comunidades.

## Como executar

```bash
pip install -r requirements.txt
cp .env.example .env
python main.py
```

No arquivo `.env`, adicione sua chave:

```bash
OLLAMA_API_KEY=sua_chave_aqui
```

## Comandos da CLI

- `/help` — mostra comandos
- `/status` — mostra telemetria atual
- `/about` — explica o projeto
- `/clear` — limpa a tela
- `/exit` — encerra

## Arquivos principais

- `src/telemetria.py` — gera dados simulados
- `src/alertas.py` — avalia riscos e criticidade
- `src/engine.py` — conecta telemetria, alertas e IA
- `src/ui.py` — interface CLI
- `prompts/system_prompt.md` — instruções da IA
