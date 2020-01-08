"""
jwt token 相关
"""
import jwt


def decode_jwt_without_verify(token: str) -> dict:
    return jwt.decode(token, verify=False)
