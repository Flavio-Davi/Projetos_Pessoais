from sqlalchemy import Column, Integer, String, Float
from cnx import Base

class Product(Base):
    """
    Esta classe mapeia para a tabela 'products' no banco de dados 'kaggle'.
    """
    __tablename__ = 'products'

    ProductId = Column(Integer, primary_key=True)
    ProductName = Column(String(50), nullable=False)
    Supplier = Column(String(50))
    ProductCost = Column(Float)