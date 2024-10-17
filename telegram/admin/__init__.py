from . import all_appeals, admin_appeals

routers = []
routers += all_appeals.routers
routers += admin_appeals.routers
