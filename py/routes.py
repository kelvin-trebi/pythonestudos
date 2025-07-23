from fastapi import APIRouter, HTTPException
from models import Usuario, Carteira, RequisicaoTransferencia, TipoUsuario
from database import adicionar_usuario, buscar_usuario_por_email, buscar_usuario_por_cpf, buscar_usuario_por_id, buscar_carteira, atualizar_carteira
import httpx

router = APIRouter()

MODO_TESTE = True  # Altere para False para usar o serviço real

@router.post("/usuarios")
def criar_usuario(usuario: Usuario):
    if buscar_usuario_por_email(usuario.email) or buscar_usuario_por_cpf(usuario.cpf):
        raise HTTPException(status_code=400, detail="Email ou CPF já cadastrado.")
    return adicionar_usuario(usuario)

@router.post("/transferencia")
def transferencia(requisicao: RequisicaoTransferencia):
    pagador = buscar_usuario_por_id(requisicao.pagador)
    recebedor = buscar_usuario_por_id(requisicao.recebedor)
    if not pagador or not recebedor:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")
    if pagador.tipo == TipoUsuario.LOJISTA:
        raise HTTPException(status_code=403, detail="Lojista não pode enviar dinheiro.")
    carteira_pagador = buscar_carteira(pagador.id)
    carteira_recebedor = buscar_carteira(recebedor.id)
    if carteira_pagador.saldo < requisicao.valor:
        raise HTTPException(status_code=400, detail="Saldo insuficiente.")
    if not MODO_TESTE:
        try:
            r = httpx.get("https://util.devi.tools/api/v2/authorize", timeout=10)
            if r.status_code != 200 or r.json().get("message") != "Autorizado":
                raise HTTPException(status_code=403, detail="Transferência não autorizada.")
        except Exception:
            raise HTTPException(status_code=503, detail="Serviço autorizador indisponível.")
    carteira_pagador.saldo -= requisicao.valor
    carteira_recebedor.saldo += requisicao.valor
    try:
        httpx.post("https://util.devi.tools/api/v1/notify", json={"usuario_id": recebedor.id, "valor": requisicao.valor}, timeout=5)
    except Exception:
        pass
    return {"status": "sucesso", "pagador": pagador.id, "recebedor": recebedor.id, "valor": requisicao.valor} 