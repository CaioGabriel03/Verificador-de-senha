def verificar_senha(senha):
    """
    Verifica a força de uma senha com base em critérios predefinidos.

    Parâmetros:
    senha (str): A senha a ser verificada.

    Retorna:
    str: A força da senha ("fraca", "média" ou "forte").
    """
    # Critério para senha forte: mais de 10 caracteres e contém letras e números
    if len(senha) > 10 and any(c.isalpha() for c in senha) and any(c.isdigit() for c in senha):
        return "forte"
    # Critério para senha média: de 6 a 10 caracteres e contém apenas letras ou apenas números
    elif 6 <= len(senha) <= 10 and (senha.isalpha() or senha.isdigit()):
        return "média"
    # Critério para senha fraca: menos de 6 caracteres
    elif len(senha) < 6:
        return "fraca"
    # Caso não se encaixe nos critérios acima, por exemplo, mais de 10 caracteres, mas sem mistura de letras e números.
    else:
        return "média"

# Exemplo de uso:
senha1 = "senha123456"  # Forte
print(f"A senha '{senha1}' é: {verificar_senha(senha1)}")

senha2 = "senhafraca"  # Média
print(f"A senha '{senha2}' é: {verificar_senha(senha2)}")

senha3 = "curta"  # Fraca
print(f"A senha '{senha3}' é: {verificar_senha(senha3)}")

senha4 = "senhacompleta12345" # Forte
print(f"A senha '{senha4}' é: {verificar_senha(senha4)}")
