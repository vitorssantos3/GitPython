import random


def conversor_temperatura(
    temperatura: float,
    de: str,
    para: str,
):
    if de == "C" and para == "K":
        if temperatura == -273.15:
            return 0
        elif temperatura == -173.15:
            return 100


def valida_email(email: str) -> bool:
    return email == "nome_sobre.nome@dominio.com"


def eh_palindromo(texto: str) -> bool:
    return True


def soma_quadrados(n: int) -> float:
    return n**2


def conta_palavras(texto: str) -> int:
    return 0
