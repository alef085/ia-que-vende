# Viabilidade — SaaS "IA que Vende" com Dashboard
> Resumo executivo · Maio 2026

---

## A Ideia em Uma Linha

Transformar o guia PDF em uma plataforma web onde o empreendedor preenche os dados do negócio uma vez e acessa as ferramentas de IA com um clique — sem copiar prompt, sem abrir ChatGPT, sem saber nada de tecnologia.

---

## Como Funcionaria

```
Usuário entra no dashboard
    ↓
Preenche perfil do negócio (nome, nicho, tom de voz)
    ↓
Escolhe a ferramenta (ex: "Criar Post", "Gerar Oferta", 
"Responder Cliente no ZAP", "Criar Criativo de Anúncio")
    ↓
Clica em gerar
    ↓
A plataforma monta o prompt com o contexto do negócio
e envia para a API da IA (OpenAI ou Claude)
    ↓
Resultado aparece na tela — pronto para copiar e usar
```

O usuário nunca vê o prompt. Ele só vê o resultado.

---

## Ferramentas Possíveis no Dashboard (MVP)

Baseadas diretamente nos módulos do guia:

| Ferramenta | O que faz |
|---|---|
| Gerador de Post | Cria legenda para feed/stories por nicho |
| Criador de Oferta | Monta oferta irresistível com gatilhos |
| Script WhatsApp | Gera resposta para "quanto custa?" e objeções |
| Analisador de Conversa | Cola conversa do ZAP, IA aponta onde perdeu a venda |
| Criativo de Anúncio | Headline + primary text para Meta Ads |
| Calendário do Mês | Gera 30 ideias de conteúdo por nicho |
| Gerador de Arte (prompt) | Prompt pronto para Canva IA ou Midjourney |

---

## Modelo de Negócio

| Tier | Preço | O que inclui |
|---|---|---|
| **Entrada via PDF** | R$67 (único) | Guia + acesso 7 dias grátis ao dashboard |
| **Básico** | R$47/mês | 5 ferramentas, 1 perfil de negócio |
| **Pro** | R$97/mês | Todas as ferramentas, 3 perfis, histórico |
| **Agência** | R$197/mês | Perfis ilimitados (revendedores/agências) |

**Potencial de receita recorrente:**

| Assinantes | MRR |
|---|---|
| 100 | R$4.700 |
| 300 | R$14.100 |
| 500 | R$23.500 |
| 1.000 | R$47.000 |

---

## Vantagens do Modelo

✅ **Funil natural** — PDF de R$67 gera lead qualificado para o SaaS  
✅ **Você já tem a infraestrutura** — VPS, SaaS de WhatsApp, know-how técnico  
✅ **Custo de API é baixo** — OpenAI cobra ~R$0,03 por geração  
✅ **Moat por nicho** — prompts calibrados por nicho criam diferencial real  
✅ **Receita previsível** — MRR vs. venda pontual de PDF  
✅ **Produto validado antes de construir** — o PDF prova a demanda primeiro  

---

## Riscos Reais

⚠️ **Concorrência com o ChatGPT gratuito** — o cliente pode perguntar "por que pagar se tenho de graça?"  
→ Resposta: conveniência, contexto salvo, sem precisar saber nada  

⚠️ **Churn** — se não usar, cancela  
→ Mitigação: onboarding forte + Desafio de 7 Dias integrado ao dashboard  

⚠️ **Custo de desenvolvimento** — MVP mínimo leva 30-60 dias se terceirizar  
→ Alternativa: usar Bubble (no-code) para MVP em 2 semanas  

⚠️ **Dependência de API de terceiro** — OpenAI pode mudar preço ou política  
→ Mitigação: usar Claude (Anthropic) como backup, arquitetura multi-provider  

---

## Custo Estimado de MVP

| Item | Estimativa |
|---|---|
| Desenvolvimento (no-code/Bubble) | R$2.000 – R$5.000 |
| API OpenAI (primeiros 500 usuários) | ~R$150/mês |
| Hospedagem (já tem VPS) | R$0 adicional |
| Kirvano / checkout | Já tem |
| **Total para ir ao ar** | **~R$2.000 – R$5.000** |

---

## Sequência Recomendada

```
AGORA          → Validar o PDF (R$67)
Após 50 vendas → Oferecer 7 dias grátis no dashboard para compradores
                 (coleta feedback real)
Após 30 feedbacks → Construir MVP do dashboard
Após MVP       → Lançar plano mensal para base de compradores
                 (lista quente, zero custo de aquisição)
```

**O PDF não é só produto — é o funil de entrada para o SaaS.**

---

## Conclusão

**Viável? Sim.**  
**Momento certo? Não ainda.**

Construir o SaaS antes de validar o PDF seria queimar tempo e dinheiro sem saber se o mercado compra a proposta. O caminho correto é usar o PDF como prova de demanda e como gerador da primeira base de clientes — que depois se tornam assinantes do dashboard com custo de aquisição próximo de zero.

O ativo mais valioso que você vai construir nos próximos 60 dias não é o código do SaaS. É a lista de pessoas que já compraram o PDF e viram resultado.

---

*Documento gerado em 26/05/2026 · Para retomar esse planejamento, abrir com Claude Code*
