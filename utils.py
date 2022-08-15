from models import Driver as DriverDB


class DriverFilterQueryBuilder:
    field_name_mapping = {
        "start_date": (DriverDB.updated_at, "gte"),
        "end_date": (DriverDB.updated_at, "lte"),
        "min_score": (DriverDB.driving_score, "gte"),
        "max_score": (DriverDB.driving_score, "lte"),
    }

    def __init__(
        self,
        start_date=None,
        end_date=None,
        min_score=None,
        max_score=None,
        limit=None,
        offset=None,
    ):
        self.queries = []
        self.start_date = start_date
        self.end_date = end_date
        self.min_score = min_score
        self.max_score = max_score

        self.limit = limit
        self.offset = offset

        self.generate_query()

    def generate_query(self):
        for field_name in self.field_name_mapping.keys():
            value = getattr(self, field_name, None)
            if value:
                self.generate_query_for_field(field_name, value)

    def generate_query_for_field(self, field_name, value):
        operator = self.field_name_mapping[field_name][1]
        func = getattr(self, f"generate_{operator}_query", None)
        func(self.field_name_mapping[field_name][0], value)

    def generate_gte_query(self, field_name, value):
        self.queries.append(field_name >= value)

    def generate_lte_query(self, field_name, value):
        self.queries.append(field_name <= value)
