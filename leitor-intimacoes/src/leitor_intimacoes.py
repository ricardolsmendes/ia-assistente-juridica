from typing import Any, Dict, Optional

from langchain_core import output_parsers, prompts

import model_factory
import prompt_templates


class LeitorIntimacoes:

    def __init__(self, familia_llm: str):
        # Inicializa o Large Language Model.
        self.llm = model_factory.ModelFactory.make_model(familia_llm)
        self.output_parser = output_parsers.JsonOutputParser()

    def _extrair_informacoes(
        self, prompt_usuario: str, dados: Dict[str, Any]
    ) -> Dict[str, Any]:
        message_list = [
            ("system", prompt_templates.SISTEMA),
            ("human", prompt_usuario),
        ]

        prompt = prompts.ChatPromptTemplate.from_messages(message_list)
        chain = prompt | self.llm | self.output_parser
        return chain.invoke({"dados": dados})

    def extrair_data_disponibilizacao(
        self, dados: Dict[str, Any]
    ) -> Dict[str, Optional[str]]:
        return self._extrair_informacoes(
            prompt_templates.EXTRAIR_DATA_DISPONIBILIZACAO, dados
        )

    def extrair_determinacao_juiz(
        self, dados: Dict[str, Any]
    ) -> Dict[str, Optional[str]]:
        return self._extrair_informacoes(
            prompt_templates.EXTRAIR_DETERMINACAO_JUIZ, dados
        )

    def extrair_orgao(self, dados: Dict[str, Any]) -> Dict[str, Optional[str]]:
        return self._extrair_informacoes(
            prompt_templates.EXTRAIR_ORGAO_RESPONSAVEL, dados
        )

    def extrair_prazo_fatal(self, dados: Dict[str, Any]) -> Dict[str, Optional[str]]:
        return self._extrair_informacoes(prompt_templates.EXTRAIR_PRAZO_FATAL, dados)

    def extrair_prazo_inicial(self, dados: Dict[str, Any]) -> Dict[str, Optional[str]]:
        return self._extrair_informacoes(prompt_templates.EXTRAIR_PRAZO_INICIAL, dados)

    def extrair_tribunal(self, dados: Dict[str, Any]) -> Dict[str, Optional[str]]:
        return self._extrair_informacoes(prompt_templates.EXTRAIR_TRIBUNAL, dados)

    def extrair_vara(self, dados: Dict[str, Any]) -> Dict[str, Optional[str]]:
        return self._extrair_informacoes(prompt_templates.EXTRAIR_VARA, dados)
