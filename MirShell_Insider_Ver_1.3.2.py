# import
import os # 执行系统命令
from sys import hash_info  
import time  # 等待 x 秒，获取当前时间
import platform # 检测设备信息
import getpass # 获取用户名

# Menu
print('MirShell 1.3.2')
print('此程序遵守 GNU 协议，由 MO_ran, SteveUbuntu 制作')
# System,python Version Check
def main():
    print('输入 "help" 即可查看命令帮助')
    if os.getcwd() == '/data/data/com.termux/files/home':
        workdir = ''
        homedir = '/data/data/com.termux/files/home'
        releases = ' Android '
    elif os.getcwd() == '/home/'+getpass.getuser():
        workdir = ''
        homedir = '/home/'+getpass.getuser()
        releases = ' Linux '
    elif os.getcwd() == '/root':
        workdir = ''
        homedir = '/root'
        releases = ' Linux '
    else:
        workdir = os.getcwd()
        homedir = 'errortype'
        releases = ' ? '
    while True:
        print('╭─('+releases+')')
        print('├─('+time.ctime()[11:19]+')')
        shinput = input('╰─('+getpass.getuser()+'@'+platform.node()+' # ')
        if shinput == 'help':
            print('当前可执行的命令有')
            print('ref        刷新 release 缓存')
            print('time       获取当前时间')
            print('ls         显示一个目录中的文件和子目录')
            print('la         显示隐藏文件')
            print('du         目录占用空间')
            print('cd         更改工作目录')
            print('vim        打开 vim 文本编辑器')
            print('nano       打开 nano 文本编辑器')
            print('micro      打开 micro 开发文本编辑器')
            print('panel      打开 管理面板')
            print('exit       退出 MirShell 程序')
            print('python     启动 Python')
            print('tmoe       启动 Tmoe Linux Manager')
            print('mkdir      创建一个目录')
            print('clear      清除屏幕')
            print('ulog       更新日志')
            print('fortune    一言')
            print('plusto     插件下载')
        elif shinput == 'ref':
            if os.getcwd() == '/data/data/com.termux/files/home':
                releases = ' Android '
                print('刷新完成')
            elif os.getcwd() == '/home/'+getpass.getuser():
                releases = ' Linux '
                print('刷新完成')
            elif os.getcwd() == '/root':
                releases = ' Linux '
                print('刷新完成')
            else:
                releases = ' ? '
                print('失败，请在用户目录重试。')
        elif shinput == 'cd':
            try:
                print('输入要更改的目录路径')
                print('..  上级目录')
                print('/   根目录')
                shinput = input('Change Dir>')
                os.chdir(shinput)
            except FileNotFoundError:
                print('无法找到该目录，请重试')    
        elif shinput == 'ls':
            print('当前在 '+os.getcwd())
            os.system('ls')
        elif shinput == 'la':
            print('当前在 '+os.getcwd())
            os.system('ls -a')
        elif shinput == 'du':
            print('当前在 '+os.getcwd())
            os.system("du -d1 -h")
        elif shinput == 'exit':
            exit()
        elif shinput == 'panel':
            print('当前可执行的命令')
            print('neofetch   打开 neofetch 系统属性查看程序')
            print('ver        查看版本，帮助信息')
            print('reu        更新/修复 MirShell 所需要的所有组件')
            print('ps         显示当前进程')
            print('htop       启动任务管理器')
            shinput = input('Panel>')     
            if shinput == 'neofetch':
                print('-'*56)
                print('Neofetch 系统属性查看器')
                print('-'*56)
                os.system('neofetch')
            elif shinput == 'ver':
                print('-'*56)
                print('MirShell , running on '+releases)
                print('Insider 1.3.2')
                print('-'*56)
                print('系统: ',platform.system())
                print('内核版本: ',platform.release())
                print('系统详细版本: ',platform.version())
                print('-'*56)
                print('您的 Python 版本: Python',platform.python_version())
                print('-'*56)
                print('处理器: ',platform.processor())
                print('处理器架构: ',platform.machine())
                print('-'*56)
                print('此设备名称: ',platform.node())
                print('-'*56)
            elif shinput == 'reu':
                print('-'*56)
                print('reu MirShell Repair 核心修复/更新程序')
                print('-'*56)
                print('正在准备自动更新/修复，您现在还有 3 秒的时间可以 Ctrl+C 退出...')
                time.sleep(3)
                os.system('clear')
                print('更新/修复程序已经启动，请勿退出!!!')
                print('正在更新/修复基础组件包...')
                os.system('apt install -y apt bash neofetch vim nano micro')
                print('正在更新/修复 git 组件包...')
                os.system('apt install git')
                print('正在修复 Python 3 必要组件')
                os.system('apt install -y python3 python-is-python3 python3-pip')
                print('更新/修复已经完成，正在更新系统所有软件包，请勿退出!')
                os.system('apt update ; apt upgrade ; apt dist-upgrade')
                print('正在清除缓存...')
                os.system('apt clean ; apt autoclean ; apt autoclean apt')
                print('所有组件修复完成!')
            elif shinput == 'ps':
                os.system('ps')
            elif shinput == 'htop':
                os.system('htop')
            else:
                print("'"+shinput+"'"+' 不是在本 Shell 可运行的命令，请重新检查您的拼写后再试')
        elif shinput == 'python':
            print('-'*56)
            print('Python 命令行交互语言')
            print('-'*56)
            os.system('python3')
        elif shinput == 'tmoe':
            print('-'*56)
            print('Tmoe-Linux Manager 系统实用工具管理器')
            print('-'*56)
            os.system('apt install -y curl ; bash -c "$(curl -L gitee.com/mo2/linux/raw/2/2)" ')
        elif shinput == 'vim':
            print('-'*56)
            print('vim Vi improved 文本编辑器')
            print('-'*56)
            print('请输入要打开的文件')
            shinput = input('Vim>')
            sinput = 'vim '+shinput
            os.system(sinput)
        elif shinput == 'nano':
            print('-'*56)
            print('nano 文本编辑器')
            print('-'*56)
            print('请输入要打开的文件')
            shinput = input('nano>')
            sinput = 'nano '+shinput
            os.system(sinput)
        elif shinput == 'micro':
            print('-'*56)
            print('micro 终端开发文本编辑器')
            print('-'*56)
            print('请输入要打开的文件')
            shinput = input('Micro>')
            sinput = 'Micro '+shinput
            os.system(sinput)
        elif shinput == 'clear':
            os.system('clear')
        elif not shinput:
            pass
        elif shinput == 'ulog':
            print('-'*56)
            print('ulog 更新日志')
            print('-'*56)
            print('-'*56)
            print('1.0')
            print('+ 发布')
            print('-'*56)
            print('1.1')
            print('+ 优化')
            print('+ 增加 apt 软件包管理器')
            print('+ 加入了 Insider MirShell')
            print('+ 增加了 panel 命令')
            print('-'*56)
            print('1.2')
            print('+ 移除了检测 Python 最新版本，只留下了检测 本地 Python 版本')
            print('+ 增加 fortune')
            print('+ 增加了 ulog')
            print('+ 增加了 eula')
            print('+ 优化文字和体验')
            print('+ 增加 pkg 软件包管理器')
            print('+ 重新加入 rep 修复 Tmoe-Linux Manager')
            print('+ 移除了待开发的 更新 功能')
            print('+ 基础功能增加 fortune')
            print('+ 简单优化非 TermuxOS Linux 系统跑 MirShell 体验 (不支持 Windows)')
            print('-'*56)
            print('1.3')
            print('+ 更改 Shell 样式')
            print('+ 增加了 Shell 显示用户名')
            print('+ 增加了 Shell 显示工作目录')
            print('= 优化操作体验')
            print('+ 更换名称为 MirShell')
            print('+ 修复了 cd 无法找到文件夹而抛出错误的问题')
            print('+ Public 版本并不会显示 Insider 什么版本更新了什么，只会总和 Insider 版本更新内容')
            print('-'*56)
            print('1.4')
            print('- 去除了 Shell 显示工作目录')
            print('+ 修复了不在用户目录启动使用 cd 回到用户目录报错的问题')
            print('+ 尝试采用 Unicode 字符')
            print('+ 所有版本并不会显示 Insider 什么版本更新了什么，只会总和 Insider 版本更新内容')
            print('+ 修复一些问题')
            print('+ 增加应用商城') 
        elif shinput == 'fortune':
            print('-'*56)
            print('fortune 一言')
            print('-'*56)
            for i in range(3):
                os.system('fortune')
        elif shinput == 'plusto':
            print('-'*20)
            print('hello_world')
            print('作者: MOranExplore')
            print('版本: latest')
            print('描述: 测试插件商城功能')
            print('-'*20)
            print('mirsh')
            print('作者: SteveUbuntu')
            print('版本: latest')
            print('描述: 一个对用户友好的 Shell，使用 Python 编写。')
            print('-'*20)
            shinput = input('插件>')
            if shinput == 'hello_world':
                    os.system('rm -rf hello_world.mplg')
                    print('正在加载 Hello World')
                    os.system('wget -q --show-progress https://download.fastgit.org/SteveUbuntu0/MirPlugins/releases/download/latest/hello_world.mplg')
                    os.system('chmod 777 hello_world.mplg')
                    print('-'*20)
                    os.system('python3 hello_world.mplg')
                    print('-'*20)
            elif shinput == 'mirsh':
                    os.system('rm -rf mirsh.mplg')
                    print('正在加载 MirShell')
                    os.system('wget -q --show-progress https://download.fastgit.org/SteveUbuntu0/MirPlugins/releases/download/latest/mirsh.mplg')
                    os.system('chmod 777 mirsh.mplg')
                    os.system('mv mirsh.mplg mirshell')
                    print('-'*20)
                    os.system('./mirshell')
                    print('-'*20)
            else:
                print('input error.')
        else:
            os.system(shinput)
if platform.system() == 'Linux':
    main()
elif platform.system() == 'Windows':
    print('MirShell 不支持 Windows')
    time.sleep(3)
    exit()
else:
    print('您的系统为非 Linux，如果继续可能会有严重错误，确定继续？')
    sinput = input('(y/N) ')
    if sinput == 'y':
        main()
    else:
        exit()
