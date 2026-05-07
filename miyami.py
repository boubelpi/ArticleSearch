import httpx

MIYAMI_URL = "https://websearch.miyami.tech"

async def search(query: str, time_range: str = None, rerank: bool = False):
    async with httpx.AsyncClient(timeout=120.0) as client:
        params = {"query": query, "rerank": rerank}
        if time_range:
            params["time_range"] = time_range
        response = await client.get(f"{MIYAMI_URL}/search-api", params=params)
        return response.json()


async def fetch(url: str, format: str = "markdown", steal_mode: str = "off"):
    async with httpx.AsyncClient(timeout=120.0) as client:
        params = {"url": url, "format": format, "steal_mode": steal_mode}
        response = await(client.get(f"{MIYAMI_URL}/fetch",  params=params))
        return response.json()