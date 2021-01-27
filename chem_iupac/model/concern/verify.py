from flask import current_app

import hashlib
import time
import random
import subprocess as sbp
import shutil

from rdkit import Chem
from datetime import datetime
from pathlib import Path


def __to_opsin_csmi(p_iupac):
    result = current_app.n2s.parseChemicalName(p_iupac, current_app.n2sconfig)
    o_smi = str(result.getSmiles()) if str(result.getStatus()) == 'SUCCESS' else ''
    try:
        o_csmi = Chem.MolToSmiles(Chem.MolFromSmiles(o_smi))
    except:
        o_csmi = o_smi
    return o_csmi


def __to_opsin_csmi_str(p_iupac_str):
    o_csmis = []
    for p_iupac in p_iupac_str.split(';'):
        o_csmi = __to_opsin_csmi(p_iupac)
        o_csmis.append(o_csmi)
    o_csmis.sort()
    o_csmi_str = '.'.join(o_csmis)
    return o_csmi_str


def __pick_one_by_opsin(g_csmi_str, predict_iupac_strs):
    for p_iupac_str in predict_iupac_strs:
        o_csmi_str = __to_opsin_csmi_str(p_iupac_str)
        if g_csmi_str == o_csmi_str:
            return o_csmi_str, p_iupac_str
            
    return '', predict_iupac_strs[0]


def verify_by_opsin(ground_smi_strs, ground_csmi_strs, predict_iupacs):
    results = {}
    for idx, predict_iupac_strs in enumerate(predict_iupacs):
        ground_csmi_str = ground_csmi_strs[idx]
        opsin_csmi_str, predict_iupac_str = __pick_one_by_opsin(ground_csmi_str, predict_iupac_strs)

        results[ground_smi_strs[idx]] = {
            'csmi': ground_csmi_str,
            'iupac': predict_iupac_str,
            'is_opsin_correct': ground_csmi_str == opsin_csmi_str
        }
    return results
