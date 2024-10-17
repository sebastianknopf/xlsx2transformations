import click
import os

from xlsx2transformations.generator import TransformationGenerator

@click.command
@click.option('--input', '-i', help='Input XLSX file for generating transformations')
@click.option('--output', '-o', help='Output TXT file for transformations')
def __main__(input, output):
    generator = TransformationGenerator(input)
    generator.generate(output)

if __name__ == '__main__':
    __main__()
