from typing import Any, Dict, Optional

from langchain_core import prompts, output_parsers
from langchain_core.prompts import ChatPromptTemplate

import model_factory
import prompts_customizados


class LeitorIntimacoes:

    def __init__(self, familia_llm: str):
        # Inicializa o Large Language Model.
        self.llm = model_factory.ModelFactory.make_model(familia_llm)
        self.output_parser = output_parsers.JsonOutputParser()

    def _extrair_informacoes(
        self, input_usuario: Dict[str, Any], prompt: ChatPromptTemplate
    ) -> Dict[str, Any]:
        chain = prompt | self.llm | self.output_parser
        return chain.invoke({"input_usuario": input_usuario})

    def extrair_data_disponibilizacao(
        self, input_usuario: Dict[str, Any]
    ) -> Dict[str, Optional[str]]:
        prompt = prompts.ChatPromptTemplate.from_messages(
            [
                ("system", prompts_customizados.EXTRATOR_DATA_DISPONIBILIZACAO),
                ("user", "{input_usuario}"),
            ]
        )
        return self._extrair_informacoes(input_usuario, prompt)

    def extrair_determinacao_juiz(
        self, input_usuario: Dict[str, Any]
    ) -> Dict[str, Optional[str]]:
        prompt = prompts.ChatPromptTemplate.from_messages(
            [
                ("system", prompts_customizados.EXTRATOR_DETERMINACAO_JUIZ),
                ("user", "{input_usuario}"),
            ]
        )
        return self._extrair_informacoes(input_usuario, prompt)

    def extrair_prazo_inicial(
        self, input_usuario: Dict[str, Any]
    ) -> Dict[str, Optional[str]]:
        prompt = prompts.ChatPromptTemplate.from_messages(
            [
                ("system", prompts_customizados.EXTRATOR_PRAZO_INICIAL),
                ("user", "{input_usuario}"),
            ]
        )
        return self._extrair_informacoes(input_usuario, prompt)

    def extrair_prazo_fatal(
        self, input_usuario: Dict[str, Any]
    ) -> Dict[str, Optional[str]]:
        prompt = prompts.ChatPromptTemplate.from_messages(
            [
                ("system", prompts_customizados.EXTRATOR_PRAZO_FATAL),
                ("user", "{input_usuario}"),
            ]
        )
        return self._extrair_informacoes(input_usuario, prompt)

    def extrair_tribunal(
        self, input_usuario: Dict[str, Any]
    ) -> Dict[str, Optional[str]]:
        prompt = prompts.ChatPromptTemplate.from_messages(
            [
                ("system", prompts_customizados.EXTRATOR_TRIBUNAL),
                ("user", "{input_usuario}"),
            ]
        )
        return self._extrair_informacoes(input_usuario, prompt)

    def extrair_vara(self, input_usuario: Dict[str, Any]) -> Dict[str, Optional[str]]:
        prompt = prompts.ChatPromptTemplate.from_messages(
            [
                ("system", prompts_customizados.EXTRATOR_VARA),
                ("user", "{input_usuario}"),
            ]
        )
        return self._extrair_informacoes(input_usuario, prompt)
