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
    company_id = fields.Many2one('res.company', # Model Tujuan
                                 string='Company', # Label untuk field ini
                                 default=lambda self : self.env.company) # Nilai default menggunakan lambda
    
    currency_id = fields.Many2one('res.currency', # Model Tujuan
                                  string='Currency',  # Label untuk field ini
                                  related='company_id.currency_id', # Field ini terkait dengan field currency_id dari model company_id
                                  store=True) # Nilai field ini akan disimpan dalam basis data, bukan secara dinamis
    
    point_rate = fields.Integer('Point Rate')
    amount = fields.Monetary('Amount', currency_id='currency_id')
    resource_ids = fields.Many2many(comodel_name ='resource.resource', # Model tujuan
                                    relation ='plannig_resource_rel', # Nama tabel relasi di database
                                    column1 ='planning_role_id', # Nama field di tabel relasi yang merujuk ke model saat ini
                                    column2 ='resource_id', # Nama kolom di tabel relasi yang merujuk ke model tujuan
                                    string='Resource') # Label untuk field di UI
    sequence = fields.Integer('Sequence')



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