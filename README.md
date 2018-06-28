# OpenID

Prova de conceito para autenticar como usuário do provedor ID Cultura.

## Pré-requisitos

* GNU/Linux
* Apache 2
* Python 3.x
* Flask
* Pypi
* Flask-OIDC
* Virtualenv

### Debian e derivados

Se você estiver usando Debian/Ubuntu ou derivados, você pode instalar as dependências acima com os comandos:
```
sudo apt-get update
sudo apt-get install apache2-dev python3 python3-pip
```

Se você estiver usando uma versão muito velha do apache2, talvez seja necessário atualizar o mod_wsgi para apontar para o Python 3 ao invés do Python 2:
```
sudo a2dismod wsgi
sudo apt-get remove libapache2-mod-wsgi
sudo apt-get install libapache2-mod-wsgi-py3
sudo a2enmod wsgi
```

## Instalação

Instale os softwares especificados acima de acordo com a sua distro e execute o comando ``setup.sh`` na pasta raiz e respondendo todas as perguntas que aparecerem. Após terminado de seguir o script de ``setup.sh``, é necessário registrar o cliente Open ID Connect com o provedor de autenticação (neste caso, o ID Cultura). Para fazê-lo basta executar o comando:
```
./openid --register https://id.cultura.gov.br/
```
