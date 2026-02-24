
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI(title="Merindilogun Plus")

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")


class Buzios(BaseModel):
    numero: str


ODUS = {
    "1": {
        "nome": "Okanran",
        "positivo": "Força, coragem e superação.",
        "negativo": "Conflitos e impulsividade.",
        "ebo_positivo": "Velas, pretas, brancas e vermelhas, mel, farinha de mandioca e dendê, oferecidos a Exu na encruzilhada, pedindo coragem e abertura de caminhos.",
        "Alerta": "Evitar discussões e brigas.",
        "orixas": ["Exu"]
    },
    "2": {
        "nome": "Ejioko",
        "positivo": "Equilíbrio e escolhas sábias.",
        "negativo": "Dúvidas e instabilidade.",
        "ebo_positivo": "Banho de ervas doces (manjericão, erva-doce, alfazema), seguido de oferenda de flores brancas e mel a Oxum, pedindo equilíbrio e clareza nas escolhas, além de entrega de frutas e doces aos Erês.",
        "Alerta": "Não procrastinar.",
        "orixas": ["Oxalá", "Ibeji", "Oxum"]
    },
    "3": {
        "nome": "Etaogunda",
        "positivo": "Renovação e crescimento.",
        "negativo": "Perdas e desgaste.",
        "ebo_positivo": "Inhame assado, frutas frescas e cervejas escuras oferecidas a Ogum, pedindo força para superar perdas e renovar energias. Além de banho de pipoca ofetada a Obaluaye",
        "Alerta": "Evitar excessos físicos.",
        "orixas": ["Ogum", "Obaluaye"]
    },
    "4": {
        "nome": "Irosun",
        "positivo": "Força e ancestralidade.",
        "negativo": "Orgulho e rigidez.",
        "ebo_positivo": "Milho vermelho cozido e amalá ofertados à Xango, Além de água fresca e flores brancas oferecidas a Yemanja, pedindo proteção ancestral e sabedoria.",
        "Alerta": "Evitar arrogância.",
        "orixas": ["Xango", "Yemanja"]
    },
    "5": {
        "nome": "Osé",
        "positivo": "Harmonia e prosperidade.",
        "negativo": "Vaidade e desperdício.",
        "ebo_positivo": " Mel, moedas douradas e água doce oferecidas a Oxum em correnteza, pedindo prosperidade e harmonia nos relacionamentos.",
        "Alerta": "Evitar ostentação.",
        "orixas": ["Oxum", "Yamin"]
    },
    "6": {
        "nome": "Obará",
        "positivo": "Comunicação e liderança.",
        "negativo": "Intrigas e fofocas.",
        "ebo_positivo": "Pão fresco, cervejas e melaço de açúcar oferecidos a Xango, Oxóssi e Logunedé, pedindo liderança justa e comunicação clara.",
        "Alerta": "Evitar falar demais.",
        "orixas": ["Xangô", "Oxossi", "Logunedé"]
    },
    "7": {
        "nome": "Odi",
        "positivo": "Proteção espiritual.",
        "negativo": "Medos e bloqueios.",
        "ebo_positivo": "Banho de folhas de proteção (guiné, arruda, espada de Ogum), seguido de oferenda de pipoca e velas a Obaluaiê, pedindo proteção espiritual contra medos e bloqueios.",
        "Alerta": "Evitar isolamento.",
        "orixas": ["Obaluaiê", "Exu", "Ogum"]
    },
    "8": {
        "nome": "Ejionile",
        "positivo": "Estabilidade e construção.",
        "negativo": "Apego e materialismo.",
        "ebo_positivo": "Milho cozido, feijão fradinho, ovos e água fresca oferecidos a Oxum, pedindo estabilidade e construção sólida nos projetos. Ofertar também canjica branca à Oxalá",
        "Alerta": "Evitar ganância.",
        "orixas": ["Oxalá", "Oxum"]
    },
    "9": {
        "nome": "Osa",
        "positivo": "Renovação e mudanças.",
        "negativo": "Instabilidade e rupturas.",
        "ebo_positivo": "Acarajés, frutas variadas e flores oferecidas a Oya, pedindo renovação e mudanças positivas.",
        "Alerta": "Evitar impulsividade.",
        "orixas": ["Oyá", "Oxum"]
    },
    "10": {
        "nome": "Ofun",
        "positivo": "Espiritualidade elevada.",
        "negativo": "Ilusões e fanatismo.",
        "ebo_positivo": "Água cristalina, velas brancas e flores claras oferecidas a Oxalá e Oxum, pedindo espiritualidade elevada e clareza mental.",
        "Alerta": "Evitar fanatismo.",
        "orixas": ["Oxalá", "Oxum"]
    },
    "11": {
        "nome": "Owarin",
        "positivo": "Conflitos e superação.",
        "negativo": "Teimosia e rivalidade.",
        "ebo_positivo": "Carne branca, vinho tinto e velas vermelhas oferecidos a Ogum, Obaluaye e Exu, pedindo força para superar conflitos e rivalidades.",
        "Alerta": "Evitar confrontos.",
        "orixas": ["Ogum", "Obaluaye", "Exu"]
    },
    "12": {
        "nome": "Ejilasébora",
        "positivo": "Justiça e equilíbrio.",
        "negativo": "Injustiça e desequilíbrio.",
        "ebo_positivo": "Peixe assado, frutas variadas e flores oferecidas a Iemanjá na beira da água, pedindo renovação e mudanças positivas.",
        "Alerta": "Evitar parcialidade.",
        "orixas": ["Xangô", "Iemanjá"]
    },
    "13": {
        "nome": "Ejiodibara",
        "positivo": "Responsabilidade e firmeza.",
        "negativo": "Rigidez e intolerância.",
        "ebo_positivo": "Inhame cozido, milho branco e água fresca oferecidos a Obaluaiê, Exu e Ogum, pedindo responsabilidade e firmeza.",
        "Alerta": "Evitar inflexibilidade.",
        "orixas": ["Obaluaiê","Exu", "Nanã"]
    },
    "14": {
        "nome": "Ika",
        "positivo": "Desafios e cautela.",
        "negativo": "Armadilhas e traições.",
        "ebo_positivo": "Feijão Fradinho com Ovos cozidos inteiros em oferendas, Serpente de Bata Doce, cercada com amendoim, ofertados à Oxumare e Ewa, pedindo renovação e transformação.",
        "Alerta": "Evitar ingenuidade.",
        "orixas": [ "Oxumarê" "Ewa"]
    },
    "15": {
        "nome": "Ogbekunda",
        "positivo": "Caminhos abertos.",
        "negativo": "Obstáculos e atrasos.",
        "ebo_positivo": "Frutas variadas, mel e flores oferecidas a Obá e Ewa, pedindo abertura de caminhos e prosperidade.",
        "Alerta": "Evitar preguiça.",
        "orixas": ["Obá", "Ewa"]
    },
    "16": {
        "nome": "Alafia",
        "positivo": "Paz, vitória e estabilidade.",
        "negativo": "Estagnação e comodismo.",
        "ebo_positivo": " Flores brancas, água fresca e velas claras oferecidas a Oxalá e Olorumilá Ifa, pedindo paz, vitória e estabilidade.",
        "Alerta": "Evitar acomodação.",
        "orixas": ["Oxalá", "Olorumilá Ifá"]
    }
}



@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/consultar")
def consultar(b: Buzios):
    odu = ODUS.get(b.numero)

    if not odu:
        return {"erro": "Odù não encontrado."}

    return odu
