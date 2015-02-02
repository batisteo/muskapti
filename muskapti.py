#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Tiu programo estas la klono en Pitono 3 de gitgub.com/LaPingvino/muskapti

from sys import argv
from random import randint


klarigo = """
Bonvenon ĉe "Kaptu la muson"!
La celo de la ludo estas diveni numeron de {min} ĝis {max}.
Vi povas provi tion unu post la alia.
{rapideco_klarigo}
Se la numero fariĝas pli alta ol {max}, ĝi reiras al {min}.
Se la numero fariĝas malpli alta ol {min}, ĝi reiras al {max}.
Multan sukceson!
"""

maltrafo = "Ne, la numero estas pli alta"


def get_arg(index, default):
    try:
        return int(argv[index])
    except (IndexError, ValueError):
        return default


def opcioj(min, max, rapideco):
    min = get_arg(1, min)
    max = get_arg(2, max)
    rapideco = get_arg(3, rapideco)
    return min, max, rapideco


def klarigu_rapidecon(rapideco):
    if rapideco > 0:
        return ("Tamen atentu! La numero povas post ĉies vico ĉu %d supreniri, "
        "ĉu tiom malsupreniri, ĉu resti sama." % rapideco)
    if rapideco == 0:
        return "Vi elektis ke la numero ĉiam restu la sama."
    if rapideco < 0:
        return ("Vi elektis veran defion. La numero povas post ĉies vico en hazarda kvanto de "
        "maksimume %d supreniri, ĉu samkvante malsupreniri, ĉu resti la sama." % -rapideco)


def klarigu_ludon(min, max, rapideco):
    print(klarigo.format(min=min,
                         max=max,
                         rapideco_klarigo=klarigu_rapidecon(rapideco))
    )


def enigu_ludantojn():
    ludantoj = []
    while True:
        nomo = input("Nomo de la {0}a ludanto: ".format(len(ludantoj) + 1))
        if nomo:
            ludantoj.append(nomo)
        elif ludantoj:
            return ludantoj


def movigu(muso, min, max, pasho):
    muso = muso + pasho
    if muso > max:
        muso = min
    if muso < min:
        muso = max
    return muso


def ludu(ludantoj, min, max, rapideco):
    vico = 0
    muso = randint(min, max)
    pasho = randint(-abs(rapideco), abs(rapideco))
    while True:
        nomo = ludantoj[vico % len(ludantoj)]
        provo = input("Estas la vico de {nomo}: kiu numero estas? ".format(nomo=nomo))
        try:
            provo = int(provo)
        except ValueError:
            provo = 0
        if provo == muso:
            return nomo, vico
        print(maltrafo if muso > provo else maltrafo.replace("pli", "malpli"))
        vico += 1
        if rapideco < 0:
            pasho = randint(rapideco, -rapideco)
        muso = movigu(muso, min, max, pasho)


def rulu_ludon(ludantoj, min, max, rapideco):
    nb_ludoj = 0
    while True:
        if nb_ludoj:
            if input("Ĉu ludi denove, jes aŭ ne? ").lower()[:1] == 'n':
                return nb_ludoj
        venkulo, nb_provoj = ludu(ludantoj, min, max, rapideco)
        print("{0} venkis post {1} provoj!".format(venkulo, nb_provoj))
        nb_ludoj += 1


if __name__ == '__main__':
    min, max, rapideco = opcioj(1, 100, 1)
    klarigu_ludon(min, max, rapideco)
    ludantoj = enigu_ludantojn()
    nb_ludoj = rulu_ludon(ludantoj, min, max, rapideco)
    print("Vi tamen {0} foje ludis! Ĝis!\n".format(nb_ludoj))
