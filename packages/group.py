import click
import jwt
from packages.j import decode_jwt_without_verify


@click.command()
@click.argument('s', nargs=-1)
def hello(s):
    raw = ''
    for i, value in enumerate(s):
        if i != 0:
            raw += '-' + value.lower()
        else:
            raw += value.lower()
    click.echo(raw)


@click.command()
@click.argument("token", nargs=1)
def jwt_tool(token):
    try:
        decode_token = decode_jwt_without_verify(token)
    except jwt.PyJWTError:
        click.echo("sorry your token is invalid")
    else:
        click.echo(decode_token)
