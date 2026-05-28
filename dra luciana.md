# Documentação do Projeto — Landing Page Dra. Luciana Marques

Este documento apresenta as especificações de design, estrutura, comportamento responsivo e diretrizes técnicas da landing page premium da **Dra. Luciana Marques** (Endocrinologista e Metabologista em Belém-PA).

---

## 1. Visão Geral do Projeto

*   **Médica**: Dra. Luciana Marques (CRM-PA 9264 | RQE 6571).
*   **Nicho**: Endocrinologia e Metabologia com foco em saúde hormonal e metabolismo da mulher 40+ (menopausa, climatério, sobrepeso e emagrecimento saudável).
*   **Objetivo**: Landing Page de alta conversão para atração de pacientes particulares, focada na escuta atenta, acolhimento e medicina de alto nível.
*   **Acesso de Produção**: `https://aleianegocios.com.br/dralucianaendocrino/`
*   **Repositório Local**: `c:\Users\Paulo Aleixo\IA que vende\dralucianaendocrino\`

---

## 2. Design System & Identidade Visual

A interface foi projetada sob uma estética **editorial premium**, com foco em leveza, sofisticação e respiro visual para transmitir autoridade e acolhimento clínico.

### 2.1 Paleta de Cores
*   **Fundo Principal (`--color-bg`)**: `#FAF9F6` (Off-white leve e confortável).
*   **Fundo Alternativo (`--color-bg-alt`)**: `#F1EDE6` (Areia suave para contrastar seções).
*   **Verde Primário (`--color-primary`)**: `#0F6668` (Teal moderno para botões e links de destaque).
*   **Verde Escuro (`--color-primary-dark`)**: `#073F42` (Verde petróleo para títulos e contraste).
*   **Rosé/Dourado (`--color-rose`)**: `#BE747D` (Rosé sofisticado para sublinhados e ícones).
*   **Verde Sálvia (`--color-sage`)**: `#DDE9E3` (Sálvia claro para fundos e marcadores secundários).
*   **Textos (`--color-text`)**: `#253033` (Cinza escuro editorial, evitando o preto puro).

### 2.2 Tipografia
*   **Títulos do Hero / Destaques (`--font-headline`)**: `Playfair Display`, serif.
*   **Títulos Gerais (`--font-heading`)**: `Cormorant Garamond`, serif.
*   **Textos e Elementos de UI (`--font-body`)**: `Manrope`, sans-serif.

### 2.3 Elementos Estéticos
*   **Textura Editorial**: Efeito de grão/ruído aplicado via CSS na tag `body` com opacidade `0.022` para simular uma revista de luxo.
*   **Bordas Arredondadas**: Padrão de `24px` para cards e `16px` para botões principais.
*   **Micro-animações**: Suavização em hover (`transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1)`) e efeitos `fade-up` disparados via `IntersectionObserver`.

---

## 3. Estrutura de Seções

A página segue uma jornada narrativa lógica para conversão (AIDA):

### 3.1 Hero Section
*   **Desktop**: Grid de duas colunas (`1.1fr 0.9fr`) com gap de `72px`. Texto com headline editorial à esquerda, foto da médica à direita. A foto possui uma forma geométrica areia de fundo (`.hero-shape-bg`), selo flutuante de avaliação no Google e a badge profissional da médica (`.doctor-badge`) posicionada abaixo dela de forma integrada (`z-index: 3`).
*   **Mobile**: A foto é movida para o topo utilizando propriedades flexbox (`order: -1` no wrapper e `order: 1` no conteúdo de textos), garantindo o impacto visual imediato em telas pequenas. Os botões de agendamento são redimensionados para `calc(100% - 48px)` com `max-width: 420px` para uma proporção perfeita.

### 3.2 Seção de Sintomas (Dores)
Grid de cards sofisticados listando as principais reclamações das pacientes.
*   **Ordem dos Cards**:
    1.  **Menstruação irregular** (Com miniatura `0_Menstruacao_irregular.png`).
    2.  **Ondas de calor e suores noturnos** (Miniatura correspondente).
    3.  **Peso persistente** (Miniatura correspondente).
    4.  **Cansaço constante** (Miniatura correspondente).
    5.  **Esquecimento e falta de foco** (Miniatura correspondente - antigo "Nevoeiro mental").
    6.  **Humor oscilante** (Miniatura correspondente).
    7.  **Insônia e sono ruim** (Miniatura correspondente).
*   **Layout**: Cards com fundo branco, bordas finas douradas e miniaturas quadradas à esquerda (`110x100px` com cantos arredondados).

### 3.3 Sobre a Dra. Luciana
Seção de biografia institucional focada em credibilidade.
*   **Visual**: Foto da médica em ambiente clínico à esquerda e bloco de texto à direita.
*   **Credenciais**: Grid de 4 blocos contendo os marcos profissionais (Formação UFPA, Residência na Santa Casa, Residência no Barros Barreto e Registro CRM/RQE).

### 3.4 Abordagem (Como Trato)
Jornada do tratamento estruturada em linha de tempo (timeline).
*   **Passos**: 1. Escuta Ativa, 2. Diagnóstico Preciso, 3. Tratamento Sob Medida, 4. Acompanhamento Próximo.
*   **Tags**: Nuvem de chips na base destacando os tratamentos principais (Saúde Hormonal Feminina, Menopausa, Reposição Hormonal, Emagrecimento, Resistência à Insulina, Tireoide).

### 3.5 Depoimentos
*   Layout em 3 colunas exibindo avaliações reais de pacientes copiadas do Google Meu Negócio, com estrelas de avaliação douradas.

### 3.6 Perguntas Frequentes (FAQ)
Acordeões interativos criados com Javascript puro.
*   **Dúvidas Respondidas**:
    *   *Dra. Luciana Marques atende convênios?* (Foco em esclarecer que o atendimento é **100% particular** e que a equipe fornece nota fiscal e relatório médico para que a paciente solicite reembolso direto com seu plano de saúde).
    *   *Onde fica localizado o consultório?* (Trav. Dom Romualdo de Seixas, 1476 — Umarizal, Belém-PA, Edifício Evolution).
    *   *Como realizo o agendamento da minha consulta?* (Exclusivamente via WhatsApp corporativo).
    *   *As consultas dão direito a retorno clínico?* (Prazo de até 30 dias para leitura de exames).

### 3.7 CTA Final & Rodapé
*   **CTA Final**: Chamada forte verde-escura estimulando o agendamento de consultas.
*   **Rodapé**: Verde escuro de alta legibilidade, com contraste aumentado (`#F6EFE6` e `#D8E2DD`), exibindo o CRM/RQE da médica e links diretos para o Instagram.

---

## 4. Otimização Responsiva (Mobile vs Desktop)

O site possui duas folhas de estilo perfeitamente isoladas para garantir a melhor experiência em qualquer dispositivo:

### 4.1 Comportamento Mobile (Telas até 900px)
*   **CSS Fixo de Conversão**: Exibição da barra inferior fixa (`.mobile-cta-bar`) com o botão "Agendar consulta pelo WhatsApp" ocupando toda a largura útil, com padding de `24px` nas laterais para não encostar na borda da tela.
*   **Botões**: Altura de `56px`, com bordas arredondadas de `16px`.
*   **Estrutura Vertical**: Elementos empilhados para leitura linear confortável no celular.

### 4.2 Comportamento Desktop (Telas acima de 901px)
As regras estão isoladas sob `@media (min-width: 901px)` para evitar conflito com o mobile:
*   **Respiro e Containers**: Largura máxima do contêiner limitada em `1260px` com `padding` lateral de `40px` e espaçamento vertical entre seções fixado em `100px`.
*   **Tipografia**:
    *   Headline Hero: `54px` (line-height: `1.15`).
    *   Títulos de Seção: `42px`.
    *   Textos do corpo: `17px` padrão (trazendo leveza e sofisticação, sem parecer gigantesco).
*   **Miniaturas**: Miniaturas dos sintomas escaladas para `110x100px`.
*   **Grid do Hero**: Divisão real em duas colunas, com foto da médica à direita (`max-width: 480px`, `height: 560px`) e texto à esquerda.

---

## 5. Especificações Técnicas & Deploy

*   **Arquitetura**: Single Page Application (SPA) estática construída com HTML5 e Vanilla CSS/JS (sem frameworks pesados para garantir velocidade máxima de carregamento).
*   **Performance**: Imagens otimizadas localmente (PNG/JPG). Google Fonts carregadas via link com preconnect.
*   **Animações**: IntersectionObserver em JS monitorando a classe `.fade-up` para adicionar a classe `.visible` no scroll.
*   **Integrações**: Rastreamento de Pixel do Facebook configurado via cabeçalho.
*   **Fluxo de Deploy (VPS)**:
    1.  As alterações locais são commitadas no repositório local.
    2.  Enviadas para o repositório remoto via `git push origin master`.
    3.  No servidor de hospedagem VPS (srv1596545), roda-se o comando:
        ```bash
        cd /home/agbotia/web/aleianegocios/ia-que-vende
        git pull origin master
        ```
