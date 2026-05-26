#!/usr/bin/env python3
import urllib.request
import json
import sys

BASE = "http://localhost:81/api"

# 1. Login no NPM
login_data = json.dumps({"identity": "alefnandes@gmail.com", "secret": "M&upriB0t26"}).encode()
req = urllib.request.Request(f"{BASE}/tokens", data=login_data, headers={"Content-Type": "application/json"})
try:
    with urllib.request.urlopen(req) as r:
        token_resp = json.loads(r.read())
        token = token_resp.get("token")
        if not token:
            print(f"ERRO login: {token_resp}")
            sys.exit(1)
        print("LOGIN NPM OK")
except Exception as e:
    print(f"ERRO ao fazer login no NPM: {e}")
    sys.exit(1)

headers = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}

# 2. Criar NOVO proxy host aleianegocios.com.br -> 172.17.0.1:8085
payload = {
    "domain_names": ["aleianegocios.com.br", "www.aleianegocios.com.br"],
    "forward_scheme": "http",
    "forward_host": "172.17.0.1",  # Gateway docker
    "forward_port": 8085,
    "access_list_id": "0",
    "certificate_id": 0,
    "ssl_forced": False,
    "caching_enabled": False,
    "block_exploits": True,
    "advanced_config": "",
    "meta": {"letsencrypt_agree": False, "dns_challenge": False},
    "allow_websocket_upgrade": False,
    "http2_support": True,
    "hsts_enabled": False,
    "hsts_subdomains": False
}

req = urllib.request.Request(
    f"{BASE}/nginx/proxy-hosts",
    data=json.dumps(payload).encode(),
    headers=headers,
    method="POST"
)
try:
    with urllib.request.urlopen(req) as r:
        result = json.loads(r.read())
        new_id = result.get("id")
        print(f"\nNOVO PROXY HOST CRIADO COM SUCESSO:")
        print(f"  ID: {new_id}")
        print(f"  Dominios: {result.get('domain_names')}")
        print(f"  Forward: {result.get('forward_host')}:{result.get('forward_port')}")
        print(f"  Status: {'Ativo' if result.get('enabled') else 'Inativo'}")
        
        # Salva o ID criado para o script de SSL poder usar
        with open("proxy_host_id.txt", "w") as f:
            f.write(str(new_id))
            
except Exception as e:
    print(f"ERRO ao criar proxy host: {e}")
    sys.exit(1)

print("\nConfiguração inicial de Proxy concluída!")
