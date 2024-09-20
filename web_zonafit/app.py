from flask import Flask,render_template,redirect,url_for
from cliente_DAO import ClienteDAO
from cliente import Cliente
from cliente_form import ClienteForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'llave_secreta'



@app.route('/')
@app.route('/index')
@app.route('/home')
def inicio():
    # Recuperamos los clientes de la db
    clientes = ClienteDAO.select()

    # Creamos un obj de cliente vacío
    cliente = Cliente()
    # Creamos un obj de tipo clienteForm
    cliente_form = ClienteForm(obj=cliente)

    return render_template('index.html',clientes=clientes,forma=cliente_form)

@app.route('/guardar',methods=['POST'])
def guardar():
    # Creamos los obj vacíos
    cliente = Cliente()
    cliente_form = ClienteForm(obj=cliente)
    if cliente_form.validate_on_submit:
        # llenamos el obj cliente con los valores del form
        cliente_form.populate_obj(cliente)

        if not cliente.id: #Si el id es vacío, regresa True
            # Guardamos el nuevo cliente en la base de datos
            ClienteDAO.insert(cliente)
        else:
            ClienteDAO.update(cliente)    

        # Redireccionar a la página de inicio
        return redirect(url_for('inicio'))
    
@app.route('/limpiar')
def limpiar():
    return redirect(url_for('inicio'))

@app.route('/editar/<int:id>')
def editar(id):
    cliente = ClienteDAO.select_for_id(id)
    cliente_forma = ClienteForm(obj=cliente)
    clientes_db = ClienteDAO.select()
    return render_template('index.html',clientes=clientes_db, forma=cliente_forma)
    
@app.route('/eliminar/<int:id>')
def eliminar(id):
    cliente = Cliente(id_cliente=id)
    ClienteDAO.delete(cliente)
    return redirect(url_for('inicio'))

if __name__ == '__main__':
    app.run(debug=True)