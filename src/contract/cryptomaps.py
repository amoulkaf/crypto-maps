from boa.interop.Neo.Runtime import CheckWitness, Log
from boa.interop.Neo.Storage import GetContext, Put, Delete, Get
from boa.interop.Neo.Runtime import Notify, Serialize, Deserialize
ctx = GetContext()

from boa.builtins import concat


def Main(operation, args):

    # Common definitions
    user_hash = args[0]
    country = args[1]
    city = args[2]

    # This doesn't require authentication
    if opperations == 'GetPlace':
        return Get(GetContext(), coutry + city)

    if opperations == 'registerPlace':
