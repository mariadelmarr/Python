class MyList(list):
    def __str__(self):
        items = ''
        for item in self:
            items += '-->' + str(item) + '...\n'
        return items

    def courses()