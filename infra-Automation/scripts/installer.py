import subprocess

def setup_runner(service):
    try:
        res = subprocess.run([".", "/c/users/home/serviceInstaller", service], capture_output=True, text=True)
        if res.returncode == 1:
            print(f'installing {service} failed, info: {res.stderr}')
        else:
            print(f'{service} installing: {res.stdout}')

    except Exception as e:
        print(f'failed to install: {e}')

ans = str(input("please enter the service: "))

setup_runner(ans)
        