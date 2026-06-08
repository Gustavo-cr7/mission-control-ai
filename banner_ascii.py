import argparse
import pyfiglet
from rich.console import Console
from rich.align import Align
from rich.text import Text

console = Console()

def mostrar_banner(font="ansi_shadow", text="Mission Control AI"):
    linha1 = pyfiglet.figlet_format("Global Solution", font=font)
    linha2 = pyfiglet.figlet_format(text, font=font)

    console.print(Align.center(Text(linha1, style="bold #A855F7")))
    console.print(Align.center(Text(linha2, style="bold #06B6D4")))
    console.print(Align.center(
        Text("── 2026.1 · Prompt Engineering and AI · FIAP ──",
        style="italic #8484A0")
    ))

def listar_fontes():
    for fonte in pyfiglet.FigletFont.getFonts():
        print(fonte)

def demo():
    fontes = ["slant", "ansi_shadow", "big", "doom", "standard", "small", "digital", "banner3-D"]
    for fonte in fontes:
        console.print(f"\nFonte: {fonte}", style="bold yellow")
        print(pyfiglet.figlet_format("Mission Control AI", font=fonte))

parser = argparse.ArgumentParser()
parser.add_argument("-fonts", action="store_true")
parser.add_argument("-font", default="ansi_shadow")
parser.add_argument("-text", default="Mission Control AI")
parser.add_argument("-demo", action="store_true")
args = parser.parse_args()

if args.fonts:
    listar_fontes()
elif args.demo:
    demo()
else:
    mostrar_banner(args.font, args.text)
