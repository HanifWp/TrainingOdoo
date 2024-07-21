# -*- coding: utf-8 -*-
{
    "name": "ini_module",
    "description": "Pelatihan Odoo, set up nya gado-gado",
    "author": "Lord H",
    "version": "17.0.1.0.0",
    "category": "Others",
    "license": "OPL-1",
	# Depencicy
    "depends": [
        "base",
        "mail",
        "hr"],
        
    "data": [
        "security/ir.model.access.csv",
        "views/views.xml"
    ],
    "auto_install": False,
    "installable": True,
    "application": True,
    "external_dependencies": {"python" : {}} 


}