import subprocess
import sys



def install(pname):
  package_name = pname
  try:
      # pip install を実行
      subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
      print(f"{package_name} のインストールが完了しました")
  except subprocess.CalledProcessError:
      print(f"{package_name} のインストールに失敗しました")

install("python-dateutil")
install("art")