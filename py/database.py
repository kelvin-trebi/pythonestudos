from typing import Dict, Optional
from models import Usuario, Carteira

usuarios: Dict[int, Usuario] = {}
carteiras: Dict[int, Carteira] = {}

indice_email: Dict[str, int] = {}
indice_cpf: Dict[str, int] = {}

usuario_id_seq = 1

def adicionar_usuario(usuario: Usuario):
    global usuario_id_seq
    usuario.id = usuario_id_seq
    usuarios[usuario.id] = usuario
    indice_email[usuario.email] = usuario.id
    indice_cpf[usuario.cpf] = usuario.id
    carteiras[usuario.id] = Carteira(usuario_id=usuario.id, saldo=1000.0)
    usuario_id_seq += 1
    return usuario

def buscar_usuario_por_id(usuario_id: int) -> Optional[Usuario]:
    return usuarios.get(usuario_id)

def buscar_usuario_por_email(email: str) -> Optional[Usuario]:
    usuario_id = indice_email.get(email)
    return usuarios.get(usuario_id) if usuario_id else None

def buscar_usuario_por_cpf(cpf: str) -> Optional[Usuario]:
    usuario_id = indice_cpf.get(cpf)
    return usuarios.get(usuario_id) if usuario_id else None

def buscar_carteira(usuario_id: int) -> Optional[Carteira]:
    return carteiras.get(usuario_id)

def atualizar_carteira(usuario_id: int, saldo: float):
    if usuario_id in carteiras:
        carteiras[usuario_id].saldo = saldo 