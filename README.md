# 🛡️ H4CKSEC – Sua assistente de Pentest & Bug Bounty com GPT-4o

H4CKSEC é uma consultora virtual inteligente, integrada ao Kali Linux e alimentada pela API do GPT-4o.  
Ela atua como sua **secretária técnica** para auxiliar em testes de invasão, bug bounty e automações ofensivas.

> 🧠 Converse, peça ajuda e até execute comandos diretamente pelo terminal, com total controle e segurança.

---

## 🚀 Funcionalidades

- 🤖 Chat interativo com GPT-4o via terminal
- 🔐 Execução de comandos no Kali (com confirmação)
- 🧠 Consultoria em exploração de vulnerabilidades (XSS, SQLi, IDOR, etc.)
- 💣 Sugestões de payloads, ferramentas e estratégias
- ⚙️ Preparada para integração com Nmap, Burp, ffuf, dirsearch, etc.

---

## 📦 Requisitos

- Python 3.10+  
- Conta OpenAI com chave de API (com acesso ao modelo `gpt-4o`)
- Kali Linux (ou outra distro com terminal compatível)
- Biblioteca [`openai`](https://pypi.org/project/openai/)

---

## 🔧 Como configurar e usar o ambiente virtual (Kali Linux)

O Kali possui restrições (`externally-managed-environment`) que impedem o uso do `pip` global.  
Por isso, é **obrigatório usar um ambiente virtual (venv)** para isolar o projeto.

### 📌 Passo a passo:

```bash
# 1. Clone o repositório
git clone https://github.com/Mr-Gleidson/H4CKSEC.git
cd H4CKSEC

# 2. Crie o ambiente virtual
python3 -m venv venv

# 3. Ative o ambiente
source venv/bin/activate

# 4. Instale a biblioteca openai
pip install openai

# 5. Execute o assistente
python3 h4cksec.py
