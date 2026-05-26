# 🚀 Instruções de Deploy: IA que Vende

Este arquivo serve como guia de orquestração para o **Claude Code rodando na VPS** configurar e hospedar esta página de vendas de forma totalmente isolada e segura.

## 📋 Informações de Rede e Servidor
* **IP da VPS**: `212.85.2.130`
* **Domínio**: `aleianegocios.com.br` e `www.aleianegocios.com.br`
* **Usuário na VPS**: `agbotia` (não rodar como root)
* **Diretório de Destino**: `/home/agbotia/web/aleianegocios/ia-que-vende`
* **Proxy Reverso**: Nginx Proxy Manager (NPM) rodando em Docker no `/opt/saas-whatsapp/`

---

## 🛠️ Passos de Deploy para o Claude na VPS

### 1. Preparar o Diretório e Clonar o Repositório
Sob o usuário `agbotia` na VPS:
```bash
# Criar diretórios de estrutura
mkdir -p /home/agbotia/web/aleianegocios/ia-que-vende

# Clonar o repositório (ou puxar atualizações)
git clone <URL_DO_REPOSITORIO_GITHUB> /home/agbotia/web/aleianegocios/ia-que-vende
```

### 2. Configurar o Servidor de Arquivos Estáticos (Isolado)
Para servir a página estática de forma 100% isolada e sem interferir no Nginx do host ou em outros serviços, vamos rodar um container Docker ultraleve com Nginx para ler essa pasta. 

Crie o arquivo `/home/agbotia/web/aleianegocios/ia-que-vende/docker-compose.yml` com a seguinte configuração:
```yaml
version: '3.8'

services:
  nginx_static:
    image: nginx:alpine
    container_name: ia_que_vende_static
    restart: always
    volumes:
      - .:/usr/share/nginx/html:ro
    ports:
      - "127.0.0.1:8085:80"
```
*Nota: A porta `8085` escuta apenas em `127.0.0.1` (localhost), garantindo que ela não fique exposta para a internet pública e respeite a segurança UFW.*

Suba o container:
```bash
docker compose up -d
```

### 3. Configurar o Nginx Proxy Manager (NPM)
Com o container rodando na porta interna `8085`:
1. Faça o túnel SSH para a porta admin do NPM (porta `81`) se necessário, ou acesse a interface web do NPM.
2. Adicione um novo **Proxy Host**:
   * **Domain Names**: `aleianegocios.com.br`, `www.aleianegocios.com.br`
   * **Scheme**: `http`
   * **Forward Host IP**: `172.17.0.1` (ou o IP de gateway do Docker na VPS, para acessar a porta do host a partir do NPM)
   * **Forward Port**: `8085`
   * **Block Common Exploits**: `True`
3. Na aba **SSL**:
   * Selecione **Request a new SSL Certificate** (Let's Encrypt).
   * Marque **Force SSL** e **HTTP/2 Support**.
   * Concorde com os termos e salve.

### 4. Validação
* Execute `curl -I http://localhost:8085` na VPS para certificar-se de que o container está servindo a página localmente.
* Após propagação do DNS, acesse `https://aleianegocios.com.br` e verifique se a página é carregada via HTTPS.

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
