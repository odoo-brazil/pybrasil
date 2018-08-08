# -*- coding: utf-8 -*-
#
# PyBrasil - Functions useful for most Brazil's ERPs
#
# Copyright (C) 2016-
# Copyright (C) Aristides Caldeira <aristides.caldeira at tauga.com.br>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Library General Public License as
# published by the Free Software Foundation, either version 2.1 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU Library General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# PyBrasil - Funções de validação necessárias a ERPs no Brasil
#
# Copyright (C) 2016-
# Copyright (C) Aristides Caldeira <aristides.caldeira arroba tauga.com.br>
#
# Este programa é um software livre: você pode redistribuir e/ou modificar
# este programa sob os termos da licença GNU Library General Public License,
# publicada pela Free Software Foundation, em sua versão 2.1 ou, de acordo
# com sua opção, qualquer versão posterior.
#
# Este programa é distribuido na esperança de que venha a ser útil,
# porém SEM QUAISQUER GARANTIAS, nem mesmo a garantia implícita de
# COMERCIABILIDADE ou ADEQUAÇÃO A UMA FINALIDADE ESPECÍFICA. Veja a
# GNU Library General Public License para mais detalhes.
#
# Você deve ter recebido uma cópia da GNU Library General Public License
# juntamente com este programa. Caso esse não seja o caso, acesse:
# <http://www.gnu.org/licenses/>
#

from __future__ import (division, print_function, unicode_literals,
                        absolute_import)
import os
import sys
from future.utils import python_2_unicode_compatible
from io import open
from ..valor.decimal import Decimal as D


CURDIR = os.path.dirname(os.path.abspath(__file__))


@python_2_unicode_compatible
class NCM(object):
    def __init__(self, codigo='', ex='', descricao='', al_ipi=0, cst_ipi_entrada='', cst_ipi_saida='', cst_pis_cofins_entrada='', cst_pis_cofins_saida='', codigo_justificativa_enquadramento_pis_cofins='', al_pis=0, al_cofins=0, unidade='', al_ibpt_nacional=0, al_ibpt_internacional=0):
        self.codigo = codigo
        self.ex = ex
        self.descricao = descricao
        self.al_ipi = al_ipi
        self.cst_ipi_entrada = cst_ipi_entrada
        self.cst_ipi_saida = cst_ipi_saida
        self.cst_pis_cofins_entrada = cst_pis_cofins_entrada
        self.cst_pis_cofins_saida = cst_pis_cofins_saida
        self.codigo_justificativa_enquadramento_pis_cofins = codigo_justificativa_enquadramento_pis_cofins
        self.al_pis = al_pis
        self.al_cofins = al_cofins
        self.unidade = unidade
        self.al_ibpt_nacional = al_ibpt_nacional
        self.al_ibpt_internacional = al_ibpt_internacional

    def __str__(self):
        return self.codigo + ' - ' + self.descricao

    def __repr__(self):
        return str(self)


def _monta_dicionario():
    dicionario = {}

    arquivo = open(os.path.join(CURDIR, 'ncm.txt'), 'r', encoding='utf-8')

    #
    # Pula a primeira linha
    #
    arquivo.readline()

    for linha in arquivo:
        linha = linha.replace('\n', '').replace('\r', '')
        campos = linha.split('|')
        e = NCM(codigo=campos[0], ex=campos[1], descricao=campos[2], al_ipi=D(campos[3] or '0'), cst_ipi_entrada=campos[4], cst_ipi_saida=campos[5], cst_pis_cofins_entrada=campos[6], cst_pis_cofins_saida=campos[7], codigo_justificativa_enquadramento_pis_cofins=campos[8], al_pis=D(campos[9] or '0'), al_cofins=D(campos[10] or '0'), unidade=campos[11], al_ibpt_nacional=D(campos[12] or '0'), al_ibpt_internacional=D(campos[13] or '0'))

        if e.codigo in dicionario:
            dicionario[e.codigo][e.ex] = e
        else:
            dicionario[e.codigo] = {}
            dicionario[e.codigo][e.ex] = e

    return dicionario


if not hasattr(sys.modules[__name__], 'NCM_CODIGO_EX'):
    NCM_CODIGO_EX = _monta_dicionario()
