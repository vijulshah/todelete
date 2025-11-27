from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend
from fastapi_cache.decorator import cache

@app.on_event("startup")
async def startup():
    FastAPICache.init(InMemoryBackend(), prefix="fastapi-cache")

@app.get("/items/{item_id}", response_model=APIResponse[ItemOut])
@api_envelope
@cache(expire=60)
async def get_item(item_id: int, response: Response):
    return ItemOut(id=item_id, title="Bar")
