# from smart_door import smart_door

# smart_door.open()
# smart_door.close()

from smart_door import smart_door as SCREAMING_SNAKE_CASE   # importing with an alias to escape shadowing (rare)

SCREAMING_SNAKE_CASE.open()
SCREAMING_SNAKE_CASE.close()

# from smart_door import * 

# smart_door.open()
# smart_door.close()

# Using 'import all' is considered a Very Bad Idea, as we don't know what is getting imported or what will be shadowed in the process

# "Explicit is better than implicit"
