from invenio_records_resources.proxies import current_service_registry
from oarepo_published_service.services.service import PublishedService


class LterPublishedService(PublishedService):
    """"""

    @property
    def files(self):
        return current_service_registry.get("published_lter_file")
