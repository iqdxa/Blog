import subprocess
import tfc_toolbox_py as tfc

def build():
    # 构建
    subprocess.run(['mkdocs', 'build'], stdout=subprocess.PIPE, text=True)
    

def serve():
    # 启动服务
    subprocess.run(['mkdocs', 'serve'], stdout=subprocess.PIPE, text=True)

def deploy():
    # 部署
    subprocess.run(['mkdocs', 'gh-deploy --force'], stdout=subprocess.PIPE, text=True)

menu_list = ["构建", "服务", "部署"]

while True:
    num = tfc.console.menu(menu_list)

    match num:
        case 1: build()
        case 2: 
            try:
                serve()
            except KeyboardInterrupt:
                print("Serve已关闭")
        case 3: deploy()
        case 0: break