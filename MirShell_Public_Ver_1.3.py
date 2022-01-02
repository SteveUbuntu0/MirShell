'''
Sign
Pressure Test , MirShell 
Powered by SteveUbuntu,MO_ran
'''

# import
import os # 执行系统命令
from sys import hash_info  
import time  # 等待 x 秒，获取当前时间
import platform # 检测设备信息
import getpass # 获取用户名

# Menu
print('MirShell 1.3')
print('此程序遵守 GNU 协议，由 MO_ran, SteveUbuntu 制作')
input('按回车继续')
# System,python Version Check
print('-'*56)
print('您的 Python 版本: Python',platform.python_version())
print('-'*56)
def main():
    print('输入 "help" 即可查看命令帮助')
    while True:
        if os.getcwd() == '/data/data/com.termux/files/home':
            workdir = '~'
        elif os.getcwd() == '/home/'+getpass.getuser():
            workdir = '~'
        else:
            workdir = os.getcwd()
        shinput = input(getpass.getuser()+'@'+platform.node()+' '+workdir+' # ')
        if shinput == 'help':
            print('当前可执行的命令有')
            print('time       获取当前时间')
            print('ls         显示一个目录中的文件和子目录')
            print('cd         更改工作目录')
            print('apt        对软件包进行管理')
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
        elif shinput == 'cd':
            try:
                print('输入要更改的目录路径，如 cd .. 或者 cd /')
                shinput = input('Change Dir>')
                os.chdir(shinput)
            except FileNotFoundError:
                print('无法找到该目录，请重试')
        elif shinput == 'time':
            print('-'*56)
            print('time 当前时间检查程序')
            print('-'*56)
             
            print(time.ctime())
        elif shinput == 'ls':
            print('当前在 '+os.getcwd())
            os.system('ls')
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
                print('MirShell')
                print('Public 1.3')
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
                print('更新/修复程序已经启动，请勿退出！！！')
                time.sleep(3)
                os.system('clear')
                print('正在更新/修复基础组件包...')
                time.sleep(3)
                os.system('apt install -y apt bash neofetch vim nano micro curl wget cowsay eatmydata')
                os.system('clear')
                print('正在更新/修复 git 组件包...')
                time.sleep(3)
                os.system('apt install git')
                print('正在更新/修复 Python 3 必要组件')
                time.sleep(3)
                os.system('apt install -y python3 python-is-python3 python3-pip')
                os.system('clear')
                time.sleep(3)
                os.system('clear')
                print('更新/修复已经完成，正在更新系统所有软件包，请勿退出！')
                os.system('apt update ; apt upgrade ; apt dist-upgrade')
                time.sleep(3)
                os.system('clear')
                print('正在清除缓存...')
                os.system('apt clean ; apt autoremove --purge ; apt autoclean ; apt autoclean apt')
                print('所有组件修复完成！')
                os.system('clear')
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
            print('Vi improve 文本编辑器')
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
            print('Public 1.0')
            print('+ 发布')
            print('-'*56)
            print('Public 1.1')
            print('+ 优化')
            print('+ 增加 apt 软件包管理器')
            print('+ 加入了 Insider MirShell')
            print('+ 增加了 panel 命令')
            print('-'*56)
            print('Public 1.2')
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
            print('Public 1.3')
            print('+ 更改 Shell 样式')
            print('+ 增加了 Shell 显示用户名')
            print('+ 增加了 Shell 显示工作目录')
            print('= 优化操作体验')
            print('+ 更换名称为 MirShell')
            print('+ 修复了 cd 无法找到文件夹而抛出错误的问题')
            print('+ Public 版本并不会显示 Insider 什么版本更新了什么，只会总和 Insider 版本更新内容')
        elif shinput == 'fortune':
            print('-'*56)
            print('fortune 一言')
            print('-'*56)
             
            for i in range(3):
                os.system('fortune')
        else:
            os.system(shinput)
if platform.system() == 'Linux':
    os.system('clear')
    main()
elif platform.system() == 'Windows':
    os.system('cls')
    print('MirShell 不支持 Windows')
    time.sleep(3)
    exit()
else:
    os.system('clear')
    print('您的系统为非 Linux，如果继续可能会有严重错误，确定继续？')
    sinput = input('(y/N) ')
    if sinput == 'y':
        main()
    else:
        exit()
