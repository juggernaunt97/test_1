# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Advanced Sale',
    'version' : 'v1.0',
    'summary': 'this app for everyone',
    'sequence': 1,
    'description': """ Alien Software""",
    'category': 'productivity',
    'website': '',
    'images': [],
    'author': "Chau Nguyen",
    'depends': ['base'],
    'data': [
        'views/sale_order.xml',
        'views/list_code.xml',
        'security/groups.xml',
        'security/ir.model.access.csv',
        'wizards/update_code.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}