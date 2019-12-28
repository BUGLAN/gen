import click


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
