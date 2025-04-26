REGRAS_SUPERIOR = {
    "Atividades de Aperfeiçoamento e Enriquecimento Cultural": {
        "maximo_curso": 120,
        "limite_semestral": 80,
        "subcategorias": {
            "Participação em atividades culturais": {
                "peso": 5,
                "limite_semestral": 30
            },
            "Visitas técnicas/culturais": {
                "peso": 5,
                "limite_semestral": 30
            },
            "Cursos de línguas, informática, etc.": {
                "peso": 1,
                "limite_semestral": 70,
                "por_hora": True
            },
            "Trabalho voluntário": {
                "peso": 10,
                "limite_semestral": 40
            }
        }
    },
    "Atividades de Divulgação Científica e Iniciação à Docência": {
        "maximo_curso": 100,
        "limite_semestral": 60,
        "subcategorias": {
            "Monitoria": {
                "peso": 15,
                "limite_semestral": 60
            },
            "Apresentação de trabalhos científicos ou palestras": {
                "peso": 10,
                "limite_semestral": 30,
                "observacao": "15 pontos se for da área do curso"
            }
        }
    },
    "Atividades de Vivência Acadêmica e Profissional": {
        "maximo_curso": 100,
        "limite_semestral": 60,
        "subcategorias": {
            "Organização de eventos": {
                "peso": 1,
                "limite_semestral": 30,
                "observacao": "10 pontos por evento completo"
            },
            "Participação como ouvinte em bancas acadêmicas": {
                "peso": 3,
                "limite_semestral": 18
            }
        }
    },
    "Atividades de Pesquisa/Extensão e Publicações": {
        "maximo_curso": 100,
        "limite_semestral": 80,
        "subcategorias": {
            "Participação em projetos de pesquisa": {
                "peso": 7.5,
                "limite_semestral": 45,
                "por_mes": True
            },
            "Publicação de artigo científico": {
                "peso": 25,
                "limite_semestral": 50,
                "observacao": "30 pontos se for em revista da área"
            }
        }
    }
}