from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

import models
import schemas
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Figurinhas da Copa",
    description="API para gerenciamento de figurinhas do álbum da Copa do Mundo"
)

# Configuração aberta de CORS (Compartilhamento de Recursos de Origem Cruzada)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Listar todas as figurinhas ──────────────────────────────────────
@app.get("/figurinhas/", response_model=List[schemas.FigurinhaResponse])
def listar_figurinhas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    lista = db.query(models.Figurinha).offset(skip).limit(limit).all()
    return lista

# ── Criar uma figurinha ─────────────────────────────────────────────
@app.post("/figurinhas/", response_model=schemas.FigurinhaResponse, status_code=201)
def criar_figurinha(figurinha: schemas.FigurinhaCreate, db: Session = Depends(get_db)):
    nova_figurinha = models.Figurinha(
        nome_jogador=figurinha.nome_jogador,
        pais=figurinha.pais,
        posicao=figurinha.posicao,
        numero_camisa=figurinha.numero_camisa,
        raridade=figurinha.raridade,
        repetida=figurinha.repetida
    )
    db.add(nova_figurinha)
    db.commit()
    db.refresh(nova_figurinha)
    return nova_figurinha

# ── Buscar figurinha por ID ─────────────────────────────────────────
@app.get("/figurinhas/{cod_figurinha}", response_model=schemas.FigurinhaResponse)
def buscar_figurinha(cod_figurinha: int, db: Session = Depends(get_db)):
    figurinha = db.query(models.Figurinha).filter(models.Figurinha.cod_figurinha == cod_figurinha).first()
    if figurinha is None:
        raise HTTPException(status_code=404, detail="Figurinha não encontrada.")
    return figurinha

# ── Atualizar figurinha ─────────────────────────────────────────────
@app.put("/figurinhas/{cod_figurinha}", response_model=schemas.FigurinhaResponse)
def atualizar_figurinha(cod_figurinha: int, figurinha_nova: schemas.FigurinhaCreate, db: Session = Depends(get_db)):
    figurinha = db.query(models.Figurinha).filter(models.Figurinha.cod_figurinha == cod_figurinha).first()

    if figurinha is None:
        raise HTTPException(status_code=404, detail="Figurinha não encontrada.")

    figurinha.nome_jogador = figurinha_nova.nome_jogador
    figurinha.pais = figurinha_nova.pais
    figurinha.posicao = figurinha_nova.posicao
    figurinha.numero_camisa = figurinha_nova.numero_camisa
    figurinha.raridade = figurinha_nova.raridade
    figurinha.repetida = figurinha_nova.repetida

    db.commit()
    db.refresh(figurinha)
    return figurinha

# ── Deletar figurinha ───────────────────────────────────────────────
@app.delete("/figurinhas/{cod_figurinha}", status_code=204)
def deletar_figurinha(cod_figurinha: int, db: Session = Depends(get_db)):
    figurinha = db.query(models.Figurinha).filter(models.Figurinha.cod_figurinha == cod_figurinha).first()
    if figurinha is None:
        raise HTTPException(status_code=404, detail="Figurinha não encontrada.")

    db.delete(figurinha)
    db.commit()
    return None

# ── Buscar figurinha por nome do jogador ────────────────────────────
@app.get("/figurinhas/busca/", response_model=schemas.FigurinhaResponse)
def buscar_figurinha_por_nome(nome: str, db: Session = Depends(get_db)):
    figurinha = db.query(models.Figurinha).filter(models.Figurinha.nome_jogador == nome).first()

    if figurinha is None:
        raise HTTPException(status_code=404, detail="Figurinha não encontrada pelo nome informado.")

    return figurinha

# ── Buscar figurinhas por país ──────────────────────────────────────
@app.get("/figurinhas/pais/{pais}", response_model=List[schemas.FigurinhaResponse])
def buscar_figurinhas_por_pais(pais: str, db: Session = Depends(get_db)):
    figurinhas = db.query(models.Figurinha).filter(models.Figurinha.pais == pais).all()

    if not figurinhas:
        raise HTTPException(status_code=404, detail="Nenhuma figurinha encontrada para este país.")

    return figurinhas
