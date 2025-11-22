from odoo import models,fields,api
from odoo.exceptions import UserError,ValidationError



class Departments(models.Model):
	_inherit = "hr.department"


	General_Doctors = fields.One2many("hr.employee","department_id",domain=[('category','=','General')])
	Private_Doctors = fields.One2many("hr.employee","department_id",domain=[('category','=','Private')])

class Doctors(models.Model):
	_inherit = "hr.employee"

	category = fields.Many2one("hospital.categoryy")


class Patients(models.Model):
	_inherit = "res.partner"


class Diagnosis(models.Model):
	_inherit = "sale.order"

	age = fields.Integer(required=True)
	symptoms = fields.Char()
	examinations = fields.Many2many("hospital.examination")
	case = fields.Selection([
		('interview','Doctor Interview'),
		('exam','Examination'),
		('surgery','Surgery'),
		('intensive','Intensive Care'),
		('done','Done')
		],default="interview")

	def examination(self):
		for rec in self:
			rec.case = "exam"

	def surgery(self):
		for rec in self:
			rec.case = "surgery"

	def intensive(self):
		for rec in self:
			rec.case = "intensive"

	def done(self):
		for rec in self:
			rec.case = "done"

	@api.model
	def create(self,vals):

		diag = super(Diagnosis,self).create(vals)
		if diag.age < 15 :
			raise UserError("You Can't Register Patients Who Is Younger Than 15")
		else :
			return diag


class Medicines(models.Model):

	_inherit = "product.template"

class Examinations(models.Model):
	_name = "hospital.examination"

	name = fields.Char()

class Categories(models.Model):

	_name = "hospital.categoryy"

	name = fields.Char()
	doctors = fields.One2many("hr.employee","category")
