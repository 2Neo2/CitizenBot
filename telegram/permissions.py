from control_db.models import Client
from general_settings.models import GeneralSettings


def is_admin(tg_id):
	settings = GeneralSettings.objects.first()
	client = Client.objects.filter(tg_id=tg_id).first()
	
	if not client:
		return False
	
	if str(client.tg_id) in [settings.consultant_id_first, settings.consultant_id_second]:
		return True
	return False
