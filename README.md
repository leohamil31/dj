# Grupo DJ Morch — Site

Site da **Grupo DJ Morch**, que vende insumos para velas, saboaria e aromatização em Curitiba - PR.
É uma página única (HTML, CSS e JavaScript puros), sem dependências, e funciona direto no navegador.

## Estrutura

```
index.html                  ← site pronto (abra no navegador / publique este arquivo)
src/template.html           ← código-fonte editável (HTML + CSS + JS)
build.py                    ← gera o index.html a partir do template
assets/images/produtos.json ← fotos dos produtos (webp em base64, tiradas do catálogo)
assets/logo/                ← logo vetorial (claro/escuro), símbolo "jd" e logos de terceiros
```

## Como editar

1. Edite `src/template.html`.
2. Rode `python3 build.py`.
3. Abra o `index.html` no navegador para conferir.

### Onde mudar as coisas mais comuns (em `src/template.html`)

| O quê | Procure por |
|---|---|
| Preço dos produtos (hoje todos R$ 5,55) | `const PRICE` |
| Lista de produtos (nome, categoria, descrição, selo) | `const P=[` |
| Número do WhatsApp | `const WA` |
| Link de pagamento no site (Nuvemshop, Mercado Pago…) | `const CHECKOUT_URL` |
| Transportadoras | `const CARRIERS` |
| Link da loja no Mercado Livre | `lista.mercadolivre.com.br/djmorch` |
| Link da loja na Shopee | `shopee.com.br/search?keyword=dj%20morch` |
| Cores do tema claro / escuro | `:root{` e `[data-theme="dark"]{` |
| Perguntas frequentes | `id="faq"` |

## Pendências

- [ ] Trocar o link do **Mercado Livre** e da **Shopee** pelos endereços oficiais das lojas.
- [ ] Definir o `CHECKOUT_URL` com o link de pagamento real.
- [ ] Confirmar as **transportadoras** usadas, as **formas de pagamento** e o texto das **Perguntas Frequentes**.
- [ ] Ajustar os **preços reais** (hoje todos em R$ 5,55).
- [ ] Trocar as logos redesenhadas (Correios, Jadlog, Loggi, J&T, Shopee) pelos arquivos oficiais.
- [ ] Se tiver o arquivo original da logo DJ Morch em vetor, substituir `assets/logo/logo_*.svg`.

## Recursos do site

- Tema claro e escuro (a escolha fica salva no navegador)
- Pilha de cartões animada no topo
- Filtros por categoria, busca com aviso de erro e carregamento animado
- Favoritos com efeito de curtir (salvos no navegador)
- Carrinho lateral: contador animado, deslizar para remover e duas formas de finalizar:
  **pagar no site** (Pix, cartão ou boleto) ou **enviar o pedido ao vendedor no WhatsApp**
- Seção de transportadoras, perguntas frequentes em sanfona e botão de voltar ao topo com anel de progresso
- Barra de abas no celular e botão flutuante do WhatsApp
- Respeita a opção "reduzir movimento" do sistema
