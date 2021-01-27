import os
import jpype
from flask import Flask

import chem_iupac.load_models as lm


OUTPUT_COUNT = 5


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        IP_WHITE_LIST='',
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    smi_to_iupac_model = lm.load_smi_to_iupac_model()
    app.smi_to_iupac_model = smi_to_iupac_model

    app.output_count = OUTPUT_COUNT

    app.chem_iupac_dir = os.path.abspath(os.getcwd()) + '/chem_iupac'

    # opsin
    jpype.startJVM(classpath=[app.chem_iupac_dir + '/opsin/opsin-2.4.0-jar-with-dependencies.jar'])
    opsin = jpype.JPackage('uk').ac.cam.ch.wwmm.opsin
    app.n2s = opsin.NameToStructure.getInstance()
    app.n2sconfig = opsin.NameToStructureConfig()
    app.n2sconfig.setAllowRadicals(True)

    @app.route('/ping')
    def ping():
        return 'pong'


    from chem_iupac.controller.api import ctrl
    app.register_blueprint(ctrl)


    return app
