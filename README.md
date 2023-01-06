# archichecture_patterns_book
### Pattern ValueObject 
It is then object is characterized by all their properties.  
For example object `Person(name='Harry', age='25')` equal only `Person(name='Harry', age='25')`.  
But `Person(name='Harry', age='26')` already not equal `Person(name='Harry', age='25')` because they have different `age` property.  

For value objects, the hash should be based on all the value attributes, and we should ensure that the objects are immutable. We get this for free by specifying `@frozen=True` decorator on the dataclass.
