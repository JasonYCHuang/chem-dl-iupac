from flask import current_app
from rdkit import Chem

from chem_iupac.model.concern.verify import verify_by_opsin


class IupacModel:
    @classmethod
    def __canonize_sort(cls, smi_strs):
        csmi_strs = []
        for smi_str in smi_strs:
            sort_csmi_str = ''
            try: # canonize & sort
                csmi_str = Chem.MolToSmiles(Chem.MolFromSmiles(smi_str))
                csmis = csmi_str.split('.')
                csmis.sort()
                sort_csmi_str = '.'.join(csmis)
            except:
                pass
            csmi_strs.append(sort_csmi_str)
        return csmi_strs

    @classmethod
    def __translate_top_k(cls, csmis, k=5):
        m = current_app.smi_to_iupac_model
        in_bins = []
        for csmi in csmis:
            toks = m.tokenize(csmi)
            bpe = m.apply_bpe(toks)
            in_bin = m.binarize(bpe)
            in_bins.append(in_bin)

        out_bins = m.generate(in_bins, beam=k)
        iupacs = []
        for ob in out_bins:
            outs = []
            for sample in ob:
                bpe = m.string(sample['tokens'])
                toks = m.remove_bpe(bpe)
                out = m.detokenize(toks)
                outs.append(out)
            iupacs.append(list(set(outs))[:5])
        return iupacs

    @classmethod
    def infer(cls, smi_strs):
        csmi_strs = cls.__canonize_sort(smi_strs)
        iupacs = cls.__translate_top_k(csmi_strs)
        results = verify_by_opsin(smi_strs, csmi_strs, iupacs)
        return results
