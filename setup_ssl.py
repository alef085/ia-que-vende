#!/usr/bin/env python3
import urllib.request
import urllib.error
import json
import sys
import os

BASE = "http://localhost:81/api"

# 1. Obter o ID do proxy host
if not os.path.exists("proxy_host_id.txt"):
    print("ERRO: Arquivo proxy_host_id.txt não encontrado. Execute o setup_npm.py primeiro.")
    sys.exit(1)

with open("proxy_host_id.txt", "r") as f:
    proxy_host_id = f.read().strip()

print(f"Configurando SSL para o Proxy Host ID: {proxy_host_id}")

# 2. Login no NPM
login_data = json.dumps({"identity": "alefnandes@gmail.com", "secret": "M&upriB0t26"}).encode()
req = urllib.request.Request(f"{BASE}/tokens", data=login_data, headers={"Content-Type": "application/json"})
try:
    with urllib.request.urlopen(req) as r:
        token = json.loads(r.read())["token"]
        print("LOGIN NPM OK")
except Exception as e:
    print(f"ERRO ao fazer login no NPM: {e}")
    sys.exit(1)

headers = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}

# 3. Solicitar Certificado Let's Encrypt para o domínio
# Tentativas com estruturas de payload diferentes que o NPM suporta
payloads = [
    {"provider": "letsencrypt", "domain_names": ["aleianegocios.com.br", "www.aleianegocios.com.br"], "meta": {"letsencrypt_agree": True, "letsencrypt_email": "alefnandes@gmail.com"}},
    {"provider": "letsencrypt", "domain_names": ["aleianegocios.com.br", "www.aleianegocios.com.br"], "meta": {"nginx_online": True, "nginx_err": None}},
    {"provider": "letsencrypt", "domain_names": ["aleianegocios.com.br", "www.aleianegocios.com.br"]}
]

cert_id = None
for i, payload in enumerate(payloads, 1):
    print(f"\nTentativa {i} de solicitar SSL Let's Encrypt...")
    req = urllib.request.Request(
        f"{BASE}/nginx/certificates",
        data=json.dumps(payload).encode(),
        headers=headers,
        method="POST"
    )
    try:
        # A geração de certificado SSL Let's Encrypt pode levar tempo (timeout estendido)
        with urllib.request.urlopen(req, timeout=180) as r:
            result = json.loads(r.read())
            cert_id = result.get("id")
            print(f"SUCESSO SSL! Certificado ID: {cert_id} | Domínios: {result.get('domain_names')} | Expira em: {result.get('expires_on')}")
            break
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        print(f"  Falha na tentativa {i} (HTTP {e.code}): {body[:300]}")
    except Exception as e:
        print(f"  Falha na tentativa {i}: {e}")

if not cert_id:
    print("\nERRO: Não foi possível emitir o certificado SSL após as tentativas.")
    print("Certifique-se de que a propagação de DNS do domínio já concluiu e aponta para o IP da VPS.")
    sys.exit(1)

# 4. Atualizar o Proxy Host para forçar SSL
print(f"\nAtualizando Proxy Host {proxy_host_id} com o Certificado SSL...")
ssl_payload = {
    "domain_names": ["aleianegocios.com.br", "www.aleianegocios.com.br"],
    "forward_scheme": "http",
    "forward_host": "172.17.0.1",
    "forward_port": 8085,
    "access_list_id": "0",
    "certificate_id": cert_id,
    "ssl_forced": True,
    "caching_enabled": False,
    "block_exploits": True,
    "advanced_config": "",
    "meta": {"nginx_online": True, "nginx_err": None},
    "allow_websocket_upgrade": False,
    "http2_support": True,
    "hsts_enabled": True,
    "hsts_subdomains": False
}

req_update = urllib.request.Request(
    f"{BASE}/nginx/proxy-hosts/{proxy_host_id}",
    data=json.dumps(ssl_payload).encode(),
    headers=headers,
    method="PUT"
)

try:
    with urllib.request.urlopen(req_update) as r2:
        r2_data = json.loads(r2.read())
        print(f"\n>>> CONFIGURAÇÃO SSL CONCLUÍDA! <<<")
        print(f"  SSL Forçado: {r2_data.get('ssl_forced')}")
        print(f"  Certificado Ativo: {r2_data.get('certificate_id')}")
        print(f"\nDomínio publicado com HTTPS: https://aleianegocios.com.br")
except Exception as e:
    print(f"ERRO ao vincular certificado ao proxy host: {e}")
    sys.exit(1)
