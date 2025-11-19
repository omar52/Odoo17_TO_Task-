from odoo import models, fields, api


class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'Task'

    # Fields:
    task_name = fields.Char(size=20, required=True)
    task_description = fields.Text(required=True)
    due_date = fields.Date(required=True)
    state = fields.Selection([
        ('new', 'New'),
        ('in progress', 'In Progress'),
        ('completed', 'Completed'),
    ], default='new')

    assign_to = fields.Many2one('res.partner', string="Assign To")
