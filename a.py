def api_envelope(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            data = await func(*args, **kwargs)
            if isinstance(data, APIResponse):
                return data
            return APIResponse(success=True, message="ok", data=data)
        except HTTPException:
            # Let global handler deal with it
            raise
        except Exception as e:
            # Convert unexpected errors into a standard response
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error",
            ) from e
    return wrapper
