import os
import subprocess
from openai import OpenAI

# Sua chave
client = OpenAI(
    api_key="sk-proj-sua-chave-aqui"
)

print("🔐 H4CKSEC pronta para te ajudar com Pentest & BugBounty!\nDigite 'exit' para sair.\n")

history = [
    {"role": "system", "content": "Você é H4CKSEC, uma consultora especialista em pentest, bug bounty e automação ofensiva. Sempre que o usuário pedir, você pode sugerir ou executar comandos no Kali Linux com base em análises."}
]

while True:
    user_input = input("🧑‍💻 Você: ")

    if user_input.lower() in ["exit", "quit", "sair"]:
        print("👋 Até mais, hacker!")
        break

    # Adiciona entrada do usuário ao histórico
    history.append({"role": "user", "content": user_input})

    # Requisição à API do ChatGPT (gpt-4o)
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=history
        )
    except Exception as e:
        print("❌ Erro:", e)
        continue

    message = response.choices[0].message.content
    print(f"\n🤖 H4CKSEC: {message}\n")

    # Confere se a resposta contém algo que deve ser executado
    if "```bash" in message:
        command = message.split("```bash")[1].split("```")[0].strip()
        confirm = input(f"⚠️ Deseja executar este comando? [s/n]\n> {command}\n")

        if confirm.lower() == "s":
            print("🕵️ Executando no Kali...")
            output = subprocess.getoutput(command)
            print(f"\n📄 Resultado:\n{output}\n")
        else:
            print("✅ Comando não executado.")

