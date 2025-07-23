from pydantic import BaseModel, EmailStr
from typing import Optional

class TipoUsuario:
    COMUM = "comum"
    LOJISTA = "lojista"

class Usuario(BaseModel):
    id: int
    nome_completo: str
    cpf: str
    email: EmailStr
    senha: str
    tipo: str  # 'comum' ou 'lojista'

class Carteira(BaseModel):
    usuario_id: int
    saldo: float = 0.0

class RequisicaoTransferencia(BaseModel):
    valor: float
    pagador: int
    recebedor: int 