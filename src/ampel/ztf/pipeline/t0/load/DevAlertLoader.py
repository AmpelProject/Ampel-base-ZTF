#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tarfile
import fastavro
from ampel.base.AmpelAlert import AmpelAlert

def shape(alert_content):

    if alert_content.get('prv_candidates') is not None:
        pps = [el for el in alert_content['prv_candidates'] if el.get('candid') is not None]
        pps.insert(0,  alert_content['candidate'])
        return pps, [el for el in alert_content['prv_candidates'] if el.get('candid') is None]
    else:
        return [alert_content['candidate']], None

def load_from_tar(tar_file_path):

    tar_file = tarfile.open(tar_file_path, mode='r:gz')

    alert_list = list()
    for content in tar_file:
        alert = tar_file.extractfile(content)
        reader = fastavro.reader(alert)
        alert_content = next(reader, None)
        alert_list.append(AmpelAlert(alert_content['objectId'], *shape(alert_content)))

    return alert_list