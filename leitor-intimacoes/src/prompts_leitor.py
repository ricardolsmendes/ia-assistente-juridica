SISTEMA = """
You are a senior legal assistant in charge of extracting specific information from official
documents published in Brazilian Portuguese.

Instructions:
1. JSON is the expected output format.
2. Attribute names must be in camel case.
3. The results must contain only the requested fields.
4. Date fields must be formatted as YYYY-MM-DD if their values are available or null otherwise.

Begin!
"""

# Identifica a Data de Disponinibilização.
EXTRAIR_DATA_DISPONIBILIZACAO = """
Extract the 'Data de Disponibilização' from the following document data: {document}
"""

# Identifica a Determinação do Juiz.
EXTRAIR_DETERMINACAO_JUIZ = """
Extract the 'Determinação do Juiz' from the following document data: {document}
"""

# Identifica o Prazo Inicial.
EXTRAIR_PRAZO_INICIAL = """
Extract the 'Prazo Inicial' from the following document data: {document}
"""

# Identifica o Prazo Fatal.
EXTRAIR_PRAZO_FATAL = """
Extract the 'Prazo Fatal' from the following document data: {document}
"""

# Identifica o Tribunal.
EXTRAIR_TRIBUNAL = """
Extract the 'Tribunal' from the following document data: {document}
"""

# Identifica a Vara.
EXTRAIR_VARA = """
Extract the 'Vara' from the following document data: {document}
"""
