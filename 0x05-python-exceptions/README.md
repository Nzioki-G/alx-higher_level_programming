# Python - Exceptions


* Programming in Python is Awesome because it's easy for beginners to learn
* Errors versus Exceptions:
    * Errors: complaints you get from compiler; either syntax errors or exceptions
    * Exceptions: complaints caused by incorrectness of the code rather than syntax
* Use exceptions when you intend to run a program to the end skipping the errors encountered
* Use exceptions thus:
    1. Handle exceptions ie. ```try```,```except``` block
    2. Raise exceptions ie. ```raise exception```
    3. Define your own eceptions
    4. Optional clean-up with ```finally``` clause
* Catching exceptions helps specify the actoin to take when at runtime erroneous code is encountered
* To raise an exception do this:
    ```
    try:
        raise SomeError
    finally:
        # something_here
    ```
* We use ```finally``` to do clean-up (like release of resources) that is necessary whether or not an exception occurred
