from odoo import models, fields, api


class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'Task'
    _inherit = ['mail.thread','mail.activity.mixin']


    # Fields:
    task_name = fields.Char(size=20, required=True)
    task_description = fields.Text(required=True)
    due_date = fields.Date(required=True)
    state = fields.Selection([
        ('new', 'New'),
        ('in progress', 'In Progress'),
        ('completed', 'Completed'),
    ], default='new',tracking=1)

    assign_to = fields.Many2one('res.partner', string="Assign To")
    assign_to_name = fields.Char(related='assign_to.name', string="Assignee Name", store=True)

    ################################################## Start Actions for State #####################################################
    # add actions buttons
    def action_new(self):
        for rec in self:
            print('inside new action')
            rec.state = 'new'
            # rec.write({
            #     'state':'new'
            # })

    def action_in_progress(self):
        for rec in self:
            print('inside in progress action')
            rec.state = 'in progress'
            # rec.write({
            #     'state':'in progress'
            # })

    def action_completed(self):
        for rec in self:
            print('inside completed action')
            rec.state = 'completed'
            # rec.write({
            #     'state':'completed'
            # })

    ################################################## End Actions for State #####################################################
