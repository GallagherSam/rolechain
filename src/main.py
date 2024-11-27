import click
from commands.prompt import execute_prompt


@click.group()
def cli():
    pass


@cli.command()
@click.option("--workflow")
@click.option("--prompt")
def prompt(workflow, prompt):
    execute_prompt(workflow, prompt)


if __name__ == "__main__":
    cli()
