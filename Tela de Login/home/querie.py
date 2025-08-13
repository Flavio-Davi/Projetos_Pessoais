from cnx import SessionLocal
# Importa o modelo ORM que representa sua tabela
from models import Product

def prod():
    """
    Busca todos os nomes de produtos no banco de dados usando o ORM.
    Retorna uma lista de strings, ideal para o CTkOptionMenu.
    """
    with SessionLocal() as session:
        try:
            query_result = session.query(Product.ProductName).all()
            
            # O resultado é uma lista de tuplas, ex: [('Chai',), ('Chang',)].
            # Esta linha converte para uma lista de strings: ['Chai', 'Chang']
            product_names = [item[0] for item in query_result]
            
            return product_names
        
        except Exception as e:
            print(f"Erro ao buscar produtos: {e}")
            return ["Erro ao carregar"]