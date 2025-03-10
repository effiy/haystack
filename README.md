[Haystack](https://haystack.deepset.ai/) 是一个强大的端到端 LLM 框架，让您能够构建由大语言模型、Transformer 模型和向量搜索等技术驱动的智能应用。无论您需要实现检索增强生成（RAG）、文档搜索、问答系统还是内容生成，Haystack 都能将先进的嵌入模型和 LLMs 有机组合成高效管道，帮助您构建完整的 NLP 应用并解决各类实际问题。

## 文档 (Documentation)

新用户请先阅读["什么是 Haystack?"](https://haystack.deepset.ai/overview/intro)，然后参考["快速入门指南"](https://haystack.deepset.ai/overview/quick-start)，几分钟内即可构建您的首个 LLM 应用。进一步学习可通过[教程](https://haystack.deepset.ai/tutorials)深入了解。对于高级用例或寻找灵感，可以在[Cookbook](https://haystack.deepset.ai/cookbook)中浏览丰富的 Haystack 示例。您可以使用 [OllamaGenerator](https://github.com/deepset-ai/haystack-integrations/blob/main/integrations/ollama.md) 在 Haystack 管道中集成 Ollama 模型。

随时查阅[官方文档](https://docs.haystack.deepset.ai/docs/intro)获取更全面的 Haystack 信息，了解其功能和底层技术原理。

## 组件（Components）

Haystack 的核心是其[组件](https://docs.haystack.deepset.ai/docs/components)构建块，这些组件可以执行文档检索、文本生成或创建嵌入等任务。单个组件已经非常强大。它可以管理本地语言模型或通过 API 与托管模型通信。

虽然 Haystack 提供了一系列开箱即用的组件，但它也允许您创建自己的自定义组件——就像编写一个 Python 类一样简单。探索由我们的合作伙伴和社区开发的自定义组件集合，您可以自由使用。

您可以将组件连接在一起以构建管道，这些管道是 Haystack 中 LLM 应用架构的基础。

## 管道（Pipelines）

[管道](https://docs.haystack.deepset.ai/docs/pipelines)是强大的抽象，允许您定义数据在 LLM 应用中的流动。它们由组件组成。

作为开发者，您可以完全控制如何在管道中排列组件。管道可以分支、合并，也可以循环回到另一个组件。您可以组合 Haystack 管道，使其能够重试、循环，甚至可能作为服务持续运行。

管道本质上是图，甚至是多重图。由于管道的灵活性，单个具有多个输出的组件可以连接到另一个具有多个输入的单个组件或多个组件。

为了帮助您入门，Haystack 提供了许多不同用例的示例管道：索引、智能聊天、RAG、抽取式问答、函数调用、网页搜索等。

## 特性 (Features)

- **技术无关性：** 用户可灵活选择所需的供应商或技术，并轻松替换任何组件。Haystack 支持使用和比较来自 OpenAI、Cohere 和 Hugging Face 的模型，以及您自己的本地模型或部署在 Azure、Bedrock 和 SageMaker 上的模型。
- **透明性：** 清晰展示不同组件之间的交互方式，便于适配您的技术栈和具体用例。
- **灵活性：** Haystack 提供一站式工具集：数据库访问、文件转换、数据清理、文本分割、模型训练、评估、推理等。需要自定义功能时，创建专属组件也非常简便。
- **可扩展性：** 为社区和第三方开发者提供统一且简洁的方式构建自己的组件，培育围绕 Haystack 的开放生态系统。

使用 Haystack 可实现的典型应用：

- 构建**检索增强生成 (RAG)** 系统，利用各种向量数据库并定制 LLM 交互，应用场景无限
- 实现**自然语言问答**，在文档中精准定位答案
- 执行**语义搜索**，基于语义而非关键词匹配检索文档
- 直接使用**预训练模型**或将其**微调**适应您的数据
- 通过**用户反馈**评估、基准测试并持续优化您的模型
- 开发能做出复杂决策的应用：如解决复杂客户查询的系统，在多个独立资源中进行知识搜索等
- 使用高效检索器和生产级组件扩展到百万级文档规模
- 在包含多种信息类型（如图像、文本、音频和表格）的知识库上进行生成式多模态问答

## 🖖 社区 (Community)

如需提出功能请求或报告错误，请随时在 [Github 上创建 issue](https://github.com/deepset-ai/haystack/issues)。我们定期检查并快速响应这些问题。若想讨论特定主题或获取关于如何将 Haystack 应用到您项目的建议，可以在 [Github Discussions](https://github.com/deepset-ai/haystack/discussions) 或我们的 [Discord 社区](https://discord.com/invite/VBpFzsgRVF)发起讨论。我们也活跃在 [𝕏 (Twitter)](https://twitter.com/haystack_ai) 和 [Stack Overflow](https://stackoverflow.com/questions/tagged/haystack)。

## 常见问题 (FAQ)

- [这个框架可以用于中文全文搜索吗？](https://github.com/deepset-ai/haystack/discussions/5471)
