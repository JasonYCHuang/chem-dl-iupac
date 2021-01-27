# chem-dl-iupac

- This repository contains [1] training a deep learning model [2] a flask inference server.
- The model can convert `SMILES` to `IUPAC nomenclature`.


### 1. Run a flask inference server

Please follow steps in:
1. `INSTALL_SERVER.md` for installation

```bash
# request
curl --location --request POST 'xxx.xxx.xxx.xxx:7107/iupac_name' \
--header 'Content-Type: application/json' \
--data-raw '{
    "smis": [
        "CS(=O)(=O)OCCCBr", 
        "CS(=O)(OCCCBr)=O", 
        "O=C(O)c1ccc(NC(=O)C2CCC2)cc1",
        "O=C(O)c1ccc(cc1)(NC(=O)C2CCC2)",
        "CN(Cc1ccc(C(C)(C)C)cc1)c1cccc2ccccc12.Cl",
        "Cl.CN(Cc1ccc(C(C)(C)C)cc1)c1cccc2ccccc12"
    ]
}'

# response
{
    "CN(Cc1ccc(C(C)(C)C)cc1)c1cccc2ccccc12.Cl": {
        "csmi": "CN(Cc1ccc(C(C)(C)C)cc1)c1cccc2ccccc12.Cl",
        "is_opsin_correct": true,
        "iupac": "N-[(4-tert-butylphenyl)methyl]-N-methyl-1-naphthalenamine;hydrochloride"
    },
    "CS(=O)(=O)OCCCBr": {
        "csmi": "CS(=O)(=O)OCCCBr",
        "is_opsin_correct": true,
        "iupac": "methanesulfonic acid 3-bromopropyl ester"
    },
    "CS(=O)(OCCCBr)=O": {
        "csmi": "CS(=O)(=O)OCCCBr",
        "is_opsin_correct": true,
        "iupac": "methanesulfonic acid 3-bromopropyl ester"
    },
    "Cl.CN(Cc1ccc(C(C)(C)C)cc1)c1cccc2ccccc12": {
        "csmi": "CN(Cc1ccc(C(C)(C)C)cc1)c1cccc2ccccc12.Cl",
        "is_opsin_correct": true,
        "iupac": "N-[(4-tert-butylphenyl)methyl]-N-methyl-1-naphthalenamine;hydrochloride"
    },
    "O=C(O)c1ccc(NC(=O)C2CCC2)cc1": {
        "csmi": "O=C(O)c1ccc(NC(=O)C2CCC2)cc1",
        "is_opsin_correct": true,
        "iupac": "4-[[cyclobutyl(oxo)methyl]amino]benzoic acid"
    },
    "O=C(O)c1ccc(cc1)(NC(=O)C2CCC2)": {
        "csmi": "O=C(O)c1ccc(NC(=O)C2CCC2)cc1",
        "is_opsin_correct": true,
        "iupac": "4-[[cyclobutyl(oxo)methyl]amino]benzoic acid"
    }
}
```

---

### License

see [LICENSE][LICENSE]

[LICENSE]: LICENSE
