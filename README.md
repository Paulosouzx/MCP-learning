# Meu Primeiro MCP

Projeto desenvolvido durante meus estudos sobre o Model Context Protocol (MCP).

## Pré-requisitos

- Python 3.11+
- Node.js (necessário para o MCP Inspector)

## Instalação

Clone o projeto:

```bash
git clone <url-do-repositorio>
cd MCP
```

Crie o ambiente virtual:

```bash
python3 -m venv .venv
```

Ative o ambiente:

```bash
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install "mcp[cli]"
```

## Executando

Inicie o MCP Inspector:

```bash
mcp dev server.py
```

Depois abra a URL informada no terminal e clique em **Connect**.

## Estrutura atual

```
.
├── server.py
└── .venv/
```

## Funcionalidades implementadas

- ✅ Servidor MCP
- ✅ Tool `say_hello`

## Próximos passos

- [ ] Schemas e validação
- [ ] Resources
- [ ] Prompts
- [ ] Tratamento de erros
