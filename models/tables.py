# -*- coding: utf-8 -*-
db.define_table('cars', Field('name', length=512), Field('date', 'date'), Field('count', 'integer'),
                Field('distance', 'integer'), migrate=False)
