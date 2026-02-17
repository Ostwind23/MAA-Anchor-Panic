# MAA-Anchor-Panic

基于 [MaaFramework](https://github.com/MaaXYZ/MaaFramework) 开发的自动化项目。

## 项目结构

```text
MAA-Anchor-Panic/
├── agent/              # Python Agent（Custom Action / Recognition）
│   ├── main.py         # Agent 入口
│   ├── agent_register.py  # 注册中心
│   ├── requirements.txt
│   └── custom/         # 自定义动作和识别
│       ├── action/     # Custom Action 实现
│       └── reco/       # Custom Recognition 实现
├── assets/             # 资源文件
│   ├── interface.json  # 项目接口配置
│   └── resource/       # 识别资源
│       ├── image/      # 模板图片
│       ├── model/      # 模型文件
│       └── pipeline/   # 任务流水线
├── config/             # 运行时配置
├── deps/               # MaaFramework 依赖
├── scrcpy/             # ADB 工具
└── tools/              # 构建与部署工具
```

## 快速开始

1. 确保已安装 Python 环境（推荐 conda）
2. 安装依赖：`pip install -r agent/requirements.txt`
3. 运行 `deps/bin/MaaPiCli.exe`

## 添加新的 Custom Action

1. 在 `agent/custom/action/` 下创建新的 `.py` 文件
2. 在 `agent/custom/action/__init__.py` 中导入新类
3. 在 `agent/agent_register.py` 中注册
4. 在 `assets/resource/pipeline/` 中创建对应的流水线 JSON

## License

MIT
