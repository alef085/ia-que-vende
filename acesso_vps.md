# 🔑 Credenciais e Instruções de Acesso: VPS e Deploy Isolado

Este documento reúne todas as credenciais de acesso, caminhos de chaves e diretrizes arquiteturais necessárias para configurar, rodar e realizar o deploy de novos projetos estáticos na nossa VPS de forma 100% isolada.

---

## 🖥️ 1. Acesso SSH à VPS

*   **IP do Servidor**: `212.85.2.130`
*   **Usuários**:
    *   `root` (para configurações globais e do sistema)
    *   `agbotia` (para deploy da aplicação e arquivos web)
*   **Autenticação**: Chave privada SSH localizada localmente no computador do usuário no caminho:
    `C:\Users\Paulo Aleixo\.ssh\agbotia_vps`
*   **Comandos de Conexão (Terminal Local)**:
    *   Conectar diretamente como usuário do site:
        ```bash
        ssh -i "C:\Users\Paulo Aleixo\.ssh\agbotia_vps" agbotia@212.85.2.130
        ```
    *   Como a configuração SSH local no arquivo `~/.ssh/config` já mapeia esse Host com o usuário root e a chave associada, você também pode conectar rodando simplesmente:
        ```bash
        ssh agbotia
        ```

---

## 🔀 2. Nginx Proxy Manager (NPM)

O NPM gerencia os direcionamentos de domínios (Proxy Hosts) e a emissão de certificados SSL (Let's Encrypt). Ele roda em Docker na VPS (no diretório `/opt/saas-whatsapp/`) e a sua API/Interface roda internamente na porta `81`.

*   **URL da API local (NPM)**: `http://localhost:81`
*   **Credenciais de Acesso (Administrador)**:
    *   **E-mail (Identity)**: `alefnandes@gmail.com`
    *   **Senha (Secret)**: `M&upriB0t26`

---

## 🛠️ 3. Guia de Arquitetura para Projetos Isolados

Para manter cada novo projeto completamente isolado e seguro das outras aplicações na VPS, siga o seguinte padrão de configuração:

### Passo 1: Criar a Estrutura de Pastas na VPS
Logado na VPS com o usuário `agbotia`, crie a pasta correspondente ao novo projeto no diretório `/home/agbotia/web/`:
```bash
mkdir -p /home/agbotia/web/nome-do-novo-projeto
```

### Passo 2: Configurar o Docker Compose Isolado
Na pasta do novo projeto na VPS, crie um arquivo `docker-compose.yml` servindo o site estático através de uma porta dedicada que esteja livre no sistema (ex: `8086`, `8087`... O site da Dra. Luciana usa a `8085`):
```yaml
version: '3.8'
services:
  web:
    image: nginx:alpine
    container_name: novo-projeto-nginx
    restart: always
    ports:
      - "8086:80"  # Substitua a porta 8086 por uma porta livre na VPS
    volumes:
      - ./public:/usr/share/nginx/html  # Pasta onde estarão os arquivos do novo site (index.html, etc.)
```

### Passo 3: Configurar o Proxy Host no NPM
Acesse o painel do NPM e adicione um novo **Proxy Host**:
*   **Domain Names**: `seudominio.com.br` e `www.seudominio.com.br`
*   **Scheme**: `http`
*   **Forward Host**: `172.17.0.1` (IP gateway do Docker na VPS)
*   **Forward Port**: `8086` (A porta que você mapeou no docker-compose)
*   **Block Exploits**: Habilitado (Recomendado)

### Passo 4: Emitir SSL (Let's Encrypt)
Assim que o DNS do novo domínio estiver propagado e apontando para o IP da VPS (`212.85.2.130`):
1.  Edite o Proxy Host criado no painel do NPM.
2.  Acesse a aba **SSL**.
3.  Selecione **Request a new SSL Certificate** com Let's Encrypt.
4.  Habilite **Force SSL** (HTTPS Forçado) e **HTTP/2 Support**.
5.  Salve as configurações.

### Passo 5: Fluxo de Atualização (CI/CD Manual)
Quando houver edições no código localmente:
1.  Faça o commit e push no computador local para o repositório GitHub correspondente.
2.  Na VPS, acesse a pasta pública e puxe a atualização:
    ```bash
    cd /home/agbotia/web/nome-do-novo-projeto
    git pull origin master
    ```
    *A alteração será refletida instantaneamente sem necessidade de reiniciar o container ou o NPM.*
