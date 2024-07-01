from typing import Any, Dict, Optional

from langchain_core import messages, prompts, output_parsers

import model_factory
import prompts_leitor


class LeitorIntimacoes:

    def __init__(self, familia_llm: str):
        # Inicializa o Large Language Model.
        self.llm = model_factory.ModelFactory.make_model(familia_llm)
        self.output_parser = output_parsers.JsonOutputParser()

    def _extrair_informacoes(
        self, prompt_usuario: str, documento: Dict[str, Any]
    ) -> Dict[str, Any]:
        prompt = prompts.ChatPromptTemplate.from_messages(
            [
                messages.system.SystemMessage(prompts_leitor.SISTEMA),
                messages.human.HumanMessage(prompt_usuario),
            ]
        )
        chain = prompt | self.llm | self.output_parser
        return chain.invoke({"document": documento})

    def extrair_data_disponibilizacao(
        self, documento: Dict[str, Any]
    ) -> Dict[str, Optional[str]]:
        return self._extrair_informacoes(
            prompts_leitor.EXTRAIR_DATA_DISPONIBILIZACAO, documento
        )

    def extrair_determinacao_juiz(
        self, documento: Dict[str, Any]
    ) -> Dict[str, Optional[str]]:
        return self._extrair_informacoes(
            prompts_leitor.EXTRAIR_DETERMINACAO_JUIZ, documento
        )

    def extrair_prazo_inicial(
        self, documento: Dict[str, Any]
    ) -> Dict[str, Optional[str]]:
        return self._extrair_informacoes(
            prompts_leitor.EXTRAIR_PRAZO_INICIAL, documento
        )

    def extrair_prazo_fatal(
        self, documento: Dict[str, Any]
    ) -> Dict[str, Optional[str]]:
        return self._extrair_informacoes(prompts_leitor.EXTRAIR_PRAZO_FATAL, documento)

    def extrair_tribunal(self, documento: Dict[str, Any]) -> Dict[str, Optional[str]]:
        return self._extrair_informacoes(prompts_leitor.EXTRAIR_TRIBUNAL, documento)

    def extrair_vara(self, documento: Dict[str, Any]) -> Dict[str, Optional[str]]:
        return self._extrair_informacoes(prompts_leitor.EXTRAIR_VARA, documento)
