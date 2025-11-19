from email.policy import default

from odoo import models, fields, api


class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'Task'

    # Fields:
    task_name = fields.Char(size=20,required=1)
    task_description = fields.Text(required=1)
    due_date = fields.Date(required=True)
    state = fields.Selection([
        ('new','New'),
        ('in progress','In Progress'),
        ('completed','Completed'),
    ],default='new')

