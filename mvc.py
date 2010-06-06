# -*- coding: utf-8 -*-
""" Web com operações CRUD """
# CherryPy
import cherrypy # CherryTemplate
import cherrytemplate
# SQLAlchemy
import sqlalchemy as sql

# Conecta ao bando
db = sql.create_engine('sqlite:///zoo.db') # Acesso aos metadados
metadata = sql.MetaData(db)
try:
# Carrega metadados da tabela
    zoo = sql.Table('zoo', metadata, autoload=True)
except: 
    # Define a estrutura da tabela zoo
    zoo = sql.Table('zoo', metadata,
        sql.Column('id', sql.Integer, primary_key=True),
        sql.Column('nome', sql.String(100), unique=True, nullable=False), 
        sql.Column('quantidade', sql.Integer, default=1),
        sql.Column('obs', sql.String(200), default='')
    )
    
    # Cria a tabela
    zoo.create()

# Os nomes das atributos
atributos = [col for col in zoo.columns.keys()]
atributos.remove('id')



class Root(object):
    """Raiz do site"""

    @cherrypy.expose
    def index(self, **args):
        """
        Lista os registros """
        msg = ''
        op = args.get('op') 
        ident = int(args.get('ident', 0))
        novo = {}
        
        for atributo in atributos:
            novo[atributo] = args.get(atributo)

        # Seleciona dados
        sel = zoo.select(order_by=zoo.c.nome)
        rec = sel.execute()
        # Gera a página principal a partir do modelo "index.html"
        return cherrytemplate.renderTemplate(file='index.html')

    @cherrypy.expose
    def create(self, **kwargs):
        novo = {}
        for atributo in atributos:
            novo[atributo] = kwargs[atributo]
        try:
            # Insere dados
            ins = zoo.insert()
            ins.execute(novo)
            msg = 'registro adicionado.'

        except sql.exceptions.IntegrityError:
            msg = 'registro existe.'

        raise cherrypy.HTTPRedirect('/')

    @cherrypy.expose
    def delete(self, **kwargs):
        # Remove dados
        ident = int(kwargs.get('ident', 0))
        rem = zoo.delete(zoo.c.id==ident)
        rem.execute()
        msg = 'registro removido.'

        raise cherrypy.HTTPRedirect('/')

    @cherrypy.expose
    def update(self, **kwargs):
        ident = int(kwargs.get('ident', 0))
        novo = {}

        for atributo in atributos:
            novo[atributo] = kwargs[atributo]

        try:
            # Modifica dados
            mod = zoo.update(zoo.c.id==ident)
            mod.execute(novo)
            msg = 'registro modificado.'

        except sql.exceptions.IntegrityError:
            msg = 'registro existe.'
        raise cherrypy.HTTPRedirect('/')

    @cherrypy.expose
    def add(self):
        """
        Cadastra novos registros
        """
        # Gera a página de registro novo a partir do modelo "add.html"
        return cherrytemplate.renderTemplate(file='add.html')
    
    @cherrypy.expose
    def rem(self, ident):
        """
        Confirma a remoção de registros
        """
        # Seleciona o registro
        sel = zoo.select(zoo.c.id==ident)
        rec = sel.execute()
        res = rec.fetchone()
        
        # Gera a página de confirmar exclusão a partir do modelo "rem.html"
        return cherrytemplate.renderTemplate(file='rem.html')
    
    @cherrypy.expose
    def mod(self, ident): 
        """
        Modifica registros
        """
        # Seleciona o registro
        sel = zoo.select(zoo.c.id==ident)
        rec = sel.execute()
        res = rec.fetchone()
        
        # Gera a página de alteração de registro a partir do modelo "mod.html"
        return cherrytemplate.renderTemplate(file='mod.html')
        
# Inicia o servidor na porta 8080
cherrypy.quickstart(Root())