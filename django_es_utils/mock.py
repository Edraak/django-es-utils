import uuid


class Transport:
    def perform_request(self, *args, **kwargs):
        pass


class FakeElasticsearch:
    """
    In-memory mock of Elasticsearch for development/migrations/tests.
    Does NOT make real HTTP requests.
    """

    def __init__(self, *args, **kwargs):
        self.__documents_dict = {}
        self.transport = Transport()

    def index(self, index, doc_type=None, body=None, id=None, params=None):
        if index not in self.__documents_dict:
            self.__documents_dict[index] = []

        if id is None:
            id = str(uuid.uuid4())

        version = 1

        document = {
            '_type': doc_type,
            '_id': id,
            '_source': body,
            '_index': index,
            '_version': version,
        }

        #self.__documents_dict[index].append(document)

        return {
            '_type': doc_type,
            '_id': id,
            'created': True,
            'result': 'created',
            '_version': version,
            '_index': index
        }

    def get_indexed_documents(self, index):
        return self.__documents_dict.get(index, [])

    def reset(self):
        self.__documents_dict = {}
