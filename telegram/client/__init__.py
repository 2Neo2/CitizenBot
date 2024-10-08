from . import start, strelka_logic, reference_info_logic, schedule_routes_logic, troika_logic, bank_card_logic

routers = [start.router]

routers += schedule_routes_logic.routers
routers += strelka_logic.routers
routers += reference_info_logic.routers
routers += troika_logic.routers
routers += bank_card_logic.routers
