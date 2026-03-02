# Proteção cibernética (site estático)

Este projeto é **estático** (HTML/CSS/JS). Isso já reduz muito o risco de invasão, porque:
- não há banco de dados
- não há login
- não há código rodando no servidor por padrão

Mesmo assim, dá para **endurecer** a segurança com headers e boas práticas.

## O que foi adicionado
1) **CSP (Content Security Policy)**:
   - bloqueia scripts externos e injeções (XSS) por padrão
2) **X-Frame-Options: DENY**
   - impede que o site seja “embutido” em iframes (proteção contra clickjacking)
3) **X-Content-Type-Options: nosniff**
   - evita “adivinhação” de tipo de arquivo (mitiga alguns ataques)
4) **Referrer-Policy**
   - reduz vazamento de URL em navegação
5) **Permissions-Policy**
   - desliga acesso a câmera/microfone/geo por padrão
6) Arquivos de configuração para host:
   - `netlify.toml` e `_headers` (Netlify)
   - `vercel.json` (Vercel)
7) Servidor local opcional com headers:
   - `secure_server.py` (Flask) — útil se você publicar via um servidor Python

## Publicando com headers (recomendado)
### Netlify
- mantenha `netlify.toml` e/ou `_headers` na raiz do site publicado.
- a Netlify aplica os headers automaticamente.

### Vercel
- mantenha `vercel.json` na raiz do projeto.
- a Vercel aplica os headers automaticamente.

## Importante
- Ao publicar, use **HTTPS**.
- Evite colar scripts de terceiros (widgets) sem necessidade.
- Se no futuro você adicionar formulários com back-end, aí entram CSRF, validação de entrada, rate limit etc.
