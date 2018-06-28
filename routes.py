# -*- coding: utf-8 -*-
from flask import Flask, g


def add_routes(app, oidc):
    """ """

    @app.route('/')
    def hello_world():
        if oidc.user_loggedin:
            return ('Hello, %s, <a href="/private">See private</a> '
                    '<a href="/logout">Log out</a>') % oidc.user_getfield('first_name')
        else:
            return 'Welcome anonymous, <a href="/private/">Log in</a>'


    @app.route('/private/')
    @oidc.require_login
    def hello_me():
        info = oidc.user_getinfo(['email', 'first_name'])
        return ('Hello, %s (%s)! <a href="/">Return</a>' %
                (info.get('email'), info.get('first_name')))


    @app.route('/api')
    @oidc.accept_token(True, ['openid'])
    def hello_api():
        return json.dumps({'hello': 'Welcome %s' % g.oidc_token_info['sub']})


    @app.route('/logout')
    def logout():
        oidc.logout()
        return 'Hi, you have been logged out! <a href="/">Return</a>'

