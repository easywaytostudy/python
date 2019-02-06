

if __name__ == '__main__':
    from QueryBuilder import QueryBuilder
    from QueryTest import QueryTest

    queryTest = QueryTest()

    select = ["*"]
    query = QueryBuilder()
    query.Select(select)
    query.Where("StarRating", queryTest.greater, "4")
    query.Or()
    query.Where("Name", queryTest.endsWith, "Hotel")
    query.Having("CountryName", queryTest.equal, "France")
    query.From("hms/hotels")
    query.Take(100)
    query.Start(0)

    data = query.query
    print(data)

# Output:
    # {"sqlselect":["*"],"table":"hms/hotels","where":[[{"col":"StarRating","test":"Greater","value":"4"}],[],[{"col":"Name","test":"EndsWith","value":"Hotel"}]],"having":[{"col":"CountryName","test":"Equal","value":"France"}],"start":0,"take":10,"withgeo":false,"projection":"EPSG_3857"}
