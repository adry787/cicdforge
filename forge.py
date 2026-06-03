#!/usr/bin/env python3
import yaml, subprocess
class Pipeline:
    def __init__(self,cfg):
        with open(cfg) as f: self.stages = yaml.safe_load(f).get("stages",[])
    def run(self):
        for s in self.stages:
            print(f"Stage: {s.get('name')}")
            for cmd in s.get("commands",[]):
                r = subprocess.run(cmd,shell=True,capture_output=True,text=True)
                if r.returncode!=0: print(f"FAIL: {r.stderr[:100]}"); return False
        print("Done!"); return True
if __name__=="__main__":
    import sys; Pipeline(sys.argv[1] if len(sys.argv)>1 else "pipeline.yaml").run()
