from google import genai
from google.genai import errors

chave = "AQ.Ab8RN6III-Ct5kCZrt3hFPSHceZ8YNOFNdGyJNppDA3NDGDsMQ"

cliente = genai.Client(api_key=chave)

print("=== Assistente de Futebol ===")
nome = input("Qual seu nome? ")
time = input("Qual seu time do coração? ")
necessidade = input("O que você procura (ex: camisa, chuteira, bola)? ")

pergunta = f"""
Você é um especialista em artigos esportivos de futebol. Um cliente chamado {nome},
torcedor do {time}, está procurando: "{necessidade}"

Recomende um produto ideal, explique por que combina com o perfil dele
e dê uma dica de uso ou cuidado com o produto.
Responda de forma curta e simples.
"""

print("\nConsultando o especialista...")

try:
    resposta = cliente.models.generate_content(
        model="gemini-3.6-flash",
        contents=pergunta
    )

    print(f"\nRecomendação para o(a) torcedor(a) do {time}:")
    print(resposta.text)

except errors.ServerError as erro:
    if erro.code == 503:
        print("O Gemini está temporariamente sobrecarregado")
        print("Tente novamente mais tarde!")
    else:
        print("Erro do servidor:", erro)

except errors.APIError as erro:
    print("Erro de API:", erro)