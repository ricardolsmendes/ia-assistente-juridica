import os

import langchain_openai
import torch
import transformers
from langchain_community.llms import huggingface_pipeline
from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline
from langchain_core.language_models.llms import BaseLLM
from langchain_openai import ChatOpenAI


class ModelFactory:
    _LLAMA2_MODEL_NAME = "meta-llama/Llama-2-7b-chat-hf"
    _OPENAI_MODEL_NAME = "gpt-3.5-turbo"

    @classmethod
    def make_model(cls, model_family: str, temperature: float = 0.0) -> BaseLLM:
        family_to_factory_map = {
            "--llama-2": cls.make_llama_2,
            "--openai": cls.make_openai,
        }
        return family_to_factory_map.get(model_family.lower())(temperature)

    @classmethod
    def make_llama_2(cls, temperature: float = 0.0) -> HuggingFacePipeline:
        """
        Instantiate the Llama 2 model.

        :param temperature: controls the RANDOMNESS of the model's output. A lower
            temperature will result in more predictable output, while a higher
            temperature will result in more random output. The temperature parameter is
            set between 0 and 1, with 0 being the most predictable and 1 being the most
            random.
        :return: the Llama 2 model
        """
        tokenizer = transformers.AutoTokenizer.from_pretrained(
            cls._LLAMA2_MODEL_NAME, token=os.environ.get("HUGGING_FACE_ACCESS_TOKEN")
        )

        model = transformers.AutoModelForCausalLM.from_pretrained(
            cls._LLAMA2_MODEL_NAME,
            token=os.environ.get("HUGGING_FACE_ACCESS_TOKEN"),
            torch_dtype=torch.float16,
            device_map="auto",
        )

        generation_config = transformers.GenerationConfig.from_pretrained(
            cls._LLAMA2_MODEL_NAME
        )
        generation_config.temperature = temperature
        generation_config.repetition_penalty = 1.15

        pipeline = transformers.pipeline(
            "text-generation",
            model=model,
            tokenizer=tokenizer,
            generation_config=generation_config,
        )

        return huggingface_pipeline.HuggingFacePipeline(
            pipeline=pipeline, model_kwargs={"temperature": temperature}
        )

    @classmethod
    def make_openai(cls, temperature: float = 0.0) -> ChatOpenAI:
        """
        Instantiate the OpenAI model.

        :param temperature: controls the RANDOMNESS of the model's output. A lower
            temperature will result in more predictable output, while a higher
            temperature will result in more random output. The temperature parameter is
            set between 0 and 1, with 0 being the most predictable and 1 being the most
            random.
        :return: the OpenAI model
        """
        return langchain_openai.ChatOpenAI(
            model_name=cls._OPENAI_MODEL_NAME, temperature=temperature
        )
