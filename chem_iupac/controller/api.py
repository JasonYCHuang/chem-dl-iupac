import io
import json
from flask import (
    Blueprint, request, jsonify
)
from chem_iupac.controller.helper.settings import get_ip_white_list
from chem_iupac.model.iupac_model import IupacModel


ctrl = Blueprint('api', __name__)


@ctrl.before_app_request
def filter_remote_ip():
    trusted_servers = get_ip_white_list()
    # if request.remote_addr not in trusted_servers:
    #     abort(403)


@ctrl.route('/iupac_name', methods=['POST'])
def prediction():
    payload = request.json['smis']
    rsp = IupacModel.infer(payload)
    return jsonify(rsp)
