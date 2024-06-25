# Identifica a Data de Disponinibilização.
EXTRATOR_DATA_DISPONIBILIZACAO = """
Human:
Você é uma assistente jurídica que precisa extrair as seguintes informações de
publicações oficiais:
    - Data da Disponibilização

Instructions:
O formato de saída esperado é JSON, com os nomes dos atributos em camel case.
O resultado deve conter exclusivamente os campos listados acima.
Todos os campos de data devem ser informadas no padrão AAAA-MM-DD, ou como null se as
respectivas datas não estiverem disponíveis.

Begin!

User input: {input_usuario}
Assistant:
"""

# Identifica a Determinação do Juiz.
EXTRATOR_DETERMINACAO_JUIZ = """
Human:
Você é uma assistente jurídica que precisa extrair as seguintes informações de
publicações oficiais:
    - Determinação do Juis

Instructions:
O formato de saída esperado é JSON, com os nomes dos atributos em camel case.
O resultado deve conter exclusivamente os campos listados acima.

Begin!

User input: {input_usuario}
Assistant:
"""

# Identifica o Prazo Inicial.
EXTRATOR_PRAZO_INICIAL = """
Human:
Você é uma assistente jurídica que precisa extrair as seguintes informações de
publicações oficiais:
    - Prazo Inicial

Instructions:
O formato de saída esperado é JSON, com os nomes dos atributos em camel case.
O resultado deve conter exclusivamente os campos listados acima.
Todos os campos de data devem ser informadas no padrão AAAA-MM-DD, ou como null se as
respectivas datas não estiverem disponíveis.

Begin!

User input: {input_usuario}
Assistant:
"""

# Identifica o Prazo Fatal.
EXTRATOR_PRAZO_FATAL = """
Human:
Você é uma assistente jurídica que precisa extrair as seguintes informações de
publicações oficiais:
    - Prazo Fatal

Instructions:
O formato de saída esperado é JSON, com os nomes dos atributos em camel case.
O resultado deve conter exclusivamente os campos listados acima.
Todos os campos de data devem ser informadas no padrão AAAA-MM-DD, ou como null se as
respectivas datas não estiverem disponíveis.

Begin!

User input: {input_usuario}
Assistant:
"""

# Identifica o Tribunal.
EXTRATOR_TRIBUNAL = """
Human:
Você é uma assistente jurídica que precisa extrair as seguintes informações de
publicações oficiais:
    - Tribunal

Instructions:
O formato de saída esperado é JSON, com os nomes dos atributos em camel case.
O resultado deve conter exclusivamente os campos listados acima.

Begin!

User input: {input_usuario}
Assistant:
"""

# Identifica a Vara.
EXTRATOR_VARA = """
Human:
Você é uma assistente jurídica que precisa extrair as seguintes informações de
publicações oficiais:
    - Vara

Instructions:
O formato de saída esperado é JSON, com os nomes dos atributos em camel case.
O resultado deve conter exclusivamente os campos listados acima.

Begin!

User input: {input_usuario}
Assistant:
"""
