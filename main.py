from google import genai
from google.genai import errors

chave = "AQ.Ab8RN6III-Ct5kCZrt3hFPSHceZ8YNOFNdGyJNppDA3NDGDsMQ"

cliente = genai.Client(api_key=chave)

print("Conectando...")

try:
    resposta = cliente.models.generate_content(
        model="gemini-3.6-flash",
        contents="Vai chover?"
    )

    print("Resposta:", resposta.text)

except errors.ServerError as erro:
    if erro.code == 503:
        print("O Gemini está temporariamente sobrecarregado")
        print("Tente novamente mais tarde!")
    else:
        print("Erro do servidor:", erro)

except errors.APIError as erro:
    print("Erro de API:", erro)