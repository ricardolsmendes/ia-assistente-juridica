SISTEMA = """
Você é um assistente sênior de advogado encarregado de extrair informações específicas de
documentos oficiais.

Instruções:
1. Responda com os valores exatamente como estão nos dados de entrada; não assuma,
calcule ou resuma nada.
2. Formate os campos de data como AAAA-MM-DD se seus valores estiverem disponíveis, ou
null caso contrário.
3. As respostas devem ser apresentadas em JSON, contendo apenas os campos solicitados.

Comece!
"""

# Identifica a Data de Disponibilização.
EXTRAIR_DATA_DISPONIBILIZACAO = """
Considerando os dados a seguir, extraia a Data de Disponibilização do documento.

Instruções:
1. A estrutura do objeto resultante deve ser:
{{
    dataDisponibilizacao: <VALOR>
}}.

Dados:
{dados}
"""

# Identifica a Determinação do Juiz.
EXTRAIR_DETERMINACAO_JUIZ = """
Considerando os dados a seguir, extraia a Determinação do Juiz.

Instruções:
1. A estrutura do objeto resultante deve ser:
{{
    determinacaoJuiz: <VALOR>
}}.

Dados:
{dados}
"""

# Identifica o Órgão responsável.
EXTRAIR_ORGAO_RESPONSAVEL = """
Considerando os dados a seguir, extraia qual é o Órgão responsável.

Instruções:
1. A estrutura do objeto resultante deve ser:
{{
    orgao: <VALOR>
}}.

Dados:
{dados}
"""

# Identifica o Prazo Fatal.
EXTRAIR_PRAZO_FATAL = """
Considerando os dados a seguir, extraia o Prazo Fatal.

Instruções:
1. O resultado deve ser apresentado como texto, exatamente como está no documento, sem
cálculos adicionais.
2. A estrutura do objeto resultante deve ser:
{{
    prazoFatal: <VALOR>
}}.

Dados:
{dados}
"""

# Identifica o Prazo Inicial.
EXTRAIR_PRAZO_INICIAL = """
Considerando os dados a seguir, extraia o Prazo Inicial.

Instruções:
1. A estrutura do objeto resultante deve ser:
{{
    prazoInicial: <VALOR>
}}.

Dados:
{dados}
"""

# Identifica o Tribunal.
EXTRAIR_TRIBUNAL = """
Considerando os dados a seguir, extraia qual é o Tribunal responsável.

Instruções:
1. A estrutura do objeto resultante deve ser:
{{
    tribunal: <VALOR>
}}.

Dados:
{dados}
"""

# Identifica a Vara.
EXTRAIR_VARA = """
Considerando os dados a seguir, extraia qual é a Vara responsável.

Instruções:
1. A estrutura do objeto resultante deve ser:
{{
    vara: <VALOR>
}}.

Dados:
{dados}
"""
