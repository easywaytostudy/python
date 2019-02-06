from Condition import Condition


class QueryBuilder(object):
    query = {}

    def Select(self, select):
        self.query['sqlselect']=select

    def Where(self, column=None, test=None, value=None):
        response = Condition(column, test, value)
        self.query['where'] = response.where

    def Or(self):
        self.query['where'] = self.Where()

    def Having(self, column=None, test=None, value=None):
        response = Condition(column, test, value)
        self.query['having'] = response.where

    def Take(self, take):
        self.query['take']=take

    def Start(self, start):
        self.query['start']=start

    def From(self, tableName):
        self.query['table']=tableName

    def GroupBy(self, value):
        pass

    def OrderBy(self, column, orderBy):
        pass

    def SelectGeoType(self):
        pass

    def UnionAll(self):
        pass

    def join(self, **kwargs):
        print(kwargs)
        pass

    def ToOrderByArgument(self, column, orderBy):
        pass

    def ProjectionType(self, p):
        pass

    def WithGeo(self, withGeo):
        pass

    def WithStats(self, withStats):
        pass
