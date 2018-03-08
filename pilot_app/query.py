import mlab
from models.service import Service

mlab.connect()

# all_services = Service.objects()
#
# first_service = all_services[0]
#
# print(first_service.name)

id_to_find = "5a956301308e841354e3d00d"

service = Service.objects().with_id(id_to_find)

print(service.to_mongo())

if service is not None:
    # service.delete()
    service.update(set__status=False)
    service.reload()
    print(service.to_mongo())
else:
    print("not found")
