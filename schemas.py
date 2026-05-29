from pydantic import BaseModel

class FigurinhaBase(BaseModel):
    nome_jogador: str
    pais: str
    posicao: str
    numero_camisa: int
    raridade: str = "Comum"
    repetida: bool = False

class FigurinhaCreate(FigurinhaBase):
    pass

class FigurinhaResponse(FigurinhaBase):
    cod_figurinha: int

    class Config:
        from_attributes = True