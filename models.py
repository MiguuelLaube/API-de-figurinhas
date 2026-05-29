from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Figurinha(Base):
    __tablename__ = "tb_figurinhas"

    cod_figurinha = Column(Integer, primary_key=True, index=True)
    nome_jogador = Column(String(100), nullable=False)
    pais = Column(String(50), nullable=False)
    posicao = Column(String(50), nullable=False)
    numero_camisa = Column(Integer, nullable=False)
    raridade = Column(String(20), nullable=False, default="Comum")
    repetida = Column(Boolean, nullable=False, default=False)