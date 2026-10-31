"""Restore a versioned data snapshot without overwriting ongoing Cloud work."""
import argparse,hashlib,json,shutil,tempfile,zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parent
def main():
    p=argparse.ArgumentParser();p.add_argument('--parts',type=Path,default=ROOT/'cloud_payload');a=p.parse_args();manifest=json.loads((a.parts/'parts_manifest.json').read_text())
    with tempfile.TemporaryDirectory(prefix='biology37_restore_') as td:
        archive=Path(td)/'snapshot.zip'
        with archive.open('wb') as out:
            for entry in manifest['parts']:
                src=a.parts/entry['file'];assert src.stat().st_size==entry['bytes'],str(src)
                with src.open('rb') as f:assert hashlib.file_digest(f,'sha256').hexdigest()==entry['sha256'],str(src)
                with src.open('rb') as f:shutil.copyfileobj(f,out)
        with archive.open('rb') as f:assert hashlib.file_digest(f,'sha256').hexdigest()==manifest['archive_sha256']
        created=0;preserved=0
        with zipfile.ZipFile(archive) as z:
            for item in z.infolist():
                dest=(ROOT/item.filename).resolve();assert dest.is_relative_to(ROOT),item.filename
                if item.is_dir():dest.mkdir(parents=True,exist_ok=True);continue
                if dest.exists():preserved+=1;continue
                dest.parent.mkdir(parents=True,exist_ok=True)
                with z.open(item) as src,dest.open('wb') as out:shutil.copyfileobj(src,out)
                created+=1
    print(json.dumps({'restored_files':created,'existing_work_preserved':preserved,'next':['python scripts/cloud_data.py verify','python scripts/cloud_data.py summary']},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
