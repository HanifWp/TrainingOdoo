from odoo import _, api, fields, models
from random import randint

class PlanningRoleTraining(models.Model):
    _name = 'planning.role.training'
    _description = 'Planning Role Training'
    _order = 'name asc'
    
    def _get_default_color(self):
        return randint(1, 11)

    name = fields.Char('Nama Role', index=True)
    active = fields.Boolean('Active', default=True)
    color = fields.Integer('Color', default=_get_default_color)


#_rec_name =
#mencatat record dengan field tertentu
#default mencari field name
#apabila tidak mendefinisikan field nama, record akan menampilkan id
#contoh record menampilkan id = planning.role.training(1,)

#_order
#fungsinya sama seperti order di query
#mengambil data dari field priority, seqence atau id
#bisa diisi 2, cth 'name asc, id desc'
#default asc

#_log_access
#default property models
#if True = akan membentuk 4 fields (write_uid, write_date, created_date, create_uid)

#_check_company_auto
#True or False
#cek relevansi data