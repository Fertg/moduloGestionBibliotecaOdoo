# -*- coding: utf-8 -*- 
 
from odoo import models, fields, api 
 

class lectores(models.Model): 
     _name = 'biblioteca.lectores' 
     _description = 'Gestión de Lectores'  
     dni = fields.Char(string='Dni*', required=True, help="Campo obligatorio") 
     nombre = fields.Char(string='Nombre') 
     apellidos = fields.Char(string='Apellidos') 
     fechaNac = fields.Date('Fecha de Nacimiento') 
     fotografia=fields.Image(max_width=200, max_height=200) 
     libro=fields.Many2many(comodel_name='biblioteca.libro',relation='lector_libro',column1='isbn',column2='dni',string='Libros en prestamo:') 
       
class libro(models.Model): 
     _name = 'biblioteca.libro' 
     _description = 'Gestión de Libros'  
     isbn = fields.Char(string='Isbn *', required=True, help="Campo obligatorio") 
     titulo = fields.Char(string="Titulo") 
     autor = fields.Char(string="Autor") 
     abstract = fields.Binary('Abstract') 
     editorial = fields.Char(string='Editorial') 
     fechaPub = fields.Date('Fecha de Publicación')     
     estanteria=fields.Integer('Numero de estanteria') 
     #usuarioPrestamo=fields.Char(string='Usuario en Prestamo') 
     estanteria=fields.Many2one('biblioteca.estanteria',cascade=True) 

     lectores=fields.Many2many(comodel_name='biblioteca.lectores',relation='lector_libro',column1='dni',column2='isbn',string='Usuarios con el libro:')    
class estanteria(models.Model): 
     _name = 'biblioteca.estanteria' 
     _description = 'Gestión de Estanterias'  
     identificador = fields.Char(string='identificador', required=True, help="Campo obligatorio") 
     nombre = fields.Char(string='nombre')   
     plantas=fields.Many2one('biblioteca.planta') #varios libros se asocian a una estanteria
     listaLibros=fields.One2many(string='Listados de Libros', inverse_name='estanteria',comodel_name='biblioteca.libro')
class planta(models.Model): 
     _name = 'biblioteca.planta' 
     _description = 'Gestión de Plantas'  
     identificador = fields.Char(string='identificador', required=True, help="Campo obligatorio") 
     nombre = fields.Char(string='nombre')  
     #listadoEstanterias = fields.Char(string='Nombre Planta')
     listadoEstanterias = fields.One2many(string='Listados Estanterias', inverse_name='plantas',comodel_name='biblioteca.estanteria')