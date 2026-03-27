from pydantic import BaseModel, Field

class CRLVResponse(BaseModel):
    carro_renavam: str = Field(description="Número do RENAVAM do veículo (11 DÍGITOS)")
    carro_placa: str = Field(description="Placa do veículo (MODELO ANTIGO OU NOVO)")
    carro_emplacamento: int = Field(description="Ano de exercício do último licenciamento (geralmente 2025)")
    ano_fabricacao: int = Field(description="Ano de fabricação do veículo")
    ano_modelo: int = Field(description="Ano do modelo do veículo")
    carro_modelo: str = Field(description="Marca e modelo do veículo ('MARCA'/'MODELO INFO A B')")
    carro_chassi: str = Field(description="Número do chassi")
    carro_cor: str = Field(description="Cor do veículo")

class CNHResponse(BaseModel):
    pessoa_nome: str = Field(description="Nome completo da pessoa (ex.: LIONEL ANDRÉS MESSI CUCCITTINI)")
    pessoa_data_nascimento: str = Field(description="Data de nascimento formato DD/MM/AAAA (ex: 25/02/2006)")
    pessoa_cpf: str = Field(description="CPF completo da pessoa com 11 dígitos (99999999900)")
    pessoa_rg: str = Field(description="RG completo da pessoa (sem formato padrão)")
    orgao_emissor: str = Field(description="Órgão emissor (ex: SSP RN)")

PROMPT_CNH_OCR = """
                    Você é uma ferramenta de automação de documentação veicular.

                    Receberá imagens de documentos pessoais.
                    Extraia as informações relevantes do documento.

                    Retorne APENAS um JSON válido, sem markdown, sem comentários, sem texto adicional,
                    seguindo exatamente esta estrutura (COM EXEMPLOS):

                    {
                    "pessoa_nome": "JOSÉ HIAGO DA SILVA",
                    "pessoa_data_nascimento": "25/02/2006",
                    "pessoa_cpf": "99922233300",
                    "pessoa_rg": "59484",
                    "orgao_emissor": "SSP RN"
                    }

                    Regras importantes:
                    - Todos os campos DEVEM existir
                    - Se um valor não for encontrado, retorne string vazia ""
                    - Ignore ruídos, bordas, linhas e textos irrelevantes
                    - Extraia apenas informações centrais e confiáveis do documento
                    - PRESERVE A INFORMAÇÃO COMO ELA É, exemplo: incluir zeros à esquerda
                 """

PROMPT_CRLV_OCR =    """
                    Você é uma ferramenta de automação de documentação veicular.

                    Receberá imagens de um contrato de compra e venda de veículo.
                    Extraia as informações relevantes do documento.

                    Retorne APENAS um JSON válido, sem markdown, sem comentários, sem texto adicional,
                    seguindo exatamente esta estrutura (COM EXEMPLOS):

                    {
                    "carro_renavam": "012345678999",
                    "carro_placa": "ABC1D23",
                    "carro_emplacamento": "2026",
                    "ano_fabricacao": "2020",
                    "ano_modelo": "2021",
                    "carro_modelo": "MARCA/MODELO INFO A B",
                    "carro_chassi": "9BGEX76H0MB115751",
                    "carro_cor": "COR"
                    }

                    Regras importantes:
                    - Todos os campos DEVEM existir
                    - Se um valor não for encontrado, retorne string vazia ""
                    - Ignore ruídos, bordas, linhas e textos irrelevantes
                    - Extraia apenas informações centrais e confiáveis do documento
                    - A placa pode estar no modelo novo ou antigo
                    - O modelo do carro deve conter todas especificações do carro (incluindo letras perto do modelo)
                    - PRESERVE A INFORMAÇÃO COMO ELA É, exemplo: incluir zeros à esquerda
                """