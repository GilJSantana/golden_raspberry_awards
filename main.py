'''
Este modulo usa o servidor de aplicação Uvicorn para executar a API FastAPI.
Ele importa o aplicativo FastAPI do modulo api e o executa na porta 8000.
Ele possui as seguintes funcoes:
1. Importa o aplicativo FastAPI do modulo api.
Parametros:
    app: Aplicativo FastAPI.
'''

import uvicorn

if __name__ == '__main__':
    uvicorn.run('api:app', host='127.0.0.1', port=8000, reload=True)
