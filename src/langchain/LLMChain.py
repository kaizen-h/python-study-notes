from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

class ProductNameChain():
    def __init__(self):
        pass

    def getName(self, productName:str):
        llm = OpenAI(model_mane="deepseek-reasoner", temperature=0.9, max_tokens=500)

        promote = PromptTemplate(input_variable=["product"],
                                 template="给制造{product}的有限公司取10个好名字，并给出完整的公司名称")
        llm_chain = LLMChain(llm, promote)
        print(llm_chain.invoke({"product": productName}))

