#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici



# TODO: Définissez vos fonction ici
import math


def volumemasse(a=2, b=4, c=6, massevolumique=10):
    v = (4/3) * math.pi * a*b*c
    m = v * massevolumique
    return v, m


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    print(volumemasse())
