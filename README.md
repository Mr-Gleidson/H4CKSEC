# H4CKSEC
H4CKSEC is a personal AI-powered assistant for penetration testing and bug bounty automation. Built with GPT-4o and integrated into Kali Linux, it acts as a technical consultant capable of answering, suggesting and even executing commands securely through the terminal.


# 🛡️ H4CKSEC – Sua assistente pessoal de Pentest & Bug Bounty

H4CKSEC é uma consultora virtual alimentada pela API do GPT-4o, integrada ao Kali Linux, projetada para te auxiliar em tarefas ofensivas de cibersegurança.  
Ela responde perguntas técnicas, sugere comandos, ajuda a construir payloads e **executa ferramentas diretamente no terminal**, com segurança e sob sua aprovação.

> 🤖 Pense nela como uma secretária hacker: rápida, técnica e fiel ao código.

---

## 🚀 Funcionalidades

- ✅ Integração com GPT-4o (OpenAI)
- ✅ Chat interativo no terminal
- ✅ Execução de comandos sugeridos (com confirmação)
- ✅ Personalidade técnica voltada para pentest e bug bounty
- ✅ Pronta para integração com ferramentas como Burp, Nmap, ffuf, dirsearch, etc.

---

## 🧰 Requisitos

- Python 3.10+
- Conta OpenAI com API Key válida
- Kali Linux (ou qualquer distro com ferramentas de pentest)
- Biblioteca `openai` instalada (`pip install openai`)

---

## 🛠️ Instalação

```bash
git clone https://github.com/Mr-Gleidson/H4CKSEC.git
cd H4CKSEC
python3 -m venv venv
source venv/bin/activate
pip install openai
