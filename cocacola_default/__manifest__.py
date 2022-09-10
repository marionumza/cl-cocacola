##############################################################################
#
#    Copyright (C) 2021  Quilsoft  (http://www.quilsoft.com)
#    All Rights Reserved.
#
##############################################################################

{
    'name': 'cocacola',
    'version': '15.0.1.0.0',
    'category': 'Tools',
    'summary': "Proyect module for Coca Cola",
    'author': "Crumges",
    'website': 'crumges.com',
    'license': 'AGPL-3',
    'depends': [
            # Modulos odoo
            #'crm',
            #'project',
            #'stock',
            #'mrp',
            #'sale_management',
            #'account_accountant',
            #'purchase',
            #'hr_attendance',
            #'contacts',
#            'calendar',
#            'account',
            # Modulos quilsoft


        ],
    'installable': True,

    'env-ver': '2',
    'odoo-license': 'CE',
    'config': [

        # 'addons_path' is always computed looking for the repositories in sources
        # 'data_dir' is a fixed location inside docker odoo image

        # You should use 2 worker threads + 1 cron thread per available CPU,
        # and 1 CPU per 10 concurent users.
        # if ommited oe will calculate workers and cron´s based on # of cpu
        #        'workers = 0',
                'max_cron_threads = 1',

        # Number of requests a worker will process before being recycled and
        # restarted. Defaults to 8192 if ommited
                'limit_request = 8192',

        # Maximum allowed virtual memory per worker. If the limit is exceeded,
        # the worker is killed and recycled at the end of the current request.
        # Defaults to 640MB
                'limit_memory_soft = 2147483648',

        # Hard limit on virtual memory, any worker exceeding the limit will be
        # immediately killed without waiting for the end of the current request
        # processing. Defaults to 768MB.
                'limit_memory_hard = 2684354560',
    ],

    'port': '8069',

    'git-repos': [
        'https://github.com/marionumza/cl-cocacola.git',

        # Quilsoft
        #'git@github.com:quilsoft-org/cocacola.git -b main',

        # OCA
        # 'https://github.com/OCA/brand oca-brand',
        #'https://github.com/OCA/web OCA-web',
        #'https://github.com/OCA/server-ux.git OCA-server-ux',

        # Quilsoft-Org
        # 'https://github.com/ingadhoc/account-financial-tools adhoc-account-financial-tools',
        # 'https://github.com/ingadhoc/account-payment adhoc-account-payment',
        # 'https://github.com/ingadhoc/aeroo_reports.git',
        # 'https://github.com/ingadhoc/argentina-sale adhoc-argentina-sale',
        #'https://github.com/ingadhoc/odoo-argentina adhoc-odoo-argentina',
        # 'https://github.com/ingadhoc/odoo-argentina-ee adhoc-odoo-argentina-ee',
        # 'https://github.com/ingadhoc/stock adhoc-stock',
    ],

    # list of images to use in the form 'name image-url'
    'docker-images': [
        'odoo marionumza/mvp_odoo:15',
        'postgres postgres:10.1-alpine',
    ]
}
