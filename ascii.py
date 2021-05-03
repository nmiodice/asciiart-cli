import argparse
import random
import urllib.request
from lxml import html



ASCII_ART_HOME="https://asciiart.website/index.php"

def get_ascii(art_path):
    url = '{0}?art={1}'.format(ASCII_ART_HOME, art_path)
    with urllib.request.urlopen(url) as response:
       tree = html.fromstring(response.read())
       asciis = tree.xpath('//pre[contains(@id, "p")]')
       ascii = random.choice(asciis)
       return ascii.text

def print_ascii(text, header = '', wrap_before = '', wrap_after = ''):
    print('{0}\n{1}{2}{3}'.format(
        header, wrap_before, text, wrap_after
    ))

def run(args):
    text = get_ascii(args.artpath[0])
    print_ascii(
        text,
        args.header[0],
        args.before[0],
        args.after[0],
    )



def getargs():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--artpath', type=str, nargs=1, help='The ascii art path to use. For example, transportation/nautical')
    parser.add_argument('--header', type=str, nargs=1, help='Header to print on a single line before the ascii art. For example, Ship It!', default = [''])
    parser.add_argument('--before', type=str, nargs=1, help='Prefix ascii in this. For example, ```', default = [''])
    parser.add_argument('--after', type=str, nargs=1, help='Postfix ascii in this. For example, ```', default = [''])

    return parser.parse_args()

if __name__ == '__main__':
    run(getargs())

