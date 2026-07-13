from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Meu Primeiro MCP")


@mcp.tool()
def say_hello(name: str) -> str:
    """Cumprimenta um utilizador."""
    return f"Olá {name}! Seja bem-vindo ao seu primeiro MCP."


@mcp.tool()
def calcular_frete(
    peso: float,
    distancia: int,
    expresso: bool
) -> float:
    """Calcula o valor do frete."""

    valor = peso * 2 + distancia * 0.5

    if expresso:
        valor *= 1.5

    return round(valor, 2)


if __name__ == "__main__":
    mcp.run()