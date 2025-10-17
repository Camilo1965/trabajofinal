"""Script para generar el diagrama Entidad-Relación de la base de datos."""

import os
from graphviz import Digraph


def generate_er_diagram():
    """Genera el diagrama entidad-relación del sistema."""
    dot = Digraph(comment='Diagrama Entidad-Relación - Sistema de Gestión', format='png')
    dot.attr(rankdir='TB')
    dot.attr('node', shape='box')
    
    # Entidades simplificadas
    dot.node('Users', 'Users\n---\nPK: user_id\nusername (UNIQUE)\nemail (UNIQUE)\npassword_hash\nrole\nfull_name\nis_active\ncreated_at\nupdated_at')
    dot.node('UserProfiles', 'UserProfiles\n---\nPK: profile_id\nFK: user_id\nphone\naddress\ndate_of_birth\nupdated_at')
    dot.node('UserPermissions', 'UserPermissions\n---\nPK: permission_id\nFK: user_id\npermission_name\ngranted_at')
    dot.node('Suppliers', 'Suppliers\n---\nPK: supplier_id\nname\ncontact_email\nphone\ncreated_at')
    dot.node('Products', 'Products\n---\nPK: product_id\nname\nprice\ncategory\nstock_quantity\nsku (UNIQUE)\nFK: supplier_id\nis_available\ncreated_at')
    dot.node('ProductReviews', 'ProductReviews\n---\nPK: review_id\nFK: product_id\nFK: user_id\nrating\ncomment\ncreated_at')
    dot.node('Orders', 'Orders\n---\nPK: order_id\nFK: user_id\ntotal_amount\norder_status\ncreated_at\nupdated_at')
    dot.node('OrderItems', 'OrderItems\n---\nPK: item_id\nFK: order_id\nFK: product_id\nquantity\nunit_price\nsubtotal')
    dot.node('Payments', 'Payments\n---\nPK: payment_id\nFK: order_id\nFK: user_id\namount\npayment_method\npayment_status\ntransaction_id\ncreated_at')
    dot.node('PaymentDetails', 'PaymentDetails\n---\nPK: details_id\nFK: payment_id\ncard_last_four\nbilling_address\nerror_message')
    
    # Relaciones
    dot.edge('Users', 'UserProfiles', label='1:1 has')
    dot.edge('Users', 'UserPermissions', label='1:N has')
    dot.edge('Users', 'ProductReviews', label='1:N writes')
    dot.edge('Users', 'Orders', label='1:N places')
    dot.edge('Users', 'Payments', label='1:N makes')
    dot.edge('Suppliers', 'Products', label='1:N supplies')
    dot.edge('Products', 'ProductReviews', label='1:N has')
    dot.edge('Products', 'OrderItems', label='1:N in')
    dot.edge('Orders', 'OrderItems', label='1:N contains')
    dot.edge('Orders', 'Payments', label='1:N has')
    dot.edge('Payments', 'PaymentDetails', label='1:1 has')
    
    # Guardar diagrama
    output_path = os.path.join(os.path.dirname(__file__), 'er_diagram')
    dot.render(output_path, cleanup=True)
    print(f"✓ Diagrama ER generado: {output_path}.png")


def main():
    """Genera el diagrama ER."""
    print("Generando diagrama Entidad-Relación...\n")
    
    try:
        generate_er_diagram()
        print("\n✓ Diagrama ER generado exitosamente!")
    except Exception as e:
        print(f"\n❌ Error al generar diagrama ER: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
