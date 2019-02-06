
class QueryTest(object):
    greater = None
    greaterOR = None

    between = None
    notBetween = None
    betweenOR = None

    less = None
    lessOR = None

    equal = None
    equalNot = None
    equalAny = None
    equalNone = None
    equalAnyList = None
    equalAllList = None

    contains = None
    containsNot = None
    containsOr = None
    containsAny = None
    containsAll = None
    containsNone = None

    startsWith = None
    startsWithNot = None

    endsWith = None
    fuzzy = None
    isEmpty = None
    isNotEmpty = None
    isNull = None
    isNotNull = None
    reverseContainsAll = None

    top = None
    bottom = None

    rowIndexMatchAny = None
    rowIndexMatchNone = None

    isideOrCrossing = None
    outsideOrCrossing = None
    crossing = None

    alwaysFalse = None

    dWithin = None
    notDWithin = None

    overlaps = None
    notOverlaps = None
    nearest = None

    notPrefix = None
    catchAll = None

    geoContains = None
    geoNotContains = None
    geoRegionContains = None
    geoRegionNotContains = None

    geoOverlaps = None
    geoNotOverlaps = None

    geoDWithin = None
    geoNotDWithin = None

    geoLengthEqual = None
    geoLengthGreater = None
    geoLengthLess = None

    geoAreaEqual = None
    geoAreaLess = None
    geoAreaGreater = None

    dayOfWeek = None
    hourOfDay = None
    withinLast = None

    isCurrent = None

    def __init__(self):
        self.greater = "Greater"
        self.greaterOR = "GreaterOR"

        self.between = "Between"
        self.notBetween = "NotBetween"
        self.betweenOR = "BetweenOR"

        self.less = "Less"
        self.lessOR = "LessOR"

        self.equal = "Equal"
        self.equalNot = "EqualNot"
        self.equalAny = "EqualAny"
        self.equalNone = "EqualNone"
        self.equalAnyList = "EqualAnyList"
        self.equalAllList = "EqualAllList"

        self.contains = "Contains"
        self.containsNot = "ContainsNot"
        self.containsOr = "ContainsOr"
        self.containsAny = "ContainsAny"
        self.containsAll = "ContainsAll"
        self.containsNone = "ContainsNone"

        self.startsWith = "StartsWith"
        self.startsWithNot = "StartsWithNot"

        self.endsWith = "EndsWith"
        self.fuzzy = "Fuzzy"
        self.isEmpty = "IsEmpty"
        self.isNotEmpty = "IsNotEmpty"
        self.isNull = "IsNull"
        self.isNotNull = "IsNotNull"
        self.reverseContainsAll = "ReverseContainsAll"

        self.top = "Top"
        self.bottom = "Bottom"

        self.rowIndexMatchAny = "Any"
        self.rowIndexMatchNone = "None"

        self.isideOrCrossing = "InsideOrCrossing"
        self.outsideOrCrossing = "OutsideOrCrossing"
        self.crossing = "Crossing"

        self.alwaysFalse = "AlwaysFalse"

        self.dWithin = "DWithin"
        self.notDWithin = "NotDWithin"

        self.overlaps = "Overlaps"
        self.notOverlaps = "NotOverlaps"
        self.nearest = "Nearest"

        self.notPrefix = "Not_"
        self.catchAll = "CatchAll"

        self.geoContains = "GeoContains"
        self.geoNotContains = "GeoNotContains"
        self.geoRegionContains = "GeoRegionContains"
        self.geoRegionNotContains = "GeoRegionNotContains"

        self.geoOverlaps = "GeoOverlaps"
        self.geoNotOverlaps = "GeoNotOverlaps"

        self.geoDWithin = "GeoDWithin"
        self.geoNotDWithin = "GeoNotDWithin"

        self.geoLengthEqual = "GeoLengthEqual"
        self.geoLengthGreater = "GeoLengthGreater"
        self.geoLengthLess = "GeoLengthLess"

        self.geoAreaEqual = "GeoAreaEqual"
        self.geoAreaLess = "GeoAreaLess"
        self.geoAreaGreater = "GeoAreaGreater"

        self.dayOfWeek = "DayOfWeek"
        self.hourOfDay = "HourOfDay"
        self.withinLast = "WithinLast"

        self.isCurrent = "IsCurrent"

