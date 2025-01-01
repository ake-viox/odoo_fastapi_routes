{
    'name': 'FastAPI Routes',
    'version': '17.0.1.0.0',
    'summary': 'Integrates Odoo with FastAPI for stock.picking data',
    'author': 'ake-viox',
    'category': 'Warehouse',
    'license': 'AGPL-3',
    'depends': ['stock'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/stock_picking_views.xml',
    ],
    'installable': True,
    'application': False,
}
