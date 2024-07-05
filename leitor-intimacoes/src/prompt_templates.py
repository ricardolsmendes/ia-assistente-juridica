SISTEMA = """
## TAREFA
Você é um assistente sênior de advogado encarregado de extrair informações específicas de
documentos oficiais.

## INSTRUÇÕES
1. Responda com os valores exatamente como estão nos dados de entrada; não assuma,
calcule ou resuma nada.
2. Formate os campos de data como AAAA-MM-DD se seus valores estiverem disponíveis, ou
null caso contrário.
3. As respostas devem ser apresentadas em JSON, contendo apenas os campos solicitados.

Comece!
"""

# Identifica a Data de Disponibilização.
EXTRAIR_DATA_DISPONIBILIZACAO = """
## TAREFA
Considerando os dados a seguir, extraia a Data de Disponibilização do documento.

## INSTRUÇÕES
1. A estrutura do objeto resultante deve ser:
{{
    dataDisponibilizacao: <VALOR>
}}.

## DADOS
{dados}
"""

# Identifica a Determinação do Juiz.
EXTRAIR_DETERMINACAO_JUIZ = """
## TAREFA
Considerando os dados a seguir, extraia a Determinação do Juiz.

## INSTRUÇÕES
1. A estrutura do objeto resultante deve ser:
{{
    determinacaoJuiz: <VALOR>
}}.

## DADOS
{dados}
"""

# Identifica o Órgão responsável.
EXTRAIR_ORGAO_RESPONSAVEL = """
## TAREFA
Considerando os dados a seguir, extraia qual é o Órgão responsável.

## INSTRUÇÕES
1. A estrutura do objeto resultante deve ser:
{{
    orgao: <VALOR>
}}.

## DADOS
{dados}
"""

# Identifica o Prazo Fatal.
EXTRAIR_PRAZO_FATAL = """
## TAREFA
Considerando os dados a seguir, extraia o Prazo Fatal.

## INSTRUÇÕES
1. O resultado deve ser apresentado como texto, exatamente como está no documento, sem
cálculos adicionais.
2. A estrutura do objeto resultante deve ser:
{{
    prazoFatal: <VALOR>
}}.

## DADOS
{dados}
"""

# Identifica o Prazo Inicial.
EXTRAIR_PRAZO_INICIAL = """
## TAREFA
Considerando os dados a seguir, extraia o Prazo Inicial.

## INSTRUÇÕES
1. A estrutura do objeto resultante deve ser:
{{
    prazoInicial: <VALOR>
}}.

## DADOS
{dados}
"""

# Identifica o Tribunal responsável.
EXTRAIR_TRIBUNAL = """
## TAREFA
Considerando os dados a seguir, extraia qual é o Tribunal responsável.

## INSTRUÇÕES
1. A estrutura do objeto resultante deve ser:
{{
    tribunal: <VALOR>
}}.

## DADOS
{dados}
"""

# Identifica a Vara responsável.
EXTRAIR_VARA = """
## TAREFA
Considerando os dados a seguir, extraia qual é a Vara responsável.

## INSTRUÇÕES
1. A estrutura do objeto resultante deve ser:
{{
    vara: <VALOR>
}}.

## DADOS
{dados}
"""
