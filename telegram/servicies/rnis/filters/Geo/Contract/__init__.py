from .create  import create
from .delete  import delete
from .plan    import plan
from .read    import read
from .to_list import to_list
from .unit    import unit
from .update  import update
from .export  import export
from .table   import table


class Contract:
    create  = create
    delete  = delete
    plan    = plan
    read    = read
    to_list = to_list
    unit    = unit
    update  = update
    export  = export
    table   = table