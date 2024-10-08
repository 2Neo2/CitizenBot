from control_db.models import Client


def is_admin(tg_id):
	client = Client.objects.filter(tg_id=tg_id)
	if client.exists():
		client = client.first()
		return client.status == 'admin'

	return False
