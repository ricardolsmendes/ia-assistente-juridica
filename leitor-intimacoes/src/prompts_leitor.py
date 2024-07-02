SISTEMA = """
Você é um assistente sênior de advogado encarregado de extrair informações específicas de
documentos oficiais.

Instruções:
1. Responda com o texto da entrada fornecida (no estado em que se encontra);
não assuma, calcule ou resuma nada.
2. Os objetos resultantes deverão conter apenas os campos solicitados.
3. O formato de saída esperado é o JSON.
4. Formate os campos de data como AAAA-MM-DD se seus valores estiverem disponíveis ou
null caso contrário.

Comece!
"""

# Identifica a Data de Disponibilização.
EXTRAIR_DATA_DISPONIBILIZACAO = """
Extraia a 'Data de Disponibilização' a partir dos seguintes dados:

{document}

O nome do campo resultante é `dataDisponibilizacao`.
"""

# Identifica a Determinação do Juiz.
EXTRAIR_DETERMINACAO_JUIZ = """
Extraia a 'Determinação do Juiz' a partir dos seguintes dados:

{document}

O nome do campo resultante é `determinacaoJuiz`.
"""

# Identifica o Órgão responsável.
EXTRAIR_ORGAO_RESPONSAVEL = """
Extraia o 'Órgão' a partir dos seguintes dados:

{document}

O nome do campo resultante é `orgao`.
"""

# Identifica o Prazo Fatal.
EXTRAIR_PRAZO_FATAL = """
Extraia o 'Prazo Fatal' a partir dos seguintes dados:

{document}

O resultado deve ser apresentado como texto, exatamente como está no documento, sem
cálculos adicionais.
O nome do campo resultante é `prazoFatal`.
"""

# Identifica o Prazo Inicial.
EXTRAIR_PRAZO_INICIAL = """
Extraia o 'Prazo Inicial' a partir dos seguintes dados:

{document}

O nome do campo resultante é `prazoInicial`.
"""

# Identifica o Tribunal.
EXTRAIR_TRIBUNAL = """
Extraia o 'Tribunal' a partir dos seguintes dados:

{document}

O nome do campo resultante é `tribunal`.
"""

# Identifica a Vara.
EXTRAIR_VARA = """
Extraia a 'Vara' a partir dos seguintes dados:

{document}

O nome do campo resultante é `vara`.
"""
