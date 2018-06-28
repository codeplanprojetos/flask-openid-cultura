# -*- coding: utf-8 -*-
from os import environ, sep, path, getcwd

class UndefinedEnvVarError(Exception):
    '''
    Variável de ambiente necessária para o funcionamento do sistema não definida.
    '''
    def __init__(self, envVar):
        self.message = 'undefined environment variable %s' % envVar


class UndefinedHome(Exception):
    '''
    Variável home não foi definida na configuração do Apache.
    '''
    def __init__(self):
        self.message = 'home variable not defined in Apache configuration file'


#
# Verifica variáveis de ambiente obrigatórias.
#

if not path.exists('./openid'):
    raise UndefinedHome()
else:
    app_base = getcwd()

if 'OPENID_DBCONN' in environ.keys():
    openid_db = environ['OPENID_DBCONN']
else:
    raise UndefinedEnvVarError('OPENID_DBCONN')

static_folder = path.join(app_base, environ.get('GEOCODE_STATICDIR', 'static'))
uri = environ.get('URI')

if uri.endswith('/'):
    redirect_uri = uri + 'oidc_callback'
else:
    redirect_uri = uri + '/oidc_callback'
