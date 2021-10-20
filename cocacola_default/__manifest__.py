{
    'name': 'cocacola',
    'version': '14.0.1.0.0',
    'category': 'Tools',
    'summary': 'Proyecto Cocacola',
    'author': 'Quilsoft',
    'depends': [
    ],
    'data': [
    ],
    'test': [
    ],
    'installable': True,
    'application': False,
    'env-ver': '2',
    'odoo-license': 'CE',
    'port': '8069',
    'config': [
        'max_cron_threads = 1',
    ],
    'git-repos': [
        'https://github.com/jobiols/cl-cocacola.git',
        # todos juntos
        # ==========================================================================================
        # 'https://github.com/OCA/account-closing oca-account-closing',
        'https://github.com/OCA/account-financial-reporting oca-account-financial-reporting',  # noqa
        'https://github.com/OCA/account-financial-tools oca-account-financial-tools',
        'https://github.com/OCA/account-payment oca-account-payment',
        # 'https://github.com/OCA/apps-store oca-apps-store',
        # 'https://github.com/OCA/bank-payment oca-bank-payment',
        # 'https://github.com/OCA/business-requirement oca-business-requirement',
        # 'https://github.com/OCA/commission oca-commission',
        # 'https://github.com/OCA/contract oca-contract',
        # 'https://github.com/OCA/credit-control oca-credit-control',
        # 'https://github.com/OCA/crm oca-crm',
        # 'https://github.com/OCA/currency oca-currency',
        # 'https://github.com/OCA/ddmrp oca-ddmrp',
        # 'https://github.com/OCA/delivery-carrier oca-delivery-carrier',
        # 'https://github.com/OCA/e-commerce oca-e-commerce',
        # 'https://github.com/OCA/event oca-event',
        # 'https://github.com/OCA/field-service oca-field-service',
        # 'https://github.com/OCA/geospatial oca-geospatial',
        # 'https://github.com/OCA/hr oca-hr',
        # 'https://github.com/OCA/hr-timesheet oca-hr-timesheet',
        # 'https://github.com/OCA/knowledge oca-knowledge',
        # 'https://github.com/OCA/management-system oca-management-system',
        # 'https://github.com/OCA/manufacture oca-manufacture',
        # 'https://github.com/OCA/manufacture-reporting oca-manufacture-reporting',
        # 'https://github.com/OCA/margin-analysis oca-margin-analysis',
        # 'https://github.com/OCA/multi-company oca-multi-company',
        # 'https://github.com/OCA/oca-custom oca-oca-custom',
        # 'https://github.com/OCA/operating-unit oca-operating-unit',
        # 'https://github.com/OCA/partner-contact oca-partner-contact',
        # 'https://github.com/OCA/pos oca-pos',
        # 'https://github.com/OCA/product-attribute oca-product-attribute',
        # 'https://github.com/OCA/product-pack oca-product-pack',
        # 'https://github.com/OCA/project oca-project',
        # 'https://github.com/OCA/project-reporting oca-project-reporting',
        # 'https://github.com/OCA/purchase-workflow oca-purchase-workflow',
        # 'https://github.com/OCA/queue oca-queue',
        # 'https://github.com/OCA/report-print-send oca-report-print-send',
        'https://github.com/OCA/reporting-engine oca-reporting-engine',
        # 'https://github.com/OCA/sale-reporting oca-sale-reporting',
        'https://github.com/OCA/sale-workflow oca-sale-workflow',
        # 'https://github.com/OCA/server-auth oca-server-auth',
        # 'https://github.com/OCA/server-backend oca-server-backend',
        'https://github.com/OCA/server-tools oca-server-tools',
        'https://github.com/OCA/server-ux oca-server-ux',
        # 'https://github.com/OCA/social oca-social',
        # 'https://github.com/OCA/stock-logistics-barcode oca-stock-logistics-barcode',
        # 'https://github.com/OCA/stock-logistics-reporting oca-stock-logistics-reporting', # noqa
        # 'https://github.com/OCA/stock-logistics-transport oca-stock-logistics-transport', # noqa
        # 'https://github.com/OCA/stock-logistics-warehouse oca-stock-logistics-warehouse', # noqa
        # 'https://github.com/OCA/stock-logistics-workflow oca-stock-logistics-workflow',
        # 'https://github.com/OCA/timesheet oca-timesheet',
        # 'https://github.com/OCA/vertical-association oca-vertical-association',
        'https://github.com/OCA/web oca-web',
        # 'https://github.com/OCA/website oca-website',
        # 'https://github.com/OCA/bank-payment oca-bank-payment',
        # 'https://github.com/OCA/account-analytic',
        # 'https://github.com/ingadhoc/account-analytic ingadhoc-account-analytic',
        # 'https://github.com/ingadhoc/hr ingadhoc-hr',
        # 'https://github.com/ingadhoc/multi-company ingadhoc-multi-company',
        # 'https://github.com/ingadhoc/multi-store ingadhoc-multi-store',

        # Fix porque falla la instalacion de l10n_ar_ux

        # 'https://github.com/jobiols/odoo-argentina jobiols-odoo-argentina',
    ],
    'docker-images': [
        'odoo jobiols/odoo-jeo:14.0',
        'postgres postgres:10.1-alpine',
    ]
}
