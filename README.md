# Mission Control AI - Global Solution 2026.1

## Trilha: EnviroSat - Observação Ambiental

## Integrantes

- Gustavo de Souza Correa RM-570746
- Arthur Tae Gun Yong RM-570647 

## Disciplina

Prompt Engineering and Artificial Intelligence

## Objetivo do Projeto

Este projeto simula um sistema de centro de controle para um satélite de observação ambiental. O sistema gera dados simulados de telemetria, identifica situações críticas utilizando regras desenvolvidas em Python e utiliza Inteligência Artificial Generativa por meio da Ollama Cloud para interpretar os dados e apresentar análises em linguagem natural.

## Problema Resolvido

O EnviroSat monitora áreas ambientais e auxilia na detecção de focos de calor, monitoramento de vegetação e identificação de riscos relacionados a incêndios e desmatamento. O objetivo é fornecer informações que possam apoiar equipes responsáveis pela preservação ambiental e resposta a emergências.

## Persona Atendida

- Operador de centro de controle ambiental
- Coordenador de brigada de combate a incêndio
- Analista de compliance ambiental

## Funcionalidades

- Geração de telemetria simulada
- Monitoramento de sensores ambientais
- Detecção automática de alertas
- Avaliação de riscos operacionais
- Análise contextualizada utilizando IA generativa
- Explicação do impacto terrestre das anomalias detectadas
- Interface CLI inspirada em sistemas de Mission Control

## Tecnologias Utilizadas

- Python
- Ollama Cloud
- Rich
- prompt-toolkit
- PyFiglet
- python-dotenv

## Estrutura do Projeto

mission-control-ai/

├── README.md

├── main.py

├── banner_ascii.py

├── requirements.txt

├── .env.example

├── .gitignore

├── src/

│ ├── __init__.py

│ ├── ui.py

│ ├── engine.py

│ ├── telemetria.py

│ └── alertas.py

├── prompts/

│ └── system_prompt.md

├── data/

└── assets/

## Como Executar

### 1. Instalar as dependências

pip install -r requirements.txt

### 2. Criar o arquivo .env

OLLAMA_API_KEY=sua_chave_aqui_sem_aspas

### 3. Executar o sistema

python main.py

## Comandos da CLI

- /help - mostra os comandos disponíveis
- /status - exibe a telemetria atual
- /about - apresenta informações do projeto
- /clear - limpa a tela do terminal
- /exit - encerra o sistema

## Funcionamento

O sistema coleta dados simulados do satélite EnviroSat, incluindo:

- Temperatura do sensor térmico
- Energia disponível
- Buffer de imagens
- Precisão de geolocalização
- Quantidade de focos de calor detectados

Após a coleta, regras implementadas em Python analisam os dados e identificam possíveis alertas. Em seguida, a IA recebe a telemetria, os alertas e a pergunta realizada pelo usuário para gerar uma resposta contextualizada sobre o estado da missão.

## Impacto Terrestre

Quando o satélite apresenta falhas operacionais, o monitoramento ambiental pode ser comprometido. Isso pode causar atrasos na detecção de incêndios, dificultar ações de combate ao desmatamento e reduzir a eficiência das equipes ambientais que atuam em campo.

## Conclusão

O projeto Mission Control AI - EnviroSat demonstra a aplicação da Inteligência Artificial Generativa no monitoramento de missões espaciais voltadas à observação ambiental.

A solução integra telemetria simulada, regras de decisão em Python e análise por IA para auxiliar operadores na identificação de riscos operacionais e seus impactos no combate a incêndios, monitoramento ambiental e preservação de áreas protegidas.