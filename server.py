from fastmcp import FastMCP

mcp = FastMCP("MCP Server")

@mcp.tool
def add(a: int, b: int) -> int:
    """두 숫자의 합을 반환합니다."""
    return a + b

@mcp.tool
def multiply(a: int, b: int) -> int:
    """두 숫자의 곱을 반환합니다."""
    return a * b

@mcp.tool
def subtract(a: int, b: int) -> int:
    """두 숫자의 차를 반환합니다."""
    return a - b

@mcp.tool
def divide(a: int, b: int) -> float:
    """두 숫자의 나눗셈 결과를 반환합니다."""
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다.")
    return a / b

if __name__ == "__main__":
    import os
    port = int(os.getenv("PORT", 8001))
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=port,
        path="/mcp",
    )