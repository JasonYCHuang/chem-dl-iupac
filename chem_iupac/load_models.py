from __future__ import print_function
from fairseq.models.transformer import TransformerModel

from pathlib import Path
import logging


logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)


root_dir = f'{Path().absolute()}/chem_iupac/smi_to_iupac'

def load_smi_to_iupac_model():
    model = TransformerModel.from_pretrained(
        str(Path().absolute()),
        checkpoint_file=f'{root_dir}/checkpoints/checkpoint_best.pt',
        data_name_or_path=f'{root_dir}/data-bin/smi_iupac.smi-iupac/',
        bpe='subword_nmt',
        bpe_codes=f'{root_dir}/preprocess/smi_iupac/code'
    )

    model.eval()

    print('Load the model OK!')
    return model

