# pyqt的安装步骤

1. 先在官网下载3.7.6 的版本， 有的版本太高找不到文件designer.exe 的文件。 假如已经装了高版本的文件 ，也是去官网下对应版本，里面有一个Uninstall 点了 等待卸载

2. 安装版本的时候选第一个 Install Now  把可以选择的 Add Python 3.7.6 to PATH 打勾  这样安装环境就自动配好了 ，不用后期去配环境

3. 等它装好了 这时候就可以 查看python的路径 win加r  cmd 打开命令窗口输入`python`进入， 用命令 `where python` 查看地址 复制粘贴到文档

4. 使用PyQt开发，要先下载相关的第三方库的工具  创建一个文件 三条命令复制粘贴 重命名为ins.bat 然后双击运行 等待下载完成

   [pip install PyQt5 -ipip install PyQt5 -i](https://mirrors.aliyun.com/pypi/simple/)

   [pip install pyqt5-tools -i](https://mirrors.aliyun.com/pypi/simple/)

   [pip install pyinstaller -i](https://mirrors.aliyun.com/pypi/simple/)

5. 在安装完成后，在Python解释器中输入： import PyQt5  如果没有报错即为安装成功 假如报错了，就再执行一遍命令.

6. 在Python解释器中输入 pip install pyqt5-tools 查看是否安装成功

7. 打开之前python的路径文档 ，复制粘贴到此电脑的搜索， 退到这个路径 

   []: C:\Users\19601\AppData\Local  找项目包 Programs\Python\Python37-32\Lib\site-packages\qt5_applications\Qt\bin

8. 然后就是配置编译器的问题  创建一个新项目  选择Python的解释器 3.7 .  之前选择的是虚拟环境去编译。 完成之后 代码放进去就不会报错了。