# ComeCut - Python 插件扩展最小示例项目

这是一个用于 [ComeCut](https://github.com/juntaosun/ComeCut) 的 Python 插件扩展最小示例项目，当前示例通过 `main.py` 演示了一个最基础的插件定义方式。


## 项目说明

该示例主要展示了以下内容：

- 插件基础元信息定义，例如分类、名称、版本、作者等。
- 输入参数声明方式，例如字符串和整数类型参数。
- 插件执行入口 `run(...)` 的实现方式。
- 返回结果给 ComeCut 的最小流程。
- 插件扩展，您将能自由编程，来处理轨道音频，视频以及图像等。    

## 文件结构

```text
.
├── main.py
└── README.md
```


## 安装示例 & Installation  

```bash
cd comecut_nodes  
git clone https://github.com/juntaosun/comecut-example  

# 你需要切换到 python_env 目录中: 
python -m pip install -r comecut-example/requirements.txt  
# ( 如果您配置了依赖表 requirements.txt ，用户则可以方便的安装它 )  
```

> 备注：ComeCut 已经集成了先进的插件安装方式，您几乎无需操作任何命令行！  

## main.py 说明

`main.py` 中定义了一个 `ExamplePlugin` 类，包含以下关键部分：

# INFO 定义插件基本元数据信息  

- `CATEGORY`：插件分类。
- `NAME`：插件显示名称。
- `VERSION`：插件版本号。
- `AUTHOR`：插件作者。
- `INPUT_TYPES()`：声明插件输入参数。
- `run(...)`：插件被调用时的执行逻辑。

您可以在此基础上继续扩展自己的业务逻辑，例如处理视频、音频、字幕或其他与剪辑流程相关的功能。

## 相关链接

- ComeCut 主项目：https://github.com/juntaosun/ComeCut
