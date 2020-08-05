## vim-calc: 一个在 Vim 中的计算器

[English Ver.](./README.md)

#### 介绍
`vim-calc` 是一款在 `Vim` 下使用的计算器

![Demo](demo.gif)


#### 使用
在 Vim 中执行 **`:call Calc()`** 来计算在当前行下的数学公式 (`vim-calc` 会将错误信息打印在状态栏下方)

或者, 如果你想绑定快捷键来计算数学公式的话, 将以下行加入到你的 `vimrc`/`init.vim`:
```vim
nnoremap <LEADER>a :call Calc()<CR>
```

现在, 你可以按下 `LEADER` 键和 `a` 键来计算

#### 安装
用 [vim-plug](https://github.com/junegunn/vim-plug) 安装 `vim-calc`:
```vim
Plug 'theniceboy/vim-calc'
```

#### Todos
The part is temp part so i don't will translate it.

- [ ] Convert equation to `latex` form

#### 贡献
此插件正处于 **开发阶段**, 所以, 如果你发现了 BUG, 请不要犹豫地[创建 Issues](https://github.com/theniceboy/vim-calc/issues/new), 提交一个拉取请求, 或者给我发邮件!

#### 协议
MIT
