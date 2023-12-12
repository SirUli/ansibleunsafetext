from ansible.plugins.action import ActionBase
from pathlib import Path

class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        result = super(ActionModule, self).run(tmp, task_vars)
        path = self._task.args.get('path')
        # Of course this is not perfect but it shows the problem
        print(type(path))
        path_obj = Path(path)
        result['path_object'] = str(path_obj)
        return result
