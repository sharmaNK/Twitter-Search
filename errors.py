"""
    This is a where all the possible exceptions to be raised by
    this library are listed
"""


class TwitterException(Exception):
    """
        To be when an exception is occured
        from twitter side.

        Mainly raised when some API call is failed
    """
    pass


class TwitterSearchException(TwitterException):
    """
        To be raised when error occured in search
    """
    pass


class TwitterAuthException(TwitterException):
    """
        To be raised when twitter auth failed
    """
    pass
