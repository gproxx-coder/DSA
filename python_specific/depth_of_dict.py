dt1 = {
    "a": "b",
    "c": {
        "d": "e"
    },
    "f": {
        "g": {
            "h": {
                1: {
                    100: False
                }
            }
        }
    },
    "i": {
        "j": {
            "final": True
        }
    },
    "x": {},
    "z": {}
}

dt2 = {
    1: 100,
    2: {
        2: 200
    },
    3: {
        2: 200,
        3: {
            3: {4: {}}
        }
    },
    4: {
        2: 400
    }
}

dt3 = {}
dt4 = {}


def get_depth(dt):
    mx = 0
    if dt:
        depth = 1
        for key, val in dt.items():
            if type(val) is dict:
                depth = get_depth(val) + 1
            if depth >= mx:
                mx = depth
        return mx
    return 0

#
# def get_depth(dt):
#     if dt:
#         depth = 1
#         final = 0
#         for key, val in dt.items():
#             if type(val) == dict:
#                 depth = get_depth(val) + 1
#             if depth >= final:
#                 final = depth
#
#         return final
#     return 1


print(get_depth(dt1))

print(get_depth(dt2))

print(get_depth({'a': 1, 'b': {'c': {'456':0}}}))

