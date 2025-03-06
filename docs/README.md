## 概述、组件、管道节点和指南

Haystack 文档可在官方网站查阅：https://docs.haystack.deepset.ai/docs/get_started。我们欢迎您的贡献，请按以下步骤操作：

1. 确认您在正确的文档版本（查看左上角版本选择器）
2. 点击页面右上角的"建议编辑"链接
3. 直接在文档中进行修改并点击**提交建议的编辑**
4. 可选：添加评论说明您的更改

我们处理完您的建议后，会通过邮件通知您更改是否已被合并，如未合并会说明原因。

请务必查阅我们的[贡献指南](https://github.com/deepset-ai/haystack/blob/main/CONTRIBUTING.md)。

## 教程

教程位于独立仓库：https://github.com/deepset-ai/haystack-tutorials。如需贡献教程，请参阅[教程贡献指南](https://github.com/deepset-ai/haystack-tutorials/blob/main/Contributing.md#contributing-to-haystack-tutorials)。

## API 参考

我们使用 Pydoc-Markdown 从代码文档字符串自动生成 Markdown 文件。每次提交时，GitHub Action 会自动重新生成 API 页面。

若要为新的 Haystack 模块创建文档，请在 `docs/src/api/api` 目录中创建配置 Pydoc-Markdown 的 `.yml` 文件并提交到主分支。

所有文档字符串的更新在提交到主分支后会自动更新到文档中。

### 配置

Pydoc 从 `/haystack/docs/_src/api/pydoc` 目录下的 `.yml` 文件读取配置，主要包含三个部分：

- **loader**：加载 Python 源文件中 API 对象的插件

  - **type**：Python 源文件加载器
  - **search_path**：源文件位置
  - **modules**：用于生成文档的模块
  - **ignore_when_discovered**：需要忽略的文件

- **processor**：处理 API 对象文档字符串的插件

  - **type: filter**：模块过滤器
  - **documented_only**：仅包含已文档化的对象
  - **do_not_filter_modules**：不过滤模块对象
  - **skip_empty_modules**：跳过空模块

- **renderer**：生成输出文件的插件
  - **type**：渲染器类型（我们使用 ReadmeRenderer 确保文件在 ReadMe 中正确显示）
  - **excerpt**：页面简短描述
  - **category**：ReadMe 类别 ID
  - **title**：文档显示标题（确保末尾添加"API"）
  - **slug**：页面别名（单词间用破折号分隔）
  - **order**：页面在目录中的位置
  - markdown:
    - **descriptive_class_title**：从类标题中移除"Object"
    - **descriptive_module_title**：在模块名称前添加"Module"
    - **add_method_class_prefix**：将类名作为方法名前缀
    - **add_member_class_prefix**：将类名作为成员名前缀
    - **filename**：生成文件的文件名（单词间用下划线分隔）
