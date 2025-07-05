import subprocess
import tfc_toolbox_py as tfc

def build():
    # 构建
    subprocess.run(['mkdocs', 'build'], capture_output=True, text=True)

def serve():
    # 启动服务
    subprocess.run(['mkdocs', 'serve'], stdout=subprocess.PIPE, text=True)

def deploy():
    # 部署
    subprocess.run(['mkdocs', 'gh-deploy --force'], capture_output=True, text=True)

menu_list = ["构建", "服务", "部署"]
serve()