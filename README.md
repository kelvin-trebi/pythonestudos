# PicPay Simplificado

## Descrição

Este projeto é uma API RESTful desenvolvida em Python com FastAPI, simulando funcionalidades básicas do PicPay, incluindo cadastro de usuários, transferência de valores entre usuários e lojistas, e regras de negócio essenciais para um sistema financeiro simplificado.

## Funcionalidades

- Cadastro de usuários (comum ou lojista), garantindo unicidade de CPF e e-mail.
- Transferência de valores entre usuários, respeitando regras de saldo, tipo de usuário e autorização.
- Notificação de recebimento de pagamento via serviço externo (mock).
- Persistência em memória (ideal para testes e prototipação).
- Endpoints e modelos totalmente em português.

## Regras de Negócio

- Usuários comuns podem enviar e receber dinheiro.
- Lojistas apenas recebem dinheiro.
- Não é permitido transferir se o saldo for insuficiente.
- Antes de transferir, é feita uma consulta a um serviço autorizador externo (pode ser ignorada em modo teste).
- Toda transferência é transacional: em caso de erro, o saldo é revertido.
- Notificações de pagamento são simuladas via serviço externo.
- API totalmente RESTful.

## Endpoints Principais

### Criar Usuário

`POST /usuarios`

Exemplo de payload:
```json
{
  "id": 0,
  "nome_completo": "Maria Teste",
  "cpf": "12345678900",
  "email": "maria@email.com",
  "senha": "senha123",
  "tipo": "comum" // ou "lojista"
}
```

### Realizar Transferência

`POST /transferencia`

Exemplo de payload:
```json
{
  "valor": 100.0,
  "pagador": 1,
  "recebedor": 2
}
```

## Como rodar o projeto

1. Instale as dependências:
   ```
   pip install -r requirements.txt
   pip install httpx
   ```
2. Execute o servidor:
   ```
   uvicorn main:app --reload
   ```
3. Acesse a documentação interativa:
   ```
   http://localhost:8000/docs
   ```

## Observações

- O saldo inicial de cada usuário é de 1000.0 (pode ser alterado em `database.py`).
- O modo de teste ignora a consulta ao serviço autorizador externo para facilitar o desenvolvimento.
- Para produção, altere `MODO_TESTE = False` em `routes.py`. 
