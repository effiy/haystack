from haystack import Document

from haystack.components.preprocessors import JiebaDocumentSplitter

# 初始化 JiebaDocumentSplitter
splitter = JiebaDocumentSplitter()

# 示例文档
documents = [Document(content="作为开发者，您可以完全控制如何在管道中排列组件。管道可以分支、合并，也可以循环回到另一个组件。您可以组合 Haystack 管道，使其能够重试、循环，甚至可能作为服务持续运行。")]

# 分割文档
result = splitter.run(documents=documents)

# 输出分割后的文档
for doc in result["documents"]:
    print(doc.content)