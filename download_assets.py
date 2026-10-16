"""Download the versioned reproducibility assets and verify every byte."""
from pathlib import Path
import argparse, hashlib, json, tarfile, urllib.request, zipfile
BASE = "https://github.com/msalih71/idt-phm-memory-pathways/releases/download/v2026.10.16/"
ASSETS = {'paper': {'file': 'IDT_PHM_Paper_Reproduction_20261016.zip', 'sha256': '55b1da8d68d6c1280a89e097ee8dadfd46e1b1f611209095480d4ee4b0015a3f'}, 'research': {'file': 'IDT_PHM_Research_20261016.tar.xz', 'sha256': 'd0ff9adcefb3aa84bf1c3a4941d4ccaf279a4f4c0f84f020a628cc410737b86a'}}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--asset',choices=ASSETS,default='paper')
    parser.add_argument('--extract',action='store_true')
    args=parser.parse_args(); item=ASSETS[args.asset]; path=Path(item['file'])
    if not path.exists():
        with urllib.request.urlopen(BASE+path.name,timeout=120) as response, path.open('wb') as output:
            while True:
                block=response.read(1024*1024)
                if not block:break
                output.write(block)
    digest=hashlib.sha256(path.read_bytes()).hexdigest()
    if digest!=item['sha256']:
        raise RuntimeError('SHA-256 mismatch; extraction refused. Remove the damaged local download before retrying.')
    if args.extract:
        if args.asset=='research':
            with tarfile.open(path) as archive:archive.extractall(path=Path.cwd(),filter='data')
        else:
            root=Path.cwd().resolve()
            with zipfile.ZipFile(path) as archive:
                for info in archive.infolist():
                    target=(root/info.filename).resolve()
                    if root not in target.parents:raise RuntimeError('Unsafe ZIP member')
                archive.extractall(root)
    print(json.dumps({'status':'PASS','asset':path.name,'sha256':digest,'extracted':args.extract}))

if __name__=='__main__':main()
