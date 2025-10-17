"""Script para generar diagramas UML del Sistema de Gestión."""

import sys
import os

# Agregar el directorio src al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from graphviz import Digraph


def generate_user_class_diagram():
    """Genera el diagrama de clases del módulo de usuarios."""
    dot = Digraph(comment='Diagrama de Clases - Gestión de Usuarios', format='png')
    dot.attr(rankdir='TB')
    dot.attr('node', shape='box')
    
    # Clases con descripción simplificada
    dot.node('UserRole', 'UserRole\n(Enum)\n---\nADMIN\nMANAGER\nEMPLOYEE\nCLIENT')
    dot.node('User', 'User\n---\nuser_id: int\nusername: str\nemail: str\nrole: UserRole\n...\n---\nactivate()\ndeactivate()\nchange_password()')
    dot.node('UserProfile', 'UserProfile\n---\nprofile_id: int\nuser_id: int\nphone: str\naddress: str\n...') 
    dot.node('UserRepository', 'UserRepository\n---\nsave(user)\nfind_by_id(id)\nfind_by_username()\nfind_all()\nupdate(user)\ndelete(id)')
    dot.node('UserController', 'UserController\n---\nuser_repository\n---\nregister_user()\nauthenticate()\nget_user()\nupdate_user()\ndelete_user()\nlist_all_users()')
    
    # Relaciones
    dot.edge('User', 'UserRole', label='uses')
    dot.edge('User', 'UserProfile', label='has 0..1')
    dot.edge('UserController', 'UserRepository', label='uses')
    dot.edge('UserController', 'User', label='manages')
    dot.edge('UserRepository', 'User', label='stores')
    
    # Guardar diagrama
    output_path = os.path.join(os.path.dirname(__file__), 'user_class_diagram')
    dot.render(output_path, cleanup=True)
    print(f"✓ Diagrama de clases de usuarios generado: {output_path}.png")


def generate_product_class_diagram():
    """Genera el diagrama de clases del módulo de productos."""
    dot = Digraph(comment='Diagrama de Clases - Gestión de Productos', format='png')
    dot.attr(rankdir='TB')
    dot.attr('node', shape='box')
    
    # Clases con descripción simplificada
    dot.node('ProductCategory', 'ProductCategory\n(Enum)\n---\nELECTRONICS\nCLOTHING\nFOOD\nBOOKS\nTOYS\nFURNITURE\nOTHER')
    dot.node('Product', 'Product\n---\nproduct_id: int\nname: str\nprice: float\ncategory: ProductCategory\nstock_quantity: int\nsku: str\n...\n---\nupdate_price()\nadd_stock()\nreduce_stock()\nis_in_stock()\nset_availability()')
    dot.node('Supplier', 'Supplier\n---\nsupplier_id: int\nname: str\ncontact_email: str\nphone: str')
    dot.node('ProductReview', 'ProductReview\n---\nreview_id: int\nproduct_id: int\nuser_id: int\nrating: int\ncomment: str')
    dot.node('ProductRepository', 'ProductRepository\n---\nsave(product)\nfind_by_id(id)\nfind_by_sku(sku)\nfind_by_category()\nfind_all()\nupdate(product)\ndelete(id)')
    dot.node('ProductController', 'ProductController\n---\nproduct_repository\n---\ncreate_product()\nget_product()\nupdate_product()\ndelete_product()\nlist_all_products()\nupdate_price()\nadd_stock()\nreduce_stock()')
    
    # Relaciones
    dot.edge('Product', 'ProductCategory', label='uses')
    dot.edge('Product', 'Supplier', label='supplied by 0..1')
    dot.edge('Product', 'ProductReview', label='has many')
    dot.edge('ProductController', 'ProductRepository', label='uses')
    dot.edge('ProductController', 'Product', label='manages')
    dot.edge('ProductRepository', 'Product', label='stores')
    
    # Guardar diagrama
    output_path = os.path.join(os.path.dirname(__file__), 'product_class_diagram')
    dot.render(output_path, cleanup=True)
    print(f"✓ Diagrama de clases de productos generado: {output_path}.png")


def generate_payment_class_diagram():
    """Genera el diagrama de clases del módulo de pagos."""
    dot = Digraph(comment='Diagrama de Clases - Procesamiento de Pagos', format='png')
    dot.attr(rankdir='TB')
    dot.attr('node', shape='box')
    
    # Clases con descripción simplificada
    dot.node('PaymentStatus', 'PaymentStatus\n(Enum)\n---\nPENDING\nPROCESSING\nCOMPLETED\nFAILED\nREFUNDED\nCANCELLED')
    dot.node('PaymentMethod', 'PaymentMethod\n(Enum)\n---\nCREDIT_CARD\nDEBIT_CARD\nPAYPAL\nBANK_TRANSFER\nCASH')
    dot.node('Payment', 'Payment\n---\npayment_id: int\norder_id: int\nuser_id: int\namount: float\nmethod: PaymentMethod\nstatus: PaymentStatus\n...\n---\nprocess()\ncomplete()\nfail()\nrefund()\ncancel()\nis_successful()')
    dot.node('PaymentDetails', 'PaymentDetails\n---\ndetails_id: int\npayment_id: int\ncard_last_four: str\nbilling_address: str')
    dot.node('Order', 'Order\n---\norder_id: int\nuser_id: int\ntotal_amount: float\nitems: List[OrderItem]\n---\nadd_item()\ncalculate_total()')
    dot.node('OrderItem', 'OrderItem\n---\nitem_id: int\norder_id: int\nproduct_id: int\nquantity: int\nunit_price: float\nsubtotal: float')
    dot.node('PaymentRepository', 'PaymentRepository\n---\nsave(payment)\nfind_by_id(id)\nfind_by_user_id()\nfind_by_order_id()\nfind_by_status()\nfind_all()\nupdate(payment)\ndelete(id)')
    dot.node('PaymentController', 'PaymentController\n---\npayment_repository\n---\ncreate_payment()\nget_payment()\nprocess_payment()\ncomplete_payment()\nrefund_payment()\ncancel_payment()\nlist_payments_by_user()\nlist_payments_by_status()')
    
    # Relaciones
    dot.edge('Payment', 'PaymentStatus', label='uses')
    dot.edge('Payment', 'PaymentMethod', label='uses')
    dot.edge('Payment', 'PaymentDetails', label='has 0..1')
    dot.edge('Order', 'Payment', label='has 0..1')
    dot.edge('Order', 'OrderItem', label='contains many')
    dot.edge('PaymentController', 'PaymentRepository', label='uses')
    dot.edge('PaymentController', 'Payment', label='manages')
    dot.edge('PaymentRepository', 'Payment', label='stores')
    
    # Guardar diagrama
    output_path = os.path.join(os.path.dirname(__file__), 'payment_class_diagram')
    dot.render(output_path, cleanup=True)
    print(f"✓ Diagrama de clases de pagos generado: {output_path}.png")


def generate_component_diagram():
    """Genera el diagrama de componentes del sistema."""
    dot = Digraph(comment='Diagrama de Componentes - Sistema de Gestión', format='png')
    dot.attr(rankdir='TB')
    dot.attr('node', shape='component')
    
    # Capa de presentación
    dot.node('View', '<<component>>\nVista\n(Console/Web UI)')
    
    # Capa de controladores
    with dot.subgraph(name='cluster_controllers') as c:
        c.attr(label='Controladores', style='dashed')
        c.node('UserController', '<<component>>\nUserController')
        c.node('ProductController', '<<component>>\nProductController')
        c.node('PaymentController', '<<component>>\nPaymentController')
    
    # Capa de modelos
    with dot.subgraph(name='cluster_models') as c:
        c.attr(label='Modelos de Dominio', style='dashed')
        c.node('UserModel', '<<component>>\nUser Model')
        c.node('ProductModel', '<<component>>\nProduct Model')
        c.node('PaymentModel', '<<component>>\nPayment Model')
    
    # Capa de repositorios
    with dot.subgraph(name='cluster_repositories') as c:
        c.attr(label='Capa de Persistencia', style='dashed')
        c.node('UserRepository', '<<component>>\nUserRepository')
        c.node('ProductRepository', '<<component>>\nProductRepository')
        c.node('PaymentRepository', '<<component>>\nPaymentRepository')
    
    # Base de datos
    dot.node('Database', '<<database>>\nBase de Datos\n(SQLite/MySQL)', shape='cylinder')
    
    # API externa
    dot.node('PaymentGateway', '<<external>>\nPayment Gateway\n(Stripe/PayPal)', shape='component', style='filled', fillcolor='lightgray')
    
    # Relaciones
    dot.edge('View', 'UserController', label='usa')
    dot.edge('View', 'ProductController', label='usa')
    dot.edge('View', 'PaymentController', label='usa')
    
    dot.edge('UserController', 'UserModel', label='gestiona')
    dot.edge('ProductController', 'ProductModel', label='gestiona')
    dot.edge('PaymentController', 'PaymentModel', label='gestiona')
    
    dot.edge('UserController', 'UserRepository', label='usa')
    dot.edge('ProductController', 'ProductRepository', label='usa')
    dot.edge('PaymentController', 'PaymentRepository', label='usa')
    
    dot.edge('UserRepository', 'Database', label='persiste en')
    dot.edge('ProductRepository', 'Database', label='persiste en')
    dot.edge('PaymentRepository', 'Database', label='persiste en')
    
    dot.edge('PaymentController', 'PaymentGateway', label='integra con')
    
    # Guardar diagrama
    output_path = os.path.join(os.path.dirname(__file__), 'component_diagram')
    dot.render(output_path, cleanup=True)
    print(f"✓ Diagrama de componentes generado: {output_path}.png")


def generate_deployment_diagram():
    """Genera el diagrama de despliegue del sistema."""
    dot = Digraph(comment='Diagrama de Despliegue - Sistema de Gestión', format='png')
    dot.attr(rankdir='TB')
    
    # Nodo Cliente
    with dot.subgraph(name='cluster_client') as c:
        c.attr(label='<<device>>\nCliente', style='dashed')
        c.node('Browser', '<<artifact>>\nNavegador Web\n(Chrome/Firefox)', shape='note')
        c.node('ConsoleApp', '<<artifact>>\nAplicación\nConsola', shape='note')
    
    # Nodo Servidor de Aplicación
    with dot.subgraph(name='cluster_appserver') as c:
        c.attr(label='<<device>>\nServidor de Aplicación\n(Linux/Windows)', style='dashed')
        c.node('Python', '<<execution environment>>\nPython 3.11+', shape='component')
        c.node('AppCode', '<<artifact>>\nSistema de Gestión\n(src/)', shape='note')
    
    # Nodo Servidor de Base de Datos
    with dot.subgraph(name='cluster_dbserver') as c:
        c.attr(label='<<device>>\nServidor de BD\n(Linux)', style='dashed')
        c.node('DBEngine', '<<execution environment>>\nSQLite/MySQL', shape='component')
        c.node('Database', '<<artifact>>\nBase de Datos', shape='cylinder')
    
    # Nodo Servicios en la Nube
    with dot.subgraph(name='cluster_cloud') as c:
        c.attr(label='<<device>>\nServicios Cloud', style='dashed')
        c.node('PaymentService', '<<artifact>>\nPayment Gateway\nAPI', shape='note')
    
    # Relaciones
    dot.edge('Browser', 'Python', label='HTTP/HTTPS')
    dot.edge('ConsoleApp', 'Python', label='Terminal I/O')
    dot.edge('Python', 'AppCode', label='ejecuta')
    dot.edge('AppCode', 'DBEngine', label='SQL\nTCP/IP')
    dot.edge('DBEngine', 'Database', label='almacena')
    dot.edge('AppCode', 'PaymentService', label='REST API\nHTTPS')
    
    # Guardar diagrama
    output_path = os.path.join(os.path.dirname(__file__), 'deployment_diagram')
    dot.render(output_path, cleanup=True)
    print(f"✓ Diagrama de despliegue generado: {output_path}.png")


def generate_sequence_diagram():
    """Genera un diagrama de secuencia para procesamiento de pagos."""
    dot = Digraph(comment='Diagrama de Secuencia - Procesamiento de Pago', format='png')
    dot.attr(rankdir='TB')
    dot.attr('node', shape='box')
    
    # Actores
    dot.node('User', 'Usuario', shape='oval')
    dot.node('View', 'Vista')
    dot.node('Controller', 'PaymentController')
    dot.node('Payment', 'Payment')
    dot.node('Repository', 'PaymentRepository')
    dot.node('Gateway', 'Payment Gateway', shape='component')
    
    # Secuencia de mensajes (simulado con nodos y aristas)
    # Esto es una simplificación; para diagramas de secuencia reales
    # se recomienda usar PlantUML
    
    dot.edge('User', 'View', label='1: create_payment()')
    dot.edge('View', 'Controller', label='2: create_payment()')
    dot.edge('Controller', 'Payment', label='3: new Payment()')
    dot.edge('Controller', 'Repository', label='4: save(payment)')
    dot.edge('Repository', 'Controller', label='5: payment')
    dot.edge('Controller', 'View', label='6: payment_id')
    dot.edge('User', 'View', label='7: process_payment()')
    dot.edge('View', 'Controller', label='8: process_payment(id)')
    dot.edge('Controller', 'Payment', label='9: process()')
    dot.edge('Controller', 'Gateway', label='10: process_transaction()')
    dot.edge('Gateway', 'Controller', label='11: success/failure')
    dot.edge('Controller', 'Payment', label='12: complete()/fail()')
    dot.edge('Controller', 'Repository', label='13: update(payment)')
    dot.edge('Controller', 'View', label='14: result')
    dot.edge('View', 'User', label='15: show_result()')
    
    # Guardar diagrama
    output_path = os.path.join(os.path.dirname(__file__), 'sequence_diagram')
    dot.render(output_path, cleanup=True)
    print(f"✓ Diagrama de secuencia generado: {output_path}.png")


def main():
    """Genera todos los diagramas."""
    print("Generando diagramas UML del Sistema de Gestión...\n")
    
    try:
        generate_user_class_diagram()
        generate_product_class_diagram()
        generate_payment_class_diagram()
        generate_component_diagram()
        generate_deployment_diagram()
        generate_sequence_diagram()
        
        print("\n✓ Todos los diagramas han sido generados exitosamente!")
        print(f"  Ubicación: {os.path.dirname(__file__)}/")
    except Exception as e:
        print(f"\n❌ Error al generar diagramas: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
