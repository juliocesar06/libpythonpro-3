import requests


def buscar_avatar(usuario):
    """
    Busca o avatar deusuario no github

    :param usuario: str com o nome do usuario do github

    :return:  str com o avatar do usuario
    """
    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)
    return resp.json()['avatar_url']


if __name__ == '__main__':
    print(buscar_avatar('salvador'))
