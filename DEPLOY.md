# 🚀 Instruções de Deploy: IA que Vende

Este arquivo serve como guia de orquestração para o **Claude Code rodando na VPS** configurar e hospedar esta página de vendas de forma totalmente isolada, segura e automatizada.

## 📋 Informações de Rede e Servidor
* **IP da VPS**: `212.85.2.130`
* **Domínio**: `aleianegocios.com.br` e `www.aleianegocios.com.br`
* **Usuário na VPS**: `agbotia` (não rodar como root)
* **Diretório de Destino**: `/home/agbotia/web/aleianegocios/ia-que-vende`
* **Proxy Reverso**: Nginx Proxy Manager (NPM) rodando em Docker no `/opt/saas-whatsapp/` (API na porta local 81)

---

## 🛠️ Passos de Deploy para o Claude na VPS

### 1. Clonar o Repositório
Sob o usuário `agbotia` na VPS:
```bash
# Criar diretórios de estrutura
mkdir -p /home/agbotia/web/aleianegocios/ia-que-vende

# Clonar o repositório para o diretório (ou puxar atualizações)
git clone <URL_DO_REPOSITORIO_GITHUB> /home/agbotia/web/aleianegocios/ia-que-vende
cd /home/agbotia/web/aleianegocios/ia-que-vende
```

### 2. Configurar o Servidor de Arquivos Estáticos (Docker Isolado)
Suba o container Nginx estático que servirá o site na porta interna `8085`:
```bash
docker compose up -d
```

### 3. Configurar o Proxy Host no NPM (Automatizado)
Em vez de configurar manualmente no painel, execute o script Python local que fará a integração automática com a API do Nginx Proxy Manager na VPS:
```bash
python3 setup_npm.py
```
*Esse script criará a regra inicial sem SSL para evitar travamento caso o DNS ainda não tenha propagado.*

### 4. Configurar SSL Let's Encrypt (Automatizado)
Após o domínio propagar (verifique via `ping aleianegocios.com.br` ou `nslookup aleianegocios.com.br`), execute o script de automação SSL:
```bash
python3 setup_ssl.py
```
*Esse script solicitará o certificado SSL Let's Encrypt e configurará o Proxy Host do NPM criado para usar HTTPS forçado.*

---

## 🔄 Fluxo de Atualizações Futuras
Quando houver edições no arquivo `index.html` no PC local:
1. Faça commit e push no PC local.
2. Na VPS, execute:
   ```bash
   cd /home/agbotia/web/aleianegocios/ia-que-vende
   git pull
   ```
   *As atualizações serão refletidas instantaneamente sem necessidade de reiniciar o container ou o NPM.*
