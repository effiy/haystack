from haystack import Pipeline
from haystack.document_stores.in_memory import InMemoryDocumentStore
from haystack.components.retrievers import InMemoryEmbeddingRetriever
from haystack.components.converters import TextFileToDocument
from haystack.components.preprocessors import DocumentCleaner, DocumentSplitter
from haystack.components.writers import DocumentWriter
from haystack.components.builders import ChatPromptBuilder
from haystack.dataclasses import ChatMessage

from haystack_integrations.components.embedders.ollama.document_embedder import OllamaDocumentEmbedder
from haystack_integrations.components.embedders.ollama.text_embedder import OllamaTextEmbedder
from haystack_integrations.components.generators.ollama import OllamaChatGenerator

# 创建一个内存文档存储
document_store = InMemoryDocumentStore()

# 初始化各个组件
text_file_converter = TextFileToDocument()  # 文本文件转换器
cleaner = DocumentCleaner()  # 文档清理器
splitter = DocumentSplitter()  # 文档分割器
embedder = OllamaDocumentEmbedder(model="nomic-embed-text", url="http://localhost:11434")  # 文档嵌入器
writer = DocumentWriter(document_store)  # 文档写入器

# 创建索引管道
indexing_pipeline = Pipeline()
indexing_pipeline.add_component("converter", text_file_converter)
indexing_pipeline.add_component("cleaner", cleaner)
indexing_pipeline.add_component("splitter", splitter)
indexing_pipeline.add_component("embedder", embedder)
indexing_pipeline.add_component("writer", writer)

# 连接各个组件
indexing_pipeline.connect("converter.documents", "cleaner.documents")
indexing_pipeline.connect("cleaner.documents", "splitter.documents")
indexing_pipeline.connect("splitter.documents", "embedder.documents")
indexing_pipeline.connect("embedder.documents", "writer.documents")

# 运行索引管道，处理指定文件
indexing_pipeline.run(data={"sources": ["/Users/yi/Workspaces/GitHubDaily/README.md"]})

# 初始化文本嵌入器和检索器
text_embedder = OllamaTextEmbedder(model="nomic-embed-text", url="http://localhost:11434")  # 使用Ollama的文本嵌入模型
retriever = InMemoryEmbeddingRetriever(document_store)  # 基于内存文档存储的检索器

# 优化后的提示模板，用于构建RAG系统的提示
prompt_template = [
    ChatMessage.from_user(
        """
        请根据以下文档内容回答问题：
        文档内容：
        {% for document in documents %}
            {{ document.content }}
        {% endfor %}

        问题：{{query}}
        请用中文回答：
        """
    )
]

# 创建提示构建器，用于生成结构化提示
prompt_builder = ChatPromptBuilder(template=prompt_template)

# 初始化聊天生成器，使用Ollama的Qwen2.5模型
llm = OllamaChatGenerator(model="qwen2.5", timeout=45, url="http://localhost:11434")

# 创建RAG(检索增强生成)管道
rag_pipeline = Pipeline()
rag_pipeline.add_component("text_embedder", text_embedder)
rag_pipeline.add_component("retriever", retriever)
rag_pipeline.add_component("prompt_builder", prompt_builder)
rag_pipeline.add_component("llm", llm)

# 连接RAG管道中的各个组件
rag_pipeline.connect("text_embedder.embedding", "retriever.query_embedding")  # 将查询文本的嵌入传递给检索器
rag_pipeline.connect("retriever.documents", "prompt_builder.documents")  # 将检索到的文档传递给提示构建器
rag_pipeline.connect("prompt_builder", "llm")  # 将构建好的提示传递给语言模型

# 定义用户查询
query = "视频字幕翻译助手有哪些？"

# 运行RAG管道，处理用户查询
result = rag_pipeline.run(data={"prompt_builder": {"query":query}, "text_embedder": {"text": query}})

# 打印生成的回答结果
print(result["llm"]["replies"][0].text)