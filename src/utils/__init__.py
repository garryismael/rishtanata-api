from fastapi import HTTPException, status


class ApiException:

    def bad_request(self, detail: str):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=detail)

    def unauthorized(self, detail: str):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=detail,
            headers={"WWW-Authenticate": "Bearer"},
        )
