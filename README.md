# Solana Devnet 学习记录

从 Hello World 开始，学习 Solana 程序的编写、编译、部署与调用。

## 第一个练习：Hello World

源码：[hello.py](hello.py)

这个练习使用 Seahorse 的 Python 风格语法。调用 `hello` 指令后，程序会在交易执行日志中输出 `Hello, World!`。

## 代码速读

- `from seahorse.prelude import *`：导入 Seahorse 的开发工具。
- `declare_id('')`：声明程序地址；Solana Playground 会在编译时自动填写。
- `@instruction`：把下面的函数声明为程序指令。
- `def hello(signer: Signer)`：定义 hello 指令，并要求提供签名账户。
- `print('Hello, World!')`：输出程序日志。

## 在 Solana Playground 中练习

1. 打开 [Hello Seahorse 教程](https://beta.solpg.io/tutorials/hello-seahorse/1)。
2. 将本仓库 `hello.py` 的内容复制到教程的源码编辑器中。
3. 点击 **Build** 编译，或在 Playground 终端输入 `build`。
4. 连接专门用于练习的 Playground 钱包，并确认网络为 **Devnet**。
5. 准备足够的 Devnet 测试 SOL 后，点击 **Deploy** 部署。
6. 按教程调用 `hello` 指令，并在交易日志中检查输出。

## 理解三个步骤

| 步骤 | 作用 | 是否需要测试 SOL |
| --- | --- | --- |
| Build | 检查代码并编译程序 | 不需要 |
| Deploy | 将程序部署到 Devnet | 需要 |
| 调用 hello | 发送交易执行程序指令 | 需要 |

本例供 Seahorse / Solana Playground 环境使用。程序地址由 Playground 管理。

## 后续练习

- 把输出文字改成自己的问候语，再次编译。
- 完成一次 Devnet 部署。
- 调用程序，找到日志中的问候语。
- 学习读取账户和查询余额。

## 钱包文件

本仓库仅保存练习源码和笔记。钱包 keypair JSON、私钥、助记词和真实 API 密钥应保存在仓库之外。

参考：[Solana Quick Start](https://solana.com/docs/intro/quick-start)
